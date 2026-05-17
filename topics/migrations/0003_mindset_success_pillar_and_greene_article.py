from django.db import migrations


def create_pillar_and_article(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')

    pillar, _ = Pillar.objects.get_or_create(
        slug='mindset-success',
        defaults={
            'name': 'Mindset & Success',
            'description': (
                "Frameworks, philosophies, and strategies from history's most powerful thinkers "
                "on how to master yourself, develop power, and build a meaningful life."
            ),
            'icon': '🧠',
            'color': 'indigo',
            'order': 4,
        }
    )

    if not Article.objects.filter(slug='robert-greene-laws-of-success').exists():
        Article.objects.create(
            title="Robert Greene's Laws of Success: How to Master Your Life",
            slug='robert-greene-laws-of-success',
            summary=(
                "Six timeless principles drawn from Robert Greene's body of work — Mastery, "
                "The 48 Laws of Power, and The Laws of Human Nature — distilled into an actionable "
                "framework for building a meaningful, powerful life."
            ),
            content="""<h2>Introduction</h2>
<p>Robert Greene has spent his life studying power, seduction, war, and human nature — reading thousands of historical biographies so you do not have to. His six major books distil timeless laws drawn from Caesar, Napoleon, Leonardo da Vinci, 50 Cent, and hundreds of others into a single, uncomfortable truth: <strong>success is not accidental. It is a craft, and it can be learned.</strong></p>

<blockquote style="border-left:4px solid #6366f1;padding:1rem 1.5rem;margin:1.5rem 0;background:#f5f3ff;border-radius:0 8px 8px 0;">
<em>"The most important skill in life is not intelligence or talent. It is the ability to endure — to keep going when it would be easier to quit." — Robert Greene</em>
</blockquote>

<h2>1. Master Your Craft Before Everything Else</h2>
<p>In <em>Mastery</em> (2012), Greene argues that every person has a unique calling — a <strong>Life's Task</strong> — hidden in their deepest interests and inclinations. The path to success begins with identifying this calling early and committing to a decade-long apprenticeship in it.</p>
<ul>
  <li><strong>Choose depth over breadth.</strong> Resist the modern temptation to jump between skills. Pick the domain that resonates most deeply and go 10,000 hours in.</li>
  <li><strong>Seek a master-apprentice relationship.</strong> The fastest learning happens when you are near someone far better than you. Observe, absorb, and eventually surpass them.</li>
  <li><strong>Embrace the painful phase.</strong> Every master passes through a period of feeling incompetent. That discomfort is not a signal to quit — it is the signal that you are growing.</li>
</ul>

<h2>2. Understand Power Without Apology</h2>
<p>Greene's <em>The 48 Laws of Power</em> (1998) is not a manual for manipulation. It is a field guide for recognising the power games that already surround you so you can navigate them consciously rather than naively.</p>
<ul>
  <li><strong>Law 1 — Never outshine the master.</strong> Make those above you feel comfortably superior. When the time is right, you will have earned enough trust to act independently.</li>
  <li><strong>Law 4 — Always say less than necessary.</strong> Words are currency. Spend them sparingly. Silence creates gravity and forces others to fill the vacuum.</li>
  <li><strong>Law 29 — Plan all the way to the end.</strong> Most people plan two steps ahead. The strategist plans to the finish line and works backwards, eliminating surprises before they occur.</li>
  <li><strong>Law 48 — Assume formlessness.</strong> Rigid strategies are brittle. Adapt your form to circumstances as water adapts to its container.</li>
</ul>

<h2>3. Develop Emotional Self-Mastery</h2>
<p>In <em>The Laws of Human Nature</em> (2018) — arguably his most mature work — Greene argues that the greatest obstacle to success is not external competition. It is your own emotional reactivity.</p>

<blockquote style="border-left:4px solid #6366f1;padding:1rem 1.5rem;margin:1.5rem 0;background:#f5f3ff;border-radius:0 8px 8px 0;">
<em>"The most dangerous people are those unaware of their own shadow — the dark, repressed side of the personality that leaks out in destructive behaviour." — Robert Greene</em>
</blockquote>

<p>His framework for emotional mastery has three steps:</p>
<ol>
  <li><strong>Observe yourself as a third party.</strong> When emotions run high, mentally step back and watch your reaction as if watching a stranger. This tiny gap is where freedom lives.</li>
  <li><strong>Trace the root of your triggers.</strong> Recurring emotional patterns almost always trace to childhood wounds or deep insecurities. Name them. Sunlight is the best disinfectant.</li>
  <li><strong>Convert negative energy into focused work.</strong> Greene calls this <em>sublimation</em> — channelling frustration, envy, or rage into productive output rather than reactive behaviour.</li>
</ol>

<h2>4. Read People Better Than They Read Themselves</h2>
<p>Human nature is consistent across centuries. Greene draws on Stoic philosophy, Jungian psychology, and evolutionary biology to map the dominant character types you will encounter:</p>
<ul>
  <li><strong>The Envious Type</strong> — disguises criticism as concern. Keep your achievements quiet around them.</li>
  <li><strong>The Passive Aggressor</strong> — indirect hostility masked as helpfulness. Name the pattern calmly and watch it dissolve.</li>
  <li><strong>The Charmer</strong> — all warmth, no substance. Enjoy the energy; do not bet your future on them.</li>
</ul>
<p>The skill of reading people is Greene's highest-order success tool. When you understand what drives those around you — their insecurities, their deep desires, their character type — you can collaborate more effectively, avoid energy vampires, and identify genuine allies.</p>

<h2>5. Build a Daily Practice Around Deep Work</h2>
<p>Greene's biographical research consistently shows that history's most effective people shared one habit: they protected long, uninterrupted blocks of focused work as non-negotiable.</p>
<ul>
  <li>Darwin walked the same gravel path every morning for uninterrupted thinking time.</li>
  <li>Einstein played violin between sessions of pure theoretical work to reset his mind.</li>
  <li>Leonardo da Vinci filled thousands of notebook pages — not to publish, but to train his eye and hand to see more precisely than anyone around him.</li>
</ul>
<p>The modern equivalent: <strong>block two to four hours each morning for your most demanding creative or strategic work</strong>, before the world demands your attention. Treat everything else as administration.</p>

<h2>6. Reverse-Engineer Your Ideal Future Self</h2>
<p>One of Greene's most practical frameworks — drawn from <em>Mastery</em> — is the <strong>primal inclination signal</strong>. Instead of asking "what should I do with my life?", ask:</p>
<ul>
  <li>What activity made time disappear when I was between eight and fourteen years old?</li>
  <li>What subject do I return to compulsively, even without external reward?</li>
  <li>What kind of work would I do for free, just to get better at it?</li>
</ul>
<p>The answers form the outline of your Life's Task. Success, in Greene's framework, is not about money or status — it is about <strong>closing the gap between who you are and who you were built to become</strong>.</p>

<h2>Key Takeaways</h2>
<ul>
  <li>Success is a craft with learnable laws, not a lottery.</li>
  <li>Identify your Life's Task and commit to a decade of deliberate practice.</li>
  <li>Study power dynamics so you can navigate them — not exploit them blindly.</li>
  <li>Master your emotions before trying to influence anyone else.</li>
  <li>Protect deep-work time as the engine of all long-term output.</li>
  <li>Let your primal inclinations, not social pressure, define your direction.</li>
</ul>""",
            pillar=pillar,
            order=1,
            published=True,
        )


def remove_pillar_and_article(apps, schema_editor):
    Pillar = apps.get_model('topics', 'Pillar')
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug='robert-greene-laws-of-success').delete()
    Pillar.objects.filter(slug='mindset-success').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_article_ai_summary'),
    ]

    operations = [
        migrations.RunPython(create_pillar_and_article, remove_pillar_and_article),
    ]
