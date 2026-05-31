from django.db import migrations
from topics.management.commands.load_sauna_heat_shock_longevity import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0041_meaningful_life_peterson_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
