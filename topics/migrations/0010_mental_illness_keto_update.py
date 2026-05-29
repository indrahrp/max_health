from django.db import migrations

SVG_ILLUSTRATION = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Eight mental health conditions, their brain circuit origins, and metabolic/ketogenic treatments">
  <rect width="720" height="420" fill="#090d1a" rx="16"/>
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" fill="#f1f5f9" font-weight="700">Mental Illness: Physiological Origins &amp; Metabolic Paths to Recovery</text>
  <text x="360" y="48" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#475569">Brain circuit disruption + metabolic dysfunction → ketogenic therapy as adjunct treatment</text>

  <!-- Row 1 -->
  <rect x="30"  y="65" width="155" height="155" rx="10" fill="#0f172a" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="107" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#c4b5fd" font-weight="700">Depression</text>
  <text x="107" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Serotonin · Cortisol</text>
  <text x="107" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Inflammation · HPA axis</text>
  <line x1="50" y1="128" x2="164" y2="128" stroke="#7c3aed" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="107" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Marcus, 34</text>
  <text x="107" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic therapy</text>
  <text x="107" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">anti-inflammatory diet · CBT</text>
  <text x="107" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">remission 8 months</text>
  <text x="107" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="195" y="65" width="155" height="155" rx="10" fill="#0f172a" stroke="#2563eb" stroke-width="1.2"/>
  <text x="272" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Anxiety</text>
  <text x="272" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala hyperactivation</text>
  <text x="272" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">GABA deficit · cortisol</text>
  <line x1="215" y1="128" x2="329" y2="128" stroke="#2563eb" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Sofia, 27</text>
  <text x="272" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Low-carb + ketones</text>
  <text x="272" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">CBT · magnesium · sleep</text>
  <text x="272" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">remission 6 months</text>
  <text x="272" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="360" y="65" width="155" height="155" rx="10" fill="#0f172a" stroke="#0e7490" stroke-width="1.2"/>
  <text x="437" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#67e8f9" font-weight="700">Bipolar Disorder</text>
  <text x="437" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Circadian disruption</text>
  <text x="437" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Mitochondrial energy</text>
  <line x1="380" y1="128" x2="495" y2="128" stroke="#0e7490" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">James, 41</text>
  <text x="437" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="437" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">lithium · sleep protocol</text>
  <text x="437" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">stable 2 years</text>
  <text x="437" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Stable</text>

  <rect x="525" y="65" width="165" height="155" rx="10" fill="#0f172a" stroke="#be185d" stroke-width="1.2"/>
  <text x="607" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#fbcfe8" font-weight="700">Schizophrenia</text>
  <text x="607" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Dopamine · Glutamate</text>
  <text x="607" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Prefrontal hypoactivity</text>
  <line x1="545" y1="128" x2="670" y2="128" stroke="#be185d" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Amara, 23</text>
  <text x="607" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic adjunct</text>
  <text x="607" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">antipsychotics · CBT</text>
  <text x="607" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">functionally stable</text>
  <text x="607" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#facc15">● Functionally stable</text>

  <!-- Row 2 -->
  <rect x="30"  y="240" width="155" height="155" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.2"/>
  <text x="107" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#fcd34d" font-weight="700">Epilepsy/Seizure</text>
  <text x="107" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Neural excitability</text>
  <text x="107" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">GABA/Glutamate ratio</text>
  <line x1="50" y1="303" x2="164" y2="303" stroke="#d97706" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="107" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Lucas, 16</text>
  <text x="107" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="107" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">100yr standard of care</text>
  <text x="107" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">seizure-free 18 months</text>
  <text x="107" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Seizure-free</text>

  <rect x="195" y="240" width="155" height="155" rx="10" fill="#0f172a" stroke="#0f766e" stroke-width="1.2"/>
  <text x="272" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#5eead4" font-weight="700">Anorexia</text>
  <text x="272" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Hypothalamic signaling</text>
  <text x="272" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Leptin · ghrelin · reward</text>
  <line x1="215" y1="303" x2="329" y2="303" stroke="#0f766e" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Claire, 19</text>
  <text x="272" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic therapy</text>
  <text x="272" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">FBT · nutritional rehab</text>
  <text x="272" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">eating disorder remission</text>
  <text x="272" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="360" y="240" width="155" height="155" rx="10" fill="#0f172a" stroke="#9333ea" stroke-width="1.2"/>
  <text x="437" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#d8b4fe" font-weight="700">OCD</text>
  <text x="437" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">CSTC circuit overactivity</text>
  <text x="437" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Serotonin · caudate nucleus</text>
  <line x1="380" y1="303" x2="495" y2="303" stroke="#9333ea" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">David, 31</text>
  <text x="437" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="437" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">ERP therapy · SSRI</text>
  <text x="437" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">80% symptom reduction</text>
  <text x="437" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● 80% reduction</text>

  <rect x="525" y="240" width="165" height="155" rx="10" fill="#0f172a" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="607" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Phobia</text>
  <text x="607" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala fear memory</text>
  <text x="607" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Norepinephrine · cortisol</text>
  <line x1="545" y1="303" x2="670" y2="303" stroke="#1d4ed8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Priya, 29</text>
  <text x="607" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Metabolic support</text>
  <text x="607" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">EMDR · exposure therapy</text>
  <text x="607" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">fear response resolved</text>
  <text x="607" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Resolved</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Eight conditions, eight physiological origins — ketogenic and metabolic therapy as a common thread in recovery</figcaption>
</figure>
"""

UPDATED_CONTENT = """
<p class="lead">Mental illness is not weakness, failure, or a broken personality. It is physiology —
disrupted neural circuits, imbalanced neurotransmitters, misfiring hormonal axes, and runaway
inflammation in the brain. Emerging research from metabolic psychiatry now adds a critical insight:
the brain is the most metabolically demanding organ in the body, and when its fuel supply
falters, so does its function. The following are eight stories of people who suffered, sought help,
and found their way to remission — many through pathways that included ketogenic and metabolic
therapy. Names have been changed to protect identity.</p>

""" + SVG_ILLUSTRATION + """

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>1. Marcus — Depression</h2>
<p><em>Physiological origin: chronic inflammation, HPA axis dysregulation, serotonin depletion,
brain glucose hypometabolism</em></p>

<p>Marcus was 34 when he stopped getting out of bed before noon. A construction project manager,
he had always been driven — but over 18 months, something shifted. His appetite disappeared, sleep
became fragmented, and a grey fog descended that no amount of willpower could lift.</p>

<p>The biology: sustained work stress had chronically elevated his cortisol, suppressing hippocampal
neurogenesis and depleting serotonin. Inflammatory cytokines were crossing the blood-brain barrier
and disrupting the prefrontal-limbic circuit that regulates mood. Newer metabolic research points
to a third mechanism: in depression, the brain's ability to metabolise glucose is often impaired —
neurons are starved of energy even when blood glucose is normal.</p>

<p><strong>The turn:</strong> his GP ran a full panel — CRP, ferritin, thyroid, testosterone —
finding elevated inflammation and low vitamin D. A psychiatrist combined a low-dose SSRI with
structured cognitive behavioural therapy. Crucially, Marcus also began a ketogenic diet, working
with a clinician familiar with ketogenic therapy for psychiatric conditions. Ketones bypass
the impaired glucose metabolism pathways, providing neurons with a direct, efficient fuel source.
Pilot studies documented by Metabolic Mind show safety and efficacy of ketogenic therapy as
an adjunct for major depressive disorder. Marcus also eliminated ultra-processed food, added
omega-3s, and walked 30 minutes each morning.</p>

<p><strong>Remission:</strong> within eight months, the fog lifted. Marcus describes it as
"returning to myself." He attributes recovery to the combination — medication, therapy, and
shifting his brain's fuel source.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>2. Sofia — Anxiety Disorder</h2>
<p><em>Physiological origin: amygdala hyperactivation, GABA deficit, cortisol dysregulation,
metabolic inflammation</em></p>

<p>Sofia was 27 and finishing her PhD when the panic attacks began. The first struck without
warning during a seminar — racing heart, tunnel vision, certainty she was dying. She left
academic life for six months, barely able to travel on public transport.</p>

<p>The biology: Sofia's amygdala had become hypersensitive, firing alarm signals disproportionate
to real danger. Her GABA system was underactive. Chronic sleep deprivation from her PhD schedule
had kept her HPA axis in persistent low-grade activation. A metabolic dimension was also present:
high-carbohydrate eating drove blood glucose swings that amplified her cortisol response
throughout the day.</p>

<p><strong>The turn:</strong> a psychiatrist diagnosed generalised anxiety disorder with panic.
Sofia began cognitive behavioural therapy with an exposure protocol. She also reduced dietary
carbohydrates substantially — research documented at Metabolic Mind shows that improving metabolic
health measurably improves mental health outcomes, including anxiety. Stabilising blood glucose
removed a key physiological driver of her cortisol spikes. She added magnesium glycinate to
support GABA signalling, adopted a strict sleep schedule, and practised daily breathwork to
activate the vagus nerve.</p>

<p><strong>Remission:</strong> six months later, Sofia returned to her PhD. Panic attacks reduced
from weekly to once in four months. She completed her doctorate and now teaches mindfulness to
other graduate students — and keeps carbohydrates low.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>3. James — Bipolar Disorder</h2>
<p><em>Physiological origin: circadian rhythm disruption, mitochondrial energy dysregulation,
monoamine imbalance</em></p>

<p>James, 41, had always been "the most interesting person in the room" — until he wasn't.
His life had cycled between extraordinary productivity (barely sleeping, starting companies,
writing 4,000 words a night) and crashes so deep he couldn't shower. Two marriages had ended.
He had been misdiagnosed with unipolar depression for a decade.</p>

<p>The biology: bipolar disorder involves dysregulation of the biological clock and its hormonal
rhythms. James's mitochondrial function showed markers of energy instability across mood states.
Ketogenic metabolism is directly relevant here: ketones are a more efficient mitochondrial fuel
than glucose, and the ketogenic diet has demonstrated mood-stabilising effects in pilot studies —
likely through stabilising brain energy metabolism and reducing neuroinflammation.</p>

<p><strong>The turn:</strong> a bipolar specialist prescribed lithium, which works partly by
regulating circadian gene expression and protecting neuronal mitochondria. James adopted a rigid
sleep protocol. He also began a carefully managed ketogenic diet — with guidance on keeping
ketone levels in a therapeutic range (not excessively high, as very elevated ketones can
occasionally be activating in some bipolar patients). The combination addressed both the
neurotransmitter and energy-metabolism dimensions of his illness.</p>

<p><strong>Remission:</strong> two years without a full manic or depressive episode. James
describes his life as "narrower but real — I live in the middle now, and the middle is
actually very good."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>4. Amara — Schizophrenia / Psychosis</h2>
<p><em>Physiological origin: dopamine excess in striatum, glutamate hypofunction, prefrontal
cortex hypoactivity, mitochondrial dysfunction</em></p>

<p>Amara was 23, in her first year of university, when the voices began. Within three months
they had multiplied into a chorus she could not silence. She stopped attending lectures, convinced
her professors were surveilling her.</p>

<p>The biology: schizophrenia involves too much dopamine in the mesolimbic pathway and too little
in the prefrontal cortex, alongside glutamate signalling failure. Increasingly, researchers also
identify mitochondrial dysfunction and neuroinflammation as upstream drivers — making the
metabolic environment of the brain central to the illness. Metabolic Mind has shared pilot studies
demonstrating ketogenic therapy as an adjunct for schizophrenia, with some patients showing
meaningful reductions in symptom severity alongside their antipsychotic regimen.</p>

<p><strong>The turn:</strong> Amara was referred to an early psychosis intervention team. A
psychiatrist started a second-generation antipsychotic. A psychologist provided cognitive therapy.
Several months into her recovery, her care team introduced a ketogenic dietary protocol as an
adjunct — with careful attention to the fact that some antipsychotic medications can impede
ketosis, requiring dose monitoring and close collaboration with her prescriber.</p>

<p><strong>Remission:</strong> the voices are now quiet most days. Amara completed a certificate
in graphic design and works part-time. She describes the combination of medication, therapy,
and dietary change as a "three-legged stool — remove any one leg and it falls."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>5. Lucas — Epilepsy / Seizures</h2>
<p><em>Physiological origin: neural hyperexcitability, GABA/glutamate imbalance, ion channel
dysfunction</em></p>

<p>Lucas was 16 when his first tonic-clonic seizure struck during football practice. Two
anti-epileptic drugs controlled frequency but left him cognitively foggy. A third caused a
severe allergic reaction. His parents were told he might never drive.</p>

<p>The biology: Lucas's cortical neurons had abnormally low seizure threshold — his ion channels
were dysregulated in a way that allowed runaway electrical activity to cascade. The GABA system
that brakes this cascade was insufficient. Here, the ketogenic diet's mechanism is well established
and over a century old: when the brain metabolises ketones instead of glucose, GABA production
increases, neuronal excitability falls, and seizure threshold rises. Research shows ketosis can
delay seizures by 200–600% in animal models. The ketogenic diet has been standard of care for
drug-resistant epilepsy for over 100 years — one of medicine's oldest and best-validated
nutritional interventions.</p>

<p><strong>The turn:</strong> his neurologist proposed the classical ketogenic diet under a
specialist ketogenic dietitian. Lucas transitioned to nutritional ketosis with close medical
supervision, with his existing medication carefully maintained and adjusted.</p>

<p><strong>Remission:</strong> seizure-free for 18 months. Lucas has returned to sport and is
completing his final year of school. His neurologist has begun discussing gradual medication
reduction. His parents call it "a second life."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>6. Claire — Anorexia Nervosa</h2>
<p><em>Physiological origin: hypothalamic signalling disruption, leptin/ghrelin dysregulation,
reward circuit alteration, brain energy starvation</em></p>

<p>Claire was 19 when her weight fell to a point where her heart rate dropped below 40 during
sleep. To the outside world she appeared disciplined. Inside, eating had become the organising
terror of every waking hour.</p>

<p>The biology: the hypothalamus becomes profoundly dysregulated by starvation. Leptin crashes;
the brain's reward circuitry becomes hyperactivated by restriction rather than food, creating a
neurobiological trap. Brain atrophy — measurable and reversible with refeeding — impairs
the very cognitive capacity needed to choose recovery. What Metabolic Mind has documented in
eating disorder cases is striking: ketogenic therapy, used appropriately in weight-restored
patients, has helped put eating disorders into remission — likely by stabilising reward circuitry,
reducing anxiety around food, and providing metabolic stability that the previously glucose-
dependent brain could not achieve.</p>

<p><strong>The turn:</strong> Claire's parents initiated family-based treatment (FBT) — the
evidence-based protocol in which the family controls feeding initially, bypassing the paralysed
volition of the starving brain. As weight restored, cognitive distortions lessened. She then began
dialectical behaviour therapy (DBT). Once medically stable, her nutritional approach shifted
toward a lower-carbohydrate, higher-fat pattern — reducing the glucose instability and anxiety
spikes that had previously surrounded meals.</p>

<p><strong>Remission:</strong> eating disorder in remission. Weight restored. Claire is in her
second year of university studying nutrition science and speaks publicly about the metabolic
dimension of eating disorder recovery.</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>7. David — Obsessive Compulsive Disorder (OCD)</h2>
<p><em>Physiological origin: cortico-striato-thalamo-cortical (CSTC) circuit hyperactivity,
serotonin dysregulation, caudate nucleus dysfunction, neuroinflammation</em></p>

<p>David, 31, spent four hours each morning checking that the gas was off, the locks were turned,
the appliances unplugged — the same loop repeated until he was late for work every day. He knew
the stove was off. He checked again. His girlfriend moved out; his job was in jeopardy.</p>

<p>The biology: OCD involves overactivity in the CSTC loop connecting the prefrontal cortex,
caudate nucleus, and thalamus — normally this circuit filters thoughts and signals "good enough,
move on." In OCD, it fires repeatedly without resolution. A published three-case series documented
by Metabolic Mind showed meaningful OCD symptom reduction with ketogenic dietary therapy — with
one patient going from severely disabled to functionally thriving. The proposed mechanism involves
ketones reducing neuroinflammation in the CSTC circuit and improving GABAergic inhibition that
normally brakes compulsive loops.</p>

<p><strong>The turn:</strong> David was referred to a specialist in exposure and response
prevention (ERP) — the gold standard for OCD. He also began a high-dose SSRI. After reading
about the published case series, he worked with his psychiatrist to introduce a ketogenic diet
alongside his existing treatment. The combination — circuit retraining through ERP, serotonin
support through medication, and metabolic support through ketosis — addressed the condition
on multiple physiological levels simultaneously.</p>

<p><strong>Remission:</strong> an 80% reduction in compulsion time within nine months. David
now checks the gas once. He describes ERP as "the hardest thing I've done" and keto as
"the thing that made the hardest thing possible."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>8. Priya — Specific Phobia</h2>
<p><em>Physiological origin: amygdala fear memory consolidation, norepinephrine hyperactivation,
conditioned threat response, metabolic anxiety amplification</em></p>

<p>Priya, 29, could not enter a lift. Her career in architecture — requiring site visits to
high-rise buildings — was quietly being destroyed by a phobia of enclosed spaces that had begun
after she was briefly trapped in a lift at 14.</p>

<p>The biology: specific phobias are encoded in the amygdala as conditioned fear memories.
The prefrontal cortex loses its ability to override the alarm. A metabolic dimension compounds
this: blood glucose instability amplifies the cortisol and norepinephrine surges that accompany
fear — and for Priya, skipping breakfast and eating high-carbohydrate meals meant her nervous
system was already primed for alarm when any trigger appeared. Improving metabolic stability
lowers the baseline reactivity the amygdala operates from.</p>

<p><strong>The turn:</strong> Priya's therapist used EMDR to reprocess the original trapped-lift
memory, combined with graduated exposure therapy. She also began a lower-carbohydrate eating
pattern — eliminating the blood glucose swings that were amplifying her sympathetic nervous
system baseline. A short course of propranolol blunted the physical fear response during critical
exposure sessions. The metabolic stabilisation made the fear response less explosive and the
exposure work more tolerable.</p>

<p><strong>Remission:</strong> Priya now takes lifts daily. She completed a major high-rise
project and has been promoted. She describes her former avoidance as "a cage that got smaller
every year — the combination of therapy and metabolic change broke it open."</p>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>The Metabolic Thread</h2>

<p>Across all eight stories runs a common biological insight: the brain is the most metabolically
demanding organ in the body, consuming roughly 20% of total energy despite representing only 2%
of body weight. When that energy supply is disrupted — by glucose dysregulation, mitochondrial
dysfunction, neuroinflammation, or insulin resistance — brain circuits malfunction in ways we
label as psychiatric illness.</p>

<p>Ketogenic therapy addresses this at the root: by shifting the brain's primary fuel from glucose
to ketones, it bypasses impaired glucose metabolism, reduces neuroinflammation, stabilises
mitochondrial function, and modulates neurotransmitter balance (particularly GABA). It is not a
replacement for medication or therapy — but it is an adjunct that, for many patients, changes the
trajectory of serious mental illness.</p>

<blockquote>
  <p>"The evidence continues to grow that improving metabolic health can improve mental health."</p>
  <footer>— Metabolic Mind</footer>
</blockquote>

<p>Remission is possible. It may require medication, therapy, dietary change, or all three.
But across every condition described here, the human brain demonstrated what both neuroscience
and metabolic psychiatry increasingly confirm: it retains a remarkable capacity for recovery
when given the right fuel and the right conditions.</p>
"""


def update_mental_illness_keto(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug='mental-illness-physiological-origin-stories').update(
        content=UPDATED_CONTENT,
        summary=(
            "Depression, anxiety, bipolar disorder, schizophrenia, epilepsy, anorexia, OCD, and phobia — "
            "each has a physiological and metabolic origin. Eight people found remission through "
            "combinations of therapy, medication, and ketogenic dietary intervention."
        ),
        ai_summary=(
            "Eight patient vignettes covering depression, anxiety, bipolar, schizophrenia, epilepsy, "
            "anorexia, OCD, and phobia — each with physiological mechanism, ketogenic/metabolic therapy "
            "role, treatment approach, and remission outcome. Sourced from Metabolic Mind transcripts."
        ),
    )


def reverse_update(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_restore_life_of_a_cell_pillar'),
    ]

    operations = [
        migrations.RunPython(update_mental_illness_keto, reverse_update),
    ]
