from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

# ── SVG 1: Insulin Inactivity vs Injection ────────────────────────────────────

SVG_INSULIN = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Three panels showing how insulin works in a healthy cell, fails in Type 2 diabetes, and how insulin injection restores glucose uptake">
  <defs>
    <radialGradient id="ins-cell-healthy" cx="50%" cy="45%" r="58%">
      <stop offset="0%" stop-color="#0d2535"/>
      <stop offset="100%" stop-color="#060f18"/>
    </radialGradient>
    <radialGradient id="ins-cell-t2d" cx="50%" cy="45%" r="58%">
      <stop offset="0%" stop-color="#1a1008"/>
      <stop offset="100%" stop-color="#0d0804"/>
    </radialGradient>
    <radialGradient id="ins-cell-inject" cx="50%" cy="45%" r="58%">
      <stop offset="0%" stop-color="#0d2018"/>
      <stop offset="100%" stop-color="#060f0a"/>
    </radialGradient>
    <radialGradient id="ins-gluc" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#fcd34d"/>
      <stop offset="100%" stop-color="#d97706"/>
    </radialGradient>
    <radialGradient id="ins-mol" cx="35%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </radialGradient>
    <radialGradient id="ins-mol-grey" cx="35%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#4b5563"/>
      <stop offset="100%" stop-color="#1f2937"/>
    </radialGradient>
    <marker id="ins-arr-g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4ade80"/></marker>
    <marker id="ins-arr-y" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#fbbf24"/></marker>
    <marker id="ins-arr-r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/></marker>
    <marker id="ins-arr-b" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#60a5fa"/></marker>
    <filter id="ins-glow-g">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="ins-glow-r">
      <feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="760" height="460" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="380" y="26" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Insulin and the Cell: From Resistance to Restoration</text>
  <text x="380" y="43" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">How insulin unlocks glucose uptake — and what happens when the lock stops working</text>

  <!-- Column dividers -->
  <line x1="252" y1="54" x2="252" y2="448" stroke="#1e293b" stroke-width="1"/>
  <line x1="506" y1="54" x2="506" y2="448" stroke="#1e293b" stroke-width="1"/>

  <!-- ══ PANEL HEADERS ══ -->
  <rect x="6"   y="54" width="240" height="24" rx="4" fill="#0a2218"/>
  <text x="126" y="70" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#4ade80" font-weight="700">Healthy Cell</text>

  <rect x="258" y="54" width="242" height="24" rx="4" fill="#220e06"/>
  <text x="379" y="70" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#fb923c" font-weight="700">Type 2 Diabetes — Insulin Resistance</text>

  <rect x="512" y="54" width="242" height="24" rx="4" fill="#0a1f14"/>
  <text x="633" y="70" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#34d399" font-weight="700">After Insulin Injection</text>

  <!-- ══════════════════════════════════════════════
       PANEL 1 — HEALTHY CELL
  ══════════════════════════════════════════════ -->

  <!-- Cell membrane -->
  <ellipse cx="126" cy="280" rx="112" ry="130" fill="url(#ins-cell-healthy)" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>

  <!-- Glucose molecules floating outside (top) -->
  <circle cx="68"  cy="105" r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="68"  y="109" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="126" cy="97"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="126" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="184" cy="105" r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="184" y="109" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>

  <!-- Insulin molecule (hexagon shape) at receptor -->
  <polygon points="126,120 140,128 140,144 126,152 112,144 112,128" fill="url(#ins-mol)" stroke="#818cf8" stroke-width="1.2"/>
  <text x="126" y="140" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#e0e7ff" font-weight="700">INS</text>

  <!-- Receptor (Y-shape on membrane) -->
  <line x1="126" y1="152" x2="126" y2="166" stroke="#22c55e" stroke-width="2.5"/>
  <line x1="126" y1="166" x2="112" y2="180" stroke="#22c55e" stroke-width="2.5"/>
  <line x1="126" y1="166" x2="140" y2="180" stroke="#22c55e" stroke-width="2.5"/>
  <!-- Receptor transmembrane -->
  <rect x="120" y="180" width="12" height="20" rx="3" fill="#22c55e" opacity="0.8"/>
  <!-- GLUT4 transporter (open) -->
  <rect x="108" y="194" width="36" height="16" rx="5" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
  <text x="126" y="206" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#86efac" font-weight="700">GLUT4 ▼ OPEN</text>

  <!-- Glucose entering cell -->
  <circle cx="126" cy="228" r="9" fill="url(#ins-gluc)" filter="url(#ins-glow-g)" opacity="0.95"/>
  <text x="126" y="232" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <line x1="126" y1="212" x2="126" y2="220" stroke="#fbbf24" stroke-width="2" marker-end="url(#ins-arr-y)"/>

  <!-- Glucose inside cell (energized) -->
  <circle cx="90"  cy="280" r="8" fill="url(#ins-gluc)" opacity="0.8"/>
  <text x="90"  y="284" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <circle cx="126" cy="300" r="8" fill="url(#ins-gluc)" opacity="0.8"/>
  <text x="126" y="304" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <circle cx="160" cy="275" r="8" fill="url(#ins-gluc)" opacity="0.8"/>
  <text x="160" y="279" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <!-- ATP produced -->
  <rect x="100" y="322" width="52" height="18" rx="4" fill="#14532d" stroke="#22c55e" stroke-width="1"/>
  <text x="126" y="334" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80" font-weight="700">⚡ ATP made</text>

  <!-- Labels healthy -->
  <text x="126" y="130" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#818cf8">insulin binds</text>
  <text x="126" y="415" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80" font-weight="600">Cell fuelled ✓</text>
  <text x="126" y="428" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#475569">Glucose enters freely</text>

  <!-- ══════════════════════════════════════════════
       PANEL 2 — TYPE 2 DIABETES
  ══════════════════════════════════════════════ -->

  <!-- Cell membrane (dull orange tint) -->
  <ellipse cx="379" cy="280" rx="112" ry="130" fill="url(#ins-cell-t2d)" stroke="#f97316" stroke-width="1.5" opacity="0.9"/>

  <!-- Blood glucose — piling up outside (many dots) -->
  <circle cx="310" cy="100" r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="310" y="104" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="330" cy="88"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="330" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="354" cy="97"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="354" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="379" cy="90"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="379" y="94" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="404" cy="97"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="404" y="101" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="428" cy="88"  r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="428" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <circle cx="448" cy="100" r="9" fill="url(#ins-gluc)" opacity="0.9"/>
  <text x="448" y="104" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <!-- "High blood glucose" label -->
  <rect x="330" y="110" width="100" height="16" rx="3" fill="#450a03" stroke="#f97316" stroke-width="1"/>
  <text x="380" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fb923c" font-weight="700">↑ High blood glucose</text>

  <!-- Insulin molecule present but BLOCKED -->
  <polygon points="379,138 393,146 393,162 379,170 365,162 365,146" fill="url(#ins-mol-grey)" stroke="#6b7280" stroke-width="1.2"/>
  <text x="379" y="158" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#9ca3af" font-weight="700">INS</text>

  <!-- Blocked receptor (X mark) -->
  <line x1="379" y1="170" x2="379" y2="184" stroke="#f97316" stroke-width="2" stroke-dasharray="3 2"/>
  <line x1="369" y1="184" x2="389" y2="198" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="389" y1="184" x2="369" y2="198" stroke="#ef4444" stroke-width="2.5"/>
  <!-- Blocked receptor body -->
  <rect x="370" y="198" width="18" height="14" rx="3" fill="#374151" stroke="#6b7280" stroke-width="1"/>
  <!-- GLUT4 closed -->
  <rect x="360" y="206" width="38" height="14" rx="5" fill="#1c1008" stroke="#6b7280" stroke-width="1.2"/>
  <text x="379" y="217" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#6b7280" font-weight="700">GLUT4 ✕ CLOSED</text>

  <!-- No glucose entering — blocked arrow -->
  <line x1="379" y1="222" x2="379" y2="238" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4 3"/>
  <!-- Cross over the arrow -->
  <line x1="372" y1="227" x2="386" y2="237" stroke="#ef4444" stroke-width="2"/>
  <line x1="386" y1="227" x2="372" y2="237" stroke="#ef4444" stroke-width="2"/>

  <!-- Cell interior — depleted, empty, dim -->
  <text x="379" y="285" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#6b7280">— depleted —</text>
  <text x="379" y="300" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#4b5563">no glucose inside</text>
  <!-- Fatigue icon (ZZZ) -->
  <text x="379" y="330" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" fill="#374151" opacity="0.6">💤</text>

  <!-- Insulin resistance callout -->
  <rect x="270" y="148" width="70" height="26" rx="4" fill="#1a0a00" stroke="#f97316" stroke-width="1"/>
  <text x="305" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fb923c" font-weight="700">Receptor</text>
  <text x="305" y="170" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fb923c">desensitised</text>

  <!-- Labels T2D -->
  <text x="379" y="415" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f97316" font-weight="600">Cell starving ✕</text>
  <text x="379" y="428" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#475569">Glucose locked out of cell</text>

  <!-- ══════════════════════════════════════════════
       PANEL 3 — INSULIN INJECTION
  ══════════════════════════════════════════════ -->

  <!-- Cell membrane (green tint, recovering) -->
  <ellipse cx="633" cy="280" rx="112" ry="130" fill="url(#ins-cell-inject)" stroke="#34d399" stroke-width="1.5" opacity="0.95"/>

  <!-- Syringe (top right, injecting) -->
  <rect x="680" y="82" width="44" height="10" rx="3" fill="#1e3a5f" stroke="#60a5fa" stroke-width="1.2" transform="rotate(-35,702,87)"/>
  <rect x="718" y="76" width="10" height="6" rx="1" fill="#3b82f6" transform="rotate(-35,723,79)"/>
  <!-- Needle -->
  <line x1="677" y1="95" x2="660" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="706" y="78" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#60a5fa" font-weight="700" transform="rotate(-35,706,78)">INSULIN</text>

  <!-- Injected insulin molecules (multiple, coming from syringe) -->
  <polygon points="648,112 658,118 658,130 648,136 638,130 638,118" fill="url(#ins-mol)" stroke="#818cf8" stroke-width="1.2"/>
  <text x="648" y="127" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#e0e7ff" font-weight="700">INS</text>
  <polygon points="630,100 638,105 638,115 630,120 622,115 622,105" fill="url(#ins-mol)" stroke="#818cf8" stroke-width="1" opacity="0.7"/>
  <text x="630" y="113" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#e0e7ff" font-weight="700">INS</text>
  <polygon points="668,98 676,103 676,113 668,118 660,113 660,103" fill="url(#ins-mol)" stroke="#818cf8" stroke-width="1" opacity="0.7"/>
  <text x="668" y="111" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#e0e7ff" font-weight="700">INS</text>

  <!-- Insulin binding to receptor -->
  <line x1="648" y1="136" x2="633" y2="152" stroke="#818cf8" stroke-width="1.5" marker-end="url(#ins-arr-b)"/>

  <!-- Receptor (active, lit up) -->
  <line x1="633" y1="155" x2="633" y2="170" stroke="#34d399" stroke-width="2.5"/>
  <line x1="633" y1="170" x2="619" y2="184" stroke="#34d399" stroke-width="2.5"/>
  <line x1="633" y1="170" x2="647" y2="184" stroke="#34d399" stroke-width="2.5"/>
  <rect x="627" y="184" width="12" height="20" rx="3" fill="#34d399" opacity="0.9"/>
  <!-- GLUT4 open again -->
  <rect x="614" y="196" width="38" height="16" rx="5" fill="#064e2c" stroke="#34d399" stroke-width="1.5"/>
  <text x="633" y="208" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#6ee7b7" font-weight="700">GLUT4 ▼ OPEN</text>

  <!-- Glucose now flowing in -->
  <circle cx="633" cy="226" r="9" fill="url(#ins-gluc)" filter="url(#ins-glow-g)"/>
  <text x="633" y="230" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6.5" fill="#78350f" font-weight="700">G</text>
  <line x1="633" y1="214" x2="633" y2="222" stroke="#fbbf24" stroke-width="2" marker-end="url(#ins-arr-y)"/>

  <!-- Glucose accumulating inside -->
  <circle cx="598" cy="272" r="8" fill="url(#ins-gluc)" opacity="0.85"/>
  <text x="598" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <circle cx="633" cy="290" r="8" fill="url(#ins-gluc)" opacity="0.85"/>
  <text x="633" y="294" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <circle cx="665" cy="268" r="8" fill="url(#ins-gluc)" opacity="0.85"/>
  <text x="665" y="272" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#78350f" font-weight="700">G</text>
  <!-- ATP badge -->
  <rect x="607" y="318" width="52" height="18" rx="4" fill="#064e2c" stroke="#34d399" stroke-width="1"/>
  <text x="633" y="330" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#34d399" font-weight="700">⚡ ATP restored</text>

  <!-- Blood glucose dropping note -->
  <rect x="540" y="96" width="80" height="24" rx="4" fill="#0a2010" stroke="#34d399" stroke-width="1"/>
  <text x="580" y="107" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7.5" fill="#34d399" font-weight="700">↓ Blood glucose</text>
  <text x="580" y="117" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#064e2c">normalising</text>

  <!-- Labels injection panel -->
  <text x="633" y="415" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#34d399" font-weight="600">Cell absorbing again ✓</text>
  <text x="633" y="428" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#475569">Injected insulin overrides resistance</text>

  <!-- Bottom legend -->
  <rect x="10" y="440" width="740" height="14" rx="3" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="28"  cy="447" r="5" fill="url(#ins-gluc)"/>
  <text x="38"  y="451" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Glucose molecule</text>
  <polygon points="110,447 116,451 116,457 110,461 104,457 104,451" fill="url(#ins-mol)" stroke="none"/>
  <text x="122" y="451" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Insulin</text>
  <rect x="200" y="443" width="30" height="8" rx="2" fill="#22c55e" opacity="0.5"/>
  <text x="236" y="451" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Active receptor/transporter</text>
  <rect x="380" y="443" width="30" height="8" rx="2" fill="#6b7280" opacity="0.5"/>
  <text x="416" y="451" font-family="system-ui,sans-serif" font-size="8" fill="#94a3b8">Blocked/inactive</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">In Type 2 diabetes, insulin is produced but cells stop responding to it — glucose piles up in the blood while the cell starves. Injecting insulin at higher concentrations can override the desensitised receptor, restoring glucose uptake.</figcaption>
</figure>"""

# ── SVG 2: Ketoacidosis cascade ───────────────────────────────────────────────

SVG_DKA = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diabetic ketoacidosis cascade: no insulin leads to fat breakdown, ketone overproduction, and dangerously acidic blood">
  <defs>
    <marker id="dka-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#f87171"/></marker>
    <marker id="dka-arr-o" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#fb923c"/></marker>
    <marker id="dka-arr-y" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#fbbf24"/></marker>
    <marker id="dka-arr-p" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#c084fc"/></marker>
    <linearGradient id="dka-acid" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7f1d1d"/>
      <stop offset="100%" stop-color="#450a03"/>
    </linearGradient>
    <filter id="dka-glow">
      <feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="760" height="400" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="380" y="26" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Diabetic Ketoacidosis (DKA): The Cascade</text>
  <text x="380" y="43" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">When no insulin is available, the body burns fat to survive — but the byproducts poison the blood</text>

  <!-- ══ STEP BOXES — left to right flow ══ -->

  <!-- STEP 1: No insulin -->
  <rect x="14" y="64" width="116" height="96" rx="8" fill="#1a0a08" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="72" cy="84" r="12" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
  <text x="72" y="89" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fca5a5" font-weight="700">1</text>
  <text x="72" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5" font-weight="700">No Insulin</text>
  <text x="72" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7f1d1d">(Type 1: pancreas</text>
  <text x="72" y="134" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7f1d1d">produces none)</text>
  <text x="72" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#6b7280">or severe T2D</text>

  <!-- Arrow 1→2 -->
  <line x1="130" y1="112" x2="152" y2="112" stroke="#ef4444" stroke-width="2" marker-end="url(#dka-arr)"/>

  <!-- STEP 2: Cells can't use glucose -->
  <rect x="154" y="64" width="126" height="96" rx="8" fill="#1a0a08" stroke="#f97316" stroke-width="1.5"/>
  <circle cx="217" cy="84" r="12" fill="#7c2d12" stroke="#f97316" stroke-width="1.5"/>
  <text x="217" y="89" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fdba74" font-weight="700">2</text>
  <text x="217" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fdba74" font-weight="700">Cells Can't Use</text>
  <text x="217" y="120" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fdba74" font-weight="700">Glucose</text>
  <text x="217" y="136" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7c2d12">Blood glucose</text>
  <text x="217" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7c2d12">skyrockets (↑ 600+)</text>

  <!-- Arrow 2→3 -->
  <line x1="280" y1="112" x2="302" y2="112" stroke="#f97316" stroke-width="2" marker-end="url(#dka-arr-o)"/>

  <!-- STEP 3: Fat breakdown (lipolysis) -->
  <rect x="304" y="64" width="126" height="96" rx="8" fill="#1a1208" stroke="#fbbf24" stroke-width="1.5"/>
  <circle cx="367" cy="84" r="12" fill="#451a03" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="367" y="89" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fde68a" font-weight="700">3</text>
  <text x="367" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fde68a" font-weight="700">Body Burns Fat</text>
  <text x="367" y="120" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fde68a" font-weight="700">(Lipolysis)</text>
  <text x="367" y="136" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#92400e">Glucagon surges,</text>
  <text x="367" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#92400e">fat cells release FFAs</text>

  <!-- Arrow 3→4 -->
  <line x1="430" y1="112" x2="452" y2="112" stroke="#fbbf24" stroke-width="2" marker-end="url(#dka-arr-y)"/>

  <!-- STEP 4: Liver makes ketones -->
  <rect x="454" y="64" width="136" height="96" rx="8" fill="#140c1a" stroke="#c084fc" stroke-width="1.5"/>
  <circle cx="522" cy="84" r="12" fill="#3b0764" stroke="#c084fc" stroke-width="1.5"/>
  <text x="522" y="89" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#e9d5ff" font-weight="700">4</text>
  <text x="522" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#e9d5ff" font-weight="700">Liver Makes Ketones</text>
  <text x="522" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7e22ce">Acetoacetate</text>
  <text x="522" y="134" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7e22ce">β-hydroxybutyrate</text>
  <text x="522" y="146" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7e22ce">Acetone (breath odour)</text>

  <!-- Arrow 4→5 -->
  <line x1="590" y1="112" x2="612" y2="112" stroke="#c084fc" stroke-width="2" marker-end="url(#dka-arr-p)"/>

  <!-- STEP 5: Blood acidified — DKA -->
  <rect x="614" y="56" width="134" height="112" rx="8" fill="url(#dka-acid)" stroke="#ef4444" stroke-width="2"/>
  <circle cx="681" cy="80" r="14" fill="#7f1d1d" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="681" y="85" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#fca5a5" font-weight="700">5</text>
  <text x="681" y="106" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#fca5a5" font-weight="700">Blood Acidified</text>
  <text x="681" y="120" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444" font-weight="700">DKA</text>
  <text x="681" y="134" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">pH drops below 7.3</text>
  <text x="681" y="146" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#fca5a5">(normal: 7.35–7.45)</text>
  <text x="681" y="158" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#b91c1c">⚠ Medical emergency</text>

  <!-- ══ SYMPTOMS PANEL (bottom left) ══ -->
  <rect x="14" y="178" width="360" height="138" rx="8" fill="#0d1118" stroke="#334155" stroke-width="1"/>
  <text x="194" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8" font-weight="700" letter-spacing="0.08em">DKA SYMPTOMS</text>

  <text x="32"  y="218" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="218" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Extreme thirst &amp; frequent urination</text>
  <text x="32"  y="234" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="234" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Nausea, vomiting, abdominal pain</text>
  <text x="32"  y="250" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="250" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Fruity-smelling breath (acetone)</text>
  <text x="32"  y="266" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="266" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Rapid, deep breathing (Kussmaul breathing)</text>
  <text x="32"  y="282" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="282" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Confusion, fatigue, loss of consciousness</text>
  <text x="32"  y="298" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">▸</text>
  <text x="44"  y="298" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Blood glucose typically above 250 mg/dL</text>

  <!-- ══ TREATMENT PANEL (bottom right) ══ -->
  <rect x="386" y="178" width="360" height="138" rx="8" fill="#0a1a10" stroke="#16a34a" stroke-width="1"/>
  <text x="566" y="198" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700" letter-spacing="0.08em">EMERGENCY TREATMENT</text>

  <text x="404" y="218" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="218" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1"><tspan font-weight="600" fill="#4ade80">IV insulin</tspan> — shuts down ketone production</text>
  <text x="404" y="234" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="234" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1"><tspan font-weight="600" fill="#4ade80">IV fluids</tspan> — rehydration &amp; dilute acid load</text>
  <text x="404" y="250" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="250" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1"><tspan font-weight="600" fill="#4ade80">Electrolytes</tspan> — potassium, sodium, phosphate</text>
  <text x="404" y="266" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="266" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Monitor &amp; treat the <tspan font-weight="600" fill="#4ade80">triggering event</tspan></text>
  <text x="404" y="282" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="282" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">ICU admission if severe (pH &lt; 7.0)</text>
  <text x="404" y="298" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">▸</text>
  <text x="416" y="298" font-family="system-ui,sans-serif" font-size="9" fill="#cbd5e1">Recovery in 24–48 h with correct treatment</text>

  <!-- ══ BLOOD pH GAUGE ══ -->
  <rect x="220" y="332" width="320" height="58" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="380" y="350" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" font-weight="600">BLOOD pH SCALE</text>
  <!-- pH bar -->
  <defs>
    <linearGradient id="ph-bar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#dc2626"/>
      <stop offset="35%"  stop-color="#f97316"/>
      <stop offset="55%"  stop-color="#22c55e"/>
      <stop offset="75%"  stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
  </defs>
  <rect x="240" y="356" width="280" height="10" rx="4" fill="url(#ph-bar)"/>
  <!-- Normal range marker -->
  <rect x="364" y="353" width="48" height="16" rx="2" fill="none" stroke="#f1f5f9" stroke-width="1.5"/>
  <!-- DKA marker (left of normal) -->
  <rect x="240" y="353" width="62" height="16" rx="2" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="242" y="383" font-family="system-ui,sans-serif" font-size="7.5" fill="#ef4444" font-weight="600">DKA (&lt;7.3)</text>
  <text x="364" y="383" font-family="system-ui,sans-serif" font-size="7.5" fill="#f1f5f9" font-weight="600">Normal (7.35–7.45)</text>
  <text x="490" y="383" font-family="system-ui,sans-serif" font-size="7.5" fill="#60a5fa">Alkaline</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">DKA most commonly occurs in Type 1 diabetes (where the pancreas produces no insulin) but can also occur in severe Type 2 diabetes. Without insulin, no glucose enters cells — so the body triggers emergency fat breakdown. The liver converts fatty acids into ketone bodies faster than they can be cleared, and the accumulating acid drives blood pH dangerously low.</figcaption>
</figure>"""

# ── Article content ───────────────────────────────────────────────────────────

ARTICLE_CONTENT = """<h2>When the Key No Longer Fits the Lock</h2>
<p>Every cell in your body runs on glucose. Insulin is the key that unlocks the door — binding to receptors on the cell surface and triggering transporters (GLUT4) to open and let glucose in. In a healthy person, this happens within minutes of eating. Blood glucose rises, the pancreas releases insulin, and cells absorb the sugar they need to function.</p>
<p>In diabetes, this elegant system breaks down — but in two very different ways depending on the type.</p>

<h2>Type 2 Diabetes: The Lock Stops Responding</h2>
<p>In Type 2 diabetes, the pancreas still produces insulin — often in large amounts — but the cells have become desensitised to it. The receptor is present, but it no longer responds normally to insulin's signal. Glucose builds up in the blood while the cell goes hungry. The pancreas compensates by producing even more insulin, which eventually exhausts the beta cells and makes the resistance worse.</p>
<p>This desensitisation is driven primarily by chronic overexposure to glucose and insulin — years of high-carbohydrate eating that keeps both perpetually elevated. Fat accumulation inside liver and muscle cells also blocks the signalling cascade that insulin depends on.</p>""" + "\n\n" + SVG_INSULIN + """

<h2>Insulin Injection: Overriding the Resistance</h2>
<p>When oral medications are no longer sufficient, injected insulin can restore glucose uptake by flooding the system with enough signal to overcome the desensitised receptors. It is a workaround, not a cure — the underlying resistance remains, and doses typically need to increase over time. For Type 1 diabetes, where the pancreas produces no insulin at all, injection is not a workaround but a life-sustaining necessity from diagnosis onward.</p>

<h2>Diabetic Ketoacidosis: When the Body Burns Its Own Fat to Survive</h2>
<p>Without any functional insulin — most commonly in untreated or undertreated Type 1 diabetes — the body faces a crisis. Cells cannot absorb glucose no matter how high blood sugar climbs. The body interprets this as starvation and activates an emergency response: it begins breaking down fat.</p>
<p>The liver converts the released fatty acids into ketone bodies — acetoacetate, beta-hydroxybutyrate, and acetone. In small amounts, ketones are a normal and healthy alternative fuel. But in DKA, they are produced far faster than the body can use or excrete them. They accumulate in the blood, and because they are acids, the blood pH drops — from the normal 7.35–7.45 into dangerously acidic territory below 7.3. This is diabetic ketoacidosis.</p>
<p>DKA is a medical emergency. Left untreated, the acidic blood disrupts enzyme function throughout the body, impairs cardiac and neurological function, and can be fatal within hours to days. The breath takes on a distinctive fruity or nail-polish odour from acetone being exhaled.</p>""" + "\n\n" + SVG_DKA + """

<h2>Why DKA Happens — The Short Version</h2>
<ul>
  <li><strong>No insulin</strong> → cells cannot absorb glucose → blood glucose spikes</li>
  <li><strong>Glucagon surges</strong> (the counter-hormone to insulin) → signals fat cells to release fatty acids</li>
  <li><strong>Liver converts fatty acids</strong> into ketone bodies at high speed</li>
  <li><strong>Ketones accumulate</strong> faster than kidneys can excrete them → blood acidifies</li>
  <li><strong>Result:</strong> blood pH below 7.3, fruity breath, vomiting, rapid deep breathing, confusion, coma</li>
</ul>
<p>DKA is treated with IV insulin (which shuts down ketone production immediately), IV fluids to rehydrate and dilute the acid load, and careful electrolyte replacement — particularly potassium, which shifts dramatically as insulin drives glucose and potassium back into cells.</p>

<h2>The Metabolic Thread</h2>
<p>Both insulin resistance and DKA are, at their root, disorders of the same system — the machinery that moves glucose from blood into cells. In Type 2 diabetes the machinery is jammed by chronic overconsumption. In Type 1 and severe Type 2, the key is simply missing. Understanding which failure you are dealing with determines everything about how it is managed.</p>"""


class Command(BaseCommand):
    help = "Create the Diabetes pillar and article with insulin + DKA illustrations"

    def handle(self, *args, **options):
        pillar, created = Pillar.objects.update_or_create(
            slug="diabetes",
            defaults={
                "name": "Diabetes",
                "description": "Type 1, Type 2, and the metabolic machinery of insulin and glucose.",
                "icon": "🩸",
                "color": "green",
                "order": 12,
            },
        )
        self.stdout.write(f"{'Created' if created else 'Updated'} pillar: {pillar.name}")

        article, created = Article.objects.update_or_create(
            slug="insulin-resistance-and-ketoacidosis",
            defaults={
                "title": "Insulin, Resistance, and the Crisis of Ketoacidosis",
                "summary": (
                    "How insulin unlocks glucose uptake in healthy cells, why cells stop responding in Type 2 diabetes, "
                    "what happens when insulin is injected to restore absorption, and how the absence of insulin triggers "
                    "the life-threatening cascade of diabetic ketoacidosis."
                ),
                "content": ARTICLE_CONTENT,
                "pillar": pillar,
                "order": 1,
                "published": True,
                "ai_summary": (
                    "Covers insulin receptor mechanism and GLUT4 transporters, Type 2 insulin resistance, "
                    "injection therapy, and the DKA cascade: no insulin → lipolysis → ketogenesis → blood acidification. "
                    "Includes symptoms, emergency treatment, and the metabolic link between T1 and T2 diabetes."
                ),
            },
        )
        self.stdout.write(f"{'Created' if created else 'Updated'} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
