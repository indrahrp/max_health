from django.db import migrations
from topics.management.commands.load_cancer_metabolic_articles import (
    create_cancer_metabolic_articles,
    reverse_cancer_metabolic_articles,
)


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0004_autoimmune_disease_article"),
    ]

    operations = [
        migrations.RunPython(
            create_cancer_metabolic_articles,
            reverse_cancer_metabolic_articles,
        ),
    ]
