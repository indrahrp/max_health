from django.db import migrations


def restore_life_of_a_cell(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar, _ = Pillar.objects.get_or_create(
        slug='life-of-a-cell',
        defaults={
            'name': 'Life of a Cell',
            'description': (
                'How cells — the fundamental units of life — arise, specialize, renew, and fail. '
                'Exploring stem cell biology, cellular aging, gene editing, and the frontier of cellular medicine.'
            ),
            'icon': '🧬',
            'color': 'blue',
            'order': 7,
        },
    )

    # Move stem cell article into this pillar
    Article.objects.filter(slug='stem-cells-how-they-arise').update(pillar=pillar)


def reverse_restore(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')
    biology = Pillar.objects.filter(slug='biology').first()
    if biology:
        Article.objects.filter(slug='stem-cells-how-they-arise').update(pillar=biology)
    Pillar.objects.filter(slug='life-of-a-cell').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0008_stemcell_tag_life_of_a_cell'),
    ]

    operations = [
        migrations.RunPython(restore_life_of_a_cell, reverse_restore),
    ]
