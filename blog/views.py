from django.shortcuts import render, get_object_or_404
from .models import Post, Project


def home(request):
    recent_posts = Post.objects.filter(published=True)[:3]
    return render(request, 'blog/home.html', {'recent_posts': recent_posts})


def about(request):
    return render(request, 'blog/about.html')


def blog_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/blog_detail.html', {'post': post})


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'blog/projects.html', {'all_projects': all_projects})