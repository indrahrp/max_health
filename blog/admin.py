from django.contrib import admin
from .models import Post, Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'published', 'created_at']
    list_filter = ['published', 'tag']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']