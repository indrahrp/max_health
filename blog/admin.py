import os
import anthropic
from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Project, Category, Tag, BookReview, Profile, Comment, Subscriber


def _ai_generate_summary(queryset, field):
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    updated = 0
    for obj in queryset:
        from django.utils.html import strip_tags
        text = strip_tags(getattr(obj, field, '') or '')[:4000]
        if not text.strip():
            continue
        msg = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=300,
            system='You are a concise summarizer. Return only a 2-3 sentence TL;DR summary.',
            messages=[{'role': 'user', 'content': f'Summarize this:\n\n{text}'}],
        )
        obj.ai_summary = msg.content[0].text
        obj.save(update_fields=['ai_summary'])
        updated += 1
    return updated


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
    actions = ['generate_ai_summary']

    def generate_ai_summary(self, request, queryset):
        n = _ai_generate_summary(queryset, 'content')
        self.message_user(request, f'Generated AI summary for {n} post(s).')
    generate_ai_summary.short_description = 'Generate AI TL;DR summary'


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at', 'approved', 'has_reply']
    list_filter = ['approved', 'created_at']
    search_fields = ['name', 'email', 'body']
    list_editable = ['approved']
    readonly_fields = ['name', 'email', 'body', 'created_at', 'post']
    fields = ['post', 'name', 'email', 'body', 'created_at', 'approved', 'author_reply']
    actions = ['approve_comments']

    def has_reply(self, obj):
        return bool(obj.author_reply)
    has_reply.boolean = True
    has_reply.short_description = 'Replied'

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = 'Approve selected comments'

    def save_model(self, request, obj, form, change):
        if obj.author_reply and not obj.replied_at:
            obj.replied_at = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'confirmed']
    list_filter = ['confirmed']
    search_fields = ['email']
    readonly_fields = ['email', 'created_at']
