from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Life of a Cell",
    "slug": "life-of-a-cell",
    "description": (
        "How cells — the fundamental units of life — arise, specialize, renew, and fail. "
        "Exploring stem cell biology, cellular aging, gene editing, and the frontier of cellular medicine."
    ),
    "icon": "🧬",
    "color": "blue",
    "order": 7,
}

SVG_ILLUSTRATION = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diagram showing stem cell hierarchy and key technologies">
  <defs>
    <marker id="sc-arr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#60a5fa"/>
    </marker>
    <radialGradient id="cellGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e40af" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.4"/>
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="32" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700" letter-spacing="-0.2">Stem Cell Hierarchy &amp; Technologies</text>
  <text x="360" y="50" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Synthesized from Siddhartha Mukherjee's research and talks</text>

  <!-- ROOT: Pluripotent Stem Cell (top center) -->
  <circle cx="360" cy="110" r="44" fill="url(#cellGrad)" stroke="#3b82f6" stroke-width="2"/>
  <text x="360" y="104" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#93c5fd" font-weight="700">Pluripotent</text>
  <text x="360" y="118" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#93c5fd" font-weight="700">Stem Cell</text>
  <text x="360" y="132" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#60a5fa">(self-renewing)</text>

  <!-- Arrow left to Hematopoietic -->
  <line x1="322" y1="138" x2="218" y2="195" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#sc-arr)"/>
  <!-- Arrow center to Skeletal -->
  <line x1="360" y1="154" x2="360" y2="205" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#sc-arr)"/>
  <!-- Arrow right to Neural -->
  <line x1="398" y1="138" x2="500" y2="195" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#sc-arr)"/>

  <!-- Hematopoietic Stem Cell (left) -->
  <circle cx="195" cy="225" r="38" fill="#172033" stroke="#22d3ee" stroke-width="1.5"/>
  <text x="195" y="219" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="700">Hematopoietic</text>
  <text x="195" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="700">Stem Cell</text>
  <text x="195" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">(blood system)</text>

  <!-- Skeletal Stem Cell (center) -->
  <circle cx="360" cy="240" r="38" fill="#172033" stroke="#a78bfa" stroke-width="1.5"/>
  <text x="360" y="234" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c4b5fd" font-weight="700">Skeletal</text>
  <text x="360" y="247" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c4b5fd" font-weight="700">Stem Cell</text>
  <text x="360" y="260" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">(bone · cartilage)</text>

  <!-- Neural Stem Cell (right) -->
  <circle cx="525" cy="225" r="38" fill="#172033" stroke="#34d399" stroke-width="1.5"/>
  <text x="525" y="219" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#6ee7b7" font-weight="700">Neural</text>
  <text x="525" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#6ee7b7" font-weight="700">Stem Cell</text>
  <text x="525" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">(nervous system)</text>

  <!-- Technologies panel at bottom -->
  <rect x="30" y="295" width="660" height="110" rx="10" fill="#0f172a" stroke="#1e3a5f" stroke-width="1"/>
  <text x="360" y="316" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#94a3b8" font-weight="700" letter-spacing="0.5">KEY TECHNOLOGIES</text>

  <!-- Tech 1 -->
  <rect x="50" y="326" width="140" height="64" rx="7" fill="#172033" stroke="#1d4ed8" stroke-width="1"/>
  <text x="120" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#93c5fd" font-weight="700">Bone Marrow</text>
  <text x="120" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#93c5fd" font-weight="700">Transplant</text>
  <text x="120" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Standard of care</text>
  <text x="120" y="382" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">leukemia · sickle cell</text>

  <!-- Tech 2 -->
  <rect x="205" y="326" width="140" height="64" rx="7" fill="#172033" stroke="#7c3aed" stroke-width="1"/>
  <text x="275" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c4b5fd" font-weight="700">CRISPR Stem</text>
  <text x="275" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c4b5fd" font-weight="700">Cell Editing</text>
  <text x="275" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Delete CD33/CLL1</text>
  <text x="275" y="382" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">VOR platform · Phase I</text>

  <!-- Tech 3 -->
  <rect x="360" y="326" width="140" height="64" rx="7" fill="#172033" stroke="#0e7490" stroke-width="1"/>
  <text x="430" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="700">CAR-T +</text>
  <text x="430" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#67e8f9" font-weight="700">Edited Graft</text>
  <text x="430" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Immune attack on</text>
  <text x="430" y="382" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">cancer, not graft</text>

  <!-- Tech 4 -->
  <rect x="515" y="326" width="140" height="64" rx="7" fill="#172033" stroke="#047857" stroke-width="1"/>
  <text x="585" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#6ee7b7" font-weight="700">iPSC</text>
  <text x="585" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#6ee7b7" font-weight="700">Reprogramming</text>
  <text x="585" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Adult cell → stem cell</text>
  <text x="585" y="382" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">drug testing · therapy</text>
</svg>
<figcaption style="font-size:0.82em;color:#64748b;text-align:center;margin-top:0.6em;">Stem cell lineage hierarchy and the four major clinical technologies discussed by Dr. Mukherjee</figcaption>
</figure>
"""

ARTICLE_CONTENT = """
<p class="lead">The gene is lifeless — it is only code. The cell is what brings it to life. And within that
cellular world, stem cells are the master architects: self-renewing, capable of generating entire
tissues from a single founder. Understanding how they arise — and how we now engineer them — is
the frontier of modern medicine.</p>

""" + SVG_ILLUSTRATION + """

<h2>What a Stem Cell Actually Is</h2>

<p>A stem cell has two defining properties. First, it can copy itself indefinitely —
<em>self-renewal</em>. Second, it can give rise to more specialized daughters —
<em>differentiation</em>. Together, these two abilities make stem cells the maintenance
crew for every tissue that wears out.</p>

<p>They exist across virtually every organ system:</p>

<ul>
  <li><strong>Hematopoietic (blood) stem cells</strong> — continuously generate red cells, platelets,
  neutrophils, macrophages, and lymphocytes from a common ancestor in the bone marrow</li>
  <li><strong>Skeletal stem cells</strong> — resident inside bone, they build and repair bone,
  cartilage, and connective tissue</li>
  <li><strong>Neural stem cells</strong> — maintain neuronal populations in the nervous system</li>
  <li><strong>Tissue-specific stem cells</strong> in skin, gut, pancreas, and other organs
  that turn over constantly</li>
</ul>

<h2>How Stem Cells Arise</h2>

<h3>Embryonic Commitment</h3>

<p>During development, pluripotent embryonic cells progressively narrow their fate. Transcription
factors act as molecular switches — once flipped, they lock a cell into a lineage. A pluripotent
cell becomes multipotent, then lineage-restricted, then fully specialized. The stem cells that
persist into adult life are those that retained the self-renewal switch while committing to a
particular tissue.</p>

<h3>The Skeletal Stem Cell: A Recent Discovery</h3>

<p>One of the most striking recent findings came from Dr. Mukherjee's own lab: the identification
of a true <strong>skeletal stem cell</strong> that builds the entire vertebrate skeleton. These
cells were discovered only a few years ago and have four remarkable properties:</p>

<ol>
  <li><strong>Hierarchical potency</strong> — a single cell generates columns of bone,
  cartilage, and fibrous tissue</li>
  <li><strong>Fracture repair</strong> — they behave like cellular glue, flooding the site
  of a bone break, repairing it locally, then stopping</li>
  <li><strong>Self-renewal</strong> — they persist and regenerate</li>
  <li><strong>Age-dependent decline</strong> — their numbers fall 10–50-fold as an organism ages,
  which Mukherjee believes is the cellular basis of arthritis and bone fragility</li>
</ol>

<blockquote>
  <p>"We were looking for a pill when we should have really been looking for a cell."</p>
  <footer>— Siddhartha Mukherjee, on the search for arthritis treatments</footer>
</blockquote>

<p>His lab is now studying centenarians to ask what is different about the skeletal stem cells in
people with exceptional longevity — and working to reintroduce these cells into humans as
a therapeutic strategy.</p>

<h3>Cancer as Stem Cell Biology Gone Wrong</h3>

<p>Mukherjee frames cancer not as alien biology but as normal stem cell biology perverted.
The genes that drive wound healing, embryonic growth, and stem cell self-renewal — when mutated —
release uncontrolled proliferation. This means normality and illness are structurally twinned.
Cancer cells exploit the very machinery that allows a stem cell to be a stem cell.</p>

<p>Two active questions define this intersection:</p>
<ul>
  <li>Do cancers contain a hierarchy of <em>cancer stem cells</em> that drive relapse and
  resistance, recapitulating self-renewal?</li>
  <li>Can healthy stem cells be used <em>therapeutically</em> against cancer — and can we
  engineer them to survive the attack?</li>
</ul>

<h2>Technologies That Generate or Engineer Stem Cells</h2>

<h3>1. Bone Marrow Transplantation</h3>

<p>The oldest proven stem cell technology. Donor hematopoietic stem cells repopulate an
entire blood system after conditioning chemotherapy. It remains standard of care for leukemia
and lymphoma. It also enables gene therapy: an autologous bone marrow transplant with a corrected
gene can cure sickle cell anemia without any germ-line modification.</p>

<h3>2. Cord Blood Stem Cells</h3>

<p>Umbilical cord blood is a rich source of hematopoietic stem cells. Mukherjee's team has
achieved <strong>90% genetic modification rates</strong> in cord blood-derived cells — making
them an efficient platform for CRISPR-based interventions.</p>

<h3>3. CRISPR Editing of Hematopoietic Stem Cells — The VOR Platform</h3>

<p>The central problem in using CAR-T cells against AML (acute myeloid leukemia) is antigen
sharing: the target (CD33) is present on both leukemia cells <em>and</em> normal blood stem
cells. CAR-T kills both, preventing engraftment.</p>

<p>Mukherjee's solution — now in Phase I clinical trials — is to edit the stem cells before
transplant:</p>

<ol>
  <li>Collect donor CD34+ hematopoietic stem/progenitor cells</li>
  <li>Use CRISPR to delete CD33 (and/or CLL1) from those cells</li>
  <li>Transplant the antigen-negative edited cells into the patient</li>
  <li>Now CAR-T cells or the antibody-toxin Mylotarg can attack residual leukemia —
  but the edited graft is invisible to them</li>
</ol>

<p>Early trial results show the edited cells constituting <strong>90–96% of reconstituted
blood</strong> at day 60, with normal recovery trajectories. The company built to manufacture
these cells at scale is <strong>Vor Biopharma</strong>.</p>

<h3>4. Base Editing</h3>

<p>Beyond standard CRISPR cutting, Mukherjee's lab has demonstrated <strong>dual base
editing</strong> — chemically converting individual DNA bases (A→G or C→T) without making
double-strand breaks, allowing simultaneous deletion of two antigens. The challenge is that
longer culture time degrades stem cell potency — the lab identified a "golden lock spot"
window in which dual editing can be completed while cells remain viable.</p>

<h3>5. Induced Pluripotent Stem Cells (iPSC)</h3>

<p>By expressing a set of reprogramming factors, ordinary adult cells can be converted back
into pluripotent stem cells. These patient-derived iPSCs can then be differentiated into
virtually any cell type, used for drug screening, or re-engineered for transplant. Mukherjee
describes this not as a future possibility but as ongoing work.</p>

<h3>6. CAR-T Combined with Edited Stem Cells</h3>

<p>The combination of CRISPR-edited hematopoietic stem cells with CAR-T immunotherapy is
Mukherjee's most advanced clinical program. In India, he co-founded <strong>ImmunACT</strong>
with entrepreneur Kiran Mazumdar-Shaw to bring CAR-T therapy from roughly $1 million per
patient down to $20,000–40,000 — comparable to the cost of a bone marrow transplant in India.</p>

<h2>Why Stem Cell Numbers Matter for Aging</h2>

<p>Perhaps the most consequential insight from stem cell biology is this: aging may be, in
large part, a stem cell exhaustion problem.</p>

<ul>
  <li>Skeletal stem cells decline 10–50-fold with age → arthritis, fractures, poor healing</li>
  <li>Hematopoietic stem cells that fail → anemia, immune collapse</li>
  <li>Neural stem cell depletion → diminished neuronal renewal</li>
</ul>

<blockquote>
  <p>"How do we keep our blood system regeneratively alive? It becomes a stem cell problem.
  It's a cellular problem at that stage."</p>
  <footer>— Siddhartha Mukherjee</footer>
</blockquote>

<p>The question Mukherjee's lab is now asking in centenarian studies: what is different about
the stem cells of people who live to 100 with intact cognition and skeletal function? The
answer may reveal the biology of healthy aging — and the targets that could extend it.</p>

<h2>Summary: From Bench to Clinic</h2>

<table style="width:100%;border-collapse:collapse;font-size:0.9em;margin-top:1em;">
  <thead>
    <tr style="background:#1e293b;">
      <th style="padding:8px 12px;text-align:left;border-bottom:1px solid #334155;">Technology</th>
      <th style="padding:8px 12px;text-align:left;border-bottom:1px solid #334155;">What It Does</th>
      <th style="padding:8px 12px;text-align:left;border-bottom:1px solid #334155;">Stage</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:8px 12px;">Bone marrow transplant</td>
      <td style="padding:8px 12px;">Replace diseased blood stem cells with donor cells</td>
      <td style="padding:8px 12px;color:#4ade80;">Standard of care</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;background:#0f172a;">
      <td style="padding:8px 12px;">Cord blood stem cells</td>
      <td style="padding:8px 12px;">Pluripotent source; ~90% CRISPR edit efficiency</td>
      <td style="padding:8px 12px;color:#4ade80;">Clinical</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:8px 12px;">CRISPR antigen deletion (CD33/CLL1)</td>
      <td style="padding:8px 12px;">Makes stem cell graft invisible to CAR-T</td>
      <td style="padding:8px 12px;color:#facc15;">Phase I</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;background:#0f172a;">
      <td style="padding:8px 12px;">Base editing</td>
      <td style="padding:8px 12px;">Dual antigen deletion without DNA cuts</td>
      <td style="padding:8px 12px;color:#facc15;">Phase I</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:8px 12px;">CAR-T + edited stem graft</td>
      <td style="padding:8px 12px;">Combined leukemia eradication + graft protection</td>
      <td style="padding:8px 12px;color:#facc15;">Phase I</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;background:#0f172a;">
      <td style="padding:8px 12px;">iPSC reprogramming</td>
      <td style="padding:8px 12px;">Patient-derived pluripotent cells for therapy/screening</td>
      <td style="padding:8px 12px;color:#60a5fa;">Early clinical</td>
    </tr>
    <tr>
      <td style="padding:8px 12px;">Gene therapy via BMT</td>
      <td style="padding:8px 12px;">Correct genetic defect in autologous stem cells (sickle cell)</td>
      <td style="padding:8px 12px;color:#4ade80;">Approved</td>
    </tr>
  </tbody>
</table>
"""


def create_stemcell_article(apps=None, schema_editor=None):
    if apps:
        PillarModel = apps.get_model('topics', 'Pillar')
        ArticleModel = apps.get_model('topics', 'Article')
    else:
        PillarModel = Pillar
        ArticleModel = Article

    biology_pillar, _ = PillarModel.objects.get_or_create(
        slug="biology",
        defaults={
            "name": "Cancer Biology",
            "description": "The biology of cancer and cellular disease.",
            "icon": "🔬",
            "color": "teal",
            "order": 6,
        },
    )

    ArticleModel.objects.update_or_create(
        slug="stem-cells-how-they-arise",
        defaults={
            "title": "Stem Cells: How They Arise and the Technologies That Harness Them",
            "summary": (
                "Siddhartha Mukherjee explains how stem cells originate in every tissue, "
                "why their numbers decline with age, and how CRISPR editing, CAR-T therapy, "
                "and bone marrow transplantation are transforming cellular medicine."
            ),
            "content": ARTICLE_CONTENT,
            "pillar": biology_pillar,
            "order": 5,
            "published": True,
            "ai_summary": (
                "Covers stem cell biology (hematopoietic, skeletal, neural), "
                "Mukherjee's discovery of skeletal stem cells, and the full technology "
                "stack: bone marrow transplant, cord blood, CRISPR/VOR platform, "
                "base editing, CAR-T + edited graft, iPSC reprogramming."
            ),
        },
    )


def reverse_stemcell_article(apps, schema_editor):
    ArticleModel = apps.get_model('topics', 'Article')
    ArticleModel.objects.filter(slug="stem-cells-how-they-arise").delete()


class Command(BaseCommand):
    help = "Load stem cell article under biology pillar (from Siddhartha Mukherjee talks)"

    def handle(self, *args, **options):
        create_stemcell_article()
        self.stdout.write(self.style.SUCCESS("Done."))
