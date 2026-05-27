from django.db import migrations
import re

DEPRESSION_FIGURE = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/depression-hpa-serotonin.png" '
    'alt="Depression: HPA Axis and Serotonin Depletion to Metabolic Recovery — a 3-stage journey" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)

BIPOLAR_FIGURE = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/bipolar-mitochondrial-origin.png" '
    'alt="Bipolar Disorder: Mitochondrial Metabolic Origin — energy dysregulation drives mood extremes" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)

REPLACEMENTS = [
    ('depression-metabolic-physiological-origin', DEPRESSION_FIGURE),
    ('bipolar-disorder-mitochondrial-metabolic-origin', BIPOLAR_FIGURE),
]


def fix_illustrations(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    for slug, new_figure in REPLACEMENTS:
        try:
            article = Article.objects.get(slug=slug)
            article.content = re.sub(
                r'<figure[^>]*>.*?</figure>',
                new_figure,
                article.content,
                count=1,
                flags=re.DOTALL,
            )
            article.save()
        except Article.DoesNotExist:
            pass


def reverse_fix(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0018_bipolar_replace_illustration'),
    ]

    operations = [
        migrations.RunPython(fix_illustrations, reverse_fix),
    ]
