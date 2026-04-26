from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap, BookReviewSitemap
from topics.sitemaps import ArticleSitemap
from blog.feeds import LatestPostsFeed

sitemaps = {
    'posts': PostSitemap,
    'books': BookReviewSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('topics/', include('topics.urls', namespace='topics')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('blog/feed/', LatestPostsFeed(), name='blog_feed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
