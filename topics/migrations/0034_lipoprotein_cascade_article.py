from django.db import migrations
from topics.management.commands.load_lipoprotein_cascade import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0033_depression_biology_sapolsky_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
