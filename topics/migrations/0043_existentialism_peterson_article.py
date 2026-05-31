from django.db import migrations
from topics.management.commands.load_existentialism_peterson import create_article, reverse_article


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0042_sauna_heat_shock_longevity_article'),
    ]

    operations = [
        migrations.RunPython(create_article, reverse_article),
    ]
