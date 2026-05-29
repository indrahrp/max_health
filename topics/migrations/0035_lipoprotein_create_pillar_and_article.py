from django.db import migrations
from topics.management.commands.load_lipoprotein_cascade import SLUG, TITLE, SUMMARY, CONTENT


def create_pillar_and_article(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar, _ = Pillar.objects.get_or_create(
        slug='carnivore-diet',
        defaults={
            'name': 'Carnivore Diet',
            'description': 'The science behind carnivore, ketogenic, and animal-based diets.',
        },
    )

    if Article.objects.filter(slug=SLUG).exists():
        return

    Article.objects.create(
        slug=SLUG,
        title=TITLE,
        summary=SUMMARY,
        content=CONTENT,
        pillar=pillar,
        order=50,
        published=True,
    )


def reverse_pillar_and_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0034_lipoprotein_cascade_article'),
    ]

    operations = [
        migrations.RunPython(create_pillar_and_article, reverse_pillar_and_article),
    ]
