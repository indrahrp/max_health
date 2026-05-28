from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR_SLUG = "physiological-origin"

SVG_ILLUSTRATION = """<figure style="margin:1.5em 0 2.5em;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" style="width:100%;border-radius:16px;display:block;background:#060c16;">
  <defs>
    <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7dd3fc" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#7dd3fc" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f87171" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#f87171" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur1"><feGaussianBlur stdDeviation="3"/></filter>
    <style>
      @keyframes suppress {
        0%,100% { opacity:0.15; transform:scaleY(0.3); }
        50% { opacity:0.9; transform:scaleY(1); }
      }
      @keyframes pulse-red {
        0%,100% { opacity:0.3; r:18; }
        50% { opacity:0.9; r:28; }
      }
      @keyframes flow-arrow {
        0% { stroke-dashoffset: 60; opacity:0.2; }
        60% { opacity:1; }
        100% { stroke-dashoffset:0; opacity:0.6; }
      }
      @keyframes drift {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
        100% { transform: translateY(0px); }
      }
      @keyframes immune-attack {
        0%,100% { opacity:0.2; r:6; }
        50% { opacity:1; r:10; }
      }
      @keyframes label-fade {
        0%,100% { opacity:0.6; }
        50% { opacity:1; }
      }
      .child-glow { animation: drift 4s ease-in-out infinite; }
      .suppress-wave { animation: suppress 3s ease-in-out infinite; }
      .immune-cell { animation: immune-attack 2s ease-in-out infinite; }
      .arrow-flow { stroke-dasharray:8,4; animation: flow-arrow 2.5s ease-in-out infinite; }
      .label-pulse { animation: label-fade 3s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="#060c16"/>
  <rect x="0" y="0" width="720" height="420" fill="url(#glow1)" opacity="0.15"/>

  <!-- Title -->
  <text x="360" y="38" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#e2e8f0" font-weight="bold">When the Body Remembers What the Mind Suppressed</text>
  <text x="360" y="58" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#94a3b8" font-style="italic">Gabor Maté — childhood environment, emotional suppression, and autoimmune disease</text>

  <!-- Stage 1: Child / Environment -->
  <g class="child-glow" transform="translate(90,220)">
    <circle cx="0" cy="-60" r="32" fill="none" stroke="#7dd3fc" stroke-width="1.5" opacity="0.5"/>
    <!-- head -->
    <ellipse cx="0" cy="-60" rx="18" ry="20" fill="#1e3a5f" stroke="#7dd3fc" stroke-width="1.2"/>
    <!-- body -->
    <rect x="-12" y="-38" width="24" height="34" rx="4" fill="#1e3a5f" stroke="#7dd3fc" stroke-width="1.2"/>
    <!-- arms -->
    <line x1="-12" y1="-30" x2="-26" y2="-16" stroke="#7dd3fc" stroke-width="2"/>
    <line x1="12" y1="-30" x2="26" y2="-16" stroke="#7dd3fc" stroke-width="2"/>
    <!-- legs -->
    <line x1="-6" y1="-4" x2="-10" y2="16" stroke="#7dd3fc" stroke-width="2"/>
    <line x1="6" y1="-4" x2="10" y2="16" stroke="#7dd3fc" stroke-width="2"/>
    <!-- face - worried expression -->
    <circle cx="-5" cy="-62" r="2.5" fill="#7dd3fc"/>
    <circle cx="5" cy="-62" r="2.5" fill="#7dd3fc"/>
    <path d="M -5,-52 Q 0,-48 5,-52" stroke="#7dd3fc" stroke-width="1.5" fill="none"/>
  </g>
  <text x="90" y="306" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7dd3fc" class="label-pulse">Childhood</text>
  <text x="90" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7dd3fc" class="label-pulse">Environment</text>
  <!-- stress lines around child -->
  <line x1="52" y1="152" x2="42" y2="138" stroke="#f97316" stroke-width="1.5" opacity="0.7"/>
  <line x1="128" y1="152" x2="138" y2="138" stroke="#f97316" stroke-width="1.5" opacity="0.7"/>
  <line x1="90" y1="140" x2="90" y2="124" stroke="#f97316" stroke-width="1.5" opacity="0.7"/>

  <!-- Arrow 1 -->
  <path d="M 150,220 Q 190,220 220,220" stroke="#94a3b8" stroke-width="2" fill="none" class="arrow-flow" marker-end="url(#arr)"/>
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#94a3b8"/>
    </marker>
  </defs>
  <text x="185" y="210" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#64748b" font-style="italic">learns to</text>
  <text x="185" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#64748b" font-style="italic">suppress</text>

  <!-- Stage 2: Suppressed Self -->
  <g transform="translate(290,220)">
    <!-- person outline, muted -->
    <ellipse cx="0" cy="-60" rx="18" ry="20" fill="#1a2535" stroke="#475569" stroke-width="1.2"/>
    <rect x="-12" y="-38" width="24" height="34" rx="4" fill="#1a2535" stroke="#475569" stroke-width="1.2"/>
    <line x1="-12" y1="-30" x2="-26" y2="-16" stroke="#475569" stroke-width="2"/>
    <line x1="12" y1="-30" x2="26" y2="-16" stroke="#475569" stroke-width="2"/>
    <line x1="-6" y1="-4" x2="-10" y2="16" stroke="#475569" stroke-width="2"/>
    <line x1="6" y1="-4" x2="10" y2="16" stroke="#475569" stroke-width="2"/>
    <!-- flat face -->
    <circle cx="-5" cy="-62" r="2.5" fill="#475569"/>
    <circle cx="5" cy="-62" r="2.5" fill="#475569"/>
    <line x1="-4" y1="-51" x2="4" y2="-51" stroke="#475569" stroke-width="1.5"/>
    <!-- suppressed emotion waves inside chest -->
    <rect x="-9" y="-30" width="18" height="20" rx="3" fill="none" stroke="#7dd3fc" stroke-width="0" opacity="0"/>
    <path d="M -8,-22 Q -2,-12 4,-22 Q 8,-12 12,-22" stroke="#f97316" stroke-width="1.8" fill="none" class="suppress-wave" opacity="0.7"/>
    <!-- lock icon -->
    <rect x="-6" y="-6" width="12" height="9" rx="2" fill="none" stroke="#f97316" stroke-width="1.5" opacity="0.8"/>
    <path d="M -4,-6 Q -4,-14 0,-14 Q 4,-14 4,-6" stroke="#f97316" stroke-width="1.5" fill="none" opacity="0.8"/>
  </g>
  <text x="290" y="306" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#94a3b8" class="label-pulse">Emotional</text>
  <text x="290" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#94a3b8" class="label-pulse">Suppression</text>

  <!-- Arrow 2 -->
  <path d="M 352,220 Q 392,220 420,220" stroke="#94a3b8" stroke-width="2" fill="none" class="arrow-flow" style="animation-delay:0.8s" marker-end="url(#arr)"/>
  <text x="386" y="210" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#64748b" font-style="italic">chronic</text>
  <text x="386" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#64748b" font-style="italic">stress</text>

  <!-- Stage 3: Immune System Dysregulation -->
  <g transform="translate(490,220)">
    <!-- central body/organ shape -->
    <ellipse cx="0" cy="-20" rx="36" ry="44" fill="#1a0a0a" stroke="#f87171" stroke-width="1.5" opacity="0.8"/>
    <!-- immune cells attacking -->
    <circle cx="-20" cy="-38" r="7" fill="#f87171" opacity="0.3" class="immune-cell"/>
    <circle cx="18" cy="-10" r="7" fill="#f87171" opacity="0.4" class="immune-cell" style="animation-delay:0.5s"/>
    <circle cx="-8" cy="14" r="7" fill="#f87171" opacity="0.35" class="immune-cell" style="animation-delay:1s"/>
    <circle cx="22" cy="-40" r="5" fill="#f87171" opacity="0.5" class="immune-cell" style="animation-delay:1.5s"/>
    <circle cx="-26" cy="2" r="5" fill="#f87171" opacity="0.4" class="immune-cell" style="animation-delay:0.3s"/>
    <!-- self-attack lines -->
    <line x1="-20" y1="-32" x2="-8" y2="-20" stroke="#f87171" stroke-width="1.2" opacity="0.6" class="arrow-flow" style="animation-delay:0.4s"/>
    <line x1="18" y1="-16" x2="6" y2="-20" stroke="#f87171" stroke-width="1.2" opacity="0.6" class="arrow-flow" style="animation-delay:0.9s"/>
    <line x1="-8" y1="8" x2="0" y2="-4" stroke="#f87171" stroke-width="1.2" opacity="0.6" class="arrow-flow" style="animation-delay:1.2s"/>
    <!-- glow center -->
    <ellipse cx="0" cy="-20" rx="18" ry="22" fill="url(#glow2)"/>
    <text x="0" y="-16" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#fca5a5">immune</text>
    <text x="0" y="-6" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#fca5a5">attack</text>
  </g>
  <text x="490" y="306" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#f87171" class="label-pulse">Autoimmune</text>
  <text x="490" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#f87171" class="label-pulse">Disease</text>

  <!-- Arrow 3 -->
  <path d="M 546,220 Q 586,220 614,220" stroke="#f87171" stroke-width="2" fill="none" class="arrow-flow" style="animation-delay:1.4s" marker-end="url(#arr-red)"/>
  <defs>
    <marker id="arr-red" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#f87171"/>
    </marker>
  </defs>

  <!-- Stage 4: The question / healing -->
  <g transform="translate(650,220)">
    <circle cx="0" cy="-30" r="36" fill="none" stroke="#34d399" stroke-width="1.2" opacity="0.5"/>
    <text x="0" y="-38" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#34d399">?</text>
    <text x="0" y="-18" text-anchor="middle" font-family="Arial,sans-serif" font-size="9.5" fill="#6ee7b7">What is</text>
    <text x="0" y="-7" text-anchor="middle" font-family="Arial,sans-serif" font-size="9.5" fill="#6ee7b7">this illness</text>
    <text x="0" y="4" text-anchor="middle" font-family="Arial,sans-serif" font-size="9.5" fill="#6ee7b7">here to teach</text>
    <text x="0" y="14" text-anchor="middle" font-family="Arial,sans-serif" font-size="9.5" fill="#6ee7b7">me about me?</text>
  </g>
  <text x="650" y="306" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#34d399" class="label-pulse">Awareness</text>
  <text x="650" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#34d399" class="label-pulse">&amp; Healing</text>

  <!-- Bottom quote -->
  <line x1="60" y1="360" x2="660" y2="360" stroke="#1e293b" stroke-width="1"/>
  <text x="360" y="382" text-anchor="middle" font-family="Georgia,serif" font-size="11.5" fill="#64748b" font-style="italic">"The body says no to what the mind cannot allow itself to feel."</text>
  <text x="360" y="400" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#475569">— Dr. Gabor Maté</text>
</svg>
</figure>"""

ARTICLE = {
    "title": "Autoimmune Disease, Trauma, and How Childhood Shapes the Body",
    "slug": "autoimmune-trauma-childhood-gabor-mate",
    "summary": (
        "Physician and trauma researcher Gabor Maté argues that autoimmune disease is rarely "
        "a random biological misfortune — it is the body saying no to a lifetime of suppressed "
        "emotion, stress absorbed in childhood, and a self that learned to put everyone else first."
    ),
    "order": 1,
    "published": True,
    "content": f"""{SVG_ILLUSTRATION}

<p>"I can guarantee you," Dr. Gabor Maté tells a packed audience, "that any of you here who've
had chronic illnesses of any kind — you're going to recognize yourself in this talk. Completely
and 100%. And you're going to wonder: why didn't anybody say this to me before?"</p>

<p>Maté spent twenty years as a family physician in Vancouver, including seven years as medical
coordinator of a palliative care unit. What he observed, over and over, contradicted what he had
been taught in medical school: <em>who got sick and who didn't was not accidental.</em></p>

<h2>The Personality the Body Pays For</h2>

<p>Western medicine tends to treat autoimmune diseases — rheumatoid arthritis, lupus, multiple
sclerosis, scleroderma, inflammatory bowel disease, chronic asthma, fibromyalgia — as distinct
biological disorders to be managed with immunosuppressive drugs. Maté doesn't dispute the
biology. He asks a deeper question: why does the immune system of certain people turn against
their own tissue in the first place?</p>

<p>In palliative care, watching people die of cancer and autoimmune disease, he kept finding the
same personality constellation. He is careful not to say these traits <em>cause</em> illness —
that would be too simple. But they contribute to onset "significantly," and in thirty years of
clinical work he says he has never found an exception.</p>

<p>The four patterns he identified:</p>

<ul>
<li><strong>Automatic concern for others while suppressing your own emotional needs.</strong>
The woman just diagnosed with breast cancer whose first thought is: "I'm worried about my
husband. How will I support him?" She is the one about to go through chemotherapy.</li>

<li><strong>Rigid identification with duty, role, and responsibility.</strong> The physician
who notices his blood pressure rising while finishing a book — because his identity is fused
with being productive, and anything that interrupts that is experienced as threat.</li>

<li><strong>Repression of healthy anger.</strong> Maté distinguishes carefully here: healthy
anger is simply a boundary defense — "You're in my space. Get out." It does its job and
dissolves. People who "never get angry," who are described by their families as selfless and
saintly, are not free of anger. They are imprisoned by it, turned inward.</li>

<li><strong>Two potentially fatal beliefs:</strong> that you are responsible for how other
people feel, and that you must never disappoint anyone.</li>
</ul>

<p>These patterns appear in the obituaries Maté reads aloud in his talks — Canada's most admired
citizens, eulogized for their selflessness, their tireless dedication, their inability to ever
say no. "We value in other people exactly what kills them," he says.</p>

<h2>Nobody Is Born This Way</h2>

<p>The crucial point: these are not character flaws or genetic predispositions. They are
<em>adaptations.</em> No infant arrives in the world reflexively suppressing its own needs.
Every newborn announces its hunger and discomfort without apology. The compulsive self-erasure
that shows up decades later in the body as autoimmune disease was learned — it was the
child's only strategy for maintaining connection with the people it depended on for survival.</p>

<p>"If your parents are alcoholics," Maté explains, "you're going to end up as a caretaker by
age four or five. You're going to be an emotional caretaker by suppressing your own needs. And
that's going to show up in illness of mind or body later on in life."</p>

<p>The child doesn't choose this. It is, in the most literal sense, a survival adaptation. In
an environment where the parent's emotional state is fragile or threatening, the child learns to
monitor the parent's feelings rather than its own. It learns that its job is to be good, to be
helpful, to take up as little space as possible. The self gets compressed to make room for the
adults. And the compression doesn't lift when the child grows up — it just moves underground,
into the body.</p>

<h2>Maté's Own Story</h2>

<p>Maté doesn't offer these ideas from a comfortable distance. He was born in Budapest in 1944,
two months before the German Army occupied Hungary. His mother called the pediatrician the day
after the occupation. "Would you please come and see Gabor — he's crying all the time." The
doctor replied: "Of course I'll come. But all my Jewish babies are crying."</p>

<p>His grandparents were killed in Auschwitz. His father was taken to forced labor. To keep him
alive, his mother handed him to a stranger on the street for six weeks. He doesn't remember this.
He doesn't need to.</p>

<p>"When mothers are stressed or in pain, the infant feels all that and takes it personally. It
becomes part of their template for how they view the world." The infant is not capable of
understanding that his mother's grief is about Auschwitz and occupation. The infant can only
conclude: <em>I'm not good enough. I'm the reason she is unhappy. It's my fault.</em></p>

<p>At seventy years old, in a therapeutic psilocybin session, that same conclusion surfaced
again — not as a memory, but as a lived experience. He began to cry. "I'm so sorry I made your
life so difficult," he said to his therapist, experiencing her as his mother, experiencing
himself as a one-year-old. "That was an unconscious memory of my sense of myself as a one-year-old."
Seventy years of building one of the world's most significant bodies of work on trauma and illness,
and the original wound was still there, waiting.</p>

<h2>The Physiology: Why Suppression Attacks the Body</h2>

<p>This isn't metaphor. There are specific physiological pathways through which emotional
suppression produces immune dysregulation.</p>

<p>When a child grows up under chronic stress — an alcoholic parent, a depressed mother, financial
precarity, persistent family tension — the body's stress response activates and stays activated.
Cortisol and adrenaline, designed to handle acute threats, flood the system chronically. "Financial
stress on the parents," Maté observes, "translates into physiological stress in the children.
They didn't inherit a disease. They're just reacting to the environment."</p>

<p>Over time, chronically elevated stress hormones alter immune function. The same system that is
supposed to distinguish self from non-self — attacking invaders while leaving the body's own
tissue alone — becomes dysregulated. It begins attacking the wrong targets. The body turns on itself.</p>

<p>There is also the direct immune effect of suppressed anger. Maté is unambiguous on this
mechanism: <em>"The repression of anger leads to autoimmune disease and cancer."</em> The
alternative — expressing rage without processing it — leads to heart disease and stroke, not
autoimmune disease. The distinction matters. It is the <em>suppression</em>, the swallowing of
what the body naturally wants to express, that creates a particular kind of chronic internal
stress.</p>

<p>At the cellular level, this chronic stress accelerates telomere shortening. Telomeres — the
protective caps on chromosomes — shorten naturally with age. Under chronic stress, they shorten
faster. Caregivers, a group Maté specifically studied, show accelerated telomere loss: not because
they inherited shorter telomeres, but because the chronic physiological toll of relentless
self-suppression and concern for others ages the cells ahead of schedule.</p>

<h2>What the Illness Is Trying to Say</h2>

<p>Maté is not arguing that people should refuse treatment, or that autoimmune disease is
deserved, or that the patient is to blame. He is arguing something more interesting and more
hopeful: that illness, in many cases, is the body communicating what the mind has not been allowed
to feel.</p>

<p>"When the body says no" — the title of his landmark book — is not a metaphor. The body is
saying no to a life structured around meeting everyone else's needs. It is saying no to the
perpetual suppression of emotion. It is saying no to the self that was compressed in childhood
and never given permission to re-expand.</p>

<p>"A lot of people," he says, "whether through help or through some intuition or some grace,
if they learn to look at their disease not just as something to get rid of, but also as a teacher —
'Where in my life was I not being myself?' — they're going to find that these patterns were present.
And they don't need to be. Because they're no longer the child that was constrained to be that way."</p>

<p>The personality that adapted to the childhood environment is not who the person actually is.
It is who they became. The illness, in this reading, is not an ending — it is an opening, a
place where the armor is thin enough for something true to get through.</p>

<h2>The Medicine That Has No Prescription</h2>

<p>None of this is taught in medical school. The Western biomedical model treats autoimmune
disease as a malfunction to be suppressed — biologic drugs to inhibit the immune response,
steroids to dampen inflammation. This treatment is real and often necessary. But it addresses
the mechanism, not the origin.</p>

<p>Maté's clinical experience — and the accumulating research on psychoneuroimmunology, ACE
(Adverse Childhood Experiences) studies, and epigenetics — points toward a different framing.
The autoimmune body is not merely malfunctioning. It is, in a very real sense, responding to
a lifetime of stored experience. The question "Why did this happen to me?" deserves a fuller
answer than genetics and bad luck.</p>

<p>That fuller answer, when people find it, often changes everything. Not necessarily the biology —
though sometimes that too — but the relationship with the illness, with the body, and with the
self that learned to disappear in order to stay safe as a child.</p>

<p><em>Based on Dr. Gabor Maté's YouTube interviews, including talks drawn from his books
<strong>When the Body Says No</strong> and <strong>The Myth of Normal</strong>, interviews on
The Diary of a CEO (Steven Bartlett), and his Mayim Bialik's Breakdown appearance.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load Gabor Maté autoimmune-trauma-childhood article into the physiological-origin pillar"

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
