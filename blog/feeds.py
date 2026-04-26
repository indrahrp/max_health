from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My Health Corner'
    link = '/blog/'
    description = 'Health writing on carnivore diet, metabolic health, and ancestral nutrition.'

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
