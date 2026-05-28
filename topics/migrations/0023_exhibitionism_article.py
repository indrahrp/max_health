from django.db import migrations
from topics.management.commands.load_exhibitionism_article import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0022_narcissism_neuroticism_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
