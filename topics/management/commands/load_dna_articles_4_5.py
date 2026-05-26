from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

# ── Article 4: Alleles and Mendel ─────────────────────────────────────────────

A4_CONTENT = """
<p class="lead">Before anyone knew what DNA was, Gregor Mendel — an Augustinian friar growing peas in a Brno monastery — deduced the fundamental rules of inheritance through nothing more than careful counting. His results, published in 1866 and ignored for thirty-four years, contain the entire logic of classical genetics. Understanding alleles and Mendel's laws is understanding why children resemble but do not replicate their parents.</p>

<h2>Alleles: alternate versions of a gene</h2>
<p>Every gene in the human genome exists at a specific location on a chromosome called a <strong>locus</strong>. Because humans are diploid — carrying two copies of each chromosome — every person carries two copies of each gene, one on each homologous chromosome. These two copies need not be identical: alternate versions of the same gene are called <strong>alleles</strong>. The two alleles a person carries at a given locus constitute their <strong>genotype</strong>. What those alleles actually produce — the observable characteristic — is the <strong>phenotype</strong>.</p>
<blockquote><p>"Gregor Mendel really launches the book and the modern history of genes. He's a fascinating character — he was the first person to see that heredity was discrete, that it came in units."</p><footer>— Siddhartha Mukherjee</footer></blockquote>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Dominant and recessive alleles: genotype and phenotype relationships">
  <rect width="720" height="360" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Alleles — Genotype vs Phenotype</text>
  <text x="360" y="46" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Dominant allele (B) masks recessive (b) when present · only bb shows recessive phenotype</text>
  <!-- Three genotype boxes -->
  <!-- BB -->
  <rect x="40" y="70" width="180" height="200" rx="12" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
  <text x="130" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#4ade80" font-weight="700">BB</text>
  <text x="130" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Homozygous dominant</text>
  <rect x="88" y="128" width="28" height="55" rx="5" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
  <text x="102" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">B</text>
  <rect x="124" y="128" width="28" height="55" rx="5" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
  <text x="138" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">B</text>
  <text x="130" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Two dominant alleles</text>
  <rect x="65" y="222" width="130" height="34" rx="8" fill="#052e16" stroke="#4ade80" stroke-width="1.2"/>
  <text x="130" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">DOMINANT phenotype</text>
  <!-- Bb -->
  <rect x="270" y="70" width="180" height="200" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="360" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#fbbf24" font-weight="700">Bb</text>
  <text x="360" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Heterozygous (carrier)</text>
  <rect x="318" y="128" width="28" height="55" rx="5" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
  <text x="332" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">B</text>
  <rect x="354" y="128" width="28" height="55" rx="5" fill="#1c1917" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="368" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">b</text>
  <text x="360" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">One of each — carries b</text>
  <text x="360" y="216" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">but b is silent</text>
  <rect x="295" y="222" width="130" height="34" rx="8" fill="#052e16" stroke="#4ade80" stroke-width="1.2"/>
  <text x="360" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">DOMINANT phenotype</text>
  <!-- bb -->
  <rect x="500" y="70" width="180" height="200" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="590" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#fca5a5" font-weight="700">bb</text>
  <text x="590" y="114" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Homozygous recessive</text>
  <rect x="548" y="128" width="28" height="55" rx="5" fill="#1c1917" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="562" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">b</text>
  <rect x="584" y="128" width="28" height="55" rx="5" fill="#1c1917" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="598" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">b</text>
  <text x="590" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Two recessive alleles</text>
  <text x="590" y="216" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">B not present to mask b</text>
  <rect x="525" y="222" width="130" height="34" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.2"/>
  <text x="590" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#ef4444" font-weight="700">RECESSIVE phenotype</text>
  <!-- Summary row -->
  <text x="130" y="295" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">e.g. Brown eyes (B dominant)</text>
  <text x="360" y="295" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">e.g. Brown eyes (carrier of blue)</text>
  <text x="590" y="295" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f472b6">e.g. Blue eyes (b recessive)</text>
  <text x="360" y="335" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Note: most traits involve multiple genes (polygenic) — eye colour is a simplified illustration</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Three possible genotypes at a two-allele locus: BB (homozygous dominant), Bb (heterozygous), and bb (homozygous recessive). The dominant allele B masks b in the Bb genotype — so both BB and Bb produce the dominant phenotype, but only bb reveals the recessive one.</figcaption>
</figure>

<h2>Mendel's pea experiments</h2>
<p>Mendel chose seven traits in pea plants that each existed in only two discrete forms: seed shape (round or wrinkled), seed colour (yellow or green), pod shape, pod colour, flower position, flower colour, and plant height. He cross-bred true-breeding plants with contrasting traits, counted the offspring across thousands of plants, and found a consistent pattern: in the first generation (F1) all offspring showed one version of the trait. In the second generation (F2), the hidden version reappeared in a ratio of approximately 3:1.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Mendel's pea cross experiment and Punnett square showing 3:1 ratio">
  <rect width="720" height="400" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Mendel's Monohybrid Cross — The 3:1 Ratio</text>
  <defs>
    <marker id="arM" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker>
  </defs>
  <!-- Parents -->
  <text x="130" y="62" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b" font-weight="600">P generation (parents)</text>
  <rect x="60" y="72" width="80" height="60" rx="8" fill="#052e16" stroke="#4ade80" stroke-width="2"/>
  <text x="100" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#4ade80" font-weight="700">BB</text>
  <text x="100" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Round seed</text>
  <text x="130" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">×</text>
  <rect x="140" y="72" width="80" height="60" rx="8" fill="#1c1917" stroke="#94a3b8" stroke-width="2"/>
  <text x="180" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#94a3b8" font-weight="700">bb</text>
  <text x="180" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Wrinkled seed</text>
  <!-- F1 arrow -->
  <line x1="130" y1="136" x2="130" y2="155" stroke="#475569" stroke-width="2" marker-end="url(#arM)"/>
  <!-- F1 generation -->
  <text x="130" y="175" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b" font-weight="600">F1 generation</text>
  <rect x="80" y="182" width="100" height="55" rx="8" fill="#052e16" stroke="#fbbf24" stroke-width="2"/>
  <text x="130" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fbbf24" font-weight="700">Bb</text>
  <text x="130" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">ALL round seeds</text>
  <text x="130" y="233" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">(B dominates)</text>
  <!-- F2 arrow -->
  <line x1="130" y1="240" x2="130" y2="258" stroke="#475569" stroke-width="2" marker-end="url(#arM)"/>
  <text x="130" y="268" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">Bb × Bb</text>
  <!-- F2 generation -->
  <text x="130" y="286" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b" font-weight="600">F2 generation</text>
  <rect x="28" y="292" width="52" height="48" rx="6" fill="#052e16" stroke="#4ade80" stroke-width="1.5"/>
  <text x="54" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">BB</text>
  <text x="54" y="333" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b">Round</text>
  <rect x="86" y="292" width="52" height="48" rx="6" fill="#052e16" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="112" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24" font-weight="700">Bb</text>
  <text x="112" y="333" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b">Round</text>
  <rect x="144" y="292" width="52" height="48" rx="6" fill="#052e16" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="170" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24" font-weight="700">bB</text>
  <text x="170" y="333" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b">Round</text>
  <rect x="202" y="292" width="52" height="48" rx="6" fill="#1c1917" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="228" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8" font-weight="700">bb</text>
  <text x="228" y="333" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b">Wrinkled</text>
  <rect x="28" y="352" width="226" height="32" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="141" y="373" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f1f5f9" font-weight="600">3 Round : 1 Wrinkled</text>
  <!-- Punnett square -->
  <text x="530" y="62" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="700">Punnett Square (F1 × F1)</text>
  <!-- Grid -->
  <rect x="430" y="72" width="200" height="200" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <line x1="530" y1="72" x2="530" y2="272" stroke="#334155" stroke-width="1"/>
  <line x1="430" y1="172" x2="630" y2="172" stroke="#334155" stroke-width="1"/>
  <!-- Headers -->
  <text x="480" y="92" text-anchor="middle" font-family="monospace,sans-serif" font-size="12" fill="#4ade80" font-weight="700">B</text>
  <text x="580" y="92" text-anchor="middle" font-family="monospace,sans-serif" font-size="12" fill="#94a3b8" font-weight="700">b</text>
  <text x="418" y="135" text-anchor="middle" font-family="monospace,sans-serif" font-size="12" fill="#4ade80" font-weight="700">B</text>
  <text x="418" y="235" text-anchor="middle" font-family="monospace,sans-serif" font-size="12" fill="#94a3b8" font-weight="700">b</text>
  <!-- Cells -->
  <rect x="432" y="174" width="96" height="96" rx="2" fill="#052e16"/>
  <text x="480" y="220" text-anchor="middle" font-family="monospace,sans-serif" font-size="14" fill="#4ade80" font-weight="700">BB</text>
  <rect x="532" y="174" width="96" height="96" rx="2" fill="#052e16"/>
  <text x="580" y="220" text-anchor="middle" font-family="monospace,sans-serif" font-size="14" fill="#fbbf24" font-weight="700">Bb</text>
  <rect x="432" y="74" width="96" height="96" rx="2" fill="#052e16"/>
  <text x="480" y="120" text-anchor="middle" font-family="monospace,sans-serif" font-size="14" fill="#fbbf24" font-weight="700">Bb</text>
  <rect x="532" y="74" width="96" height="96" rx="2" fill="#1c1917"/>
  <text x="580" y="120" text-anchor="middle" font-family="monospace,sans-serif" font-size="14" fill="#f472b6" font-weight="700">bb</text>
  <!-- Ratios -->
  <text x="530" y="298" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="600">Genotype ratio: 1 BB : 2 Bb : 1 bb</text>
  <text x="530" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">Phenotype ratio: 3 dominant : 1 recessive</text>
  <text x="530" y="340" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Mendel observed this 3:1 ratio in</text>
  <text x="530" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">7,324 F2 peas — 5,474 round : 1,850 wrinkled</text>
  <text x="530" y="368" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">(actual ratio: 2.96:1)</text>
  <text x="530" y="385" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Published 1866. Rediscovered 1900.</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Mendel's monohybrid cross: crossing true-breeding round (BB) with wrinkled (bb) peas produces all-round F1 (Bb). Crossing F1 with F1 gives the 3:1 phenotype ratio. The Punnett square predicts the same outcome by tracking which alleles can combine at fertilisation.</figcaption>
</figure>

<h2>The two laws Mendel deduced</h2>
<p><strong>The Law of Segregation</strong> states that the two alleles for any trait separate during gamete formation — each gamete receives only one allele at each locus. This is the physical consequence of meiosis: when a parent cell divides to form eggs or sperm, homologous chromosomes separate, and each gamete receives only one copy of each chromosome pair.</p>
<p><strong>The Law of Independent Assortment</strong> states that alleles for different traits are inherited independently of each other — the allele a child inherits at the eye-colour locus has no bearing on which allele they inherit at the blood-type locus. This holds true for genes on different chromosomes. Genes on the same chromosome violate independent assortment and are said to be <strong>linked</strong> — they tend to be inherited together unless crossing-over during meiosis separates them.</p>
<p>Mendel did not know what chromosomes were. He deduced the logic of inheritance from plant counts alone. When his papers were rediscovered in 1900 — sixteen years after his death — and when Thomas Hunt Morgan's work on fruit flies in the 1910s connected Mendel's abstract factors to physical chromosomes, the two halves of genetics clicked together.</p>

<h2>Beyond simple dominance</h2>
<p>Mendel's peas happen to exhibit clean dominant-recessive relationships. Biology is often messier. In <strong>incomplete dominance</strong>, neither allele fully masks the other — a cross between a red-flowered plant and a white-flowered plant produces pink offspring. In <strong>codominance</strong>, both alleles are fully expressed simultaneously — the AB blood type is produced by the simultaneous expression of both A and B antigens on red blood cells. Most human traits are <strong>polygenic</strong> — determined by many genes at once — which is why height, skin colour, and intelligence do not distribute in simple Mendelian ratios but in continuous bell curves.</p>"""

# ── Article 5: Sex Chromosomes and Inheritance ────────────────────────────────

A5_CONTENT = """
<p class="lead">Every human being begins with a single cell. In that cell, among the 46 chromosomes, lies the answer to a question that has shaped cultures, determined dynasties, and been catastrophically misunderstood for most of recorded history: what determines whether a person develops as male or female? The answer is chromosomal, precise, and decided at the moment of fertilisation — and it is entirely determined by the father's sperm, not the mother's egg.</p>

<h2>The XX/XY system</h2>
<p>Females carry two copies of the X chromosome (XX). Males carry one X and one Y chromosome (XY). The X chromosome is large — about 155 million base pairs, carrying approximately 800–900 genes. The Y chromosome is much smaller — about 57 million base pairs, carrying only approximately 70 protein-coding genes, many of them involved in male sex determination and sperm production.</p>
<p>The critical gene on the Y chromosome is <strong>SRY</strong> (Sex-determining Region Y) — a master switch gene that, when present and active during embryonic development, triggers a cascade that directs the undifferentiated gonads to develop into testes rather than ovaries. Without SRY, development defaults toward the female pathway.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="How sex chromosomes are inherited: eggs always carry X, sperm carry either X or Y, determining sex at fertilisation">
  <rect width="720" height="400" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Sex Chromosome Inheritance — Father Determines Sex</text>
  <text x="360" y="46" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Mother always contributes X · Father contributes X (daughter) or Y (son)</text>
  <defs>
    <marker id="arS" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker>
  </defs>
  <!-- Mother -->
  <rect x="40" y="65" width="150" height="90" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="115" y="88" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#fcd34d" font-weight="700">Mother ♀</text>
  <text x="115" y="106" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f59e0b" font-weight="900">XX</text>
  <text x="115" y="126" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Somatic cells carry XX</text>
  <text x="115" y="140" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">All eggs carry one X</text>
  <!-- Father -->
  <rect x="530" y="65" width="150" height="90" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="605" y="88" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#86efac" font-weight="700">Father ♂</text>
  <text x="605" y="106" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#22c55e" font-weight="900">XY</text>
  <text x="605" y="126" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Somatic cells carry XY</text>
  <text x="605" y="140" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Sperm: 50% X · 50% Y</text>
  <!-- Meiosis arrows -->
  <line x1="115" y1="158" x2="115" y2="195" stroke="#f59e0b" stroke-width="2" marker-end="url(#arS)"/>
  <text x="115" y="178" text-anchor="start" font-family="system-ui,sans-serif" font-size="8" fill="#64748b" dx="6">meiosis</text>
  <line x1="605" y1="158" x2="605" y2="195" stroke="#22c55e" stroke-width="2" marker-end="url(#arS)"/>
  <text x="605" y="178" text-anchor="start" font-family="system-ui,sans-serif" font-size="8" fill="#64748b" dx="6">meiosis</text>
  <!-- Egg -->
  <circle cx="115" cy="222" r="28" fill="#1c0f05" stroke="#f59e0b" stroke-width="2"/>
  <text x="115" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24" font-weight="700">Egg</text>
  <text x="115" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#f59e0b" font-weight="900">X</text>
  <text x="115" y="262" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">Always X</text>
  <!-- Sperm X and Y -->
  <circle cx="565" cy="222" r="24" fill="#021a0f" stroke="#22c55e" stroke-width="2"/>
  <text x="565" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac" font-weight="700">Sperm</text>
  <text x="565" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#22c55e" font-weight="900">X</text>
  <text x="565" y="258" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">50% of sperm</text>
  <circle cx="645" cy="222" r="24" fill="#0a0a1a" stroke="#818cf8" stroke-width="2"/>
  <text x="645" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd" font-weight="700">Sperm</text>
  <text x="645" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#818cf8" font-weight="900">Y</text>
  <text x="645" y="258" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">50% of sperm</text>
  <!-- Fertilisation arrows -->
  <line x1="143" y1="222" x2="325" y2="305" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arS)"/>
  <line x1="143" y1="235" x2="325" y2="340" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arS)"/>
  <line x1="538" y1="222" x2="395" y2="305" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arS)"/>
  <line x1="620" y1="222" x2="395" y2="340" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arS)"/>
  <!-- Outcomes -->
  <rect x="295" y="285" width="130" height="55" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="360" y="308" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#f59e0b" font-weight="900">XX ♀</text>
  <text x="360" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Daughter</text>
  <text x="360" y="338" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">(X egg + X sperm)</text>
  <rect x="295" y="352" width="130" height="38" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="2"/>
  <text x="360" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#818cf8" font-weight="900">XY ♂</text>
  <text x="360" y="383" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">Son (X egg + Y sperm)</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Sex is determined at fertilisation entirely by the father's sperm. Because every egg carries an X chromosome (the mother has no Y to give), the child's sex depends on whether the fertilising sperm carries X (producing XX, a daughter) or Y (producing XY, a son). Each pregnancy is an independent 50/50 event.</figcaption>
</figure>

<h2>Why the father — not the mother — determines sex</h2>
<p>For most of recorded history, women were blamed, punished, and discarded when they "failed to produce sons." Henry VIII annulled two marriages and executed one wife in the pursuit of a male heir. The irony — invisible without genetics — is that the mother has no capacity to influence the sex of her child. Every egg a woman produces carries one X chromosome. That is the only option. The sperm, produced by the father, are the variable: approximately half carry an X chromosome, half carry a Y. At fertilisation it is the sperm that decides.</p>
<blockquote><p>"The gene is the fundamental unit of heredity — and what we discover in that unit changes everything we thought we knew about identity, fate, and the meaning of what we inherit."</p><footer>— Siddhartha Mukherjee, The Gene: An Intimate History</footer></blockquote>

<h2>X-linked inheritance: why some traits affect sons more than daughters</h2>
<p>The X chromosome carries approximately 800 functional genes, many of them having nothing to do with sex. Conditions caused by recessive alleles on the X chromosome follow a distinctive inheritance pattern: <strong>X-linked recessive</strong> conditions affect males far more commonly than females, because males have only one X chromosome. If that single X carries the disease allele, there is no second X to provide a working copy.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="X-linked recessive inheritance pattern showing why sons of carrier mothers are affected">
  <rect width="720" height="380" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">X-Linked Recessive Inheritance</text>
  <text x="360" y="46" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">Example: haemophilia A (Factor VIII gene on X) · colour blindness · Duchenne muscular dystrophy</text>
  <defs>
    <marker id="arX" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker>
  </defs>
  <!-- Legend -->
  <rect x="40" y="60" width="200" height="90" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="140" y="80" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="600">Legend</text>
  <text x="56" y="98" font-family="monospace,sans-serif" font-size="11" fill="#f59e0b">Xᴬ</text>
  <text x="80" y="98" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= X with normal allele</text>
  <text x="56" y="116" font-family="monospace,sans-serif" font-size="11" fill="#ef4444">Xᵃ</text>
  <text x="80" y="116" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= X with disease allele</text>
  <text x="56" y="134" font-family="monospace,sans-serif" font-size="11" fill="#22c55e">Y</text>
  <text x="80" y="134" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= Y chromosome</text>
  <!-- Parents -->
  <rect x="270" y="60" width="120" height="70" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="330" y="82" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fcd34d" font-weight="700">Mother ♀</text>
  <text x="330" y="102" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="355" y="102" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#ef4444" font-weight="700">Xᵃ</text>
  <text x="330" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">Carrier — unaffected</text>
  <rect x="430" y="60" width="120" height="70" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="490" y="82" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac" font-weight="700">Father ♂</text>
  <text x="490" y="102" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="515" y="102" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#22c55e" font-weight="700">Y</text>
  <text x="490" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">Unaffected male</text>
  <!-- Arrows down -->
  <line x1="330" y1="133" x2="330" y2="158" stroke="#475569" stroke-width="1.5" marker-end="url(#arX)"/>
  <line x1="490" y1="133" x2="490" y2="158" stroke="#475569" stroke-width="1.5" marker-end="url(#arX)"/>
  <!-- Four offspring -->
  <!-- Daughter 1: XA XA - unaffected, not carrier -->
  <rect x="50" y="165" width="130" height="90" rx="8" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="115" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">Daughter ♀</text>
  <text x="95" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="120" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="115" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#4ade80">Unaffected</text>
  <text x="115" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">Not a carrier</text>
  <text x="115" y="266" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">25% probability</text>
  <!-- Daughter 2: XA Xa - carrier -->
  <rect x="200" y="165" width="130" height="90" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="265" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24" font-weight="700">Daughter ♀</text>
  <text x="243" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="268" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#ef4444" font-weight="700">Xᵃ</text>
  <text x="265" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#fbbf24">Unaffected</text>
  <text x="265" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fbbf24">Carrier</text>
  <text x="265" y="266" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">25% probability</text>
  <!-- Son 1: XA Y - unaffected -->
  <rect x="350" y="165" width="130" height="90" rx="8" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="415" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">Son ♂</text>
  <text x="393" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#f59e0b" font-weight="700">Xᴬ</text>
  <text x="418" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#22c55e" font-weight="700">Y</text>
  <text x="415" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#4ade80">Unaffected</text>
  <text x="415" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">Normal male</text>
  <text x="415" y="266" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">25% probability</text>
  <!-- Son 2: Xa Y - AFFECTED -->
  <rect x="500" y="165" width="175" height="90" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
  <text x="588" y="186" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5" font-weight="700">Son ♂</text>
  <text x="560" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#ef4444" font-weight="700">Xᵃ</text>
  <text x="585" y="210" text-anchor="middle" font-family="monospace,sans-serif" font-size="13" fill="#22c55e" font-weight="700">Y</text>
  <text x="588" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444" font-weight="700">AFFECTED</text>
  <text x="588" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">No working copy — Y</text>
  <text x="588" y="256" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">cannot compensate</text>
  <text x="588" y="268" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">25% probability</text>
  <!-- Key insight box -->
  <rect x="50" y="296" width="620" height="72" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="360" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="700">Why X-linked conditions affect sons at twice the rate of daughters</text>
  <text x="360" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Daughters have two X chromosomes — even if one carries the disease allele, the other X often provides a functional backup.</text>
  <text x="360" y="352" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Sons have only one X. If that X carries the disease allele, there is no second copy. The Y chromosome has no matching gene.</text>
  <text x="360" y="368" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Famous examples: haemophilia A (Queen Victoria carrier) · red-green colour blindness (8% of males, 0.5% females) · Duchenne MD</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">X-linked recessive inheritance from a carrier mother: daughters have a 50% chance of being carriers; sons have a 50% chance of being affected. No son can inherit the condition from his father (he receives only the Y); no son can pass it to his sons (he gives them the Y, not his X).</figcaption>
</figure>

<h2>Historical note: the weight of biological misattribution</h2>
<p>The genetic mechanism of sex determination was not understood until the early twentieth century. Thomas Hunt Morgan's work on fruit flies, beginning in 1908, established that sex was chromosomally determined and that genes on the X chromosome followed a distinctive inheritance pattern. The full mechanism of SRY as the master sex-determination switch was not identified until 1990.</p>
<p>Before this understanding, the cultural consequences of biological ignorance were severe. Dynasties were built on the assumption that a woman's body "chose" to produce sons or daughters. The European haemophilia that spread through Queen Victoria's descendants — a condition carried silently by daughters and expressed devastatingly in sons — was attributed to various causes before the genetics became clear. Mukherjee's point in <em>The Gene</em> is that the history of genetics is inseparable from the history of what we thought we knew about inheritance — and what that wrong knowledge was used to justify.</p>
<p>The X and Y chromosomes are not merely sex determinants. They carry functional genes whose expression differences between males and females contribute to differences in disease susceptibility, drug metabolism, immune function, and longevity. The Y chromosome has been slowly losing genes across evolutionary time — from an ancestral autosome carrying hundreds of genes, it has shed all but approximately 70. Whether this erosion will continue is an open question in evolutionary biology.</p>"""


ARTICLES = [
    {
        'title': 'Alleles and Inheritance: Mendel, Dominant and Recessive, and Why Traits Skip Generations',
        'slug': 'alleles-mendel-inheritance-dominant-recessive',
        'summary': (
            'Before DNA was discovered, Gregor Mendel deduced the rules of inheritance from pea counts. '
            'What alleles are, why some are dominant and others recessive, how the Punnett square predicts '
            'offspring ratios, and why the 3:1 ratio Mendel found in 7,324 peas still holds today.'
        ),
        'content': A4_CONTENT,
        'order': 4,
        'ai_summary': 'Allele, locus, genotype, phenotype. Dominant/recessive, heterozygous/homozygous. Law of Segregation, Law of Independent Assortment. Punnett square. F1/F2 cross. Incomplete dominance, codominance, polygenic traits. Mukherjee on Mendel.',
    },
    {
        'title': 'Sex Chromosomes: Why Sons Get Y from Father and X from Mother — and What That Means',
        'slug': 'sex-chromosomes-xy-inheritance-x-linked',
        'summary': (
            'Sex is determined at fertilisation by a single genetic difference: whether the fertilising '
            'sperm carries an X or a Y. Every egg carries X — so the father always determines the child\'s '
            'sex. Why X-linked conditions devastate sons but spare daughters, and the history of getting '
            'this catastrophically wrong.'
        ),
        'content': A5_CONTENT,
        'order': 5,
        'ai_summary': 'XX female, XY male. SRY gene as sex-determination switch. All eggs carry X; sperm carry X or Y. X-linked recessive: sons affected, daughters carriers. Haemophilia, colour blindness, Duchenne. Y chromosome gene loss. Mukherjee on inheritance and history.',
    },
]


class Command(BaseCommand):
    help = "Load DNA/genetics articles 4-5 (Alleles/Mendel and Sex Chromosomes)"

    def handle(self, *args, **options):
        pillar, _ = Pillar.objects.get_or_create(
            slug='origin-stories-of-dna',
            defaults={
                'name': 'The Origin Stories of DNA',
                'description': 'Mendel, Watson, Crick, and the long argument about what heredity actually is.',
                'icon': '🧬',
                'color': 'pink',
                'order': 11,
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
