from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

PILLAR = {
    "name": "Autoimmune Disease",
    "slug": "autoimmune-disease",
    "description": (
        "How autoimmune diseases start, why your immune system attacks your own body, "
        "and what the clinical evidence says about reversing them through diet."
    ),
    "icon": "🛡",
    "color": "violet",
    "order": 5,
}

SVG_ILLUSTRATION = """
<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 410" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;" role="img" aria-label="5-step diagram showing how a leaky gut triggers autoimmune disease">
  <defs>
    <marker id="ai-arr" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#334155"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="720" height="410" fill="#090d1a" rx="16"/>

  <!-- Title -->
  <text x="360" y="32" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="14" fill="#f1f5f9" font-weight="700" letter-spacing="-0.2">How a Leaky Gut Triggers Autoimmune Disease</text>
  <text x="360" y="49" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" fill="#475569">Dr. Zsófia Clemens · Paleomedicina Hungary</text>

  <!-- =============================================================
       ROW 1: Five step circles   cy=128, r=50
       cx: 72, 216, 360, 504, 648
  ============================================================= -->

  <!-- STEP 1 · Gut-Damaging Foods -->
  <circle cx="72" cy="128" r="50" fill="#172033" stroke="#1d4ed8" stroke-width="1.5"/>
  <circle cx="108" cy="88"  r="10" fill="#1d4ed8"/>
  <text x="108" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="white" font-weight="700">1</text>
  <!-- Bread icon -->
  <rect x="50" y="118" width="44" height="20" rx="3" fill="#92400e"/>
  <rect x="50" y="112" width="44" height="14" rx="6" fill="#b45309"/>
  <line x1="61" y1="113" x2="61" y2="132" stroke="#78350f" stroke-width="1.2"/>
  <line x1="72" y1="111" x2="72" y2="132" stroke="#78350f" stroke-width="1.2"/>
  <line x1="83" y1="113" x2="83" y2="132" stroke="#78350f" stroke-width="1.2"/>
  <text x="72" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Gut-Damaging</text>
  <text x="72" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Foods Eaten</text>
  <text x="72" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">Grains · lectins</text>
  <text x="72" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">processed foods</text>

  <!-- Arrow 1→2 -->
  <line x1="124" y1="128" x2="161" y2="128" stroke="#334155" stroke-width="2" marker-end="url(#ai-arr)"/>

  <!-- STEP 2 · Gut Wall Breaks Open -->
  <circle cx="216" cy="128" r="50" fill="#1a0f2a" stroke="#7c3aed" stroke-width="1.5"/>
  <circle cx="252" cy="88"  r="10" fill="#7c3aed"/>
  <text x="252" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="white" font-weight="700">2</text>
  <!-- 4 gut epithelial cells -->
  <rect x="190" y="111" width="10" height="32" rx="2" fill="#15803d"/>
  <rect x="203" y="111" width="10" height="32" rx="2" fill="#15803d"/>
  <!-- crack between cells 2 and 3 -->
  <path d="M214,111 L211,127 L218,127 L215,143" stroke="#dc2626" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <rect x="224" y="111" width="10" height="32" rx="2" fill="#15803d"/>
  <rect x="237" y="111" width="10" height="32" rx="2" fill="#15803d"/>
  <!-- protein triangle leaking through crack -->
  <polygon points="215,144 209,155 221,155" fill="#f97316"/>
  <text x="216" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Gut Wall</text>
  <text x="216" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Breaks Open</text>
  <text x="216" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">Tight junctions</text>
  <text x="216" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">rupture → leaky gut</text>

  <!-- Arrow 2→3 -->
  <line x1="268" y1="128" x2="305" y2="128" stroke="#334155" stroke-width="2" marker-end="url(#ai-arr)"/>

  <!-- STEP 3 · Proteins Flood Bloodstream -->
  <circle cx="360" cy="128" r="50" fill="#1a0a0a" stroke="#b91c1c" stroke-width="1.5"/>
  <circle cx="396" cy="88"  r="10" fill="#b91c1c"/>
  <text x="396" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="white" font-weight="700">3</text>
  <!-- Blood vessel -->
  <ellipse cx="360" cy="126" rx="36" ry="20" fill="#7f1d1d" opacity="0.9"/>
  <!-- protein triangles -->
  <polygon points="344,120 340,132 348,132" fill="#f97316"/>
  <polygon points="362,117 358,129 366,129" fill="#fb923c"/>
  <polygon points="378,121 374,132 382,132" fill="#f97316" opacity="0.8"/>
  <text x="360" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Proteins Flood</text>
  <text x="360" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Bloodstream</text>
  <text x="360" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">Immune system</text>
  <text x="360" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">spots invaders</text>

  <!-- Arrow 3→4 -->
  <line x1="412" y1="128" x2="449" y2="128" stroke="#334155" stroke-width="2" marker-end="url(#ai-arr)"/>

  <!-- STEP 4 · Immune System Attacks Own Body -->
  <circle cx="504" cy="128" r="50" fill="#1a1000" stroke="#d97706" stroke-width="1.5"/>
  <circle cx="540" cy="88"  r="10" fill="#d97706"/>
  <text x="540" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="white" font-weight="700">4</text>
  <!-- Immune cell: circle with 8 spikes -->
  <circle cx="504" cy="125" r="14" fill="#d97706" opacity="0.9"/>
  <line x1="504" y1="107" x2="504" y2="101" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="514" y1="110" x2="519" y2="105" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="518" y1="121" x2="524" y2="120" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="514" y1="132" x2="519" y2="137" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="504" y1="139" x2="504" y2="145" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="494" y1="132" x2="489" y2="137" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="490" y1="121" x2="484" y2="120" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="494" y1="110" x2="489" y2="105" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Antibody Y-shape inside -->
  <path d="M504,123 L500,116 M504,123 L508,116 M504,123 L504,130" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <text x="504" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Immune System</text>
  <text x="504" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Attacks Own Body</text>
  <text x="504" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">Antibodies target</text>
  <text x="504" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">your own tissues</text>

  <!-- Arrow 4→5 -->
  <line x1="556" y1="128" x2="593" y2="128" stroke="#334155" stroke-width="2" marker-end="url(#ai-arr)"/>

  <!-- STEP 5 · Cytokines Spread Inflammation -->
  <circle cx="648" cy="128" r="50" fill="#1a0808" stroke="#dc2626" stroke-width="1.5"/>
  <circle cx="684" cy="88"  r="10" fill="#dc2626"/>
  <text x="684" y="92" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="white" font-weight="700">5</text>
  <!-- Starburst / explosion -->
  <circle cx="648" cy="125" r="13" fill="#dc2626" opacity="0.85"/>
  <line x1="648" y1="108" x2="648" y2="102" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="658" y1="111" x2="663" y2="106" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="662" y1="121" x2="668" y2="120" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="658" y1="131" x2="663" y2="136" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="648" y1="138" x2="648" y2="144" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="638" y1="131" x2="633" y2="136" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="634" y1="121" x2="628" y2="120" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="638" y1="111" x2="633" y2="106" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <text x="648" y="123" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7"   fill="white" font-weight="700">TNF-α</text>
  <text x="648" y="131" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7"   fill="white">IL-6  IL-1β</text>
  <text x="648" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Cytokines</text>
  <text x="648" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#e2e8f0" font-weight="600">Spread Inflammation</text>
  <text x="648" y="188" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">Chronic systemic</text>
  <text x="648" y="199" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#64748b">inflammation</text>

  <!-- Divider -->
  <line x1="20" y1="216" x2="700" y2="216" stroke="#1e293b" stroke-width="1"/>
  <rect x="280" y="208" width="160" height="16" rx="4" fill="#090d1a"/>
  <text x="360" y="220" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5" fill="#475569" letter-spacing="0.1em">DISEASES THAT RESULT</text>

  <!-- =============================================================
       ROW 2: Disease boxes   y=227, height=107
       x: 16, 191, 366, 541   width=163   centers: 97, 272, 448, 622
  ============================================================= -->

  <!-- Crohn's Disease -->
  <rect x="16"  y="227" width="163" height="107" rx="10" fill="#0a1a0a" stroke="#15803d" stroke-width="1.5"/>
  <path d="M57,249 C49,249 46,257 51,262 C56,267 65,266 70,260 C75,254 83,253 87,259" stroke="#22c55e" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <text x="97"  y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#4ade80" font-weight="700">Crohn's Disease</text>
  <text x="97"  y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">Gut lining attacked</text>
  <text x="97"  y="311" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">by immune cells</text>
  <text x="97"  y="327" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#475569">Also: IBD, colitis</text>

  <!-- Type 1 Diabetes -->
  <rect x="191" y="227" width="163" height="107" rx="10" fill="#1a0f00" stroke="#d97706" stroke-width="1.5"/>
  <path d="M272,243 C272,243 264,255 264,261 C264,269 272,273 272,273 C272,273 280,269 280,261 C280,255 272,243 272,243 Z" fill="#fbbf24" opacity="0.85"/>
  <text x="272" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#fbbf24" font-weight="700">Type 1 Diabetes</text>
  <text x="272" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">Pancreas beta cells</text>
  <text x="272" y="311" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">destroyed by immune</text>
  <text x="272" y="327" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#475569">Also: LADA diabetes</text>

  <!-- Hashimoto's -->
  <rect x="366" y="227" width="163" height="107" rx="10" fill="#0a0f20" stroke="#3b82f6" stroke-width="1.5"/>
  <!-- Thyroid butterfly: two lobes + isthmus centered at 448 -->
  <ellipse cx="436" cy="251" rx="15" ry="11" fill="#3b82f6" opacity="0.65"/>
  <ellipse cx="462" cy="251" rx="15" ry="11" fill="#3b82f6" opacity="0.65"/>
  <ellipse cx="449" cy="251" rx="7"  ry="8"  fill="#1d4ed8" opacity="0.85"/>
  <text x="448" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#60a5fa" font-weight="700">Hashimoto's</text>
  <text x="448" y="297" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">Thyroid attacked,</text>
  <text x="448" y="311" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">hormones disrupted</text>
  <text x="448" y="327" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9"    fill="#475569">Also: Graves' disease</text>

  <!-- Rheumatoid Arthritis -->
  <rect x="541" y="227" width="163" height="107" rx="10" fill="#1a0808" stroke="#dc2626" stroke-width="1.5"/>
  <!-- Joint icon -->
  <rect x="608" y="241" width="28" height="9" rx="3" fill="#ef4444" opacity="0.8"/>
  <circle cx="622" cy="258" r="8" fill="#fca5a5" opacity="0.9"/>
  <rect x="608" y="264" width="28" height="9" rx="3" fill="#ef4444" opacity="0.8"/>
  <text x="622" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#f87171" font-weight="700">Rheumatoid</text>
  <text x="622" y="294" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12.5" fill="#f87171" font-weight="700">Arthritis</text>
  <text x="622" y="311" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">Joints attacked,</text>
  <text x="622" y="325" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10"   fill="#94a3b8">swollen and painful</text>

  <!-- The Fix bar -->
  <rect x="16"  y="345" width="688" height="52" rx="10" fill="#061a0e" stroke="#15803d" stroke-width="1.5"/>
  <text x="360" y="365" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10.5" fill="#4ade80" font-weight="700">THE FIX: Remove gut-damaging foods</text>
  <text x="360" y="381" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9.5"  fill="#94a3b8">Gut wall heals → tight junctions restore → proteins stop leaking → immune alarm stops → disease reverses</text>
  <text x="360" y="393" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8.5"  fill="#475569">PKD normalizes intestinal permeability within 3–4 weeks (confirmed by PEG permeability test, Paleomedicina Hungary)</text>

</svg>
<figcaption style="text-align:center;font-size:13px;color:var(--fg-3,#64748b);margin-top:10px;font-style:italic;">
  Based on Dr. Zsófia Clemens' clinical model, Paleomedicina Hungary. PKD = Paleolithic Ketogenic Diet.
</figcaption>
</figure>
"""

ARTICLE_CONTENT = SVG_ILLUSTRATION + """
<h2>Your immune system is not broken — it is responding to a real trigger</h2>

<p>Autoimmune disease is one of medicine's greatest puzzles. Why would the body attack itself? The conventional answer is that something went wrong with the immune system. But Dr. Zsófia Clemens, a neurobiologist and clinical researcher at Paleomedicina in Hungary, has spent over a decade showing that the real problem is not in the immune system at all — it starts much earlier, in the gut.</p>

<p>According to Dr. Clemens, autoimmune disease follows a predictable chain: the wrong foods damage the gut wall, the gut becomes leaky, proteins escape into the bloodstream, the immune system detects them as foreign invaders, and in trying to destroy those invaders, it accidentally attacks the body's own tissues. Understanding this chain is the first step to reversing it.</p>

<h2>Step 1 — What starts it: foods that damage the gut</h2>

<p>Your digestive tract is about 7 meters long and its inner wall is only one cell thick in places. Those cells are the only barrier between everything you eat and the rest of your body. Under a microscope, the cells are packed tightly together, held shut by structures called <strong>tight junctions</strong> — think of them as a zipper running between every adjacent cell.</p>

<p>When everything is working correctly, only fully digested nutrients — single amino acids from proteins, simple sugars from carbohydrates, fatty acids from fats — pass through this barrier in a carefully controlled way. Large, undigested food molecules cannot get through. That is the design.</p>

<p>Certain foods interfere with this design. Dr. Clemens identifies foods that contain compounds capable of loosening or breaking those tight junctions — allowing things through that should never enter your bloodstream. These foods include grains (especially those containing gluten), many other plant foods containing compounds called lectins and phytates, and highly processed foods with chemical additives. These are staples of the modern Western diet.</p>

<h2>Step 2 — The gut becomes leaky</h2>

<p>When tight junctions are damaged repeatedly over time, gaps open up between gut cells. This is what doctors and researchers call <strong>intestinal permeability</strong> — or, in plain language, a <em>leaky gut</em>.</p>

<p>The gut still has two jobs — absorb nutrients and act as a barrier — but it is now failing at the second job. Like a cracked dam, things that should stay on one side are getting through to the other.</p>

<p>This is not a fringe theory. Elevated intestinal permeability is measurable with a clinical test called the PEG test (polyethylene glycol), in which molecules of different sizes are swallowed and their recovery in urine is tracked. Anything that makes it through the gut wall when it should not shows up clearly. Dr. Clemens' clinic has been measuring this in hundreds of patients since 2015.</p>

<h2>Step 3 — Food proteins flood the bloodstream</h2>

<p>With a leaky gut, large food protein fragments — proteins that have not been fully broken down into their individual amino acid pieces — slip through the damaged wall and enter the bloodstream. Your immune system has never been designed to encounter these molecules circulating in blood. It has only ever expected to see them inside the digestive tract, where they belong.</p>

<p>The moment those proteins reach the bloodstream, alarm bells go off. Your immune system treats them exactly as it would treat bacteria or a virus — as foreign invaders that must be destroyed.</p>

<h2>Step 4 — The immune system makes a terrible mistake</h2>

<p>Your immune system is extraordinarily good at recognizing and attacking foreign proteins. It does this by creating antibodies — specialized molecules that lock onto a specific target and mark it for destruction. The problem here is one of <strong>mistaken identity</strong>.</p>

<p>Some of the food proteins that leak through have a shape that closely resembles the proteins that make up your own body's tissues. The immune system — working exactly as intended — makes antibodies against the food protein. But those same antibodies then also target your own tissues, because they look similar enough to be confused for the enemy.</p>

<p>This is the "autoimmune" attack: your immune system is not malfunctioning. It is doing its job competently. It just has the wrong target, because the trigger that set it off came from outside the gut where it should never have appeared.</p>

<p>Which tissues get attacked depends on which proteins leaked through and which of your tissues happen to look similar to those proteins:</p>

<ul>
<li><strong>If the antibodies target the gut lining itself</strong> → Crohn's disease or ulcerative colitis</li>
<li><strong>If they target the beta cells in the pancreas</strong> → Type 1 diabetes</li>
<li><strong>If they target the thyroid gland</strong> → Hashimoto's (underactive thyroid) or Graves' disease (overactive thyroid)</li>
<li><strong>If they target joint tissues</strong> → Rheumatoid arthritis</li>
</ul>

<h2>Step 5 — Cytokines spread the fire everywhere</h2>

<p>Once the immune system is activated, it does not just send antibodies. It also releases chemical alarm signals called <strong>cytokines</strong> — molecules like TNF-alpha, IL-6, and IL-1 beta — that spread the inflammatory signal throughout the body. Think of cytokines as a fire alarm that, once triggered, makes every smoke detector in the building go off at once.</p>

<p>This systemic inflammation is what causes the fatigue, pain, brain fog, swelling, and general feeling of illness that accompany autoimmune conditions. It is not just the targeted organ that suffers — the entire body is living in a state of chemical emergency.</p>

<blockquote>
<p>"The foods that are causing an increased intestinal permeability are the cause responsible for a wide area of autoimmune diseases and cancer. Since the PKD excludes these food items, there is a way to reverse this condition."</p>
<p style="font-size:14px;margin-top:6px;">— Dr. Zsófia Clemens, Paleomedicina Hungary</p>
</blockquote>

<h2>Why standard medical treatment does not fix the root cause</h2>

<p>The standard approach to autoimmune disease focuses on suppressing the immune system — using medications like steroids, methotrexate, or biologics that turn down the immune response. This can reduce symptoms and slow damage, but it does not address why the immune system is attacking in the first place.</p>

<p>It is like unplugging a fire alarm instead of putting out the fire. The alarm stops, which brings relief — but the fire (the leaky gut, the proteins entering the bloodstream) is still burning.</p>

<p>Other common interventions that have been tried — probiotics, prebiotics, colostrum supplements, FODMAP diets, fecal transplantation — have shown some benefit for symptoms or gut bacteria composition, but none have reliably normalized elevated intestinal permeability. A 2014 clinical study of a regular paleolithic diet found it improved weight and glucose control but had no meaningful effect on intestinal permeability or inflammation levels — the two things that actually drive autoimmune disease.</p>

<h2>The domino effect: one autoimmune disease leads to the next</h2>

<p>One of the most important and overlooked observations in Dr. Clemens' clinical practice is this: if the root cause (the leaky gut) is not addressed, autoimmune disease tends to spread and accumulate. Because the trigger — food proteins entering the bloodstream — is continuous, the immune system keeps encountering new targets.</p>

<p>She has observed a common sequence in children: it often starts with eczema, then allergy develops, then asthma, and later Crohn's disease and Type 1 diabetes appear together. Each new condition is not a separate bad luck event — it is the same underlying cause finding new tissue to attack.</p>

<p>This also explains why people with one autoimmune condition are statistically much more likely to develop a second or third one over their lifetime. Medicine treats each disease separately. The leaky gut model explains them as a single root problem with multiple expressions.</p>

<h2>The clinical evidence: what reversal looks like</h2>

<p>Dr. Clemens' clinic has documented dozens of patients achieving complete reversal of autoimmune conditions using the Paleolithic Ketogenic Diet (PKD) — a meat and fat-based diet, built around four-legged animals and organ meats, that eliminates all foods known to damage the gut lining.</p>

<p>The evidence is measured, not anecdotal. PEG intestinal permeability tests in patients starting PKD show normalization of elevated gut permeability within <strong>3 to 4 weeks</strong>. Inflammation markers (CRP and ESR) drop. Antibody levels fall. And symptoms resolve — often completely.</p>

<p>Notable documented cases include:</p>

<ul>
<li>A young man with severe Crohn's disease, facing surgery, who achieved complete remission on PKD. He is medicine-free, disease-free, and has now been followed for seven years. His case was the first documented normalization of intestinal permeability by any dietary intervention, published in 2016.</li>
<li>Children with new-onset Type 1 diabetes where PKD was able to preserve and in some cases increase the pancreas's own insulin production — something not achieved by any other known intervention.</li>
<li>A woman with Hashimoto's thyroiditis of 16 years who was able to taper off thyroid medication after starting PKD.</li>
<li>A child with juvenile rheumatoid arthritis whose joint swelling, edema, and pain resolved within 3 weeks, allowing medication to be reduced.</li>
</ul>

<h2>The key insight for anyone with an autoimmune condition</h2>

<p>Your immune system is not your enemy. In autoimmune disease, it is doing its job correctly — detecting and attacking what it has been shown as a foreign threat. The problem is upstream: food compounds are entering the bloodstream where they do not belong, because the gut wall that should block them has been damaged.</p>

<p>The path forward is to remove the foods that cause the damage, allow the gut wall to heal, and give the immune system nothing left to alarm it. When the trigger disappears, the alarm stops. When the alarm stops, the attack on your own tissues stops. And when that stops, the disease — in many cases — reverses.</p>

<p>This is not about managing symptoms for life. It is about removing the cause.</p>

<hr style="margin:2em 0;border-color:var(--hairline);">

<p style="font-size:14px;color:var(--fg-3,#64748b);line-height:1.6;">
<strong>Source:</strong> Dr. Zsófia Clemens, "Autoimmune Disease: Root Causes &amp; Reversal Using PKD," YouTube, 2022 (<a href="https://www.youtube.com/watch?v=olwgCf_1d98" rel="noopener noreferrer" target="_blank" style="color:inherit;">youtu.be/olwgCf_1d98</a>). Dr. Clemens is a neurobiologist and clinical researcher, CEO of ICMNI – Paleomedicina, Budapest, Hungary. The Paleomedicina team has published peer-reviewed case studies on PKD in autoimmune disease and cancer in journals including the <em>International Journal of Case Reports and Images</em> and <em>Frontiers in Nutrition</em>.
</p>
"""


class Command(BaseCommand):
    help = "Load Dr. Zsófia Clemens autoimmune disease article with SVG illustration"

    def add_arguments(self, parser):
        parser.add_argument(
            "--publish",
            action="store_true",
            help="Mark the article as published immediately",
        )

    def handle(self, *args, **options):
        pillar, pillar_created = Pillar.objects.get_or_create(
            slug=PILLAR["slug"],
            defaults={
                "name":        PILLAR["name"],
                "description": PILLAR["description"],
                "icon":        PILLAR["icon"],
                "color":       PILLAR["color"],
                "order":       PILLAR["order"],
            },
        )
        if pillar_created:
            self.stdout.write(f"  Created pillar: {pillar.name}")
        else:
            self.stdout.write(f"  Using existing pillar: {pillar.name}")

        publish = options["publish"]
        article, created = Article.objects.update_or_create(
            slug="leaky-gut-autoimmune-root-cause",
            defaults={
                "title":   "Why Your Immune System Attacks You: The Leaky Gut Root Cause of Autoimmune Disease",
                "summary": (
                    "Dr. Zsófia Clemens has shown that autoimmune disease begins not in the immune system — "
                    "but in the gut. When the wrong foods damage your gut wall, foreign proteins flood your "
                    "bloodstream, trigger a mistaken immune attack on your own tissues, and spark a cascade "
                    "of chronic inflammation."
                ),
                "ai_summary": (
                    "Autoimmune disease is not a broken immune system. It begins when certain foods damage "
                    "the gut lining, proteins leak into the bloodstream, and the immune system — doing its "
                    "job — mistakes your own tissues for invaders. Remove the gut-damaging foods, the "
                    "barrier heals, the immune trigger disappears, and in many cases the disease reverses. "
                    "Dr. Clemens' clinic has confirmed gut permeability normalization within 3–4 weeks "
                    "on the Paleolithic Ketogenic Diet, with complete remission in Crohn's, Type 1 diabetes, "
                    "Hashimoto's, Graves' disease, and rheumatoid arthritis."
                ),
                "content":   ARTICLE_CONTENT,
                "pillar":    pillar,
                "order":     1,
                "published": publish,
            },
        )
        action = "Created" if created else "Updated"
        status = "published" if publish else "draft"
        self.stdout.write(f"  {action} article ({status}): {article.title}")

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. Article {'published' if publish else 'saved as draft — run with --publish to make live'}."
        ))
