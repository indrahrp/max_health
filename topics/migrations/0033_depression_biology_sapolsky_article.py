from django.db import migrations
from topics.management.commands.load_depression_biology_sapolsky import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0032_psychedelics_pillar'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
