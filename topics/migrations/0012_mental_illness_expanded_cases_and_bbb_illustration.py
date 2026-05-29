from django.db import migrations

BBB_SVG = """
<figure style="margin:2em 0 2.5em;">
<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="How ketones generated from fat by the liver cross the blood-brain barrier, which fat itself cannot fuel neurons directly">
  <defs>
    <marker id="arrG" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#22c55e"/></marker>
    <marker id="arrO" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#f97316"/></marker>
    <marker id="arrR" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#ef4444"/></marker>
  </defs>
  <rect width="760" height="290" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="380" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13.5" fill="#f1f5f9" font-weight="700">How Ketones Fuel the Brain — Fat Cannot Cross, Ketones Can</text>
  <text x="380" y="46" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">The liver converts fat (triglycerides) into ketone bodies — small molecules that freely cross the blood-brain barrier</text>

  <!-- Zone labels -->
  <text x="118" y="68" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">FAT STORES &amp; LIVER</text>
  <text x="373" y="68" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">BLOODSTREAM</text>
  <text x="630" y="68" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" font-weight="600">BRAIN</text>

  <!-- Zone divider -->
  <line x1="240" y1="58" x2="240" y2="278" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Blood-Brain Barrier -->
  <rect x="506" y="58" width="8" height="220" fill="#f59e0b" opacity="0.12" rx="3"/>
  <line x1="510" y1="58" x2="510" y2="278" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="7,4"/>
  <text x="510" y="286" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f59e0b" font-weight="700">Blood-Brain Barrier</text>

  <!-- Adipose fat droplet -->
  <circle cx="65" cy="158" r="33" fill="#1c0f05" stroke="#f97316" stroke-width="1.5"/>
  <circle cx="62" cy="150" r="17" fill="#f97316" opacity="0.22"/>
  <circle cx="75" cy="168" r="11" fill="#f97316" opacity="0.18"/>
  <circle cx="52" cy="167" r="9"  fill="#f97316" opacity="0.18"/>
  <text x="65" y="155" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#fdba74" font-weight="700">FAT</text>
  <text x="65" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#fdba74">adipose</text>
  <text x="65" y="203" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">Triglycerides</text>
  <text x="65" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">(dietary fat / fasting)</text>

  <!-- Arrow: fat → liver -->
  <path d="M 100 158 L 142 158" stroke="#f97316" stroke-width="2" fill="none" marker-end="url(#arrO)"/>

  <!-- Liver -->
  <rect x="148" y="122" width="84" height="72" rx="9" fill="#111805" stroke="#84cc16" stroke-width="1.5"/>
  <text x="190" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11.5" fill="#bef264" font-weight="700">LIVER</text>
  <text x="190" y="158" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a3e635">β-oxidation</text>
  <text x="190" y="171" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a3e635">Acetyl-CoA →</text>
  <text x="190" y="184" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a3e635">Ketogenesis</text>

  <!-- Arrow: liver → ketones -->
  <path d="M 232 158 L 270 158" stroke="#22c55e" stroke-width="2.2" fill="none" marker-end="url(#arrG)"/>
  <text x="251" y="151" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">produces</text>

  <!-- Ketone bodies box (green) -->
  <rect x="276" y="96" width="148" height="98" rx="9" fill="#021a0f" stroke="#22c55e" stroke-width="1.8"/>
  <text x="350" y="116" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#86efac" font-weight="700">Ketone Bodies</text>
  <line x1="290" y1="123" x2="410" y2="123" stroke="#14532d" stroke-width="0.8"/>
  <text x="350" y="137" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">β-Hydroxybutyrate (BHB)</text>
  <text x="350" y="150" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">Acetoacetate (AcAc)</text>
  <text x="350" y="163" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">small · water-soluble</text>
  <text x="350" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80" font-weight="700">✓  Crosses BBB via MCT1</text>

  <!-- Fat TG blocked box (red) -->
  <rect x="276" y="210" width="148" height="55" rx="9" fill="#1a0505" stroke="#ef4444" stroke-width="1.5"/>
  <text x="350" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#fca5a5" font-weight="700">Triglycerides (Fat)</text>
  <text x="350" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">large lipid molecules</text>
  <text x="350" y="258" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#ef4444" font-weight="700">✕  Cannot directly fuel neurons</text>

  <!-- Arrow: ketones → BBB crossing (green) -->
  <path d="M 424 145 L 504 145" stroke="#22c55e" stroke-width="2.5" fill="none" marker-end="url(#arrG)"/>
  <text x="463" y="138" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">MCT1 transporter ✓</text>

  <!-- Fat blocked at BBB (red dashed) -->
  <path d="M 424 237 L 494 237" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="5,3" fill="none"/>
  <text x="512" y="242" text-anchor="middle" font-family="system-ui,sans-serif" font-size="20" fill="#ef4444">✕</text>

  <!-- Neuron box (right) -->
  <rect x="522" y="80" width="220" height="190" rx="12" fill="#080e24" stroke="#818cf8" stroke-width="1.8"/>
  <text x="632" y="102" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#a5b4fc" font-weight="700">Neuron</text>
  <line x1="534" y1="110" x2="730" y2="110" stroke="#1e2a5a" stroke-width="1"/>
  <text x="632" y="126" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">Ketones → Acetyl-CoA → ATP</text>
  <text x="632" y="140" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">~25% more efficient than glucose</text>
  <line x1="534" y1="149" x2="730" y2="149" stroke="#1e2a5a" stroke-width="0.8" stroke-dasharray="3,3"/>
  <text x="632" y="165" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac" font-weight="700">Brain Benefits</text>
  <text x="632" y="181" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#67e8f9">↑ GABA — calming neurotransmitter</text>
  <text x="632" y="196" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#67e8f9">↓ Neuroinflammation</text>
  <text x="632" y="211" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#67e8f9">↑ Mitochondrial biogenesis</text>
  <text x="632" y="226" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#67e8f9">↓ Oxidative stress</text>
  <text x="632" y="241" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#67e8f9">Bypasses impaired glucose uptake</text>
  <text x="632" y="256" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#6b7280">(depression, Alzheimer's, epilepsy)</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Fat (triglycerides) cannot directly fuel neurons — the liver must convert it to ketone bodies first. Ketones cross the blood-brain barrier freely via MCT1 transporters; fat cannot. This is why ketogenic therapy reaches the brain when other dietary changes do not.</figcaption>
</figure>
"""

MAIN_SVG = """
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
  <text x="107" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Marcus · Elena · Theo</text>
  <text x="107" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic therapy</text>
  <text x="107" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">anti-inflammatory · CBT</text>
  <text x="107" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">remission 8–14 months</text>
  <text x="107" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="195" y="65" width="155" height="155" rx="10" fill="#0f172a" stroke="#2563eb" stroke-width="1.2"/>
  <text x="272" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Anxiety</text>
  <text x="272" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala hyperactivation</text>
  <text x="272" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">GABA deficit · cortisol</text>
  <line x1="215" y1="128" x2="329" y2="128" stroke="#2563eb" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Sofia · Rashida · Omar</text>
  <text x="272" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Low-carb + ketones</text>
  <text x="272" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">CBT · magnesium · sleep</text>
  <text x="272" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">remission 6 months</text>
  <text x="272" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="360" y="65" width="155" height="155" rx="10" fill="#0f172a" stroke="#0e7490" stroke-width="1.2"/>
  <text x="437" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#67e8f9" font-weight="700">Bipolar Disorder</text>
  <text x="437" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Circadian disruption</text>
  <text x="437" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Mitochondrial energy</text>
  <line x1="380" y1="128" x2="495" y2="128" stroke="#0e7490" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">James · Nina · Ray</text>
  <text x="437" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="437" y="169" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">lithium · sleep protocol</text>
  <text x="437" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">stable 2+ years</text>
  <text x="437" y="197" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Stable</text>

  <rect x="525" y="65" width="165" height="155" rx="10" fill="#0f172a" stroke="#be185d" stroke-width="1.2"/>
  <text x="607" y="86"  text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#fbcfe8" font-weight="700">Schizophrenia</text>
  <text x="607" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Dopamine · Glutamate</text>
  <text x="607" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Prefrontal hypoactivity</text>
  <line x1="545" y1="128" x2="670" y2="128" stroke="#be185d" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Amara · Kwame · Yuki</text>
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
  <text x="107" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Lucas · Beatriz · Nathan</text>
  <text x="107" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="107" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">100yr standard of care</text>
  <text x="107" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">seizure-free</text>
  <text x="107" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Seizure-free</text>

  <rect x="195" y="240" width="155" height="155" rx="10" fill="#0f172a" stroke="#0f766e" stroke-width="1.2"/>
  <text x="272" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#5eead4" font-weight="700">Anorexia</text>
  <text x="272" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Hypothalamic signaling</text>
  <text x="272" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Leptin · ghrelin · reward</text>
  <line x1="215" y1="303" x2="329" y2="303" stroke="#0f766e" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="272" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Claire · Sasha · Lena</text>
  <text x="272" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic therapy</text>
  <text x="272" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">FBT · nutritional rehab</text>
  <text x="272" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">eating disorder remission</text>
  <text x="272" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● In remission</text>

  <rect x="360" y="240" width="155" height="155" rx="10" fill="#0f172a" stroke="#9333ea" stroke-width="1.2"/>
  <text x="437" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#d8b4fe" font-weight="700">OCD</text>
  <text x="437" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">CSTC circuit overactivity</text>
  <text x="437" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Serotonin · caudate nucleus</text>
  <line x1="380" y1="303" x2="495" y2="303" stroke="#9333ea" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="437" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">David · Mia · Eli</text>
  <text x="437" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Ketogenic diet</text>
  <text x="437" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">ERP therapy · SSRI</text>
  <text x="437" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">60–80% symptom reduction</text>
  <text x="437" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● 60–80% reduction</text>

  <rect x="525" y="240" width="165" height="155" rx="10" fill="#0f172a" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="607" y="261" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11"   fill="#93c5fd" font-weight="700">Phobia</text>
  <text x="607" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Amygdala fear memory</text>
  <text x="607" y="289" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#64748b">Norepinephrine · cortisol</text>
  <line x1="545" y1="303" x2="670" y2="303" stroke="#1d4ed8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="607" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">Priya · Fatima · Ben</text>
  <text x="607" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#fbbf24">🥑 Metabolic support</text>
  <text x="607" y="344" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">EMDR · exposure therapy</text>
  <text x="607" y="357" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8"    fill="#94a3b8">fear response resolved</text>
  <text x="607" y="372" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#4ade80">● Resolved</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Eight conditions, eight physiological origins — ketogenic and metabolic therapy as a common thread in recovery</figcaption>
</figure>
"""

EXTRA_CASES_STYLE = "background:#0d1827;border-left:3px solid {color};padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;"
NAME_STYLE = "color:{color};font-weight:700;"
CASE_P_STYLE = "margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"
CASE_LAST_P_STYLE = "margin:0;font-size:0.93em;line-height:1.6;"

UPDATED_CONTENT = """
<p class="lead">Mental illness is not weakness, failure, or a broken personality. It is physiology —
disrupted neural circuits, imbalanced neurotransmitters, misfiring hormonal axes, and runaway
inflammation in the brain. Emerging research from metabolic psychiatry now adds a critical insight:
the brain is the most metabolically demanding organ in the body, and when its fuel supply
falters, so does its function. The following are twenty-four stories of people who suffered, sought
help, and found their way to remission — many through pathways that included ketogenic and metabolic
therapy. Names have been changed to protect identity.</p>

""" + MAIN_SVG + """

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
structured cognitive behavioural therapy. Crucially, Marcus also began a ketogenic diet under
clinical supervision. Ketones bypass the impaired glucose metabolism pathways, providing neurons
with a direct, efficient fuel source that crosses the blood-brain barrier even when glucose
uptake is impaired. Marcus also eliminated ultra-processed food, added omega-3s, and walked
30 minutes each morning.</p>

<p><strong>Remission:</strong> within eight months, the fog lifted. Marcus describes it as
"returning to myself." He attributes recovery to the combination — medication, therapy, and
shifting his brain's fuel source.</p>

<div style="background:#0d1827;border-left:3px solid #7c3aed;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#c4b5fd;">Elena, 52</strong> — Perimenopause triggered her first depressive episode after 20 years of good mental health. Oestrogen decline had amplified her cortisol sensitivity and depleted serotonin. Her GP added hormone therapy; a psychiatrist prescribed a short SSRI course; and a nutritionist guided her onto a ketogenic diet that stabilised blood glucose and reduced her inflammatory markers. Symptom-free within ten months — she now runs a perimenopause peer support group.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#c4b5fd;">Theo, 22</strong> — Two SSRIs had failed before a university mental health team referred him to a metabolic psychiatry clinic. Brain imaging showed reduced prefrontal glucose uptake — a pattern increasingly documented in treatment-resistant depression. A ketogenic protocol was added to low-dose lithium augmentation; depression scores halved in four months. He returned to complete his final year of engineering.</p>
</div>

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
Sofia began cognitive behavioural therapy with an exposure protocol. She reduced dietary
carbohydrates substantially — improving metabolic health measurably improves mental health
outcomes, including anxiety. Stabilising blood glucose removed a key physiological driver of
her cortisol spikes. She added magnesium glycinate to support GABA signalling and practised
daily breathwork to activate the vagus nerve.</p>

<p><strong>Remission:</strong> six months later, Sofia returned to her PhD. Panic attacks reduced
from weekly to once in four months. She completed her doctorate and now teaches mindfulness to
other graduate students.</p>

<div style="background:#0d1827;border-left:3px solid #2563eb;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#93c5fd;">Rashida, 38</strong> — Health anxiety following a cancer scare that proved benign; she spent hours each day researching symptoms online. CBT broke the reassurance-seeking cycle, while reducing dietary sugar and refined carbohydrates removed the afternoon cortisol spikes that had been amplifying her rumination. Discharged after six months, largely symptom-free.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#93c5fd;">Omar, 44</strong> — Social anxiety had stalled his career despite obvious talent; he froze before client presentations. An SSRI helped, as did magnesium glycinate at night; a lower-glycaemic diet eliminated the energy crashes that had heightened self-consciousness in social settings. He now leads team presentations and was promoted to senior partner.</p>
</div>

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
regulating circadian gene expression and protecting neuronal mitochondria. James adopted a
rigid sleep protocol. He also began a carefully managed ketogenic diet — with guidance on
keeping ketone levels in a therapeutic range (not excessively high, as very elevated ketones
can occasionally be activating in some bipolar patients). The combination addressed both the
neurotransmitter and energy-metabolism dimensions of his illness.</p>

<p><strong>Remission:</strong> two years without a full manic or depressive episode. James
describes his life as "narrower but real — I live in the middle now, and the middle is
actually very good."</p>

<div style="background:#0d1827;border-left:3px solid #0e7490;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#67e8f9;">Nina, 33</strong> — Rapid-cycling bipolar II with four mood episodes in a single year before correct diagnosis. Lamotrigine brought partial stabilisation; a ketogenic diet introduced at a metabolic psychiatry clinic resolved residual cycling within three months. She runs a bipolar peer support network and attributes three things to her stability: consistent sleep, medication, and keeping carbohydrates low.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#67e8f9;">Ray, 55</strong> — Long-standing bipolar I with multiple hospitalisations over 20 years. His metabolic psychiatrist added a ketogenic dietary protocol alongside existing valproate; hospitalisation frequency dropped from twice yearly to zero over the next two years. He describes the change as "the medication helped, but the energy stability the diet gave my brain changed everything."</p>
</div>

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
metabolic environment of the brain central to the illness. Pilot studies have demonstrated
ketogenic therapy as an adjunct for schizophrenia, with some patients showing meaningful
reductions in symptom severity alongside their antipsychotic regimen.</p>

<p><strong>The turn:</strong> Amara was referred to an early psychosis intervention team. A
psychiatrist started a second-generation antipsychotic. A psychologist provided cognitive therapy.
Several months into her recovery, her care team introduced a ketogenic dietary protocol as an
adjunct — with careful attention to the fact that some antipsychotic medications can impede
ketosis, requiring close prescriber collaboration.</p>

<p><strong>Remission:</strong> the voices are now quiet most days. Amara completed a certificate
in graphic design and works part-time. She describes the combination of medication, therapy,
and dietary change as "a three-legged stool — remove any one leg and it falls."</p>

<div style="background:#0d1827;border-left:3px solid #be185d;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#fbcfe8;">Kwame, 28</strong> — First-episode psychosis at 25; maintained on clozapine but had gained 22 kg and developed pre-diabetes — common metabolic side effects of the medication. A ketogenic dietary intervention reversed the metabolic complications and, unexpectedly, reduced residual negative symptoms including flat affect and social withdrawal. He returned to work full-time.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#fbcfe8;">Yuki, 35</strong> — Chronic schizophrenia with treatment-resistant auditory hallucinations despite two antipsychotics over ten years. Enrolled in a metabolic psychiatry pilot; ketogenic therapy reduced the voices from continuous to intermittent within eight weeks. She describes the voices now as "further away — I can hear myself think again."</p>
</div>

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
drug-resistant epilepsy for over 100 years.</p>

<p><strong>The turn:</strong> his neurologist proposed the classical ketogenic diet under a
specialist ketogenic dietitian. Lucas transitioned to nutritional ketosis with close medical
supervision, with his existing medication carefully maintained and adjusted.</p>

<p><strong>Remission:</strong> seizure-free for 18 months. Lucas has returned to sport and is
completing his final year of school. His neurologist has begun discussing gradual medication
reduction. His parents call it "a second life."</p>

<div style="background:#0d1827;border-left:3px solid #d97706;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#fcd34d;">Beatriz, 7</strong> — Absence epilepsy causing dozens of episodes daily, poorly controlled on two medications. A classical ketogenic diet (4:1 fat-to-protein-carbohydrate ratio) was initiated under a specialist neurological dietitian at a paediatric epilepsy centre. Seizure-free within six weeks; medications gradually tapered. Her teachers describe a complete transformation in classroom attention and engagement.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#fcd34d;">Nathan, 42</strong> — Seizures began after a traumatic brain injury; anti-epileptic drugs reduced frequency but could not eliminate them. A Modified Atkins Diet — a less restrictive ketogenic variant designed for adults — reduced his monthly seizure count from 12 to 2 and allowed him to return to driving. He has maintained the dietary approach for three years.</p>
</div>

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
the very cognitive capacity needed to choose recovery. Ketogenic therapy, used appropriately in
weight-restored patients, has helped put eating disorders into remission — likely by stabilising
reward circuitry, reducing anxiety around food, and providing metabolic stability that the
previously glucose-dependent brain could not achieve.</p>

<p><strong>The turn:</strong> Claire's parents initiated family-based treatment (FBT) — the
evidence-based protocol in which the family controls feeding initially, bypassing the paralysed
volition of the starving brain. As weight restored, cognitive distortions lessened. Once medically
stable, her nutritional approach shifted toward a lower-carbohydrate, higher-fat pattern —
reducing the glucose instability and anxiety spikes that had previously surrounded meals.</p>

<p><strong>Remission:</strong> eating disorder in remission. Weight restored. Claire is in her
second year of university studying nutrition science and speaks publicly about the metabolic
dimension of eating disorder recovery.</p>

<div style="background:#0d1827;border-left:3px solid #0f766e;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#5eead4;">Sasha, 17</strong> — Anorexia athletica: restriction disguised as athletic commitment, running 15 km daily on fewer than 700 calories. Family-based treatment restored weight; once medically stable, a structured higher-fat, lower-sugar eating plan eliminated the glucose-driven anxiety spikes that had surrounded meals and destabilised her recovery. Now training appropriately for her age under a sports physiologist.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#5eead4;">Lena, 26</strong> — Two prior inpatient admissions before she found a treatment team that incorporated metabolic psychiatry support alongside CBT. A higher-fat eating pattern stabilised her appetite hormones — leptin and ghrelin — reducing the obsessive food thoughts that had preceded each previous relapse. In remission for 18 months and studying to become a therapist specialising in eating disorders.</p>
</div>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>7. David — Obsessive Compulsive Disorder (OCD)</h2>
<p><em>Physiological origin: cortico-striato-thalamo-cortical (CSTC) circuit hyperactivity,
serotonin dysregulation, caudate nucleus dysfunction, neuroinflammation</em></p>

<p>David, 31, spent four hours each morning checking that the gas was off, the locks were turned,
the appliances unplugged — the same loop repeated until he was late for work every day. He knew
the stove was off. He checked again. His girlfriend moved out; his job was in jeopardy.</p>

<p>The biology: OCD involves overactivity in the CSTC loop connecting the prefrontal cortex,
caudate nucleus, and thalamus — normally this circuit filters thoughts and signals "good enough,
move on." In OCD, it fires repeatedly without resolution. A published three-case series showed
meaningful OCD symptom reduction with ketogenic dietary therapy, with one patient going from
severely disabled to functionally thriving. The proposed mechanism involves ketones reducing
neuroinflammation in the CSTC circuit and improving GABAergic inhibition that normally brakes
compulsive loops.</p>

<p><strong>The turn:</strong> David was referred to a specialist in exposure and response
prevention (ERP) — the gold standard for OCD. He also began a high-dose SSRI. After reading
about the published case series, he worked with his psychiatrist to introduce a ketogenic diet
alongside his existing treatment.</p>

<p><strong>Remission:</strong> an 80% reduction in compulsion time within nine months. David
now checks the gas once. He describes ERP as "the hardest thing I've done" and keto as
"the thing that made the hardest thing possible."</p>

<div style="background:#0d1827;border-left:3px solid #9333ea;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#d8b4fe;">Mia, 24</strong> — Contamination OCD with five-hour daily hand-washing rituals that had ended her nursing career before it started. ERP was the primary treatment; after six weeks of partial response, her psychiatrist introduced a ketogenic diet based on the published case series. Ritual time fell from five hours to 20 minutes by month four. She returned to nursing school the following year.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#d8b4fe;">Eli, 47</strong> — Harm OCD and decades of partial response to SSRIs despite multiple medication trials and years of CBT. A metabolic psychiatrist introduced ketogenic dietary therapy as an adjunct; his Yale-Brown OCD score fell 60% over 12 months. He describes the dietary change as "turning down the volume on every intrusive thought — they're still there but they no longer shout."</p>
</div>

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
system was already primed for alarm when any trigger appeared.</p>

<p><strong>The turn:</strong> Priya's therapist used EMDR to reprocess the original trapped-lift
memory, combined with graduated exposure therapy. She also began a lower-carbohydrate eating
pattern — eliminating the blood glucose swings that were amplifying her sympathetic nervous
system baseline. A short course of propranolol blunted the physical fear response during critical
exposure sessions.</p>

<p><strong>Remission:</strong> Priya now takes lifts daily. She completed a major high-rise
project and has been promoted. She describes her former avoidance as "a cage that got smaller
every year — the combination of therapy and metabolic change broke it open."</p>

<div style="background:#0d1827;border-left:3px solid #1d4ed8;padding:0.85em 1.2em;border-radius:0 8px 8px 0;margin:1em 0 0;">
  <p style="margin:0 0 0.55em;font-size:0.93em;line-height:1.6;"><strong style="color:#93c5fd;">Fatima, 35</strong> — Needle phobia preventing cancer screening; she had not had a blood test in seven years. A single-session exposure therapy protocol, combined with metabolic stabilisation (eliminating the sugary snack she had relied on as pre-appointment comfort, which had been spiking and crashing her blood glucose in the waiting room), allowed her to complete the session calmly. She has since completed three blood draws and her first mammogram.</p>
  <p style="margin:0;font-size:0.93em;line-height:1.6;"><strong style="color:#93c5fd;">Ben, 22</strong> — Emetophobia — fear of vomiting — had restricted his diet to a handful of "safe" foods for five years and prevented international travel. CBT with graded exposure; a higher-fat, lower-carbohydrate diet eliminated the nausea from blood glucose drops he had been misreading as pre-vomiting signals. He now eats freely, travels internationally, and recently backpacked through Southeast Asia.</p>
</div>

<hr style="border-color:#1e293b;margin:2em 0;"/>

<h2>The Metabolic Thread</h2>

<p>Across all twenty-four stories runs a common biological insight: the brain is the most
metabolically demanding organ in the body, consuming roughly 20% of total energy despite
representing only 2% of body weight. When that energy supply is disrupted — by glucose
dysregulation, mitochondrial dysfunction, neuroinflammation, or insulin resistance —
brain circuits malfunction in ways we label as psychiatric illness.</p>

""" + BBB_SVG + """

<p>The diagram above captures the mechanism. Dietary fat and stored body fat (triglycerides)
cannot directly fuel neurons — the brain has minimal capacity to oxidise fatty acids. Instead,
the liver performs β-oxidation: it cleaves fatty acids into acetyl-CoA and packages the
surplus into ketone bodies — primarily beta-hydroxybutyrate (BHB) and acetoacetate. These
small, water-soluble molecules cross the blood-brain barrier freely via MCT1 transporters,
entering neurons where they are converted back into acetyl-CoA and fed into the mitochondrial
energy cycle.</p>

<p>The result is a more efficient fuel — ketones yield approximately 25% more ATP per unit
of oxygen than glucose, while simultaneously raising GABA (the brain's primary calming
neurotransmitter), reducing neuroinflammation, and supporting mitochondrial biogenesis.
Crucially, this pathway bypasses impaired glucose transporters — a common finding in
depression, Alzheimer's disease, and epilepsy — delivering energy to neurons that have
effectively stopped responding to glucose.</p>

<p>Ketogenic therapy addresses this at the root. It is not a replacement for medication or
therapy — but it is an adjunct that, for many patients, changes the trajectory of serious
mental illness by addressing the energy crisis that underlies it.</p>

<blockquote>
  <p>"The evidence continues to grow that improving metabolic health can improve mental health."</p>
  <footer>— Metabolic Mind</footer>
</blockquote>

<p>Remission is possible. It may require medication, therapy, dietary change, or all three.
But across every condition described here, the human brain demonstrated what both neuroscience
and metabolic psychiatry increasingly confirm: it retains a remarkable capacity for recovery
when given the right fuel and the right conditions.</p>
"""


def update_mental_illness_expanded(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug='mental-illness-physiological-origin-stories').update(
        content=UPDATED_CONTENT,
        summary=(
            "Depression, anxiety, bipolar disorder, schizophrenia, epilepsy, anorexia, OCD, and phobia — "
            "each has a physiological and metabolic origin. Twenty-four people, three per condition, found "
            "remission through combinations of therapy, medication, and ketogenic dietary intervention. "
            "Includes a diagram of how ketones generated by the liver from fat cross the blood-brain barrier."
        ),
        ai_summary=(
            "Twenty-four patient vignettes (three per condition) covering depression, anxiety, bipolar, "
            "schizophrenia, epilepsy, anorexia, OCD, and phobia — each with physiological mechanism, "
            "ketogenic/metabolic therapy role, treatment approach, and remission outcome. Includes SVG "
            "illustration of the fat → liver → ketone → blood-brain-barrier → neuron pathway. "
            "Sourced from Metabolic Mind transcripts."
        ),
    )


def reverse_update(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0011_mental_illness_physiological_origin_pillar'),
    ]

    operations = [
        migrations.RunPython(update_mental_illness_expanded, reverse_update),
    ]
