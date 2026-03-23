from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Pillar, Article


@admin.register(Pillar)
class PillarAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon', 'color', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title', 'pillar', 'published', 'order', 'created_at']
    list_filter = ['published', 'pillar']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'order']
    filter_horizontal = ['related_posts']

