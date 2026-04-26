from django import forms
from .models import Comment, Subscriber


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'style': 'width:100%;padding:0.6rem 1rem;border:1px solid var(--warm-border);border-radius:8px;background:var(--warm-surface);color:var(--warm-text);font-size:0.95rem;outline:none;'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email (not published)',
                'style': 'width:100%;padding:0.6rem 1rem;border:1px solid var(--warm-border);border-radius:8px;background:var(--warm-surface);color:var(--warm-text);font-size:0.95rem;outline:none;'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts...',
                'rows': 4,
                'style': 'width:100%;padding:0.6rem 1rem;border:1px solid var(--warm-border);border-radius:8px;background:var(--warm-surface);color:var(--warm-text);font-size:0.95rem;outline:none;resize:vertical;'
            }),
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'style': 'flex:1;padding:0.6rem 1rem;border:1px solid var(--warm-border);border-radius:2rem 0 0 2rem;background:var(--warm-surface);color:var(--warm-text);font-size:0.92rem;outline:none;',
            }),
        }