from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post, Project, Category, Tag, BookReview
from .forms import CommentForm, SubscribeForm


def home(request):
    recent_posts = Post.objects.filter(published=True)[:3]
    post_count = Post.objects.filter(published=True).count()
    book_count = BookReview.objects.filter(published=True).count()
    currently_reading = BookReview.objects.filter(published=True, status='reading').first()
    return render(request, 'blog/home.html', {
        'recent_posts': recent_posts,
        'post_count': post_count,
        'book_count': book_count,
        'currently_reading': currently_reading,
    })


def about(request):
    from .models import Profile
    profile = Profile.objects.first()
    interests = [
        'Carnivore diet',
        'Chronic disease prevention',
        'Metabolic health',
        'Ancestral nutrition',
        'Inflammation',
        'Gut health',
    ]
    return render(request, 'blog/about.html', {
        'profile': profile,
        'interests': interests,
    })


def blog_list(request):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    tags = Tag.objects.filter(posts__published=True).distinct()
    selected_cat = request.GET.get('category')
    selected_tag = request.GET.get('tag')

    if selected_cat:
        posts = posts.filter(category__slug=selected_cat)
    if selected_tag:
        posts = posts.filter(tags__slug=selected_tag)

    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'selected': selected_cat,
        'selected_tag': selected_tag,
    })


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

    return render(request, 'blog/blog_detail.html', {
        'post': post,
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
