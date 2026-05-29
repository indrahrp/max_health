#!/usr/bin/env python3
"""
YouTube Transcript Fetcher for Trading Strategy Extraction

Usage:
  # Single video
  python fetch_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

  # Multiple videos
  python fetch_transcript.py "URL1" "URL2" "URL3"

  # Channel — auto-pull cookies from Chrome (recommended, bypasses IP blocks)
  python fetch_transcript.py "https://www.youtube.com/@ToriTrades" --channel --max 100 --cookies-from-browser chrome

  # Channel — use a saved cookies.txt file
  python fetch_transcript.py "https://www.youtube.com/@ToriTrades" --channel --max 100 --cookies cookies.txt

  # Save to a specific file
  python fetch_transcript.py "https://www.youtube.com/@ToriTrades" --channel --output tori_transcripts.txt --cookies-from-browser chrome

Bypassing IP blocks:
  YouTube blocks unauthenticated bulk requests. Pass your browser cookies so
  requests look like a logged-in session:

  Option A (easiest): --cookies-from-browser chrome
    Reads cookies directly from your Chrome profile. Also works with:
    firefox, safari, brave, edge, opera, chromium

  Option B: --cookies cookies.txt
    Export cookies manually via the "Get cookies.txt LOCALLY" Chrome extension,
    then point this flag at the file.

After running, paste the output file contents into:
  prompts/01-extract-strategy.md  (below the dashed line)
Then Claude will extract the strategy and save it to rules.json.
"""

import os
import sys
import re
import time
import json
import html
import random
import argparse
import tempfile
import subprocess
import urllib.parse
from http.cookiejar import MozillaCookieJar
from pathlib import Path

import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

RETRY_ATTEMPTS = 3
RETRY_BACKOFF = [3, 8, 20]              # seconds between library method retries
REQUEST_DELAY = (5.0, 10.0)             # random delay between videos — key to avoiding 429s
TRANSCRIPT_RETRY_BACKOFF = [30, 90, 180]  # backoff for timedtext 429s (30s → 1.5m → 3m)


def extract_video_id(url: str) -> str | None:
    patterns = [
        r"(?:v=|/)([0-9A-Za-z_-]{11})(?:[&?]|$)",
        r"(?:embed/)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be/)([0-9A-Za-z_-]{11})",
        r"(?:shorts/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    if re.match(r"^[0-9A-Za-z_-]{11}$", url):
        return url
    return None


def build_session(cookies_file: str | None = None, cookies_from_browser: str | None = None) -> requests.Session:
    session = requests.Session()

    if cookies_from_browser:
        # Generate a path but do NOT create the file — yt-dlp needs to create it fresh
        tmp_path = Path(tempfile.gettempdir()) / f"yt_cookies_{os.getpid()}.txt"
        if tmp_path.exists():
            tmp_path.unlink()

        print(f"  Extracting cookies from {cookies_from_browser} (may prompt for keychain access)...")
        result = subprocess.run(
            [
                "yt-dlp",
                "--cookies-from-browser", cookies_from_browser,
                "--cookies", str(tmp_path),
                "--skip-download",
                "--no-warnings",
                # Use a real short video so yt-dlp actually processes the request and dumps cookies
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            ],
            capture_output=True,
            text=True,
        )
        if tmp_path.exists() and tmp_path.stat().st_size > 0:
            cookies_file = str(tmp_path)
            print("  Cookies extracted successfully.")
        else:
            err = (result.stderr or result.stdout).strip().split("\n")[0]
            print(f"  Warning: cookie extraction failed ({err}). Continuing without.")
            print("  Tip: make sure Chrome is running and you are logged into YouTube.")

    if cookies_file:
        jar = MozillaCookieJar(cookies_file)
        try:
            jar.load(ignore_discard=True, ignore_expires=True)
            session.cookies = jar
            count = len(list(jar))
            print(f"  Loaded {count} cookies.")
        except Exception as e:
            print(f"  Warning: could not parse cookies file ({e}). Continuing without.")

    # Set browser-like headers so requests look like Chrome
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    })

    return session


def fetch_via_direct_api(video_id: str, session: requests.Session) -> tuple[str | None, str]:
    """
    Fetch transcript by parsing ytInitialPlayerResponse from the watch page.
    Returns (text, reason) where reason explains failure if text is None.
    Authenticated session bypasses IP blocks via logged-in browser cookies.
    """
    try:
        r = session.get(f"https://www.youtube.com/watch?v={video_id}", timeout=20)
        if r.status_code != 200:
            return None, f"watch page {r.status_code}"

        m = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.+?\});\s*(?:var |window\[)", r.text)
        if not m:
            return None, "ytInitialPlayerResponse not found"

        data = json.loads(m.group(1))
        tracks = (
            data.get("captions", {})
                .get("playerCaptionsTracklistRenderer", {})
                .get("captionTracks", [])
        )
        if not tracks:
            return None, "no captions"

        track = next(
            (t for t in tracks if t.get("languageCode", "").startswith("en")),
            tracks[0],
        )
        base_url = track.get("baseUrl", "")
        if not base_url:
            return None, "no baseUrl"

        api_url = re.sub(r"&fmt=[^&]*", "", base_url) + "&fmt=json3"

        # Retry the timedtext fetch — this endpoint rate-limits at 429
        for attempt, backoff in enumerate(TRANSCRIPT_RETRY_BACKOFF):
            tr = session.get(api_url, timeout=15)
            if tr.status_code == 200:
                break
            if tr.status_code == 429:
                if attempt < len(TRANSCRIPT_RETRY_BACKOFF) - 1:
                    print(f"    Transcript rate-limited (429) — waiting {backoff}s...")
                    time.sleep(backoff)
                else:
                    return None, "timedtext 429 after retries"
            else:
                return None, f"timedtext {tr.status_code}"

        events = tr.json().get("events", [])
        parts = [
            seg.get("utf8", "").strip()
            for ev in events
            for seg in ev.get("segs", [])
            if seg.get("utf8", "").strip() not in ("", "\n")
        ]
        return (" ".join(parts) if parts else None), "empty transcript"
    except Exception as e:
        return None, str(e)


def normalize_channel_url(url: str) -> str:
    """Append /videos to channel URLs so we only get regular uploads, not shorts or live."""
    url = url.rstrip("/")
    if not url.startswith("http"):
        url = "https://" + url
    # Already pointing at a specific playlist or /videos
    if any(x in url for x in ["/videos", "/playlist", "list="]):
        return url
    return url + "/videos"


def get_channel_video_ids(channel_url: str, max_videos: int, cookies_from_browser: str | None) -> list[str]:
    url = normalize_channel_url(channel_url)
    print(f"  Fetching video list from: {url} (up to {max_videos} videos)...")
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print", "id",
        "--playlist-end", str(max_videos),
        "--no-warnings",
        "--no-check-certificates",
        "--extractor-args", "youtubetab:skip=authcheck",
    ]
    if cookies_from_browser:
        cmd += ["--cookies-from-browser", cookies_from_browser]
    cmd.append(url)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  yt-dlp error: {result.stderr.strip()}", file=sys.stderr)
        return []
    ids = [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]
    print(f"  Found {len(ids)} videos.")
    return ids


def get_video_title(video_id: str, cookies_from_browser: str | None) -> str:
    cmd = ["yt-dlp", "--print", "title", "--no-warnings"]
    if cookies_from_browser:
        cmd += ["--cookies-from-browser", cookies_from_browser]
    cmd.append(f"https://www.youtube.com/watch?v={video_id}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else video_id


def _parse_vtt(vtt_text: str) -> str:
    """Strip VTT formatting tags and timestamps, return plain text."""
    lines = []
    for line in vtt_text.splitlines():
        line = line.strip()
        if not line or line.startswith("WEBVTT") or "-->" in line or line.isdigit():
            continue
        # Strip HTML tags like <c>, <00:00:00.000>
        line = re.sub(r"<[^>]+>", "", line)
        if line:
            lines.append(line)
    # Deduplicate consecutive identical lines (VTT often repeats)
    deduped = [lines[0]] if lines else []
    for line in lines[1:]:
        if line != deduped[-1]:
            deduped.append(line)
    return " ".join(deduped)


def fetch_via_ytdlp(video_id: str, cookies_from_browser: str | None, cookies_file: str | None) -> str | None:
    """Use yt-dlp to download auto-generated subtitles. Handles auth and IP blocks."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--sub-format", "vtt",
            "--skip-download",
            "--no-warnings",
            "--no-check-certificates",
            "--output", os.path.join(tmpdir, "%(id)s"),
        ]
        if cookies_from_browser:
            cmd += ["--cookies-from-browser", cookies_from_browser]
        elif cookies_file:
            cmd += ["--cookies", cookies_file]
        cmd.append(f"https://www.youtube.com/watch?v={video_id}")

        result = subprocess.run(cmd, capture_output=True, text=True)
        vtt_files = list(Path(tmpdir).glob("*.vtt"))
        if not vtt_files:
            return None
        return _parse_vtt(vtt_files[0].read_text(encoding="utf-8", errors="ignore"))


def fetch_transcript(
    video_id: str,
    api: YouTubeTranscriptApi,
    session: requests.Session,
    cookies_from_browser: str | None,
    cookies_file: str | None,
) -> str | None:
    # Method 1: Direct timedtext API with authenticated session (fastest, bypasses IP block)
    text, reason = fetch_via_direct_api(video_id, session)
    if text:
        return text
    if reason == "no captions":
        print(f"    No captions on this video — skipping.")
        return None
    if reason not in ("empty transcript",):
        print(f"    Direct API: {reason} — trying yt-dlp...")

    # Method 2: yt-dlp subtitle download (handles auth and geo-restrictions)
    text = fetch_via_ytdlp(video_id, cookies_from_browser, cookies_file)
    if text:
        return text

    # Method 3: youtube-transcript-api library (works when no IP block)
    for attempt in range(RETRY_ATTEMPTS):
        try:
            fetched = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
            return " ".join(e.text for e in fetched)
        except (TranscriptsDisabled, NoTranscriptFound):
            try:
                transcript_list = api.list(video_id)
                transcript = transcript_list.find_generated_transcript(["en"])
                entries = transcript.fetch()
                return " ".join(e.text for e in entries)
            except Exception:
                print(f"    No English transcript available — skipping.")
                return None
        except VideoUnavailable:
            print(f"    Video unavailable — skipping.")
            return None
        except CouldNotRetrieveTranscript as e:
            msg = str(e)
            is_ip_block = "blocking" in msg.lower() or "ip" in msg.lower() or "cloud" in msg.lower()
            if is_ip_block and attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF[attempt]
                print(f"    Retrying library method in {wait}s (attempt {attempt + 1}/{RETRY_ATTEMPTS})...")
                time.sleep(wait)
            else:
                print(f"    Could not retrieve transcript — skipping.")
                return None
        except Exception as e:
            if attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF[attempt]
                print(f"    Error ({e}) — retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"    Error: {e} — skipping.")
                return None
    return None


def load_progress(progress_file: Path) -> dict[str, dict]:
    """Load previously fetched transcripts keyed by video ID."""
    if not progress_file.exists():
        return {}
    try:
        return json.loads(progress_file.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_progress(progress_file: Path, cache: dict[str, dict]) -> None:
    progress_file.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def process_videos(
    video_ids: list[str],
    api: YouTubeTranscriptApi,
    session: requests.Session,
    cookies_from_browser: str | None,
    cookies_file: str | None,
    progress_file: Path,
) -> list[dict]:
    cache = load_progress(progress_file)
    if cache:
        print(f"  Resuming — {len(cache)} videos already fetched.\n")

    results = list(cache.values())  # start with already-fetched ones
    todo = [vid for vid in video_ids if vid not in cache]

    for i, vid_id in enumerate(todo, 1):
        pos = len(results) + 1
        title = get_video_title(vid_id, cookies_from_browser)
        print(f"  [{pos}/{len(video_ids)}] {title}")
        text = fetch_transcript(vid_id, api, session, cookies_from_browser, cookies_file)
        if text:
            entry = {"id": vid_id, "title": title, "transcript": text}
            results.append(entry)
            cache[vid_id] = entry
            save_progress(progress_file, cache)   # persist after every success
            word_count = len(text.split())
            print(f"    OK — {word_count:,} words  (saved to progress file)")
        else:
            cache[vid_id] = {"id": vid_id, "title": title, "transcript": None}
            save_progress(progress_file, cache)   # mark as attempted so we don't retry it

        if i < len(todo):
            delay = random.uniform(*REQUEST_DELAY)
            time.sleep(delay)

    return [r for r in results if r.get("transcript")]


def build_output(results: list[dict]) -> str:
    sections = []
    for r in results:
        header = f"=== VIDEO: {r['title']} (https://youtu.be/{r['id']}) ==="
        sections.append(f"{header}\n\n{r['transcript']}")
    return "\n\n" + ("\n\n" + "-" * 80 + "\n\n").join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcripts for trading strategy extraction",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("urls", nargs="+", help="YouTube video URL(s) or channel URL (with --channel)")
    parser.add_argument("--channel", action="store_true", help="Treat the URL as a channel")
    parser.add_argument("--max", type=int, default=20, help="Max videos to fetch from a channel (default: 20)")
    parser.add_argument("--output", default="transcripts.txt", help="Output file (default: transcripts.txt)")
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume a previous run (skip already-fetched videos). Progress is saved to <output>.progress.json",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help=(
            "Incremental update mode: skip already-fetched videos (using the existing progress file) "
            "and APPEND only new transcripts to the output file. "
            "Use this on repeat runs to pick up new videos added to a channel since the last run."
        ),
    )
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="Extract cookies from browser to bypass IP blocks (chrome, firefox, safari, brave, edge)",
    )
    parser.add_argument(
        "--cookies",
        metavar="FILE",
        help="Path to a Netscape-format cookies.txt file",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    progress_file = output_path.with_suffix("").with_name(output_path.stem + ".progress.json")
    video_ids: list[str] = []
    incremental = args.incremental

    if not args.resume and not incremental and progress_file.exists():
        progress_file.unlink()   # fresh run — clear any old progress

    print()

    if args.channel:
        if len(args.urls) != 1:
            print("Error: --channel requires exactly one channel URL.", file=sys.stderr)
            sys.exit(1)
        print(f"Channel mode: {args.urls[0]}")
        video_ids = get_channel_video_ids(args.urls[0], args.max, args.cookies_from_browser)
        if not video_ids:
            print("No videos found. Check the channel URL.", file=sys.stderr)
            sys.exit(1)
    else:
        for url in args.urls:
            vid_id = extract_video_id(url)
            if vid_id:
                video_ids.append(vid_id)
            else:
                print(f"Warning: could not parse video ID from '{url}' — skipping.", file=sys.stderr)

    if not video_ids:
        print("No valid video IDs found.", file=sys.stderr)
        sys.exit(1)

    session = build_session(
        cookies_file=args.cookies,
        cookies_from_browser=args.cookies_from_browser,
    )
    api = YouTubeTranscriptApi(http_client=session)
    # resolved_cookies_file is set inside build_session; we pass the original for yt-dlp calls
    resolved_cookies_file = args.cookies

    if incremental:
        existing_cache = load_progress(progress_file)
        new_ids = [vid for vid in video_ids if vid not in existing_cache]
        print(f"\nIncremental mode: {len(existing_cache)} already fetched, {len(new_ids)} new video(s) to fetch.\n")
        if not new_ids:
            print("No new videos found. Output file is up to date.")
            sys.exit(0)
        video_ids = new_ids

    print(f"\nFetching transcripts for {len(video_ids)} video(s)...\n")
    print(f"  Progress saved to: {progress_file}")
    print(f"  If interrupted, re-run with --resume to continue where you left off.\n")
    results = process_videos(video_ids, api, session, args.cookies_from_browser, resolved_cookies_file, progress_file)

    if not results:
        print("\nNo transcripts were retrieved.", file=sys.stderr)
        print("YouTube may be rate-limiting your IP. Wait 30–60 minutes then re-run with --resume.", file=sys.stderr)
        print("If this is a fresh run, try adding --cookies-from-browser chrome.", file=sys.stderr)
        sys.exit(1)

    if incremental and output_path.exists():
        # Append only the newly fetched transcripts
        new_fetched = [r for r in results if r["id"] in {vid for vid in video_ids}]
        if new_fetched:
            with output_path.open("a", encoding="utf-8") as f:
                f.write("\n\n" + ("-" * 80) + "\n\n")
                f.write(build_output(new_fetched).strip())
                f.write("\n")
        success_rate = f"{len(new_fetched)} new"
    else:
        output = build_output(results)
        output_path.write_text(output, encoding="utf-8")
        success_rate = f"{len(results)}/{len(video_ids)}"

    print(f"\nDone. {success_rate} transcripts saved to: {output_path}")
    print("\nNext step:")
    print("  Open  prompts/01-extract-strategy.md  in Claude Code.")
    print(f"  Paste the contents of  {output_path}  below the dashed line at the bottom.")
    print("  Claude will extract the strategy and save it to rules.json.\n")


if __name__ == "__main__":
    main()
