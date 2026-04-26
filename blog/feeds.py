from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Essential Topics'
    link = '/blog/'
    description = 'Deep dives into AI, health, biology, and genetics.'

    def items(self):
        return Post.objects.filter(published=True)[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_pubdate(self, item):
        return item.created_at

    def item_link(self, item):
        return reverse('blog:blog_detail', args=[item.slug])
