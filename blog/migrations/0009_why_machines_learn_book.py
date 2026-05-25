import urllib.request
from django.db import migrations


REVIEW_CONTENT = '''<p class="lead">Most popular books about AI tell you what machine learning does. This one tells you why it works — by unpacking the mathematics that make neural networks, backpropagation, and transformers possible. It is one of the rare books that treats a curious reader as someone capable of handling real ideas.</p>

<h2>What the Book Is About</h2>

<p>Anil Ananthaswamy is a science journalist who spent years trying to understand the mathematics behind modern AI — not to become a machine learning engineer, but to genuinely understand what the field has built. <em>Why Machines Learn</em> is the result of that inquiry: a patient, methodical tour of the mathematical concepts that underpin machine learning, from the simplest perceptron to the transformer architecture that powers large language models.</p>

<p>The book covers gradient descent, the optimization algorithm that trains neural networks by nudging weights in the direction that reduces error. It explains backpropagation, the chain-rule calculus trick that makes training deep networks computationally feasible. It walks through activation functions, loss functions, and regularization. And it builds toward the attention mechanism at the core of transformers — the innovation that made GPT, BERT, and their successors possible.</p>

<h2>Who It Is For</h2>

<p>This is not a book for someone who wants to use AI tools without understanding them. Nor is it a textbook for someone learning to build systems. It sits in the middle: aimed at a reader who is intellectually serious, comfortable with the idea of equations, and wants to understand not just the what but the why and the how.</p>

<p>Ananthaswamy is unusually good at the art of the worked example. Abstract concepts — like why a loss function shaped like a bowl means gradient descent will always find the bottom — become intuitive when you see the geometry drawn out. The prose is precise without being cold.</p>

<h2>What Makes It Stand Out</h2>

<p>Most accessible AI books skip the mathematics entirely, using analogies that eventually break down. Most technical treatments assume a background in linear algebra and calculus that many readers do not have. Ananthaswamy threads this needle by building mathematical intuition gradually — showing why each idea was needed before introducing it, and always connecting the abstraction back to what it means for how a network learns.</p>

<p>The chapters on the history of neural networks are also unusually good. The field's long winters — the periods when funding dried up and researchers were marginalized — are told with genuine narrative momentum. The reader comes away understanding why the resurgence of deep learning in the 2010s was so dramatic: it resolved decades-old puzzles about how to train networks with many layers.</p>

<h2>A Note on Depth</h2>

<p>The book does not shy away from equations, though it explains each one before using it. Readers who are entirely unfamiliar with calculus may find some sections demanding. But Ananthaswamy is careful to provide geometric and physical intuitions alongside the algebra, so a motivated reader without a formal mathematics background can follow the thread even when the symbols become dense.</p>

<p>For anyone who has wondered what is actually happening inside a neural network — what "learning" means mathematically, what a weight is, why attention changed everything — this is the most accessible serious treatment currently available.</p>'''


def add_book(apps, schema_editor):
    BookReview = apps.get_model('blog', 'BookReview')
    Category = apps.get_model('blog', 'Category')

    cat, _ = Category.objects.get_or_create(
        slug='ai',
        defaults={'name': 'AI'},
    )

    book, created = BookReview.objects.get_or_create(
        slug='why-machines-learn-the-elegant-math-behind-modern',
        defaults={
            'title': 'Why Machines Learn: The Elegant Math Behind Modern AI',
            'author': 'Anil Ananthaswamy',
            'category': cat,
            'summary': (
                'A rigorous but accessible tour of the mathematics that makes AI work — '
                'from gradient descent and backpropagation to transformers — written for '
                'curious readers who want to understand not just what AI does but why it works.'
            ),
            'review_content': REVIEW_CONTENT,
            'rating': 5,
            'status': 'read',
            'buy_link': 'https://www.amazon.com/Why-Machines-Learn-Elegant-Behind-ebook/dp/B0CF1223R8/',
            'recommended': True,
            'published': True,
        },
    )

    if created or not book.cover_image:
        _try_attach_cover(book)


def _try_attach_cover(book):
    from django.core.files.base import ContentFile
    slug = book.slug
    cover_url = 'https://images-na.ssl-images-amazon.com/images/P/B0CF1223R8.01._LZZZZZZZ_.jpg'
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
    BookReview.objects.filter(slug='why-machines-learn-the-elegant-math-behind-modern').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_hinton_ai_posts'),
    ]

    operations = [
        migrations.RunPython(add_book, remove_book),
    ]
