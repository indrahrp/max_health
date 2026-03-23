from django.shortcuts import render, get_object_or_404
from .models import Post, Project, Category


def home(request):
    from .models import BookReview
    recent_posts = Post.objects.filter(published=True)[:3]
    post_count = Post.objects.filter(published=True).count()
    book_count = BookReview.objects.filter(published=True).count()
    return render(request, 'blog/home.html', {
        'recent_posts': recent_posts,
        'post_count': post_count,
        'book_count': book_count,
    })


def about(request):
    interests = [
        'Carnivore diet',
        'Chronic disease prevention',
        'Metabolic health',
        'Ancestral nutrition',
        'Inflammation',
        'Gut health',
    ]
    return render(request, 'blog/about.html', {'interests': interests})


def blog_list(request):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    selected = request.GET.get('category')

    if selected:
        posts = posts.filter(category__slug=selected)

    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'selected': selected,
    })


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    related = Post.objects.filter(
        category=post.category,
        published=True
    ).exclude(id=post.id)[:3]
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'related': related,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, published=True)
    categories = Category.objects.all()
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'selected': slug,
        'category': category,
    })


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'blog/projects.html', {'all_projects': all_projects})


def book_list(request):
    from .models import BookReview
    books = BookReview.objects.filter(published=True)
    return render(request, 'blog/book_list.html', {'books': books})


def book_detail(request, slug):
    from .models import BookReview
    book = get_object_or_404(BookReview, slug=slug, published=True)
    return render(request, 'blog/book_detail.html', {'book': book})