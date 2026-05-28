from django.db import migrations
from topics.management.commands.load_dostoevsky_peterson_article import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0025_timidity_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
