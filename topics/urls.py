from django.urls import path
from . import views

app_name = 'topics'

urlpatterns = [
    path('', views.topics_home, name='topics_home'),
    path('search/', views.topics_search, name='topics_search'),
    path('<slug:slug>/', views.pillar_detail, name='pillar_detail'),
    path('<slug:pillar_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
]