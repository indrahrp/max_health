from django.db import migrations
from topics.management.commands.load_alphafold_article import (
    create_alphafold_article,
    reverse_alphafold_article,
)


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0013_mental_illness_reorder_metabolic_thread_top"),
    ]

    operations = [
        migrations.RunPython(
            create_alphafold_article,
            reverse_alphafold_article,
        ),
    ]
