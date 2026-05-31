from django.db import migrations
from topics.management.commands.load_meaningful_life_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0040_posture_body_language_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
