from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Neuroscience",
    "slug": "neuroscience",
    "description": (
        "How the brain works, what consciousness is, and what neuroscience reveals about "
        "memory, perception, emotion, and the nature of the self."
    ),
    "icon": "🧠",
    "color": "violet",
    "order": 11,
}

SVG_BRAIN_MIND = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diagram showing the brain as physical substrate and the mind as emergent experience, separated by the explanatory gap">
  <defs>
    <radialGradient id="brainGrad" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#1e1b4b" stop-opacity="0.6"/>
    </radialGradient>
    <radialGradient id="mindGrad" cx="60%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#1c1007" stop-opacity="0.5"/>
    </radialGradient>
    <filter id="glow-v">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-a">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <marker id="arr-gap" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#94a3b8"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="720" height="400" fill="#080c18" rx="16"/>

  <!-- Title -->
  <text x="360" y="32" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="15" fill="#f1f5f9" font-weight="700" letter-spacing="-0.3">Brain vs Mind: The Explanatory Gap</text>
  <text x="360" y="51" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">From David Eagleman · Inner Cosmos</text>

  <!-- ─── LEFT: BRAIN (physical) ─── -->
  <ellipse cx="185" cy="210" rx="130" ry="110" fill="url(#brainGrad)" stroke="#6366f1" stroke-width="1.5" opacity="0.85"/>

  <!-- Brain fold lines (decorative) -->
  <path d="M120,175 Q155,160 185,178 Q215,195 235,175" fill="none" stroke="#818cf8" stroke-width="1.5" opacity="0.6"/>
  <path d="M105,210 Q145,198 175,215 Q205,232 245,215" fill="none" stroke="#818cf8" stroke-width="1.5" opacity="0.5"/>
  <path d="M115,245 Q150,238 180,250 Q210,262 240,248" fill="none" stroke="#818cf8" stroke-width="1.5" opacity="0.4"/>
  <path d="M140,270 Q170,265 195,275 Q218,282 235,268" fill="none" stroke="#818cf8" stroke-width="1.2" opacity="0.35"/>

  <!-- Neuron dots -->
  <circle cx="155" cy="190" r="3" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="195" cy="178" r="2.5" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="220" cy="205" r="3" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="170" cy="225" r="2.5" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="205" cy="240" r="3" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="150" cy="248" r="2" fill="#a5b4fc" filter="url(#glow-v)"/>
  <circle cx="185" cy="260" r="2.5" fill="#a5b4fc" filter="url(#glow-v)"/>
  <!-- Synapse lines -->
  <line x1="155" y1="190" x2="195" y2="178" stroke="#818cf8" stroke-width="0.8" opacity="0.7"/>
  <line x1="195" y1="178" x2="220" y2="205" stroke="#818cf8" stroke-width="0.8" opacity="0.7"/>
  <line x1="220" y1="205" x2="205" y2="240" stroke="#818cf8" stroke-width="0.8" opacity="0.7"/>
  <line x1="170" y1="225" x2="205" y2="240" stroke="#818cf8" stroke-width="0.8" opacity="0.5"/>
  <line x1="170" y1="225" x2="150" y2="248" stroke="#818cf8" stroke-width="0.8" opacity="0.5"/>
  <line x1="185" y1="260" x2="205" y2="240" stroke="#818cf8" stroke-width="0.8" opacity="0.5"/>

  <!-- Brain label -->
  <text x="185" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#a5b4fc" font-weight="700">THE BRAIN</text>
  <text x="185" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#6366f1">Physical · Measurable</text>

  <!-- Brain bullet points -->
  <text x="60" y="378" font-family="system-ui,sans-serif" font-size="9" fill="#475569">86 billion neurons · 100 trillion synapses</text>

  <!-- ─── RIGHT: MIND (experiential) ─── -->
  <ellipse cx="535" cy="210" rx="130" ry="110" fill="url(#mindGrad)" stroke="#f59e0b" stroke-width="1.5" opacity="0.75"/>

  <!-- Mind experience icons (abstract) -->
  <!-- Color qualia - red dot with glow -->
  <circle cx="490" cy="185" r="14" fill="#ef4444" opacity="0.85" filter="url(#glow-a)"/>
  <text x="490" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="white" font-weight="700">RED</text>

  <!-- Sweet qualia -->
  <circle cx="535" cy="175" r="14" fill="#a3e635" opacity="0.75" filter="url(#glow-a)"/>
  <text x="535" y="180" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#1a2e05" font-weight="700">SWEET</text>

  <!-- Pain qualia -->
  <circle cx="580" cy="190" r="14" fill="#f97316" opacity="0.8" filter="url(#glow-a)"/>
  <text x="580" y="195" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="white" font-weight="700">PAIN</text>

  <!-- Self / awareness -->
  <circle cx="510" cy="230" r="18" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4 2"/>
  <text x="510" y="228" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fde68a">aware</text>
  <text x="510" y="240" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fde68a">of self</text>

  <!-- Memory -->
  <circle cx="560" cy="235" r="15" fill="#7c3aed" opacity="0.7" filter="url(#glow-a)"/>
  <text x="560" y="240" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#ede9fe" font-weight="700">MEMORY</text>

  <!-- Thought wave -->
  <path d="M485,265 Q500,255 515,265 Q530,275 545,265 Q560,255 575,265" fill="none" stroke="#fbbf24" stroke-width="1.5" opacity="0.7"/>
  <text x="530" y="285" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#92400e">inner voice · dreams</text>

  <!-- Mind label -->
  <text x="535" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#fbbf24" font-weight="700">THE MIND</text>
  <text x="535" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#d97706">Subjective · Private</text>

  <!-- Mind bullet -->
  <text x="410" y="378" font-family="system-ui,sans-serif" font-size="9" fill="#475569">qualia · consciousness · inner experience</text>

  <!-- ─── CENTER: THE GAP ─── -->
  <!-- Dashed vertical gap line -->
  <line x1="360" y1="90" x2="360" y2="320" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Question mark in the gap -->
  <circle cx="360" cy="210" r="28" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <text x="360" y="204" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#94a3b8" font-weight="700">?</text>
  <text x="360" y="222" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#475569">hard</text>
  <text x="360" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#475569">problem</text>

  <!-- Arrows toward center from both sides -->
  <line x1="318" y1="210" x2="340" y2="210" stroke="#475569" stroke-width="1.2" marker-end="url(#arr-gap)" opacity="0.6"/>
  <line x1="402" y1="210" x2="380" y2="210" stroke="#475569" stroke-width="1.2" marker-end="url(#arr-gap)" opacity="0.6"/>

  <!-- Gap label -->
  <text x="360" y="105" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">explanatory</text>
  <text x="360" y="117" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">gap</text>
</svg>
</figure>"""

ARTICLE = {
    "title": "Is the Brain and the Mind the Same Thing?",
    "slug": "brain-and-mind-same-thing",
    "summary": (
        "Neuroscientist David Eagleman explores one of science's deepest questions: "
        "the brain is a measurable physical organ, but the mind — the redness of red, "
        "the inner voice, the feeling of being you — remains stubbornly hard to explain "
        "in purely physical terms."
    ),
    "order": 1,
    "published": True,
    "content": f"""{SVG_BRAIN_MIND}

<p>Every morning when you wake up, something remarkable happens. One moment you're a
sack of unconscious tissue. The next, you are <em>you</em> — aware of your name, your
history, the smell of coffee, the feel of sheets. What switched on? And what, exactly,
is doing the experiencing?</p>

<p>This is the question neuroscientist David Eagleman has spent his career circling. His
answer isn't a simple yes or no — it's a window into one of the deepest unsolved problems
in science.</p>

<h2>The Brain Is Undeniable</h2>

<p>Start with what we know. You have roughly 86 billion neurons in your skull, each
firing electrical spikes tens to hundreds of times per second, linked by perhaps 100
trillion synaptic connections. This three-pound organ — "our three-pound universe," as
Eagleman calls it — controls everything you do, feel, and think.</p>

<p>Damage a region of the brain and you lose a piece of yourself. Stroke a motor area
and an arm stops moving. Remove the hippocampus and new memories stop forming. Flood the
prefrontal cortex with alcohol and your judgment dissolves. Personality, desire, moral
reasoning, love — every aspect of your inner life has a neural address. The case that the
brain produces the mind looks overwhelming.</p>

<p>Most neuroscientists today subscribe to what Eagleman calls materialism and
reductionism: "We should be understandable as a collection of cells and blood vessels
and hormones and proteins and fluids all following the basic laws of chemistry and
physics." Each day, neuroscientists go into the lab and work under this assumption. And
it works — up to a point.</p>

<h2>The Thing That Flickers to Life</h2>

<p>Here is where the story gets harder. Eagleman defines consciousness simply and
precisely: <em>"Consciousness is the thing that flickers to life when you wake up in
the morning."</em> You have the same brain the moment before you wake and the moment
after. A tiny change in the pattern of neural activity — and suddenly there is someone
home. A sack of potatoes becomes a person with a past, a name, and an inner world.</p>

<p>Why? That's the problem. 100 billion neurons having little electrical spikes is not,
on its face, obviously different from 19 billion transistors inside an iPhone. Yet we
don't believe the iPhone experiences anything when it displays a funny video. As Eagleman
puts it: "When your phone gets an email from your boss, does it feel stressed?" Almost
certainly not. But your brain, doing something not entirely unlike that computation, does.
What is the difference?</p>

<p>This is what philosopher David Chalmers called the "hard problem" of consciousness —
and Eagleman takes it seriously. The easy problems are explaining how the brain processes
sensory information, controls behavior, reports internal states. The <em>hard</em>
problem is explaining why any of that processing is accompanied by <em>experience</em>.</p>

<h2>Qualia: The Redness of Red</h2>

<p>Consider color. When you look at a red apple, photons hit your retina, signals travel
to your visual cortex, and a particular pattern of cells activates. That part is
measurable. A neuroscientist can point to exactly which neurons fired.</p>

<p>But <em>why does that pattern feel red to you?</em> There's nothing inherently red
about a particular wavelength of light. The redness is something the brain constructs —
and it could, in principle, have been experienced as blue or green, or as a sound, or as
nothing at all. The inner experience — what philosophers call a <em>quale</em> — is
irreducible. It can't be fully described in terms of anything else. If you've never
tasted an avocado, no amount of description will give you the experience. The experience
is private, subjective, and untransmittable.</p>

<p>As Eagleman's colleague Anil Seth puts it: "For a conscious organism there is
<em>something it is like</em> to be that organism." That simple phrase, from philosopher
Thomas Nagel, is doing a lot of work. It draws a line between systems that process
information (thermostats, phones, possibly very simple animals) and systems that
<em>experience</em> something as they do it.</p>

<h2>Why Reductionism Hits a Wall</h2>

<p>Eagleman uses the Human Genome Project as an analogy for the limits of breaking
things down. When scientists sequenced the entire human genome, it was a landmark
achievement — and in some ways a surprise. We found that humans share essentially the
same genetic recipe as squirrels and tuna fish. The genome tells you the nuts and
bolts, not the product. A squirrel and a human are built from similar screws, but they
are radically different things. The instruction set doesn't explain the experience of
being either one.</p>

<p>The same logic applies to neurons. Even if you mapped every connection in every human
brain — a project of staggering complexity — you'd have a wiring diagram. You wouldn't
automatically have an explanation of why that wiring diagram is accompanied by the
sensation of tasting chocolate, or the ache of loneliness, or the particular quality
of hearing your name called in a crowd.</p>

<p>"The brain with its private subjective experience is unlike any of the problems that
we've tackled so far," Eagleman writes. "And anybody who tells you that we have the
problem cornered with a reductionist approach doesn't actually understand the complexity
of the problem."</p>

<h2>Eagleman's Honest Position</h2>

<p>So is the brain the mind? Eagleman's answer is careful. He doesn't invoke a soul or
a non-physical substance. There is no evidence for a ghost in the machine — brain
damage, drugs, and sleep all prove the mind is tethered to the physical brain in the
most direct way possible. But he is equally honest that our current scientific framework
may be insufficient to explain the leap from neurons firing to the feeling of being you.</p>

<p>"Every single generation before us has worked under the assumption that they possessed
all the major tools for understanding the universe," he writes, "and they were all wrong
without exception." We understood rainbows only after optics. Lightning only after
electricity. It's possible — likely, even — that consciousness will require concepts we
don't yet have.</p>

<p>What excites Eagleman is not the gap but the territory it reveals. Even in a purely
material universe, the fact that arranged molecules can feel awe, compose music, fall in
love, and contemplate their own existence is — in his words — "mind-blowingly amazing.
Better than anything ever proposed in anyone's holy text."</p>

<h2>The Working Answer</h2>

<p>Brain and mind are not two separate substances — there is no free-floating mind
drifting around without a brain. But they are also not simply identical in the way a
wave and the ocean are identical. The mind is what it feels like to <em>be</em> the
brain running. It is the first-person perspective generated by a third-person physical
process, and bridging those two descriptions remains, for now, the central unsolved
problem of neuroscience.</p>

<p>Eagleman's science doesn't erase the mystery — it illuminates how deep it goes. Every
time you wake up and experience the world as <em>you</em>, something is happening that
the smartest people alive still cannot fully account for. That's not cause for
mysticism. It's cause for curiosity.</p>

<p><em>Based on David Eagleman's Inner Cosmos podcast, including episodes on
consciousness, qualia, materialism, and the hard problem of subjective experience.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load Eagleman brain-vs-mind article into the Neuroscience pillar"

    def handle(self, *args, **options):
        pillar, created = Pillar.objects.get_or_create(
            slug=PILLAR["slug"],
            defaults=PILLAR,
        )
        if not created:
            for k, v in PILLAR.items():
                setattr(pillar, k, v)
            pillar.save()
        action = "Created" if created else "Updated"
        self.stdout.write(f"{action} pillar: {pillar.name}")

        article, created = Article.objects.get_or_create(
            slug=ARTICLE["slug"],
            defaults={**ARTICLE, "pillar": pillar},
        )
        if not created:
            for k, v in ARTICLE.items():
                setattr(article, k, v)
            article.pillar = pillar
            article.save()
        action = "Created" if created else "Updated"
        self.stdout.write(f"{action} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
