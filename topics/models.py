import re
from django.db import models
from blog.models import Post


class Pillar(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=10, default='📖')
    color = models.CharField(max_length=20, default='teal')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def article_count(self):
        return self.articles.filter(published=True).count()


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=300)
    content = models.TextField()
    pillar = models.ForeignKey(
        Pillar,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )
    related_posts = models.ManyToManyField(
        Post,
        blank=True,
        related_name='related_articles'
    )
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    ai_summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def reading_time(self):
        from django.utils.html import strip_tags
        word_count = len(strip_tags(self.content).split())
        minutes = max(1, round(word_count / 200))
        return f"{minutes} min read"

    @property
    def og_image_url(self):
        """First <img src> in the article content as an absolute, OG-safe URL.

        Major social platforms (Facebook, X, LinkedIn, WhatsApp) do not render SVG
        OG images — they drop the preview thumbnail entirely. For SVGs we rewrite
        the URL to a Cloudinary upload-transform that rasterises to JPG 1200x630
        (with a dark Cogitra-bg fill). This requires the SVG to have been uploaded
        to Cloudinary at `cogitra/<basename>` first; Cloudinary natively rasterises
        uploaded SVGs when requested in a raster format like f_jpg.
        """
        OG_TRANSFORM = 'c_fill,w_1200,h_630,f_jpg,b_rgb:060c16'
        CLOUD = 'https://res.cloudinary.com/dxmrrtzha'

        m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', self.content or '')
        if not m:
            return ''
        src = m.group(1).strip()

        # Normalise to an absolute URL.
        if src.startswith('//'):
            src = 'https:' + src
        elif src.startswith('/'):
            src = 'https://cogitra.com' + src

        is_svg = src.lower().split('?')[0].endswith('.svg')

        # Already on Cloudinary: insert the OG transform before the public_id.
        cloud_upload_prefix = f'{CLOUD}/image/upload/'
        if src.startswith(cloud_upload_prefix):
            if not is_svg:
                return src  # raster Cloudinary asset — fine for OG as-is
            tail = src[len(cloud_upload_prefix):]
            # Strip any existing transformations (segments containing commas before public_id).
            # Cloudinary upload URLs look like: .../upload/[transforms/][v123/]public_id.ext
            parts = tail.split('/')
            # Remove leading transform segment (contains commas) if present.
            if parts and ',' in parts[0]:
                parts = parts[1:]
            return f'{cloud_upload_prefix}{OG_TRANSFORM}/' + '/'.join(parts)

        # Local static SVG → assume Cloudinary mirror at cogitra/<basename>.svg
        if is_svg and '/static/blog/illustrations/' in src:
            basename = src.rsplit('/', 1)[-1].split('?')[0]  # e.g. "enduring-darkness-peterson.svg"
            return f'{cloud_upload_prefix}{OG_TRANSFORM}/cogitra/{basename}'

        return src


