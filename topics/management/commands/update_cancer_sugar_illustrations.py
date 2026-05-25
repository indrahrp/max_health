from django.core.management.base import BaseCommand
from topics.models import Article

# ── SVG 1: Warburg Effect ─────────────────────────────────────────────────────

SVG_WARBURG = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 460" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Diagram comparing energy production in normal cells versus cancer cells showing the Warburg Effect">
  <defs>
    <marker id="w-arr-g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4ade80"/></marker>
    <marker id="w-arr-r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/></marker>
    <marker id="w-arr-y" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#facc15"/></marker>
    <marker id="w-arr-b" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#60a5fa"/></marker>
    <radialGradient id="mito-healthy" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#14532d"/>
      <stop offset="100%" stop-color="#052e16"/>
    </radialGradient>
    <radialGradient id="mito-dead" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#1c1c1c"/>
      <stop offset="100%" stop-color="#0a0a0a"/>
    </radialGradient>
    <radialGradient id="cell-normal-bg" cx="50%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#0a1628"/>
      <stop offset="100%" stop-color="#060d18"/>
    </radialGradient>
    <radialGradient id="cell-cancer-bg" cx="50%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#1a0505"/>
      <stop offset="100%" stop-color="#0d0202"/>
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect width="720" height="460" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">The Warburg Effect: How Cancer Makes Energy Differently</text>
  <text x="360" y="45" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Normal cells burn fuel cleanly in mitochondria — cancer cells ferment it, even when oxygen is available</text>

  <!-- ── CENTER DIVIDER ── -->
  <line x1="360" y1="58" x2="360" y2="430" stroke="#1e293b" stroke-width="1.5"/>

  <!-- ── COLUMN HEADERS ── -->
  <rect x="10" y="58" width="344" height="26" rx="5" fill="#0d2218"/>
  <text x="182" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#4ade80" font-weight="700">Normal Cell</text>
  <rect x="366" y="58" width="344" height="26" rx="5" fill="#200808"/>
  <text x="538" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#f87171" font-weight="700">Cancer Cell  (Warburg Effect)</text>

  <!-- ════════════════════════════════════════════════
       LEFT SIDE — Normal Cell
  ════════════════════════════════════════════════ -->

  <!-- Cell membrane (left) -->
  <ellipse cx="182" cy="270" rx="155" ry="155" fill="url(#cell-normal-bg)" stroke="#22c55e" stroke-width="1.5" opacity="0.9"/>
  <text x="40" y="425" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80" opacity="0.6">cell membrane</text>

  <!-- O2 enters (top left) -->
  <text x="72" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#60a5fa">O₂</text>
  <line x1="72" y1="118" x2="100" y2="148" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#w-arr-b)" stroke-dasharray="4 2"/>
  <text x="56" y="107" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">oxygen in</text>

  <!-- Glucose enters -->
  <rect x="148" y="96" width="68" height="22" rx="4" fill="#78350f" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="182" y="111" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fcd34d" font-weight="600">Glucose</text>
  <line x1="182" y1="118" x2="182" y2="140" stroke="#facc15" stroke-width="2" marker-end="url(#w-arr-y)"/>

  <!-- STEP 1: Glycolysis (cytoplasm) -->
  <rect x="128" y="142" width="108" height="38" rx="6" fill="#1a2035" stroke="#334155" stroke-width="1"/>
  <text x="182" y="158" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8" font-weight="600">Glycolysis</text>
  <text x="182" y="172" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">(in cytoplasm)</text>
  <!-- 2 ATP badge -->
  <rect x="246" y="148" width="40" height="22" rx="4" fill="#1c2e1c" stroke="#22c55e" stroke-width="1"/>
  <text x="266" y="163" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80" font-weight="700">+2 ATP</text>

  <!-- Arrow: glycolysis → pyruvate -->
  <line x1="182" y1="180" x2="182" y2="200" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#w-arr-b)"/>
  <text x="192" y="194" font-family="system-ui,sans-serif" font-size="9" fill="#475569">pyruvate</text>

  <!-- HEALTHY MITOCHONDRIA -->
  <ellipse cx="182" cy="270" rx="62" ry="42" fill="url(#mito-healthy)" stroke="#22c55e" stroke-width="2"/>
  <!-- Cristae folds (inner membrane pattern) -->
  <path d="M 144 265 Q 155 255, 165 268 Q 175 280, 185 268 Q 195 255, 205 268 Q 215 280, 220 268" fill="none" stroke="#16a34a" stroke-width="1.2" opacity="0.7"/>
  <text x="182" y="258" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#86efac" font-weight="700">Mitochondria</text>
  <text x="182" y="271" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">(healthy)</text>
  <text x="182" y="284" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">Krebs cycle + ETC</text>

  <!-- Arrow: pyruvate → mitochondria -->
  <line x1="182" y1="200" x2="182" y2="228" stroke="#4ade80" stroke-width="2" marker-end="url(#w-arr-g)"/>

  <!-- +34 ATP badge -->
  <rect x="248" y="254" width="44" height="22" rx="4" fill="#1c2e1c" stroke="#22c55e" stroke-width="1.2"/>
  <text x="270" y="269" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80" font-weight="700">+34 ATP</text>

  <!-- CO2 out -->
  <line x1="182" y1="312" x2="182" y2="336" stroke="#64748b" stroke-width="1.5" marker-end="url(#w-arr-b)" stroke-dasharray="3 2"/>
  <text x="182" y="350" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#475569">CO₂ out</text>

  <!-- TOTAL ATP (left) -->
  <rect x="114" y="390" width="136" height="32" rx="6" fill="#052e16" stroke="#16a34a" stroke-width="1.5"/>
  <text x="182" y="405" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80" font-weight="700">Total: ~36 ATP</text>
  <text x="182" y="418" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#16a34a">per glucose molecule</text>

  <!-- ════════════════════════════════════════════════
       RIGHT SIDE — Cancer Cell (Warburg Effect)
  ════════════════════════════════════════════════ -->

  <!-- Cell membrane (right) -->
  <ellipse cx="538" cy="270" rx="155" ry="155" fill="url(#cell-cancer-bg)" stroke="#ef4444" stroke-width="1.5" opacity="0.9"/>

  <!-- O2 present but UNUSED -->
  <text x="412" y="115" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#475569">O₂</text>
  <text x="412" y="128" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#ef4444" font-weight="700">✕ ignored</text>
  <text x="412" y="107" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#475569">oxygen present</text>

  <!-- More glucose enters (wider arrow to show excess) -->
  <rect x="494" y="92" width="88" height="22" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
  <text x="538" y="107" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5" font-weight="600">Glucose ×10</text>
  <line x1="538" y1="114" x2="538" y2="140" stroke="#f87171" stroke-width="3" marker-end="url(#w-arr-r)"/>
  <text x="590" y="128" font-family="system-ui,sans-serif" font-size="8.5" fill="#ef4444">needs far</text>
  <text x="590" y="139" font-family="system-ui,sans-serif" font-size="8.5" fill="#ef4444">more fuel</text>

  <!-- STEP 1: Glycolysis (cancer) -->
  <rect x="484" y="142" width="108" height="38" rx="6" fill="#1f1010" stroke="#7f1d1d" stroke-width="1"/>
  <text x="538" y="158" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#fca5a5" font-weight="600">Glycolysis</text>
  <text x="538" y="172" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#7f1d1d">(in cytoplasm)</text>
  <!-- 2 ATP badge -->
  <rect x="598" y="148" width="40" height="22" rx="4" fill="#1f1010" stroke="#f87171" stroke-width="1"/>
  <text x="618" y="163" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#f87171" font-weight="700">+2 ATP</text>

  <!-- Arrow down to split: ↓ (blocked path) vs → lactic acid -->
  <line x1="538" y1="180" x2="538" y2="208" stroke="#f87171" stroke-width="1.5"/>

  <!-- BLOCKED path to mitochondria (X) -->
  <line x1="538" y1="208" x2="538" y2="228" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3"/>
  <!-- X mark -->
  <line x1="524" y1="218" x2="552" y2="232" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="552" y1="218" x2="524" y2="232" stroke="#ef4444" stroke-width="2.5"/>

  <!-- Damaged Mitochondria -->
  <ellipse cx="538" cy="280" rx="58" ry="38" fill="url(#mito-dead)" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="538" y="274" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#475569" font-weight="700">Mitochondria</text>
  <text x="538" y="287" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#374151">(damaged)</text>
  <text x="538" y="300" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#374151">cannot use pyruvate</text>

  <!-- Arrow: pyruvate → lactic acid (sideways) -->
  <line x1="538" y1="208" x2="460" y2="208" stroke="#f87171" stroke-width="2" marker-end="url(#w-arr-r)"/>
  <rect x="388" y="195" width="70" height="26" rx="4" fill="#2d0505" stroke="#ef4444" stroke-width="1.2"/>
  <text x="423" y="207" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5" font-weight="700">Lactic</text>
  <text x="423" y="218" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5" font-weight="700">acid out</text>
  <!-- Lactic acid exits cell -->
  <line x1="388" y1="208" x2="370" y2="208" stroke="#f87171" stroke-width="1.5" marker-end="url(#w-arr-r)" stroke-dasharray="3 2"/>

  <!-- "EVEN WITH O2 PRESENT" callout -->
  <rect x="610" y="188" width="98" height="32" rx="5" fill="#2d0a0a" stroke="#ef4444" stroke-width="1.2"/>
  <text x="659" y="202" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171" font-weight="700">Even with O₂</text>
  <text x="659" y="214" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#b91c1c">present! (aerobic)</text>

  <!-- TOTAL ATP (right) -->
  <rect x="470" y="390" width="136" height="32" rx="6" fill="#2d0505" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="538" y="405" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#f87171" font-weight="700">Total: only 2 ATP</text>
  <text x="538" y="418" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#7f1d1d">18× less efficient</text>

  <!-- ── BOTTOM SUMMARY ── -->
  <rect x="140" y="434" width="440" height="20" rx="4" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="360" y="448" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8">Cancer compensates with <tspan fill="#f87171" font-weight="700">speed and volume</tspan> — consuming up to 200× more glucose than the same normal cell</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">The Warburg Effect, first observed by Otto Warburg in the 1920s: cancer cells bypass the mitochondria entirely, fermenting glucose into lactic acid even when oxygen is available — producing far less energy per molecule, but consuming far more glucose to make up for it.</figcaption>
</figure>"""

# ── SVG 2: PET Scan ───────────────────────────────────────────────────────────

SVG_PET = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="How a PET scan detects cancer using radioactive glucose that cancer cells absorb at an abnormally high rate">
  <defs>
    <marker id="p-arr-w" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#94a3b8"/></marker>
    <marker id="p-arr-o" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#fb923c"/></marker>
    <radialGradient id="tumor-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#fbbf24" stop-opacity="1"/>
      <stop offset="35%"  stop-color="#f97316" stop-opacity="0.9"/>
      <stop offset="70%"  stop-color="#dc2626" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#dc2626" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="body-fill" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#0f1f3a"/>
      <stop offset="100%" stop-color="#060e1c"/>
    </radialGradient>
    <filter id="tumor-blur">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="720" height="380" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="26" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">FDG-PET Scan: How Cancer Lights Itself Up</text>
  <text x="360" y="43" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Radioactive glucose injected → cancer cells absorb it far faster → tumour glows on the scan</text>

  <!-- ══ LEFT PANEL: PET scan view (body silhouette) ══════════════════ -->

  <!-- Scan frame (dark monitor look) -->
  <rect x="18" y="55" width="260" height="310" rx="8" fill="#06090f" stroke="#1e293b" stroke-width="1.5"/>
  <text x="148" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#334155" letter-spacing="0.12em">FDG-PET SCAN IMAGE</text>

  <!-- Body silhouette (simplified frontal, head + torso) -->
  <!-- Head -->
  <ellipse cx="148" cy="108" rx="28" ry="30" fill="#0d1f38" stroke="#1e3a5f" stroke-width="1.2"/>
  <!-- Neck -->
  <rect x="138" y="136" width="20" height="14" fill="#0d1f38"/>
  <!-- Shoulders + torso -->
  <path d="M 90 150 Q 80 155, 78 200 L 78 300 Q 78 315, 95 318 L 200 318 Q 218 315, 218 300 L 218 200 Q 216 155, 205 150 Q 185 140, 148 140 Q 110 140, 90 150 Z" fill="url(#body-fill)" stroke="#1e3a5f" stroke-width="1.2"/>
  <!-- Arms -->
  <path d="M 78 165 Q 60 170, 55 220 Q 52 250, 55 270" fill="none" stroke="#1e3a5f" stroke-width="8" stroke-linecap="round" opacity="0.7"/>
  <path d="M 218 165 Q 236 170, 241 220 Q 244 250, 241 270" fill="none" stroke="#1e3a5f" stroke-width="8" stroke-linecap="round" opacity="0.7"/>

  <!-- Spine suggestion -->
  <line x1="148" y1="150" x2="148" y2="310" stroke="#0f2a48" stroke-width="3" stroke-dasharray="5 3"/>

  <!-- Rib cage hint -->
  <ellipse cx="148" cy="205" rx="42" ry="32" fill="none" stroke="#0f2a48" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6"/>
  <ellipse cx="148" cy="225" rx="40" ry="28" fill="none" stroke="#0f2a48" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>

  <!-- Normal tissue (dim, cool blue dots — low uptake) -->
  <circle cx="120" cy="190" r="5" fill="#1a4a7a" opacity="0.4"/>
  <circle cx="175" cy="185" r="4" fill="#1a4a7a" opacity="0.35"/>
  <circle cx="130" cy="240" r="5" fill="#1a4a7a" opacity="0.3"/>
  <circle cx="165" cy="255" r="4" fill="#1a4a7a" opacity="0.3"/>
  <circle cx="148" cy="280" r="5" fill="#1a4a7a" opacity="0.3"/>

  <!-- TUMOUR HOT SPOT — left lung area, glowing orange-red -->
  <circle cx="122" cy="210" r="28" fill="url(#tumor-glow)" filter="url(#tumor-blur)"/>
  <circle cx="122" cy="210" r="12" fill="#fbbf24" opacity="0.95"/>

  <!-- Tumour label -->
  <line x1="140" y1="200" x2="196" y2="175" stroke="#fb923c" stroke-width="1" stroke-dasharray="3 2"/>
  <rect x="196" y="162" width="72" height="26" rx="4" fill="#1a0a00" stroke="#f97316" stroke-width="1"/>
  <text x="232" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fb923c" font-weight="700">Tumour</text>
  <text x="232" y="184" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#7c3917">high FDG uptake</text>

  <!-- Normal tissue label -->
  <line x1="175" y1="185" x2="200" y2="148" stroke="#334155" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="206" y="143" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Normal tissue</text>
  <text x="206" y="154" font-family="system-ui,sans-serif" font-size="8.5" fill="#334155">(low uptake, dim)</text>

  <!-- Brain uptake (brain normally uses lots of glucose — shown bright too) -->
  <circle cx="148" cy="108" r="14" fill="#f97316" opacity="0.35"/>
  <text x="54" y="105" font-family="system-ui,sans-serif" font-size="8" fill="#475569">brain (normal</text>
  <text x="54" y="116" font-family="system-ui,sans-serif" font-size="8" fill="#475569">high uptake)</text>
  <line x1="90" y1="110" x2="134" y2="108" stroke="#334155" stroke-width="1" stroke-dasharray="2 2"/>

  <!-- Colour scale bar -->
  <defs>
    <linearGradient id="pet-scale" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d1f38"/>
      <stop offset="40%" stop-color="#1e40af"/>
      <stop offset="65%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#fbbf24"/>
    </linearGradient>
  </defs>
  <rect x="28" y="338" width="240" height="10" rx="3" fill="url(#pet-scale)"/>
  <text x="28" y="360" font-family="system-ui,sans-serif" font-size="8.5" fill="#334155">Low glucose uptake</text>
  <text x="268" y="360" text-anchor="end" font-family="system-ui,sans-serif" font-size="8.5" fill="#fb923c">High glucose uptake</text>

  <!-- ══ RIGHT PANEL: 4-step explanation ══════════════════════════════ -->

  <!-- Step boxes (stacked vertically) -->

  <!-- STEP 1 -->
  <rect x="290" y="58" width="416" height="68" rx="8" fill="#0d1625" stroke="#1e293b" stroke-width="1"/>
  <circle cx="316" cy="92" r="16" fill="#1e3a5f" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="316" y="97" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#60a5fa" font-weight="700">1</text>
  <text x="342" y="80" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">Radioactive glucose (FDG) injected</text>
  <text x="342" y="96" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">A glucose molecule tagged with a radioactive tracer is</text>
  <text x="342" y="110" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">put into the bloodstream — it behaves just like real glucose.</text>

  <!-- Arrow 1→2 -->
  <line x1="498" y1="126" x2="498" y2="140" stroke="#334155" stroke-width="1.5" marker-end="url(#p-arr-w)"/>

  <!-- STEP 2 -->
  <rect x="290" y="142" width="416" height="68" rx="8" fill="#0d1625" stroke="#1e293b" stroke-width="1"/>
  <circle cx="316" cy="176" r="16" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
  <text x="316" y="181" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#f87171" font-weight="700">2</text>
  <text x="342" y="164" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">Cancer cells absorb it at extreme speed</text>
  <text x="342" y="180" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">Because cancer cells need so much glucose to survive,</text>
  <text x="342" y="194" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">they pull in FDG <tspan fill="#f87171" font-weight="600">5–10× faster</tspan> than normal cells around them.</text>

  <!-- Arrow 2→3 -->
  <line x1="498" y1="210" x2="498" y2="224" stroke="#334155" stroke-width="1.5" marker-end="url(#p-arr-w)"/>

  <!-- STEP 3 -->
  <rect x="290" y="226" width="416" height="68" rx="8" fill="#0d1625" stroke="#1e293b" stroke-width="1"/>
  <circle cx="316" cy="260" r="16" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="316" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#fbbf24" font-weight="700">3</text>
  <text x="342" y="248" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">The tracer decays — emitting radiation</text>
  <text x="342" y="264" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">The radioactive tag emits positrons. These collide with</text>
  <text x="342" y="278" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">electrons, releasing gamma rays the scanner detects.</text>

  <!-- Arrow 3→4 -->
  <line x1="498" y1="294" x2="498" y2="308" stroke="#334155" stroke-width="1.5" marker-end="url(#p-arr-w)"/>

  <!-- STEP 4 -->
  <rect x="290" y="310" width="416" height="57" rx="8" fill="#0a2010" stroke="#16a34a" stroke-width="1.2"/>
  <circle cx="316" cy="338" r="16" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
  <text x="316" y="343" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#4ade80" font-weight="700">4</text>
  <text x="342" y="328" font-family="system-ui,sans-serif" font-size="11" fill="#e2e8f0" font-weight="600">Scanner maps the hot spots → tumour found</text>
  <text x="342" y="344" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">Where radiation clusters = where cancer is. The more</text>
  <text x="342" y="358" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">aggressive the tumour, the brighter it glows on the scan.</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">Every FDG-PET scan performed in oncology departments worldwide is direct proof of the Warburg Effect — tumours reveal themselves by their abnormal hunger for glucose.</figcaption>
</figure>"""

# ── Insertion markers ─────────────────────────────────────────────────────────

# Insert Warburg SVG after the paragraph ending "...producing only a fraction of the energy..."
WARBURG_ANCHOR = (
    "This became known as the <strong>Warburg Effect</strong>, or aerobic fermentation. "
    "It is inefficient — producing only a fraction of the energy that oxidative phosphorylation "
    "generates — but it is fast, and it gives cancer cells a growth advantage because it produces "
    "the carbon building blocks needed for rapid cell division."
)

# Insert PET SVG after the paragraph ending "...treating cancer."
PET_ANCHOR = (
    "The medical community uses this fact daily to detect cancer — while the mainstream research "
    "and treatment paradigm has been slow to act on its implications for <em>treating</em> cancer."
)


class Command(BaseCommand):
    help = "Insert Warburg Effect and PET scan SVG illustrations into the why-sugar-feeds-cancer article"

    def handle(self, *args, **kwargs):
        try:
            article = Article.objects.get(slug="why-sugar-feeds-cancer")
        except Article.DoesNotExist:
            self.stderr.write("Article 'why-sugar-feeds-cancer' not found.")
            return

        content = article.content

        if SVG_WARBURG in content and SVG_PET in content:
            self.stdout.write("Illustrations already present — nothing to do.")
            return

        # Insert Warburg SVG after the matching paragraph
        if WARBURG_ANCHOR in content and SVG_WARBURG not in content:
            content = content.replace(
                WARBURG_ANCHOR,
                WARBURG_ANCHOR + "\n\n" + SVG_WARBURG,
            )
            self.stdout.write("Inserted Warburg Effect illustration.")
        else:
            self.stderr.write("WARNING: Warburg anchor not found or SVG already present.")

        # Insert PET SVG after the matching sentence
        if PET_ANCHOR in content and SVG_PET not in content:
            content = content.replace(
                PET_ANCHOR,
                PET_ANCHOR + "\n\n" + SVG_PET,
            )
            self.stdout.write("Inserted PET scan illustration.")
        else:
            self.stderr.write("WARNING: PET anchor not found or SVG already present.")

        article.content = content
        article.save()
        self.stdout.write("Article saved.")
