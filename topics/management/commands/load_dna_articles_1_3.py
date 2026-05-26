from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

# ── Article 1: DNA Structure ──────────────────────────────────────────────────

A1_CONTENT = """
<p class="lead">Inside every one of your 37 trillion cells sits a molecule two metres long, coiled so tightly it fits inside a space six micrometres across. That molecule — deoxyribonucleic acid — is the master archive of everything the cell needs to build, run, and replicate itself. Understanding DNA begins with understanding its physical shape, because the shape is the mechanism.</p>

<h2>The four-letter alphabet</h2>
<p>DNA is built from four chemical units called nucleotides, each consisting of a sugar (deoxyribose), a phosphate group, and one of four nitrogen-containing bases: <strong>adenine (A)</strong>, <strong>thymine (T)</strong>, <strong>guanine (G)</strong>, and <strong>cytosine (C)</strong>. The bases are the letters of the genetic code. Their sequence along the DNA strand is the information.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="The four DNA bases and their pairing rules">
  <rect width="720" height="340" fill="#090d1a" rx="16"/>
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">The Four DNA Bases — Complementary Base Pairing</text>
  <text x="360" y="50" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">A always pairs with T (2 hydrogen bonds) · G always pairs with C (3 hydrogen bonds)</text>
  <!-- A-T pair -->
  <rect x="40" y="70" width="140" height="110" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="110" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#fbbf24" font-weight="900">A</text>
  <text x="110" y="116" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#fcd34d">Adenine</text>
  <text x="110" y="132" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Purine</text>
  <text x="110" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">2 H-bonds with T</text>
  <line x1="180" y1="125" x2="260" y2="125" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
  <line x1="180" y1="133" x2="260" y2="133" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="220" y="118" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">H·H</text>
  <rect x="260" y="70" width="140" height="110" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
  <text x="330" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#6ee7b7" font-weight="900">T</text>
  <text x="330" y="116" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#6ee7b7">Thymine</text>
  <text x="330" y="132" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Pyrimidine</text>
  <text x="330" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">2 H-bonds with A</text>
  <!-- G-C pair -->
  <rect x="40" y="210" width="140" height="110" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
  <text x="110" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#a5b4fc" font-weight="900">G</text>
  <text x="110" y="256" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#a5b4fc">Guanine</text>
  <text x="110" y="272" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Purine</text>
  <text x="110" y="305" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">3 H-bonds with C</text>
  <line x1="180" y1="262" x2="260" y2="262" stroke="#818cf8" stroke-width="2" stroke-dasharray="5,3"/>
  <line x1="180" y1="270" x2="260" y2="270" stroke="#818cf8" stroke-width="2" stroke-dasharray="5,3"/>
  <line x1="180" y1="278" x2="260" y2="278" stroke="#818cf8" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="220" y="256" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">H·H·H</text>
  <rect x="260" y="210" width="140" height="110" rx="10" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
  <text x="330" y="236" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" fill="#f9a8d4" font-weight="900">C</text>
  <text x="330" y="256" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#f9a8d4">Cytosine</text>
  <text x="330" y="272" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Pyrimidine</text>
  <text x="330" y="305" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">3 H-bonds with G</text>
  <!-- Rule summary panel -->
  <rect x="440" y="70" width="250" height="250" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="565" y="98" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="700">Chargaff's Rules</text>
  <line x1="455" y1="106" x2="675" y2="106" stroke="#1e293b" stroke-width="1"/>
  <text x="565" y="126" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">In any DNA molecule:</text>
  <text x="565" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#fbbf24">%A = %T</text>
  <text x="565" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#a5b4fc">%G = %C</text>
  <text x="565" y="195" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">This symmetry told Watson &amp; Crick</text>
  <text x="565" y="209" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">the two strands were complementary</text>
  <text x="565" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">— one determines the other</text>
  <line x1="455" y1="237" x2="675" y2="237" stroke="#1e293b" stroke-width="1"/>
  <text x="565" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Human genome: ~3.2 billion</text>
  <text x="565" y="269" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">base pairs per haploid cell</text>
  <text x="565" y="290" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">~20,000 protein-coding genes</text>
  <text x="565" y="306" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">encoding ~100,000 proteins</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Complementary base pairing: A-T (2 hydrogen bonds) and G-C (3 hydrogen bonds). Erwin Chargaff noticed the ratio symmetry in 1950; Watson and Crick used it to deduce the double-helix structure in 1953.</figcaption>
</figure>

<h2>The double helix</h2>
<p>James Watson and Francis Crick's 1953 paper in <em>Nature</em> — building on X-ray crystallography data produced by Rosalind Franklin and Maurice Wilkins — described DNA's three-dimensional structure: two strands wound around each other in a right-handed spiral, with the sugar-phosphate backbones on the outside and the bases pointing inward, held together by the hydrogen bonds between complementary pairs.</p>
<blockquote><p>"Watson and Crick's double helix wasn't just some pretty shape. It was a mechanism. The moment you saw it, you understood how information could be copied."</p><footer>— Siddhartha Mukherjee, from lectures on The Gene</footer></blockquote>
<p>The genius of the structure is its self-explaining elegance: each strand is the template for rebuilding the other. When a cell divides, the helix unzips, and each single strand serves as the pattern from which a new complementary strand is synthesised. The result: two identical double helices from one.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="DNA double helix structure showing sugar-phosphate backbone and base pairs">
  <rect width="720" height="400" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">The DNA Double Helix — Structure and Replication Logic</text>
  <!-- Left helix: strand 1 (backbone) -->
  <path d="M 130 50 C 90 100 170 150 130 200 C 90 250 170 300 130 350" stroke="#f59e0b" stroke-width="6" fill="none" stroke-linecap="round"/>
  <!-- Right helix: strand 2 (backbone) -->
  <path d="M 230 50 C 270 100 190 150 230 200 C 270 250 190 300 230 350" stroke="#34d399" stroke-width="6" fill="none" stroke-linecap="round"/>
  <!-- Base pairs (rungs) -->
  <line x1="130" y1="95"  x2="230" y2="95"  stroke="#818cf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="145" y1="125" x2="215" y2="125" stroke="#f472b6" stroke-width="3" stroke-linecap="round"/>
  <line x1="165" y1="155" x2="195" y2="155" stroke="#818cf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="175" y1="185" x2="185" y2="185" stroke="#f472b6" stroke-width="3" stroke-linecap="round"/>
  <line x1="165" y1="215" x2="195" y2="215" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <line x1="145" y1="245" x2="215" y2="245" stroke="#818cf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="130" y1="275" x2="230" y2="275" stroke="#f472b6" stroke-width="3" stroke-linecap="round"/>
  <line x1="140" y1="305" x2="220" y2="305" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <!-- Labels left side -->
  <text x="80" y="58" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">5' end</text>
  <text x="80" y="355" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">3' end</text>
  <text x="275" y="58" text-anchor="start" font-family="system-ui,sans-serif" font-size="9" fill="#34d399">3' end</text>
  <text x="275" y="355" text-anchor="start" font-family="system-ui,sans-serif" font-size="9" fill="#34d399">5' end</text>
  <text x="40" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24" font-weight="600">Sugar-</text>
  <text x="40" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24" font-weight="600">phosphate</text>
  <text x="40" y="231" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24" font-weight="600">backbone</text>
  <line x1="68" y1="220" x2="120" y2="200" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- Annotations -->
  <text x="290" y="98" font-family="system-ui,sans-serif" font-size="9" fill="#818cf8">G-C pair (3 bonds)</text>
  <text x="290" y="128" font-family="system-ui,sans-serif" font-size="9" fill="#f472b6">A-T pair (2 bonds)</text>
  <text x="290" y="158" font-family="system-ui,sans-serif" font-size="9" fill="#818cf8">G-C pair</text>
  <text x="290" y="188" font-family="system-ui,sans-serif" font-size="9" fill="#f472b6">A-T pair</text>
  <!-- Replication panel -->
  <rect x="360" y="50" width="330" height="320" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="525" y="76" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">DNA Replication Logic</text>
  <text x="525" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Semi-conservative: each daughter cell gets</text>
  <text x="525" y="110" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">one original strand + one new strand</text>
  <!-- Original helix -->
  <path d="M 415 130 C 400 155 430 175 415 200" stroke="#f59e0b" stroke-width="4" fill="none"/>
  <path d="M 445 130 C 460 155 430 175 445 200" stroke="#34d399" stroke-width="4" fill="none"/>
  <line x1="415" y1="148" x2="445" y2="148" stroke="#94a3b8" stroke-width="2"/>
  <line x1="424" y1="165" x2="436" y2="165" stroke="#94a3b8" stroke-width="2"/>
  <line x1="418" y1="182" x2="442" y2="182" stroke="#94a3b8" stroke-width="2"/>
  <text x="430" y="120" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">Original</text>
  <!-- Arrow down -->
  <text x="430" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">Helicase unzips →</text>
  <text x="430" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">DNA polymerase builds</text>
  <!-- Two daughter helices -->
  <path d="M 400 255 C 385 275 408 290 400 310" stroke="#f59e0b" stroke-width="3" fill="none"/>
  <path d="M 420 255 C 435 275 408 290 420 310" stroke="#60a5fa" stroke-width="3" fill="none" stroke-dasharray="4,2"/>
  <line x1="400" y1="268" x2="420" y2="268" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="405" y1="283" x2="415" y2="283" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="402" y1="298" x2="418" y2="298" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="410" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Daughter 1</text>
  <path d="M 490 255 C 475 275 498 290 490 310" stroke="#34d399" stroke-width="3" fill="none"/>
  <path d="M 510 255 C 525 275 498 290 510 310" stroke="#60a5fa" stroke-width="3" fill="none" stroke-dasharray="4,2"/>
  <line x1="490" y1="268" x2="510" y2="268" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="495" y1="283" x2="505" y2="283" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="492" y1="298" x2="508" y2="298" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="500" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Daughter 2</text>
  <!-- Legend -->
  <line x1="375" y1="332" x2="395" y2="332" stroke="#f59e0b" stroke-width="3"/>
  <text x="400" y="336" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Original strand</text>
  <line x1="375" y1="350" x2="395" y2="350" stroke="#60a5fa" stroke-width="3" stroke-dasharray="4,2"/>
  <text x="400" y="354" font-family="system-ui,sans-serif" font-size="9" fill="#60a5fa">Newly synthesised</text>
  <text x="525" y="336" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">Error rate: ~1 in 10⁹ bases</text>
  <text x="525" y="350" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">(proofreading by polymerase)</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">The double helix: two antiparallel strands wound around a central axis. During replication the strands separate and each serves as a template — producing two identical copies, each with one original and one new strand (semi-conservative replication).</figcaption>
</figure>

<h2>From molecule to information</h2>
<p>The sequence of bases along a DNA strand is analogous to a text written in a four-letter alphabet. The order of letters encodes instructions: which amino acids to assemble into proteins, when to activate or silence a gene, and how to regulate the cell's entire metabolic programme. Three consecutive bases (a codon) specify one amino acid; the full set of three-letter words translates into the proteins that build and operate every living cell.</p>
<p>The human genome contains approximately 3.2 billion base pairs — enough text, if printed, to fill several thousand books. Of that sequence, only about 1.5% encodes proteins directly. The rest was once dismissed as "junk DNA" but is now understood to include regulatory regions, structural elements, and sequences whose function is still being mapped. As Mukherjee observed, the discovery of the gene's physical structure was only the beginning of understanding what genes actually do.</p>

<h2>Why the structure matters</h2>
<p>Watson and Crick's double helix was not merely a molecular discovery — it was the answer to the most fundamental biological question: how is hereditary information stored and copied with enough fidelity to transmit across generations, yet with enough variation to allow evolution? The answer is encoded in the molecule's shape. The complementary base-pairing rule ensures accurate copying; the four-base alphabet allows virtually unlimited informational complexity; and the antiparallel strand orientation provides the directionality that the replication machinery requires.</p>
<blockquote><p>"Here was Watson, here's this is where Watson stood up and said let's do this. It was a visual tour, as it were, of history — the moment the mechanism of heredity became visible."</p><footer>— Siddhartha Mukherjee</footer></blockquote>"""

# ── Article 2: RNA and Transcription ─────────────────────────────────────────

A2_CONTENT = """
<p class="lead">DNA stores the instructions. But DNA never leaves the nucleus — it is too valuable, too irreplaceable to risk in the noisy machinery of cellular production. Instead, a working copy is made: RNA. The flow of information from DNA to RNA to protein — called the central dogma of molecular biology — is the mechanism by which the genome's instructions become the physical substance of life.</p>

<h2>RNA: the working copy</h2>
<p>Ribonucleic acid (RNA) is chemically similar to DNA with two key differences: it uses ribose sugar instead of deoxyribose, and it uses <strong>uracil (U)</strong> instead of thymine (T). RNA is also typically single-stranded rather than double-stranded, which allows it to fold into three-dimensional shapes and perform catalytic functions — a versatility DNA, locked in its stable double helix, cannot match.</p>
<p>There are three main types of RNA involved in protein synthesis: <strong>messenger RNA (mRNA)</strong>, which carries the gene's instructions from nucleus to ribosome; <strong>transfer RNA (tRNA)</strong>, which reads the instructions and delivers the correct amino acid; and <strong>ribosomal RNA (rRNA)</strong>, which forms the structural and catalytic core of the ribosome itself.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Transcription: DNA is copied into messenger RNA in the nucleus">
  <rect width="720" height="360" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Transcription — DNA → mRNA in the Nucleus</text>
  <defs>
    <marker id="arT" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker>
  </defs>
  <!-- Nucleus boundary -->
  <ellipse cx="360" cy="190" rx="320" ry="145" fill="#0d1b2a" stroke="#334155" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="360" y="60" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569" font-weight="600">NUCLEUS</text>
  <!-- DNA double strand -->
  <path d="M 80 155 Q 200 135 320 155 Q 440 175 560 155" stroke="#f59e0b" stroke-width="4" fill="none"/>
  <path d="M 80 185 Q 200 165 320 185 Q 440 205 560 185" stroke="#34d399" stroke-width="4" fill="none"/>
  <!-- rungs -->
  <line x1="110" y1="159" x2="110" y2="181" stroke="#94a3b8" stroke-width="2"/>
  <line x1="150" y1="147" x2="150" y2="169" stroke="#94a3b8" stroke-width="2"/>
  <line x1="190" y1="140" x2="190" y2="162" stroke="#94a3b8" stroke-width="2"/>
  <line x1="230" y1="143" x2="230" y2="165" stroke="#94a3b8" stroke-width="2"/>
  <line x1="270" y1="150" x2="270" y2="172" stroke="#94a3b8" stroke-width="2"/>
  <!-- Unzipped region with RNA polymerase -->
  <ellipse cx="360" cy="172" rx="55" ry="30" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
  <text x="360" y="166" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd" font-weight="700">RNA</text>
  <text x="360" y="180" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd">Polymerase</text>
  <!-- Growing mRNA strand -->
  <path d="M 415 172 Q 460 200 510 185 Q 555 170 600 182" stroke="#f97316" stroke-width="3.5" fill="none"/>
  <text x="555" y="165" font-family="system-ui,sans-serif" font-size="9" fill="#fb923c" font-weight="600">mRNA</text>
  <text x="555" y="178" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">growing 5'→3'</text>
  <!-- Labels -->
  <text x="100" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Template strand</text>
  <text x="100" y="233" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">(3'→5' read)</text>
  <text x="100" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#34d399">Coding strand</text>
  <text x="100" y="136" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#34d399">(sense strand)</text>
  <!-- Base comparison box -->
  <rect x="80" y="268" width="280" height="70" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="220" y="286" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="600">DNA vs RNA bases</text>
  <text x="220" y="304" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">DNA: A  T  G  C</text>
  <text x="220" y="320" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f97316">RNA: A  U  G  C  (U replaces T)</text>
  <text x="220" y="332" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">+ ribose sugar · single-stranded</text>
  <!-- mRNA exits -->
  <rect x="400" y="268" width="280" height="70" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="540" y="286" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="600">mRNA is processed</text>
  <text x="540" y="303" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">5' cap added · poly-A tail added</text>
  <text x="540" y="317" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Introns spliced out · exons joined</text>
  <text x="540" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">→ exported to cytoplasm</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Transcription: RNA polymerase binds to a promoter sequence on DNA, unzips a short stretch of the double helix, and reads the template strand 3'→5', synthesising a complementary mRNA strand 5'→3'. The mRNA is then processed and exported to the cytoplasm.</figcaption>
</figure>

<h2>Translation: reading the code</h2>
<p>Once the processed mRNA reaches the cytoplasm, ribosomes — molecular machines made of rRNA and proteins — clamp onto it and read the sequence three bases at a time. Each three-base codon specifies one amino acid. Transfer RNA molecules, each carrying a specific amino acid on one end and a three-base anticodon on the other, match codon to anticodon and deliver the correct amino acid to the growing protein chain.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Translation: ribosome reads mRNA and builds a protein chain">
  <rect width="720" height="380" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Translation — mRNA → Protein at the Ribosome</text>
  <!-- mRNA strand -->
  <rect x="40" y="175" width="640" height="32" rx="8" fill="#1c0a00" stroke="#f97316" stroke-width="1.5"/>
  <text x="52" y="186" font-family="system-ui,sans-serif" font-size="8.5" fill="#fb923c">5'</text>
  <text x="85"  y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#fbbf24">AUG</text>
  <text x="120" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#94a3b8">GCU</text>
  <text x="155" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#94a3b8">UAC</text>
  <text x="190" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#94a3b8">CCG</text>
  <text x="225" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#94a3b8">GAA</text>
  <text x="260" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#86efac">codon</text>
  <text x="295" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#86efac">codon</text>
  <text x="330" y="196" text-anchor="middle" font-family="monospace,sans-serif" font-size="10" fill="#86efac">…</text>
  <text x="668" y="186" font-family="system-ui,sans-serif" font-size="8.5" fill="#fb923c">3'</text>
  <text x="85" y="208" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fbbf24">START</text>
  <!-- Ribosome body -->
  <ellipse cx="310" cy="148" rx="90" ry="36" fill="#172554" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="310" y="143" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#93c5fd" font-weight="700">Large subunit (60S)</text>
  <text x="310" y="157" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">contains rRNA + proteins</text>
  <ellipse cx="310" cy="184" rx="85" ry="20" fill="#0f1f3d" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="310" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#93c5fd" font-weight="700">Small subunit (40S)</text>
  <!-- tRNA molecules -->
  <!-- tRNA at A site -->
  <path d="M 320 100 L 310 100 L 310 112 L 295 120 L 325 120 L 310 112" fill="#14532d" stroke="#22c55e" stroke-width="1.2"/>
  <text x="310" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#86efac">tRNA (A site)</text>
  <circle cx="310" cy="80" r="12" fill="#166534" stroke="#4ade80" stroke-width="1.2"/>
  <text x="310" y="84" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#86efac">AA</text>
  <!-- tRNA at P site -->
  <path d="M 270 100 L 260 100 L 260 112 L 245 120 L 275 120 L 260 112" fill="#1c1917" stroke="#f97316" stroke-width="1.2"/>
  <text x="260" y="96" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#fb923c">tRNA (P site)</text>
  <circle cx="260" cy="80" r="12" fill="#431407" stroke="#f97316" stroke-width="1.2"/>
  <text x="260" y="84" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fb923c">AA</text>
  <!-- Protein chain leaving -->
  <path d="M 190 105 Q 160 95 140 90 Q 120 85 100 92 Q 80 99 60 95" stroke="#a855f7" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <text x="95" y="80" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c084fc">Growing protein chain</text>
  <text x="95" y="93" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">(polypeptide)</text>
  <!-- Genetic code table -->
  <rect x="400" y="240" width="290" height="120" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="545" y="260" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="700">The Genetic Code (sample)</text>
  <text x="415" y="278" font-family="monospace,sans-serif" font-size="9" fill="#fbbf24">AUG</text>
  <text x="450" y="278" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= Methionine (START)</text>
  <text x="415" y="294" font-family="monospace,sans-serif" font-size="9" fill="#86efac">GCU</text>
  <text x="450" y="294" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= Alanine</text>
  <text x="415" y="310" font-family="monospace,sans-serif" font-size="9" fill="#86efac">GAA</text>
  <text x="450" y="310" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= Glutamic acid</text>
  <text x="415" y="326" font-family="monospace,sans-serif" font-size="9" fill="#f472b6">UAA/UAG/UGA</text>
  <text x="530" y="326" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">= STOP</text>
  <text x="415" y="347" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">64 codons → 20 amino acids (redundant)</text>
  <!-- Flow summary -->
  <text x="200" y="268" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#e2e8f0" font-weight="700">Central Dogma</text>
  <text x="200" y="285" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fbbf24">DNA</text>
  <text x="200" y="300" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">↓ transcription</text>
  <text x="200" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f97316">mRNA</text>
  <text x="200" y="331" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">↓ translation</text>
  <text x="200" y="347" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#a855f7">Protein</text>
  <text x="200" y="363" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">Francis Crick, 1958</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Translation: the ribosome moves along the mRNA reading codons at the A site and P site. tRNA molecules deliver matching amino acids. The growing polypeptide chain exits the ribosome and folds into a functional protein. One gene can be translated by many ribosomes simultaneously (polysome).</figcaption>
</figure>

<h2>Why RNA is more than a messenger</h2>
<p>The central dogma — DNA → RNA → protein — was Francis Crick's original formulation in 1958. It remains fundamentally correct but significantly incomplete. RNA is now known to perform dozens of regulatory functions beyond simple information relay. MicroRNAs silence genes. Small interfering RNAs (siRNAs) destroy specific mRNA molecules. Long non-coding RNAs organise chromosome structure. Ribosomal RNA catalyses the peptide bond that joins amino acids together. Some RNAs can even evolve catalytic activity — ribozymes — suggesting that RNA, not DNA or protein, may have been the original molecule of life.</p>
<p>The mRNA vaccines developed against COVID-19 exploited this machinery directly: synthetic mRNA encoding the spike protein was delivered into human cells, which then translated it into protein, triggering an immune response. The vaccine was, in a precise sense, a piece of molecular biology's central dogma deployed as medicine.</p>"""

# ── Article 3: Chromosomes ────────────────────────────────────────────────────

A3_CONTENT = """
<p class="lead">If DNA is the text, chromosomes are the books. Each chromosome is a single, enormously long DNA molecule wrapped and organised into a compact structure that can be replicated, sorted, and delivered to daughter cells with extraordinary precision. The way DNA is packaged is not incidental to gene function — it is itself a layer of the genetic code.</p>

<h2>From naked DNA to chromosome</h2>
<p>The two metres of DNA in a human cell must be compacted into a nucleus about six micrometres across — a compression ratio of roughly 50,000:1. This is achieved through a hierarchy of packaging. DNA first wraps twice around protein spools called <strong>histones</strong>, forming structures called <strong>nucleosomes</strong> — the basic unit of chromatin, resembling beads on a string. The nucleosome chain is then folded and coiled through successive levels of higher-order organisation until the full chromosome is formed.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="DNA packaging from double helix to chromosome — five levels of compaction">
  <rect width="720" height="380" fill="#090d1a" rx="16"/>
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">DNA Packaging — From 2 m of DNA to a 5 μm Chromosome</text>
  <defs>
    <marker id="arC" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#475569"/></marker>
  </defs>
  <!-- Level 1: DNA double helix -->
  <text x="60" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">1</text>
  <path d="M 30 95 C 25 110 55 120 50 135 C 45 150 75 160 70 175" stroke="#f59e0b" stroke-width="3" fill="none"/>
  <path d="M 90 95 C 95 110 65 120 70 135 C 75 150 45 160 50 175" stroke="#34d399" stroke-width="3" fill="none"/>
  <line x1="50" y1="108" x2="70" y2="108" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="60" y1="125" x2="60" y2="125" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="55" y1="140" x2="65" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="60" y1="156" x2="60" y2="156" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="60" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#e2e8f0">Double helix</text>
  <text x="60" y="213" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">2 nm wide</text>
  <!-- Arrow -->
  <line x1="105" y1="135" x2="128" y2="135" stroke="#475569" stroke-width="2" marker-end="url(#arC)"/>
  <!-- Level 2: Nucleosomes -->
  <text x="185" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">2</text>
  <path d="M 135 135 Q 148 120 161 135 Q 174 120 187 135 Q 200 120 213 135 Q 226 120 235 135" stroke="#f59e0b" stroke-width="2" fill="none"/>
  <circle cx="148" cy="135" r="10" fill="#334155" stroke="#818cf8" stroke-width="1.5"/>
  <circle cx="174" cy="135" r="10" fill="#334155" stroke="#818cf8" stroke-width="1.5"/>
  <circle cx="200" cy="135" r="10" fill="#334155" stroke="#818cf8" stroke-width="1.5"/>
  <text x="185" y="165" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#e2e8f0">Nucleosomes</text>
  <text x="185" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">"beads on a string"</text>
  <text x="185" y="191" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">11 nm wide</text>
  <!-- Arrow -->
  <line x1="248" y1="135" x2="268" y2="135" stroke="#475569" stroke-width="2" marker-end="url(#arC)"/>
  <!-- Level 3: 30 nm chromatin fibre -->
  <text x="310" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">3</text>
  <path d="M 278 95 Q 300 115 282 135 Q 264 155 286 175" stroke="#818cf8" stroke-width="7" fill="none" stroke-linecap="round"/>
  <text x="310" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#e2e8f0">30 nm fibre</text>
  <text x="310" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">solenoid coiling</text>
  <!-- Arrow -->
  <line x1="345" y1="135" x2="368" y2="135" stroke="#475569" stroke-width="2" marker-end="url(#arC)"/>
  <!-- Level 4: Loop domains -->
  <text x="430" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">4</text>
  <line x1="430" y1="88" x2="430" y2="175" stroke="#334155" stroke-width="2"/>
  <path d="M 430 100 Q 460 115 430 130" stroke="#818cf8" stroke-width="5" fill="none"/>
  <path d="M 430 120 Q 400 135 430 150" stroke="#818cf8" stroke-width="5" fill="none"/>
  <path d="M 430 140 Q 460 155 430 170" stroke="#818cf8" stroke-width="5" fill="none"/>
  <text x="430" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#e2e8f0">Loop domains</text>
  <text x="430" y="211" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">300 nm scaffold</text>
  <!-- Arrow -->
  <line x1="472" y1="135" x2="492" y2="135" stroke="#475569" stroke-width="2" marker-end="url(#arC)"/>
  <!-- Level 5: Chromosome -->
  <text x="595" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">5</text>
  <path d="M 570 88 Q 555 105 565 128 Q 575 150 560 170 Q 553 183 565 195 Q 580 210 575 225 Q 568 245 583 258" stroke="#22c55e" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M 620 88 Q 635 105 625 128 Q 615 150 630 170 Q 637 183 625 195 Q 610 210 615 225 Q 622 245 607 258" stroke="#22c55e" stroke-width="12" fill="none" stroke-linecap="round"/>
  <ellipse cx="595" cy="173" rx="12" ry="8" fill="#052e16" stroke="#4ade80" stroke-width="1.5"/>
  <text x="595" y="177" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#86efac">CEN</text>
  <text x="595" y="298" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#e2e8f0">Chromosome</text>
  <text x="595" y="311" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">1,400 nm · 50,000× compacted</text>
  <!-- Scale bar -->
  <text x="360" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">Compression: 2 metres of DNA → 5 micrometres of chromosome</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Five levels of DNA compaction: the double helix wraps around histone octamers to form nucleosomes, which coil into 30 nm fibres, which loop and scaffold into progressively more compact structures until the final metaphase chromosome is achieved.</figcaption>
</figure>

<h2>Human chromosomes: 23 pairs</h2>
<p>Humans carry 46 chromosomes in 23 pairs. For each pair, one chromosome came from the mother's egg and one from the father's sperm. Pairs 1 through 22 are called <strong>autosomes</strong> — they are present in both males and females in matching pairs. The 23rd pair is the <strong>sex chromosomes</strong>: females carry two X chromosomes (XX), males carry one X and one Y (XY). The chromosome number, shape, and banding pattern together form the <strong>karyotype</strong> — a cellular signature of the genome's structural organisation.</p>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Human karyotype showing 23 chromosome pairs including XX and XY sex chromosomes">
  <rect width="720" height="380" fill="#090d1a" rx="16"/>
  <text x="360" y="24" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#f1f5f9" font-weight="700">Human Karyotype — 23 Chromosome Pairs</text>
  <text x="360" y="41" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#475569">22 autosome pairs + 1 sex chromosome pair · 46 chromosomes total</text>
  <!-- Chromosomes arranged in rows, pair numbers below -->
  <!-- Row 1: chr 1-7 -->
  <g transform="translate(0,10)">
  <!-- Pair 1 (largest) -->
  <rect x="28" y="58" width="7" height="54" rx="3" fill="#6366f1"/><rect x="38" y="58" width="7" height="54" rx="3" fill="#6366f1"/>
  <text x="38" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">1</text>
  <!-- Pair 2 -->
  <rect x="55" y="63" width="7" height="48" rx="3" fill="#6366f1"/><rect x="65" y="63" width="7" height="48" rx="3" fill="#6366f1"/>
  <text x="65" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">2</text>
  <!-- Pair 3 -->
  <rect x="82" y="66" width="7" height="44" rx="3" fill="#6366f1"/><rect x="92" y="66" width="7" height="44" rx="3" fill="#6366f1"/>
  <text x="92" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">3</text>
  <!-- Pair 4 -->
  <rect x="109" y="69" width="7" height="40" rx="3" fill="#0284c7"/><rect x="119" y="69" width="7" height="40" rx="3" fill="#0284c7"/>
  <text x="119" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">4</text>
  <!-- Pair 5 -->
  <rect x="136" y="69" width="7" height="40" rx="3" fill="#0284c7"/><rect x="146" y="69" width="7" height="40" rx="3" fill="#0284c7"/>
  <text x="146" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">5</text>
  <!-- Pair 6 -->
  <rect x="163" y="71" width="7" height="37" rx="3" fill="#0284c7"/><rect x="173" y="71" width="7" height="37" rx="3" fill="#0284c7"/>
  <text x="173" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">6</text>
  <!-- Pair 7 -->
  <rect x="190" y="73" width="7" height="34" rx="3" fill="#0284c7"/><rect x="200" y="73" width="7" height="34" rx="3" fill="#0284c7"/>
  <text x="200" y="124" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">7</text>
  <!-- Row 2: chr 8-15 -->
  <!-- Pair 8 -->
  <rect x="28" y="148" width="7" height="30" rx="3" fill="#059669"/><rect x="38" y="148" width="7" height="30" rx="3" fill="#059669"/>
  <text x="38" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">8</text>
  <!-- Pair 9 -->
  <rect x="55" y="150" width="7" height="28" rx="3" fill="#059669"/><rect x="65" y="150" width="7" height="28" rx="3" fill="#059669"/>
  <text x="65" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">9</text>
  <!-- Pair 10 -->
  <rect x="82" y="152" width="7" height="26" rx="3" fill="#059669"/><rect x="92" y="152" width="7" height="26" rx="3" fill="#059669"/>
  <text x="92" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">10</text>
  <!-- Pair 11 -->
  <rect x="109" y="152" width="7" height="26" rx="3" fill="#059669"/><rect x="119" y="152" width="7" height="26" rx="3" fill="#059669"/>
  <text x="119" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">11</text>
  <!-- Pair 12 -->
  <rect x="136" y="152" width="7" height="26" rx="3" fill="#059669"/><rect x="146" y="152" width="7" height="26" rx="3" fill="#059669"/>
  <text x="146" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">12</text>
  <!-- Pair 13 -->
  <rect x="163" y="155" width="7" height="22" rx="3" fill="#b45309"/><rect x="173" y="155" width="7" height="22" rx="3" fill="#b45309"/>
  <text x="173" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">13</text>
  <!-- Pair 14 -->
  <rect x="190" y="155" width="7" height="22" rx="3" fill="#b45309"/><rect x="200" y="155" width="7" height="22" rx="3" fill="#b45309"/>
  <text x="200" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">14</text>
  <!-- Pair 15 -->
  <rect x="217" y="155" width="7" height="22" rx="3" fill="#b45309"/><rect x="227" y="155" width="7" height="22" rx="3" fill="#b45309"/>
  <text x="227" y="190" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">15</text>
  <!-- Row 3: chr 16-22 + sex -->
  <!-- Pair 16 -->
  <rect x="28" y="212" width="7" height="19" rx="3" fill="#7c3aed"/><rect x="38" y="212" width="7" height="19" rx="3" fill="#7c3aed"/>
  <text x="38" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">16</text>
  <!-- Pair 17 -->
  <rect x="55" y="213" width="7" height="18" rx="3" fill="#7c3aed"/><rect x="65" y="213" width="7" height="18" rx="3" fill="#7c3aed"/>
  <text x="65" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">17</text>
  <!-- Pair 18 -->
  <rect x="82" y="214" width="7" height="17" rx="3" fill="#7c3aed"/><rect x="92" y="214" width="7" height="17" rx="3" fill="#7c3aed"/>
  <text x="92" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">18</text>
  <!-- Pair 19 -->
  <rect x="109" y="215" width="7" height="15" rx="3" fill="#be185d"/><rect x="119" y="215" width="7" height="15" rx="3" fill="#be185d"/>
  <text x="119" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">19</text>
  <!-- Pair 20 -->
  <rect x="136" y="215" width="7" height="15" rx="3" fill="#be185d"/><rect x="146" y="215" width="7" height="15" rx="3" fill="#be185d"/>
  <text x="146" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">20</text>
  <!-- Pair 21 -->
  <rect x="163" y="217" width="7" height="12" rx="3" fill="#be185d"/><rect x="173" y="217" width="7" height="12" rx="3" fill="#be185d"/>
  <text x="173" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">21</text>
  <!-- Pair 22 -->
  <rect x="190" y="217" width="7" height="12" rx="3" fill="#be185d"/><rect x="200" y="217" width="7" height="12" rx="3" fill="#be185d"/>
  <text x="200" y="244" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#94a3b8">22</text>
  <!-- Sex chromosomes highlighted -->
  <rect x="228" y="202" width="60" height="56" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="234" y="208" width="9" height="35" rx="3" fill="#f59e0b"/>
  <rect x="246" y="208" width="9" height="35" rx="3" fill="#f59e0b"/>
  <text x="248" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#fbbf24">XX ♀</text>
  <rect x="300" y="202" width="60" height="56" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <rect x="306" y="208" width="9" height="35" rx="3" fill="#22c55e"/>
  <rect x="318" y="218" width="9" height="19" rx="3" fill="#22c55e"/>
  <text x="318" y="252" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#4ade80">XY ♂</text>
  <text x="278" y="272" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Pair 23 — Sex chromosomes</text>
  </g>
  <!-- Info panel -->
  <rect x="390" y="58" width="300" height="280" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="540" y="80" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="700">Chromosome Key Facts</text>
  <line x1="405" y1="88" x2="675" y2="88" stroke="#1e293b" stroke-width="1"/>
  <text x="405" y="106" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Total chromosomes:</text>
  <text x="675" y="106" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#f1f5f9">46 (diploid)</text>
  <text x="405" y="124" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">From mother (egg):</text>
  <text x="675" y="124" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#f1f5f9">23 chromosomes</text>
  <text x="405" y="142" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">From father (sperm):</text>
  <text x="675" y="142" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#f1f5f9">23 chromosomes</text>
  <text x="405" y="160" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Autosome pairs:</text>
  <text x="675" y="160" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#f1f5f9">22 pairs</text>
  <text x="405" y="178" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Sex chromosome pair:</text>
  <text x="675" y="178" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#f1f5f9">1 pair (XX or XY)</text>
  <line x1="405" y1="188" x2="675" y2="188" stroke="#1e293b" stroke-width="1"/>
  <text x="405" y="206" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Largest: Chr 1</text>
  <text x="675" y="206" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">~249 Mb · ~2,000 genes</text>
  <text x="405" y="224" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Smallest: Chr 21</text>
  <text x="675" y="224" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">~47 Mb · ~200 genes</text>
  <text x="405" y="242" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">Y chromosome:</text>
  <text x="675" y="242" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#fbbf24">~57 Mb · only ~70 genes</text>
  <line x1="405" y1="252" x2="675" y2="252" stroke="#1e293b" stroke-width="1"/>
  <text x="540" y="270" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#94a3b8">Chromatin states</text>
  <text x="405" y="287" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">Euchromatin:</text>
  <text x="675" y="287" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">open · transcribed · active genes</text>
  <text x="405" y="305" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Heterochromatin:</text>
  <text x="675" y="305" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">condensed · silenced genes</text>
  <text x="540" y="325" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#475569">Histone modifications (methylation, acetylation)</text>
  <text x="540" y="337" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#475569">control which state chromatin adopts</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Human karyotype: 22 autosome pairs (numbered by size, largest first) plus one sex chromosome pair. Females are XX; males are XY. The Y chromosome is far smaller than the X and carries far fewer genes.</figcaption>
</figure>

<h2>The centromere, telomeres, and chromosome architecture</h2>
<p>Every chromosome has three functionally essential elements. The <strong>centromere</strong> is a constricted region where the two sister chromatids are joined after DNA replication and where the kinetochore — the attachment point for the spindle fibres that pull chromosomes apart during cell division — assembles. The <strong>telomeres</strong> are repetitive DNA sequences (TTAGGG repeated thousands of times) that cap each chromosome end, protecting it from degradation and preventing chromosome ends from being recognised as DNA breaks. <strong>Origins of replication</strong> are the sites where DNA replication initiates along each chromosome.</p>
<p>Telomere length is now understood as a biological clock of cellular ageing. Each round of DNA replication shortens the telomere slightly — because the replication machinery cannot copy the very end of a linear chromosome. When telomeres shorten to a critical length, cells cease dividing. Telomerase, an enzyme that extends telomeres, is active in stem cells and germline cells but largely absent from differentiated somatic cells — which is why most adult cells have a finite replicative lifespan. Cancer cells, notably, reactivate telomerase, achieving the immortality of uncontrolled division.</p>"""


ARTICLES = [
    {
        'title': 'DNA: The Double Helix — Structure, Base Pairing, and Replication',
        'slug': 'dna-double-helix-structure-replication',
        'summary': (
            'Inside every cell sits two metres of DNA coiled into a space six micrometres across. '
            'How the double helix works, why complementary base pairing matters, and how one molecule '
            'copies itself with extraordinary fidelity — with Mukherjee on the moment the mechanism '
            'of heredity became visible.'
        ),
        'content': A1_CONTENT,
        'order': 1,
        'ai_summary': 'Four bases (A, T, G, C), Chargaff rules, Watson-Crick double helix, semi-conservative replication via helicase and DNA polymerase. Error rate ~1 in 10^9. Mukherjee perspective on the 1953 discovery.',
    },
    {
        'title': 'RNA, Transcription, and Translation: How DNA Instructions Become Proteins',
        'slug': 'rna-transcription-translation-central-dogma',
        'summary': (
            'DNA stores the instructions but never leaves the nucleus. RNA carries the working copy. '
            'How transcription turns a gene into messenger RNA, how translation reads the genetic '
            'code three bases at a time, and why RNA turns out to be far more than a mere messenger.'
        ),
        'content': A2_CONTENT,
        'order': 2,
        'ai_summary': 'mRNA, tRNA, rRNA roles. RNA polymerase, promoters, intron splicing. Ribosome A/P sites, tRNA anticodon, codon table. Central dogma (Crick 1958). mRNA vaccines as applied central dogma.',
    },
    {
        'title': 'Chromosomes: How Two Metres of DNA Fits Inside a Cell — and Why the Packaging Matters',
        'slug': 'chromosomes-packaging-karyotype-structure',
        'summary': (
            'Chromosomes are not merely storage — the way DNA is packaged controls which genes '
            'are active. Five levels of compaction from double helix to metaphase chromosome, '
            'the human karyotype of 23 pairs, and why telomere length is a biological clock.'
        ),
        'content': A3_CONTENT,
        'order': 3,
        'ai_summary': 'Nucleosomes, 30nm chromatin fibre, loop domains, metaphase chromosome. 46 chromosomes, 23 pairs, autosomes 1-22 plus sex pair. Centromere, telomere, origins of replication. Euchromatin vs heterochromatin, histone modifications, telomerase in cancer.',
    },
]


class Command(BaseCommand):
    help = "Load DNA/genetics articles 1-3 (DNA, RNA, Chromosomes) into origin-stories-of-dna pillar"

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
