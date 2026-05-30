from django.db import migrations
from topics.management.commands.load_posture_body_language_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0039_fertilization_replace_illustration'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
