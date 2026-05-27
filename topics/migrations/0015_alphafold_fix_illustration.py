from django.db import migrations


ILLUSTRATION = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/alphafold-protein-folding.svg" '
    'alt="AlphaFold: from amino acid sequence to 3D protein structure" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)


def fix_illustration(apps, schema_editor):
    Article = apps.get_model("topics", "Article")
    for slug in ["alphafold-protein-folding-ai", "alphafold-protein-folding-ai-ai"]:
        try:
            article = Article.objects.get(slug=slug)
            # Replace the inline SVG block (everything between <figure and </figure>) with the img ref
            import re
            article.content = re.sub(
                r'<figure[^>]*>\s*<svg[\s\S]*?</svg>\s*</figure>',
                ILLUSTRATION,
                article.content,
                count=1,
            )
            article.save()
        except Article.DoesNotExist:
            pass


def reverse_fix(apps, schema_editor):
    pass  # no need to reverse illustration swap


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0014_alphafold_article"),
    ]

    operations = [
        migrations.RunPython(fix_illustration, reverse_fix),
    ]
