from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR_SLUG = "mindset-success"

SVG_ILLUSTRATION = """<figure style="margin:1.5em 0 2.5em;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" style="width:100%;border-radius:16px;display:block;background:#07060f;">
  <defs>
    <radialGradient id="mglow" cx="50%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="shadow-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#dc2626" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#dc2626" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="light-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
    <style>
      @keyframes shadow-breathe {
        0%,100% { opacity:0.5; transform:scale(1); }
        50% { opacity:0.9; transform:scale(1.06); }
      }
      @keyframes light-breathe {
        0%,100% { opacity:0.6; transform:scale(1); }
        50% { opacity:1; transform:scale(1.04); }
      }
      @keyframes chain-pull {
        0%,100% { stroke-dashoffset:0; opacity:0.4; }
        50% { stroke-dashoffset:8; opacity:0.8; }
      }
      @keyframes title-pulse {
        0%,100% { opacity:0.7; }
        50% { opacity:1; }
      }
      @keyframes eye-glow {
        0%,100% { opacity:0.4; r:3; }
        50% { opacity:1; r:4.5; }
      }
      .shadow-figure { transform-origin: 200px 220px; animation: shadow-breathe 4s ease-in-out infinite; }
      .light-figure { transform-origin: 520px 220px; animation: light-breathe 4s ease-in-out infinite; animation-delay:2s; }
      .chain { stroke-dasharray:6,4; animation: chain-pull 3s ease-in-out infinite; }
      .eye { animation: eye-glow 2.5s ease-in-out infinite; }
      .lbl { animation: title-pulse 4s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="#07060f"/>
  <rect width="720" height="420" fill="url(#mglow)"/>

  <!-- Left: Shadow / Monster side -->
  <g class="shadow-figure">
    <circle cx="200" cy="220" r="70" fill="url(#shadow-glow)"/>
    <!-- dark figure -->
    <ellipse cx="200" cy="172" rx="28" ry="32" fill="#1a0505" stroke="#dc2626" stroke-width="1.5"/>
    <!-- horns / shadow features -->
    <path d="M 184,150 L 178,132 L 190,148" fill="#3d0a0a" stroke="#dc2626" stroke-width="1.2"/>
    <path d="M 216,150 L 222,132 L 210,148" fill="#3d0a0a" stroke="#dc2626" stroke-width="1.2"/>
    <!-- eyes -->
    <circle cx="192" cy="168" r="3" fill="#dc2626" class="eye"/>
    <circle cx="208" cy="168" r="3" fill="#dc2626" class="eye" style="animation-delay:0.4s"/>
    <!-- body -->
    <rect x="178" y="204" width="44" height="50" rx="6" fill="#1a0505" stroke="#dc2626" stroke-width="1.5"/>
    <!-- claws/arms -->
    <path d="M 178,218 L 152,238 L 148,252 M 148,252 L 144,248 M 148,252 L 152,248" stroke="#dc2626" stroke-width="2" fill="none"/>
    <path d="M 222,218 L 248,238 L 252,252 M 252,252 L 248,248 M 252,252 L 256,248" stroke="#dc2626" stroke-width="2" fill="none"/>
    <!-- legs -->
    <line x1="190" y1="254" x2="184" y2="284" stroke="#dc2626" stroke-width="2.5"/>
    <line x1="210" y1="254" x2="216" y2="284" stroke="#dc2626" stroke-width="2.5"/>
  </g>
  <text x="200" y="318" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#f87171" class="lbl">The Shadow</text>
  <text x="200" y="334" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#b91c1c" font-style="italic">(the capacity for harm)</text>

  <!-- Center divider + chain -->
  <line x1="360" y1="80" x2="360" y2="340" stroke="#4b5563" stroke-width="1" stroke-dasharray="4,4"/>
  <!-- chain connecting the two -->
  <path d="M 270,220 Q 315,200 360,220 Q 405,240 450,220" stroke="#a78bfa" stroke-width="2" fill="none" class="chain"/>
  <text x="360" y="215" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7c3aed" font-style="italic">disciplined will</text>

  <!-- Right: Light / Virtuous side -->
  <g class="light-figure">
    <circle cx="520" cy="220" r="70" fill="url(#light-glow)"/>
    <!-- upright figure -->
    <ellipse cx="520" cy="168" rx="26" ry="30" fill="#1a1205" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- crown / halo suggestion -->
    <path d="M 504,148 L 508,136 L 520,144 L 532,136 L 536,148" stroke="#f59e0b" stroke-width="1.5" fill="none" opacity="0.7"/>
    <!-- calm eyes -->
    <ellipse cx="512" cy="165" rx="4" ry="3" fill="#f59e0b" opacity="0.8"/>
    <ellipse cx="528" cy="165" rx="4" ry="3" fill="#f59e0b" opacity="0.8"/>
    <!-- slight smile -->
    <path d="M 510,178 Q 520,184 530,178" stroke="#f59e0b" stroke-width="1.5" fill="none" opacity="0.7"/>
    <!-- body - upright, shoulders back -->
    <rect x="500" y="200" width="40" height="52" rx="5" fill="#1a1205" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- strong arms at sides -->
    <line x1="500" y1="212" x2="476" y2="240" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="540" y1="212" x2="564" y2="240" stroke="#f59e0b" stroke-width="2.5"/>
    <!-- legs planted -->
    <line x1="510" y1="252" x2="504" y2="282" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="530" y1="252" x2="536" y2="282" stroke="#f59e0b" stroke-width="2.5"/>
  </g>
  <text x="520" y="318" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#fcd34d" class="lbl">The Restrained Monster</text>
  <text x="520" y="334" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#d97706" font-style="italic">(dangerous by choice, not by default)</text>

  <!-- Title -->
  <text x="360" y="36" text-anchor="middle" font-family="Georgia,serif" font-size="20" fill="#e2e8f0" font-weight="bold">Be a Monster — and Learn to Control It</text>
  <text x="360" y="57" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" fill="#94a3b8" font-style="italic">Jordan Peterson on why harmlessness is not the same as virtue</text>

  <!-- Bottom quote -->
  <line x1="60" y1="356" x2="660" y2="356" stroke="#1e1b2e" stroke-width="1"/>
  <text x="360" y="377" text-anchor="middle" font-family="Georgia,serif" font-size="11.5" fill="#6d28d9" font-style="italic">"A man who is capable of aggression but has it under control is far more useful than one who cannot."</text>
  <text x="360" y="396" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#4c1d95">— Jordan Peterson</text>
</svg>
</figure>"""

ARTICLE = {
    "title": "Be a Monster — and Learn to Control It",
    "slug": "peterson-be-a-monster-virtue-strength",
    "summary": (
        "Jordan Peterson's most counter-intuitive idea: you should cultivate your capacity "
        "for aggression, danger, and darkness — not suppress it. A person who is harmless "
        "is not virtuous. A person who is dangerous but chooses restraint is. "
        "The difference matters more than most people want to admit."
    ),
    "order": 1,
    "published": True,
    "content": f"""{SVG_ILLUSTRATION}

<p>Jordan Peterson tells young men something they are rarely told and almost never want to
hear: <em>"I think you should be a monster. An absolute monster. And then you should learn
how to control it."</em></p>

<p>This is not edgy advice designed to shock. It is one of the most serious claims in his
work, rooted in clinical psychology, Jungian shadow theory, and decades of watching people
collapse under lives they built on the premise that being inoffensive was the same thing
as being good.</p>

<p>It isn't.</p>

<h2>Harmlessness Is Not a Virtue</h2>

<p>The confusion runs deep. In a culture that prizes agreeableness, conflict-avoidance,
and sensitivity, many people grow up believing that the absence of aggression constitutes
goodness. They don't fight back. They don't assert themselves. They don't say no. They
call this virtue. Peterson calls it something else: weakness dressed up as morality.</p>

<p>"A man who's capable of aggression but has it under control is a way more useful man
than one who cannot do that."</p>

<p>The distinction is everything. There is a fundamental difference between a person who
doesn't harm others because they lack the power to harm — and a person who doesn't harm
others because they have chosen not to. The first is simply incapable. The second is
making a genuine moral decision, one that requires something real to restrain.</p>

<p>Genuine virtue, Peterson argues, is only possible for someone who has access to their
own capacity for harm and consciously governs it. You cannot choose peace if you are
incapable of conflict. You cannot choose kindness if cruelty is not a live option. The
goodness of a person who has never faced their own darkness is untested, and therefore
shallow — like courage in someone who has never been afraid.</p>

<h2>The Question You Don't Want to Ask</h2>

<p>The deepest version of this idea comes from Peterson's engagement with one of the most
disturbing questions in moral psychology: could you have been a Nazi prison guard?</p>

<p>"Are you the Nazi prison guard? Are you so sure you aren't? That's the real question."</p>

<p>Most people answer immediately: of course not. Peterson's point is that the confidence
of that answer is the problem. The people who became guards, perpetrators, willing
participants in atrocities — they were human beings with families, preferences, ordinary
daily lives. The distance between an ordinary person and someone capable of great evil
is not as wide as we prefer to believe.</p>

<p>"Nothing human is foreign to me," he says — a phrase borrowed from the Roman playwright
Terence, adopted by Jung, and made the center of Peterson's account of the shadow. The
monster inside you is not a stranger. It is you, under different conditions. And if you
refuse to look at it, it doesn't disappear. It just operates without supervision.</p>

<p>"I don't think you can contemplate the good without contemplating the evil first. You
can't stumble toward the light without acknowledging the darkness."</p>

<h2>What the Shadow Actually Is</h2>

<p>Peterson draws heavily on Carl Jung's concept of the shadow — the part of the psyche
that contains everything we have repressed, denied, or refused to acknowledge about
ourselves. Our capacity for rage, cruelty, manipulation, selfishness. The thoughts we
don't permit ourselves to have. The impulses we immediately suppress and pretend we
never felt.</p>

<p>The danger is not in having a shadow. Everyone does. The danger is in pretending you
don't. When the shadow goes unacknowledged, it doesn't lie dormant — it leaks out
sideways. In passive-aggression. In resentment. In the sudden disproportionate eruptions
that shock even the person who produces them. The person who insists they are never angry
is often the most frightening person in the room, because their anger has no address.</p>

<p>Integration is the alternative. Not indulgence — you are not being invited to act on
every dark impulse. But honest acknowledgment: this is part of me. I contain this. I am
capable of this. And because I see it clearly, I can govern it rather than be governed by it.</p>

<h2>Women, Men, and the Dangerous Man</h2>

<p>Peterson returns to this theme when discussing what women actually want from men — as
distinct from what culture currently tells them they should want. The data is
uncomfortable: female fantasy literature, analyzed across millions of examples, consistently
centers on a particular archetype. "Mad, bad, and dangerous to know," Peterson paraphrases.
The vampire, the werewolf, the pirate billionaire. The barely domesticated predator.</p>

<p>"Women want men who are capable — and even capable of being dangerous — but they want
that encapsulated within something. It's the soothing of the savage beast. There's a need
to harness that unconstrained vitalism."</p>

<p>What the fantasy reveals is not a desire for harm, but a desire for genuine power that
has been brought under voluntary control. A man who has genuinely mastered something
dangerous within himself is more attractive — and more trustworthy — than a man who has
simply never been dangerous. The first has demonstrated something real. The second has
demonstrated nothing at all.</p>

<h2>The Dragon at the Gate</h2>

<p>Peterson's favorite metaphor for this process is the hero who fights the dragon guarding
the treasure. The dragon is not an obstacle to avoid — it is the necessary guardian of
everything worth having. The treasure on the other side of the interview, the difficult
conversation, the confrontation, the risk: it is only accessible to someone willing to
fight for it.</p>

<p>"You want to fight the dragons that guard the gates of the treasure that you wish to
attain. Productivity requires aim, orientation, responsibility, discipline — the willingness
to work, the willingness to make sacrifices. If you do that it gives you a dragon to fight."</p>

<p>This is why, Peterson argues, telling young people they are fine exactly as they are is
one of the cruelest things you can do to them. It deflates them. It removes the necessity
of transformation. The person who doesn't need to become anything won't. And then the
dragons multiply, undefeated, while the person grows smaller behind a wall of comfortable
self-acceptance that was really just a refusal to grow.</p>

<h2>The Decision</h2>

<p>The point is not to become destructive. The point is to become capable — and then to
make a genuine choice about how to use that capability. Peterson frames this as the
foundational moral decision:</p>

<p><em>"You have to say to yourself: I will do good nonetheless. Everyone great makes that
decision. Make that decision — because maybe you're great."</em></p>

<p>The "nonetheless" carries the full weight. It means: despite knowing what I'm capable
of, despite acknowledging the darkness in me, despite the fact that there are easier and
more destructive paths available — I will aim at the good. That is a choice. It requires
something to choose against.</p>

<p>A person without a monster has nothing to restrain. Their goodness costs them nothing.
And things that cost nothing are worth exactly what you paid.</p>

<p><em>Based on Jordan Peterson's YouTube lectures and interviews, including discussions of
Jungian shadow integration, the nature of virtue, and what it means to become a fully
realized person.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load Peterson 'Be a Monster' article into mindset-success pillar"

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
