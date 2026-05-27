from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

DNA_AI_PILLAR = {
    "name": "DNA, AI, and the Future of Humanity",
    "slug": "dna-ai-future",
    "description": (
        "CRISPR, polygenic prediction, AlphaFold, and what we can do now that "
        "machines can read the genome at scale."
    ),
    "icon": "🧬",
    "color": "rose",
    "order": 3,
}

AI_PILLAR = {
    "name": "Artificial Intelligence",
    "slug": "artificial-intelligence",
    "description": (
        "Machine learning, deep learning, and the systems that are beginning to "
        "reshape science, medicine, and the nature of discovery."
    ),
    "icon": "🤖",
    "color": "indigo",
    "order": 1,
}

SVG_ALPHAFOLD = """<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="AlphaFold: from amino acid sequence to 3D protein structure">
  <defs>
    <radialGradient id="af-bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#0f1a2e" stop-opacity="1"/>
      <stop offset="100%" stop-color="#060c16" stop-opacity="1"/>
    </radialGradient>
    <radialGradient id="af-glow1" cx="30%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#c43d62" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#c43d62" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="af-glow2" cx="70%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#5b6cff" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#5b6cff" stop-opacity="0"/>
    </radialGradient>
    <filter id="af-blur">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="af-glow-soft">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <marker id="af-arr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#94a3b8"/>
    </marker>
    <marker id="af-arr-pink" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#c43d62"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="url(#af-bg)" rx="16"/>
  <rect width="720" height="420" fill="url(#af-glow1)" rx="16"/>
  <rect width="720" height="420" fill="url(#af-glow2)" rx="16"/>

  <!-- Title -->
  <text x="360" y="34" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="15" fill="#f1f5f9" font-weight="700" letter-spacing="-0.3">AlphaFold: Solving Biology's 50-Year Grand Challenge</text>
  <text x="360" y="53" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">From amino acid sequence → 3D protein structure · DeepMind / Google</text>

  <!-- ── LEFT PANEL: Amino Acid Sequence ── -->
  <rect x="30" y="72" width="190" height="290" rx="12" fill="rgba(255,255,255,0.03)" stroke="#1e293b" stroke-width="1.2"/>
  <text x="125" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#94a3b8" font-weight="600" letter-spacing="0.08em">INPUT</text>
  <text x="125" y="113" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#e2e8f0" font-weight="700">Amino Acid Sequence</text>

  <!-- sequence beads -->
  <g transform="translate(48, 130)">
    <!-- Row 1 -->
    <circle cx="0"   cy="0" r="11" fill="#c43d62" opacity="0.9" filter="url(#af-blur)"/>
    <text x="0"  y="4" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Met</text>
    <circle cx="28"  cy="0" r="11" fill="#5b6cff" opacity="0.85" filter="url(#af-blur)"/>
    <text x="28" y="4" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Ala</text>
    <circle cx="56"  cy="0" r="11" fill="#26c2c9" opacity="0.85" filter="url(#af-blur)"/>
    <text x="56" y="4" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Gly</text>
    <circle cx="84"  cy="0" r="11" fill="#a387ff" opacity="0.85" filter="url(#af-blur)"/>
    <text x="84" y="4" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Leu</text>
    <circle cx="112" cy="0" r="11" fill="#2fbf7c" opacity="0.85" filter="url(#af-blur)"/>
    <text x="112" y="4" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Val</text>
    <!-- connecting line -->
    <line x1="11" y1="0" x2="17" y2="0" stroke="#334155" stroke-width="1.5"/>
    <line x1="39" y1="0" x2="45" y2="0" stroke="#334155" stroke-width="1.5"/>
    <line x1="67" y1="0" x2="73" y2="0" stroke="#334155" stroke-width="1.5"/>
    <line x1="95" y1="0" x2="101" y2="0" stroke="#334155" stroke-width="1.5"/>

    <!-- Row 2 -->
    <circle cx="0"   cy="32" r="11" fill="#d4a23a" opacity="0.85" filter="url(#af-blur)"/>
    <text x="0"  y="36" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Ser</text>
    <circle cx="28"  cy="32" r="11" fill="#c43d62" opacity="0.75" filter="url(#af-blur)"/>
    <text x="28" y="36" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Thr</text>
    <circle cx="56"  cy="32" r="11" fill="#5b6cff" opacity="0.8" filter="url(#af-blur)"/>
    <text x="56" y="36" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Pro</text>
    <circle cx="84"  cy="32" r="11" fill="#26c2c9" opacity="0.8" filter="url(#af-blur)"/>
    <text x="84" y="36" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Asp</text>
    <circle cx="112" cy="32" r="11" fill="#a387ff" opacity="0.8" filter="url(#af-blur)"/>
    <text x="112" y="36" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Glu</text>
    <line x1="11" y1="32" x2="17" y2="32" stroke="#334155" stroke-width="1.5"/>
    <line x1="39" y1="32" x2="45" y2="32" stroke="#334155" stroke-width="1.5"/>
    <line x1="67" y1="32" x2="73" y2="32" stroke="#334155" stroke-width="1.5"/>
    <line x1="95" y1="32" x2="101" y2="32" stroke="#334155" stroke-width="1.5"/>

    <!-- Row 3 -->
    <circle cx="0"   cy="64" r="11" fill="#2fbf7c" opacity="0.8"/>
    <text x="0"  y="68" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Arg</text>
    <circle cx="28"  cy="64" r="11" fill="#d4a23a" opacity="0.8"/>
    <text x="28" y="68" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Lys</text>
    <circle cx="56"  cy="64" r="11" fill="#c43d62" opacity="0.75"/>
    <text x="56" y="68" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">His</text>
    <circle cx="84"  cy="64" r="11" fill="#5b6cff" opacity="0.75"/>
    <text x="84" y="68" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Phe</text>
    <circle cx="112" cy="64" r="11" fill="#26c2c9" opacity="0.75"/>
    <text x="112" y="68" text-anchor="middle" font-family="monospace" font-size="9" fill="white" font-weight="700">Trp</text>
    <line x1="11" y1="64" x2="17" y2="64" stroke="#334155" stroke-width="1.5"/>
    <line x1="39" y1="64" x2="45" y2="64" stroke="#334155" stroke-width="1.5"/>
    <line x1="67" y1="64" x2="73" y2="64" stroke="#334155" stroke-width="1.5"/>
    <line x1="95" y1="64" x2="101" y2="64" stroke="#334155" stroke-width="1.5"/>

    <!-- dots indicating more -->
    <circle cx="14"  cy="100" r="3" fill="#334155"/>
    <circle cx="56"  cy="100" r="3" fill="#334155"/>
    <circle cx="98"  cy="100" r="3" fill="#334155"/>
  </g>

  <text x="125" y="310" text-anchor="middle" font-family="monospace" font-size="10" fill="#475569">20 amino acid types</text>
  <text x="125" y="325" text-anchor="middle" font-family="monospace" font-size="10" fill="#475569">100s–1000s of residues</text>
  <text x="125" y="345" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">50 years · no solution</text>
  <rect x="55" y="335" width="140" height="18" rx="4" fill="rgba(196,61,98,0.12)" stroke="#c43d62" stroke-width="0.8"/>
  <text x="125" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c43d62" font-weight="600">Grand Challenge · 1972–2020</text>

  <!-- ── CENTER: AlphaFold Neural Network ── -->
  <rect x="255" y="72" width="210" height="290" rx="12" fill="rgba(91,108,255,0.07)" stroke="#5b6cff" stroke-width="1.2" opacity="0.8"/>
  <text x="360" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#818cf8" font-weight="600" letter-spacing="0.08em">ALPHAFOLD 2 / 3</text>
  <text x="360" y="113" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#e2e8f0" font-weight="700">Deep Learning Engine</text>

  <!-- Neural net layers -->
  <g transform="translate(275, 130)">
    <!-- MSA layer -->
    <rect x="10" y="0" width="170" height="32" rx="6" fill="rgba(91,108,255,0.2)" stroke="#5b6cff" stroke-width="0.8"/>
    <text x="95" y="12" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#a5b4fc" font-weight="600">Multiple Sequence Alignment</text>
    <text x="95" y="24" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#6366f1">Evolution's memory — 3.5 bn years of data</text>

    <!-- Arrow down -->
    <line x1="95" y1="33" x2="95" y2="46" stroke="#334155" stroke-width="1.5" marker-end="url(#af-arr)"/>

    <!-- Evoformer -->
    <rect x="10" y="48" width="170" height="32" rx="6" fill="rgba(163,135,255,0.2)" stroke="#a387ff" stroke-width="0.8"/>
    <text x="95" y="60" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c4b5fd" font-weight="600">Evoformer / Diffusion Stack</text>
    <text x="95" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#7c3aed">48 transformer blocks · attention maps</text>

    <!-- Arrow down -->
    <line x1="95" y1="81" x2="95" y2="94" stroke="#334155" stroke-width="1.5" marker-end="url(#af-arr)"/>

    <!-- Pairwise representation -->
    <rect x="10" y="96" width="170" height="32" rx="6" fill="rgba(38,194,201,0.15)" stroke="#26c2c9" stroke-width="0.8"/>
    <text x="95" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="600">Pairwise Distance Matrix</text>
    <text x="95" y="120" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#0891b2">residue–residue contact prediction</text>

    <!-- Arrow down -->
    <line x1="95" y1="129" x2="95" y2="142" stroke="#334155" stroke-width="1.5" marker-end="url(#af-arr)"/>

    <!-- Structure module -->
    <rect x="10" y="144" width="170" height="32" rx="6" fill="rgba(196,61,98,0.2)" stroke="#c43d62" stroke-width="0.8"/>
    <text x="95" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#fb7185" font-weight="600">Structure Module</text>
    <text x="95" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#be185d">3D coordinate prediction · atomic resolution</text>

    <!-- pLDDT confidence -->
    <rect x="30" y="190" width="130" height="22" rx="5" fill="rgba(47,191,124,0.15)" stroke="#2fbf7c" stroke-width="0.8"/>
    <text x="95" y="205" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80" font-weight="600">pLDDT confidence score · 0–100</text>
  </g>

  <text x="360" y="355" text-anchor="middle" font-family="monospace" font-size="9.5" fill="#475569">Trained on PDB · 170,000 known structures</text>
  <text x="360" y="370" text-anchor="middle" font-family="monospace" font-size="9.5" fill="#475569">Inference: minutes · Lab: months–years</text>

  <!-- ── RIGHT PANEL: Output + Impact ── -->
  <rect x="500" y="72" width="190" height="290" rx="12" fill="rgba(255,255,255,0.03)" stroke="#1e293b" stroke-width="1.2"/>
  <text x="595" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#94a3b8" font-weight="600" letter-spacing="0.08em">OUTPUT &amp; IMPACT</text>
  <text x="595" y="113" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#e2e8f0" font-weight="700">Protein 3D Structure</text>

  <!-- 3D protein schematic (ribbon diagram abstraction) -->
  <g transform="translate(510, 128)">
    <!-- Alpha helix (ribbon) -->
    <path d="M 20 20 C 20 10, 50 10, 50 20 C 50 30, 20 30, 20 40 C 20 50, 50 50, 50 60 C 50 70, 20 70, 20 80"
          fill="none" stroke="#c43d62" stroke-width="6" stroke-linecap="round" opacity="0.85" filter="url(#af-glow-soft)"/>
    <!-- Beta sheet (arrows) -->
    <path d="M 65 15 L 65 45 L 80 45 L 70 60 L 80 60 L 65 75 L 65 105"
          fill="none" stroke="#5b6cff" stroke-width="4" stroke-linecap="round" opacity="0.8"/>
    <polygon points="55,42 75,42 65,55" fill="#5b6cff" opacity="0.75"/>
    <polygon points="55,72 75,72 65,85" fill="#5b6cff" opacity="0.65"/>
    <!-- Loop regions -->
    <path d="M 50 60 C 58 65, 58 70, 65 75" fill="none" stroke="#26c2c9" stroke-width="2.5" stroke-dasharray="3 2" opacity="0.7"/>
    <path d="M 50 20 C 55 12, 60 12, 65 15" fill="none" stroke="#26c2c9" stroke-width="2.5" stroke-dasharray="3 2" opacity="0.7"/>

    <!-- confidence color bar -->
    <rect x="0" y="110" width="160" height="8" rx="4" fill="url(#conf-grad)"/>
  </g>

  <!-- confidence gradient def -->
  <defs>
    <linearGradient id="conf-grad" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="40%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>
  </defs>

  <text x="515" y="252" font-family="system-ui,sans-serif" font-size="8" fill="#ef4444">Low</text>
  <text x="637" y="252" font-family="system-ui,sans-serif" font-size="8" fill="#22c55e" text-anchor="end">High confidence</text>

  <!-- Impact stats -->
  <g transform="translate(510, 262)">
    <rect x="0" y="0" width="160" height="18" rx="4" fill="rgba(196,61,98,0.12)"/>
    <text x="80" y="13" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#fb7185" font-weight="600">200M+ structures in database</text>

    <rect x="0" y="22" width="160" height="18" rx="4" fill="rgba(91,108,255,0.12)"/>
    <text x="80" y="35" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#818cf8" font-weight="600">3M+ researchers · 190 countries</text>

    <rect x="0" y="44" width="160" height="18" rx="4" fill="rgba(38,194,201,0.12)"/>
    <text x="80" y="57" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="600">35,000+ papers cite AlphaFold</text>

    <rect x="0" y="66" width="160" height="18" rx="4" fill="rgba(47,191,124,0.12)"/>
    <text x="80" y="79" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80" font-weight="600">Nobel Prize in Chemistry · 2024</text>
  </g>

  <!-- Arrows: sequence → alphafold → structure -->
  <line x1="222" y1="210" x2="252" y2="210" stroke="#c43d62" stroke-width="2" marker-end="url(#af-arr-pink)"/>
  <line x1="467" y1="210" x2="497" y2="210" stroke="#c43d62" stroke-width="2" marker-end="url(#af-arr-pink)"/>

  <!-- Bottom labels -->
  <text x="360" y="398" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#334155">Based on Demis Hassabis · Google DeepMind · John Jumper · Nobel Laureate 2024</text>
</svg>
</figure>"""

ARTICLE_CONTENT = f"""{SVG_ALPHAFOLD}

<p>In 1972, Christian Anfinsen accepted the Nobel Prize in Chemistry with a prediction. His
work had established that the three-dimensional shape of a protein is determined entirely by
its sequence of amino acids — the linear chain of chemical building blocks the gene encodes.
The implication was bold: given a sequence, the structure should be computable. Nature did it
spontaneously, in milliseconds. Science should eventually be able to do it too.</p>

<p>It took forty-eight years.</p>

<h2>The Grand Challenge</h2>

<p>Proteins are the machines of life. They catalyse every chemical reaction in the cell,
carry oxygen through the blood, replicate DNA, fight pathogens, and transmit signals across
nerve membranes. Their function is almost always inseparable from their shape — the precise,
intricate three-dimensional fold that a linear chain of amino acids twists itself into within
milliseconds of being manufactured by a ribosome.</p>

<p>Understanding that shape is not a curiosity. It is the basis of most modern medicine.
Drug designers spend years trying to determine the shape of a target protein so they can
engineer a molecule that fits into its active site like a key into a lock. Vaccine developers
need to know the shape of a pathogen's surface proteins to build antibodies that can recognise
them. Researchers studying genetic disease need to understand how a mutation changes a
protein's fold — and therefore its function.</p>

<p>The experimental methods for determining protein structure — X-ray crystallography,
cryo-electron microscopy, NMR spectroscopy — are painstaking. A single protein structure can
take a graduate student months or years of work. By 2020, the global scientific community had
collectively solved roughly 170,000 protein structures in 70 years. There are approximately
200 million proteins in nature. At that pace, the gap would never close.</p>

<p>This was the protein folding problem. It was considered one of the great unsolved problems
in biology. It had its own competitive benchmark — the Critical Assessment of Protein
Structure Prediction (CASP) — that had been running since 1994, grading computational
attempts every two years. Progress had been slow and incremental. Most experts thought a real
solution was still decades away.</p>

<h2>The Man Who Chose the Problem on Purpose</h2>

<p>Demis Hassabis founded DeepMind in London in 2010 with a specific ambition: to build
artificial general intelligence, and then use it to solve science's hardest problems. Protein
folding was always on his list. He had studied neuroscience and AI simultaneously, and the
intersection he cared about was not chatbots or recommendation engines — it was using
machine learning to accelerate the rate at which science produces knowledge.</p>

<p>The moment he became certain protein folding was solvable came in March 2016, during the
match between AlphaGo and the world Go champion Lee Sedol. Hassabis watched the game. When
AlphaGo won, he turned to his team and said — and the quote has been verified by those
present — <em>"We can solve protein folding. I'm sure we can do that now."</em></p>

<p>The logic was not obvious. Go and protein folding appear to have nothing in common. But
Hassabis understood something that most biologists did not: the techniques that had allowed
a neural network to master Go — learning from vast libraries of game states, discovering
patterns invisible to human players, training through self-play against evolving positions —
could be applied to the evolutionary information encoded in protein sequences.</p>

<p>Every species that has ever lived has been a protein folding experiment. Evolution has
been running protein structures through billions of years of selection, keeping the ones that
work and discarding the rest. The entire history of that experiment is written in the genomes
of living organisms — in the variations between related proteins across different species.
If you knew which amino acids had changed and which had stayed fixed across 3.5 billion years
of evolution, you would know something deep about which residues are touching each other in
the folded structure (because changing one and not compensating with a paired change would
break the protein). This evolutionary co-variation was the hidden signal AlphaFold was built
to read.</p>

<h2>How AlphaFold Works</h2>

<p>John Jumper, the DeepMind researcher who led the AlphaFold 2 development and shared the
2024 Nobel Prize in Chemistry with Hassabis, describes the core insight simply: <em>"This
process takes a year in the lab. The notion that we'll turn that work into a machine that
gives you a really good answer in five minutes — that was the goal."</em></p>

<p>AlphaFold 2, released in 2020, works in several stages. First, it constructs a
multiple sequence alignment — a comparison of the query protein against thousands of related
proteins from other organisms, cataloguing which positions vary and which stay fixed across
species. This is the evolutionary memory of the protein. Second, it feeds this alignment into
a novel transformer architecture called the Evoformer, which builds a pairwise representation:
for every pair of amino acid positions in the chain, it learns to predict the probability that
those two residues are physically close in the final structure. Third, a structure module uses
these pairwise distances to predict the actual three-dimensional coordinates of every atom
in the protein. Finally, it outputs a confidence score for each residue — a number from zero
to one hundred indicating how certain the model is about each prediction.</p>

<p>At CASP14 in December 2020, AlphaFold 2 achieved a median accuracy of 92.4 GDT — a score
so far above the second-place competitors (which scored in the 70s) that the organizers
described it as a solution to the problem. Many structures were predicted with atomic-level
accuracy indistinguishable from experimental determination. The protein folding problem —
officially — was solved.</p>

<h2>The Database That Changed Science Overnight</h2>

<p>DeepMind could have kept AlphaFold proprietary. They chose not to. In July 2021, they
released the AlphaFold Protein Structure Database in partnership with the European
Bioinformatics Institute, initially containing structures for all 20,000 proteins encoded by
the human genome, and the proteomes of twenty model organisms. In 2022 they expanded to
200 million structures — essentially every protein from every organism whose genome had been
sequenced.</p>

<p>The effect on biology was immediate and global. Within two years, more than three million
researchers in 190 countries were using the database. Over 35,000 scientific papers have
cited AlphaFold. The structures are free, downloadable, and computed. A graduate student who
would have spent a year solving one protein structure can now download a highly accurate
prediction in seconds.</p>

<p>The scope of what this enables is difficult to overstate. Drug designers can examine the
binding pockets of disease targets they could never previously visualise. Researchers in low-
and middle-income countries — who lack the expensive cryo-EM equipment required for
experimental structure determination — can now conduct structural biology on a laptop. A
researcher in Uganda, working on a potential breast cancer vaccine, described using AlphaFold
to narrow 15,000 candidate protein sites to 15 in the time it would have previously taken
to characterise a handful experimentally.</p>

<h2>AlphaFold 3: Beyond Proteins</h2>

<p>AlphaFold 2 predicted protein structures. AlphaFold 3, released in 2024, predicts
interactions between proteins, DNA, RNA, and small molecules — including drug candidates.
The architectural shift was significant: where AlphaFold 2 used a custom transformer
(the Evoformer), AlphaFold 3 uses a diffusion model, the same class of neural network that
powers image generation systems like DALL-E and Stable Diffusion. Instead of predicting
atomic coordinates directly, AlphaFold 3 learns to start from a cloud of random atomic
noise and progressively refine it into a physically plausible molecular structure.</p>

<p>For drug discovery, this is the critical extension. Most drugs are not proteins — they are
small organic molecules that bind to proteins. AlphaFold 2 told you the shape of the target.
AlphaFold 3 tells you how the target and the drug fit together. Hassabis has described this
as potentially compressing the early stages of drug discovery — which typically takes five
to ten years and costs hundreds of millions of dollars — by an order of magnitude. His
commercial vehicle for this, Isomorphic Labs, is applying AlphaFold 3 to drug pipeline
development in partnership with major pharmaceutical companies.</p>

<h2>The Democratisation of Hard Science</h2>

<p>One of Hassabis's consistent themes is democratisation. Experimental structural biology
requires equipment costing millions of dollars, expertise that takes decades to develop, and
access to synchrotrons or cryo-EM facilities that exist in perhaps fifty places on Earth.
AlphaFold runs on a laptop with an internet connection. The knowledge embedded in 3.5 billion
years of evolution, distilled into a neural network, is now accessible to any researcher
anywhere in the world who can frame a scientific question.</p>

<p>This matters most at the frontier of neglected disease. Pathogens that cause the largest
burden of disease globally — malaria, tuberculosis, schistosomiasis — have historically
received the least structural biology attention because the commercial return does not justify
the experimental investment. AlphaFold allows researchers in affected countries to work on
these proteins directly, without needing to ship samples to a facility in Europe or the
United States and wait months for results.</p>

<h2>The Nobel and What It Means</h2>

<p>In October 2024, the Royal Swedish Academy of Sciences awarded the Nobel Prize in
Chemistry to Demis Hassabis and John Jumper for AlphaFold, and to David Baker (University
of Washington) for the related work of computational protein design — using similar
techniques to design new proteins that don't exist in nature. The committee called it "a
discovery that has fundamentally changed our understanding of the relationship between amino
acid sequence and protein structure."</p>

<p>It is the first Nobel Prize awarded primarily for a machine learning system. That is
worth pausing on. The prize is not for the hardware, not for the dataset, and not for
the biology alone — it is for the architecture of a neural network and the insight that
evolutionary information could be used to train it. A piece of software, trained on
publicly available data, solved a fifty-year problem that had defeated generations of
experimental scientists.</p>

<p>Jumper has noted the strangeness of this recognition: <em>"35,000 papers cite AlphaFold.
That's the measure of it. Not that we built something impressive — but that it changed
what other people could do."</em></p>

<h2>What Comes Next</h2>

<p>Hassabis has described the protein folding result not as an endpoint but as a template.
The same framework — identify a grand challenge in science, find the data in which the
answer is implicitly encoded, build the architecture to read it — is being applied to other
problems: the prediction of gene regulatory networks, the modelling of whole-cell behaviour,
the understanding of protein dynamics rather than just static structure.</p>

<p>His broader ambition is an AI system that can function as a scientific collaborator —
not automating the craft of science but accelerating the rate of hypothesis generation and
experimental design. "We want to compress decades of scientific progress into just a few
years," he has said. Given that AlphaFold compressed fifty years of structural biology into
a prediction that runs in five minutes, there is reason to take that ambition seriously.</p>

<p>The protein folding problem was supposed to be a long way off. It wasn't. That's the
most important lesson AlphaFold teaches — not about proteins, but about the pace of change
when the right algorithm meets the right data.</p>

<p><em>Based on interviews and lectures by Demis Hassabis (Google DeepMind) and John Jumper
(Nobel Prize in Chemistry 2024), including their discussions of AlphaFold's development,
the CASP14 results, and the AlphaFold protein structure database.</em></p>
"""

ARTICLE = {
    "title": "AlphaFold: How AI Solved Biology's 50-Year Grand Challenge",
    "slug": "alphafold-protein-folding-ai",
    "summary": (
        "In 2020, DeepMind's AlphaFold predicted protein structures with atomic-level "
        "accuracy — solving a problem that had defeated structural biology for fifty years. "
        "The result: 200 million protein structures freely available to every researcher "
        "on Earth, a Nobel Prize, and a template for using AI to compress decades of "
        "scientific progress."
    ),
    "order": 1,
    "published": True,
    "content": ARTICLE_CONTENT,
}


def create_alphafold_article(apps, schema_editor):
    if apps is None:
        from topics.models import Pillar, Article
    else:
        Pillar = apps.get_model("topics", "Pillar")
        Article = apps.get_model("topics", "Article")

    dna_pillar, _ = Pillar.objects.get_or_create(
        slug=DNA_AI_PILLAR["slug"], defaults=DNA_AI_PILLAR
    )
    ai_pillar, _ = Pillar.objects.get_or_create(
        slug=AI_PILLAR["slug"], defaults=AI_PILLAR
    )

    Article.objects.get_or_create(
        slug=ARTICLE["slug"],
        defaults={**ARTICLE, "pillar": dna_pillar},
    )

    ai_slug = ARTICLE["slug"] + "-ai"
    Article.objects.get_or_create(
        slug=ai_slug,
        defaults={**ARTICLE, "pillar": ai_pillar, "slug": ai_slug},
    )


def reverse_alphafold_article(apps, schema_editor):
    Article = apps.get_model("topics", "Article")
    Article.objects.filter(
        slug__in=[ARTICLE["slug"], ARTICLE["slug"] + "-ai"]
    ).delete()


class Command(BaseCommand):
    help = "Load AlphaFold article into dna-ai-future and artificial-intelligence pillars"

    def handle(self, *args, **options):
        create_alphafold_article(None, None)
        self.stdout.write(self.style.SUCCESS("Done."))
