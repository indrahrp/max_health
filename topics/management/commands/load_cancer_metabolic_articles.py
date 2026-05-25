from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Cancer Biology",
    "slug": "biology",
    "description": (
        "The science of what cancer actually is — and why the leading theory may be wrong. "
        "We cover mitochondria, metabolism, and the experiments that changed what researchers think."
    ),
    "icon": "🔬",
    "color": "teal",
    "order": 6,
}

# ─────────────────────────────────────────────────────────────────────────────
# ARTICLE 1: The Genetic Theory Problem
# ─────────────────────────────────────────────────────────────────────────────

SVG_1 = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Two competing theories of cancer compared side by side">
  <defs>
    <marker id="arr1" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#475569"/>
    </marker>
  </defs>

  <rect width="720" height="420" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Two Theories of Cancer</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#475569">Which one better explains what we see?</text>

  <!-- VS divider -->
  <line x1="360" y1="60" x2="360" y2="395" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="338" y="180" width="44" height="26" fill="#1e293b" rx="6"/>
  <text x="360" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#94a3b8" font-weight="700">VS</text>

  <!-- LEFT: Somatic Mutation Theory -->
  <rect x="16" y="60" width="326" height="340" fill="#0f172a" rx="12" stroke="#1e3a5f" stroke-width="1"/>
  <rect x="16" y="60" width="326" height="36" fill="#1d3557" rx-top-left="12" rx-top-right="12"/>
  <!-- rounded top corners manually -->
  <rect x="16" y="78" width="326" height="18" fill="#1d3557"/>
  <text x="179" y="84" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#93c5fd" font-weight="700">SOMATIC MUTATION THEORY</text>
  <text x="179" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#60a5fa">Dominant view · ~1970s–present</text>

  <!-- DNA double helix icon (left) -->
  <g transform="translate(120,120)">
    <!-- helix left strand -->
    <path d="M -18,0 C -10,-14 10,-14 18,0 C 10,14 -10,14 -18,0" stroke="#3b82f6" stroke-width="2" fill="none"/>
    <path d="M -18,0 C -10,14 10,14 18,0" stroke="#3b82f6" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
    <!-- X marks for mutations -->
    <line x1="-6" y1="-6" x2="6" y2="6" stroke="#f87171" stroke-width="2"/>
    <line x1="6" y1="-6" x2="-6" y2="6" stroke="#f87171" stroke-width="2"/>
    <circle cx="-18" cy="0" r="5" fill="#1d4ed8"/>
    <circle cx="18" cy="0" r="5" fill="#1d4ed8"/>
    <!-- label -->
    <text x="0" y="32" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#93c5fd">Damaged DNA</text>
    <text x="0" y="44" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">(mutation ✗)</text>
  </g>

  <!-- Left theory explanation bullets -->
  <text x="34" y="185" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">Claim: Cancer starts when DNA in the</text>
  <text x="34" y="198" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">nucleus mutates — turning off tumor</text>
  <text x="34" y="211" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">suppressors or activating oncogenes.</text>

  <text x="34" y="234" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Problems researchers found:</text>
  <circle cx="43" cy="249" r="3" fill="#f87171"/>
  <text x="52" y="253" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">Cancers with no mutations found</text>
  <circle cx="43" cy="266" r="3" fill="#f87171"/>
  <text x="52" y="270" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">Mutations differ in every single cell</text>
  <circle cx="43" cy="283" r="3" fill="#f87171"/>
  <text x="52" y="287" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">No consistent "driver" mutation found</text>
  <circle cx="43" cy="300" r="3" fill="#f87171"/>
  <text x="52" y="304" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">Normal cells can have same mutations</text>
  <circle cx="43" cy="317" r="3" fill="#f87171"/>
  <text x="52" y="321" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">50 yrs of gene-targeting: limited cures</text>

  <rect x="24" y="333" width="310" height="22" fill="#1e293b" rx="6"/>
  <text x="179" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8">Focus: target the mutations one by one →</text>
  <text x="179" y="361" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8">whack-a-mole against thousands of variants</text>

  <!-- RIGHT: Metabolic Theory -->
  <rect x="378" y="60" width="326" height="340" fill="#0f2a1f" rx="12" stroke="#1e4a3a" stroke-width="1"/>
  <rect x="378" y="60" width="326" height="36" fill="#14532d"/>
  <rect x="378" y="78" width="326" height="18" fill="#14532d"/>
  <text x="541" y="84" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#86efac" font-weight="700">METABOLIC THEORY</text>
  <text x="541" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80">Warburg 1924 · Seyfried revival · 2010s–now</text>

  <!-- Mitochondria icon (right) -->
  <g transform="translate(485,128)">
    <ellipse cx="0" cy="0" rx="26" ry="16" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <path d="M -22,0 Q -10,-12 0,-2 Q 10,-12 22,0" stroke="#22c55e" stroke-width="1.5" fill="none"/>
    <!-- lightning bolt = damaged -->
    <line x1="-4" y1="-10" x2="-8" y2="0" stroke="#fbbf24" stroke-width="2"/>
    <line x1="-8" y1="0" x2="-2" y2="0" stroke="#fbbf24" stroke-width="2"/>
    <line x1="-2" y1="0" x2="-6" y2="10" stroke="#fbbf24" stroke-width="2"/>
    <text x="0" y="30" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">Mitochondria</text>
    <text x="0" y="42" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24">(damaged ⚡)</text>
  </g>

  <!-- Right theory bullets -->
  <text x="396" y="185" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">Claim: Cancer starts when the cell's</text>
  <text x="396" y="198" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">power plants (mitochondria) break down.</text>
  <text x="396" y="211" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8">DNA mutations are a downstream effect.</text>

  <text x="396" y="234" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Evidence supporting this:</text>
  <circle cx="405" cy="249" r="3" fill="#4ade80"/>
  <text x="414" y="253" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">All cancers share the same metabolism</text>
  <circle cx="405" cy="266" r="3" fill="#4ade80"/>
  <text x="414" y="270" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">Nuclear transfer experiments (see article 3)</text>
  <circle cx="405" cy="283" r="3" fill="#4ade80"/>
  <text x="414" y="287" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">Cancer cells all use aerobic glycolysis</text>
  <circle cx="405" cy="300" r="3" fill="#4ade80"/>
  <text x="414" y="304" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">Restricting glucose slows cancer growth</text>
  <circle cx="405" cy="317" r="3" fill="#4ade80"/>
  <text x="414" y="321" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">Damaged mitochondria → genomic instability</text>

  <rect x="386" y="333" width="310" height="22" fill="#14532d" rx="6"/>
  <text x="541" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#86efac">Focus: starve the metabolism that ALL</text>
  <text x="541" y="361" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#86efac">cancers share → one unified strategy</text>

</svg>
<figcaption style="font-size:0.8em;color:#64748b;text-align:center;margin-top:0.5em;">
  Two frameworks for understanding cancer. The metabolic theory does not deny that mutations exist — it argues they are caused by mitochondrial damage, not the other way around.
</figcaption>
</figure>
"""

CONTENT_1 = """
<p class="lead">For fifty years the dominant story about cancer has been simple: a gene breaks, a cell goes rogue. Pour billions into finding the broken gene, fix it, cure the disease. But after decades of searching, something unexpected has emerged — the story may be backward.</p>

<h2>The Theory Everyone Knows</h2>

<p>Ask almost any doctor what causes cancer and you will hear roughly the same answer: mutations in DNA. Certain genes — called tumor suppressors and oncogenes — normally keep cell division under tight control. When those genes mutate, the controls fail. Cells divide without stopping. That is cancer.</p>

<p>This explanation, called the Somatic Mutation Theory, has driven cancer research since the 1970s. It produced the Human Genome Project, the cancer genome atlas, and an enormous class of drugs called targeted therapies — drugs that hunt specific mutations in specific cancers.</p>

<p>The investment has been extraordinary. The logic seemed airtight. And yet — results have been frustrating.</p>

<h2>What the Genome Data Actually Showed</h2>

<p>When researchers sequenced cancer genomes in detail, they expected to find consistent mutations — the same broken gene driving the same cancer type. What they found instead was chaos.</p>

<p>"Every cancer cell within a single tumor has different mutations," explains Dr. Thomas Seyfried of Boston College, who has spent three decades studying cancer metabolism. "You have thousands of different mutations. There's no consistent genetic signature. There are some cancers that have very few mutations — pediatric medulloblastoma, for example — and yet they're just as aggressive and deadly as cancers with thousands of mutations."</p>

""" + SVG_1 + """

<p>This is a serious problem for the mutation theory. If cancer is caused by specific broken genes, why doesn't every cancer of the same type have the same broken genes? Why do some deadly cancers have almost no mutations at all?</p>

<p>Travis Christofferson, author of <em>Tripping Over the Truth</em>, described the experience of cancer genome researchers as they confronted this: "They expected to find maybe a handful of driver mutations common across cancer types. Instead they found tens of thousands of mutations, most of them different in every patient, every tumor, every cell within the tumor."</p>

<h2>The Deeper Problem: Mutations Follow Damage</h2>

<p>Here is what makes the metabolic theory compelling to a growing number of researchers: when mitochondria — the cell's energy generators — are damaged, the nucleus becomes unstable. Chromosomes break. DNA copying becomes error-prone. Mutations accumulate.</p>

<p>In this view, mutations are not the cause of cancer. They are a symptom of something happening earlier, in the cell's energy system.</p>

<p>Seyfried frames it this way: "The mitochondria are controlling the genome. When the mitochondria are damaged, the genome becomes unstable and you get all of these downstream mutations. These mutations are a downstream effect of the primary disturbance in energy metabolism."</p>

<p>This is the metabolic theory of cancer in its simplest form: cancer is a disease of energy metabolism. The cell's power plants break down. The cell reverts to an ancient, inefficient backup energy system. And the resulting instability — in chemistry, in signaling, in gene expression — cascades into the uncontrolled growth we call cancer.</p>

<h2>Why This Matters for Treatment</h2>

<p>The two theories lead to very different strategies.</p>

<p>If cancer is driven by specific mutations, you need specific drugs for each mutation. Since mutations differ in every patient, every tumor, every cell, you end up playing a kind of genetic whack-a-mole — developing targeted therapies against thousands of different variants. This is expensive, often toxic, and frequently temporary (tumors evolve resistance).</p>

<p>If cancer is driven by a universal metabolic dysfunction — specifically, a dependence on glucose and glutamine as fuel — then every cancer shares the same weakness. You do not need to chase thousands of mutations. You target the metabolism that all cancers require to survive.</p>

<p>The next three articles explore the specific evidence behind this idea: what happens inside cancer cells, what a famous set of experiments proved about where cancer control actually lives, and what the two-fuel system means for new treatment approaches.</p>
"""

ARTICLE_1 = {
    "title": "Cancer Is Not What You Think: The Genetic Theory Has a Problem",
    "slug": "cancer-genetic-theory-problem",
    "summary": (
        "For fifty years we have blamed cancer on broken genes. But the genome data "
        "revealed chaos — thousands of different mutations in every tumor, no consistent "
        "pattern. A growing body of research points to something earlier and more fundamental."
    ),
    "reading_time": "8 min read",
    "content": CONTENT_1,
}

# ─────────────────────────────────────────────────────────────────────────────
# ARTICLE 2: The Warburg Effect
# ─────────────────────────────────────────────────────────────────────────────

SVG_2 = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 460" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Side-by-side comparison of how normal cells and cancer cells make energy">
  <defs>
    <marker id="arr2" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#475569"/>
    </marker>
    <marker id="arr2g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#22c55e"/>
    </marker>
    <marker id="arr2r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/>
    </marker>
  </defs>

  <rect width="720" height="460" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">How Cells Make Energy: Normal vs. Cancer</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#475569">The Warburg Effect — discovered 1924, rediscovered by PET scans</text>

  <!-- Divider -->
  <line x1="360" y1="58" x2="360" y2="445" stroke="#1e293b" stroke-width="1.5"/>

  <!-- ─── LEFT SIDE: Normal Cell ─── -->
  <text x="179" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#93c5fd" font-weight="700">NORMAL CELL</text>

  <!-- Glucose input -->
  <rect x="130" y="84" width="98" height="26" fill="#1d3557" rx="6"/>
  <text x="179" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#93c5fd">🍬 Glucose</text>

  <!-- Arrow down -->
  <line x1="179" y1="110" x2="179" y2="132" stroke="#475569" stroke-width="1.5" marker-end="url(#arr2)"/>

  <!-- Pyruvate -->
  <rect x="125" y="132" width="108" height="22" fill="#1e293b" rx="5"/>
  <text x="179" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">→ Pyruvate (2 ATP)</text>

  <!-- Arrow to mitochondria -->
  <line x1="179" y1="154" x2="179" y2="184" stroke="#475569" stroke-width="1.5" marker-end="url(#arr2)"/>
  <text x="195" y="172" font-family="system-ui,sans-serif" font-size="9" fill="#475569">enters</text>

  <!-- Mitochondria box -->
  <rect x="60" y="184" width="238" height="110" fill="#0f2a1f" rx="10" stroke="#22c55e" stroke-width="1.5"/>
  <text x="179" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#86efac" font-weight="700">⚡ Mitochondria</text>
  <text x="179" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80">Electron Transport Chain (ETC)</text>
  <!-- O2 in -->
  <text x="80" y="240" font-family="system-ui,sans-serif" font-size="10" fill="#60a5fa">O₂ in</text>
  <text x="80" y="255" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(oxygen)</text>
  <!-- ATP produced -->
  <rect x="138" y="243" width="82" height="32" fill="#14532d" rx="6"/>
  <text x="179" y="259" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#4ade80" font-weight="700">36–38 ATP</text>
  <text x="179" y="271" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">energy units</text>
  <!-- CO2 out -->
  <text x="240" y="240" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">CO₂ out</text>
  <text x="240" y="255" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(exhaled)</text>

  <!-- Label below -->
  <text x="179" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Efficient. Clean. Requires oxygen.</text>

  <!-- Efficiency bar normal -->
  <rect x="80" y="320" width="200" height="14" fill="#1e293b" rx="4"/>
  <rect x="80" y="320" width="190" height="14" fill="#22c55e" rx="4"/>
  <text x="179" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fff">95% efficient</text>

  <!-- Normal summary -->
  <rect x="60" y="344" width="238" height="50" fill="#0f172a" rx="8"/>
  <text x="179" y="362" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">Normal cells burn glucose completely</text>
  <text x="179" y="375" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">through mitochondria. They can also</text>
  <text x="179" y="388" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">switch to fat or ketones if needed.</text>

  <!-- ─── RIGHT SIDE: Cancer Cell ─── -->
  <text x="541" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#f87171" font-weight="700">CANCER CELL</text>

  <!-- Glucose input (hungry) -->
  <rect x="452" y="84" width="178" height="26" fill="#3b0f0f" rx="6"/>
  <text x="541" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#f87171">🍬🍬🍬 Glucose (hungry!)</text>

  <!-- Arrow down -->
  <line x1="541" y1="110" x2="541" y2="132" stroke="#475569" stroke-width="1.5" marker-end="url(#arr2)"/>

  <!-- Pyruvate -->
  <rect x="487" y="132" width="108" height="22" fill="#1e293b" rx="5"/>
  <text x="541" y="147" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">→ Pyruvate (2 ATP)</text>

  <!-- Arrow bypasses mitochondria -->
  <line x1="541" y1="154" x2="541" y2="172" stroke="#f87171" stroke-width="1.5"/>
  <!-- X over the path to mitochondria -->
  <rect x="510" y="172" width="62" height="20" fill="#3b0f0f" rx="4"/>
  <text x="541" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">BYPASS ✗</text>

  <!-- Broken mitochondria box -->
  <rect x="422" y="200" width="120" height="60" fill="#1a0f0f" rx="8" stroke="#f87171" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="482" y="222" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">Mitochondria</text>
  <text x="482" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">💀 Damaged</text>
  <text x="482" y="250" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#6b2121">ETC broken</text>

  <!-- Lactic acid output -->
  <rect x="564" y="192" width="138" height="52" fill="#3b1f00" rx="8"/>
  <text x="633" y="211" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#fbbf24" font-weight="700">Lactic Acid</text>
  <text x="633" y="225" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f59e0b">excreted as waste</text>
  <text x="633" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#d97706">(even with O₂ present)</text>

  <!-- Only 2 ATP box -->
  <rect x="500" y="264" width="82" height="32" fill="#3b0f0f" rx="6"/>
  <text x="541" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#f87171" font-weight="700">2 ATP</text>
  <text x="541" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">energy units</text>

  <!-- Efficiency bar cancer -->
  <rect x="422" y="308" width="238" height="14" fill="#1e293b" rx="4"/>
  <rect x="422" y="308" width="14" height="14" fill="#f87171" rx="4"/>
  <text x="541" y="319" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">~5% efficient (18× less ATP)</text>

  <!-- Key insight box -->
  <rect x="422" y="332" width="238" height="62" fill="#1a0a0a" rx="8" stroke="#f59e0b" stroke-width="1"/>
  <text x="541" y="350" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24" font-weight="700">The Warburg Effect:</text>
  <text x="541" y="364" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f59e0b">Cancer cells ferment glucose into</text>
  <text x="541" y="378" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f59e0b">lactic acid — even when oxygen</text>
  <text x="541" y="392" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f59e0b">is available. This is the signature.</text>

  <!-- PET scan note at bottom -->
  <rect x="30" y="406" width="660" height="30" fill="#1e293b" rx="8"/>
  <text x="360" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">PET scans detect cancer by injecting radioactive glucose — tumors light up because they consume far more glucose than normal tissue</text>
</svg>
<figcaption style="font-size:0.8em;color:#64748b;text-align:center;margin-top:0.5em;">
  Normal cells extract 36–38 ATP from one glucose molecule via mitochondria. Cancer cells skip the mitochondria and extract only 2 ATP — then dump lactic acid as waste. To compensate, they consume vastly more glucose.
</figcaption>
</figure>
"""

CONTENT_2 = """
<p class="lead">In 1924, a German biochemist named Otto Warburg made an observation that should have changed everything. Cancer cells, he found, make energy in a strikingly inefficient way — even when oxygen is freely available. For decades, this discovery was sidelined. PET scans brought it back.</p>

<h2>How Normal Cells Make Energy</h2>

<p>Every cell in your body needs energy to survive and do its job. That energy comes in the form of a molecule called ATP — adenosine triphosphate. Think of ATP as the universal currency of cellular work: muscles use it to contract, neurons use it to fire, every cell uses it to pump ions and repair itself.</p>

<p>Normal cells are extraordinarily efficient at making ATP. Here is how they do it:</p>

<ol>
  <li><strong>Glucose enters the cell</strong> and is broken down in the cytoplasm (the cell's liquid interior) into a molecule called pyruvate. This step yields 2 ATP.</li>
  <li><strong>Pyruvate enters the mitochondria</strong> — the cell's power plants. There, through a complex process called the Electron Transport Chain (ETC), it is fully combusted using oxygen.</li>
  <li><strong>This produces 36–38 ATP</strong> per glucose molecule, plus carbon dioxide and water as waste products.</li>
</ol>

<p>This process is called oxidative phosphorylation. It requires oxygen, uses mitochondria, and is about 95% efficient at extracting energy from glucose. When oxygen is scarce — during intense exercise, for example — cells can temporarily fall back on the 2-ATP fermentation pathway. But they return to oxidative phosphorylation as soon as oxygen is available again.</p>

<h2>What Warburg Discovered</h2>

<p>In 1924, Otto Warburg measured the metabolism of cancer tissue and normal tissue side by side. His finding was startling: cancer cells were fermenting glucose into lactic acid — even in the presence of abundant oxygen. They were ignoring the mitochondria and running on the backup pathway, all the time.</p>

""" + SVG_2 + """

<p>This became known as the Warburg Effect, or <em>aerobic glycolysis</em>: aerobic because oxygen is present, glycolysis because the cells are running on the inefficient 2-step glucose breakdown rather than the full mitochondrial combustion.</p>

<p>It is extraordinarily wasteful. Cancer cells get 18 times less energy per glucose molecule than a normal cell would. To compensate, they consume glucose at a frantic rate — sometimes 200 times more than the surrounding healthy tissue.</p>

<h2>This Is Why PET Scans Work</h2>

<p>This fact underlies one of the most widely used cancer detection tools in medicine: the PET scan. Before a PET scan, you are injected with radioactive glucose. The scanner then detects where in the body the radioactive glucose accumulates. Tumors light up because they are consuming vastly more glucose than the normal tissue around them.</p>

<p>PET scanning works because of the Warburg Effect. Every oncologist who orders a PET scan is, in effect, using Warburg's 100-year-old discovery to find cancer. And yet for decades the mainstream interpretation was that this metabolic shift was merely a side effect of cancer — a consequence of genetic mutations that happened to break the mitochondria along the way.</p>

<h2>Why Did Warburg Get Ignored?</h2>

<p>Warburg's observation was sidelined after the discovery of DNA's structure in 1953 and the rise of molecular biology. If DNA contained the blueprint of life, and if mutations in DNA could change cell behavior, then cancer must be about broken DNA. The metabolic observation looked like a downstream effect — not a root cause.</p>

<p>Warburg himself disagreed until he died in 1970. "The prime cause of cancer is the replacement of the respiration of oxygen in normal body cells by a fermentation of sugar," he wrote. He believed the mitochondrial damage was primary, not secondary.</p>

<p>What has changed in the last two decades is the ability to study mitochondria in detail — and the accumulating evidence that Warburg was right about the causal sequence. When researchers damage mitochondria deliberately in normal cells, those cells begin exhibiting aerobic glycolysis. The genome destabilizes. Mutations appear. The cell starts to look and behave like a cancer cell.</p>

<h2>The Energy Crisis Creates the Chaos</h2>

<p>Dr. Thomas Seyfried of Boston College argues that the sequence matters: "The mitochondria are damaged first. Once the mitochondria are damaged and can no longer do oxidative phosphorylation, the cell reverts to fermentation. And once it reverts to fermentation, you get reactive oxygen species flooding the nucleus, breaking DNA, causing the mutations that everyone has been chasing."</p>

<p>In this view, the genetic chaos seen in cancer — the thousands of different mutations in every tumor — is a downstream consequence of the energy crisis, not its origin. The cancer cell is not a rogue genetically mutant cell. It is a cell that lost its power plants and reverted to the most ancient energy system life has — fermentation — in a desperate attempt to survive.</p>

<p>The next article looks at the most direct experimental evidence for this: what happens when you take the nucleus out of a cancer cell and put it into a healthy cell, and vice versa.</p>
"""

ARTICLE_2 = {
    "title": "The Warburg Effect: Why Cancer Cells Abandon Normal Energy Production",
    "slug": "warburg-effect-cancer-energy",
    "summary": (
        "Normal cells extract 36 ATP from one glucose molecule. Cancer cells extract 2 — "
        "then dump lactic acid as waste, even when oxygen is available. Otto Warburg "
        "discovered this in 1924. PET scans use it every day. It may explain everything."
    ),
    "reading_time": "9 min read",
    "content": CONTENT_2,
}

# ─────────────────────────────────────────────────────────────────────────────
# ARTICLE 3: Nuclear Transfer Experiments
# ─────────────────────────────────────────────────────────────────────────────

SVG_3 = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 490" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Four-panel diagram of nuclear cytoplasm transfer experiments in cancer research">
  <defs>
    <marker id="a3n" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#22c55e"/>
    </marker>
    <marker id="a3r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/>
    </marker>
    <marker id="a3b" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#64748b"/>
    </marker>
  </defs>

  <rect width="720" height="490" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">The Nuclear Transfer Experiments</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#475569">What happens when you move the nucleus between normal and cancer cells?</text>

  <!-- Legend -->
  <circle cx="60" cy="64" r="7" fill="#1d4ed8" opacity="0.7"/>
  <text x="73" y="68" font-family="system-ui,sans-serif" font-size="9.5" fill="#93c5fd">= Nucleus (DNA)</text>
  <ellipse cx="168" cy="64" rx="12" ry="7" fill="#14532d" stroke="#22c55e" stroke-width="1"/>
  <text x="186" y="68" font-family="system-ui,sans-serif" font-size="9.5" fill="#86efac">= Mitochondria (cytoplasm)</text>
  <circle cx="310" cy="64" r="7" fill="#dc2626" opacity="0.7"/>
  <text x="323" y="68" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171">= Tumor nucleus</text>
  <ellipse cx="430" cy="64" rx="12" ry="7" fill="#3b0f0f" stroke="#f87171" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="448" y="68" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171">= Damaged mitochondria</text>

  <!-- ─── PANEL A (top-left) ─── -->
  <rect x="16" y="78" width="334" height="190" fill="#0f172a" rx="10" stroke="#1d4ed8" stroke-width="1"/>
  <rect x="16" y="78" width="334" height="28" fill="#1d3557" rx="8"/>
  <rect x="16" y="96" width="334" height="10" fill="#1d3557"/>
  <text x="183" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#93c5fd" font-weight="700">Experiment A</text>

  <!-- Tumor nucleus icon -->
  <circle cx="90" cy="152" r="28" fill="#1a0a0a" stroke="#dc2626" stroke-width="2"/>
  <circle cx="90" cy="152" r="16" fill="#dc2626" opacity="0.4"/>
  <text x="90" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171" font-weight="700">TUMOR</text>
  <text x="90" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">NUCLEUS</text>
  <text x="90" y="192" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171">from cancer cell</text>

  <!-- Plus sign -->
  <text x="145" y="157" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" fill="#475569">+</text>

  <!-- Normal cytoplasm/mitochondria -->
  <ellipse cx="210" cy="152" rx="32" ry="22" fill="#0f2a1f" stroke="#22c55e" stroke-width="2"/>
  <ellipse cx="198" cy="148" rx="9" ry="6" fill="#14532d" stroke="#22c55e" stroke-width="1"/>
  <ellipse cx="220" cy="156" rx="9" ry="6" fill="#14532d" stroke="#22c55e" stroke-width="1"/>
  <text x="210" y="192" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#86efac">NORMAL cytoplasm</text>
  <text x="210" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#86efac">(healthy mitochondria)</text>

  <!-- Arrow -->
  <line x1="260" y1="152" x2="288" y2="152" stroke="#22c55e" stroke-width="1.5" marker-end="url(#a3n)"/>

  <!-- Result: Normal growth -->
  <rect x="295" y="128" width="44" height="44" fill="#14532d" rx="8"/>
  <text x="317" y="153" text-anchor="middle" font-family="system-ui,sans-serif" font-size="20">✓</text>
  <text x="317" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">NORMAL</text>
  <text x="317" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">growth</text>

  <!-- Panel A finding -->
  <rect x="26" y="218" width="314" height="36" fill="#0a1a0a" rx="6"/>
  <text x="183" y="233" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">Finding: Tumor nucleus placed in healthy cytoplasm</text>
  <text x="183" y="247" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac">→ Cell grows normally. Tumor nucleus was SUPPRESSED.</text>

  <!-- ─── PANEL B (top-right) — THE KEY EXPERIMENT ─── -->
  <rect x="370" y="78" width="334" height="190" fill="#1a0a0a" rx="10" stroke="#f87171" stroke-width="2"/>
  <rect x="370" y="78" width="334" height="28" fill="#3b0f0f" rx="8"/>
  <rect x="370" y="96" width="334" height="10" fill="#3b0f0f"/>
  <text x="537" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#f87171" font-weight="700">Experiment B  ← KEY FINDING</text>

  <!-- Normal nucleus -->
  <circle cx="444" cy="152" r="28" fill="#0f172a" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="444" cy="152" r="16" fill="#1d4ed8" opacity="0.3"/>
  <text x="444" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#93c5fd" font-weight="700">NORMAL</text>
  <text x="444" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#93c5fd">NUCLEUS</text>
  <text x="444" y="192" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#93c5fd">from normal cell</text>

  <!-- Plus -->
  <text x="499" y="157" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" fill="#475569">+</text>

  <!-- Tumor cytoplasm -->
  <ellipse cx="562" cy="152" rx="32" ry="22" fill="#1a0a0a" stroke="#f87171" stroke-width="2" stroke-dasharray="4,3"/>
  <ellipse cx="550" cy="148" rx="9" ry="6" fill="#3b0f0f" stroke="#f87171" stroke-width="1"/>
  <ellipse cx="572" cy="156" rx="9" ry="6" fill="#3b0f0f" stroke="#f87171" stroke-width="1"/>
  <text x="562" y="192" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171">TUMOR cytoplasm</text>
  <text x="562" y="204" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171">(damaged mitochondria)</text>

  <!-- Arrow -->
  <line x1="612" y1="152" x2="640" y2="152" stroke="#f87171" stroke-width="1.5" marker-end="url(#a3r)"/>

  <!-- Result: Cancer! -->
  <rect x="649" y="128" width="44" height="44" fill="#3b0f0f" rx="8"/>
  <text x="671" y="153" text-anchor="middle" font-family="system-ui,sans-serif" font-size="20">✗</text>
  <text x="671" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">CANCER</text>
  <text x="671" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">behavior</text>

  <!-- Panel B finding -->
  <rect x="380" y="218" width="314" height="36" fill="#1a0808" rx="6"/>
  <text x="537" y="233" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171" font-weight="700">Finding: Normal nucleus placed in tumor cytoplasm</text>
  <text x="537" y="247" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5">→ Cell becomes cancerous. The cytoplasm DRIVES cancer.</text>

  <!-- ─── CONCLUSION BOX ─── -->
  <rect x="16" y="282" width="688" height="56" fill="#1a1a0a" rx="10" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="360" y="302" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fbbf24" font-weight="700">What these experiments prove:</text>
  <text x="360" y="320" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#f59e0b">Cancer is controlled by the CYTOPLASM (where mitochondria live) — not by the DNA in the nucleus.</text>
  <text x="360" y="334" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#f59e0b">A normal nucleus placed in cancerous cytoplasm becomes cancerous. Fixing the DNA alone cannot cure cancer if the mitochondria remain broken.</text>

  <!-- ─── PANEL C and D — Control experiments ─── -->
  <!-- Panel C -->
  <rect x="16" y="350" width="334" height="120" fill="#0f172a" rx="10" stroke="#475569" stroke-width="1"/>
  <text x="183" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8" font-weight="700">Experiment C (Control)</text>
  <text x="183" y="388" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">Normal nucleus + Normal cytoplasm</text>
  <text x="183" y="408" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22">✓</text>
  <text x="183" y="426" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">Normal cell growth — as expected</text>
  <text x="183" y="440" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(confirms the transfer technique works)</text>
  <text x="183" y="455" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(healthy cytoplasm protects against tumor nucleus)</text>

  <!-- Panel D -->
  <rect x="370" y="350" width="334" height="120" fill="#1a0a0a" rx="10" stroke="#475569" stroke-width="1"/>
  <text x="537" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#94a3b8" font-weight="700">Experiment D (Control)</text>
  <text x="537" y="388" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">Tumor nucleus + Tumor cytoplasm</text>
  <text x="537" y="408" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22">✗</text>
  <text x="537" y="426" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">Cancer behavior — as expected</text>
  <text x="537" y="440" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(confirms cancer cells remain cancerous without intervention)</text>
  <text x="537" y="455" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">(tumor cytoplasm overrides even a good nucleus)</text>
</svg>
<figcaption style="font-size:0.8em;color:#64748b;text-align:center;margin-top:0.5em;">
  The key experiment is B: when researchers placed a <em>normal</em> nucleus into <em>tumor</em> cytoplasm, the cell behaved like a cancer cell. The DNA was fine — but the cytoplasm (with its damaged mitochondria) turned it cancerous anyway.
</figcaption>
</figure>
"""

CONTENT_3 = """
<p class="lead">If cancer is caused by mutations in DNA, then the nucleus — which contains the DNA — should be the seat of the disease. Move the tumor nucleus into a healthy cell, and you should get cancer. Move a healthy nucleus into a cancer cell, and it should recover. A series of remarkable experiments tested exactly this. The results were the opposite of what the genetic theory predicted.</p>

<h2>The Logic of the Experiment</h2>

<p>Scientists have developed techniques to transfer the nucleus of one cell into the cytoplasm of another — a process called somatic cell nuclear transfer. The same technique was used to clone Dolly the sheep.</p>

<p>The question for cancer research was straightforward: where does cancer control live? Is it in the nucleus, where the DNA sits? Or is it in the cytoplasm — the rest of the cell, where the mitochondria are?</p>

<p>Researchers designed four combinations:</p>
<ul>
  <li>Tumor nucleus + Normal cytoplasm → What happens?</li>
  <li>Normal nucleus + Tumor cytoplasm → What happens?</li>
  <li>Normal nucleus + Normal cytoplasm → (Control)</li>
  <li>Tumor nucleus + Tumor cytoplasm → (Control)</li>
</ul>

<p>If the genetic theory is correct, the nucleus controls cancer, so:</p>
<ul>
  <li>Tumor nucleus + Normal cytoplasm → should produce cancer</li>
  <li>Normal nucleus + Tumor cytoplasm → should produce normal cells</li>
</ul>

<p>Here is what they actually found.</p>

""" + SVG_3 + """

<h2>The Result That Changed Everything</h2>

<p>The key finding — Experiment B — was that a normal nucleus placed inside tumor cytoplasm caused the resulting cell to behave like a cancer cell. The DNA was completely normal. There were no mutations in it. But the cytoplasm — with its damaged mitochondria — turned normal DNA cancerous.</p>

<p>And in Experiment A, the opposite: a tumor nucleus placed inside healthy cytoplasm was suppressed. The cell grew normally. The same DNA that produces cancer in one environment was completely controlled in another.</p>

<p>Dr. Thomas Seyfried, who has reviewed this literature extensively, summarizes the conclusion: "The tumor nucleus was suppressed in its abnormal growth when placed in a normal cytoplasm. And the normal nucleus was transformed when placed in tumor cytoplasm. This tells you in the clearest possible way: it is the cytoplasm that controls cancer — not the nucleus. And in the cytoplasm are the mitochondria."</p>

<h2>What Lives in the Cytoplasm?</h2>

<p>The cytoplasm is everything in the cell outside the nucleus — the liquid interior, the structural scaffolding, and critically, the mitochondria. Mitochondria are not in the nucleus. They float in the cytoplasm, and they control the energy supply of the cell.</p>

<p>When mitochondria are damaged, the cytoplasm sends distress signals. These signals reach the nucleus via epigenetic pathways — chemical tags on DNA that switch genes on or off without changing the DNA sequence itself. Damaged mitochondria can reprogram gene expression, turning off tumor suppressor genes and turning on growth genes.</p>

<p>This is why the nuclear transfer experiment shows what it shows: a normal nucleus in a damaged cytoplasm gets reprogrammed by the damaged signals emanating from broken mitochondria. The DNA sequence is fine. The instructions being sent to it are not.</p>

<h2>The Implication for Treatment</h2>

<p>This finding has a direct and unsettling implication for the strategy of targeting cancer mutations with drugs.</p>

<p>If the mutations are downstream of cytoplasmic damage — if they are caused by damaged mitochondria sending bad signals to the nucleus — then correcting specific mutations may not fix anything. The underlying cause is still there, still generating new mutations, still sending corrupted signals. You correct one mutation, the cell generates another.</p>

<p>Travis Christofferson describes it this way: "The mutations are downstream. They're a symptom, not the cause. If your car engine is on fire and you replace the upholstery, the car is still going to burn. Targeting individual mutations while leaving the mitochondrial damage intact is working on the wrong layer."</p>

<h2>The Experiments Were Done Decades Ago</h2>

<p>What makes this evidence particularly striking is that some of these experiments were done decades ago — and their implications were not incorporated into the dominant framework of cancer research.</p>

<p>Israel and Schaeffer published nuclear transfer results in cancer cell lines in 1987. Shay and Werbin conducted similar work in the 1990s. Seyfried and colleagues have reviewed and extended this literature. The results have been consistent: cytoplasm drives cancer, not the nucleus.</p>

<p>The reason this body of work did not redirect cancer research is a matter of scientific sociology as much as science. The Human Genome Project was attracting enormous funding and excitement. The story of broken genes was compelling and legible. The cytoplasm was harder to tell a story about.</p>

<p>That story is now being told in greater detail — and the next article explores what it means for how cancer is actually treated.</p>
"""

ARTICLE_3 = {
    "title": "The Nuclear Transfer Experiments: The Proof Was in the Cytoplasm",
    "slug": "nuclear-transfer-experiments-cytoplasm",
    "summary": (
        "What happens when you move a tumor nucleus into a healthy cell — and a healthy nucleus "
        "into cancer cytoplasm? Researchers did exactly this. The results upended the genetic "
        "theory: cancer is controlled by the cytoplasm (and its mitochondria), not the DNA."
    ),
    "reading_time": "9 min read",
    "content": CONTENT_3,
}

# ─────────────────────────────────────────────────────────────────────────────
# ARTICLE 4: Glucose and Glutamine — The Two Fuels
# ─────────────────────────────────────────────────────────────────────────────

SVG_4 = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diagram showing cancer's two fuel sources and the press-pulse strategy to cut them off">
  <defs>
    <marker id="a4o" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#f59e0b"/>
    </marker>
    <marker id="a4b" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#60a5fa"/>
    </marker>
    <marker id="a4g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#4ade80"/>
    </marker>
  </defs>

  <rect width="720" height="470" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Cancer's Two Fuels — and How to Cut Them Off</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#475569">The Press-Pulse Strategy: Dr. Thomas Seyfried, Boston College</text>

  <!-- ─── TOP SECTION: Two fuel tanks ─── -->
  <!-- Glucose Tank -->
  <rect x="50" y="64" width="240" height="130" fill="#1a0f00" rx="12" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="50" y="64" width="240" height="32" fill="#7c3a00" rx="10"/>
  <rect x="50" y="82" width="240" height="14" fill="#7c3a00"/>
  <text x="170" y="86" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fbbf24" font-weight="700">⛽ FUEL #1: GLUCOSE</text>

  <text x="170" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#f59e0b">From: sugar, bread, pasta, starchy foods</text>
  <text x="170" y="130" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#f59e0b">Used by: ALL cancer cells, always</text>
  <text x="170" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#d97706">Cancer cannot survive without glucose.</text>
  <text x="170" y="163" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#d97706">Normal cells can switch to ketones.</text>
  <text x="170" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#d97706">Cancer cells cannot make this switch.</text>

  <!-- Glutamine Tank -->
  <rect x="430" y="64" width="240" height="130" fill="#0f0f2a" rx="12" stroke="#a78bfa" stroke-width="1.5"/>
  <rect x="430" y="64" width="240" height="32" fill="#2d1f6e" rx="10"/>
  <rect x="430" y="82" width="240" height="14" fill="#2d1f6e"/>
  <text x="550" y="86" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#c4b5fd" font-weight="700">⛽ FUEL #2: GLUTAMINE</text>

  <text x="550" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#a78bfa">From: protein breakdown, muscle tissue</text>
  <text x="550" y="130" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#a78bfa">Used by: cancer when glucose is restricted</text>
  <text x="550" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#7c3aed">Second backup fuel for cancer cells.</text>
  <text x="550" y="163" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#7c3aed">Used for building cancer cell parts.</text>
  <text x="550" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#7c3aed">Inhibiting it causes cancer cell death.</text>

  <!-- Arrow from both tanks to cancer cell -->
  <line x1="170" y1="194" x2="320" y2="240" stroke="#f59e0b" stroke-width="2" marker-end="url(#a4o)"/>
  <line x1="550" y1="194" x2="400" y2="240" stroke="#a78bfa" stroke-width="2"/>
  <path d="M400,240 L330,240" stroke="#a78bfa" stroke-width="2" marker-end="url(#a4b)"/>

  <!-- Cancer cell center -->
  <circle cx="360" cy="272" r="46" fill="#1a0808" stroke="#f87171" stroke-width="2"/>
  <text x="360" y="264" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#f87171" font-weight="700">☠ CANCER</text>
  <text x="360" y="278" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">CELL</text>
  <text x="360" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Needs both fuels</text>
  <text x="360" y="304" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">to survive &amp; grow</text>

  <!-- ─── BOTTOM SECTION: Press-Pulse ─── -->
  <text x="360" y="340" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#f1f5f9" font-weight="700">The Press-Pulse Strategy</text>

  <!-- PRESS box (left) -->
  <rect x="30" y="354" width="296" height="98" fill="#0a1a0a" rx="10" stroke="#22c55e" stroke-width="1.5"/>
  <rect x="30" y="354" width="296" height="28" fill="#14532d" rx="8"/>
  <rect x="30" y="370" width="296" height="12" fill="#14532d"/>
  <text x="178" y="371" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11.5" fill="#86efac" font-weight="700">THE PRESS (sustained)</text>
  <text x="178" y="392" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">Ketogenic diet + intermittent fasting</text>
  <text x="178" y="406" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">→ Blood glucose drops ↓</text>
  <text x="178" y="420" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">→ Ketones rise ↑ (normal cells thrive)</text>
  <text x="178" y="434" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">→ Cancer cells starved of glucose</text>

  <!-- PULSE box (right) -->
  <rect x="394" y="354" width="296" height="98" fill="#0f0a1a" rx="10" stroke="#a78bfa" stroke-width="1.5"/>
  <rect x="394" y="354" width="296" height="28" fill="#2d1f6e" rx="8"/>
  <rect x="394" y="370" width="296" height="12" fill="#2d1f6e"/>
  <text x="542" y="371" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11.5" fill="#c4b5fd" font-weight="700">THE PULSE (targeted)</text>
  <text x="542" y="392" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#a78bfa">DON (6-diazo-5-oxo-l-norleucine)</text>
  <text x="542" y="406" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#a78bfa">→ Inhibits glutamine use</text>
  <text x="542" y="420" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#a78bfa">→ Cancer cannot switch fuels</text>
  <text x="542" y="434" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#a78bfa">→ Cancer cell death (apoptosis)</text>

  <!-- Key insight strip -->
  <rect x="30" y="460" width="660" height="0" fill="none"/>
</svg>
<figcaption style="font-size:0.8em;color:#64748b;text-align:center;margin-top:0.5em;">
  Cancer depends on exactly two fuels: glucose and glutamine. The press-pulse strategy restricts glucose via diet (press) and blocks glutamine via targeted drugs (pulse). Normal cells, which can burn fat and ketones, survive. Cancer cells, which cannot, die.
</figcaption>
</figure>
"""

CONTENT_4 = """
<p class="lead">"Is there any kind of cancer out there anywhere that can survive without glucose and glutamine? We haven't found one." That statement, from Dr. Thomas Seyfried of Boston College, points to something remarkable: despite the extraordinary genetic diversity of cancer — thousands of different mutations, hundreds of different tumor types — every cancer shares the same two fuel dependencies.</p>

<h2>Why Two Fuels?</h2>

<p>Cancer cells, as we explored in the previous article, cannot use the normal mitochondrial energy pathway efficiently. They are stuck running on fermentation — the backup pathway that uses glucose but not oxygen. This is the Warburg Effect: aerobic glycolysis.</p>

<p>But cancer cells are not passive. They are under severe metabolic stress, growing faster than normal cells, and they need not just energy (ATP) but also the raw material to build new cancer cells — proteins, fats, nucleic acids for DNA. Glutamine, an amino acid, provides much of this building material. It feeds into several metabolic pathways that supply the carbon and nitrogen cancer cells need to grow.</p>

<p>So cancer requires:</p>
<ol>
  <li><strong>Glucose</strong> — for energy (ATP), even via the inefficient fermentation pathway</li>
  <li><strong>Glutamine</strong> — for biomass (building new cancer cell parts) and additional ATP</li>
</ol>

<p>Critically, normal healthy cells are metabolically flexible. They can burn fat. They can use ketones — the molecules produced by the liver when glucose is scarce. They are not dependent on glucose for survival. Cancer cells, with their broken mitochondria, have lost this flexibility. They need glucose. They cannot run on ketones effectively.</p>

""" + SVG_4 + """

<h2>The Press-Pulse Strategy</h2>

<p>Dr. Seyfried and colleagues developed a treatment framework called Press-Pulse specifically around this fuel dependency. The idea draws from an analogy in ecology: predators use sustained pressure (press) combined with sharp targeted attacks (pulse) to take down prey. The metabolic strategy works the same way.</p>

<h3>The Press: Restrict Glucose</h3>

<p>The sustained pressure is dietary: a strict ketogenic diet combined with intermittent fasting. When you dramatically reduce carbohydrates and eat in a controlled window, blood glucose levels fall. The liver begins producing ketones from fat. Normal cells thrive on ketones. Cancer cells cannot.</p>

<p>Studies in animals and early human trials have shown that caloric restriction and ketogenic diets can slow tumor growth, improve response to chemotherapy, and in some cases dramatically extend survival. The mechanism is straightforward: you are removing the primary fuel cancer depends on while leaving normal cells well-nourished on an alternative fuel.</p>

<p>Travis Christofferson describes the elegance of this: "The ketogenic diet is remarkably non-toxic. You are not poisoning cells. You are simply removing the fuel that cancer cells need and cannot replace, while giving normal cells an equally good or better alternative. That asymmetry is the entire therapy."</p>

<h3>The Pulse: Block Glutamine</h3>

<p>The targeted attack is pharmacological. When glucose is restricted, cancer cells ramp up their use of glutamine — their backup fuel. A drug called DON (6-diazo-5-oxo-l-norleucine) inhibits glutamine metabolism. With both pathways blocked simultaneously, cancer cells have nowhere to turn.</p>

<p>In animal studies, the press-pulse combination — ketogenic diet/fasting plus DON — has shown striking results, achieving complete remission in some aggressive cancer models. The key to the approach is timing: the dietary press creates metabolic vulnerability in the cancer cells, and the drug pulse exploits that vulnerability at its peak.</p>

<h2>Why Normal Cells Are Safe</h2>

<p>The elegance of targeting cancer metabolism is the selectivity it offers. Normal cells are metabolically flexible: they can burn glucose, fat, ketones, and can meet their glutamine needs from multiple sources. Cancer cells, stuck in a rigid fermentation-dependent state, cannot adapt the same way.</p>

<p>This is the opposite of conventional chemotherapy, which broadly poisons any rapidly-dividing cell. The metabolic approach says: exploit the specific metabolic vulnerability that cancer cells have and normal cells do not. The therapy is not easy — ketogenic diets are demanding, and DON has side effects that researchers are working to minimize. But the underlying strategy is targeting a universal cancer weakness rather than chasing individual mutations.</p>

<h2>Where the Research Stands</h2>

<p>The press-pulse strategy is still in clinical development. Dr. Seyfried and colleagues at Boston College are actively researching optimized protocols. Several clinical trials are examining ketogenic diets in combination with standard-of-care treatment for glioblastoma and other cancers. The DON drug was shelved decades ago due to gastrointestinal side effects; researchers are now developing modified versions designed to deliver DON specifically to tumor tissue, reducing systemic toxicity.</p>

<p>The metabolic theory of cancer does not argue that surgery, radiation, and chemotherapy should be abandoned. It argues that the metabolic framework offers a more coherent understanding of what cancer is — and that targeting metabolism can complement, or in some cases replace, therapies that have been limited by the complexity of genetic targets.</p>

<h2>What This Means for Prevention</h2>

<p>Perhaps the most immediately actionable implication of the metabolic theory is for prevention. If cancer cells depend on glucose and cannot survive on ketones, then chronically elevated blood sugar — from diets high in refined carbohydrates and sugar — creates the metabolic environment in which cancer thrives.</p>

<p>This connects the metabolic theory of cancer to the broader literature on insulin resistance, metabolic syndrome, and obesity as cancer risk factors. These are not separate phenomena. They are facets of the same metabolic dysfunction: chronically elevated glucose and insulin that feed exactly the fermentation-dependent energy system that cancer exploits.</p>

<p>Seyfried is direct about the implication: "If you want to prevent cancer, or slow its growth if you have it, you want low blood glucose. You want elevated ketones. You want a metabolism that keeps the fuel cancer depends on as scarce as possible." Diet is not a peripheral concern in this framework. It is the first line of metabolic defense.</p>
"""

ARTICLE_4 = {
    "title": "Glucose and Glutamine: The Two Fuels Every Cancer Depends On",
    "slug": "glucose-glutamine-cancer-fuels",
    "summary": (
        "No matter how genetically different cancers are, they all depend on exactly two fuels: "
        "glucose and glutamine. The press-pulse strategy exploits this universal dependency — "
        "restrict glucose via diet, block glutamine with targeted drugs. Cancer cells cannot adapt."
    ),
    "reading_time": "10 min read",
    "content": CONTENT_4,
}

# ─────────────────────────────────────────────────────────────────────────────

ALL_ARTICLES = [ARTICLE_1, ARTICLE_2, ARTICLE_3, ARTICLE_4]


def create_cancer_metabolic_articles(apps=None, schema_editor=None):
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

    for data in ALL_ARTICLES:
        ArticleModel.objects.update_or_create(
            slug=data["slug"],
            defaults={
                "pillar": pillar,
                "title": data["title"],
                "summary": data["summary"],
                "content": data["content"],
                "published": True,
            },
        )


def reverse_cancer_metabolic_articles(apps, schema_editor):
    ArticleModel = apps.get_model('topics', 'Article')
    PillarModel = apps.get_model('topics', 'Pillar')
    for data in ALL_ARTICLES:
        ArticleModel.objects.filter(slug=data["slug"]).delete()
    PillarModel.objects.filter(slug=PILLAR["slug"]).delete()


class Command(BaseCommand):
    help = "Load Cancer as Metabolic Disease articles into the Biology pillar"

    def add_arguments(self, parser):
        parser.add_argument("--publish", action="store_true", default=True)

    def handle(self, *args, **options):
        create_cancer_metabolic_articles()
        self.stdout.write(self.style.SUCCESS(
            f"Created {len(ALL_ARTICLES)} cancer metabolic articles under '{PILLAR['name']}' pillar."
        ))
