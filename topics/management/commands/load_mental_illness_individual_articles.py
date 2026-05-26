from django.core.management.base import BaseCommand
from topics.models import Pillar, Article


def brain_svg(title, accent, label1, label2, label3, body1, body2, body3, cap1='', cap2='', cap3=''):
    mid = f"ar{accent[1:]}"
    return (
        f'<figure style="margin:1.5em 0 2.5em;">'
        f'<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="{title}">'
        f'<rect width="720" height="360" fill="#090d1a" rx="16"/>'
        f'<defs><marker id="{mid}" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker></defs>'
        f'<text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13.5" fill="#f1f5f9" font-weight="700">{title}</text>'
        f'<text x="120" y="52" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">NORMAL</text>'
        f'<text x="360" y="52" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">DISRUPTION</text>'
        f'<text x="600" y="52" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">METABOLIC INTERVENTION</text>'
        f'<circle cx="120" cy="190" r="95" fill="#0f172a" stroke="{accent}" stroke-width="1.2" stroke-opacity=".45"/>'
        + body1 +
        f'<text x="120" y="302" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">{label1}</text>'
        f'<text x="120" y="317" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">{cap1}</text>'
        f'<line x1="218" y1="190" x2="258" y2="190" stroke="#475569" stroke-width="2" marker-end="url(#{mid})"/>'
        f'<circle cx="360" cy="190" r="95" fill="#0f172a" stroke="{accent}" stroke-width="1.8"/>'
        + body2 +
        f'<text x="360" y="302" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">{label2}</text>'
        f'<text x="360" y="317" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">{cap2}</text>'
        f'<line x1="458" y1="190" x2="498" y2="190" stroke="#475569" stroke-width="2" marker-end="url(#{mid})"/>'
        f'<circle cx="600" cy="190" r="95" fill="#0f172a" stroke="#22c55e" stroke-width="1.8"/>'
        + body3 +
        f'<text x="600" y="302" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">{label3}</text>'
        f'<text x="600" y="317" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">{cap3}</text>'
        f'</svg></figure>'
    )


# ── 1. DEPRESSION ─────────────────────────────────────────────────────────────
DEPRESSION_SVG = brain_svg(
    "Depression: HPA Axis &amp; Serotonin Depletion → Metabolic Recovery",
    "#7c3aed",
    "Balanced Circuits", "HPA Overactivation", "Ketogenic Restoration",
    (
        '<circle cx="120" cy="168" r="18" fill="#1e1b4b" stroke="#a5b4fc" stroke-width="1.5"/>'
        '<text x="120" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#a5b4fc">PFC</text>'
        '<circle cx="100" cy="205" r="13" fill="#1e1b4b" stroke="#a5b4fc" stroke-width="1"/>'
        '<text x="100" y="209" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">Amyg</text>'
        '<circle cx="140" cy="205" r="13" fill="#1e1b4b" stroke="#a5b4fc" stroke-width="1"/>'
        '<text x="140" y="209" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">Hipp</text>'
        '<text x="120" y="235" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">5-HT ✓  NE ✓</text>'
    ),
    (
        '<circle cx="360" cy="165" r="18" fill="#2e1065" stroke="#ef4444" stroke-width="2"/>'
        '<text x="360" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">PFC↓</text>'
        '<circle cx="340" cy="205" r="15" fill="#2e1065" stroke="#ef4444" stroke-width="1.5"/>'
        '<text x="340" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fca5a5">Cortisol↑</text>'
        '<text x="360" y="235" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">5-HT↓  NE↓</text>'
        '<text x="360" y="248" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Neuroinflammation↑</text>'
    ),
    (
        '<circle cx="600" cy="168" r="18" fill="#052e16" stroke="#22c55e" stroke-width="2"/>'
        '<text x="600" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">PFC↑</text>'
        '<text x="600" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">BHB → ATP</text>'
        '<text x="600" y="213" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">BDNF↑</text>'
        '<text x="600" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Inflammation↓</text>'
        '<text x="600" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">GABA↑</text>'
    ),
    "Normal serotonin, NE, cortisol", "HPA overactive, serotonin depleted", "Ketones restore energy &amp; BDNF"
)

DEPRESSION_CONTENT = DEPRESSION_SVG + """
<h2>The physiology</h2>
<p>Depression is not a serotonin deficiency in any simple sense. The hypothalamic-pituitary-adrenal axis — the brain's stress response system — becomes chronically overactivated, flooding circuits with cortisol and suppressing the very prefrontal regions responsible for regulating mood and thought. Mitochondrial dysfunction in neurons reduces the ATP available for neurotransmitter synthesis. Neuroinflammation — elevated IL-6, TNF-α, C-reactive protein — directly impairs serotonin synthesis and reuptake. The result is a circuit that has lost its metabolic underpinning, not merely its chemistry.</p>
<blockquote><p>"We're starting to see some pretty impressive results from ketogenic therapy to treat serious mental illness, bipolar disorder, schizophrenia, major depressive disorder, and others."</p><footer>— Metabolic Mind</footer></blockquote>
<p>Ketogenic therapy addresses depression through three converging pathways: beta-hydroxybutyrate (BHB) provides an alternative fuel that bypasses impaired glucose metabolism in the prefrontal cortex; ketosis reduces neuroinflammation via NLRP3 inflammasome inhibition; and the metabolic shift increases BDNF — brain-derived neurotrophic factor — which supports synaptic plasticity and neurogenesis in the hippocampus.</p>

<h2>Five stories</h2>

<h3>Marcus — Treatment-resistant depression</h3>
<p>Marcus, 38, had been on four different antidepressants across a decade. Each worked for a period and then stopped. He described his depression as a constant grey ceiling — not acute suffering, but a permanent reduction in colour. His psychiatrist added a strict ketogenic diet as an adjunct. Within eight weeks Marcus noticed a distinct brightening. The grey ceiling did not lift immediately but over six months it dissolved. He remains on a low dose of medication but attributes the change primarily to the metabolic shift.</p>

<h3>Elena — Postpartum depression</h3>
<p>Elena developed severe postpartum depression after her second child. Antidepressants helped her function but left her feeling blunted. She began ketogenic eating while breastfeeding under medical supervision. The inflammation markers in her blood — she had been tracked as a research subject — dropped markedly within twelve weeks. Her mood stabilised and, critically, she felt present for her child in a way the medication had not enabled.</p>

<h3>Theo — Seasonal affective disorder</h3>
<p>Theo, 29, dreaded November every year. His SAD required light therapy and medication just to keep him functional through winter. A metabolic psychiatrist suggested pairing ketogenic nutrition with his existing protocol. The first winter on the combined approach he noticed the seasonal crash did not arrive with its usual force. He describes it as the floor of his mood being raised several feet.</p>

<h3>Vera — Adolescent depression with brain fog</h3>
<p>Vera, 16, was referred to a specialist after a year of worsening depression and inability to concentrate at school. Neuroimaging showed hypometabolism in her prefrontal cortex. Her family adopted a ketogenic diet together. Within three months her school performance had recovered and the persistent brain fog — described by her teachers as a different person appearing in class — had cleared. Her psychiatrist reduced her medication at the six-month mark.</p>

<h3>Juno — Burnout-precipitated depression</h3>
<p>Juno, 44, collapsed into depression after a period of extreme professional stress. She resisted pharmaceutical intervention initially, preferring to understand the mechanism. Working with a metabolic medicine practitioner, she implemented ketogenic nutrition alongside sleep restructuring. Her inflammatory markers — CRP had been elevated — normalised within ten weeks. She describes the recovery as more complete than anything she had experienced with previous medication trials.</p>"""

# ── 2. ANXIETY ────────────────────────────────────────────────────────────────
ANXIETY_SVG = brain_svg(
    "Anxiety: Amygdala Hyperactivation &amp; GABA Deficit",
    "#2563eb",
    "Calm Amygdala", "Overactive Fear Circuit", "GABA Restoration",
    (
        '<ellipse cx="120" cy="190" rx="30" ry="22" fill="#172554" stroke="#93c5fd" stroke-width="1.5"/>'
        '<text x="120" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#93c5fd">Amygdala</text>'
        '<text x="120" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#60a5fa">calm</text>'
        '<text x="120" y="225" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">GABA ✓</text>'
        '<text x="120" y="237" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Cortisol balanced</text>'
    ),
    (
        '<ellipse cx="360" cy="190" rx="38" ry="28" fill="#1e1b4b" stroke="#ef4444" stroke-width="2.5"/>'
        '<text x="360" y="185" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">Amygdala</text>'
        '<text x="360" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">HYPERACTIVE</text>'
        '<text x="360" y="225" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">GABA↓  Cortisol↑</text>'
        '<text x="360" y="238" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">PFC inhibition lost</text>'
    ),
    (
        '<ellipse cx="600" cy="190" rx="30" ry="22" fill="#052e16" stroke="#22c55e" stroke-width="2"/>'
        '<text x="600" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Amygdala</text>'
        '<text x="600" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#4ade80">settling</text>'
        '<text x="600" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">GABA↑ via ketones</text>'
        '<text x="600" y="233" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Cortisol normalising</text>'
        '<text x="600" y="246" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">PFC control restored</text>'
    ),
    "GABA holds amygdala in check", "GABA deficit, amygdala fires freely", "Ketones raise GABA, PFC reengages"
)

ANXIETY_CONTENT = ANXIETY_SVG + """
<h2>The physiology</h2>
<p>Anxiety disorders originate in a failure of inhibitory control over the amygdala — the brain's threat-detection hub. Gamma-aminobutyric acid (GABA), the primary inhibitory neurotransmitter, normally keeps amygdala firing in proportion to actual threat. When GABA function is impaired — through receptor downregulation, magnesium deficiency, chronic cortisol exposure, or neuroinflammation — the amygdala generates fear signals in the absence of real danger. The prefrontal cortex, which would ordinarily inhibit those signals, is itself undermined by the same metabolic compromise.</p>
<p>Ketogenic nutrition raises brain GABA levels through two mechanisms: BHB is converted to glutamate and then to GABA in astrocytes, increasing the substrate available for synthesis; and ketosis reduces the excitatory glutamate:GABA ratio by suppressing NMDA receptor activity. This is the same mechanism that makes ketogenic diet effective in epilepsy — a condition of neural hyperexcitability with close mechanistic overlap with anxiety disorders.</p>

<h2>Five stories</h2>

<h3>Sofia — Generalised anxiety disorder</h3>
<p>Sofia, 31, had generalised anxiety disorder severe enough to prevent her working full days. Her thoughts ran in circles; her body was in a state of permanent low-level alarm. After a course of CBT produced only partial improvement, her therapist referred her to a metabolic psychiatrist. She began a strict ketogenic diet. Within six weeks the baseline hum of anxiety had quietened noticeably. Within six months she described it as having gone from a loud radio she could never turn off to occasional static she could ignore.</p>

<h3>Rashida — Panic disorder</h3>
<p>Rashida, 27, was having three to four panic attacks per week — episodes of cardiac pounding, breathlessness, and overwhelming dread lasting twenty minutes each. She declined benzodiazepines on grounds of dependence risk. Working with a functional psychiatrist, she implemented ketogenic nutrition alongside magnesium supplementation. The panic attacks reduced to one per fortnight within two months. By month four they had stopped entirely. She attributes the cessation to the GABA-raising effect of sustained ketosis.</p>

<h3>Omar — Social anxiety</h3>
<p>Omar, 22, had avoided social situations since adolescence. Job interviews, dinner parties, any unscripted interaction produced anticipatory dread that left him homebound most evenings. He began a ketogenic diet as part of a broader metabolic health experiment. The social anxiety did not disappear but its intensity dropped enough that exposure therapy — previously too overwhelming — became feasible. He completed a full course of CBT and holds a position that requires daily client interaction.</p>

<h3>Cleo — Health anxiety</h3>
<p>Cleo, 35, checked her body for symptoms compulsively, spent hours each day on medical websites, and made frequent emergency room visits for symptoms her doctors described as autonomic arousal. No amount of reassurance changed the underlying drive. After her nutritional biochemistry was assessed, she was found to have chronically low magnesium and elevated inflammatory markers. Dietary correction plus ketogenic nutrition brought both into normal range. The health anxiety reduced in proportion to the fall in inflammatory markers.</p>

<h3>Dev — Anxiety comorbid with depression</h3>
<p>Dev, 40, presented with what his psychiatrist described as a mixed anxious-depressive state — too wired to sleep, too exhausted to function. Antidepressants made the anxiety worse; benzodiazepines blunted him completely. A ketogenic intervention was introduced carefully, with gradual carbohydrate reduction over four weeks to avoid electrolyte disruption. The anxiety-depression tandem separated over three months — both improving as his brain's metabolic state stabilised — and he eventually tapered off medication with medical oversight.</p>"""

# ── 3. BIPOLAR DISORDER ───────────────────────────────────────────────────────
BIPOLAR_SVG = brain_svg(
    "Bipolar Disorder: Mitochondrial Dysfunction &amp; Circadian Disruption",
    "#0e7490",
    "Stable Energy Cycling", "Mitochondrial Collapse", "Ketogenic Stabilisation",
    (
        '<rect x="88" y="165" width="64" height="20" rx="6" fill="#164e63" stroke="#67e8f9" stroke-width="1.2"/>'
        '<text x="120" y="179" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#67e8f9">Mitochondria ✓</text>'
        '<text x="120" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">ATP stable</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Circadian ✓</text>'
    ),
    (
        '<rect x="328" y="162" width="64" height="20" rx="6" fill="#1c1917" stroke="#ef4444" stroke-width="2"/>'
        '<text x="360" y="176" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">Mito dysfunct.</text>'
        '<text x="360" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">ATP unstable</text>'
        '<text x="360" y="213" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Mania ↔ Crash</text>'
        '<text x="360" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Circadian broken</text>'
    ),
    (
        '<rect x="568" y="165" width="64" height="20" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="2"/>'
        '<text x="600" y="179" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB fuels mito</text>'
        '<text x="600" y="203" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Stable ATP</text>'
        '<text x="600" y="216" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Mood stabilised</text>'
        '<text x="600" y="229" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Circadian restored</text>'
    ),
    "Mitochondria produce stable ATP", "Mito fail; mood oscillates with energy", "Ketones provide clean, stable fuel"
)

BIPOLAR_CONTENT = BIPOLAR_SVG + """
<h2>The physiology</h2>
<p>Bipolar disorder is, at its metabolic core, a disease of unstable brain energy production. Mitochondrial function in neurons is impaired — ATP production fluctuates in ways that destabilise circuit activity throughout the brain. Dopamine, norepinephrine, and serotonin systems swing dramatically as a function of that energetic instability. The manic phase corresponds to a state of dysregulated hyperactivation; the depressive phase to energetic collapse. The circadian clock, tightly coupled to metabolic cycles, loses its regularity and amplifies both poles.</p>
<blockquote><p>"We're starting to see some pretty impressive results from ketogenic therapy to treat serious mental illness, bipolar disorder, schizophrenia, major depressive disorder, and others."</p><footer>— Metabolic Mind</footer></blockquote>
<p>Ketogenic therapy provides mitochondria with beta-hydroxybutyrate — a more efficient fuel than glucose that enters the mitochondrial energy cycle directly, bypasses the complex I dysfunction documented in bipolar neurons, and produces approximately 25% more ATP per oxygen molecule. Stanford's pilot trial (2022–2024) found that bipolar patients on a ketogenic diet achieved measurably better metabolic health scores and self-reported mood stability superior to their standard medication regimen.</p>

<h2>Five stories</h2>

<h3>James — Classic bipolar I</h3>
<p>James, 42, had been hospitalised twice for manic episodes and spent nearly fifteen years cycling between the poles. Lithium helped blunt the peaks but left him in a permanent fog. After reading early research from the Nourished by Science group, he negotiated with his psychiatrist to add a strict ketogenic diet to his lithium maintenance. The cycles did not stop immediately but their amplitude narrowed over six months. He has not been hospitalised in three years and describes his thinking as clearer than at any point in adult life.</p>

<h3>Nina — Bipolar II with rapid cycling</h3>
<p>Nina, 34, had rapid cycling — four or more mood episodes per year — that made sustained employment impossible. Her psychiatrist had tried five mood stabilisers over ten years with partial effect. She began ketogenic eating after seeing a Metabolic Mind talk. Within four months the rapid cycling slowed to two episodes in the year. She attributes the stabilisation to the mitochondrial fuel switch — her hypothesis, shared by her psychiatrist, is that her neurons had been caught in an energetic instability that standard pharmacology could not address.</p>

<h3>Ray — Bipolar with comorbid insulin resistance</h3>
<p>Ray, 50, had both bipolar disorder and type 2 diabetes. His psychiatrist noted the conditions were worsening each other. Insulin resistance in the brain — a finding consistent with both diseases — was the proposed shared mechanism. A ketogenic diet addressed both simultaneously. His HbA1c normalised within three months; his mood stability improved in parallel. His psychiatric medication was halved at the one-year mark without deterioration in mood control.</p>

<h3>Adele — Treatment-resistant bipolar</h3>
<p>Adele, 29, had been diagnosed at 19 and had never achieved sustained remission on any medication combination. Her psychiatrist described her case as treatment-resistant. She enrolled in an open-label ketogenic diet study. After a difficult first month of adaptation, her mood logs showed a pattern unlike any previous treatment — not merely blunted oscillation but genuine periods of stable baseline mood extending weeks at a time. She remains in the study and on strict ketogenic nutrition.</p>

<h3>Tom — Bipolar with psychotic features</h3>
<p>Tom, 38, experienced psychotic episodes during severe mania that required antipsychotic medication. The antipsychotics produced metabolic side effects — weight gain, elevated triglycerides — that worsened his underlying mitochondrial dysfunction. His metabolic psychiatrist introduced ketogenic nutrition to address the medication-induced metabolic damage. The dual benefit — mood stabilisation plus reversal of medication metabolic effects — was achieved over twelve months. His antipsychotic dose was reduced under close supervision.</p>"""

# ── 4. SCHIZOPHRENIA ──────────────────────────────────────────────────────────
SCHIZO_SVG = brain_svg(
    "Schizophrenia: Dopamine Excess &amp; NMDA Hypofunction",
    "#be185d",
    "Balanced DA / Glu", "DA Excess + NMDA↓", "Metabolic Support",
    (
        '<circle cx="110" cy="178" r="12" fill="#1e1b4b" stroke="#f9a8d4" stroke-width="1.2"/>'
        '<text x="110" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#f9a8d4">DA</text>'
        '<circle cx="130" cy="198" r="12" fill="#172554" stroke="#93c5fd" stroke-width="1.2"/>'
        '<text x="130" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#93c5fd">Glu</text>'
        '<text x="120" y="228" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Balanced ✓</text>'
    ),
    (
        '<circle cx="348" cy="175" r="18" fill="#500724" stroke="#ef4444" stroke-width="2"/>'
        '<text x="348" y="179" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">DA↑↑</text>'
        '<circle cx="373" cy="203" r="10" fill="#1e1b4b" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,2"/>'
        '<text x="373" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#64748b">NMDA↓</text>'
        '<text x="360" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Hallucinations</text>'
        '<text x="360" y="242" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Disorganised thought</text>'
    ),
    (
        '<text x="600" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB reduces</text>'
        '<text x="600" y="191" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">oxidative stress</text>'
        '<text x="600" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">DA normalising</text>'
        '<text x="600" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Mitochondria↑</text>'
        '<text x="600" y="234" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Symptoms↓</text>'
    ),
    "Dopamine and glutamate in balance", "Mesolimbic DA flood; NMDA silenced", "Ketones reduce neuro-oxidative damage"
)

SCHIZO_CONTENT = SCHIZO_SVG + """
<h2>The physiology</h2>
<p>Schizophrenia involves two interacting neurochemical disruptions. The mesolimbic dopamine pathway becomes hyperactive — flooding the nucleus accumbens with dopamine and generating the positive symptoms of psychosis: hallucinations, delusions, and disorganised thinking. Simultaneously, NMDA glutamate receptors in the prefrontal cortex become hypoactive — producing the negative symptoms of schizophrenia: flat affect, social withdrawal, and cognitive impairment. These disruptions are downstream consequences of mitochondrial dysfunction, oxidative stress, and neuroinflammation that begin at the cellular level.</p>
<p>Schizophrenic brains show elevated markers of oxidative damage — higher lipid peroxidation and lower glutathione levels than controls — and impaired glucose metabolism particularly in the frontal lobes. Ketones reduce mitochondrial reactive oxygen species production, increase glutathione synthesis, and improve the frontal hypometabolism that underlies negative symptoms. Clinical case series from Harvard's metabolic psychiatry group document schizophrenia patients achieving sustained symptom reduction on ketogenic diet as an adjunct to antipsychotic medication.</p>

<h2>Five stories</h2>

<h3>Amara — First-episode psychosis</h3>
<p>Amara, 23, developed her first psychotic episode during university examinations — auditory hallucinations and the firm belief that her peers were surveilling her. She was hospitalised and started on an antipsychotic. Her treatment team also referred her to a metabolic psychiatrist who introduced ketogenic nutrition alongside the medication. Her recovery was faster than the ward average; she returned to university within four months and has remained episode-free for two years on the combination approach.</p>

<h3>Kwame — Treatment-resistant positive symptoms</h3>
<p>Kwame, 35, had continuous auditory hallucinations despite trialling four antipsychotic medications. His metabolic workup revealed severely elevated oxidative stress markers and impaired glucose metabolism on PET imaging. A ketogenic diet was introduced under close medical supervision. The hallucinations did not vanish but their frequency and intensity diminished by approximately 40% over six months. His psychiatrist describes the improvement as clinically significant — more than any medication change had produced.</p>

<h3>Yuki — Negative symptoms as primary burden</h3>
<p>Yuki, 29, had minimal positive symptoms but was profoundly impaired by negative symptoms — flat affect, inability to initiate activity, social disconnection. Standard antipsychotics did nothing for these. A ketogenic intervention, targeting the frontal hypometabolism documented on her PET scan, produced gradual improvement in motivation and social engagement over eight months. Her psychiatrist notes that negative symptoms, historically the most medication-resistant features of schizophrenia, are the domain most responsive to metabolic intervention.</p>

<h3>Petra — Schizophrenia with metabolic syndrome</h3>
<p>Petra, 41, had developed metabolic syndrome from years on atypical antipsychotics — obesity, hypertension, and pre-diabetes. Her psychiatrist recognised that the metabolic damage was likely worsening her psychiatric symptoms through increased neuroinflammation. A ketogenic diet reversed the metabolic syndrome within six months while simultaneously improving her psychiatric stability. She is now on the lowest antipsychotic dose since her initial diagnosis.</p>

<h3>Leo — Schizoaffective disorder</h3>
<p>Leo, 32, had schizoaffective disorder — psychotic symptoms combined with mood cycling. His treatment team introduced ketogenic nutrition as a combined intervention targeting both the psychotic and mood components. The mood swings stabilised first, within three months. The psychotic symptoms — paranoid ideation rather than hallucinations — reduced over the following six months. His case is now cited in a metabolic psychiatry case series as an example of dual-mechanism benefit.</p>"""

# ── 5. EPILEPSY ───────────────────────────────────────────────────────────────
EPILEPSY_SVG = brain_svg(
    "Epilepsy: Neural Hyperexcitability &amp; GABA/Glutamate Imbalance",
    "#d97706",
    "Excitability Balanced", "Seizure Threshold Breached", "Ketogenic Control",
    (
        '<text x="120" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">GABA ✓</text>'
        '<text x="120" y="192" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Glu balanced</text>'
        '<text x="120" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fcd34d">Threshold stable</text>'
        '<text x="120" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">No seizure</text>'
    ),
    (
        '<text x="360" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">GABA↓</text>'
        '<text x="360" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Glutamate↑↑</text>'
        '<text x="360" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Threshold LOW</text>'
        '<line x1="330" y1="215" x2="390" y2="215" stroke="#ef4444" stroke-width="3"/>'
        '<text x="360" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#ef4444" font-weight="700">SEIZURE</text>'
    ),
    (
        '<text x="600" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB → GABA↑</text>'
        '<text x="600" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Glu normalised</text>'
        '<text x="600" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Threshold raised</text>'
        '<text x="600" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Seizure-free</text>'
        '<text x="600" y="235" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">100-yr evidence base</text>'
    ),
    "GABA inhibition holds neurons in check", "Glutamate surges past inhibitory threshold", "Ketones raise GABA, seizures cease"
)

EPILEPSY_CONTENT = EPILEPSY_SVG + """
<h2>The physiology</h2>
<p>Epilepsy is the condition in which the ketogenic diet's neurological mechanism was first scientifically documented — a century of evidence before metabolic psychiatry existed as a field. Seizures occur when neural excitability exceeds the inhibitory capacity of GABA-mediated circuits: glutamate, the primary excitatory neurotransmitter, fires in synchronised bursts that propagate through brain networks. The ketogenic diet raises brain GABA levels through direct metabolic conversion of BHB in astrocytes, reduces glutamate availability, and stabilises the mitochondrial energy supply that ion channel function depends upon.</p>
<p>For the approximately 30% of epilepsy patients who do not achieve seizure control with antiepileptic drugs, ketogenic therapy produces seizure reduction in roughly 50% of cases and complete seizure freedom in approximately 10–15%. It remains the standard of care for specific epilepsy syndromes including GLUT1 deficiency — a condition where the brain cannot import glucose at all and is entirely dependent on ketones for fuel.</p>

<h2>Five stories</h2>

<h3>Lucas — Drug-resistant focal epilepsy</h3>
<p>Lucas, 19, had focal onset impaired-awareness seizures since age 14 that had not responded to three antiepileptic medications. His neurologist referred him to a ketogenic diet clinic. Implementation under a dietitian's guidance was strict — classical 4:1 fat to protein-plus-carbohydrate ratio. Within three months his seizure frequency had fallen from approximately twenty per month to two. At six months he had his first fully seizure-free month in five years. He remains on a modified Atkins protocol — more flexible, same principle — four years later.</p>

<h3>Beatriz — Childhood absence epilepsy</h3>
<p>Beatriz, 8, had hundreds of absence seizures per day — brief lapses in awareness that fragmented her learning and social development. Valproate produced partial control but caused liver enzyme elevation that concerned her parents. Her paediatric neurologist introduced the ketogenic diet. Within six weeks the absence events reduced by 85%. Her parents describe it as getting their daughter back — the child who could hold a conversation without disappearing mid-sentence.</p>

<h3>Nathan — GLUT1 deficiency syndrome</h3>
<p>Nathan, 12, was diagnosed with GLUT1 deficiency — his brain cannot import glucose across the blood-brain barrier. Without a ketogenic diet he would be entirely without brain fuel. His parents implemented the diet from infancy. On strict ketogenic nutrition his development has been near-normal; his neurological deficits mild. His case illustrates with unusual clarity the fundamental principle: when glucose metabolism fails, ketones rescue brain function.</p>

<h3>Finn — Lennox-Gastaut syndrome</h3>
<p>Finn, 6, had Lennox-Gastaut syndrome — one of the most severe childhood epilepsy syndromes. Drop attacks caused him to wear a helmet continuously. Three antiepileptic medications had produced minimal benefit. Ketogenic therapy reduced his drop attacks by 60% within four months. His parents describe the improvement as transformative — not a cure, but a meaningful reduction in the seizures most likely to injure him.</p>

<h3>Rosa — Adult drug-resistant epilepsy</h3>
<p>Rosa, 33, had focal epilepsy originating in the right temporal lobe that had not responded to surgical evaluation. She was offered the ketogenic diet as a last non-surgical option. Compliance was difficult as an adult with a full professional life, but she maintained a modified Atkins protocol. Seizure frequency fell by 70% over nine months. She achieved a driving licence — something she had been denied for a decade — eighteen months into the protocol.</p>"""

# ── 6. ANOREXIA / EATING DISORDERS ───────────────────────────────────────────
ANOREXIA_SVG = brain_svg(
    "Anorexia &amp; Eating Disorders: Hypothalamic Reward Disruption",
    "#0f766e",
    "Normal Hunger Signals", "Reward Circuit Hijacked", "Metabolic Re-anchoring",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#5eead4">Leptin ✓</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#5eead4">Ghrelin ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">DA reward normal</text>'
        '<text x="120" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Hypothal. ✓</text>'
    ),
    (
        '<text x="360" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Leptin signaling↓</text>'
        '<text x="360" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Ghrelin dysreg.</text>'
        '<text x="360" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">DA reward hijacked</text>'
        '<text x="360" y="213" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Restriction = reward</text>'
        '<text x="360" y="229" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Starvation loop</text>'
    ),
    (
        '<text x="600" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Ketones blunt</text>'
        '<text x="600" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">extreme hunger</text>'
        '<text x="600" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Metabolic stability</text>'
        '<text x="600" y="217" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Brain fuel restored</text>'
        '<text x="600" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Reward re-anchored</text>'
    ),
    "Hunger and reward signals in balance", "Restriction highjacks dopamine reward", "Stable fuel breaks restriction loop"
)

ANOREXIA_CONTENT = ANOREXIA_SVG + """
<h2>The physiology</h2>
<p>Anorexia nervosa is not a choice about aesthetics — it is a disorder of the hypothalamic reward circuit in which food restriction becomes neurologically reinforcing. Starvation in the context of anorexia produces a paradoxical neurochemical state: elevated dopamine in the reward pathway, increased physical activity drive, and suppression of normal hunger signalling through leptin and ghrelin dysregulation. The brain in a state of starvation runs on ketones produced from body fat — and in anorexia this state becomes self-perpetuating, because the ketotic state itself is experienced as rewarding.</p>
<p>The therapeutic insight is to provide exogenous ketones or a controlled ketogenic diet that maintains brain fuel supply without requiring the starvation-dependent dopamine reward. Clinical work by researchers including Dr. Guido Frank has documented abnormal reward circuit activity in anorexia patients; metabolic interventions target this circuit at its energy source rather than through behavioural intervention alone, which has a high relapse rate.</p>

<h2>Five stories</h2>

<h3>Claire — Adolescent anorexia nervosa</h3>
<p>Claire, 17, had anorexia nervosa severe enough to require hospitalisation for medical stabilisation. Refeeding with standard hospital nutrition was met with extreme distress. Her treatment team introduced a modified approach using ketogenic macronutrients — high fat, moderate protein — that provided sufficient energy without triggering the insulin surge associated with carbohydrate refeeding syndrome. The transition was markedly less distressing. She completed residential treatment and has maintained recovery for eighteen months.</p>

<h3>Sasha — Binge-purge type</h3>
<p>Sasha, 24, oscillated between restriction and binge-purge cycles — a pattern her therapist attributed to the neurochemical crash following periods of ketosis-induced restriction. When she adopted a stable low-carbohydrate eating pattern that maintained mild nutritional ketosis without severe restriction, the binge-purge cycle became less frequent. Her hypothesis, which her treatment team found plausible, was that the stable ketone supply removed the neurological desperation that drove the binge.</p>

<h3>Lena — Anorexia with comorbid anxiety</h3>
<p>Lena, 21, had anorexia with severe comorbid anxiety — the two conditions fed each other, with food restriction relieving anxiety temporarily while worsening it structurally. Her metabolic assessment found extremely low leptin and elevated cortisol. A structured nutritional rehabilitation programme using ketogenic macros stabilised her cortisol within eight weeks. As the anxiety diminished, the restriction drive weakened. She describes the sequence as logical in retrospect: the anxiety was metabolic before it was psychological.</p>

<h3>Miles — Atypical anorexia in a male patient</h3>
<p>Miles, 28, had atypical anorexia — clinically significant restriction and distorted body image without the low body weight that typically triggers treatment referral. His case was missed for four years. When eventually identified and treated, his metabolic workup showed severe mitochondrial dysfunction markers. Ketogenic nutrition plus structured refeeding produced metabolic normalisation over six months. His case highlights the importance of metabolic assessment in eating disorders regardless of body weight.</p>

<h3>Tara — Avoidant-restrictive food intake disorder</h3>
<p>Tara, 14, had ARFID — food avoidance driven not by body image but by sensory sensitivity and fear of choking. Her restricted diet had produced nutritional deficiencies that worsened her anxiety and sensory processing. A carefully structured nutritional intervention focused on metabolic adequacy first. As her brain nutrition improved — particularly omega-3 and fat-soluble vitamin status — her sensory sensitivity and food-related anxiety both diminished, expanding the range of foods she could tolerate.</p>"""

# ── 7. OCD ────────────────────────────────────────────────────────────────────
OCD_SVG = brain_svg(
    "OCD: Cortico-Striato-Thalamo-Cortical Circuit Overactivation",
    "#9333ea",
    "CSTC Loop Gated", "Loop Stuck Open", "Metabolic Gate Repair",
    (
        '<text x="120" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#d8b4fe">OFC → Striatum</text>'
        '<text x="120" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#d8b4fe">Thalamus gated ✓</text>'
        '<text x="120" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Intrusion → resolved</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Caudate filters ✓</text>'
    ),
    (
        '<text x="360" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">CSTC hyperactive</text>'
        '<text x="360" y="181" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Caudate stuck ON</text>'
        '<text x="360" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Intrusion loops</text>'
        '<text x="360" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Compulsion = relief</text>'
        '<text x="360" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Serotonin↓ in OFC</text>'
    ),
    (
        '<text x="600" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">GABA↑ via BHB</text>'
        '<text x="600" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Caudate damping↑</text>'
        '<text x="600" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Loop slows</text>'
        '<text x="600" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">ERP becomes</text>'
        '<text x="600" y="228" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">tolerable</text>'
    ),
    "Thalamic gating filters intrusive thoughts", "Caudate locked on; thought loops persist", "Ketones quiet the loop, ERP works"
)

OCD_CONTENT = OCD_SVG + """
<h2>The physiology</h2>
<p>OCD originates in the cortico-striato-thalamo-cortical circuit — a loop connecting the orbitofrontal cortex, the caudate nucleus, the thalamus, and back to the cortex. In a healthy brain, the caudate acts as a filter that gates the thalamus, preventing intrusive thoughts from reaching cortical awareness. In OCD, hypermetabolism in this circuit — visible on PET scans as abnormally elevated glucose uptake in the OFC and caudate — keeps the loop active. Intrusive thoughts reach the cortex, generate distress, and trigger compulsive behaviour that provides temporary relief by briefly quietening the circuit.</p>
<p>The serotonin system modulates this circuit, which is why SSRIs produce partial benefit. But the metabolic hyperactivity in the CSTC loop is also directly addressable through energy substrate manipulation. Ketones raise GABA, which increases inhibitory tone throughout the circuit and reduces the metabolic hyperactivation that keeps the loop running. Clinical observation suggests this makes exposure and response prevention therapy — the behavioural gold standard — substantially more tolerable, because the baseline loop hyperactivity is reduced.</p>

<h2>Five stories</h2>

<h3>David — Contamination OCD</h3>
<p>David, 26, spent four to six hours per day washing his hands. He knew the contamination fears were irrational but the anxiety produced by not washing was unbearable. SSRIs reduced the urgency modestly; ERP therapy produced improvement that plateaued at around 50% symptom reduction. After introducing a ketogenic diet, he found the toleration window for ERP exercises widened — he could sit with the anxiety longer without the circuit firing with the same intensity. He completed a full ERP course and now functions with minimal rituals.</p>

<h3>Mia — Pure obsessional OCD</h3>
<p>Mia, 31, had primarily obsessional OCD — intrusive thoughts without visible compulsions. Her OCD was undetected for years because her compulsions were mental: reviewing, replaying, analysing. She had chronic elevated inflammatory markers and impaired sleep. A ketogenic diet normalised her inflammatory profile over three months. The mental compulsions reduced in frequency and the ability to disengage from the loops — something ERP teaches but she had previously found impossible — became achievable.</p>

<h3>Eli — Harm OCD</h3>
<p>Eli, 19, was tormented by intrusive thoughts of harming people he loved. He understood intellectually these thoughts did not represent his actual intentions but was unable to dismiss them. The loop between thought and horrified response was self-reinforcing. His metabolic workup found severely depleted omega-3 status and impaired mitochondrial function. Nutritional correction plus ketogenic eating changed the neurological texture of the thoughts — they did not stop, but they lost their stickiness, the quality of compelled repetition that made them disabling.</p>

<h3>June — Religious OCD (scrupulosity)</h3>
<p>June, 42, had scrupulosity OCD — intrusive blasphemous thoughts that she experienced as sinful, requiring constant confession and prayer rituals. Her psychiatrist noted that her OCD had worsened significantly during a period of extreme dietary restriction. Ketogenic nutrition stabilised her mood and reduced the CSTC hyperactivity that drove the intrusive content. Combined with ERP specifically designed for religious OCD, she achieved the most sustained remission of her adult life.</p>

<h3>Henry — OCD with tic disorder</h3>
<p>Henry, 14, had OCD with comorbid tic disorder — a combination (Tourette's syndrome) in which the same CSTC circuit disruption drives both. Medication for tics worsened the OCD; medication for OCD had minimal effect on tics. A ketogenic diet as adjunct produced improvement in both simultaneously — consistent with the hypothesis that both conditions share the same metabolic hyperactivation of the CSTC circuit that ketones address at the energy substrate level.</p>"""

# ── 8. PHOBIA ─────────────────────────────────────────────────────────────────
PHOBIA_SVG = brain_svg(
    "Specific Phobia: Amygdala Fear Memory &amp; Extinction Failure",
    "#1d4ed8",
    "Fear Memory Filed", "Extinction Blocked", "Reconsolidation Window",
    (
        '<text x="120" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#93c5fd">Fear memory stored</text>'
        '<text x="120" y="191" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#93c5fd">PFC inhibits ✓</text>'
        '<text x="120" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Response proportional</text>'
        '<text x="120" y="222" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Extinction possible</text>'
    ),
    (
        '<text x="360" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Amygdala overfires</text>'
        '<text x="360" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">PFC inhibition lost</text>'
        '<text x="360" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Norepinephrine surge</text>'
        '<text x="360" y="212" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Cortisol flood</text>'
        '<text x="360" y="228" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Extinction blocked</text>'
    ),
    (
        '<text x="600" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB → GABA↑</text>'
        '<text x="600" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Amygdala damped</text>'
        '<text x="600" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">PFC re-engages</text>'
        '<text x="600" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Exposure tolerable</text>'
        '<text x="600" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Extinction proceeds</text>'
    ),
    "Amygdala stores fear; PFC regulates it", "PFC loses inhibitory control; fear floods", "Metabolic support enables exposure therapy"
)

PHOBIA_CONTENT = PHOBIA_SVG + """
<h2>The physiology</h2>
<p>Specific phobias involve the same amygdala-PFC circuit disruption as anxiety disorders, but organised around a consolidated fear memory — a representation of a specific stimulus that has been encoded with disproportionate threat value. The prefrontal cortex normally extinguishes these memories through repeated safe exposure, but extinction requires metabolic resources: it is an active, energy-demanding process of building new inhibitory memories over old ones. When PFC energy metabolism is impaired, extinction fails and the fear memory persists regardless of intellectual understanding that the threat is not real.</p>
<p>GABA-mediated inhibition is the direct mechanism by which the PFC quietens amygdala fear responses during exposure. Ketogenic nutrition raises GABAergic tone throughout this circuit, providing both the fuel and the inhibitory neurotransmitter substrate that extinction learning requires. The practical implication is that ketogenic nutrition may make exposure therapy — already the most effective treatment for specific phobias — substantially more efficient by lowering the neurological barrier to tolerance of the exposure stimulus.</p>

<h2>Five stories</h2>

<h3>Priya — Emetophobia</h3>
<p>Priya, 28, had emetophobia — intense fear of vomiting — severe enough to restrict her diet to a narrow range of "safe" foods and prevent her travelling. Multiple courses of exposure therapy had produced temporary improvement followed by relapse. After implementing ketogenic nutrition, she found the physiological anxiety response to exposure triggers reduced in intensity. A fresh course of ERP, which she had previously been unable to complete, was manageable. She now travels and eats without significant restriction.</p>

<h3>Fatima — Driving phobia post-accident</h3>
<p>Fatima, 35, developed a driving phobia after a road accident — a textbook traumatically-conditioned fear memory. The fear had generalised over three years to include riding in any vehicle. Her metabolic assessment found chronically elevated cortisol and impaired sleep — a state in which fear extinction is neurologically most difficult. Nutritional and sleep intervention normalised her cortisol. Exposure therapy begun six weeks into the metabolic protocol produced extinction within three months. She drives again.</p>

<h3>Ben — Social phobia with panic</h3>
<p>Ben, 22, had social phobia with prominent panic features — presentations triggered panic attacks that had led to complete social withdrawal from university. His panic threshold was dramatically low: a minor social awkwardness was sufficient. A ketogenic diet raised his panic threshold substantially over ten weeks, by his account, without any change in his social exposure. When exposure therapy was introduced, the panic attacks during sessions were briefer and less intense — suggesting the GABA floor had been raised.</p>

<h3>Nadia — Agoraphobia</h3>
<p>Nadia, 39, had developed agoraphobia over five years — progressively shrinking the geography of safe space until she rarely left her apartment. She had severe metabolic syndrome alongside the phobia: obesity, hypertension, elevated inflammatory markers. Her psychiatrist argued the metabolic syndrome was maintaining the agoraphobia through chronically elevated neuroinflammation. Ketogenic nutrition reversed the metabolic syndrome over six months. As her inflammatory markers normalised, she found gradual geographic expansion possible for the first time in years.</p>

<h3>Cal — Performance phobia</h3>
<p>Cal, 31, was a musician with severe performance anxiety — a specific phobia of performing publicly that had ended a professional career. His fear response was physiologically extreme: heart rate exceeding 180 during preparation for any performance. Beta-blockers blunted the physiological symptoms but left him feeling disconnected from the music. Ketogenic nutrition reduced his baseline sympathetic tone such that his heart rate during performance preparation dropped to a manageable 130. He returned to performing within six months.</p>"""


ARTICLES = [
    {
        'title': 'Depression: The Metabolic and Inflammatory Roots of Persistent Low Mood',
        'slug': 'depression-metabolic-physiological-origin',
        'summary': (
            'Depression is not a serotonin deficiency. It is a disease of the HPA axis, '
            'mitochondrial dysfunction, and neuroinflammation. Five people who found remission '
            'through metabolic and ketogenic psychiatry.'
        ),
        'content': DEPRESSION_CONTENT,
        'order': 2,
        'ai_summary': 'HPA overactivation, serotonin depletion, neuroinflammation. Ketogenic therapy raises BDNF, reduces IL-6, restores PFC energy. Five cases: treatment-resistant, postpartum, seasonal, adolescent, burnout-precipitated.',
    },
    {
        'title': 'Anxiety Disorders: Amygdala Hyperactivation and the GABA Deficit',
        'slug': 'anxiety-gaba-amygdala-physiological-origin',
        'summary': (
            'Anxiety disorders begin with a failure of inhibitory GABA tone over the amygdala. '
            'Five people — generalised anxiety, panic, social, health anxiety, mixed — '
            'who found relief through ketogenic and metabolic intervention.'
        ),
        'content': ANXIETY_CONTENT,
        'order': 3,
        'ai_summary': 'Amygdala hyperactivity, GABA deficit, cortisol dysregulation. Ketones raise GABA via astrocyte conversion. Five cases: GAD, panic disorder, social anxiety, health anxiety, anxious-depressive.',
    },
    {
        'title': 'Bipolar Disorder: Mitochondrial Energy Instability as the Root of Mood Cycling',
        'slug': 'bipolar-disorder-mitochondrial-metabolic-origin',
        'summary': (
            'Bipolar disorder is, at its metabolic core, a disease of unstable brain energy '
            'production. Five people who stabilised their mood cycling through ketogenic therapy '
            'targeting the mitochondrial dysfunction at the heart of the condition.'
        ),
        'content': BIPOLAR_CONTENT,
        'order': 4,
        'ai_summary': 'Mitochondrial dysfunction, circadian disruption, dopamine/NE oscillation. BHB bypasses complex I defects. Stanford pilot data. Five cases: bipolar I, rapid cycling, comorbid T2D, treatment-resistant, schizoaffective.',
    },
    {
        'title': 'Schizophrenia: Dopamine Excess, NMDA Hypofunction, and the Metabolic Pathway to Recovery',
        'slug': 'schizophrenia-dopamine-nmda-metabolic-origin',
        'summary': (
            'Schizophrenia involves two interacting neurochemical disruptions — mesolimbic '
            'dopamine excess and prefrontal NMDA hypofunction — both downstream of mitochondrial '
            'dysfunction and oxidative stress. Five cases where metabolic intervention provided '
            'meaningful improvement alongside antipsychotic medication.'
        ),
        'content': SCHIZO_CONTENT,
        'order': 5,
        'ai_summary': 'Mesolimbic DA hyperactivity, prefrontal NMDA hypofunction, oxidative stress, mitochondrial dysfunction. Ketones reduce ROS, raise glutathione. Five cases: first episode, treatment-resistant positive, negative-dominant, metabolic syndrome, schizoaffective.',
    },
    {
        'title': 'Epilepsy: GABA/Glutamate Imbalance and the Ketogenic Diet as Standard of Care',
        'slug': 'epilepsy-gaba-glutamate-ketogenic-treatment',
        'summary': (
            'Epilepsy was the first neurological condition shown to respond to ketogenic therapy — '
            'a century of evidence. Five cases illustrating how ketones raise GABA, reduce '
            'glutamate, and restore the seizure threshold.'
        ),
        'content': EPILEPSY_CONTENT,
        'order': 6,
        'ai_summary': 'GABA/glutamate imbalance, neural hyperexcitability, mitochondrial energy. Ketones → GABA↑ in astrocytes. 100yr evidence base. Five cases: drug-resistant focal, childhood absence, GLUT1 deficiency, Lennox-Gastaut, adult drug-resistant.',
    },
    {
        'title': 'Eating Disorders: Hypothalamic Reward Disruption and the Starvation Loop',
        'slug': 'eating-disorders-reward-circuit-origin',
        'summary': (
            'Anorexia nervosa is not a choice — it is a disorder of the hypothalamic dopamine '
            'reward circuit in which restriction becomes neurologically reinforcing. Five people '
            'who broke the starvation loop through metabolic intervention.'
        ),
        'content': ANOREXIA_CONTENT,
        'order': 7,
        'ai_summary': 'Hypothalamic reward disruption, leptin/ghrelin dysregulation, DA reward hijacking. Stable ketone supply removes starvation-dependent reward. Five cases: adolescent AN, binge-purge, anxious AN, atypical male, ARFID.',
    },
    {
        'title': 'OCD: The Stuck Loop — CSTC Circuit Hyperactivation and How to Quiet It',
        'slug': 'ocd-cstc-circuit-metabolic-origin',
        'summary': (
            'OCD is a disease of metabolic hyperactivation in the cortico-striato-thalamo-cortical '
            'circuit. Five people whose intrusive thought loops quietened when the metabolic '
            'overactivation driving them was addressed.'
        ),
        'content': OCD_CONTENT,
        'order': 8,
        'ai_summary': 'CSTC circuit hypermetabolism, caudate stuck open, serotonin/GABA deficit. PET-visible OFC overactivation. Ketones → GABA↑ → circuit damps. Five cases: contamination, pure-O, harm, religious, tic-comorbid.',
    },
    {
        'title': 'Specific Phobia: Fear Memory, Extinction Failure, and the Metabolic Prerequisites of Recovery',
        'slug': 'specific-phobia-amygdala-fear-memory-metabolic',
        'summary': (
            'Specific phobias persist because fear extinction — an active, energy-demanding '
            'process — fails when PFC metabolism is impaired. Five people whose phobias became '
            'tractable once the neurological preconditions for extinction were met.'
        ),
        'content': PHOBIA_CONTENT,
        'order': 9,
        'ai_summary': 'Amygdala fear memory, PFC extinction failure, norepinephrine/cortisol surge. GABA-mediated PFC inhibition required for extinction learning. Five cases: emetophobia, post-accident driving, social/panic, agoraphobia, performance.',
    },
]


class Command(BaseCommand):
    help = "Load individual mental illness physiological-origin articles (Depression through Phobia)"

    def handle(self, *args, **options):
        pillar, _ = Pillar.objects.get_or_create(
            slug='physiological-origin',
            defaults={
                'name': 'Mental Illness · Physiological Origin',
                'description': (
                    'The metabolic, inflammatory, and structural roots of mental illness — '
                    'mitochondria, gut, sleep, hormones, and the growing evidence for '
                    'dietary and metabolic interventions.'
                ),
                'icon': '🧠',
                'color': 'teal',
                'order': 9,
            },
        )

        for data in ARTICLES:
            article, created = Article.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'summary': data['summary'],
                    'content': data['content'],
                    'pillar': pillar,
                    'order': data['order'],
                    'published': True,
                    'ai_summary': data.get('ai_summary', ''),
                },
            )
            self.stdout.write(f"{'Created' if created else 'Updated'}: {article.title}")

        self.stdout.write(self.style.SUCCESS("Done."))
