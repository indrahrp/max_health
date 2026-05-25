from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from .models import Post, Project, Category, Tag, BookReview
from .forms import CommentForm, SubscribeForm


# Cogitra section system — 8 sections, each with its own accent + curve + typography
# Curve SVG paths are in viewBox 0 0 200 200
SECTION_CONFIG = {
    'ai': {
        'index': 1, 'short': 'AI',
        'title': 'Artificial Intelligence',
        'tagline': 'Machine learning, deep learning, research, tools, and trends.',
        'note': 'Two decades into the AI summer, the patient work has barely begun. This section covers the architectures, the open questions, and the slow weather that follows the headlines.',
        'editor': 'Lena Okafor',
        'accent_hex': '#5b6cff',
        'curve': 'M 40 30 L 60 30 L 80 90 L 100 70 L 120 130 L 140 110 L 160 170',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.026em',
        'pillar_slugs': ['artificial-intelligence'],
        'category_slugs': ['ai', 'artificial-intelligence'],
    },
    'health': {
        'index': 2, 'short': 'Health',
        'title': 'Health',
        'tagline': 'Medical advances, wellness, and public-health reporting.',
        'note': 'Health, properly understood, is mostly other people’s problem. We report on medicine, public policy, and the long argument about what the body owes the world.',
        'editor': 'Priya Shah',
        'accent_hex': '#2fbf7c',
        'curve': 'M 30 100 L 70 100 L 80 70 L 95 130 L 110 60 L 125 120 L 150 100 L 175 100',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.02em',
        'pillar_slugs': ['species-appropriate-diet', 'cancer', 'cancer-metabolic-health', 'carnivore-diet', 'autoimmune', 'autoimmune-disease'],
        'category_slugs': ['health'],
    },
    'biology': {
        'index': 3, 'short': 'Biology',
        'title': 'Biology',
        'tagline': 'Cells, evolution, ecology, and biotechnology.',
        'note': 'Life keeps doing improbable things on long enough timescales. We follow cells, ecosystems, and the people doggedly watching them.',
        'editor': 'Mateo Reyes',
        'accent_hex': '#26c2c9',
        'curve': 'M 50 50 C 80 60, 90 110, 60 130 C 30 150, 80 170, 130 160 C 170 152, 165 130, 160 110',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.012em',
        'pillar_slugs': ['biology'],
        'category_slugs': ['biology'],
    },
    'mindset': {
        'index': 4, 'short': 'Mindset',
        'title': 'Mindset',
        'tagline': 'Cognition, attention, and the inner life of the thinker.',
        'note': 'The inner life resists optimisation. We file dispatches from that resistance — the science of attention, the practice of slowness, the case for thinking on purpose.',
        'editor': 'Iris Kovac',
        'accent_hex': '#a387ff',
        'curve': 'M 60 30 C 130 60, 50 110, 130 130 C 80 150, 130 170, 90 185',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'italic',
        'type_tracking': '-0.008em',
        'pillar_slugs': ['mindset-success', 'mindset'],
        'category_slugs': ['mindset'],
    },
    'genetics': {
        'index': 5, 'short': 'Genetics',
        'title': 'Genetics',
        'tagline': 'Genomics, gene editing, CRISPR, heritability, and beyond.',
        'note': 'We can finally read what we used to guess at. Genomes, edits, ancestry, and the politics of the alphabet our cells were already using.',
        'editor': 'Dr. Adaeze Williams',
        'accent_hex': '#e0567a',
        'curve': 'M 70 30 C 110 50, 70 80, 110 100 C 70 120, 110 150, 80 180',
        'type_family': 'var(--font-sans)',
        'type_weight': '600',
        'type_style': 'normal',
        'type_tracking': '-0.032em',
        'pillar_slugs': ['genetics'],
        'category_slugs': ['genetics'],
    },
    'longevity': {
        'index': 6, 'short': 'Longevity',
        'title': 'Longevity',
        'tagline': 'Aging, senescence, and the long arithmetic of human time.',
        'note': 'The slowest field in biology, in a hurry. We cover the science of ageing and the strange new industries it has started.',
        'editor': 'Jonas Bremmer',
        'accent_hex': '#d4a23a',
        'curve': 'M 60 30 C 45 80, 50 140, 110 170 C 145 188, 165 175, 175 150',
        'type_family': 'var(--font-serif)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.008em',
        'pillar_slugs': ['longevity'],
        'category_slugs': ['longevity'],
    },
    'physics': {
        'index': 7, 'short': 'Physics',
        'title': 'Physics',
        'tagline': 'Cosmology, particles, condensed matter, and first principles.',
        'note': 'The interesting questions have moved out of the headlines. We follow them — into solid-state matter, the structure of the vacuum, and the patient instruments measuring both.',
        'editor': 'Hana Park',
        'accent_hex': '#6db4d8',
        'curve': 'M 40 110 C 60 60, 140 60, 170 110 C 150 170, 80 170, 50 130',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.022em',
        'pillar_slugs': ['physics'],
        'category_slugs': ['physics'],
    },
    'books': {
        'index': 8, 'short': 'Books',
        'title': 'Book Review',
        'tagline': 'Long reads on long books — fiction and nonfiction, considered slowly.',
        'note': 'The slow read deserves slow company. We review the books that matter — fiction, science, and the long, patient nonfiction that does not make the news.',
        'editor': 'Naomi Kessel',
        'accent_hex': '#b88a5c',
        'curve': 'M 100 30 C 60 50, 60 130, 60 170 M 100 30 C 140 50, 140 130, 140 170 M 60 170 C 80 175, 120 175, 140 170',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.01em',
        'pillar_slugs': [],
        'category_slugs': [],
        'is_books': True,  # rendered differently — sources from BookReview, not Article/Post
    },
}


def section_landing(request, key):
    from topics.models import Article
    config = SECTION_CONFIG.get(key)
    if not config:
        raise Http404('Unknown section')

    if config.get('is_books'):
        # Books section sources from BookReview instead of Article/Post
        books = list(BookReview.objects.filter(published=True).select_related('category'))
        items = books
    else:
        articles = list(Article.objects.filter(
            published=True, pillar__slug__in=config['pillar_slugs']
        ).select_related('pillar'))
        posts = list(Post.objects.filter(
            published=True, category__slug__in=config['category_slugs']
        ).select_related('category'))
        items = articles + posts

    item_count = len(items)
    hero_item = items[0] if items else None
    grid_items = items[1:11] if len(items) > 1 else []

    # All other sections (for "Other sections" footer)
    other_sections = [(k, v) for k, v in SECTION_CONFIG.items() if k != key]

    return render(request, 'blog/section_landing.html', {
        'key': key,
        'config': config,
        'hero_item': hero_item,
        'grid_items': grid_items,
        'item_count': item_count,
        'other_sections': other_sections,
    })


def home(request):
    from topics.models import Article
    all_published = Post.objects.filter(published=True)
    hero_post = all_published.filter(featured=True).first() or all_published.first()
    secondary_posts = list(all_published.exclude(id=hero_post.id)[:2]) if hero_post else []
    latest_posts = all_published[:4]
    popular_posts = all_published[:4]
    post_count = all_published.count()
    book_count = BookReview.objects.filter(published=True).count()
    currently_reading = BookReview.objects.filter(published=True, status='reading').first()
    featured_articles = Article.objects.filter(published=True).select_related('pillar')[:3]
    categories = Category.objects.all()

    # Health topics — articles from health-related pillars
    HEALTH_PILLARS = ['cancer', 'species-appropriate-diet', 'cancer-metabolic-health', 'carnivore-diet', 'autoimmune-disease']
    health_articles = (
        Article.objects
        .filter(published=True, pillar__slug__in=HEALTH_PILLARS)
        .select_related('pillar')[:8]
    )
    health_count = Article.objects.filter(
        published=True, pillar__slug__in=HEALTH_PILLARS
    ).count()

    return render(request, 'blog/home.html', {
        'hero_post': hero_post,
        'secondary_posts': secondary_posts,
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        'post_count': post_count,
        'book_count': book_count,
        'featured_articles': featured_articles,
        'currently_reading': currently_reading,
        'categories': categories,
        'health_articles': health_articles,
        'health_count': health_count,
        'sections': SECTION_CONFIG,
    })


def about(request):
    from .models import Profile
    profile = Profile.objects.first()
    interests = [
        'Biology',
        'Physics',
        'Health & metabolism',
        'Psychiatry',
        'Human behaviour',
        'Neuroscience',
        'Evolutionary science',
    ]
    return render(request, 'blog/about.html', {
        'profile': profile,
        'interests': interests,
    })


def blog_list(request):
    from topics.models import Article
    from itertools import groupby

    selected = request.GET.get('section') or request.GET.get('category')
    selected_tag = request.GET.get('tag')

    posts = Post.objects.filter(published=True).select_related('category')
    articles = Article.objects.filter(published=True).select_related('pillar')

    if selected:
        cfg = SECTION_CONFIG.get(selected)
        if cfg:
            posts = posts.filter(category__slug__in=cfg['category_slugs'])
            articles = articles.filter(pillar__slug__in=cfg['pillar_slugs'])
        else:
            posts = posts.filter(category__slug=selected)
            articles = articles.none()

    if selected_tag:
        posts = posts.filter(tags__slug=selected_tag)
        articles = articles.none()

    # Combined timeline
    combined = []
    for p in posts:
        combined.append({
            'item': p, 'kind': 'post', 'date': p.created_at,
            'title': p.title, 'slug': p.slug,
            'category_slug': p.category.slug if p.category else None,
            'category_name': p.category.name if p.category else None,
            'reading_time': p.reading_time(),
            'url': f'/blog/{p.slug}/',
        })
    for a in articles:
        combined.append({
            'item': a, 'kind': 'article', 'date': a.created_at,
            'title': a.title, 'slug': a.slug,
            'category_slug': a.pillar.slug if a.pillar else None,
            'category_name': a.pillar.name if a.pillar else None,
            'reading_time': a.reading_time(),
            'url': f'/topics/{a.pillar.slug}/{a.slug}/' if a.pillar else None,
        })
    combined.sort(key=lambda x: x['date'], reverse=True)

    # Map every category slug → section accent (for the dots/pills)
    slug_to_section = {}
    for sec_key, sec in SECTION_CONFIG.items():
        for s in sec.get('pillar_slugs', []) + sec.get('category_slugs', []):
            slug_to_section[s] = (sec_key, sec)
    for entry in combined:
        s = entry.get('category_slug')
        if s and s in slug_to_section:
            entry['section_key'], entry['section'] = slug_to_section[s]

    # Group by month (e.g. "May 2026")
    def month_key(e):
        return e['date'].strftime('%B %Y')
    grouped = []
    for month, items in groupby(combined, key=month_key):
        grouped.append((month, list(items)))

    categories = Category.objects.all()
    tags = Tag.objects.filter(posts__published=True).distinct()

    return render(request, 'blog/blog_list.html', {
        'grouped_entries': grouped,
        'total_count': len(combined),
        'sections': SECTION_CONFIG,
        'selected': selected,
        'selected_tag': selected_tag,
        'categories': categories,
        'tags': tags,
    })


def _section_for_slug(slug):
    """Find the SECTION_CONFIG entry that owns a given category or pillar slug."""
    if not slug:
        return None, None
    for key, cfg in SECTION_CONFIG.items():
        if slug in cfg.get('category_slugs', []) or slug in cfg.get('pillar_slugs', []):
            return key, cfg
    return None, None


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    related = Post.objects.filter(
        category=post.category, published=True
    ).exclude(id=post.id)[:3]
    related_topics = post.related_articles.filter(published=True)
    comments = post.comments.filter(approved=True)
    comment_form = CommentForm()
    comment_submitted = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_submitted = True
            comment_form = CommentForm()

    section_key, section = _section_for_slug(post.category.slug if post.category else None)

    # See-also items — 3 most recent from other sections (variety)
    from topics.models import Article
    see_also_posts = list(Post.objects.filter(published=True).exclude(id=post.id).select_related('category')[:6])
    see_also_articles = list(Article.objects.filter(published=True).select_related('pillar')[:6])
    combined = []
    for p in see_also_posts:
        skey, _ = _section_for_slug(p.category.slug if p.category else None)
        combined.append({'title': p.title, 'url': f'/blog/{p.slug}/', 'section_key': skey, 'date': p.created_at, 'reading_time': p.reading_time()})
    for a in see_also_articles:
        skey, _ = _section_for_slug(a.pillar.slug if a.pillar else None)
        combined.append({'title': a.title, 'url': f'/topics/{a.pillar.slug}/{a.slug}/' if a.pillar else None, 'section_key': skey, 'date': a.created_at, 'reading_time': a.reading_time()})
    combined.sort(key=lambda x: x['date'], reverse=True)
    # Variety-weighted: try to take one per unique section first
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
    # Attach section config
    for c in see_also:
        c['section'] = SECTION_CONFIG.get(c['section_key'])

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'section_key': section_key,
        'section': section,
        'see_also': see_also,
        'related': related,
        'related_topics': related_topics,
        'comments': comments,
        'comment_form': comment_form,
        'comment_submitted': comment_submitted,
        'comment_count': comments.count(),
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, published=True)
    categories = Category.objects.all()
    tags = Tag.objects.filter(posts__published=True).distinct()
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'selected': slug,
        'category': category,
    })


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'blog/projects.html', {'all_projects': all_projects})


def book_list(request):
    currently_reading = BookReview.objects.filter(published=True, status='reading')
    read = BookReview.objects.filter(published=True, status='read').select_related('category')
    wishlist = BookReview.objects.filter(published=True, status='wishlist')
    categories = Category.objects.filter(book_reviews__published=True).distinct()
    selected_cat = request.GET.get('category')
    if selected_cat:
        read = read.filter(category__slug=selected_cat)
    return render(request, 'blog/book_list.html', {
        'currently_reading': currently_reading,
        'read': read,
        'wishlist': wishlist,
        'book_categories': categories,
        'selected_book_cat': selected_cat,
    })


def book_detail(request, slug):
    book = get_object_or_404(BookReview, slug=slug, published=True)
    return render(request, 'blog/book_detail.html', {'book': book})


def search(request):
    from topics.models import Article
    query = request.GET.get('q', '').strip()
    post_results = []
    article_results = []
    if query:
        post_results = Post.objects.filter(published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query)
        )[:10]
        article_results = Article.objects.filter(published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query)
        )[:10]
    return render(request, 'blog/search_results.html', {
        'query': query,
        'post_results': post_results,
        'article_results': article_results,
    })


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'blog/subscribe_thanks.html')
            except Exception:
                pass
    return redirect('blog:home')
