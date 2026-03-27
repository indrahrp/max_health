from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Project, Category, Tag, BookReview
from .models import Post, Project, Category, Tag, BookReview, Profile
from .models import Comment



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title', 'category', 'featured', 'published', 'created_at']
    list_filter = ['published', 'featured', 'category', 'tags']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'featured']
    filter_horizontal = ['tags']


@admin.register(BookReview)
class BookReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('review_content',)
    list_display = ['title', 'author', 'status', 'rating', 'recommended', 'published', 'created_at']
    list_filter = ['published', 'recommended', 'status', 'rating', 'category']
    search_fields = ['title', 'author', 'review_content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published', 'recommended', 'status']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'location']

from .models import Post, Project, Category, Tag, BookReview, Profile, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    search_fields = ['name', 'email', 'body']
    list_editable = ['approved']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = 'Approve selected comments'