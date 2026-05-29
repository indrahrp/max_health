from django.db import migrations


def create_physiological_origin_pillar(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar, _ = Pillar.objects.get_or_create(
        slug='physiological-origin',
        defaults={
            'name': 'Mental Illness · Physiological Origin',
            'description': (
                'The metabolic, inflammatory, and structural roots of mental illness — '
                'mitochondria, gut, sleep, hormones, and the growing evidence for '
                'dietary and metabolic interventions.'
            ),
            'icon': '🧠',
            'color': 'teal',
            'order': 9,
        },
    )

    Article.objects.filter(
        slug='mental-illness-physiological-origin-stories'
    ).update(pillar=pillar)


def reverse_physiological_origin_pillar(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    mental_health = Pillar.objects.filter(slug='mental-health').first()
    if mental_health:
        Article.objects.filter(
            slug='mental-illness-physiological-origin-stories'
        ).update(pillar=mental_health)

    Pillar.objects.filter(slug='physiological-origin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_mental_illness_keto_update'),
    ]

    operations = [
        migrations.RunPython(
            create_physiological_origin_pillar,
            reverse_physiological_origin_pillar,
        ),
    ]
