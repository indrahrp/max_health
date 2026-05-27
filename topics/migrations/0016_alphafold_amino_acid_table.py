from django.db import migrations

AMINO_ACID_FIGURE = (
    '\n\n<figure style="margin:2em 0 2.5em;">'
    '<img src="/static/blog/illustrations/amino-acids-table.svg" '
    'alt="The 20 amino acids — building blocks of every protein, grouped by chemical property" '
    'style="width:100%;border-radius:16px;display:block;">'
    '<figcaption style="margin-top:10px;font-family:var(--font-mono,monospace);font-size:11px;'
    'color:#475569;text-align:center;letter-spacing:0.06em;">'
    'THE 20 AMINO ACIDS · Single letter · Three letter · Chemical property'
    '</figcaption>'
    '</figure>\n\n'
)

# Insert just before the second h2 heading
INSERTION_MARKER = '<h2>The Man Who Chose the Problem on Purpose</h2>'


def add_amino_acid_table(apps, schema_editor):
    Article = apps.get_model("topics", "Article")
    for slug in ["alphafold-protein-folding-ai", "alphafold-protein-folding-ai-ai"]:
        try:
            article = Article.objects.get(slug=slug)
            if AMINO_ACID_FIGURE not in article.content:
                article.content = article.content.replace(
                    INSERTION_MARKER,
                    AMINO_ACID_FIGURE + INSERTION_MARKER,
                    1,
                )
                article.save()
        except Article.DoesNotExist:
            pass


def remove_amino_acid_table(apps, schema_editor):
    Article = apps.get_model("topics", "Article")
    for slug in ["alphafold-protein-folding-ai", "alphafold-protein-folding-ai-ai"]:
        try:
            article = Article.objects.get(slug=slug)
            article.content = article.content.replace(AMINO_ACID_FIGURE, "")
            article.save()
        except Article.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0015_alphafold_fix_illustration"),
    ]

    operations = [
        migrations.RunPython(add_amino_acid_table, remove_amino_acid_table),
    ]
