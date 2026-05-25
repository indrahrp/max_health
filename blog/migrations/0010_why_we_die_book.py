import urllib.request
from django.db import migrations


REVIEW_CONTENT = '''<p class="lead">Venki Ramakrishnan won the Nobel Prize in Chemistry for working out the atomic structure of the ribosome — the cell's protein factory. In <em>Why We Die</em>, he turns the same methodical mind toward ageing itself: what it is, why evolution produced it, and whether the emerging longevity industry might one day change it. The result is the clearest scientific account of ageing written for a general reader.</p>

<h2>What the Book Is About</h2>

<p>Ramakrishnan begins where the question actually starts: evolution. Ageing is not a flaw in the design of life — it is a consequence of it. Natural selection optimises for reproduction, not longevity. Once an organism has reproduced, evolution loses interest in it. This is not a melancholy observation but a scientific one, and understanding it reframes everything that follows.</p>

<p>From there the book descends into the cellular and molecular details. What actually goes wrong inside a cell as it ages? Ramakrishnan covers the accumulation of DNA damage, the shortening of telomeres, the decline of the proteome (the collection of proteins the cell maintains), the dysfunction of mitochondria, and the phenomenon of senescence — cells that stop dividing but refuse to die, secreting inflammatory signals that damage surrounding tissue.</p>

<p>Each mechanism is explained from scratch, with real care for the non-specialist reader. Ramakrishnan has the gift of the scientist who has genuinely thought something through rather than just repeated a textbook explanation.</p>

<h2>On the Longevity Industry</h2>

<p>The second half of the book engages critically with the current wave of longevity research and the companies built around it. Ramakrishnan is neither a booster nor a dismisser — he is a working scientist evaluating the evidence. On caloric restriction, on rapamycin, on senolytics (drugs that clear senescent cells), on reprogramming cells with Yamanaka factors, he asks the same question: what does the actual evidence show, not what do the investors hope?</p>

<p>His assessment is sober. Some interventions show genuine promise in model organisms — worms, flies, mice. Almost all have failed to translate to humans in the ways hoped. The human ageing process is vastly more complex than a nematode's, and decades of over-promised results have made the field prone to both hype and backlash.</p>

<p>Ramakrishnan is also honest about a question the longevity industry rarely confronts directly: what kind of life would extreme longevity actually produce? Not just for the individual but for society, for the young, for the planet? These are not anti-science questions. They are the questions a scientist should ask before declaring a goal worth pursuing at civilisational scale.</p>

<h2>The Writing</h2>

<p>The prose is precise and calm — the voice of someone who has spent a career writing for peer reviewers and has now chosen to write for a broader audience without compromising on accuracy. The explanations are earned, not borrowed. When Ramakrishnan says something is uncertain, you believe him, because you have seen him be precise about what is known.</p>

<p>This is the rare popular science book that genuinely teaches. Not just what researchers think but why they think it, what the evidence looks like, and where the honest uncertainty lies.</p>

<h2>Who Should Read It</h2>

<p>Anyone who wants a reliable, scientifically grounded account of why we age and what can realistically be done about it. Also anyone interested in the biology of the cell, in how evolution shapes life histories, or in how to think critically about the claims of the longevity industry. Ramakrishnan does not write for readers who want to be told that immortality is around the corner. He writes for readers who want to understand what is actually true.</p>'''


def add_book(apps, schema_editor):
    BookReview = apps.get_model('blog', 'BookReview')
    Category = apps.get_model('blog', 'Category')

    cat, _ = Category.objects.get_or_create(
        slug='ai',
        defaults={'name': 'AI'},
    )

    book, created = BookReview.objects.get_or_create(
        slug='why-we-die-the-new-science-of-ageing-and-the-quest',
        defaults={
            'title': 'Why We Die: The New Science of Ageing and the Quest for Immortality',
            'author': 'Venki Ramakrishnan',
            'category': cat,
            'summary': (
                'A Nobel Prize-winning biologist turns his eye on the science of ageing — '
                'why we age, why we die, and whether biology might one day change the answer. '
                'Clear-eyed, rigorous, and unexpectedly moving.'
            ),
            'review_content': REVIEW_CONTENT,
            'rating': 5,
            'status': 'read',
            'buy_link': 'https://www.amazon.com/Why-We-Die-Science-Immortality/dp/0063113287/',
            'recommended': True,
            'published': True,
        },
    )

    if created or not book.cover_image:
        _try_attach_cover(book)


def _try_attach_cover(book):
    from django.core.files.base import ContentFile
    slug = book.slug
    cover_url = 'https://images-na.ssl-images-amazon.com/images/P/0063113287.01.L.jpg'
    try:
        req = urllib.request.Request(cover_url, headers={'User-Agent': 'Mozilla/5.0 Cogitra/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) > 5000:
            book.cover_image.save(f'{slug}.jpg', ContentFile(data), save=True)
    except Exception:
        pass


def remove_book(apps, schema_editor):
    BookReview = apps.get_model('blog', 'BookReview')
    BookReview.objects.filter(slug='why-we-die-the-new-science-of-ageing-and-the-quest').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_why_machines_learn_book'),
    ]

    operations = [
        migrations.RunPython(add_book, remove_book),
    ]
