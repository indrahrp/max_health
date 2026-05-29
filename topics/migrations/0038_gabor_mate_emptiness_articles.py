from django.db import migrations
from topics.management.commands.load_why_you_feel_empty_gabor_mate import (
    create_article as create_empty, reverse_article as reverse_empty
)
from topics.management.commands.load_authenticity_attachment_gabor_mate import (
    create_article as create_auth, reverse_article as reverse_auth
)


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0037_sexual_orientation_add_illustration'),
    ]

    operations = [
        migrations.RunPython(create_empty, reverse_empty),
        migrations.RunPython(create_auth, reverse_auth),
    ]
