from django.contrib import admin
from .models import Post, Project, Category, Tag, BookReview

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'rating', 'recommended', 'published', 'created_at']
    list_filter = ['published', 'recommended', 'rating', 'category']
    search_fields = ['title', 'author', 'review_content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'recommended']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'published', 'created_at']
    list_filter = ['published', 'featured', 'category', 'tags']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'featured']
    filter_horizontal = ['tags']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']