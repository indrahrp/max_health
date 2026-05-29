from django.db import migrations
import re

NEW_FIGURE = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/depression-hpa-serotonin.png" '
    'alt="Depression: HPA Axis and Serotonin Depletion to Metabolic Recovery — a 3-stage journey" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)


def replace_illustration(apps, schema_editor):
    Article = apps.get_model("topics", "Article")
    # Filter by both pillar AND slug. Pillar-only .get() crashes with
    # MultipleObjectsReturned now that this pillar holds many articles.
    # Migration 0019 re-applies this targeted by slug, so it's safe if this is a no-op.
    article = Article.objects.filter(
        pillar__slug="physiological-origin",
        slug="depression-metabolic-physiological-origin",
    ).first()
    if not article:
        return
    article.content = re.sub(
        r'<figure[^>]*>.*?</figure>',
        NEW_FIGURE,
        article.content,
        count=1,
        flags=re.DOTALL,
    )
    article.save()


def reverse_illustration(apps, schema_editor):
    pass  # not reversing a multi-KB SVG back


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0016_alphafold_amino_acid_table"),
    ]

    operations = [
        migrations.RunPython(replace_illustration, reverse_illustration),
    ]
