from django.db import migrations
from topics.management.commands.load_repressing_feelings_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0029_spotting_manipulators_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
