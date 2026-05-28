from django.db import migrations
from topics.management.commands.load_narcissism_neuroticism_article import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0021_eating_disorders_replace_illustration'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
