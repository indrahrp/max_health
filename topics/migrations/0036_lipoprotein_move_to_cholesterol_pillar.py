from django.db import migrations

SLUG = 'lipoprotein-cascade-vldl-ldl-apob'


def move_to_cholesterol(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar, _ = Pillar.objects.get_or_create(
        slug='cholesterol',
        defaults={
            'name': 'The Cholesterol Debate',
            'description': 'Saturated fat, LDL, statins, ApoB, and the seventy-year argument that shaped cardiovascular medicine.',
        },
    )

    Article.objects.filter(slug=SLUG).update(pillar=pillar)


def reverse_move(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar = Pillar.objects.filter(slug='carnivore-diet').first()
    if pillar:
        Article.objects.filter(slug=SLUG).update(pillar=pillar)


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0035_lipoprotein_create_pillar_and_article'),
    ]

    operations = [
        migrations.RunPython(move_to_cholesterol, reverse_move),
    ]
