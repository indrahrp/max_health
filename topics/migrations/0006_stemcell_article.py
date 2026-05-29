from django.db import migrations
from topics.management.commands.load_life_of_a_cell_stemcell import (
    create_stemcell_article,
    reverse_stemcell_article,
)


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0005_cancer_metabolic_biology_articles"),
    ]

    operations = [
        migrations.RunPython(
            create_stemcell_article,
            reverse_stemcell_article,
        ),
    ]
