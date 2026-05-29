from django.db import migrations

SLUG = 'sapolsky-sexual-orientation-limbic-wiring'
IMG_SRC = 'https://res.cloudinary.com/dxmrrtzha/image/upload/v1780083755/cogitra/sapolsky-sexual-orientation-limbic-wiring.jpg'
ALT = 'Limbic system diagram showing hypothalamus, INAH-3 nucleus, amygdala, hippocampus and thalamus; INAH-3 size comparison by orientation; prenatal androgen developmental mechanism'

FIGURE = f'<figure style="margin:1.5em 0 2.5em;">\n<img src="{IMG_SRC}" alt="{ALT}" style="width:100%;border-radius:16px;display:block;">\n</figure>\n\n'


def add_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    if IMG_SRC in article.content:
        return
    article.content = FIGURE + article.content
    article.save(update_fields=['content'])


def remove_illustration(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    article.content = article.content.replace(FIGURE, '', 1)
    article.save(update_fields=['content'])


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0036_lipoprotein_move_to_cholesterol_pillar'),
    ]

    operations = [
        migrations.RunPython(add_illustration, remove_illustration),
    ]
