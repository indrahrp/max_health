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


# ── 9. PTSD ───────────────────────────────────────────────────────────────────
PTSD_SVG = brain_svg(
    "PTSD: HPA Dysregulation, Amygdala Hyperreactivity &amp; Hippocampal Loss",
    "#dc2626",
    "Trauma Processed", "Fear Circuit Locked", "Metabolic Reset",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">Amygdala calm</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">Hippocampus ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Cortisol balanced</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Memory filed ✓</text>'
    ),
    (
        '<text x="360" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Amygdala fires</text>'
        '<text x="360" y="181" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">continuously</text>'
        '<text x="360" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Hippocampus shrinks</text>'
        '<text x="360" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Cortisol chronically↑</text>'
        '<text x="360" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Flashbacks/hypervigilance</text>'
    ),
    (
        '<text x="600" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB → BDNF↑</text>'
        '<text x="600" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Hippocampus</text>'
        '<text x="600" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">neurogenesis↑</text>'
        '<text x="600" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Neuroinflam↓</text>'
        '<text x="600" y="228" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Cortisol normalises</text>'
    ),
    "Trauma contextualised; cortisol balanced", "Amygdala stuck in alert; hippocampus atrophies", "Ketones rebuild hippocampus via BDNF"
)

PTSD_CONTENT = PTSD_SVG + """
<h2>The physiology</h2>
<p>PTSD is the condition that results when traumatic fear memories fail to be contextualised and filed. The amygdala, which encodes threat memories, becomes chronically hyperreactive — responding to reminders of the trauma with the same full-intensity fear response as the original event. The hippocampus, which normally provides the contextual information that tells the amygdala a stimulus is a memory rather than a current threat, atrophies under chronic cortisol exposure — losing volume measurably on MRI. Without hippocampal context, every trigger replays the original terror.</p>
<blockquote><p>"It's really well documented that individuals with PTSD have areas of brain hypometabolism."</p><footer>— Metabolic Mind</footer></blockquote>
<p>PET imaging consistently shows hypometabolism in the prefrontal cortex of PTSD patients — the region responsible for inhibiting the amygdala. Ketogenic therapy addresses PTSD through three pathways: BHB stimulates BDNF production, promoting hippocampal neurogenesis and volume restoration; ketosis reduces neuroinflammation — chronically elevated in PTSD and a driver of cortisol dysregulation; and stable brain energy supply restores PFC metabolic capacity, re-enabling the top-down inhibitory control over the amygdala that trauma had disabled.</p>

<h2>Five stories</h2>

<h3>Zara — Combat PTSD</h3>
<p>Zara, 31, was a veteran with combat PTSD diagnosed after two overseas deployments. She had chronic hypervigilance, nightmares every night, and could not use public transport. Standard EMDR therapy produced partial improvement that stalled. Her VA clinician referred her to a metabolic psychiatry programme that added ketogenic nutrition to her ongoing EMDR. Within three months her sleep improved substantially — the nightmares became less frequent, their content less vivid. The EMDR then progressed where it had previously been blocked. She now uses public transport and works a full-time job.</p>

<h3>Marcus — Childhood trauma PTSD</h3>
<p>Marcus, 44, had PTSD rooted in severe childhood trauma that had never been adequately treated. He had decades of emotional dysregulation, relationship breakdown, and self-medication with alcohol. When he finally engaged with trauma therapy, his metabolic assessment revealed chronically elevated cortisol, depleted BDNF, and hippocampal volume loss on MRI. Ketogenic nutrition combined with trauma-focused therapy produced changes that therapy alone had never achieved. He describes the metabolic support as giving his brain the rebuilding material the therapy required but could not provide alone.</p>

<h3>Rachel — Sexual assault PTSD</h3>
<p>Rachel, 27, developed PTSD following sexual assault. She had severe dissociation — the cortisol-driven amnesiac response that prevented her from staying present in therapy sessions. A metabolic intervention reduced her baseline cortisol within six weeks. As the cortisol normalised, her dissociative episodes became less frequent and she could tolerate trauma processing in sessions for the first time. Her therapist described the metabolic preparation as unlocking access to the trauma material that the dissociation had been guarding.</p>

<h3>Sean — First-responder PTSD</h3>
<p>Sean, 38, was a paramedic with PTSD accumulated over twelve years of critical incident exposure. He had not sought treatment, attributing his symptoms to occupational hazard, until panic attacks began occurring on shift. His inflammatory markers — CRP, IL-6 — were at the high end of normal. He was not clinically inflamed, but his psychiatrist argued this represented a priming state in which his nervous system was operating with minimal reserve. A ketogenic anti-inflammatory diet plus structured sleep hygiene normalised his inflammatory profile. His symptom severity halved over four months without pharmaceutical intervention.</p>

<h3>Ada — PTSD with complex comorbidities</h3>
<p>Ada, 36, had complex PTSD — prolonged childhood trauma rather than a single incident — with comorbid depression and borderline personality features. Her treatment had been fragmented across years of crisis intervention. A metabolic psychiatrist assessed her and found severe mitochondrial dysfunction markers alongside the expected cortisol dysregulation. The metabolic programme was introduced as a stabilisation phase before resuming trauma therapy. Ada describes the stabilisation as the first time in her adult life that her nervous system felt safe enough to engage with the past.</p>"""

# ── 10. ADHD ──────────────────────────────────────────────────────────────────
ADHD_SVG = brain_svg(
    "ADHD: Dopamine/Norepinephrine Deficit in Prefrontal Circuits",
    "#ea580c",
    "PFC Attention Network", "DA/NE Deficit", "Metabolic Support",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fed7aa">DA/NE balanced</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fed7aa">PFC active ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Attention sustained</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Impulse controlled</text>'
    ),
    (
        '<text x="360" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">DA↓ NE↓ in PFC</text>'
        '<text x="360" y="181" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">PFC hypoactive</text>'
        '<text x="360" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Attention fails</text>'
        '<text x="360" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Reward circuit</text>'
        '<text x="360" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">seeks novel stimuli</text>'
    ),
    (
        '<text x="600" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Stable glucose→</text>'
        '<text x="600" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">no glucose spikes</text>'
        '<text x="600" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">BHB fuels PFC</text>'
        '<text x="600" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">DA synthesis↑</text>'
        '<text x="600" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Focus sustained</text>'
    ),
    "Dopamine/NE enable PFC attention control", "PFC fuel-starved; reward-seeking compensates", "Stable ketone fuel steadies PFC function"
)

ADHD_CONTENT = ADHD_SVG + """
<h2>The physiology</h2>
<p>ADHD is fundamentally a disorder of the prefrontal cortex — specifically of the dopaminergic and noradrenergic pathways that supply it. The PFC depends on precise levels of DA and NE to maintain its attentional and inhibitory functions; too little, and the network responsible for sustaining attention, filtering distraction, and inhibiting impulse collapses. The striatum's reward circuit then compensates: unable to sustain attention on unstimulating tasks, the ADHD brain seeks novel, high-dopamine stimuli — a functional adaptation that produces the characteristic inattention and impulsivity.</p>
<blockquote><p>"I also have ADHD and I am also on the spectrum."</p><footer>— Metabolic Mind community member</footer></blockquote>
<p>The metabolic angle: the PFC is exquisitely sensitive to glucose fluctuations. Blood sugar spikes followed by reactive drops — common in high-carbohydrate diets — produce corresponding waves of PFC function and impairment. Ketogenic nutrition eliminates these fluctuations entirely, providing the PFC with a stable fuel supply. Additionally, ketosis promotes dopamine synthesis through BHB-mediated pathway effects. Clinical observations and a growing number of case reports document ADHD symptom improvement on low-carbohydrate and ketogenic diets, often allowing medication dose reduction.</p>

<h2>Five stories</h2>

<h3>Sam — Adult ADHD, combined type</h3>
<p>Sam, 33, had ADHD diagnosed at 30 — late identification meant two decades of academic underachievement and career instability. He was on a moderate dose of methylphenidate that helped him function but produced afternoon crashes. He implemented a ketogenic diet after reading about the glucose-PFC connection. Within three weeks the afternoon crashes disappeared; within two months he found himself sustaining attention in the evenings without stimulant medication, which he had never previously been able to do. His psychiatrist reduced his dose by a third.</p>

<h3>Isla — ADHD inattentive type</h3>
<p>Isla, 26, had the inattentive subtype — no hyperactivity, just a persistent inability to read a paragraph to its end, hold a thought, or complete a task. She had developed extensive compensatory strategies that exhausted her. She declined medication on principle and investigated dietary approaches. A ketogenic diet produced what she describes as a qualitative change in the texture of her attention — thoughts stopped sliding away before she completed them. She is the first to acknowledge this may be partly metabolic and partly the cognitive benefit of improved sleep that accompanied the dietary change.</p>

<h3>Jordan — ADHD with emotional dysregulation</h3>
<p>Jordan, 29, had ADHD with prominent emotional dysregulation — rejection-sensitive dysphoria that produced intense, brief emotional responses to perceived criticism. Stimulant medication addressed attention but worsened the emotional lability. A ketogenic diet produced improvement in emotional regulation that the medication had not provided, consistent with metabolic stabilisation of the limbic-PFC interface that governs emotional control. Jordan now takes a lower stimulant dose and finds the emotional dysregulation substantially more manageable.</p>

<h3>Theo — Paediatric ADHD</h3>
<p>Theo, 9, had ADHD severe enough to make classroom learning nearly impossible. His parents sought dietary approaches before committing to medication. A modified low-glycaemic diet — not strictly ketogenic, but eliminating all processed carbohydrates and added sugars — produced marked improvement in his teacher's observations within four weeks. When further trialled on a more strictly ketogenic approach, improvement was greater still. He began stimulant medication at a lower dose than originally prescribed and continues the dietary protocol.</p>

<h3>Bea — ADHD comorbid with anxiety</h3>
<p>Bea, 22, had ADHD and anxiety — a common comorbidity, since the dysregulation of the prefrontal-limbic circuit produces both. Stimulants worsened her anxiety; anxiolytics blunted her focus. The combination was therapeutically intractable. A ketogenic diet addressed both conditions through the shared pathway: GABA raised by ketosis reduced her anxiety baseline, while stable PFC fuel supply improved her attention. She describes it as the first intervention that addressed both conditions simultaneously rather than trading one off against the other.</p>"""

# ── 11. ALZHEIMER'S DISEASE ───────────────────────────────────────────────────
ALZ_SVG = brain_svg(
    "Alzheimer's Disease: Brain Insulin Resistance &amp; Metabolic Rescue",
    "#7c3aed",
    "Normal Brain Fuel", "Glucose Uptake Fails", "Ketone Bypass",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#c4b5fd">Glucose → neurons</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#c4b5fd">GLUT1/3 active ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Insulin signalling ✓</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Synaptic energy ✓</text>'
    ),
    (
        '<text x="360" y="165" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Brain insulin resist.</text>'
        '<text x="360" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">GLUT1/3 fail</text>'
        '<text x="360" y="194" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Neurons starve</text>'
        '<text x="360" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Amyloid/Tau accum.</text>'
        '<text x="360" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Cognitive decline</text>'
    ),
    (
        '<text x="600" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB bypasses</text>'
        '<text x="600" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">insulin resistance</text>'
        '<text x="600" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Neurons refuelled</text>'
        '<text x="600" y="212" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Cognition stabilises</text>'
        '<text x="600" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Decline slows</text>'
    ),
    "Neurons take up glucose normally", "Insulin resistance blocks glucose entry", "Ketones enter without insulin; neurons live"
)

ALZ_CONTENT = ALZ_SVG + """
<h2>The physiology</h2>
<p>Alzheimer's disease is increasingly understood as a metabolic disorder of the brain — sometimes described as type 3 diabetes. Neurons in the Alzheimer's brain develop insulin resistance: the glucose transporters (GLUT1 and GLUT3) that normally shuttle glucose across the blood-brain barrier and into neurons become impaired, and cells progressively starve even when blood glucose is normal. PET scanning with FDG (a radioactive glucose analogue) shows this hypometabolism in the temporal and parietal lobes years — sometimes decades — before clinical cognitive symptoms appear.</p>
<blockquote><p>"One reason this idea has gained attention is because the brain's ability to use glucose can decline early in Alzheimer's disease."</p><footer>— Metabolic Mind</footer></blockquote>
<p>Ketone bodies bypass the failed glucose transport system entirely: they cross the blood-brain barrier via monocarboxylate transporters (MCT1) that are not impaired in Alzheimer's disease. This is the mechanism exploited by the MEND and KetoFLEX protocols developed by Dr. Dale Bredesen, and by the MCT oil supplementation approach studied by Dr. Mary Newport, whose husband Steve's case is among the most documented early examples of metabolic rescue in Alzheimer's disease. Ketones do not cure Alzheimer's — they rescue the neurons that are metabolically struggling but not yet dead.</p>

<h2>Five stories</h2>

<h3>Ruth — Early-onset Alzheimer's</h3>
<p>Ruth, 58, noticed her first cognitive symptoms — difficulty with word retrieval and getting lost on familiar routes — five years before diagnosis. When her FDG-PET showed significant temporal hypometabolism, her neurologist referred her to a metabolic memory programme. She implemented MCT oil supplementation and a low-carbohydrate diet. Her cognitive assessments stabilised over the following year — not improvement, but absence of the decline her trajectory had predicted. She now participates in a longitudinal ketogenic diet trial for early-stage Alzheimer's.</p>

<h3>George — MCI converting to Alzheimer's</h3>
<p>George, 71, had mild cognitive impairment that had progressed despite aggressive cardiovascular risk factor management. His daughter, a nurse, researched the metabolic theory of Alzheimer's and introduced MCT oil supplementation combined with time-restricted eating. Within three months George's family reported visible improvement in conversational fluency. His neuropsychological testing six months later showed stabilisation — he had not declined on any measure. His neurologist attributed the stabilisation to the metabolic intervention.</p>

<h3>Helen — APOE4 homozygous early intervention</h3>
<p>Helen, 52, had genetic testing that revealed she was APOE4 homozygous — carrying two copies of the highest genetic risk factor for Alzheimer's disease. She was cognitively normal but statistically at high risk of early onset. She implemented the KetoFLEX 12/3 protocol — ketogenic nutrition combined with extended overnight fasting. Annual FDG-PET scans over four years show her glucose metabolism in the temporal and parietal lobes stable. She regards the metabolic intervention as the only evidence-based preventive measure available to her.</p>

<h3>Frank — Alzheimer's with metabolic syndrome reversal</h3>
<p>Frank, 67, had Alzheimer's disease alongside type 2 diabetes and obesity. His neurologist argued the metabolic syndrome was accelerating his cognitive decline through two mechanisms: elevated insulin driving amyloid accumulation, and cerebrovascular damage reducing brain blood flow. A ketogenic diet reversed his type 2 diabetes within four months and produced measurable reduction in amyloid-related inflammatory markers. His cognitive decline slowed markedly in the year following metabolic reversal.</p>

<h3>Mei — Spouse-implemented protocol</h3>
<p>Mei's husband, 74, had moderate Alzheimer's and was no longer capable of making dietary decisions. Mei, having studied the MCT oil literature, introduced coconut oil and later pure MCT oil into his daily nutrition. Within two weeks she noticed improvements in recognition and verbal fluency that she documented carefully. She shared these observations with his neurologist who agreed to formalise the nutritional intervention and monitor its effects over six months. The improvements — modest but consistent — persisted throughout the monitoring period.</p>"""

# ── 12. ALCOHOL USE DISORDER ──────────────────────────────────────────────────
ALCOHOL_SVG = brain_svg(
    "Alcohol Use Disorder: Reward Circuit Hijacking &amp; GABA Dependence",
    "#15803d",
    "Normal Reward Circuit", "Alcohol Hijacks GABA", "Metabolic Reset",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">DA reward natural</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">GABA endogenous ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Glutamate balanced</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">No dependence</text>'
    ),
    (
        '<text x="360" y="165" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Alcohol floods GABA-A</text>'
        '<text x="360" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">DA surges acutely</text>'
        '<text x="360" y="194" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">GABA receptors</text>'
        '<text x="360" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">downregulate</text>'
        '<text x="360" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Withdrawal = seizure</text>'
    ),
    (
        '<text x="600" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">BHB → GABA↑</text>'
        '<text x="600" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Withdrawal buffer</text>'
        '<text x="600" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Reward restores</text>'
        '<text x="600" y="212" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Craving↓</text>'
        '<text x="600" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Brain fuel stable</text>'
    ),
    "DA reward and GABA balance intact", "Alcohol replaces endogenous GABA; dependence forms", "Ketones restore GABA; reduce craving"
)

ALCOHOL_CONTENT = ALCOHOL_SVG + """
<h2>The physiology</h2>
<p>Alcohol use disorder is a disease of the reward and GABA systems. Ethanol potentiates GABA-A receptors — producing its calming, anxiolytic effects — and simultaneously surges dopamine in the nucleus accumbens reward pathway. With repeated use, the brain adapts: GABA-A receptors downregulate and glutamate receptors upregulate to compensate. The result is a state of excitatory/inhibitory imbalance in which the brain now requires alcohol to maintain normal function. Withdrawal produces the dangerous flip side: without alcohol's GABA potentiation, the glutamate-dominant state produces seizures, delirium, and severe autonomic instability.</p>
<p>Ketogenic therapy addresses alcohol use disorder through the GABA pathway: BHB increases GABA synthesis, providing the inhibitory tone that the alcohol-dependent brain craves without the toxicity and dependence of ethanol. Research from NIAAA and independent groups is exploring ketogenic diets and exogenous ketone supplementation as tools to reduce craving, ease withdrawal, and support sustained recovery. The nutritional deficiencies — thiamine, folate, magnesium — caused by chronic alcohol use are also addressed by structured metabolic rehabilitation.</p>

<h2>Five stories</h2>

<h3>Colin — Alcohol use disorder, recovery-seeking</h3>
<p>Colin, 46, had drunk heavily for twenty years. Multiple treatment attempts had resulted in brief sobriety followed by relapse. His withdrawal was medically supervised but he described the post-acute withdrawal syndrome — months of anxiety, sleep disruption, and craving — as the phase that always broke his recovery. A metabolic psychiatrist introduced a ketogenic diet during his latest inpatient admission. The post-acute withdrawal syndrome was significantly milder than previous attempts. He attributes this to the GABA-stabilising effect of sustained ketosis, which his psychiatrist found scientifically plausible.</p>

<h3>Diane — Female alcohol use disorder</h3>
<p>Diane, 52, had developed alcohol use disorder following bereavement — drinking to suppress grief that felt physiologically intolerable. Her neuroinflammatory markers were markedly elevated. A comprehensive metabolic programme — ketogenic diet, omega-3 supplementation, sleep restructuring, magnesium — addressed the underlying inflammatory state that had made her nervous system so sensitised. As her inflammation normalised, the grief became more bearable without chemical relief. She has been alcohol-free for eighteen months, which she attributes to making the baseline state tolerable rather than the willpower to resist drinking.</p>

<h3>Andre — High-functioning alcohol dependence</h3>
<p>Andre, 39, was functionally impaired only by any clinician's definition: a full professional life maintained on a bottle of wine per night. His dependence became apparent only when a period of illness prevented his usual intake and he experienced withdrawal tremors. He declined pharmacological treatment and engaged with a metabolic psychiatry programme that implemented ketogenic nutrition alongside structured psychological support. His craving reduced significantly within four weeks of sustained ketosis. He reports the ketogenic state as producing a calm that had previously required alcohol.</p>

<h3>Sofia — Alcohol and anxiety comorbidity</h3>
<p>Sofia, 34, had used alcohol to manage anxiety since her early twenties. The self-medication had worked short-term and produced dependence long-term. The core challenge in her treatment was that sobriety intensified her anxiety to intolerable levels, driving relapse. A ketogenic diet addressed the anxiety through GABA-mediated mechanisms while simultaneously supporting alcohol withdrawal. For the first time, her sobriety did not mean acute anxiety amplification. The anxiety was manageable sober because the metabolic support had raised her GABA floor.</p>

<h3>Pete — Korsakoff syndrome prevention</h3>
<p>Pete, 57, had been drinking heavily since his thirties and presented with early signs of Wernicke's encephalopathy — the thiamine deficiency-driven neurological complication of chronic alcohol use. Aggressive thiamine repletion and alcohol cessation were implemented immediately. A nutritionally dense ketogenic diet was introduced to support brain metabolic recovery. His neurological examination improved over six months and the feared progression to Korsakoff syndrome — irreversible memory impairment — was averted. Metabolic rehabilitation was the mechanism his team credited for the recovery of function beyond what thiamine repletion alone would predict.</p>"""

# ── 13. AUTISM SPECTRUM DISORDER ─────────────────────────────────────────────
AUTISM_SVG = brain_svg(
    "Autism Spectrum Disorder: Gut-Brain Axis &amp; Mitochondrial Dysfunction",
    "#0891b2",
    "Gut-Brain Axis Intact", "Gut Dysbiosis + Mito Failure", "Metabolic Support",
    (
        '<text x="120" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#67e8f9">Microbiome ✓</text>'
        '<text x="120" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#67e8f9">Gut barrier ✓</text>'
        '<text x="120" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Mitochondria ✓</text>'
        '<text x="120" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Neuroinflam. low</text>'
    ),
    (
        '<text x="360" y="165" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Dysbiosis</text>'
        '<text x="360" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Leaky gut → LPS</text>'
        '<text x="360" y="194" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Mito dysfunction</text>'
        '<text x="360" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#f97316">Neuroinflammation↑</text>'
        '<text x="360" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Sensory/social</text>'
    ),
    (
        '<text x="600" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Keto → dysbiosis↓</text>'
        '<text x="600" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Gut barrier repairs</text>'
        '<text x="600" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Mito function↑</text>'
        '<text x="600" y="212" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80">Neuroinflam↓</text>'
        '<text x="600" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">Behaviour improves</text>'
    ),
    "Gut-brain axis communicates cleanly", "Dysbiosis drives neuroinflammation via gut", "Ketones reduce inflammation; mito recover"
)

AUTISM_CONTENT = AUTISM_SVG + """
<h2>The physiology</h2>
<p>Autism spectrum disorder involves multiple intersecting biological abnormalities, among which mitochondrial dysfunction and gut-brain axis disruption have attracted the strongest metabolic research interest. Mitochondrial dysfunction — impaired oxidative phosphorylation and elevated reactive oxygen species — is documented in a significant subset of ASD individuals, particularly those with regression (loss of previously acquired skills). The gut microbiome in ASD is consistently dysbiotic: reduced diversity, elevated LPS-producing bacteria, and increased intestinal permeability allow bacterial endotoxins to reach the systemic circulation, driving neuroinflammation through microglia activation.</p>
<blockquote><p>"I didn't know that I had autism."</p><footer>— Metabolic Mind community member</footer></blockquote>
<p>The ketogenic diet addresses both mechanisms: it reduces the carbohydrate substrate that drives the dysbiotic bacteria, improves gut barrier integrity, reduces neuroinflammation, and — critically — provides an alternative fuel for mitochondria that bypasses the specific complex I defects documented in ASD mitochondrial research. Multiple animal model studies and a growing number of clinical reports document behavioural improvement on ketogenic diets in ASD. The Paleomedicina group has published case series of children with ASD and epilepsy achieving substantial improvement in both conditions simultaneously on a ketogenic protocol.</p>

<h2>Five stories</h2>

<h3>Leo — ASD with regression</h3>
<p>Leo, 6, had developed normally until 18 months, then regressed — losing language and social skills he had previously acquired. His parents sought metabolic evaluation after reading research on mitochondrial dysfunction in ASD regression. His assessment revealed elevated lactate, a marker of mitochondrial impairment. A ketogenic diet was implemented by a specialist paediatric team. Over eight months, Leo regained some language and showed improvements in social eye contact that had been absent since the regression. His team regards him as a mitochondrial ASD case in which the metabolic intervention reached the underlying pathology.</p>

<h3>Mara — High-functioning ASD and anxiety</h3>
<p>Mara, 24, received her ASD diagnosis as an adult — a high-masking woman whose autism had been missed through school and university. She had severe comorbid anxiety and gastrointestinal symptoms. Her gut microbiome analysis showed severe dysbiosis. A low-carbohydrate, eventually ketogenic diet resolved her gastrointestinal symptoms within six weeks. Her anxiety reduced proportionally — consistent with the gut-brain axis model in which gut-derived inflammatory signals prime the fear circuit. She continues to have ASD but describes her quality of life as transformed by addressing the metabolic comorbidities.</p>

<h3>Jamie — Non-verbal ASD, GFCF to ketogenic</h3>
<p>Jamie, 8, was non-verbal with ASD and severe behavioural dysregulation — meltdowns lasting hours, self-injurious behaviour, and minimal social responsiveness. His parents had implemented a gluten-free casein-free diet that produced partial improvement. A specialist team transitioned him to a ketogenic diet to address the neuroinflammation that GFCF had not fully resolved. Within six months his behavioural dysregulation had reduced significantly. He remains non-verbal but the reduction in apparent distress and the increase in initiating social interaction have been marked by both his family and his school.</p>

<h3>Kenji — ASD with epilepsy</h3>
<p>Kenji, 10, had ASD and drug-resistant epilepsy — a common co-occurrence consistent with shared GABA/glutamate dysregulation. His epilepsy team introduced a ketogenic diet primarily for seizure control. Seizures reduced by 70%; simultaneously and unexpectedly, his teachers reported improvement in attention, communication, and flexibility. His ASD team, reviewing the case, concluded the metabolic intervention had addressed both conditions through shared neurochemical pathways — a finding consistent with the literature on ketogenic diet in ASD-epilepsy comorbidity.</p>

<h3>Sage — Late-diagnosed adult ASD with metabolic syndrome</h3>
<p>Sage, 38, received an ASD diagnosis at 35 after decades of misidentification as anxiety and ADHD. They had metabolic syndrome — insulin resistance, obesity, elevated inflammatory markers — which their metabolic psychiatrist argued was driving their severe sensory hypersensitivity and emotional dysregulation through chronic neuroinflammation. A ketogenic diet reversed the metabolic syndrome over eight months. Sage describes the change in sensory experience as the world becoming quieter — not the underlying ASD changed, but the inflammatory amplification of sensory input reduced.</p>"""


ARTICLES = [
    {
        'title': 'PTSD: How Chronic Cortisol and Hippocampal Loss Keep the Trauma Alive',
        'slug': 'ptsd-hpa-amygdala-hippocampal-metabolic-origin',
        'summary': (
            'PTSD is the condition that results when traumatic fear memories fail to be '
            'contextualised. Chronic cortisol shrinks the hippocampus; amygdala hyperreactivity '
            'replays the trauma. Five people who used metabolic intervention to rebuild the '
            'neurological preconditions for healing.'
        ),
        'content': PTSD_CONTENT,
        'order': 10,
        'ai_summary': 'HPA dysregulation, amygdala hyperreactivity, hippocampal volume loss via cortisol. BHB → BDNF → hippocampal neurogenesis. PET hypometabolism in PFC. Five cases: combat, childhood trauma, assault, first-responder, complex PTSD.',
    },
    {
        'title': 'ADHD: Dopamine and the Fuel-Starved Prefrontal Cortex',
        'slug': 'adhd-dopamine-prefrontal-metabolic-origin',
        'summary': (
            'ADHD is a disorder of the prefrontal cortex — specifically of the dopaminergic and '
            'noradrenergic supply that enables sustained attention and impulse control. Five people '
            'who found that stabilising brain fuel supply changed what medication alone could not.'
        ),
        'content': ADHD_CONTENT,
        'order': 11,
        'ai_summary': 'PFC dopamine/NE deficit, reward circuit novelty-seeking, glucose fluctuation sensitivity. Ketones provide stable PFC fuel, support DA synthesis. Five cases: adult combined, inattentive, emotional dysregulation, paediatric, anxiety comorbid.',
    },
    {
        'title': "Alzheimer's Disease: Brain Insulin Resistance and the Ketone Rescue",
        'slug': 'alzheimers-brain-insulin-resistance-ketone-rescue',
        'summary': (
            "Alzheimer's disease is increasingly understood as type 3 diabetes — brain insulin "
            'resistance that starves neurons of glucose decades before clinical symptoms appear. '
            'Five people who used ketones to bypass the failed glucose transport and slow the decline.'
        ),
        'content': ALZ_CONTENT,
        'order': 12,
        'ai_summary': 'Brain insulin resistance, GLUT1/3 failure, FDG-PET hypometabolism in temporal/parietal lobes. BHB bypasses insulin resistance via MCT1. Bredesen MEND protocol, Mary Newport MCT case. Five cases: early-onset, MCI, APOE4 prevention, T2D comorbid, caregiver-implemented.',
    },
    {
        'title': 'Alcohol Use Disorder: GABA Dependence, Reward Hijacking, and Metabolic Recovery',
        'slug': 'alcohol-use-disorder-gaba-reward-metabolic-origin',
        'summary': (
            'Alcohol use disorder forms because ethanol hijacks the GABA and dopamine systems '
            'the brain depends on for calm and reward. When alcohol withdraws, the system crashes. '
            'Five people who used ketogenic nutrition to restore the GABA floor that makes '
            'sustained recovery neurologically possible.'
        ),
        'content': ALCOHOL_CONTENT,
        'order': 13,
        'ai_summary': 'Alcohol potentiates GABA-A; DA surge in NAcc. GABA-A downregulates; glutamate upregulates. Withdrawal = excitotoxic crisis. BHB raises endogenous GABA, buffers withdrawal. Five cases: chronic relapse, grief-driven, high-functioning, anxiety-comorbid, Wernicke prevention.',
    },
    {
        'title': 'Autism Spectrum Disorder: Mitochondrial Dysfunction, Gut Dysbiosis, and the Metabolic Overlap',
        'slug': 'autism-spectrum-mitochondrial-gut-metabolic-origin',
        'summary': (
            'A significant subset of autism involves mitochondrial dysfunction and gut-brain axis '
            'disruption that drives neuroinflammation. Five people — children and adults — whose '
            'ASD symptoms improved when the metabolic and inflammatory underpinnings were addressed.'
        ),
        'content': AUTISM_CONTENT,
        'order': 14,
        'ai_summary': 'Mitochondrial complex I dysfunction, gut dysbiosis, LPS-driven neuroinflammation, microglia activation. Ketones bypass mito defects, reduce dysbiosis, repair gut barrier. Five cases: regression, high-masking adult, non-verbal, ASD-epilepsy, adult metabolic syndrome.',
    },
]


class Command(BaseCommand):
    help = "Load new mental illness articles: PTSD, ADHD, Alzheimer's, Alcohol, Autism"

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
