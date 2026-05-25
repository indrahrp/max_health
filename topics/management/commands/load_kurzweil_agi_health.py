from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Artificial Intelligence",
    "slug": "artificial-intelligence",
    "description": (
        "Machine learning, large language models, AGI, and the technologies reshaping science and society."
    ),
    "icon": "🤖",
    "color": "blue",
    "order": 1,
}

SVG_ESCAPE_VELOCITY = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Chart showing longevity escape velocity: the point where medical progress outpaces aging">
  <defs>
    <marker id="ev-arr-g" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#4ade80"/></marker>
    <marker id="ev-arr-r" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#f87171"/></marker>
    <linearGradient id="grad-green" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#22c55e" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="grad-red" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.03"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="720" height="360" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="30" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Longevity Escape Velocity</text>
  <text x="360" y="47" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">The race between how fast you age and how fast medicine advances</text>

  <!-- ─── CHART AREA  x: 60→680, y: 65→300 ─── -->

  <!-- Grid lines (horizontal) -->
  <line x1="60" y1="300" x2="680" y2="300" stroke="#1e293b" stroke-width="1"/>
  <line x1="60" y1="250" x2="680" y2="250" stroke="#1e293b" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="60" y1="200" x2="680" y2="200" stroke="#1e293b" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="60" y1="150" x2="680" y2="150" stroke="#1e293b" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="60" y1="100" x2="680" y2="100" stroke="#1e293b" stroke-width="0.5" stroke-dasharray="3 3"/>

  <!-- Y-axis -->
  <line x1="60" y1="65" x2="60" y2="305" stroke="#334155" stroke-width="1.5"/>
  <!-- Y labels -->
  <text x="52" y="304" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#475569">0</text>
  <text x="52" y="254" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#475569">+5y</text>
  <text x="52" y="204" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#475569">+10y</text>
  <text x="52" y="154" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#475569">+20y</text>
  <text x="52" y="104" text-anchor="end" font-family="system-ui,sans-serif" font-size="9" fill="#475569">+40y</text>
  <text x="10" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" transform="rotate(-90,10,200)">Extra years gained</text>

  <!-- X-axis labels: 2024, 2029, 2032, 2040, 2045 -->
  <!-- x positions: 2024=100, 2029=240, 2032=315, 2040=515, 2045=640 -->
  <text x="100" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">2024</text>
  <text x="240" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#facc15" font-weight="700">2029</text>
  <text x="315" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#4ade80">2032</text>
  <text x="515" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b">2040</text>
  <text x="640" y="318" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#a78bfa">2045</text>

  <!-- Vertical marker lines -->
  <line x1="240" y1="68" x2="240" y2="300" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
  <line x1="640" y1="68" x2="640" y2="300" stroke="#a78bfa" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>

  <!-- ─── LINE 1: Aging (what you lose each year) — flat/slow rise ─── -->
  <!-- Points: (100,283) (240,260) (315,250) (515,238) (640,232) -->
  <!-- Fill area under aging line -->
  <polygon points="100,283 240,260 315,250 515,238 640,232 640,300 100,300" fill="url(#grad-red)" opacity="0.6"/>
  <polyline points="100,283 240,260 315,250 515,238 640,232" fill="none" stroke="#f87171" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Aging line end arrow -->
  <circle cx="640" cy="232" r="4" fill="#f87171"/>

  <!-- ─── LINE 2: Medical progress (gains per year) — accelerating curve ─── -->
  <!-- Points: (100,278) (240,260) (315,245) (515,170) (640,88) -->
  <polygon points="100,278 240,260 315,245 515,170 640,88 640,300 100,300" fill="url(#grad-green)" opacity="0.6"/>
  <polyline points="100,278 240,260 315,245 515,170 640,88" fill="none" stroke="#4ade80" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="640" cy="88" r="4" fill="#4ade80"/>

  <!-- ─── CROSSING POINT at 2029 ─── -->
  <circle cx="240" cy="260" r="9" fill="#facc15" opacity="0.2"/>
  <circle cx="240" cy="260" r="5" fill="#facc15"/>
  <!-- Callout -->
  <rect x="248" y="234" width="130" height="34" rx="5" fill="#1c1a08" stroke="#facc15" stroke-width="1"/>
  <text x="313" y="248" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#facc15" font-weight="700">Escape Velocity</text>
  <text x="313" y="262" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a38b00">Medicine overtakes aging</text>

  <!-- ─── ANNOTATION: Today (2024) ─── -->
  <line x1="100" y1="283" x2="100" y2="280" stroke="#f87171" stroke-width="1"/>
  <text x="108" y="276" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">Today: medicine adds</text>
  <text x="108" y="287" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">~4 months/year</text>

  <!-- ─── ANNOTATION: 2045 Singularity ─── -->
  <rect x="648" y="72" width="62" height="40" rx="4" fill="#1a1130" stroke="#a78bfa" stroke-width="1"/>
  <text x="679" y="86" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#a78bfa" font-weight="700">Singularity</text>
  <text x="679" y="98" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7c3aed">Human + AI</text>
  <text x="679" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#7c3aed">fully merged</text>

  <!-- ─── LEGEND ─── -->
  <line x1="68" y1="337" x2="95" y2="337" stroke="#f87171" stroke-width="2.5"/>
  <text x="100" y="341" font-family="system-ui,sans-serif" font-size="10" fill="#f87171">How fast you age</text>
  <line x1="230" y1="337" x2="257" y2="337" stroke="#4ade80" stroke-width="2.5"/>
  <text x="262" y="341" font-family="system-ui,sans-serif" font-size="10" fill="#4ade80">Medical breakthroughs per year</text>
  <circle cx="460" cy="337" r="5" fill="#facc15"/>
  <text x="470" y="341" font-family="system-ui,sans-serif" font-size="10" fill="#facc15">Escape velocity (2029)</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">Kurzweil predicts medical progress will outpace aging by 2029 — the point at which every year you live adds more than a year to your expected lifespan.</figcaption>
</figure>"""

SVG_NANOBOTS = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="Illustration of nanobots inside a blood vessel, repairing damaged cells">
  <defs>
    <linearGradient id="vessel-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a0a0a"/>
      <stop offset="50%" stop-color="#2d0a0a"/>
      <stop offset="100%" stop-color="#1a0a0a"/>
    </linearGradient>
    <linearGradient id="rbc-grad" cx="40%" cy="40%" r="50%" gradientUnits="objectBoundingBox" id="rbc-g">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <radialGradient id="nb-grad" cx="40%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0c1a2e"/>
    </radialGradient>
    <marker id="nb-arr" markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="#60a5fa"/></marker>
    <filter id="glow-b">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="720" height="380" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="28" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700">Nanobots Inside Your Bloodstream — 2030s</text>
  <text x="360" y="45" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Microscopic robots the size of a blood cell, patrolling and repairing your body from within</text>

  <!-- ─── BLOOD VESSEL (tube) ─── -->
  <rect x="30" y="70" width="660" height="240" rx="12" fill="url(#vessel-grad)" stroke="#5f1212" stroke-width="2"/>
  <!-- Inner vessel walls -->
  <rect x="30" y="70" width="660" height="28" rx="0" fill="#3b0d0d" opacity="0.5"/>
  <rect x="30" y="282" width="660" height="28" rx="0" fill="#3b0d0d" opacity="0.5"/>
  <!-- Vessel label -->
  <text x="360" y="88" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" letter-spacing="0.1em">BLOOD VESSEL WALL</text>
  <text x="360" y="304" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#64748b" letter-spacing="0.1em">BLOOD VESSEL WALL</text>

  <!-- ─── RED BLOOD CELLS (donut shapes) ─── -->
  <!-- RBC 1 -->
  <ellipse cx="120" cy="185" rx="38" ry="30" fill="#991b1b" opacity="0.9"/>
  <ellipse cx="120" cy="185" rx="20" ry="14" fill="#7f1d1d" opacity="0.7"/>
  <!-- RBC 2 -->
  <ellipse cx="230" cy="155" rx="36" ry="28" fill="#b91c1c" opacity="0.85"/>
  <ellipse cx="230" cy="155" rx="18" ry="13" fill="#991b1b" opacity="0.7"/>
  <!-- RBC 3 (behind nanobot, dimmer) -->
  <ellipse cx="430" cy="210" rx="35" ry="27" fill="#7f1d1d" opacity="0.6"/>
  <ellipse cx="430" cy="210" rx="18" ry="12" fill="#6b1212" opacity="0.5"/>
  <!-- RBC 4 -->
  <ellipse cx="580" cy="170" rx="37" ry="29" fill="#991b1b" opacity="0.85"/>
  <ellipse cx="580" cy="170" rx="19" ry="13" fill="#7f1d1d" opacity="0.7"/>
  <!-- RBC 5 (small, background) -->
  <ellipse cx="510" cy="245" rx="30" ry="23" fill="#7f1d1d" opacity="0.55"/>
  <ellipse cx="510" cy="245" rx="15" ry="10" fill="#6b1212" opacity="0.45"/>

  <!-- Label: Red Blood Cell -->
  <line x1="120" y1="154" x2="120" y2="128" stroke="#475569" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="120" y="122" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#64748b">Red blood cell</text>
  <text x="120" y="112" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">(carries oxygen)</text>

  <!-- ─── DAMAGED CELL (glowing red, irregular) ─── -->
  <ellipse cx="320" cy="200" rx="32" ry="26" fill="#3b0000" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="320" y="196" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Damaged</text>
  <text x="320" y="208" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">cell ⚠</text>
  <!-- Damage lines -->
  <line x1="305" y1="185" x2="296" y2="178" stroke="#ef4444" stroke-width="1.2" opacity="0.6"/>
  <line x1="335" y1="187" x2="343" y2="180" stroke="#ef4444" stroke-width="1.2" opacity="0.6"/>
  <!-- Label -->
  <line x1="320" y1="226" x2="320" y2="255" stroke="#475569" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="320" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f87171">Diseased / aging cell</text>
  <text x="320" y="276" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">target for repair</text>

  <!-- ─── NANOBOT (main hero, center-left approaching damaged cell) ─── -->
  <!-- Body -->
  <rect x="218" y="175" width="52" height="40" rx="8" fill="url(#nb-grad)" stroke="#3b82f6" stroke-width="2" filter="url(#glow-b)"/>
  <!-- Body grid lines (circuit look) -->
  <line x1="234" y1="175" x2="234" y2="215" stroke="#1e40af" stroke-width="0.8" opacity="0.6"/>
  <line x1="250" y1="175" x2="250" y2="215" stroke="#1e40af" stroke-width="0.8" opacity="0.6"/>
  <line x1="218" y1="192" x2="270" y2="192" stroke="#1e40af" stroke-width="0.8" opacity="0.6"/>
  <!-- Eye / sensor -->
  <circle cx="244" cy="187" r="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
  <circle cx="244" cy="187" r="3" fill="#60a5fa" opacity="0.8"/>
  <!-- Arms extending toward damaged cell -->
  <line x1="270" y1="188" x2="288" y2="192" stroke="#60a5fa" stroke-width="2" marker-end="url(#nb-arr)"/>
  <line x1="270" y1="200" x2="288" y2="204" stroke="#60a5fa" stroke-width="2" marker-end="url(#nb-arr)"/>
  <!-- Propeller/thruster -->
  <ellipse cx="222" cy="191" rx="5" ry="10" fill="none" stroke="#475569" stroke-width="1.5"/>
  <line x1="222" y1="181" x2="222" y2="201" stroke="#334155" stroke-width="1" stroke-dasharray="2 1"/>

  <!-- Nanobot label -->
  <rect x="142" y="210" width="64" height="30" rx="4" fill="#0f1929" stroke="#3b82f6" stroke-width="1"/>
  <text x="174" y="223" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#60a5fa" font-weight="700">Nanobot</text>
  <text x="174" y="235" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">size of blood cell</text>
  <line x1="206" y1="218" x2="220" y2="195" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3 2"/>

  <!-- ─── SECOND NANOBOT (smaller, near RBC 4, patrolling) ─── -->
  <rect x="620" y="195" width="38" height="30" rx="6" fill="url(#nb-grad)" stroke="#3b82f6" stroke-width="1.5" opacity="0.85"/>
  <circle cx="638" cy="207" r="4" fill="#0f172a" stroke="#60a5fa" stroke-width="1.2"/>
  <circle cx="638" cy="207" r="2" fill="#60a5fa" opacity="0.7"/>
  <ellipse cx="622" cy="210" rx="3" ry="7" fill="none" stroke="#475569" stroke-width="1" opacity="0.7"/>
  <text x="639" y="240" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b">patrolling</text>

  <!-- ─── REPAIRED CELL (glowing green, right side) ─── -->
  <ellipse cx="640" cy="130" rx="28" ry="22" fill="#052e16" stroke="#22c55e" stroke-width="1.5"/>
  <text x="640" y="127" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">Healthy</text>
  <text x="640" y="139" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">cell ✓</text>
  <line x1="640" y1="108" x2="640" y2="96" stroke="#475569" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="640" y="90" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#4ade80">After repair</text>

  <!-- ─── FLOW ARROWS (blood flow direction) ─── -->
  <text x="48" y="190" font-family="system-ui,sans-serif" font-size="20" fill="#334155" opacity="0.5">→</text>
  <text x="680" y="190" font-family="system-ui,sans-serif" font-size="20" fill="#334155" opacity="0.5">→</text>

  <!-- ─── BOTTOM CAPTION BOXES ─── -->
  <rect x="30" y="332" width="200" height="38" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="130" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8" font-weight="600">What nanobots can do</text>
  <text x="130" y="362" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Repair · Remove toxins · Patrol</text>

  <rect x="260" y="332" width="200" height="38" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="360" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8" font-weight="600">When</text>
  <text x="360" y="362" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Kurzweil predicts: 2030s</text>

  <rect x="490" y="332" width="200" height="38" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="590" y="348" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#94a3b8" font-weight="600">How they get in</text>
  <text x="590" y="362" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5" fill="#475569">Swallowed or injected</text>
</svg>
<figcaption style="font-size:0.78rem;color:#64748b;margin-top:0.5em;text-align:center;">Kurzweil's vision for the 2030s: nanoscale robots circulate in the bloodstream, identifying and repairing damaged or aging cells before disease takes hold.</figcaption>
</figure>"""

ARTICLE_BODY = """<p class="lead">Ray Kurzweil has spent fifty years making predictions about technology — and getting an uncomfortable number of them right. His 1999 book predicted that a computer would beat the world chess champion (it happened in 1997), that the internet would become a global nervous system (it did), and that handheld devices would connect wirelessly to vast libraries of information (you're reading this on one now). His next set of predictions is about your body.</p>

<p>The claim is this: within the next ten to twenty years, artificial intelligence will do to medicine what it has already done to chess, translation, and image recognition — and the result will be that aging stops being something that happens to you and starts being something you can fix.</p>

<p>You don't need to be a scientist to understand why. You just need to understand one idea.</p>

<h2>Your Body Is Running Software</h2>

<p>Here is an example Kurzweil uses that stays with you. Inside every cell in your body is a gene called the fat insulin receptor gene. Its job, which it has been doing faithfully for hundreds of thousands of years, is to tell your body: <em>hold on to every calorie you can. The next hunting season might not work out.</em></p>

<p>That was good advice in the Stone Age. Today, with food available around the clock, it's why so many people struggle with weight and metabolism. The gene is running an old program — and the program no longer matches the environment.</p>

<p>Kurzweil's insight is that this is not a tragedy of biology. It's a software problem. And software can be updated.</p>

<p>Every process in your body — growth, repair, immunity, aging — is governed by instructions encoded in DNA. Those instructions can, in principle, be read, understood, and rewritten. The question has always been: how do you read four billion letters of genetic code fast enough, and understand them well enough, to know which ones to change?</p>

<p>The answer is: you need a machine that is very, very good at finding patterns in enormous amounts of data. That machine is now being built. It's called artificial general intelligence.</p>

<h2>What AI Is Already Doing to Medicine</h2>

<p>To understand what comes after AGI, it helps to see what AI is doing right now — before it has even reached human-level general intelligence.</p>

<p>When COVID-19 arrived in 2020, the traditional process for developing a vaccine takes five to ten years. Researchers hypothesize, test, fail, repeat. Thousands of human volunteers. Years of trials. The Moderna vaccine used a different approach. AI generated <em>several billion possible mRNA sequences</em>, ran biological simulations on all of them, and identified the optimal one in two days. The vaccine that emerged is still in use today.</p>

<p>This is the model for what comes next. Instead of scientists guessing what might work, AI proposes candidates. Instead of running trials on hundreds of people over years, simulations test on a million virtual patients in days. Instead of understanding one disease at a time, AI reads the entire medical literature — every study, every clinical record — and finds connections no human team could spot.</p>

<p>Kurzweil predicts this approach will, in the coming years, produce breakthroughs against cancer, Alzheimer's disease, heart disease, and diabetes — not by inventing new biology, but by finally understanding the biology we already have.</p>

<h2>The Race Against Your Own Clock</h2>

""" + SVG_ESCAPE_VELOCITY + """

<p>The phrase Kurzweil uses is "longevity escape velocity." It sounds like rocket science because it borrows from rocket science — but the idea is simple.</p>

<p>Right now, medical progress adds roughly four months of additional life expectancy every year. That means for every year you live, you lose about eight months to aging and gain back four from science — a net loss of four months. You're running, but the finish line is still getting closer.</p>

<p>By 2029, Kurzweil predicts something will change. Medical progress — accelerated by AI — will add a full year of life expectancy for every year that passes. You'll be running just fast enough to stay even. The finish line stops moving toward you.</p>

<p>After that, the curve bends upward. By 2032, you'll be gaining more than a year for every year lived. The finish line will start moving away. People alive today, who are careful about their health and live to see that inflection point, could in principle live for centuries — not because science made them immortal, but because every year brings enough new medicine to more than offset that year's aging.</p>

<p>This is not a guarantee. Kurzweil is explicit about that. You could still die in an accident. The progress depends on research actually happening at the pace he predicts. But the arithmetic — if the trend lines are correct — is real.</p>

<h2>Tiny Doctors in Your Blood</h2>

""" + SVG_NANOBOTS + """

<p>The technology Kurzweil is most vivid about is also the most science-fictional-sounding: nanobots. Microscopic robots, small enough to travel through your bloodstream alongside red blood cells, designed to patrol your body and fix things that break.</p>

<p>He uses a simple observation to explain why this is plausible rather than fantasy: everything keeps getting smaller. The computing power that once required a building now fits in your pocket. What fits in your pocket today will, following the same exponential curve, fit inside a blood cell within decades. We are not inventing new physics; we are just following the trajectory of miniaturisation that has been running since the 1950s.</p>

<p>In Kurzweil's vision for the 2030s, these nanobots would:</p>

<ul>
  <li><strong>Patrol your bloodstream continuously</strong> — looking for damaged cells, pathogens, and early signs of disease, the way a smoke detector monitors a room around the clock</li>
  <li><strong>Repair cells before they fail</strong> — fixing the molecular damage that accumulates with age, rather than waiting for that damage to produce a disease that doctors then treat</li>
  <li><strong>Remove toxins and metabolic waste</strong> — clearing the cellular debris that aging produces and that the body's natural cleaning systems gradually lose the ability to handle</li>
  <li><strong>Enter the brain</strong> — travelling through the tiny blood vessels (capillaries) that run through brain tissue, where they could detect and address the early changes of Alzheimer's decades before symptoms appear</li>
</ul>

<p>The shift this represents is enormous. Today, medicine is largely <em>reactive</em>: we wait for disease to declare itself, then try to treat it. Nanobots would make medicine <em>preventive at the cellular level</em> — catching and correcting damage the moment it begins, before it ever becomes a disease at all.</p>

<h2>The Brain Gets an Upgrade</h2>

<p>Kurzweil's predictions for health don't stop at the bloodstream. By the 2030s, he also predicts that nanobots will create a physical bridge between the human brain and cloud-based computing — entering through the tiny capillaries that thread through the brain and connecting our neurons to artificial intelligence systems outside the body.</p>

<p>This sounds alarming, and Kurzweil acknowledges that many people's first reaction is discomfort. But he points out that we are already extending our minds into machines. Your smartphone is, in a meaningful sense, an extension of your memory. You know things — how to get somewhere, what a word means, the name of a film — that you would not know without it. The difference he's describing is that the connection becomes faster, richer, and eventually invisible.</p>

<p>The health implications of this brain connection are specific:</p>

<p>First, it allows continuous monitoring of brain chemistry and neural activity — detecting the very first molecular signs of dementia, depression, or other neurological changes long before they affect behaviour. Second, it allows intervention at that early stage, with nanobots adjusting neurotransmitter levels or repairing cellular damage before it compounds. Third — and most strangely — Kurzweil predicts that by 2045, the information that constitutes your mind will be able to be captured and stored: your memories, your personality, the pattern of connections between your neurons. A backup, in effect.</p>

<h2>The Bigger Picture: 2045</h2>

<p>All of these technologies converge, in Kurzweil's framing, at a point he calls the Singularity — around 2045 — when human intelligence, augmented and merged with artificial intelligence, will be so far beyond what it is today that predicting what happens afterwards is nearly impossible.</p>

<p>He uses a deliberate analogy. If you asked a mouse what it would be like to have human intelligence, the mouse cannot even form the question. The gap between mouse cognition and human cognition is simply too large. The gap between human cognition in 2025 and human-AI hybrid cognition in 2045, Kurzweil suggests, is comparable. We cannot fully imagine what beings that intelligent will understand about biology, disease, and the body.</p>

<p>What we can say is this: the problems that today seem like fundamental limits — cancer, neurodegeneration, the wearing out of cells and organs — are, in his framework, engineering problems. They are hard engineering problems. But they are problems of information: how genes are expressed, how proteins fold, how cells communicate, how damage accumulates. And engineering problems, given enough intelligence and enough tools, get solved.</p>

<h2>The One Thing Required of You</h2>

<p>Kurzweil is careful to say that none of this is automatic. The escape velocity scenario — where each year of your life buys you more than a year of extended life expectancy — applies to people who are "diligent." That word carries weight.</p>

<p>The diligent thing, right now, is the familiar and unglamorous list: sleep enough, eat in a way that doesn't accelerate metabolic damage, move your body, avoid the things that are known to shorten life. Not because these are permanent solutions, but because they keep you in the race long enough to reach the finish line that, if Kurzweil is right, is about to start moving away from you.</p>

<p>The goal is to live well enough, for long enough, to reach the point where the technology does the rest.</p>

<p>Whether or not you believe the timeline — and there are thoughtful people who think Kurzweil is too optimistic, and others who think he's too conservative — the underlying logic is harder to dismiss than it once was. AI is already accelerating drug discovery. Gene therapy is becoming real. The exponential curves are measurable. The direction of travel is clear.</p>

<p>The question is whether you'll be around to see where it leads.</p>

<p style="color:#64748b;font-size:0.9rem;margin-top:2em;border-top:1px solid #1e293b;padding-top:1em;">Synthesized from Ray Kurzweil's lectures, interviews, and books — including <em>The Singularity Is Near</em> (2005), <em>The Singularity Is Nearer</em> (2024), TIME magazine interviews, TED talks, and conversations with Lex Fridman, Peter Diamandis, and others.</p>"""

ARTICLE = {
    "title": "After AGI: What Happens to Your Body",
    "slug": "kurzweil-agi-health-future",
    "summary": "Ray Kurzweil's predictions for medicine after artificial general intelligence — nanobots, longevity escape velocity, and why aging may become optional by the 2030s.",
    "content": ARTICLE_BODY,
    "published": True,
    "order": 1,
}


class Command(BaseCommand):
    help = "Load Ray Kurzweil AGI and health article into longevity pillar"

    def handle(self, *args, **kwargs):
        pillar, created = Pillar.objects.get_or_create(
            slug=PILLAR["slug"],
            defaults={k: v for k, v in PILLAR.items() if k != "slug"},
        )
        verb = "Created" if created else "Found"
        self.stdout.write(f"{verb} pillar: {pillar.name}")

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
