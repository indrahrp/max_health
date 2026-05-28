from django.db import migrations

SLUG = 'enduring-lifes-darkest-moments-peterson'

FIGURE_HTML = '''
<figure style="margin:2em 0 2.5em;">
<img src="/static/blog/illustrations/wanderer-above-sea-of-fog-friedrich.jpg"
  alt="Caspar David Friedrich — Wanderer above the Sea of Fog (1818). A solitary figure stands on a rocky peak, back to the viewer, gazing out over a sea of clouds and distant mountains."
  style="width:100%;border-radius:12px;display:block;">
<figcaption style="margin-top:0.7em;font-size:0.88em;color:#6a7080;font-style:italic;text-align:center;">
  Caspar David Friedrich, <em>Wanderer above the Sea of Fog</em> (1818). Public domain, Kunsthalle Hamburg.
  The figure has climbed above the fog — not past it. Below is still chaos. The upward aim is not an escape from difficulty; it is a vantage point from which to face it.
</figcaption>
</figure>'''

# Insert after the third paragraph — after "The question is not how to avoid the hard parts."
ANCHOR = '<h2>Why meaning is not optional</h2>'


def add_painting(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    if 'wanderer-above-sea-of-fog' in article.content:
        return  # already inserted
    if ANCHOR not in article.content:
        return  # anchor not found, skip safely
    article.content = article.content.replace(ANCHOR, FIGURE_HTML + '\n' + ANCHOR, 1)
    article.save(update_fields=['content'])


def remove_painting(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    article = Article.objects.filter(slug=SLUG).first()
    if not article:
        return
    article.content = article.content.replace(FIGURE_HTML + '\n' + ANCHOR, ANCHOR, 1)
    article.save(update_fields=['content'])


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0027_enduring_darkness_peterson_article'),
    ]

    operations = [
        migrations.RunPython(add_painting, remove_painting),
    ]
