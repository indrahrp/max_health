from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Article.objects.filter(published=True).select_related('pillar')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        from django.urls import reverse
        return reverse('topics:article_detail', args=[obj.pillar.slug, obj.slug])
