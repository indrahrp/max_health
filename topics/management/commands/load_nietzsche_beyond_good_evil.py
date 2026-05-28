from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR_SLUG = "mindset-success"

SVG_ILLUSTRATION = """<figure style="margin:1.5em 0 2.5em;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" style="width:100%;border-radius:16px;display:block;background:#07090f;">
  <defs>
    <radialGradient id="ng1" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#a78bfa" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ng2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
    <style>
      @keyframes hammer-swing {
        0%,100% { transform: rotate(-20deg) translate(0,0); }
        45% { transform: rotate(30deg) translate(4px, 8px); }
        50% { transform: rotate(32deg) translate(4px, 10px); }
        55% { transform: rotate(30deg) translate(4px, 8px); }
      }
      @keyframes crack-appear {
        0%,40% { opacity:0; stroke-dashoffset:80; }
        50%,100% { opacity:1; stroke-dashoffset:0; }
      }
      @keyframes word-fade {
        0%,100% { opacity:0.15; }
        50% { opacity:1; }
      }
      @keyframes glow-pulse {
        0%,100% { opacity:0.3; }
        50% { opacity:0.7; }
      }
      @keyframes float-up {
        0%,100% { transform: translateY(0); opacity:0.6; }
        50% { transform: translateY(-8px); opacity:1; }
      }
      .hammer-arm { transform-origin: 380px 180px; animation: hammer-swing 3s ease-in-out infinite; }
      .crack { stroke-dasharray:80; animation: crack-appear 3s ease-in-out infinite; }
      .word1 { animation: word-fade 4s ease-in-out infinite; }
      .word2 { animation: word-fade 4s ease-in-out infinite; animation-delay:1s; }
      .word3 { animation: word-fade 4s ease-in-out infinite; animation-delay:2s; }
      .word4 { animation: word-fade 4s ease-in-out infinite; animation-delay:3s; }
      .glow { animation: glow-pulse 3s ease-in-out infinite; }
      .float { animation: float-up 4s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="#07090f"/>
  <rect x="0" y="0" width="720" height="420" fill="url(#ng1)"/>

  <!-- Title -->
  <text x="360" y="38" text-anchor="middle" font-family="Georgia,serif" font-size="19" fill="#e2e8f0" font-weight="bold">Beyond Good and Evil</text>
  <text x="360" y="60" text-anchor="middle" font-family="Georgia,serif" font-size="13" fill="#94a3b8" font-style="italic">Nietzsche's bombs — through the eyes of Jordan Peterson</text>

  <!-- Left: Tablet / stone being shattered -->
  <g transform="translate(160,230)">
    <!-- stone tablet -->
    <rect x="-55" y="-90" width="110" height="130" rx="6" fill="#1e1b2e" stroke="#4c1d95" stroke-width="1.5"/>
    <text x="0" y="-58" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#7c3aed">GOOD</text>
    <line x1="-30" y1="-48" x2="30" y2="-48" stroke="#4c1d95" stroke-width="0.8"/>
    <text x="0" y="-34" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#7c3aed">EVIL</text>
    <line x1="-30" y1="-24" x2="30" y2="-24" stroke="#4c1d95" stroke-width="0.8"/>
    <text x="0" y="-10" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#6d28d9">TRUTH</text>
    <text x="0" y="8" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#6d28d9">VIRTUE</text>
    <text x="0" y="26" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#6d28d9">MORALITY</text>
    <!-- cracks -->
    <path d="M -10,-80 L 5,-20 L -5,40" stroke="#f59e0b" stroke-width="1.8" fill="none" class="crack"/>
    <path d="M 20,-70 L 10,10 L 25,40" stroke="#f59e0b" stroke-width="1.2" fill="none" class="crack" style="animation-delay:0.3s"/>
  </g>
  <text x="160" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7c3aed">Inherited Morality</text>
  <text x="160" y="332" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7c3aed">Being Questioned</text>

  <!-- Center: Hammer (philosophizing with a hammer) -->
  <g class="hammer-arm">
    <!-- handle -->
    <line x1="360" y1="150" x2="420" y2="240" stroke="#92400e" stroke-width="6" stroke-linecap="round"/>
    <!-- head -->
    <rect x="408" y="222" width="40" height="26" rx="4" fill="#78350f" stroke="#f59e0b" stroke-width="1.5" transform="rotate(30,428,235)"/>
  </g>
  <!-- impact glow -->
  <circle cx="222" cy="240" r="40" fill="url(#ng2)" class="glow"/>

  <!-- Right side: Fragments / new concepts emerging -->
  <g transform="translate(530,160)">
    <!-- fragment shards -->
    <polygon points="-30,-60 10,-40 -5,-10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.2" class="float" style="animation-delay:0s"/>
    <polygon points="20,-50 50,-30 30,-5" fill="#1e293b" stroke="#a78bfa" stroke-width="1.2" class="float" style="animation-delay:0.7s"/>
    <polygon points="-20,10 15,30 -10,55" fill="#1e293b" stroke="#a78bfa" stroke-width="1.2" class="float" style="animation-delay:1.4s"/>
    <polygon points="25,0 60,20 40,50" fill="#1e293b" stroke="#a78bfa" stroke-width="1.2" class="float" style="animation-delay:2.1s"/>
    <!-- labels on fragments -->
    <text x="-12" y="-30" font-family="Arial,sans-serif" font-size="9" fill="#c4b5fd" class="word1">Will to</text>
    <text x="-12" y="-19" font-family="Arial,sans-serif" font-size="9" fill="#c4b5fd" class="word1">Power</text>
    <text x="26" y="-18" font-family="Arial,sans-serif" font-size="9" fill="#c4b5fd" class="word2">Nihilism</text>
    <text x="-6" y="32" font-family="Arial,sans-serif" font-size="9" fill="#c4b5fd" class="word3">Übermensch</text>
    <text x="30" y="28" font-family="Arial,sans-serif" font-size="9" fill="#c4b5fd" class="word4">Revaluation</text>
  </g>
  <text x="540" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#a78bfa">New Values</text>
  <text x="540" y="332" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#a78bfa">Emerging</text>

  <!-- Dynamite aphorism boxes - bottom strip -->
  <g transform="translate(0,356)">
    <rect x="60" y="0" width="140" height="32" rx="5" fill="#1a0a2e" stroke="#7c3aed" stroke-width="1" opacity="0.8"/>
    <text x="130" y="13" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#c4b5fd" font-style="italic">"God is dead."</text>
    <text x="130" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">— Nietzsche</text>

    <rect x="220" y="0" width="160" height="32" rx="5" fill="#1a0a2e" stroke="#7c3aed" stroke-width="1" opacity="0.8"/>
    <text x="300" y="13" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#c4b5fd" font-style="italic">"He philosophized</text>
    <text x="300" y="25" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#c4b5fd" font-style="italic">with a hammer."</text>

    <rect x="400" y="0" width="260" height="32" rx="5" fill="#1a0a2e" stroke="#7c3aed" stroke-width="1" opacity="0.8"/>
    <text x="530" y="13" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#c4b5fd" font-style="italic">"Let the bombs go off in your brain."</text>
    <text x="530" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">— Peterson on Nietzsche</text>
  </g>
</svg>
</figure>"""

ARTICLE = {
    "title": "Nietzsche's Beyond Good and Evil: Peterson's Guide to the Bombs",
    "slug": "nietzsche-beyond-good-evil-peterson",
    "summary": (
        "Jordan Peterson has read Nietzsche's Beyond Good and Evil more carefully than almost "
        "anyone alive. His verdict: it's not a book you agree or disagree with — it's a sequence "
        "of philosophical explosives that, if you let them, detonate your assumptions about "
        "morality, truth, and what it means to be a serious person."
    ),
    "order": 1,
    "published": True,
    "content": f"""{SVG_ILLUSTRATION}

<p>Jordan Peterson keeps his most-read books on a specific shelf. The pages are double
dog-eared — a remarkable thought on one side, another on the facing page, so the whole
volume is nothing but creased corners. Beyond Good and Evil, he says, was one of those books.</p>

<p>"Every damn sentence is a thought. And a deep thought. Reading Beyond Good and Evil is
like just constantly being punched."</p>

<h2>A Man Who Could Write a Bomb</h2>

<p>Nietzsche was a very sick man for most of his productive life — migraines, failing eyesight,
collapsing health. He couldn't write for long stretches. So instead he would think, sometimes
for weeks, and then compress everything into a single aphorism. The result is a book that
reads less like an argument and more like a minefield.</p>

<p>Peterson quotes Nietzsche's own description of himself as an author — what he calls the most
arrogant statement he's ever heard anyone make:</p>

<blockquote>
<p>"I can write in a sentence what it takes other people a book to relate." And then he
topped it: "No — what other people can't even relate in a book."</p>
</blockquote>

<p>Peterson's reaction: "It's like arrogant, and then he topped it. This is a man who could
really write." The arrogance isn't vanity. It's accuracy. Nietzsche was writing for readers
who could keep up, and he had no interest in padding his ideas for those who couldn't.</p>

<h2>You Don't Agree With Nietzsche. You Let Him Detonate.</h2>

<p>Peterson is careful about how he frames his relationship to Nietzsche. You can't simply
say you agree with him — not because his ideas are wrong, but because they resist that kind
of consumption. Nietzsche wasn't trying to build a systematic philosophy. Beyond Good and Evil
is not a thesis with supporting arguments. It's a sequence of detonations.</p>

<p>"You can sure let the bombs go off in your brain if you read what he has to say."</p>

<p>That phrase — letting the bombs go off — captures something important about how Peterson
recommends engaging with difficult thinkers. You don't read Nietzsche to extract conclusions.
You read him to have your assumptions broken open. If nothing breaks, you weren't reading
carefully enough.</p>

<p>The punishment for careful reading is different: "You stumble across something you
understand, and then that breaks you apart because you understand it." The confusion is one
kind of punch. The comprehension is another. Both cost you something.</p>

<h2>What the Bombs Are Actually About</h2>

<p>The book's central provocation is its title. "Beyond Good and Evil" doesn't mean that good
and evil don't exist, or that morality is an illusion to be discarded. It means something harder:
that our inherited moral categories — the ones we absorbed from culture, religion, and childhood
without questioning them — may themselves be in need of examination.</p>

<p>Nietzsche's target, in Peterson's reading, is not Christianity itself but institutional
Christianity — specifically what he called <em>slave morality</em>: the idea that the oppressed
are inherently virtuous, that suffering confers nobility, that weakness is a kind of spiritual
credential. This, Nietzsche argued, inverts the actual relationship between suffering and
virtue. Suffering doesn't make you good. It makes you suffer.</p>

<p>"The slave morality idea — the idea that the oppressed are somehow virtuous — that's something
Nietzsche criticized as part and parcel of what was constructed in institutional Christianity,"
Peterson explains. But he's careful to distinguish this from Nietzsche being anti-Christian in
any simple sense: "It isn't obvious at all that Nietzsche was antithetically opposed to the
founding ideas. There are many places where he writes that indicate quite the contrary."</p>

<h2>The Death of God and the Nihilism That Followed</h2>

<p>The most famous bomb in the book isn't an aphorism — it's a declaration: <em>God is dead.</em>
But Peterson emphasizes what most people miss about this claim. Nietzsche is not celebrating.
He is diagnosing.</p>

<p>In the Will to Power, Nietzsche writes: "Radical nihilism is the conviction of an absolute
untenability of existence when it comes to the highest values. One recognizes this as a
consequence of the cultivation of truthfulness." In other words: the values of the
Enlightenment — reason, honesty, the pursuit of truth — when followed faithfully to their
conclusion, undercut the very framework that gave life its meaning. You can't hold science
and faith at the same time if you're truly honest, Nietzsche thought. But once you let the
faith go, the meaning goes with it, and nothing fills the space.</p>

<p>Peterson reads this as one of Nietzsche's most prophetic observations. The 20th century
confirmed it. The ideologies that rushed to fill the God-shaped vacuum — nationalism, Marxism,
fascism — produced the largest mass deaths in human history. Dostoevsky and Nietzsche both
predicted this, Peterson argues, before it happened.</p>

<h2>Philosophizing With a Hammer</h2>

<p>Nietzsche described his own method: <em>philosophizing with a hammer.</em> He wasn't just
criticizing bad ideas. He was breaking the structures that housed them — the assumptions so
fundamental they were invisible, the values so embedded they had stopped being felt as values
at all.</p>

<p>For Peterson, this is exactly why Nietzsche remains indispensable. Most philosophy teaches
you to think more clearly within your existing framework. Nietzsche forces you to question the
framework itself. That's more dangerous — and more necessary.</p>

<p>"I found him extraordinarily useful in training me how to think," Peterson says. Not in
telling him what to think, but in teaching him to notice what he was already thinking — the
implicit axioms, the unexamined assumptions, the values disguised as facts.</p>

<h2>How to Read It</h2>

<p>Peterson's practical advice: don't try to read it like a textbook. Don't look for the
argument. Dog-ear the pages that stop you. Sit with the aphorisms that don't make immediate
sense — because they usually don't fail to make sense for random reasons. They fail because
they're pointing at something your existing framework doesn't have a category for yet.</p>

<p>Then let it take time. Nietzsche thought for weeks to compress a year's worth of
philosophy into a paragraph. It's reasonable that the unpacking takes more than an afternoon.</p>

<p>The book will punch you. Some punches land because you're confused. Some land harder because
you're not.</p>

<p><em>Based on Jordan Peterson's discussions of Nietzsche across multiple YouTube lectures
and interviews, including conversations about Beyond Good and Evil, nihilism, slave morality,
and the death of God.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load Nietzsche Beyond Good and Evil (Peterson) article into mindset-success pillar"

    def handle(self, *args, **options):
        pillar = Pillar.objects.get(slug=PILLAR_SLUG)
        self.stdout.write(f"Pillar: {pillar.name}")

        article, created = Article.objects.get_or_create(
            slug=ARTICLE["slug"],
            defaults={**ARTICLE, "pillar": pillar},
        )
        if not created:
            article.title = ARTICLE["title"]
            article.summary = ARTICLE["summary"]
            article.pillar = pillar
            article.published = ARTICLE["published"]
            article.save(update_fields=["title", "summary", "pillar", "published"])
        action = "Created" if created else "Updated (content preserved)"
        self.stdout.write(f"{action} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
