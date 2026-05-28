from django.db import migrations

SLUG = 'repressing-feelings-makes-them-stronger-peterson'
OLD_SRC = '/static/blog/illustrations/repressing-feelings-peterson.svg'
NEW_SRC = 'https://res.cloudinary.com/dxmrrtzha/image/upload/v1779995345/cogitra/repressing-feelings-peterson-illustration.png'
NEW_ALT = 'What you push down grows in the dark — suppressed vs expressed emotion infographic'


def replace_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    if NEW_SRC in article.content:
        return
    article.content = article.content.replace(OLD_SRC, NEW_SRC, 1)
    # Also update alt text
    old_alt = 'Two figures side by side: one with suppressed dark energy building to a breaking point inside them, one with that same energy expressed and flowing outward as calm light'
    article.content = article.content.replace(old_alt, NEW_ALT, 1)
    article.save(update_fields=['content'])


def reverse_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    article.content = article.content.replace(NEW_SRC, OLD_SRC, 1)
    article.content = article.content.replace(NEW_ALT, 'Two figures side by side: one with suppressed dark energy building to a breaking point inside them, one with that same energy expressed and flowing outward as calm light', 1)
    article.save(update_fields=['content'])


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0030_repressing_feelings_peterson_article'),
    ]

    operations = [
        migrations.RunPython(replace_illustration, reverse_illustration),
    ]
