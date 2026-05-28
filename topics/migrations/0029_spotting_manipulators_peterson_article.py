from django.db import migrations
from topics.management.commands.load_spotting_manipulators_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0028_enduring_darkness_add_friedrich_painting'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
