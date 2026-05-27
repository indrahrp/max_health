from django.db import migrations
import re

NEW_FIGURE = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/bipolar-mitochondrial-origin.png" '
    'alt="Bipolar Disorder: Mitochondrial Metabolic Origin — energy dysregulation drives mood extremes" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)

SLUG = 'bipolar-disorder-mitochondrial-metabolic-origin'


def replace_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Pillar = apps.get_model('topics', 'Pillar')

    try:
        article = Article.objects.get(slug=SLUG)
        # Replace first <figure>…</figure> (the SVG illustration)
        article.content = re.sub(
            r'<figure[^>]*>.*?</figure>',
            NEW_FIGURE,
            article.content,
            count=1,
            flags=re.DOTALL,
        )
        article.save()
        return
    except Article.DoesNotExist:
        pass

    # Article not in DB — create it with the new illustration via the management command
    from topics.management.commands.load_mental_illness_individual_articles import (
        BIPOLAR_CONTENT,
    )
    pillar = Pillar.objects.filter(slug='physiological-origin').first()
    if not pillar:
        return

    content_with_new_fig = re.sub(
        r'<figure[^>]*>.*?</figure>',
        NEW_FIGURE,
        BIPOLAR_CONTENT,
        count=1,
        flags=re.DOTALL,
    )

    Article.objects.create(
        slug=SLUG,
        title='Bipolar Disorder: Mitochondrial Dysfunction, Circadian Collapse, and the Metabolic Path to Stability',
        summary=(
            'Bipolar disorder is, at its metabolic core, a disease of unstable brain energy '
            'production. Five people who stabilised their mood cycling through ketogenic therapy '
            'targeting the mitochondrial dysfunction at the heart of the condition.'
        ),
        content=content_with_new_fig,
        pillar=pillar,
        order=4,
        published=True,
    )


def reverse_illustration(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0017_depression_replace_illustration'),
    ]

    operations = [
        migrations.RunPython(replace_illustration, reverse_illustration),
    ]
