from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Pillar, Article


def topics_home(request):
    pillars = Pillar.objects.all()
    return render(request, 'topics/topics_home.html', {'pillars': pillars})


def pillar_detail(request, slug):
    pillar = get_object_or_404(Pillar, slug=slug)
    articles = Article.objects.filter(pillar=pillar, published=True)
    all_pillars = Pillar.objects.all()
    return render(request, 'topics/pillar_detail.html', {
        'pillar': pillar,
        'articles': articles,
        'all_pillars': all_pillars,
    })


def article_detail(request, pillar_slug, article_slug):
    pillar = get_object_or_404(Pillar, slug=pillar_slug)
    article = get_object_or_404(Article, slug=article_slug, published=True)
    related_posts = article.related_posts.filter(published=True)
    other_articles = Article.objects.filter(
        pillar=pillar, published=True
    ).exclude(id=article.id)[:4]
    return render(request, 'topics/article_detail.html', {
        'pillar': pillar,
        'article': article,
        'related_posts': related_posts,
        'other_articles': other_articles,
    })


def topics_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Article.objects.filter(
            published=True
        ).filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, 'topics/topics_search.html', {
        'query': query,
        'results': results,
    })

