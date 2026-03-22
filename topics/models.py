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