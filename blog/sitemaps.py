from django.contrib.sitemaps import Sitemap
from .models import Post, BookReview


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        from django.urls import reverse
        return reverse('blog:blog_detail', args=[obj.slug])


class BookReviewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return BookReview.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        from django.urls import reverse
        return reverse('blog:book_detail', args=[obj.slug])
