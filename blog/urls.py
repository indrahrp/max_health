from django.urls import path
from . import views
from . import ai_views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ai/', views.section_landing, {'key': 'ai'}, name='section_ai'),
    path('health/', views.section_landing, {'key': 'health'}, name='section_health'),
    path('mental/', views.section_landing, {'key': 'mental'}, name='section_mental'),
    path('biology/', views.section_landing, {'key': 'biology'}, name='section_biology'),
    path('mindset/', views.section_landing, {'key': 'mindset'}, name='section_mindset'),
    path('genetics/', views.section_landing, {'key': 'genetics'}, name='section_genetics'),
    path('longevity/', views.section_landing, {'key': 'longevity'}, name='section_longevity'),
    path('physics/', views.section_landing, {'key': 'physics'}, name='section_physics'),
    path('section/books/', views.section_landing, {'key': 'books'}, name='section_books'),
    path('archive/', views.blog_list, name='archive'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('books/', views.book_list, name='book_list'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/', views.search, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('ai/improve/', ai_views.improve_text, name='ai_improve'),
    path('ai/chat/', ai_views.health_chat, name='health_chat'),
]
