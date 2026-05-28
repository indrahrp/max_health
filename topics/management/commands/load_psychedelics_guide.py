from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Psychedelics",
    "slug": "psychedelics",
    "description": (
        "Psilocybin, MDMA, DMT, LSD, and ketamine — the science, the history, and the "
        "renewed clinical research into psychedelic-assisted therapy for depression, PTSD, "
        "addiction, and end-of-life distress."
    ),
    "icon": "🍄",
    "color": "purple",
    "order": 13,
}

SVG_ILLUSTRATION = """<figure style="margin:1.5em 0 2.5em;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" style="width:100%;border-radius:16px;display:block;background:#07030f;">
  <defs>
    <radialGradient id="bg-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/>
    </radialGradient>
    <style>
      @keyframes orbit1 {
        from { transform: rotate(0deg) translateX(130px) rotate(0deg); }
        to   { transform: rotate(360deg) translateX(130px) rotate(-360deg); }
      }
      @keyframes orbit2 {
        from { transform: rotate(72deg) translateX(130px) rotate(-72deg); }
        to   { transform: rotate(432deg) translateX(130px) rotate(-432deg); }
      }
      @keyframes orbit3 {
        from { transform: rotate(144deg) translateX(130px) rotate(-144deg); }
        to   { transform: rotate(504deg) translateX(130px) rotate(-504deg); }
      }
      @keyframes orbit4 {
        from { transform: rotate(216deg) translateX(130px) rotate(-216deg); }
        to   { transform: rotate(576deg) translateX(130px) rotate(-576deg); }
      }
      @keyframes orbit5 {
        from { transform: rotate(288deg) translateX(130px) rotate(-288deg); }
        to   { transform: rotate(648deg) translateX(130px) rotate(-648deg); }
      }
      @keyframes center-pulse {
        0%,100% { r:34; opacity:0.7; }
        50% { r:42; opacity:1; }
      }
      @keyframes glow-ring {
        0%,100% { opacity:0.2; }
        50% { opacity:0.5; }
      }
      @keyframes label-glow {
        0%,100% { opacity:0.7; }
        50% { opacity:1; }
      }
      .node1 { transform-origin: 360px 210px; animation: orbit1 18s linear infinite; }
      .node2 { transform-origin: 360px 210px; animation: orbit2 18s linear infinite; }
      .node3 { transform-origin: 360px 210px; animation: orbit3 18s linear infinite; }
      .node4 { transform-origin: 360px 210px; animation: orbit4 18s linear infinite; }
      .node5 { transform-origin: 360px 210px; animation: orbit5 18s linear infinite; }
      .center-orb { animation: center-pulse 4s ease-in-out infinite; }
      .orbit-ring { animation: glow-ring 4s ease-in-out infinite; }
      .lbl { animation: label-glow 4s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="#07030f"/>
  <rect width="720" height="420" fill="url(#bg-glow)"/>

  <!-- Orbit ring -->
  <ellipse cx="360" cy="210" rx="130" ry="130" fill="none" stroke="#4c1d95" stroke-width="0.8" stroke-dasharray="4,6" class="orbit-ring"/>

  <!-- Center brain/mind orb -->
  <circle cx="360" cy="210" r="34" fill="#1a0a2e" stroke="#a78bfa" stroke-width="1.5" class="center-orb"/>
  <text x="360" y="206" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c4b5fd">Mind &amp;</text>
  <text x="360" y="219" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c4b5fd">Healing</text>

  <!-- Node 1: Psilocybin (mushroom gold) -->
  <g class="node1">
    <circle cx="360" cy="210" r="28" fill="#3d1a00" stroke="#f59e0b" stroke-width="2"/>
    <!-- mushroom icon -->
    <ellipse cx="360" cy="204" rx="14" ry="8" fill="#f59e0b" opacity="0.9"/>
    <rect x="357" y="204" width="6" height="11" rx="2" fill="#f59e0b" opacity="0.7"/>
    <text x="360" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#fcd34d" class="lbl">Psilocybin</text>
  </g>

  <!-- Node 2: MDMA (warm pink) -->
  <g class="node2">
    <circle cx="360" cy="210" r="28" fill="#2d001a" stroke="#f472b6" stroke-width="2"/>
    <!-- heart icon -->
    <path d="M 352,204 C 352,200 356,198 360,202 C 364,198 368,200 368,204 C 368,208 360,215 360,215 C 360,215 352,208 352,204 Z" fill="#f472b6" opacity="0.9"/>
    <text x="360" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#f9a8d4" class="lbl">MDMA</text>
  </g>

  <!-- Node 3: DMT/Ayahuasca (teal-green) -->
  <g class="node3">
    <circle cx="360" cy="210" r="28" fill="#001a1a" stroke="#2dd4bf" stroke-width="2"/>
    <!-- spiral/vine symbol -->
    <path d="M 360,200 C 354,203 352,208 356,212 C 360,216 368,214 368,208 C 368,202 362,198 360,200" stroke="#2dd4bf" stroke-width="2" fill="none"/>
    <circle cx="360" cy="210" r="3" fill="#2dd4bf" opacity="0.8"/>
    <text x="360" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#5eead4" class="lbl">DMT / Ayahuasca</text>
  </g>

  <!-- Node 4: LSD (electric blue) -->
  <g class="node4">
    <circle cx="360" cy="210" r="28" fill="#000d2e" stroke="#60a5fa" stroke-width="2"/>
    <!-- lightning / wave -->
    <path d="M 364,199 L 358,209 L 364,209 L 356,221 L 362,211 L 356,211 Z" fill="#60a5fa" opacity="0.9"/>
    <text x="360" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#93c5fd" class="lbl">LSD</text>
  </g>

  <!-- Node 5: Ketamine (silver-white) -->
  <g class="node5">
    <circle cx="360" cy="210" r="28" fill="#0d0d1a" stroke="#94a3b8" stroke-width="2"/>
    <!-- K+ ion / hexagon -->
    <polygon points="360,199 368,204 368,214 360,219 352,214 352,204" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="360" y="213" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#cbd5e1">K</text>
    <text x="360" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#cbd5e1" class="lbl">Ketamine</text>
  </g>

  <!-- Title -->
  <text x="360" y="36" text-anchor="middle" font-family="Georgia,serif" font-size="19" fill="#e2e8f0" font-weight="bold">Five Psychedelics, Five Mechanisms</text>
  <text x="360" y="56" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" fill="#94a3b8" font-style="italic">What the latest research says about psilocybin, MDMA, DMT, LSD, and ketamine</text>

  <!-- Bottom legend bar -->
  <rect x="40" y="368" width="640" height="40" rx="8" fill="#0f0520" stroke="#1e0a38" stroke-width="1"/>
  <circle cx="78" cy="388" r="6" fill="#f59e0b"/>
  <text x="90" y="392" font-family="Arial,sans-serif" font-size="9" fill="#fcd34d">Psilocybin</text>
  <circle cx="166" cy="388" r="6" fill="#f472b6"/>
  <text x="178" y="392" font-family="Arial,sans-serif" font-size="9" fill="#f9a8d4">MDMA</text>
  <circle cx="236" cy="388" r="6" fill="#2dd4bf"/>
  <text x="248" y="392" font-family="Arial,sans-serif" font-size="9" fill="#5eead4">DMT / Ayahuasca</text>
  <circle cx="356" cy="388" r="6" fill="#60a5fa"/>
  <text x="368" y="392" font-family="Arial,sans-serif" font-size="9" fill="#93c5fd">LSD</text>
  <circle cx="412" cy="388" r="6" fill="#94a3b8"/>
  <text x="424" y="392" font-family="Arial,sans-serif" font-size="9" fill="#cbd5e1">Ketamine</text>
  <text x="600" y="392" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="#4c1d95">18-second orbit</text>
</svg>
</figure>"""

ARTICLE = {
    "title": "Five Psychedelics: What the Latest Research Shows",
    "slug": "psychedelics-psilocybin-mdma-dmt-lsd-ketamine-guide",
    "summary": (
        "Psilocybin, MDMA, DMT, LSD, and ketamine are not the same drug. Each works through "
        "a different mechanism, targets different conditions, and carries a different risk "
        "profile. Researchers Matthew Johnson, Robin Carhart-Harris, Rick Doblin, Michael "
        "Pollan, and Paul Stamets explain what we now know."
    ),
    "order": 1,
    "published": True,
    "content": f"""{SVG_ILLUSTRATION}

<p>For decades, the entire category of psychedelics was legally and scientifically frozen.
Now, in the span of a few years, FDA breakthrough therapy designations, Phase 3 clinical
trials, and a wave of peer-reviewed brain imaging studies have forced medicine to make
distinctions it long refused to make. These are not the same drug. They are not even
the same class of drug. Here is what the research now says about each.</p>

<h2>1. Psilocybin — The Mystical Molecule</h2>

<p>Psilocybin is the active compound in over 200 species of mushrooms. In the body it
converts to psilocin, which binds tightly to serotonin 2A receptors — the same receptors
targeted by antidepressants, but with a radically different effect. Rather than raising
baseline serotonin, psilocybin temporarily disrupts the brain's default mode network:
the system responsible for self-referential thought, rumination, and the narrative sense
of "I."</p>

<p>Neuroscientist Robin Carhart-Harris, who led the first modern brain imaging studies of
psilocybin at Imperial College London, describes the result: "Networks break down. The
strength of the communication between nodes decreases — and it's not just the default mode
network. It's a broad range of high-level networks, those that seem especially expanded in
our species." The experience is often described as ego dissolution — a temporary loss of
the boundary between self and world.</p>

<p>What makes psilocybin medically significant is the correlation between that mystical
quality and clinical outcomes. Matthew Johnson, professor of psychiatry at Johns Hopkins,
has run trials using psilocybin for tobacco addiction, cancer-related anxiety, and
treatment-resistant depression. His finding: "The mystical nature of the experience
correlates with reductions in depression and anxiety." Participants who report the deepest
experiences show the most durable improvements — sometimes years after a single session.</p>

<p>Paul Stamets, mycologist and researcher, points to a mechanism beyond serotonin: "Psilocin
docks with TrkB receptors that lead to proliferation of neurons — neurogenesis, neuroregeneration,
and neuroplasticity. The neurons proliferate and then they shake hands. You have a new pathway."
His lab has dosed human stem cells with psilocin under DEA license and observed increased
neuronal proliferation compared to controls.</p>

<p><strong>What it's being studied for:</strong> treatment-resistant depression, PTSD,
end-of-life anxiety, tobacco addiction, alcohol use disorder, OCD.<br/>
<strong>Status:</strong> FDA Breakthrough Therapy designation for treatment-resistant
depression. Multiple Phase 2 and Phase 3 trials underway.</p>

<h2>2. MDMA — The Empathogen</h2>

<p>MDMA is not a classical psychedelic. It doesn't bind primarily to serotonin 2A receptors.
It causes a massive release of serotonin, dopamine, and oxytocin — creating a state of
emotional openness and dramatically reduced fear response. That combination turns out to be
precisely what trauma therapy has always needed and rarely had.</p>

<p>Rick Doblin, founder of MAPS (Multidisciplinary Association for Psychedelic Studies),
has spent thirty years shepherding MDMA-assisted therapy through the FDA pipeline. In Phase
2 trials for PTSD, the results were striking: two-thirds of participants no longer met
diagnostic criteria for PTSD after three MDMA sessions combined with psychotherapy. "MDMA
works regardless of the cause of PTSD," Doblin says — combat veterans, sexual assault
survivors, first responders. The SSRIs that currently dominate treatment work in women but
"completely failed in combat-related PTSD." MDMA-assisted therapy worked across both.</p>

<p>The mechanism is well understood. MDMA doesn't erase the traumatic memory. It allows the
patient to revisit it without being overwhelmed — what researchers call fear extinction.
The therapeutic window is typically eight hours. During that window, with a trained
therapist present, patients can process memories they could not otherwise approach.</p>

<p>The FDA granted MDMA-assisted psychotherapy for PTSD Breakthrough Therapy designation.
Phase 3 trials have been completed. Approval has been delayed pending additional data
review, but the clinical case is the strongest of any psychedelic therapy to date.</p>

<p><strong>What it's being studied for:</strong> PTSD, social anxiety in autism, alcohol
use disorder, couples therapy.<br/>
<strong>Status:</strong> Breakthrough Therapy designation; Phase 3 complete; under FDA review.</p>

<h2>3. DMT and Ayahuasca — The Ancient Visionary</h2>

<p>DMT (dimethyltryptamine) is among the most powerful psychedelics known, producing
complete immersive hallucinations within seconds of inhalation — what users describe as
"breakthrough" experiences, often involving contact with geometric patterns, other beings,
or an overwhelming sense of another dimension. It is also the active ingredient in
ayahuasca, the Amazonian ceremonial brew that combines DMT-containing plants with
MAO inhibitors that allow the compound to become orally active.</p>

<p>Carhart-Harris has conducted brain imaging studies with DMT, finding similar patterns
to psilocybin but compressed into minutes. "We saw the same kind of effect — hot colors
crossing the brain, regions breaching their borders, speaking more to the rest of the
brain. That's how the mind is made visible."</p>

<p>Michael Pollan, whose book <em>How to Change Your Mind</em> brought psychedelic research
to mainstream attention, notes that both psilocybin and DMT have been used in indigenous
healing traditions for centuries — the Aztecs used mushrooms, South American tribes have
used ayahuasca for an unknown length of time. "This is something that's been happening
for a long time," he says. The modern clinical interest is, in this sense, a rediscovery.</p>

<p>One property shared with psilocybin: classical psychedelics including DMT are
"remarkably non-toxic. There is no known lethal dose of either LSD or psilocybin,"
Pollan notes. The risk profile is primarily psychological, not physiological — the danger
is a destabilizing experience without adequate preparation or support.</p>

<p><strong>What it's being studied for:</strong> depression, addiction, end-of-life distress,
spiritual well-being.<br/>
<strong>Status:</strong> Early clinical trials underway; ayahuasca studied in Brazil
and Spain. No FDA designation yet.</p>

<h2>4. LSD — The Brain's Entropy Machine</h2>

<p>LSD was the first psychedelic to enter systematic clinical research, in the 1950s, where
it was tested for alcoholism, anxiety, and neurosis with promising early results. That
research was shut down entirely by 1970 following its scheduling as a Schedule I substance.
Carhart-Harris's team revived brain imaging of LSD in the 2010s and found something
unexpected: LSD produces a state of dramatically increased brain entropy — a measure of
the variety and unpredictability of brain activity.</p>

<p>"There's an enrichment of the picture," Carhart-Harris explains. "Networks break down,
but what's really happening is a broad expansion — particularly the high-level networks,
those that overlap with what makes us distinctly human." Under LSD, the brain becomes
more flexible, more interconnected, less locked into its usual patterns. This is
consistent with patients reporting that entrenched thought patterns — rumination, rigid
self-narratives, compulsive behaviors — become easier to observe and interrupt.</p>

<p>Pollan describes the addiction research context: "It's a non-addictive drug that seems
effective in dealing with cigarette addiction, alcohol addiction, and cocaine addiction.
You give rats LSD in that lever experiment — they'll press it once and never again." The
classic animal addiction model completely fails with LSD, which is precisely what you'd
expect from a drug that makes habitual behavior harder to sustain.</p>

<p>Six randomized studies using LSD for alcoholism in the 1950s and 60s showed, in
aggregate, roughly doubled rates of improved outcomes at first follow-up. Those results
have never been seriously followed up — until recently.</p>

<p><strong>What it's being studied for:</strong> anxiety, alcohol use disorder, cluster
headaches, cognitive flexibility, depression.<br/>
<strong>Status:</strong> Phase 2 trials underway in Europe and North America.
No FDA designation yet.</p>

<h2>5. Ketamine — The One That's Already Approved</h2>

<p>Ketamine is different from the others in almost every way. It's a dissociative
anesthetic, not a classical psychedelic. It doesn't bind to serotonin 2A receptors — it
blocks NMDA glutamate receptors. The subjective experience is distinct: dissociation,
floating, altered sense of time, sometimes mild hallucinations, but not the full ego
dissolution of psilocybin or LSD.</p>

<p>Its medical distinction: ketamine is the only psychedelic-like compound currently
FDA-approved for treatment-resistant depression. Esketamine (Spravato), a nasal-spray
form of one ketamine isomer, was approved in 2019. IV ketamine infusions are widely
used off-label at ketamine clinics across the US.</p>

<p>Carhart-Harris places ketamine carefully in the psychedelic landscape: "If we only had
compounds like ketamine, MDMA, cannabis — compounds that could be said, broadly speaking,
to be psychedelic-like — I don't think it would have captured the world's attention the
way it has. The classic psychedelics have something different." What ketamine offers is
speed — antidepressant effects often within hours rather than weeks — and an established
regulatory path that the others are still navigating.</p>

<p>For patients who have failed multiple antidepressants, ketamine represents something
that previously didn't exist: a fast-acting alternative. Its therapeutic mechanism may
involve rapid synaptogenesis — the formation of new synaptic connections — triggered
by the glutamate surge following NMDA blockade.</p>

<p><strong>What it's approved for:</strong> treatment-resistant depression (esketamine/Spravato),
general anesthesia.<br/>
<strong>Status:</strong> FDA-approved. Widely available at ketamine clinics. Ongoing
research into optimal dosing and long-term outcomes.</p>

<h2>What They Share</h2>

<p>Despite their differences, Pollan identifies a few properties that hold across the
classical psychedelics: "They are remarkably non-toxic. There is no known lethal dose.
They are not habit forming. The first thought you have upon finishing a psychedelic trip
is not 'when can I do that again?' — it's 'do I ever have to do that again?'"</p>

<p>All of them appear to work, at least in part, by temporarily disrupting the brain's
habitual patterns — the default mode network, the entrenched self-narrative, the
conditioned fear response — and creating a window of increased psychological flexibility.
That window, when used with skilled therapeutic support, seems to be where the healing
happens.</p>

<p>The research is early but the effect sizes are large. For conditions that have resisted
decades of pharmaceutical and therapeutic intervention, that combination is rare enough
to be worth serious attention.</p>

<p><em>Based on talks and interviews by Dr. Matthew Johnson (Johns Hopkins), Dr. Robin
Carhart-Harris (UCSF / Imperial College London), Rick Doblin (MAPS), Michael Pollan
(<em>How to Change Your Mind</em>), and Paul Stamets, collected from YouTube transcripts.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load psychedelics guide article (psilocybin, MDMA, DMT, LSD, ketamine)"

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
            article.title = ARTICLE["title"]
            article.summary = ARTICLE["summary"]
            article.pillar = pillar
            article.published = ARTICLE["published"]
            article.save(update_fields=["title", "summary", "pillar", "published"])
        action = "Created" if created else "Updated (content preserved)"
        self.stdout.write(f"{action} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
