from django.db import migrations


def create_psychedelics_pillar(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Pillar.objects.get_or_create(
        slug='psychedelics',
        defaults={
            'name': 'Psychedelics',
            'description': (
                'Psilocybin, MDMA, ketamine, ayahuasca, and the renewed clinical '
                'research into psychedelic-assisted therapy for depression, PTSD, '
                'addiction, and end-of-life distress.'
            ),
            'order': 18,
        },
    )


def reverse(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Pillar.objects.filter(slug='psychedelics').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0031_repressing_feelings_replace_illustration'),
    ]

    operations = [
        migrations.RunPython(create_psychedelics_pillar, reverse),
    ]
