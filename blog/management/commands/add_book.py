"""
Add a BookReview from an Amazon URL or ISBN.
Auto-fetches title, author, description, and cover.

Usage:
  python manage.py add_book https://www.amazon.com/dp/0593543475/
  python manage.py add_book 9780593543474 --publish
  python manage.py add_book 0593543475 --category=biology --status=wishlist
  python manage.py add_book <url> --title="Custom" --author="Manual" --publish
"""

import json
import re
import urllib.request

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from blog.models import BookReview, Category


USER_AGENT = "Mozilla/5.0 Cogitra/1.0"


class Command(BaseCommand):
    help = "Add a BookReview from an Amazon URL or ISBN. Fetches metadata + cover."

    def add_arguments(self, parser):
        parser.add_argument(
            "url_or_isbn",
            help="Amazon product URL (containing /dp/ASIN/) or a bare ISBN-10/ISBN-13",
        )
        parser.add_argument(
            "--category",
            default="health",
            help="Category slug to assign (default: health). Must already exist.",
        )
        parser.add_argument(
            "--status",
            default="read",
            choices=["read", "reading", "wishlist"],
            help="Reading status (default: read)",
        )
        parser.add_argument("--rating", type=int, default=5, help="1-5 rating (default: 5)")
        parser.add_argument(
            "--publish",
            action="store_true",
            help="Set published=True (default keeps draft so you can edit first)",
        )
        parser.add_argument("--title", help="Override fetched title")
        parser.add_argument("--author", help="Override fetched author")
        parser.add_argument("--summary", help="Override fetched summary (max 300 chars)")
        parser.add_argument(
            "--no-cover",
            action="store_true",
            help="Skip cover image fetch",
        )

    def handle(self, *args, **opts):
        url = opts["url_or_isbn"].strip()
        identifier = self._extract_identifier(url)
        if not identifier:
            raise CommandError(
                f"Couldn't extract ISBN/ASIN from input. Expected an Amazon URL with /dp/XXXXXXXXXX/ or a bare ISBN. Got: {url}"
            )
        self.stdout.write(f"Identifier: {identifier}")

        # Try Google Books, then OpenLibrary, for metadata
        meta = self._fetch_google_books(identifier) or self._fetch_openlibrary(identifier) or {}
        title = opts.get("title") or meta.get("title")
        author = opts.get("author") or meta.get("author")
        description = meta.get("description", "")

        if not title or not author:
            raise CommandError(
                f"Couldn't fetch title/author from Google Books for {identifier}. "
                f"Pass --title and --author manually."
            )

        # SlugField default max_length is 50; truncate at a word boundary if possible
        slug = slugify(title)[:50].rstrip("-")
        self.stdout.write(f"Title:  {title}")
        self.stdout.write(f"Author: {author}")
        self.stdout.write(f"Slug:   {slug}")

        # Resolve category
        try:
            cat = Category.objects.get(slug=opts["category"])
        except Category.DoesNotExist:
            available = list(Category.objects.values_list("slug", flat=True))
            raise CommandError(
                f"Category '{opts['category']}' not found. Available: {available}"
            )

        # Build summary
        summary = opts.get("summary") or self._make_summary(description, title, author)

        # Create or update
        book, created = BookReview.objects.get_or_create(
            slug=slug,
            defaults={
                "title": title,
                "author": author,
                "category": cat,
                "summary": summary,
                "review_content": (
                    f"<p>{description}</p>" if description else "<p>Review pending.</p>"
                ),
                "rating": opts["rating"],
                "status": opts["status"],
                "buy_link": url if url.startswith("http") else "",
                "recommended": True,
                "published": opts["publish"],
            },
        )
        action = "Created" if created else "Found existing"
        self.stdout.write(self.style.SUCCESS(f"{action}: {book.title}"))

        # Fetch cover
        if opts["no_cover"]:
            self.stdout.write("Skipping cover (--no-cover)")
        elif not book.cover_image:
            cover, src = self._fetch_cover(identifier, meta)
            if cover:
                book.cover_image.save(f"{slug}.jpg", ContentFile(cover), save=True)
                self.stdout.write(
                    self.style.SUCCESS(f"Cover uploaded ({len(cover)}B from {src})")
                )
            else:
                self.stdout.write(self.style.WARNING("No cover found — upload via admin"))
        else:
            self.stdout.write("Cover already set, skipping")

        self.stdout.write(f"\nLive at: https://cogitra.com/books/{slug}/")
        if not opts["publish"]:
            self.stdout.write(
                self.style.WARNING(
                    "(Not published — edit in admin then check 'Published' box, "
                    "or pass --publish to skip review.)"
                )
            )

    # ─── helpers ────────────────────────────────────────────────────────

    @staticmethod
    def _extract_identifier(url):
        """Extract ASIN/ISBN from Amazon URL or accept a bare ISBN."""
        # Amazon: /dp/XXXXXXXXXX/ or /gp/product/XXXXXXXXXX/
        m = re.search(r"/(?:dp|gp/product)/([A-Z0-9]{10})", url)
        if m:
            return m.group(1)
        # Bare ISBN-10, ISBN-13, or ASIN
        s = url.strip().replace("-", "")
        if re.fullmatch(r"\d{10}|\d{13}|97[89]\d{10}|[A-Z0-9]{10}", s):
            return s
        return None

    @staticmethod
    def _fetch_google_books(identifier):
        api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{identifier}"
        try:
            req = urllib.request.Request(api, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read())
        except Exception as e:
            print(f"Google Books fetch failed: {e}")
            return None
        items = data.get("items", [])
        if not items:
            return None
        info = items[0]["volumeInfo"]
        title = info.get("title", "")
        if info.get("subtitle"):
            title = f"{title}: {info['subtitle']}"
        return {
            "title": title,
            "author": ", ".join(info.get("authors", [])),
            "description": info.get("description", "") or "",
            "image_links": info.get("imageLinks", {}),
        }

    @staticmethod
    def _fetch_openlibrary(identifier):
        """Fallback metadata source — no rate limit, but descriptions are often missing."""
        api = f"https://openlibrary.org/api/books?bibkeys=ISBN:{identifier}&format=json&jscmd=data"
        try:
            req = urllib.request.Request(api, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read())
        except Exception as e:
            print(f"OpenLibrary fetch failed: {e}")
            return None
        key = f"ISBN:{identifier}"
        if key not in data:
            return None
        info = data[key]
        title = info.get("title", "")
        if info.get("subtitle"):
            title = f"{title}: {info['subtitle']}"
        # OpenLibrary returns titles in sentence case; convert to title case if all-lower
        if title and title == title.lower():
            title = title.title()
        # Dedupe authors (OpenLibrary often returns the same person twice)
        seen = []
        for a in info.get("authors", []):
            name = a.get("name", "").strip()
            if name and name not in seen:
                seen.append(name)
        return {
            "title": title,
            "author": ", ".join(seen),
            "description": info.get("description", "") if isinstance(info.get("description"), str)
                          else info.get("description", {}).get("value", ""),
            "image_links": {},
        }

    @staticmethod
    def _make_summary(description, title, author):
        if description:
            # Google Books descriptions often start with the title — trim to fit 300 chars
            return description[:297].rsplit(" ", 1)[0] + "…" if len(description) > 300 else description
        return f"{title} by {author}"

    @staticmethod
    def _fetch_cover(identifier, meta):
        """Try OpenLibrary, then Google Books, then Amazon CDN. Returns (bytes, source) or (None, None)."""
        candidates = []
        # OpenLibrary first (best quality for ISBN-based lookups)
        if re.fullmatch(r"\d{10}|\d{13}|97[89]\d{10}", identifier):
            candidates.append(
                (f"https://covers.openlibrary.org/b/isbn/{identifier}-L.jpg", "OpenLibrary")
            )
        # Google Books thumbnail (works for any identifier)
        if meta:
            for key in ("extraLarge", "large", "medium", "thumbnail", "smallThumbnail"):
                url = meta.get("image_links", {}).get(key)
                if url:
                    # Upgrade to higher resolution by removing zoom param
                    url = url.replace("&edge=curl", "").replace("&zoom=1", "&zoom=0")
                    candidates.append((url, f"Google Books ({key})"))
                    break
        # Amazon CDN fallback (works for both ASIN and ISBN-10)
        candidates.append(
            (
                f"https://images-na.ssl-images-amazon.com/images/P/{identifier}.01._LZZZZZZZ_.jpg",
                "Amazon CDN",
            )
        )

        for url, src in candidates:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=20) as r:
                    data = r.read()
                if len(data) > 5000:
                    return data, src
            except Exception:
                continue
        return None, None
