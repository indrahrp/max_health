from django.db import migrations

SLUG = 'ramakrishnan-fertilization-and-editing'
OLD_SRC = 'https://res.cloudinary.com/dxmrrtzha/image/upload/cogitra/ramakrishnan-fertilization-and-editing.svg'
NEW_SRC = 'https://res.cloudinary.com/dxmrrtzha/image/upload/v1780086554/cogitra/ramakrishnan-fertilization-and-editing.jpg'
OLD_ALT = 'Illustration: a sperm meeting and entering an ovum at the moment of fertilization'
NEW_ALT = 'Fertilization infographic: 5-step process from sperm approach to zygote formation, with zona pellucida, pronuclei fusion, and epigenetic clock reset'


def replace_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article or NEW_SRC in article.content:
        return
    article.content = article.content.replace(OLD_SRC, NEW_SRC, 1)
    article.content = article.content.replace(OLD_ALT, NEW_ALT, 1)
    article.save(update_fields=['content'])


def reverse_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    article.content = article.content.replace(NEW_SRC, OLD_SRC, 1)
    article.content = article.content.replace(NEW_ALT, OLD_ALT, 1)
    article.save(update_fields=['content'])


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0038_gabor_mate_emptiness_articles'),
    ]

    operations = [
        migrations.RunPython(replace_illustration, reverse_illustration),
    ]
