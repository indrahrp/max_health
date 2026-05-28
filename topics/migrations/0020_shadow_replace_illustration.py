from django.db import migrations
import re

SLUG = 'integrating-your-shadow-peterson-greene'

NEW_FIGURE = (
    '<figure style="margin:1.5em 0 2.5em;">'
    '<img src="/static/blog/illustrations/shadow-peterson-greene.png" '
    'alt="Peterson · Greene on the Shadow: You don\'t amputate the dark half — you claim it" '
    'style="width:100%;border-radius:16px;display:block;">'
    '</figure>'
)


def replace_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    try:
        article = Article.objects.get(slug=SLUG)
        article.content = re.sub(
            r'<figure[^>]*>.*?</figure>',
            NEW_FIGURE,
            article.content,
            count=1,
            flags=re.DOTALL,
        )
        article.save()
    except Article.DoesNotExist:
        pass


def reverse_illustration(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0019_fix_illustration_slugs'),
    ]

    operations = [
        migrations.RunPython(replace_illustration, reverse_illustration),
    ]
