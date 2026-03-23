from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Project, Category, Tag, BookReview


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


from .models import Post, Project, Category, Tag, BookReview, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'location']