from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView

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
    # Short-URL aliases → redirect to canonical /topics/<slug>/ (query_string=True preserves ?topic= etc.)
    path('mental/', RedirectView.as_view(url='/topics/mental-health/', permanent=False, query_string=True)),
    path('mental/<slug:article_slug>/', RedirectView.as_view(pattern_name='topics:article_detail', permanent=False, query_string=True), kwargs={'pillar_slug': 'mental-health'}),
    path('biology/', RedirectView.as_view(url='/topics/biology/', permanent=False, query_string=True)),
    path('biology/<slug:article_slug>/', RedirectView.as_view(pattern_name='topics:article_detail', permanent=False, query_string=True), kwargs={'pillar_slug': 'biology'}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('blog/feed/', LatestPostsFeed(), name='blog_feed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
