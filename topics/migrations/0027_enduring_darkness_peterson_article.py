from django.db import migrations
from topics.management.commands.load_enduring_darkness_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0026_dostoevsky_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
