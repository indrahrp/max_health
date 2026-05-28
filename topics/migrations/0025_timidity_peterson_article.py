from django.db import migrations
from topics.management.commands.load_timidity_peterson_article import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0024_exhibitionism_simplify'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
