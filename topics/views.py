from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Pillar, Article
from blog.models import Post


def topics_home(request):
    pillars = Pillar.objects.all()
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    return render(request, 'topics/topics_home.html', {
        'pillars': pillars,
        'recent_posts': recent_posts,
    })


def pillar_detail(request, slug):
    from blog.views import _section_for_slug
    pillar = get_object_or_404(Pillar, slug=slug)
    articles = Article.objects.filter(pillar=pillar, published=True)
    topic = request.GET.get('topic', '').strip()
    if topic:
        keyword = topic.replace('-', ' ')
        articles = articles.filter(
            Q(slug__icontains=topic) |
            Q(title__icontains=keyword) |
            Q(summary__icontains=keyword) |
            Q(ai_summary__icontains=keyword)
        )
    all_pillars = Pillar.objects.all()
    section_key, section = _section_for_slug(pillar.slug)
    return render(request, 'topics/pillar_detail.html', {
        'pillar': pillar,
        'articles': articles,
        'all_pillars': all_pillars,
        'section_key': section_key,
        'section': section,
        'active_topic': topic,
    })


def article_detail(request, pillar_slug, article_slug):
    from blog.views import SECTION_CONFIG, _section_for_slug
    from blog.models import Post
    pillar = get_object_or_404(Pillar, slug=pillar_slug)
    article = get_object_or_404(Article, slug=article_slug, published=True)
    related_posts = article.related_posts.filter(published=True)
    other_articles = Article.objects.filter(
        pillar=pillar, published=True
    ).exclude(id=article.id)[:4]

    section_key, section = _section_for_slug(pillar.slug)

    # See-also footer (3 items across sections)
    see_also_articles = list(Article.objects.filter(published=True).exclude(id=article.id).select_related('pillar')[:6])
    see_also_posts = list(Post.objects.filter(published=True).select_related('category')[:6])
    combined = []
    for a in see_also_articles:
        skey, _ = _section_for_slug(a.pillar.slug if a.pillar else None)
        combined.append({'title': a.title, 'url': f'/topics/{a.pillar.slug}/{a.slug}/' if a.pillar else None, 'section_key': skey, 'date': a.created_at, 'reading_time': a.reading_time()})
    for p in see_also_posts:
        skey, _ = _section_for_slug(p.category.slug if p.category else None)
        combined.append({'title': p.title, 'url': f'/blog/{p.slug}/', 'section_key': skey, 'date': p.created_at, 'reading_time': p.reading_time()})
    combined.sort(key=lambda x: x['date'], reverse=True)
    see_also = []
    seen_sections = set()
    for c in combined:
        if c['section_key'] not in seen_sections:
            see_also.append(c); seen_sections.add(c['section_key'])
        if len(see_also) >= 3: break
    if len(see_also) < 3:
        for c in combined:
            if c not in see_also:
                see_also.append(c)
            if len(see_also) >= 3: break
    for c in see_also:
        c['section'] = SECTION_CONFIG.get(c['section_key'])

    return render(request, 'topics/article_detail.html', {
        'pillar': pillar,
        'article': article,
        'section_key': section_key,
        'section': section,
        'see_also': see_also,
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

