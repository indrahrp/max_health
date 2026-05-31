from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from .models import Post, Project, Category, Tag, BookReview
from .forms import CommentForm, SubscribeForm


# Cogitra section system — 9 sections, each with its own accent + curve + typography
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
        'index': 2, 'short': 'Physical',
        'title': 'Physical Health',
        'tagline': 'The body, its diseases, the medicine, and the institutions around them.',
        'note': "The body is, properly understood, mostly other people's problem. We report on disease, medicine, public policy, and the long argument about what the body owes the world.",
        'editor': 'Priya Shah',
        'accent_hex': '#2fbf7c',
        'curve': 'M 30 100 L 70 100 L 80 70 L 95 130 L 110 60 L 125 120 L 150 100 L 175 100',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.02em',
        'pillar_slugs': [
            'species-appropriate-diet', 'carnivore-diet',
            'autoimmune', 'autoimmune-disease',
            'heart-disease', 'diabetes', 'type-1-diabetes',
            'weight', 'obesity', 'liver-disease', 'kidney-disease',
            'alzheimers', 'dementia',
            'cholesterol', 'biological-drugs', 'biologics',
            'medical-mishaps', 'mishaps',
        ],
        'category_slugs': ['health'],
        'subcategories': [
            {
                'id': 'diseases', 'name': 'Diseases', 'short': 'Diseases',
                'blurb': 'The conditions themselves — what is known, what is being researched, and what remains uncertain.',
                'accent': '#34a366', 'is_group': True,
                'subcategories': [
                    {
                        'id': 'autoimmune', 'name': 'Autoimmune Disease', 'short': 'Autoimmune',
                        'blurb': 'When the immune system mistakes home for elsewhere — lupus, MS, RA, and the long bench of the chronically misread.',
                        'accent': '#4cc995', 'match_slugs': ['autoimmune', 'autoimmune-disease'],
                    },
                    {
                        'id': 'metabolic', 'name': 'Metabolic Disease', 'short': 'Metabolic',
                        'blurb': 'Heart disease, diabetes, weight, liver and kidney conditions — sharing a common root in broken metabolism.',
                        'accent': '#3aab6b', 'is_group': True,
                        'subcategories': [
                            {'id': 'heart-disease',  'name': 'Heart Disease',        'short': 'Heart',       'blurb': 'The most common killer in the developed world — and the most often misframed. Lipids, inflammation, and the metabolic argument.', 'accent': '#34a366', 'match_slugs': ['heart-disease']},
                            {'id': 'diabetes',       'name': 'Diabetes',             'short': 'Diabetes',    'blurb': 'Type 1, type 2, type 1.5 — a family of metabolic diseases whose lines keep moving.', 'accent': '#5ecf86', 'match_slugs': ['diabetes', 'type-1-diabetes']},
                            {'id': 'weight',         'name': 'Weight',               'short': 'Weight',      'blurb': 'Obesity, GLP-1 drugs, set-point theory, and the long contest over what makes a body store and shed.', 'accent': '#43b878', 'match_slugs': ['weight', 'obesity']},
                            {'id': 'liver-disease',  'name': 'Liver Disease',        'short': 'Liver',       'blurb': 'Fatty liver, fibrosis, and the silent organ that bears the brunt of modern eating.', 'accent': '#2a8a52', 'match_slugs': ['liver-disease']},
                            {'id': 'kidney-disease', 'name': 'Kidney Disease',       'short': 'Kidney',      'blurb': "Diabetic nephropathy, hypertension, and the slow strangling of the body's filtration system.", 'accent': '#74d49d', 'match_slugs': ['kidney-disease']},
                            {'id': 'alzheimers',     'name': "Alzheimer's Disease",  'short': "Alzheimer's", 'blurb': 'Amyloid, tau, ApoE, and the slow re-thinking of dementia as a disease of brain metabolism.', 'accent': '#9bdcb6', 'match_slugs': ['alzheimers', 'dementia']},
                        ],
                    },
                ],
            },
            {
                'id': 'controversies', 'name': 'Medical Controversies', 'short': 'Controversies',
                'blurb': 'The arguments medicine keeps having with itself — cholesterol, biologics, and the system that resists correction.',
                'accent': '#86d3a6', 'is_group': True,
                'subcategories': [
                    {'id': 'cholesterol', 'name': 'The Cholesterol Debate', 'short': 'Cholesterol', 'blurb': 'Saturated fat, LDL, statins, and the seventy-year argument that shaped cardiovascular medicine.', 'accent': '#7bc99c', 'match_slugs': ['cholesterol']},
                    {'id': 'biologics',   'name': 'Biological Drugs',       'short': 'Biologics',   'blurb': 'Monoclonal antibodies, TNF inhibitors, and the pharmaceutical engineering that changed autoimmune care.', 'accent': '#92d4ad', 'match_slugs': ['biological-drugs', 'biologics']},
                    {'id': 'mishaps',     'name': 'Medical System Mishaps', 'short': 'Mishaps',     'blurb': 'When medicine gets it wrong — misdiagnosis, overtreatment, and the institutions that resist correction.', 'accent': '#a3deb9', 'match_slugs': ['medical-mishaps', 'mishaps']},
                ],
            },
            {
                'id': 'path-to-health', 'name': 'Path Toward Health', 'short': 'Path',
                'blurb': 'The practical interventions with actual evidence — diet, sleep, movement, and the slow reconstruction of function.',
                'accent': '#5cc191', 'match_slugs': ['species-appropriate-diet', 'carnivore-diet'],
            },
        ],
    },
    'mental': {
        'index': 3, 'short': 'Mental',
        'title': 'Mental Health',
        'tagline': 'Depression, anxiety, trauma, therapy, psychiatry, and what we now know about caring for the mind.',
        'note': 'The mind is a long, patient instrument. We cover the clinical literature, the politics of care, and the slow craft of getting better — in whatever sense that turns out to mean.',
        'editor': 'Dr. Sela Hartmann',
        'accent_hex': '#5ba896',
        'curve': 'M 30 110 C 55 60, 80 60, 100 110 C 120 160, 145 160, 170 110 C 178 95, 178 90, 175 80',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.01em',
        'pillar_slugs': ['mental-health', 'physiological-origin', 'psychological-origin', 'psychedelics'],
        'category_slugs': ['mental'],
        'subcategories': [
            {'id': 'physiological-origin', 'name': 'Mental Illness · Physiological Origin', 'short': 'Physiological', 'blurb': 'The metabolic, inflammatory, and structural roots of mental illness — mitochondria, gut, sleep, hormones.', 'accent': '#7ec0b0', 'match_slugs': ['physiological-origin']},
            {'id': 'psychological-origin', 'name': 'Mental Illness · Psychological Origin', 'short': 'Psychological', 'blurb': 'Trauma, attachment, cognition, and what the clinical literature still calls the talking cure.', 'accent': '#3d8576', 'match_slugs': ['psychological-origin']},
            {'id': 'psychedelics',         'name': 'Psychedelics',                          'short': 'Psychedelics',  'blurb': 'Psilocybin, MDMA, ketamine, and the renewed clinical research into psychedelic-assisted therapy for depression, PTSD, addiction, and end-of-life distress.', 'accent': '#c89ce8', 'match_slugs': ['psychedelics']},
        ],
    },
    'biology': {
        'index': 4, 'short': 'Biology',
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
        'pillar_slugs': ['biology', 'cancer', 'cancer-metabolic-health', 'life-of-a-cell', 'neuroscience'],
        'category_slugs': ['biology'],
        'subcategories': [
            {'id': 'origin-of-cancer', 'name': 'Origin of Cancer', 'short': 'Cancer',        'blurb': 'The metabolic theory of cancer, the Warburg effect, and the slow re-thinking of oncology.', 'accent': '#5cd2d8', 'match_slugs': ['cancer', 'cancer-metabolic-health']},
            {'id': 'life-of-a-cell',   'name': 'Life of a Cell',   'short': 'Cells',         'blurb': 'Mitochondria, signalling, autophagy, and the small economies inside every body.', 'accent': '#1ea5ad', 'match_slugs': ['life-of-a-cell']},
            {'id': 'neuroscience',     'name': 'Neuroscience',     'short': 'Neuro',         'blurb': 'How the brain works, what consciousness is, and what neuroscience reveals about memory, perception, and the self.', 'accent': '#818cf8', 'match_slugs': ['neuroscience']},
        ],
    },
    'mindset': {
        'index': 5, 'short': 'Mindset',
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
        'subcategories': [
            {
                'id': 'peterson', 'name': 'Jordan Peterson', 'short': 'Peterson',
                'blurb': 'On responsibility, meaning, and the long argument for getting your own house in order before you take aim at the world.',
                'accent': '#b9a3ff',
                'match_article_keywords': ['peterson'],
            },
            {
                'id': 'greene', 'name': 'Robert Greene', 'short': 'Greene',
                'blurb': 'Power, mastery, and human nature — the slow study of how people actually behave, drawn from a long shelf of history.',
                'accent': '#8e6ff5',
                'match_article_keywords': ['greene'],
            },
            {
                'id': 'mate', 'name': 'Gabor Maté', 'short': 'Maté',
                'blurb': 'Trauma, attachment, and addiction — the case that the body keeps a score the mind would rather not read.',
                'accent': '#c8b3ff',
                'match_article_keywords': ['gabor'],
            },
            {
                'id': 'general', 'name': 'General', 'short': 'General',
                'blurb': 'Everything else — essays, books, and ideas that shaped how I think but did not fit one author.',
                'accent': '#7b5ce8',
                'match_slugs': ['mindset-success', 'mindset'],
                'exclude_article_keywords': ['peterson', 'greene', 'gabor'],
            },
        ],
    },
    'genetics': {
        'index': 6, 'short': 'Genetics',
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
        'pillar_slugs': ['genetics', 'origin-stories-of-dna', 'dna-ai-future'],
        'category_slugs': ['genetics'],
        'subcategories': [
            {'id': 'origin-stories-of-dna',   'name': 'The Origin Stories of DNA',          'short': 'Origins',         'blurb': 'Mendel, Watson, Crick, and the long argument about what heredity actually is.', 'accent': '#ec7a96', 'match_slugs': ['origin-stories-of-dna']},
            {'id': 'dna-ai-future',           'name': 'DNA, AI, and the Future of Humanity','short': 'DNA · AI',   'blurb': 'CRISPR, polygenic prediction, and what we can do now that machines can read at scale.', 'accent': '#c43d62', 'match_slugs': ['dna-ai-future']},
        ],
    },
    'longevity': {
        'index': 7, 'short': 'Longevity',
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
        'subcategories': [
            {'id': 'supporting-biochemistry', 'name': 'Supporting Biochemistry', 'short': 'Biochemistry', 'blurb': 'NAD+, autophagy, mTOR, senolytics — the molecular knobs and what we know about turning them.', 'accent': '#e6b85e', 'match_slugs': ['supporting-biochemistry'], 'match_article_keywords': ['mtor', 'nad', 'senescen', 'longevity-pathway', 'venki']},
            {'id': 'lifestyle',               'name': 'Lifestyle',              'short': 'Lifestyle',    'blurb': 'Sleep, exercise, fasting, sun. The boring interventions that actually have data behind them.',     'accent': '#b8861f', 'match_slugs': ['lifestyle'], 'match_article_keywords': ['sauna']},
            {'id': 'longevity-research',      'name': 'Longevity Research',     'short': 'Research',     'blurb': 'The labs, the clinical trials, the strange new industries the field has started.',                'accent': '#c89530', 'match_slugs': ['longevity-research']},
        ],
    },
    'physics': {
        'index': 8, 'short': 'Physics',
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
        'index': 9, 'short': 'Books',
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


def _item_slug(it):
    if hasattr(it, 'pillar') and it.pillar:
        return it.pillar.slug
    if hasattr(it, 'category') and it.category:
        return it.category.slug
    return None


def _collect_leaf_slugs(node):
    """Return all match_slugs from leaf descendants of node."""
    if node.get('is_group') and node.get('subcategories'):
        result = []
        for child in node['subcategories']:
            result.extend(_collect_leaf_slugs(child))
        return result
    return list(node.get('match_slugs', []))


def _find_topic(subs, target_id, ancestors=None):
    """Return (node, ancestors_list) for the node with id==target_id."""
    if ancestors is None:
        ancestors = []
    for s in subs:
        if s['id'] == target_id:
            return s, ancestors
        if s.get('subcategories'):
            found, path = _find_topic(s['subcategories'], target_id, ancestors + [s])
            if found:
                return found, path
    return None, []


def _item_matches_node(it, node):
    """Return True if item matches this leaf node's pillar slugs, article keywords, and exclusions."""
    slugs = set(node.get('match_slugs', []))
    keywords = node.get('match_article_keywords', [])
    exclude_kws = node.get('exclude_article_keywords', [])
    article_slug = getattr(it, 'slug', '')
    basic = _item_slug(it) in slugs or (keywords and any(kw in article_slug for kw in keywords))
    if not basic:
        return False
    if exclude_kws and any(kw in article_slug for kw in exclude_kws):
        return False
    return True


def _count_node(node, all_items):
    """Set node['count'] = total essay count for this node (recursive for groups). Returns count."""
    if node.get('is_group') and node.get('subcategories'):
        total = sum(_count_node(child, all_items) for child in node['subcategories'])
        node['count'] = total
        return total
    count = sum(1 for it in all_items if _item_matches_node(it, node))
    node['count'] = count
    return count


def section_landing(request, key):
    import copy
    from topics.models import Article
    config = SECTION_CONFIG.get(key)
    if not config:
        raise Http404('Unknown section')

    active_topic_id = request.GET.get('topic')
    # Deep copy so we can mutate 'count' on nested nodes without touching SECTION_CONFIG
    subcategories = copy.deepcopy(config.get('subcategories', []))

    if config.get('is_books'):
        books = list(BookReview.objects.filter(published=True).select_related('category'))
        PINNED_FIRST = 'the-song-of-the-cell'
        books.sort(key=lambda b: b.slug != PINNED_FIRST)
        all_items = books
    else:
        articles = list(Article.objects.filter(
            published=True, pillar__slug__in=config['pillar_slugs']
        ).select_related('pillar'))
        posts = list(Post.objects.filter(
            published=True, category__slug__in=config['category_slugs']
        ).select_related('category'))
        all_items = articles + posts

    # Compute essay counts on every node in the tree (always, before filtering)
    for s in subcategories:
        _count_node(s, all_items)

    # Resolve active topic and its ancestor chain
    active_topic, ancestors = (None, [])
    if active_topic_id:
        active_topic, ancestors = _find_topic(subcategories, active_topic_id)

    # Determine chip_parent (deepest group "in view") and breadcrumb chain
    chip_parent = None
    breadcrumb_chain = []
    child_chips = []
    if active_topic:
        if active_topic.get('is_group'):
            chip_parent = active_topic
            chip_parent_ancestors = list(ancestors)
        elif ancestors:
            chip_parent = ancestors[-1]   # leaf's direct parent group
            chip_parent_ancestors = ancestors[:-1]
        else:
            chip_parent = None
            chip_parent_ancestors = []

        if chip_parent:
            child_chips = chip_parent.get('subcategories', [])
            # Breadcrumb only when chip_parent itself has ancestors (depth ≥ 2)
            if chip_parent_ancestors:
                breadcrumb_chain = chip_parent_ancestors + [chip_parent]

    ancestor_id_list = [a['id'] for a in ancestors]

    # Apply topic filter using leaf matching (supports match_slugs, match_article_keywords, exclude_article_keywords)
    if active_topic:
        def _leaves(node):
            if node.get('is_group') and node.get('subcategories'):
                result = []
                for child in node['subcategories']:
                    result.extend(_leaves(child))
                return result
            return [node]
        leaf_nodes = _leaves(active_topic)
        items = [it for it in all_items if any(_item_matches_node(it, leaf) for leaf in leaf_nodes)]
    else:
        items = all_items

    item_count = len(items)
    hero_item = items[0] if items else None
    grid_items = items[1:] if len(items) > 1 else []

    other_sections = [(k, v) for k, v in SECTION_CONFIG.items() if k != key]

    return render(request, 'blog/section_landing.html', {
        'key': key,
        'config': config,
        'subcategories': subcategories,
        'active_topic': active_topic,
        'ancestor_id_list': ancestor_id_list,
        'child_chips': child_chips,
        'chip_parent_id': chip_parent['id'] if chip_parent else '',
        'breadcrumb_chain': breadcrumb_chain,
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
    HEALTH_PILLARS = ['cancer', 'species-appropriate-diet', 'cancer-metabolic-health', 'carnivore-diet', 'autoimmune-disease', 'biology']
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
    from topics.models import Article
    profile = Profile.objects.first()
    essays_this_year = Article.objects.filter(published=True).count() + Post.objects.filter(published=True).count()
    sections = SECTION_CONFIG  # for masthead
    return render(request, 'blog/about.html', {
        'profile': profile,
        'sections': sections,
        'essays_this_year': essays_this_year,
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
