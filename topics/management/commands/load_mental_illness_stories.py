from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Mental Health",
    "slug": "mental-health",
    "description": (
        "Mental illness is not a character flaw — it is a physiological condition rooted in "
        "brain chemistry, neural circuitry, hormones, and inflammation. These are stories of "
        "real struggles and real recoveries."
    ),
    "icon": "🧠",
    "color": "violet",
    "order": 8,
}

SVG_ILLUSTRATION = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Eight mental health conditions and their brain circuit origins">
  <rect width="720" height="380" fill="#090d1a" rx="16"/>
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" fill="#f1f5f9" font-weight="700">Mental Illness: Physiological Origins in the Brain</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#475569">Each condition maps to disrupted circuits, chemistry, and physiology — not character flaws</text>

  <!-- Row 1: 4 conditions -->
  <!-- Depression -->
  <rect x="30"  y="65" width="155" height="130" rx="10" fill="#0f172a" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="107" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#c4b5fd" font-weight="700">Depression</text>
  <text x="107" y="102" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Serotonin · Cortisol</text>
  <text x="107" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Inflammation · HPA axis</text>
  <line x1="50" y1="130" x2="164" y2="130" stroke="#7c3aed" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="107" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Marcus, 34</text>
  <text x="107" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Anti-inflammatory diet</text>
  <text x="107" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">therapy · remission 8mo</text>
  <text x="107" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <!-- Anxiety -->
  <rect x="195" y="65" width="155" height="130" rx="10" fill="#0f172a" stroke="#2563eb" stroke-width="1.2"/>
  <text x="272" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Anxiety</text>
  <text x="272" y="102" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala hyperactivation</text>
  <text x="272" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">GABA deficit · cortisol</text>
  <line x1="215" y1="130" x2="329" y2="130" stroke="#2563eb" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Sofia, 27</text>
  <text x="272" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">CBT · magnesium</text>
  <text x="272" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">breathwork · remission 6mo</text>
  <text x="272" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <!-- Bipolar -->
  <rect x="360" y="65" width="155" height="130" rx="10" fill="#0f172a" stroke="#0e7490" stroke-width="1.2"/>
  <text x="437" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#67e8f9" font-weight="700">Bipolar Disorder</text>
  <text x="437" y="102" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Circadian disruption</text>
  <text x="437" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Mitochondrial energy</text>
  <line x1="380" y1="130" x2="495" y2="130" stroke="#0e7490" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">James, 41</text>
  <text x="437" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Lithium · sleep protocol</text>
  <text x="437" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">ketogenic diet · stable 2yr</text>
  <text x="437" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Stable</text>

  <!-- Schizophrenia -->
  <rect x="525" y="65" width="165" height="130" rx="10" fill="#0f172a" stroke="#be185d" stroke-width="1.2"/>
  <text x="607" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#fbcfe8" font-weight="700">Schizophrenia</text>
  <text x="607" y="102" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Dopamine · Glutamate</text>
  <text x="607" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Prefrontal hypoactivity</text>
  <line x1="545" y1="130" x2="670" y2="130" stroke="#be185d" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Amara, 23</text>
  <text x="607" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Antipsychotics · CBT</text>
  <text x="607" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">family therapy · functional</text>
  <text x="607" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#facc15">● Functionally stable</text>

  <!-- Row 2: 4 conditions -->
  <!-- Seizure -->
  <rect x="30"  y="215" width="155" height="130" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.2"/>
  <text x="107" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#fcd34d" font-weight="700">Epilepsy/Seizure</text>
  <text x="107" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Neural excitability</text>
  <text x="107" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">GABA/Glutamate ratio</text>
  <line x1="50" y1="280" x2="164" y2="280" stroke="#d97706" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="107" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Lucas, 16</text>
  <text x="107" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Ketogenic diet</text>
  <text x="107" y="323" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">anti-epileptics · seizure-free</text>
  <text x="107" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Seizure-free 18mo</text>

  <!-- Anorexia -->
  <rect x="195" y="215" width="155" height="130" rx="10" fill="#0f172a" stroke="#0f766e" stroke-width="1.2"/>
  <text x="272" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#5eead4" font-weight="700">Anorexia</text>
  <text x="272" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Hypothalamic signaling</text>
  <text x="272" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Leptin · ghrelin · reward</text>
  <line x1="215" y1="280" x2="329" y2="280" stroke="#0f766e" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Claire, 19</text>
  <text x="272" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">FBT · nutritional rehab</text>
  <text x="272" y="323" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">DBT · weight restored</text>
  <text x="272" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Weight restored</text>

  <!-- OCD -->
  <rect x="360" y="215" width="155" height="130" rx="10" fill="#0f172a" stroke="#9333ea" stroke-width="1.2"/>
  <text x="437" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#d8b4fe" font-weight="700">OCD</text>
  <text x="437" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">CSTC circuit overactivity</text>
  <text x="437" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Serotonin · caudate nucleus</text>
  <line x1="380" y1="280" x2="495" y2="280" stroke="#9333ea" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">David, 31</text>
  <text x="437" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">ERP therapy · SSRI</text>
  <text x="437" y="323" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">mindfulness · 80% reduction</text>
  <text x="437" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● 80% symptom reduction</text>

  <!-- Phobia -->
  <rect x="525" y="215" width="165" height="130" rx="10" fill="#0f172a" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="607" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Phobia</text>
  <text x="607" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala fear memory</text>
  <text x="607" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Norepinephrine · cortisol</text>
  <line x1="545" y1="280" x2="670" y2="280" stroke="#1d4ed8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Priya, 29</text>
  <text x="607" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Exposure therapy</text>
  <text x="607" y="323" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">EMDR · propranolol · free</text>
  <text x="607" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Fear response resolved</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Eight conditions, eight physiological origins, eight paths to remission</figcaption>
</figure>
"""

ARTICLE_CONTENT = """
<p class="lead">Mental illness is not weakness, failure, or a broken personality. It is physiology —
disrupted neural circuits, imbalanced neurotransmitters, misfiring hormonal axes, and runaway
inflammation in the brain. The following are eight stories of people who suffered, sought help,
and found their way to remission. Names have been changed to protect identity.</p>

""" + SVG_ILLUSTRATION + """

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>1. Marcus — Depression</h2>
<p><em>Physiological origin: chronic inflammation, HPA axis dysregulation, serotonin depletion</em></p>

<p>Marcus was 34 when he stopped getting out of bed before noon. A construction project manager,
he had always been driven — but over 18 months, something shifted. His appetite disappeared, sleep
became fragmented, and a grey fog descended that no amount of willpower could lift. He assumed
he was lazy. His wife knew better.</p>

<p>What was happening in Marcus's brain: sustained work stress had chronically elevated his cortisol,
suppressing hippocampal neurogenesis and depleting serotonin. Inflammatory cytokines — measurable
in his blood — were crossing the blood-brain barrier and disrupting the prefrontal-limbic circuit
that regulates mood. His depression was as biological as a broken leg, invisible only because
brain scans aren't routine.</p>

<p><strong>The turn:</strong> his GP ran a full panel — CRP, ferritin, thyroid, testosterone — and
found elevated inflammation and low vitamin D. He was referred to a psychiatrist who combined a
low-dose SSRI with structured cognitive behavioural therapy. Marcus also changed his diet,
eliminating ultra-processed food and adding omega-3s. He began walking 30 minutes each morning.</p>

<p><strong>Remission:</strong> within eight months, the fog lifted. Marcus describes it as
"returning to myself." He still sees his therapist monthly and remains aware that stress is
a biological trigger — not just a mindset problem.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>2. Sofia — Anxiety Disorder</h2>
<p><em>Physiological origin: amygdala hyperactivation, GABA deficit, cortisol dysregulation</em></p>

<p>Sofia was 27 and finishing her PhD when the panic attacks began. The first struck without
warning during a seminar — racing heart, tunnel vision, certainty she was dying. She left
academic life for six months, barely able to travel on public transport. Avoiding triggers
only widened her world of fear.</p>

<p>The biology: Sofia's amygdala — the brain's threat-detection centre — had become hypersensitive,
firing alarm signals disproportionate to real danger. Her GABA system, the brain's primary
inhibitory neurotransmitter network, was underactive. Chronic sleep deprivation from her PhD
schedule had compounded both problems, keeping her HPA axis in a state of persistent
low-grade activation.</p>

<p><strong>The turn:</strong> a psychiatrist diagnosed generalised anxiety disorder with panic.
Sofia began weekly cognitive behavioural therapy with an exposure protocol — gradually and
deliberately facing feared situations. She added magnesium glycinate (shown to support GABA
signalling), reduced caffeine, and adopted a strict sleep schedule. Diaphragmatic breathwork
— physiologically proven to activate the vagus nerve and dampen the sympathetic response —
became a daily practice.</p>

<p><strong>Remission:</strong> six months later, Sofia returned to her PhD. Panic attacks
reduced from weekly to once in four months. She completed her doctorate and now teaches
mindfulness to other graduate students.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>3. James — Bipolar Disorder</h2>
<p><em>Physiological origin: circadian rhythm disruption, mitochondrial energy dysregulation,
monoamine imbalance</em></p>

<p>James, 41, had always been "the most interesting person in the room" — until he wasn't.
His life had cycled between periods of extraordinary productivity (barely sleeping, starting
companies, writing 4,000 words a night) and crashes so deep he couldn't shower. Two marriages
had ended. He had been misdiagnosed with unipolar depression for a decade.</p>

<p>The biology: bipolar disorder involves dysregulation of the biological clock — the suprachiasmatic
nucleus and its downstream hormonal rhythms. James's mitochondrial function showed markers of
energy instability across mood states. His manic phases corresponded to dopamine and norepinephrine
surges; his depressive phases to their collapse. The circadian system that should anchor mood was
chronically disrupted by irregular sleep, alcohol, and years of ignoring early warning signs.</p>

<p><strong>The turn:</strong> a bipolar specialist prescribed lithium — one of psychiatry's oldest
and most effective mood stabilisers, which works partly by regulating circadian gene expression
and protecting neuronal mitochondria. James adopted a rigid sleep protocol: same bedtime and wake
time every day, including weekends. He also began a modified ketogenic diet, which emerging
research suggests stabilises brain energy metabolism in bipolar disorder.</p>

<p><strong>Remission:</strong> two years without a full manic or depressive episode. James
describes his life as "narrower but real — I live in the middle now, and the middle is
actually very good."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>4. Amara — Schizophrenia / Psychosis</h2>
<p><em>Physiological origin: dopamine excess in striatum, glutamate hypofunction, prefrontal
cortex hypoactivity</em></p>

<p>Amara was 23, in her first year of university, when the voices began. Soft at first —
comments on her behaviour, whispered warnings. Within three months they had multiplied into
a chorus she could not silence. She stopped attending lectures, convinced her professors were
surveilling her. Her family noticed she had stopped recognising close friends.</p>

<p>The biology: schizophrenia involves too much dopamine activity in the mesolimbic pathway
(producing hallucinations and delusions) and too little in the prefrontal cortex (producing
cognitive flattening). Glutamate signalling through NMDA receptors is underactive, which
further disrupts the brain's ability to filter irrelevant information from meaningful signal.
Neuroimaging shows reduced grey matter in prefrontal areas and enlarged ventricles in some
patients — this is structural, not imagined.</p>

<p><strong>The turn:</strong> Amara's family brought her to an early psychosis intervention
team — a specialised service that combines antipsychotic medication, cognitive therapy, and
family education. She began a low-dose second-generation antipsychotic that rebalances
dopamine without the numbing side effects of older medications. A psychologist helped her
develop skills to evaluate the reality of her perceptions. Her family learned not to argue
with her beliefs but to remain calm anchors of consistency.</p>

<p><strong>Remission:</strong> the voices are now quiet most days. Amara completed a
certificate in graphic design and works part-time. She will likely remain on medication
long-term, which she accepts as she would any chronic physiological condition.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>5. Lucas — Epilepsy / Seizures</h2>
<p><em>Physiological origin: neural hyperexcitability, GABA/glutamate imbalance, ion channel
dysfunction</em></p>

<p>Lucas was 16 when his first tonic-clonic seizure struck during football practice. What
followed was a two-year ordeal: two anti-epileptic drugs that controlled frequency but left
him cognitively foggy and unable to concentrate in school. A third drug caused a severe
allergic reaction. His parents were told he might never drive, might always need supervision.</p>

<p>The biology: Lucas's seizures arose from a focal region of cortical neurons with abnormally
low seizure threshold — his ion channels were dysregulated in a way that allowed runaway
electrical activity to cascade across brain networks. The GABA system that normally brakes
this cascade was insufficient. His EEG confirmed left temporal lobe origin.</p>

<p><strong>The turn:</strong> his neurologist proposed the classical ketogenic diet — a
high-fat, very-low-carbohydrate protocol that has been used for drug-resistant epilepsy
since the 1920s. When the brain metabolises ketones instead of glucose, GABA production
increases and neuronal excitability falls. Lucas was admitted for a supervised dietary
transition under a ketogenic dietitian and neurologist.</p>

<p><strong>Remission:</strong> seizure-free for 18 months. He has returned to sport, is
completing his final year of school, and his neurologist has begun discussing gradual
medication reduction. His parents call it "a second life."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>6. Claire — Anorexia Nervosa</h2>
<p><em>Physiological origin: hypothalamic signalling disruption, leptin/ghrelin dysregulation,
reward circuit alteration</em></p>

<p>Claire was 19 when her weight fell to a point where her heart rate dropped below 40 during
sleep. To the outside world she appeared disciplined and high-achieving. Inside, eating had
become the organising terror of every waking hour — an obsession her family first mistook
for a diet.</p>

<p>The biology: anorexia is not vanity. The hypothalamus — the brain's metabolic command
centre — becomes profoundly dysregulated as starvation sets in. Leptin (the satiety hormone)
crashes; ghrelin (the hunger hormone) paradoxically stops sending distress signals at low
weight in many patients. The brain's reward circuitry, particularly the dopaminergic pathway,
becomes hyperactivated by restriction rather than food, creating a neurobiological trap.
Starvation also causes measurable brain atrophy, reversible with refeeding.</p>

<p><strong>The turn:</strong> Claire's parents initiated family-based treatment (FBT) —
an evidence-based protocol in which the family, not the patient, initially controls feeding.
This bypasses the paralysed volition of the starving brain and begins physical recovery.
As weight restored, Claire's cognitive distortions lessened — not because of willpower,
but because a properly nourished brain can think. She then began dialectical behaviour
therapy (DBT) to build emotional regulation skills.</p>

<p><strong>Remission:</strong> weight restored. Claire is now in her second year of
university studying nutrition science. She speaks publicly about eating disorder recovery
and the physiology that underpins it.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>7. David — Obsessive Compulsive Disorder (OCD)</h2>
<p><em>Physiological origin: cortico-striato-thalamo-cortical (CSTC) circuit hyperactivity,
serotonin dysregulation, caudate nucleus dysfunction</em></p>

<p>David, 31, spent four hours each morning checking that the gas was off, the locks were
turned, the appliances unplugged — the same loop repeated until he was late for work every
day. He knew the stove was off. He had checked forty times. He checked again. His girlfriend
eventually moved out; his job was in jeopardy.</p>

<p>The biology: OCD involves overactivity in the CSTC circuit — a loop connecting the
prefrontal cortex, caudate nucleus, and thalamus. Normally this circuit filters thoughts
and signals "good enough, move on." In OCD, it fires repeatedly without resolution,
generating the experience of incompleteness and the compulsion to act again. Serotonin
modulates this circuit; its dysfunction is why SSRIs at higher doses are effective in OCD
specifically (they are targeting circuit function, not just mood).</p>

<p><strong>The turn:</strong> David was referred to a specialist in exposure and response
prevention (ERP) — the gold standard for OCD. ERP involves deliberately triggering the
obsessive thought without performing the compulsion, allowing the anxiety to peak and fall
without reinforcement. It is uncomfortable and requires courage. His psychiatrist added
a high-dose SSRI. David also began mindfulness practice to develop non-reactive awareness
of intrusive thoughts.</p>

<p><strong>Remission:</strong> an 80% reduction in compulsion time within nine months.
David now checks the gas once. He returned to full work hours and is in a new relationship.
He describes ERP as "the hardest and most important thing I have ever done."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>8. Priya — Specific Phobia</h2>
<p><em>Physiological origin: amygdala fear memory consolidation, norepinephrine hyperactivation,
conditioned threat response</em></p>

<p>Priya, 29, could not enter a lift. Her career in architecture — which required site visits
to high-rise buildings — was quietly being destroyed by a phobia of enclosed spaces that had
begun after she was briefly trapped in a lift at 14. The memory had encoded a fear response so
powerful that even imagining a lift caused her heart to race and her vision to narrow.</p>

<p>The biology: specific phobias are encoded in the amygdala as conditioned fear memories.
A single traumatic episode can wire the amygdala to fire a full threat response — norepinephrine
surge, cortisol spike, sympathetic activation — to any stimulus resembling the original trigger.
The prefrontal cortex, which normally inhibits amygdala responses through learned safety signals,
loses its ability to override the alarm. The memory is not irrational — it is inscribed in
neural circuitry.</p>

<p><strong>The turn:</strong> Priya's therapist used a combination of EMDR (eye movement
desensitisation and reprocessing) to reprocess the original trapped-lift memory, and graduated
exposure therapy — starting with looking at photographs of lifts, then standing outside one,
then entering with the door open, eventually riding alone. Her psychiatrist prescribed a
short course of propranolol (a beta-blocker) to blunt the physical fear response during
critical exposure sessions, making it possible for her to tolerate the process.</p>

<p><strong>Remission:</strong> Priya now takes lifts daily. She completed a major high-rise
project and has been promoted. She describes her former avoidance as "a cage that got smaller
every year — exposure broke it open."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>A Note on Physiological Origin</h2>

<p>These eight stories share a common thread: the suffering was real, the biology was real,
and the recovery was real. Mental illness sits at the intersection of genetics, environment,
stress physiology, nutrition, sleep, and neural circuitry. Characterising it as weakness
or a failure of will is not only wrong — it delays people from seeking the help that can
genuinely change their brain biology.</p>

<p>Remission is possible. It may require medication, therapy, dietary change, or all three.
It requires time. But across every condition described here, the human brain demonstrated
what neuroscience increasingly confirms: it retains a remarkable capacity for change —
neuroplasticity in service of recovery — when given the right conditions.</p>

<blockquote>
  <p>"The brain is not the author of mental illness. It is also the organ of recovery."</p>
</blockquote>
"""


def create_mental_illness_stories(apps=None, schema_editor=None):
    if apps:
        PillarModel = apps.get_model('topics', 'Pillar')
        ArticleModel = apps.get_model('topics', 'Article')
    else:
        PillarModel = Pillar
        ArticleModel = Article

    pillar, _ = PillarModel.objects.get_or_create(
        slug=PILLAR["slug"],
        defaults={
            "name": PILLAR["name"],
            "description": PILLAR["description"],
            "icon": PILLAR["icon"],
            "color": PILLAR["color"],
            "order": PILLAR["order"],
        },
    )

    ArticleModel.objects.update_or_create(
        slug="mental-illness-physiological-origin-stories",
        defaults={
            "title": "When the Brain Breaks: Eight Stories of Mental Illness, Physiology, and Recovery",
            "summary": (
                "Depression, anxiety, bipolar disorder, schizophrenia, epilepsy, anorexia, OCD, and phobia — "
                "each has a physiological origin in disrupted brain circuits and chemistry. "
                "Eight people. Eight diagnoses. Eight paths to remission."
            ),
            "content": ARTICLE_CONTENT,
            "pillar": pillar,
            "order": 1,
            "published": True,
            "ai_summary": (
                "Eight patient vignettes (first name only) covering depression, anxiety, bipolar, "
                "schizophrenia, epilepsy, anorexia, OCD, and specific phobia — each with physiological "
                "mechanism, treatment approach, and remission outcome."
            ),
        },
    )


def reverse_mental_illness_stories(apps, schema_editor):
    ArticleModel = apps.get_model('topics', 'Article')
    PillarModel = apps.get_model('topics', 'Pillar')
    ArticleModel.objects.filter(slug="mental-illness-physiological-origin-stories").delete()
    PillarModel.objects.filter(slug=PILLAR["slug"]).delete()


class Command(BaseCommand):
    help = "Load Mental Health pillar and mental illness stories article"

    def handle(self, *args, **options):
        create_mental_illness_stories()
        self.stdout.write(self.style.SUCCESS("Done."))
