from django.db import migrations
from topics.management.commands.load_peterson_evolved_thinking import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0043_existentialism_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
