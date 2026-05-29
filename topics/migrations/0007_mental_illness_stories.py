from django.db import migrations
from topics.management.commands.load_mental_illness_stories import (
    create_mental_illness_stories,
    reverse_mental_illness_stories,
)


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0006_stemcell_article"),
    ]

    operations = [
        migrations.RunPython(
            create_mental_illness_stories,
            reverse_mental_illness_stories,
        ),
    ]
