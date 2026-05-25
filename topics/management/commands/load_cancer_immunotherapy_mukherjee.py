from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Cancer",
    "slug": "cancer-metabolic-health",
    "description": (
        "The biology of cancer — its origins, metabolic theory, immune evasion, and the treatments rewriting oncology."
    ),
    "icon": "🔬",
    "color": "red",
    "order": 3,
}

SVG_CHECKPOINT = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 460" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diagram showing how cancer evades the immune system and how checkpoint inhibitors restore T-cell attack">
  <defs>
    <marker id="arr-b" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#60a5fa"/></marker>
    <marker id="arr-r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/></marker>
    <marker id="arr-g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4ade80"/></marker>
    <marker id="arr-y" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#facc15"/></marker>
    <radialGradient id="tcell-grad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </radialGradient>
    <radialGradient id="tcell-active-grad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#14532d"/>
      <stop offset="100%" stop-color="#052e16"/>
    </radialGradient>
    <radialGradient id="cancer-grad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4c1d1d"/>
      <stop offset="100%" stop-color="#1a0a0a"/>
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect width="720" height="460" fill="#090d1a" rx="16"/>

  <!-- Main title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700" letter-spacing="-0.2">How Cancer Hides — and How Immunotherapy Exposes It</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Synthesized from Siddhartha Mukherjee's research and talks</text>

  <!-- ─── DIVIDER LINES ─────────────────────────────────────── -->
  <line x1="243" y1="62" x2="243" y2="290" stroke="#1e293b" stroke-width="1"/>
  <line x1="477" y1="62" x2="477" y2="290" stroke="#1e293b" stroke-width="1"/>

  <!-- ─── COLUMN HEADERS ────────────────────────────────────── -->
  <rect x="10" y="62" width="228" height="24" rx="4" fill="#1e293b"/>
  <text x="124" y="78" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#94a3b8" font-weight="600">① Normal Immune Surveillance</text>

  <rect x="248" y="62" width="224" height="24" rx="4" fill="#2d1515"/>
  <text x="360" y="78" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#f87171" font-weight="600">② Cancer Flips the "Off Switch"</text>

  <rect x="482" y="62" width="228" height="24" rx="4" fill="#0d2218"/>
  <text x="596" y="78" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#4ade80" font-weight="600">③ Checkpoint Inhibitor Restores Kill</text>

  <!-- ═══════════════════════════════════════════════════════════
       COLUMN 1 — Normal immune surveillance
  ═══════════════════════════════════════════════════════════ -->
  <!-- T cell (active, green) -->
  <circle cx="90" cy="175" r="38" fill="url(#tcell-active-grad)" stroke="#22c55e" stroke-width="2"/>
  <text x="90" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac" font-weight="700">T Cell</text>
  <text x="90" y="184" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">(active)</text>

  <!-- TCR receptor stub -->
  <rect x="126" y="169" width="14" height="12" rx="3" fill="#22c55e"/>
  <text x="133" y="178" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#052e16" font-weight="700">TCR</text>

  <!-- Arrow T→C -->
  <line x1="142" y1="175" x2="168" y2="175" stroke="#4ade80" stroke-width="2" marker-end="url(#arr-g)"/>

  <!-- Cancer cell (dying, fading) -->
  <circle cx="203" cy="175" r="30" fill="url(#cancer-grad)" stroke="#f87171" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="203" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Cancer</text>
  <text x="203" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444">Cell ✕</text>

  <!-- MHC antigen on cancer -->
  <rect x="176" y="148" width="14" height="10" rx="2" fill="#b91c1c"/>
  <text x="183" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fecaca">MHC</text>

  <!-- Label -->
  <text x="124" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">T cell recognises cancer</text>
  <text x="124" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">via MHC antigen → kills it</text>

  <!-- ═══════════════════════════════════════════════════════════
       COLUMN 2 — Cancer flips the "off switch"
  ═══════════════════════════════════════════════════════════ -->
  <!-- T cell (exhausted, grey-blue) -->
  <circle cx="310" cy="175" r="38" fill="url(#tcell-grad)" stroke="#475569" stroke-width="1.5"/>
  <text x="310" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8" font-weight="700">T Cell</text>
  <text x="310" y="184" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">(exhausted)</text>

  <!-- PD-1 receptor on T cell -->
  <rect x="345" y="162" width="20" height="13" rx="3" fill="#1e40af"/>
  <text x="355" y="171" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#bfdbfe" font-weight="700">PD-1</text>

  <!-- Binding line PD-1 to PD-L1 -->
  <line x1="366" y1="168" x2="385" y2="168" stroke="#facc15" stroke-width="2.5"/>

  <!-- Cancer cell (thriving) -->
  <circle cx="420" cy="175" r="33" fill="#2d0a0a" stroke="#f87171" stroke-width="2"/>
  <text x="420" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#fca5a5" font-weight="700">Cancer</text>
  <text x="420" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#ef4444">Cell ✓</text>

  <!-- PD-L1 on cancer -->
  <rect x="383" y="162" width="22" height="13" rx="3" fill="#7f1d1d"/>
  <text x="394" y="171" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fca5a5" font-weight="700">PD-L1</text>

  <!-- "STOP" signal label on the binding -->
  <text x="376" y="156" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#facc15" font-weight="700">🔴 STOP</text>

  <!-- Labels -->
  <text x="360" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Cancer displays PD-L1 — binds</text>
  <text x="360" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">PD-1 on T cell → "stand down"</text>

  <!-- ═══════════════════════════════════════════════════════════
       COLUMN 3 — Checkpoint inhibitor frees T cell
  ═══════════════════════════════════════════════════════════ -->
  <!-- T cell (active again) -->
  <circle cx="547" cy="175" r="38" fill="url(#tcell-active-grad)" stroke="#22c55e" stroke-width="2"/>
  <text x="547" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac" font-weight="700">T Cell</text>
  <text x="547" y="184" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">(reactivated)</text>

  <!-- PD-1 blocked by antibody -->
  <rect x="580" y="162" width="20" height="13" rx="3" fill="#1e40af"/>
  <text x="590" y="171" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#bfdbfe" font-weight="700">PD-1</text>

  <!-- Antibody blocker shape (Y shape) -->
  <line x1="601" y1="168" x2="613" y2="168" stroke="#a855f7" stroke-width="2.5"/>
  <line x1="613" y1="168" x2="619" y2="160" stroke="#a855f7" stroke-width="2"/>
  <line x1="613" y1="168" x2="619" y2="176" stroke="#a855f7" stroke-width="2"/>
  <circle cx="614" cy="168" r="8" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="2 1.5"/>
  <text x="627" y="155" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#d8b4fe" font-weight="700">anti-</text>
  <text x="627" y="164" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#d8b4fe" font-weight="700">PD-1</text>
  <text x="627" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#d8b4fe" font-weight="700">drug</text>

  <!-- X blocking the PD-L1 binding -->
  <text x="638" y="172" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#4ade80" font-weight="700">✕</text>

  <!-- Cancer cell (dying) -->
  <circle cx="680" cy="175" r="30" fill="url(#cancer-grad)" stroke="#f87171" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.55"/>
  <text x="680" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Cancer</text>
  <text x="680" y="183" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444">Cell ✕</text>

  <!-- Labels -->
  <text x="596" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">Antibody drug blocks PD-1</text>
  <text x="596" y="245" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">binding → T cell kills again</text>

  <!-- ─── DIVIDER ───────────────────────────────────────────── -->
  <line x1="20" y1="300" x2="700" y2="300" stroke="#1e293b" stroke-width="1"/>

  <!-- ═══════════════════════════════════════════════════════════
       BOTTOM PANEL — CAR-T Cell Therapy
  ═══════════════════════════════════════════════════════════ -->
  <rect x="10" y="308" width="700" height="24" rx="4" fill="#1c1430"/>
  <text x="360" y="324" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#c084fc" font-weight="600">④ CAR-T Cell Therapy: Engineering the Hunter</text>

  <!-- Step 1: Extract T cells -->
  <rect x="18" y="342" width="110" height="96" rx="8" fill="#13101f" stroke="#4c1d95" stroke-width="1"/>
  <text x="73" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c084fc" font-weight="700">Step 1</text>
  <circle cx="73" cy="388" r="22" fill="#1e1035" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="73" y="384" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a78bfa">Patient</text>
  <text x="73" y="396" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a78bfa">T cells</text>
  <text x="73" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">harvested from</text>
  <text x="73" y="436" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">patient's blood</text>

  <!-- Arrow 1→2 -->
  <line x1="130" y1="390" x2="148" y2="390" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arr-b)"/>

  <!-- Step 2: Engineer CAR -->
  <rect x="150" y="342" width="110" height="96" rx="8" fill="#13101f" stroke="#4c1d95" stroke-width="1"/>
  <text x="205" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c084fc" font-weight="700">Step 2</text>
  <circle cx="205" cy="388" r="22" fill="#1e1035" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="205" y="384" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a78bfa">CAR gene</text>
  <text x="205" y="396" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a78bfa">inserted</text>
  <text x="205" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">viral vector delivers</text>
  <text x="205" y="436" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">CAR receptor gene</text>

  <!-- Arrow 2→3 -->
  <line x1="262" y1="390" x2="280" y2="390" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arr-b)"/>

  <!-- Step 3: Expand -->
  <rect x="282" y="342" width="110" height="96" rx="8" fill="#13101f" stroke="#4c1d95" stroke-width="1"/>
  <text x="337" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c084fc" font-weight="700">Step 3</text>
  <circle cx="337" cy="388" r="22" fill="#1e1035" stroke="#a855f7" stroke-width="2"/>
  <text x="337" y="384" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#d8b4fe">CAR-T</text>
  <text x="337" y="396" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#d8b4fe">expanded</text>
  <text x="337" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">billions of engineered</text>
  <text x="337" y="436" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">cells grown in lab</text>

  <!-- Arrow 3→4 -->
  <line x1="394" y1="390" x2="412" y2="390" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arr-b)"/>

  <!-- Step 4: Infuse back -->
  <rect x="414" y="342" width="110" height="96" rx="8" fill="#13101f" stroke="#4c1d95" stroke-width="1"/>
  <text x="469" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#c084fc" font-weight="700">Step 4</text>
  <circle cx="469" cy="388" r="22" fill="#1e1035" stroke="#a855f7" stroke-width="2"/>
  <text x="469" y="384" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#d8b4fe">infused</text>
  <text x="469" y="396" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#d8b4fe">into patient</text>
  <text x="469" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">IV infusion into</text>
  <text x="469" y="436" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">patient's bloodstream</text>

  <!-- Arrow 4→5 -->
  <line x1="526" y1="390" x2="544" y2="390" stroke="#4ade80" stroke-width="1.5" marker-end="url(#arr-g)"/>

  <!-- Step 5: Kill cancer -->
  <rect x="546" y="342" width="162" height="96" rx="8" fill="#052e16" stroke="#16a34a" stroke-width="1.5"/>
  <text x="627" y="358" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80" font-weight="700">Step 5 — Targeted Kill</text>
  <circle cx="595" cy="392" r="22" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
  <text x="595" y="388" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac" font-weight="700">CAR-T</text>
  <text x="595" y="400" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#86efac">locks on</text>
  <line x1="617" y1="390" x2="633" y2="390" stroke="#4ade80" stroke-width="2" marker-end="url(#arr-g)"/>
  <circle cx="657" cy="392" r="20" fill="#1a0a0a" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3 2" opacity="0.6"/>
  <text x="657" y="388" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">Cancer</text>
  <text x="657" y="400" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444">✕</text>
  <text x="627" y="428" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">CAR binds antigen → kills</text>
  <text x="627" y="438" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">cancer without MHC needed</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">Checkpoint inhibitors (nivolumab, pembrolizumab, ipilimumab) release the immune brake; CAR-T cells are engineered to hunt without it.</figcaption>
</figure>"""

ARTICLE_BODY = """<p class="lead">For most of the twentieth century, oncologists fought cancer the way armies fought World War I: with poisons, radiation, and blunt instruments, hoping to destroy the enemy before destroying the patient. Then, in a series of slow discoveries spanning forty years, a different idea took hold — one that did not ask how to kill cancer but asked instead: <em>why isn't the body already killing it?</em></p>

<p>The answer, when it came, was startling. The immune system <em>can</em> kill cancer. In most people, it does so constantly, destroying aberrant cells before they take root. The problem is that cancer, as Siddhartha Mukherjee puts it, is "an astonishing perversion of the normal cell" — one so successful at exploiting the body's own machinery that it has learned, among other tricks, to impersonate the signals of restraint that the immune system uses to prevent it from attacking healthy tissue. Cancer doesn't just evade the immune system. It <em>subverts</em> it.</p>

<h2>The Emperor's Old Trick</h2>

<p>Mukherjee — oncologist, cell biologist, Columbia professor, and author of <em>The Emperor of All Maladies</em> — has a DPhil in immunology from Oxford. He spent years studying how the immune system tells friend from foe, and why that discrimination sometimes fails. That background makes him unusually well-placed to explain why immunotherapy is not merely a new class of drugs but a conceptual revolution.</p>

<p>The core problem, he explains, is the checkpoint. The immune system runs on a series of molecular brakes — proteins that tell activated immune cells to stand down, to prevent them from turning on the body's own tissues. These are not design flaws; they are essential safety mechanisms. Without them, autoimmune disease is the result. The brakes have names: CTLA-4, PD-1, PD-L1. They sit on the surface of T cells and on the cells they interact with, forming handshakes that signal "this is self — do not attack."</p>

<p>Cancer learned to speak that language.</p>

<p>A tumour that upregulates PD-L1 on its surface can grab hold of PD-1 on approaching T cells and deliver the "stand down" signal. The T cell, receiving a message it was built to obey, disengages. It doesn't die; it exhausts, entering a state of immunological paralysis. The cancer grows undisturbed, wearing the body's own safety signals as camouflage.</p>

<h2>Releasing the Brakes</h2>

""" + SVG_CHECKPOINT + """

<p>The story of checkpoint inhibition begins with James Allison at the University of Texas, who spent years trying to convince a sceptical oncology community that blocking CTLA-4 — one of the first known immune brakes — could treat cancer. His drug, ipilimumab, was approved by the FDA in 2011 for metastatic melanoma. The field shifted.</p>

<p>What followed was a rapid expansion of targets. PD-1 and its ligand PD-L1 proved even more tractable. Nivolumab (anti-PD-1) and pembrolizumab (anti-PD-1) were approved in quick succession across an expanding list of cancers: melanoma, lung, kidney, bladder, head and neck, Hodgkin's lymphoma. Atezolizumab targeted PD-L1 directly, blocking the cancer-side of the handshake instead of the T cell side.</p>

<p>The results, in patients who respond, are unlike anything in oncology's history. Metastatic melanoma — which killed nearly everyone within a year in the 1970s — now has a substantial fraction of patients alive at five and ten years. Some appear cured, though oncologists use that word with characteristic caution. The response is not universal: roughly 20–40% of patients with many tumour types respond meaningfully to checkpoint blockade. The question of who responds, and why, is one of the most active areas of cancer research.</p>

<p>Mukherjee is careful to frame this uncertainty in human terms. He describes standing with medical students in the oncology ward, looking at a patient with metastatic melanoma, and explaining that she might be in the 15% who survive long-term — or she might not. There is, for now, no reliable way to know in advance. This is not a failure of the drugs; it is the frontier where the science currently lives.</p>

<h2>The CAR-T Revolution</h2>

<p>If checkpoint inhibitors remove the brakes, CAR-T therapy rebuilds the engine.</p>

<p>Chimeric antigen receptor T cells — CAR-T cells — are the patient's own immune cells, extracted, genetically reprogrammed in the laboratory to target a specific cancer antigen, expanded into billions, and reinfused. The work was pioneered by Carl June at the University of Pennsylvania and others who spent decades refining the viral delivery of the CAR gene, the expansion protocols, and the management of the extraordinary toxicities that can result when billions of armed T cells flood into a tumour-bearing body.</p>

<p>The clinical results in blood cancers — acute lymphoblastic leukaemia (ALL), diffuse large B-cell lymphoma, multiple myeloma — have been, in some patients, dramatic. Children with relapsed ALL, for whom every other option had failed, entered remission. Some stayed there. These are patients who, a generation ago, would have had no realistic prospect of survival.</p>

<p>Mukherjee is not a bystander to this work. He co-founded Immuneel Therapeutics in Bangalore in collaboration with Kiran Mazumdar-Shaw, with the explicit goal of conducting CAR-T clinical trials designed to reduce the cost of the therapy for patients in India and the developing world — where a treatment costing $400,000 per infusion is effectively nonexistent. His lab at Columbia is working on the next generation: solid tumour CAR-T, which remains far harder than blood cancer because solid tumours create hostile microenvironments that exhaust and exclude infiltrating T cells.</p>

<h2>Cancer as a Successful Parasite</h2>

<p>Mukherjee's framing of cancer immunotherapy carries his broader intellectual signature. He does not treat immunotherapy as a triumph to be celebrated cleanly. He treats it as a clarification — a new angle from which the fundamental problem of cancer becomes sharper and more demanding.</p>

<p>Cancer succeeds, he argues, because it is not alien. It is self. A cancer cell, at its origin, was a normal cell that accumulated the right (or wrong) combination of mutations to break free of the regulatory circuits governing growth, death, and identity. What it uses to survive — growth signals, evasion mechanisms, the ability to recruit blood supply and suppress immune recognition — is the same toolkit the body uses for legitimate purposes. The immune system, having evolved to distinguish self from non-self, is badly equipped to deal with an enemy that is genuinely both.</p>

<p>Immunotherapy works, when it works, by tilting that balance. Tumours accumulate mutations, and some of those mutations produce neoantigens — protein fragments that are sufficiently different from normal self that, if the immune system were paying full attention, it would recognise them. The checkpoint inhibitors restore that attention. They do not create a new immune response; they remove the suppression of one that was already there, waiting.</p>

<h2>What Comes Next</h2>

<p>The open problems are the ones Mukherjee finds most interesting, and most honest to describe.</p>

<p>Solid tumour CAR-T remains the hard frontier. Blood cancers work because T cells can circulate and reach their targets. Solid tumours — pancreatic cancer, glioblastoma, ovarian cancer — build barricades: a suppressive microenvironment that excludes and exhausts T cells before they reach the tumour core. Solving this requires not just better receptors but better understanding of how tumours co-opt the surrounding stroma, blood vessels, and immune architecture to protect themselves.</p>

<p>Combination therapies — checkpoint inhibitors plus chemotherapy, plus targeted therapy, plus CAR-T — are multiplying faster than our ability to understand their interactions. The signal in any individual combination trial is often confounded by the complexity of what the drugs are doing simultaneously.</p>

<p>Tumour heterogeneity compounds everything. A single tumour may contain many distinct cell populations, each with different mutation profiles, different antigen expression, different susceptibility to immune attack. A therapy that clears 99% of cells but leaves one resistant subclone will fail. This is not a theoretical concern; it is the pattern of relapse that oncologists observe constantly.</p>

<p>And cost. Mukherjee returns to this with the insistence of someone who has thought hard about who gets to benefit from a revolution. CAR-T therapy, at current prices, is available to a vanishingly small fraction of the world's cancer patients. Checkpoint inhibitors are cheaper but still out of reach for most. The science is advancing faster than the delivery mechanisms. Immuneel, his Indian venture, is a bet that manufacturing and trial costs can be reduced enough to change that equation — but it remains a bet.</p>

<h2>The Long Arc</h2>

<p>Mukherjee keeps a long lens on cancer history. He begins <em>The Emperor of All Maladies</em> with the Edwin Smith Papyrus, an Egyptian medical document from roughly 1600 BCE, which describes breast cancer and notes of it, plainly, that there is no treatment. He ends the book in a different register — not triumphalism, but the recognition that the arc of cancer medicine, measured across centuries, has been one of slow, hard-won, sometimes reversible progress.</p>

<p>Acute lymphoblastic leukaemia in children went from 100% mortality in 1947 to 90% survival today. Melanoma went from a near-universal death sentence to a disease with meaningful long-term survivors. The progress is real. The uncertainty about any individual patient remains profound.</p>

<p>What immunotherapy adds to that arc is a new and finally coherent theory: that cancer is not, at bottom, a problem of chemistry or radiation tolerance, but of recognition. The immune system is the body's most sophisticated surveillance apparatus. Cancer's greatest trick has been to become invisible to it. The task of the next generation of cancer medicine — checkpoint inhibitors, CAR-T, cancer vaccines, bispecific antibodies, tumour microenvironment engineering — is to make it visible again.</p>

<p style="color:#64748b;font-size:0.9rem;margin-top:2em;border-top:1px solid #1e293b;padding-top:1em;">Synthesized from Siddhartha Mukherjee's lectures, interviews, and research — including NHGRI oral history, Columbia Grand Rounds, the Weizmann Global Gathering, and <em>The Emperor of All Maladies</em>, <em>The Gene</em>, and <em>The Song of the Cell</em>.</p>"""

ARTICLE = {
    "title": "Cancer Immunotherapy: How the Body Learned to Fight Back",
    "slug": "cancer-immunotherapy-mukherjee",
    "summary": "Checkpoint inhibitors, CAR-T cells, and the long story of teaching the immune system to see what cancer made invisible.",
    "content": ARTICLE_BODY,
    "published": True,
    "order": 2,
}


class Command(BaseCommand):
    help = "Load cancer immunotherapy article (Siddhartha Mukherjee) into life-of-a-cell pillar"

    def handle(self, *args, **kwargs):
        pillar, created = Pillar.objects.get_or_create(
            slug=PILLAR["slug"],
            defaults={k: v for k, v in PILLAR.items() if k != "slug"},
        )
        if created:
            self.stdout.write(f"Created pillar: {pillar.name}")
        else:
            self.stdout.write(f"Pillar exists: {pillar.name}")

        article, created = Article.objects.update_or_create(
            slug=ARTICLE["slug"],
            defaults={
                "pillar": pillar,
                "title": ARTICLE["title"],
                "summary": ARTICLE["summary"],
                "content": ARTICLE["content"],
                "published": ARTICLE["published"],
                "order": ARTICLE["order"],
            },
        )
        verb = "Created" if created else "Updated"
        self.stdout.write(f"{verb} article: {article.title}")
        self.stdout.write("Done.")
