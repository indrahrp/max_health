from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

# ── helpers ──────────────────────────────────────────────────────────────────

def svg(disease_title, accent, stage1_label, stage2_label, stage3_label,
        stage1_shapes, stage2_shapes, stage3_shapes,
        stage1_note='', stage2_note='', stage3_note=''):
    """Build a 3-stage disease-process SVG (720×400, dark bg)."""
    arrow = (
        '<defs>'
        f'<marker id="ar{accent[1:]}" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto">'
        '<path d="M0,0 L7,3 L0,6 Z" fill="#475569"/>'
        '</marker>'
        '</defs>'
    )
    mid = f'ar{accent[1:]}'

    def panel(cx, label, shapes, note, step_num):
        num_circle = f'<circle cx="{cx-80}" cy="52" r="12" fill="{accent}"/><text x="{cx-80}" y="57" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="white" font-weight="700">{step_num}</text>'
        bg = f'<circle cx="{cx}" cy="200" r="100" fill="#111827" stroke="{accent}" stroke-width="1.2" stroke-opacity=".55"/>'
        lbl = f'<text x="{cx}" y="325" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#e2e8f0" font-weight="600">{label}</text>'
        nt = f'<text x="{cx}" y="342" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#64748b">{note}</text>' if note else ''
        return num_circle + bg + shapes + lbl + nt

    p1 = panel(120, stage1_label, stage1_shapes, stage1_note, '1')
    p2 = panel(360, stage2_label, stage2_shapes, stage2_note, '2')
    p3 = panel(600, stage3_label, stage3_shapes, stage3_note, '3')

    arrows = (
        f'<line x1="222" y1="200" x2="258" y2="200" stroke="#475569" stroke-width="2" marker-end="url(#{mid})"/>'
        f'<line x1="462" y1="200" x2="498" y2="200" stroke="#475569" stroke-width="2" marker-end="url(#{mid})"/>'
    )

    title_svg = (
        f'<text x="360" y="32" text-anchor="middle" font-family="system-ui,sans-serif" '
        f'font-size="14" fill="#f1f5f9" font-weight="700">{disease_title}</text>'
    )

    return (
        f'<figure style="margin:1.5em 0 2.5em;">'
        f'<svg viewBox="0 0 720 370" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;border-radius:16px;" role="img" aria-label="{disease_title} disease process diagram">'
        f'<rect width="720" height="370" fill="#090d1a" rx="16"/>'
        + arrow + title_svg + p1 + arrows + p2 + p3 +
        f'</svg></figure>'
    )


# ── 15 disease articles ───────────────────────────────────────────────────────

ARTICLES = []

# 1. LUPUS ─────────────────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Lupus: When Antibodies Attack Your Own DNA',
    'slug': 'lupus-sle-autoimmune',
    'summary': (
        'In lupus, the immune system produces antibodies against the body\'s own DNA. '
        'Those antibodies form immune complexes that lodge in the kidneys, skin, and joints — '
        'triggering inflammation in organs throughout the body.'
    ),
    'content': svg(
        'Lupus (SLE): How Anti-DNA Antibodies Damage Organs',
        '#6366f1',
        'Healthy Nucleus', 'Antibody Formation', 'Immune Complex Damage',
        # stage 1 – nucleus with DNA
        (
            '<ellipse cx="120" cy="200" rx="55" ry="45" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.4"/>'
            '<path d="M98,183 Q108,175 118,183 Q128,191 138,183" stroke="#a5b4fc" stroke-width="2" fill="none"/>'
            '<path d="M98,193 Q108,185 118,193 Q128,201 138,193" stroke="#a5b4fc" stroke-width="2" fill="none"/>'
            '<path d="M98,203 Q108,195 118,203 Q128,211 138,203" stroke="#a5b4fc" stroke-width="2" fill="none"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#818cf8">DNA in nucleus</text>'
        ),
        # stage 2 – DNA fragments + Y-antibodies
        (
            '<line x1="340" y1="178" x2="355" y2="165" stroke="#a5b4fc" stroke-width="1.5"/>'
            '<line x1="355" y1="165" x2="370" y2="178" stroke="#a5b4fc" stroke-width="1.5"/>'
            '<line x1="355" y1="165" x2="355" y2="145" stroke="#6366f1" stroke-width="2"/>'
            '<circle cx="355" cy="140" r="8" fill="#4338ca"/>'
            '<line x1="335" y1="215" x2="350" y2="202" stroke="#a5b4fc" stroke-width="1.5"/>'
            '<line x1="350" y1="202" x2="365" y2="215" stroke="#a5b4fc" stroke-width="1.5"/>'
            '<line x1="350" y1="202" x2="350" y2="182" stroke="#6366f1" stroke-width="2"/>'
            '<circle cx="350" cy="177" r="8" fill="#4338ca"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#818cf8">Anti-dsDNA antibodies bind</text>'
        ),
        # stage 3 – immune complex in kidney glomerulus
        (
            '<circle cx="600" cy="200" r="38" fill="none" stroke="#6366f1" stroke-width="1.2" stroke-opacity=".6"/>'
            '<circle cx="585" cy="190" r="10" fill="#3730a3" stroke="#6366f1" stroke-width="1"/>'
            '<circle cx="605" cy="185" r="8" fill="#3730a3" stroke="#6366f1" stroke-width="1"/>'
            '<circle cx="615" cy="202" r="9" fill="#3730a3" stroke="#6366f1" stroke-width="1"/>'
            '<circle cx="597" cy="212" r="10" fill="#3730a3" stroke="#6366f1" stroke-width="1"/>'
            '<circle cx="578" cy="207" r="8" fill="#3730a3" stroke="#6366f1" stroke-width="1"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#818cf8">Complexes deposit in glomerulus</text>'
        ),
        'Normal DNA in nucleus', 'DNA fragments escape; B cells make antibodies', 'Immune complexes trigger organ inflammation',
    ) + '''
<h2>What is happening in the body</h2>
<p>Systemic lupus erythematosus begins when the immune system fails to clear dying cells efficiently. Fragments of DNA and nuclear proteins from apoptotic cells enter the circulation, and B cells — primed by a loss of tolerance — begin producing antibodies directed at those fragments. The most specific are anti-double-stranded DNA antibodies (anti-dsDNA), which serve as the key diagnostic marker of the disease.</p>
<p>The antibodies do not attack tissue directly. Instead, they bind their targets and form circulating immune complexes — antigen-antibody clusters that are too large for the kidney to filter cleanly. Those complexes lodge in the basement membranes of the kidney's glomeruli, in the capillaries of the skin, in joint linings, and in small blood vessels throughout the body. Once lodged, they activate complement and draw neutrophils, which release tissue-damaging enzymes.</p>
<p>The kidney injury — lupus nephritis — is the most dangerous complication, progressing to kidney failure in a significant minority of patients if untreated. The butterfly-shaped facial rash, joint pain, and fatigue are the more visible but less life-threatening faces of the same underlying immune complex storm.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Butterfly-shaped malar rash across the cheeks and nose</li>
<li>Joint pain and swelling (arthralgia, non-erosive arthritis)</li>
<li>Extreme fatigue and brain fog</li>
<li>Photosensitivity — rash or flare triggered by sun exposure</li>
<li>Kidney inflammation (proteinuria, haematuria in nephritis)</li>
<li>Serositis — inflammation of the lining around the heart and lungs</li>
<li>Thrombocytopenia, haemolytic anaemia (blood count abnormalities)</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Lupus illustrates the downstream consequences of impaired self-tolerance. The initial trigger is the failure to clear apoptotic cellular debris — a failure that can be amplified by the same intestinal permeability and systemic immune activation described in the leaky gut model. When food-derived peptides with structural similarities to nuclear proteins reach the systemic immune system repeatedly, they may serve as the initial primer that breaks tolerance to self-antigens.</p>
<p>Patients with lupus have consistently elevated markers of intestinal permeability compared to healthy controls, and dysbiosis — particularly overgrowth of certain Proteobacteria — is a reproducible finding. The carnivore and PKD protocol removes the dietary sources of gut barrier disruption and eliminates cross-reactive plant lectins, addressing the upstream driver rather than suppressing the downstream antibody response.</p>

<h2>What the clinical data shows</h2>
<p>Case series from Paleomedicina Hungary document lupus patients achieving sustained clinical remission on the Paleolithic Ketogenic Diet. In one published case, a 23-year-old woman with biopsy-confirmed lupus nephritis — on hydroxychloroquine and mycophenolate — achieved normalization of all renal parameters and negative anti-dsDNA titers within six months of adopting PKD, subsequently tapering all medication. Complement C3 and C4, chronically suppressed, normalized. The mechanism proposed is elimination of the gut permeability that continuously feeds antigenic material into the systemic circulation.</p>

<h2>A life with this condition</h2>
<p><strong>Sarah, 23.</strong> Her face swelled overnight — both cheeks flushed in a butterfly pattern that her GP photographed and sent to a dermatologist the same afternoon. Before that she had been dizzy for two weeks and had lost four kilograms without trying. The blood tests came back showing her kidneys were inflamed; she was started on hydroxychloroquine and told to avoid sunlight. For the next three years, every spring flare arrived on schedule, triggered by an afternoon in a garden or a weekend at the coast. What no one explained clearly was that her immune system had decided her own DNA was an invader — and that the butterfly rash was the least dangerous part of what was happening.</p>
<p><strong>Marcus, 40.</strong> He had been told for three years that his joint pain was from old sporting injuries. He was a former semi-professional footballer and the diagnosis felt plausible. It was only after he developed pleuritis — a stabbing chest pain that worsened with every breath — that his GP ordered the full autoimmune panel. His anti-dsDNA came back at 1:640. He had lupus. Looking back, the fatigue he had attributed to age, the mouth ulcers he had dismissed as stress, and the occasional facial flushing he had blamed on alcohol were all part of the same disease. He had been living with it for years without a name for it.</p>
<p><strong>Aiko, 35.</strong> Her lupus presented not with a rash but with a platelet count of 28,000 — low enough to cause spontaneous bruising across her forearms that her haematologist initially investigated as a blood cancer. The bone marrow biopsy came back normal. It was the haematologist who ordered the ANA panel on a hunch, and it came back at 1:1280 with anti-dsDNA positive. Aiko had never had a rash. She had haemolytic anaemia and thrombocytopenia — her immune system attacking her blood cells with the same antibodies it directed at her kidneys. She had assumed the bruises were from the iron deficiency she already knew about. They were not.</p>
''',
})

# 2. MULTIPLE SCLEROSIS ────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Multiple Sclerosis: The Immune System Strips Nerve Insulation',
    'slug': 'multiple-sclerosis-autoimmune',
    'summary': (
        'In multiple sclerosis, autoreactive T-cells cross the blood-brain barrier and destroy myelin — '
        'the insulating sheath around nerve fibres. Without myelin, electrical signals slow, distort, '
        'and eventually fail, producing the cascading neurological deficits of the disease.'
    ),
    'content': svg(
        'Multiple Sclerosis: T-Cells Strip the Myelin Sheath',
        '#f59e0b',
        'Myelinated Axon', 'T-Cell Attack', 'Demyelinated Axon',
        # stage 1 – myelinated neuron
        (
            '<line x1="68" y1="200" x2="172" y2="200" stroke="#fcd34d" stroke-width="3"/>'
            '<ellipse cx="90" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<ellipse cx="110" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<ellipse cx="130" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<ellipse cx="150" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">Myelin sheaths intact</text>'
        ),
        # stage 2 – T-cells attacking myelin
        (
            '<line x1="308" y1="200" x2="412" y2="200" stroke="#fcd34d" stroke-width="3"/>'
            '<ellipse cx="330" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".5" stroke-dasharray="3 2"/>'
            '<ellipse cx="370" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<ellipse cx="390" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<circle cx="330" cy="175" r="9" fill="#92400e" stroke="#f59e0b" stroke-width="1.2"/>'
            '<line x1="326" y1="168" x2="322" y2="162" stroke="#f59e0b" stroke-width="1"/>'
            '<line x1="333" y1="166" x2="336" y2="160" stroke="#f59e0b" stroke-width="1"/>'
            '<line x1="338" y1="170" x2="344" y2="166" stroke="#f59e0b" stroke-width="1"/>'
            '<line x1="330" y1="184" x2="330" y2="180" stroke="#f59e0b" stroke-width="1.2"/>'
            '<circle cx="350" cy="225" r="9" fill="#92400e" stroke="#f59e0b" stroke-width="1.2"/>'
            '<line x1="350" y1="216" x2="350" y2="220" stroke="#f59e0b" stroke-width="1.2"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">CD8+ T-cells attack myelin</text>'
        ),
        # stage 3 – demyelinated, scarred axon
        (
            '<line x1="548" y1="200" x2="652" y2="200" stroke="#fcd34d" stroke-width="3"/>'
            '<line x1="558" y1="200" x2="558" y2="200" stroke="#dc2626" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
            '<line x1="575" y1="200" x2="575" y2="200" stroke="#dc2626" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
            '<line x1="592" y1="200" x2="592" y2="200" stroke="#dc2626" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
            '<ellipse cx="630" cy="200" rx="12" ry="20" fill="none" stroke="#f59e0b" stroke-width="1.4" opacity=".9"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">Bare axon · signal fails</text>'
            '<text x="574" y="180" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#dc2626">sclerotic plaques</text>'
        ),
        'Intact myelin, fast conduction', 'Autoreactive T-cells cross BBB, attack myelin', 'Demyelination, scarring, signal failure',
    ) + '''
<h2>What is happening in the body</h2>
<p>The central nervous system is normally protected from immune surveillance by the blood-brain barrier — a tightly sealed endothelium that prevents most immune cells from crossing into brain tissue. In MS, that barrier fails at focal points. Autoreactive CD4+ and CD8+ T-cells — primed in the periphery to recognise myelin antigens, particularly myelin basic protein (MBP) — cross into the CNS and initiate an inflammatory cascade.</p>
<p>The T-cells attack the myelin sheath, the fatty insulating layer wrapped around axons by oligodendrocytes. Myelin is not decorative — it enables rapid saltatory conduction, the mechanism by which electrical signals jump between nodes of Ranvier at high speed. When myelin is stripped, conduction slows dramatically. In areas of complete demyelination, transmission fails entirely. Repeated episodes of inflammation leave behind glial scars — the "sclerotic plaques" that give the disease its name — which resist remyelination.</p>
<p>The location of each plaque determines the symptom. Lesions in the optic nerve cause visual disturbance. Lesions in the spinal cord cause limb weakness and bladder dysfunction. Lesions in the cerebellum cause balance problems. Over time, progressive axon loss — even in areas with incomplete demyelination — produces the irreversible neurological decline of secondary progressive MS.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Optic neuritis — blurred or lost vision in one eye, often painful</li>
<li>Numbness, tingling, or electric sensations in limbs (Lhermitte's sign)</li>
<li>Muscle weakness and spasticity</li>
<li>Fatigue disproportionate to activity</li>
<li>Bladder urgency and incontinence</li>
<li>Cognitive difficulties — memory, processing speed</li>
<li>Balance and coordination problems (ataxia)</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>The peripheral priming of myelin-reactive T-cells almost certainly requires an environmental trigger. Molecular mimicry between bacterial or food peptides and myelin antigens is the most studied mechanism. Wheat gliadin shares peptide sequences with MBP; dietary lectins and gut dysbiosis create the systemic immune activation that allows autoreactive clones to escape tolerance. Epidemiological studies show MS prevalence tracking closely with wheat consumption and latitude-based vitamin D deficiency — both downstream effects of the same dietary and lifestyle variables that drive intestinal permeability.</p>

<h2>What the clinical data shows</h2>
<p>Paleomedicina case series include patients with relapsing-remitting MS who achieved sustained remission — no new MRI lesions, no clinical relapses — on the PKD protocol. In several cases, patients who had been on disease-modifying therapy (interferon beta, glatiramer acetate) were able to taper and discontinue medication under clinical supervision after MRI stability was established. The PKD's elimination of gluten, dairy, and processed foods removes the peripheral antigenic triggers while the animal-fat-rich diet provides the cholesterol and saturated fatty acids required for myelin synthesis and repair.</p>

<h2>A life with this condition</h2>
<p><strong>James, 31.</strong> He noticed something wrong when his right foot stopped lifting properly on long runs. By the time he saw a neurologist six weeks later, his right leg felt wrapped in cotton wool and his left eye had given him a week of blurred vision he had attributed to fatigue. The MRI showed nine lesions scattered through the white matter of his brain and along his cervical spine. He was diagnosed with relapsing-remitting MS on a Thursday, sat in the car for an hour unable to drive, and spent the next year learning why rest reliably restored function that exercise took away, and why heat made everything worse.</p>
<p><strong>Rachel, 27.</strong> Her first symptom was pain behind her right eye, followed within days by a grey smear across the centre of her vision. Her optometrist referred her urgently; her ophthalmologist said "optic neuritis" within the first minute of the examination. The neurology referral happened the same day. Her MRI showed two lesions in the white matter — not enough for an MS diagnosis yet, but enough to call it clinically isolated syndrome, which her neurologist explained carried a 50% risk of a second episode within two years. Thirteen months later, she had the second episode. The diagnosis became definitive.</p>
<p><strong>David, 44.</strong> His MS crept in without drama. There was no single devastating episode — just a gradual narrowing of what his body could do. He had begun to notice fatigue so disproportionate to his activity that he stopped mentioning it socially, because no one had a frame of reference for exhaustion that arrived after a short walk. He was eventually diagnosed with primary progressive MS, the form that accumulates disability steadily without distinct relapses. His MRI showed lesions that had been there, silently, for years. There had been no acute event to send him to a doctor sooner.</p>
''',
})

# 3. RHEUMATOID ARTHRITIS ─────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Rheumatoid Arthritis: How Joints Become the Battleground',
    'slug': 'rheumatoid-arthritis-autoimmune',
    'summary': (
        'Rheumatoid arthritis is driven by immune cells that invade the synovial lining of joints, '
        'forming an aggressive pannus tissue that erodes cartilage and bone. '
        'Unlike osteoarthritis, the damage begins in the immune system, not in the joint itself.'
    ),
    'content': svg(
        'Rheumatoid Arthritis: Pannus Erosion of the Joint',
        '#ef4444',
        'Healthy Joint', 'Synovial Invasion', 'Pannus & Bone Erosion',
        # stage 1 – clean joint
        (
            '<rect x="75" y="162" width="45" height="35" rx="4" fill="#374151" stroke="#9ca3af" stroke-width="1.2"/>'
            '<rect x="75" y="197" width="45" height="8" rx="2" fill="#6ee7b7" stroke="#34d399" stroke-width="1"/>'
            '<rect x="75" y="205" width="45" height="8" rx="2" fill="#6ee7b7" stroke="#34d399" stroke-width="1"/>'
            '<rect x="75" y="213" width="45" height="35" rx="4" fill="#374151" stroke="#9ca3af" stroke-width="1.2"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#6ee7b7">Cartilage intact</text>'
        ),
        # stage 2 – inflamed synovium
        (
            '<rect x="315" y="162" width="45" height="35" rx="4" fill="#374151" stroke="#9ca3af" stroke-width="1.2"/>'
            '<path d="M310,200 Q335,190 362,200 Q348,218 322,218 Z" fill="#dc2626" fill-opacity=".7" stroke="#ef4444" stroke-width="1.2"/>'
            '<circle cx="328" cy="208" r="4" fill="#fca5a5"/>'
            '<circle cx="340" cy="204" r="3" fill="#fca5a5"/>'
            '<circle cx="352" cy="208" r="4" fill="#fca5a5"/>'
            '<rect x="315" y="220" width="45" height="28" rx="4" fill="#374151" stroke="#9ca3af" stroke-width="1.2"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Synovial pannus forming</text>'
        ),
        # stage 3 – bone erosion
        (
            '<rect x="555" y="162" width="45" height="30" rx="4" fill="#374151" stroke="#9ca3af" stroke-width="1.2"/>'
            '<path d="M550,192 Q575,180 602,192 Q594,225 560,225 Z" fill="#b91c1c" fill-opacity=".85" stroke="#ef4444" stroke-width="1.3"/>'
            '<path d="M558,193 Q564,197 558,202" stroke="#f87171" stroke-width="1.5" fill="none"/>'
            '<path d="M598,193 Q592,197 598,202" stroke="#f87171" stroke-width="1.5" fill="none"/>'
            '<rect x="555" y="226" width="45" height="20" rx="4" fill="#1f2937" stroke="#6b7280" stroke-width="1" opacity=".7"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Bone eroded by pannus</text>'
        ),
        'Cartilage cushions bone', 'Macrophages, T-cells flood synovium', 'Pannus invades, erodes bone',
    ) + '''
<h2>What is happening in the body</h2>
<p>Rheumatoid arthritis begins not in the joint but in the systemic immune system. The disease is characterised by the production of rheumatoid factor (RF) and anti-citrullinated protein antibodies (ACPA) — antibodies that target citrullinated proteins, which are normal proteins altered by an enzyme called peptidylarginine deiminase. ACPA can appear in the bloodstream years before any joint symptoms, marking the period of immune system priming that precedes clinical disease.</p>
<p>Once the immune response is established, the synovium — the thin membrane lining joint cavities — becomes the target tissue. Macrophages, dendritic cells, and T-cells infiltrate the synovium, secreting TNF-alpha, IL-1, and IL-6, which drive a positive feedback loop of inflammation. The synovium proliferates pathologically, forming a mass of inflammatory tissue called pannus. Pannus is the destructive agent of RA: it invades cartilage and underlying bone, secreting matrix metalloproteinases and osteoclast-activating factors that dissolve both.</p>
<p>The result is progressive joint destruction — initially reversible through medication but ultimately producing the characteristic deformities of advanced RA: ulnar deviation of the fingers, swan-neck and boutonnière deformities, and loss of joint space visible on X-ray.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Symmetrical joint pain and swelling (both hands, both wrists simultaneously)</li>
<li>Morning stiffness lasting more than an hour</li>
<li>Systemic fatigue and low-grade fever</li>
<li>Rheumatoid nodules under the skin at pressure points</li>
<li>Gradual joint deformity if untreated</li>
<li>Extra-articular manifestations: lung fibrosis, vasculitis, eye inflammation</li>
<li>Anaemia of chronic disease</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Citrullination of proteins in the gut — driven by dysbiosis, particularly by Prevotella copri overgrowth, which is consistently elevated in new-onset RA — is the suspected mechanism by which ACPA tolerance breaks. Porphyromonas gingivalis, the periodontal pathogen, produces its own citrullinating enzyme and is strongly linked to RA risk. Both gut and periodontal dysbiosis create systemic exposure to citrullinated antigens, priming the B and T cell response that later targets joint tissue through molecular mimicry.</p>

<h2>What the clinical data shows</h2>
<p>A child with juvenile idiopathic arthritis (the paediatric form of RA) is among the Paleomedicina published case series: joint swelling and pain resolved within weeks of initiating the Paleolithic Ketogenic Diet, and inflammatory markers normalised. Adult RA patients on PKD have reported significant reduction in disease activity scores. The mechanism is thought to involve removal of dietary lectins that trigger Prevotella and Porphyromonas activity, combined with the anti-inflammatory ketone body beta-hydroxybutyrate, which directly inhibits the NLRP3 inflammasome responsible for IL-1 beta secretion.</p>

<h2>A life with this condition</h2>
<p><strong>Maya, 38.</strong> The first sign was her hands in the morning — both of them, which she later learned was important. One stiff hand might be an injury; both at once, mirror-image, was the immune system. She was an architect, and she began arriving an hour early to let the stiffness pass before she needed to use a mouse. Her anti-CCP came back strongly positive. The antibodies had probably been circulating for years before her joints became the target, forming against citrullinated proteins in a silent priming phase. She was told her disease had been active "for a while." Her hands, the tools of her profession, were the battlefield.</p>
<p><strong>Robert, 55.</strong> His RA started in his feet, not his hands — a detail that delayed diagnosis by eighteen months because neither his GP nor his first rheumatology referral thought to examine his metatarsophalangeal joints. He had been told his forefoot pain was Morton's neuroma, then plantar fasciitis. It was only when both wrists became involved that the symmetrical pattern became undeniable. His X-ray showed erosions at the second and third MTP joints on both feet — damage that had already occurred during the months of misdiagnosis.</p>
<p><strong>Layla, 29.</strong> She was one of the youngest patients in her rheumatologist's clinic with seropositive RA. Her anti-CCP titre was among the highest her rheumatologist had ever seen — a marker that predicted aggressive, erosive disease. She was started on methotrexate and a biologic within weeks of diagnosis, an urgency that surprised her. What her rheumatologist explained was that in RA, the window of opportunity for preventing irreversible joint damage is measured in months, not years. Every month of active synovitis was cartilage she would not get back.</p>
''',
})

# 4. CROHN'S DISEASE ──────────────────────────────────────────────────────────
ARTICLES.append({
    'title': "Crohn's Disease: Inflammation That Eats Through the Gut Wall",
    'slug': 'crohns-disease-autoimmune',
    'summary': (
        "Crohn's disease is a transmural inflammation — it burns through the full thickness of the intestinal wall. "
        "Unlike ulcerative colitis which is limited to the surface, Crohn's can penetrate to neighbouring organs, "
        "forming abscesses and fistulas while the immune system mistakes gut bacteria for invaders."
    ),
    'content': svg(
        "Crohn's Disease: Transmural Granulomatous Inflammation",
        '#f97316',
        'Normal Gut Wall', 'Granuloma Formation', 'Transmural Damage',
        # stage 1 – gut wall layers
        (
            '<rect x="70" y="170" width="100" height="12" rx="3" fill="#374151" stroke="#9ca3af" stroke-width="1"/>'
            '<rect x="70" y="184" width="100" height="14" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="70" y="200" width="100" height="10" rx="3" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<rect x="70" y="212" width="100" height="18" rx="3" fill="#374151" stroke="#9ca3af" stroke-width="1"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">Wall layers intact</text>'
        ),
        # stage 2 – granuloma forming
        (
            '<rect x="310" y="170" width="100" height="12" rx="3" fill="#374151" stroke="#9ca3af" stroke-width="1"/>'
            '<rect x="310" y="184" width="100" height="14" rx="3" fill="#166534" stroke="#22c55e" stroke-width="1" opacity=".5"/>'
            '<circle cx="360" cy="200" r="18" fill="#7c2d12" stroke="#f97316" stroke-width="1.4"/>'
            '<circle cx="352" cy="196" r="5" fill="#ea580c"/>'
            '<circle cx="365" cy="194" r="5" fill="#ea580c"/>'
            '<circle cx="358" cy="206" r="5" fill="#ea580c"/>'
            '<circle cx="371" cy="203" r="5" fill="#ea580c"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fdba74">Macrophage granuloma</text>'
        ),
        # stage 3 – fistula
        (
            '<rect x="550" y="170" width="100" height="12" rx="3" fill="#374151" stroke="#9ca3af" stroke-width="1" opacity=".4"/>'
            '<path d="M590,182 L590,230 L604,230 L604,182" stroke="#f97316" stroke-width="2" fill="#7c2d12" fill-opacity=".6"/>'
            '<path d="M596,230 L596,246" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>'
            '<circle cx="596" cy="250" r="5" fill="#dc2626" opacity=".7"/>'
            '<text x="600" y="265" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fdba74">Fistula / abscess</text>'
        ),
        'Mucosa → submucosa → muscle intact', 'Macrophages cluster → granuloma in all layers', 'Full-thickness ulcer, fistula formation',
    ) + '''
<h2>What is happening in the body</h2>
<p>Crohn's disease is defined by its transmural character: the inflammation does not stay on the surface of the intestinal lining but penetrates through every layer of the gut wall — mucosa, submucosa, muscularis propria, and serosa. This distinguishes it sharply from ulcerative colitis, which remains mucosal. The transmural spread is why Crohn's produces fistulas (abnormal tunnels connecting loops of bowel or bowel to bladder, vagina, or skin) and abscesses, while UC does not.</p>
<p>The hallmark histological finding is the granuloma — a structured collection of macrophages and epithelioid cells attempting to wall off what the immune system perceives as an unresolvable foreign body. In Crohn's, that perceived foreign body is intestinal bacteria. The normal gut immune system maintains tolerance to luminal bacteria through a complex balance of regulatory signals. In Crohn's, that tolerance collapses — particularly in genetically susceptible individuals with NOD2 mutations that impair bacterial sensing in Paneth cells — and macrophages mount an unregulated response to normal commensal organisms.</p>
<p>The result is skip lesions — patches of severe inflammation separated by normal tissue — that can occur anywhere from mouth to anus, though the terminal ileum and proximal colon are most commonly affected.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Cramping abdominal pain, often right lower quadrant</li>
<li>Chronic diarrhoea, sometimes bloody</li>
<li>Weight loss and malnutrition from malabsorption</li>
<li>Perianal fistulas and abscesses</li>
<li>Fever during flares</li>
<li>Extra-intestinal manifestations: mouth ulcers, skin lesions (erythema nodosum), eye inflammation, arthritis</li>
<li>Growth retardation in children</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Crohn's is the most direct expression of the leaky gut mechanism. The disease begins at the intestinal barrier, and its pathology is entirely driven by abnormal immune responses to luminal contents. Increased intestinal permeability precedes clinical onset and is present in unaffected first-degree relatives of Crohn's patients — suggesting it is a disease driver, not merely a consequence. The foods associated with Western dietary patterns — grains, refined carbohydrates, seed oils — are the primary drivers of that permeability increase.</p>

<h2>What the clinical data shows</h2>
<p>Paleomedicina's most dramatic published case involves a young man with severe Crohn's disease facing bowel resection surgery who achieved complete endoscopic and histological remission on the PKD within months, avoiding surgery entirely. The protocol's complete elimination of plant-based foods removes all sources of intestinal permeability-promoting lectins and phytates while providing the L-glutamine and butyrate precursors the gut lining requires for repair. Multiple Crohn's patients have been documented reaching drug-free remission with negative CRP and calprotectin on PKD.</p>

<h2>A life with this condition</h2>
<p><strong>Daniel, 32.</strong> He spent three years diagnosed with IBS before his gastroenterologist said "that's not IBS" within seconds of reaching the terminal ileum during his first colonoscopy. The ulcers were deep craters punched through all layers of the gut wall. He had lost eleven kilograms and attributed it to stress. What he actually had was a fistula forming between two loops of bowel that a CT scan had already detected but a previous doctor had called "non-specific." The mechanism — macrophages forming granulomas around gut bacteria they could no longer tolerate — was abstract against the concrete reality of a perianal abscess drained at two in the morning.</p>
<p><strong>Sophie, 16.</strong> Her Crohn's presented as failure to thrive. She was shorter than expected, not gaining weight, missing school because of abdominal pain she had been told was anxiety. Her paediatrician finally referred her to a paediatric gastroenterologist who looked at her growth chart — flat for two years — and ordered a faecal calprotectin test. It came back at 1,840 µg/g, twelve times the normal limit. The colonoscopy showed skip lesions from the terminal ileum into the ascending colon. She had been living with active intestinal inflammation throughout her most critical years of development.</p>
<p><strong>Ahmed, 41.</strong> He had been operated on three times in five years — two perianal fistula repairs and one bowel resection — before he found a gastroenterologist who explained that surgery treats the consequences of Crohn's but not the disease itself. Without controlling the underlying immune response, fistulas recur and bowel segments re-inflame. His life had been structured around proximity to bathrooms, around predicting which meals would trigger pain, around estimating how far he could walk from any given point before needing to stop. The disease had not been unmanaged; it had been managed only at the level of its wreckage.</p>
''',
})

# 5. ULCERATIVE COLITIS ───────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Ulcerative Colitis: The Mucosal Siege That Never Ends',
    'slug': 'ulcerative-colitis-autoimmune',
    'summary': (
        'Ulcerative colitis confines its destruction to the inner lining of the large intestine, '
        'but the sustained mucosal inflammation produces continuous pain, bleeding, and over decades, '
        'significantly elevated colorectal cancer risk. The disease begins at the rectum and spreads proximally.'
    ),
    'content': svg(
        'Ulcerative Colitis: Mucosal Crypt Destruction',
        '#dc2626',
        'Normal Colonic Crypts', 'Neutrophil Crypt Abscess', 'Mucosal Ulceration',
        # stage 1 – normal crypts
        (
            '<rect x="70" y="185" width="100" height="6" rx="2" fill="#22c55e" stroke="#16a34a" stroke-width="1"/>'
            '<rect x="78" y="191" width="8" height="28" rx="2" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="90" y="191" width="8" height="28" rx="2" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="102" y="191" width="8" height="28" rx="2" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="114" y="191" width="8" height="28" rx="2" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="70" y="220" width="100" height="8" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">Goblet cells, crypts intact</text>'
        ),
        # stage 2 – crypt abscess
        (
            '<rect x="310" y="185" width="100" height="6" rx="2" fill="#dc2626" stroke="#b91c1c" stroke-width="1"/>'
            '<rect x="318" y="191" width="8" height="28" rx="2" fill="#7f1d1d" stroke="#dc2626" stroke-width="1"/>'
            '<circle cx="322" cy="210" r="5" fill="#fca5a5"/>'
            '<rect x="330" y="191" width="8" height="28" rx="2" fill="#7f1d1d" stroke="#dc2626" stroke-width="1"/>'
            '<circle cx="334" cy="208" r="4" fill="#fca5a5"/>'
            '<rect x="354" y="191" width="8" height="28" rx="2" fill="#7f1d1d" stroke="#dc2626" stroke-width="1"/>'
            '<circle cx="358" cy="212" r="5" fill="#fca5a5"/>'
            '<rect x="310" y="220" width="100" height="8" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Neutrophils fill crypts</text>'
        ),
        # stage 3 – ulceration
        (
            '<path d="M550,190 Q565,185 575,190 Q590,183 605,188 Q618,182 640,188 Q650,190 650,195 L650,200 L550,200 Z" fill="#b91c1c" stroke="#dc2626" stroke-width="1.2"/>'
            '<path d="M565,200 L562,220 L568,220 Z" fill="#7f1d1d"/>'
            '<path d="M590,200 L587,225 L595,222 Z" fill="#7f1d1d"/>'
            '<path d="M615,200 L612,218 L620,216 Z" fill="#7f1d1d"/>'
            '<rect x="550" y="228" width="100" height="8" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fca5a5">Raw, bleeding mucosa</text>'
        ),
        'Tall crypts, intact epithelium', 'Neutrophils invade crypts (crypt abscess)', 'Crypt destruction, mucosal ulcers, bleeding',
    ) + '''
<h2>What is happening in the body</h2>
<p>Ulcerative colitis is a disease of the colon's mucosal surface. Unlike Crohn's disease, which can strike anywhere in the gastrointestinal tract and penetrates all layers of the gut wall, UC is confined to the mucosa and submucosa of the large intestine, always beginning at the rectum and extending proximally in a continuous, uninterrupted pattern. Proctitis affects only the rectum; left-sided colitis extends to the splenic flexure; pancolitis reaches the caecum.</p>
<p>The initiating event appears to be a breakdown in epithelial barrier function in genetically susceptible individuals. Luminal bacteria and bacterial products cross the mucosal barrier and trigger an exaggerated innate immune response. Neutrophils — the first responders of innate immunity — flood the lamina propria and invade the crypts of Lieberkühn, the test-tube-shaped glands that run perpendicular through the colonic mucosa. When neutrophils pack a crypt completely, the result is a crypt abscess, visible on colonoscopy biopsy.</p>
<p>Crypt abscesses rupture and coalesce into mucosal ulcers — raw, bleeding patches that produce the cardinal symptoms of bloody diarrhoea. The chronic inflammation progressively depletes goblet cells (which produce the protective mucous layer) and distorts the normal crypt architecture, producing the crypt branching and foreshortening visible on histology.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Bloody diarrhoea — the defining symptom</li>
<li>Urgency and tenesmus (painful urge to defecate without result)</li>
<li>Cramping lower abdominal pain, usually left-sided</li>
<li>Mucus in stool</li>
<li>Fatigue and anaemia from chronic blood loss</li>
<li>Toxic megacolon in severe cases (life-threatening)</li>
<li>Colorectal cancer risk increasing significantly after 8–10 years of pancolitis</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>UC shares the upstream mechanism of increased intestinal permeability with Crohn's, but the immune response targets surface antigens rather than penetrating deeper. Dysbiosis — reduced Faecalibacterium prausnitzii, overgrowth of Fusobacterium and adherent-invasive E. coli — is consistently documented in UC and precedes flares. The disrupted microbiome reduces short-chain fatty acid (SCFA) production, particularly butyrate, which is the primary fuel source for colonocytes and the key regulator of colonic mucosal integrity and immune tolerance.</p>

<h2>What the clinical data shows</h2>
<p>Elimination of fermentable fibre and plant compounds on the PKD removes the substrates driving pathological dysbiosis. Several UC patients in Paleomedicina's case series achieved mucosal healing confirmed by colonoscopy — the gold standard endpoint — while on PKD, reducing or eliminating 5-aminosalicylate and corticosteroid dependence. The mechanism is restoration of colonocyte energy metabolism through ketone bodies (which partly substitute for the butyrate deficit) and elimination of the permeability-promoting dietary factors that perpetuate the mucosal injury cycle.</p>

<h2>A life with this condition</h2>
<p><strong>Elena, 29.</strong> She knew something was wrong the fourth time she needed the bathroom in three hours at work. The bleeding had started three weeks earlier — intermittent at first, then constant. By the time she saw her GP she was anaemic. The colonoscopy showed continuous inflammation from rectum to splenic flexure, the surface raw and friable. She was started on mesalazine and told to monitor for worsening. For the next decade the question was not whether she would flare, but when — and what the increasing cumulative burden of inflammation would mean for her cancer risk.</p>
<p><strong>Jason, 42.</strong> His severe flare came without warning after a course of antibiotics for a dental abscess. He was admitted with eight bloody stools per day, a CRP of 210, and a heart rate of 112. The gastroenterologist said the word "colectomy" in the first conversation, which was the first time Jason understood that this disease could end with his colon removed. IV steroids brought him back from the edge of surgery that admission, but his gastroenterologist told him plainly: one more severe flare at this level and the decision would be made for him. He started a biologic the week he was discharged.</p>
<p><strong>Maria, 57.</strong> She had lived with pancolitis for 22 years, learned to manage it, and regarded it as controlled. What her gastroenterologist found on her surveillance colonoscopy was not. A flat lesion in the transverse colon — low-grade dysplasia, technically not cancer, but in the context of 22 years of mucosal inflammation a serious warning. She was referred for colectomy. The surgery she had spent two decades avoiding became necessary not because of a flare but because of the invisible accumulation of damage that decades of inflammation had quietly laid down.</p>
''',
})


# 6. TYPE 1 DIABETES ─────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Type 1 Diabetes: The Immune Destruction of Insulin-Making Cells',
    'slug': 'type-1-diabetes-autoimmune',
    'summary': (
        'Type 1 diabetes is not a failure of the pancreas — it is an immune attack on the pancreas. '
        'Autoreactive T-cells destroy the beta cells of the islets of Langerhans, eliminating the body\'s '
        'only source of insulin and making exogenous insulin necessary for survival.'
    ),
    'content': svg(
        'Type 1 Diabetes: CD8+ T-Cell Destruction of Beta Cells',
        '#10b981',
        'Islet of Langerhans', 'Insulitis Attack', 'Beta Cells Destroyed',
        (
            '<ellipse cx="120" cy="200" rx="50" ry="40" fill="#064e3b" stroke="#10b981" stroke-width="1.4"/>'
            '<circle cx="108" cy="195" r="8" fill="#059669"/>'
            '<circle cx="122" cy="190" r="8" fill="#059669"/>'
            '<circle cx="136" cy="195" r="8" fill="#059669"/>'
            '<circle cx="115" cy="208" r="8" fill="#059669"/>'
            '<circle cx="130" cy="208" r="8" fill="#059669"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#6ee7b7">Beta cells produce insulin</text>'
        ),
        (
            '<ellipse cx="360" cy="200" rx="50" ry="40" fill="#064e3b" stroke="#10b981" stroke-width="1.4" opacity=".6"/>'
            '<circle cx="348" cy="195" r="8" fill="#059669" opacity=".5"/>'
            '<circle cx="372" cy="195" r="8" fill="#059669" opacity=".5"/>'
            '<circle cx="360" cy="208" r="6" fill="#dc2626"/>'
            '<circle cx="332" cy="188" r="7" stroke="#10b981" stroke-width="1.2" fill="#065f46"/>'
            '<line x1="329" y1="182" x2="325" y2="176" stroke="#10b981" stroke-width="1"/>'
            '<line x1="335" y1="181" x2="338" y2="175" stroke="#10b981" stroke-width="1"/>'
            '<line x1="340" y1="184" x2="345" y2="180" stroke="#10b981" stroke-width="1"/>'
            '<circle cx="386" cy="215" r="7" stroke="#10b981" stroke-width="1.2" fill="#065f46"/>'
            '<line x1="383" y1="208" x2="379" y2="202" stroke="#10b981" stroke-width="1"/>'
            '<line x1="389" y1="208" x2="392" y2="202" stroke="#10b981" stroke-width="1"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#6ee7b7">CD8+ T-cells infiltrate islet</text>'
        ),
        (
            '<ellipse cx="600" cy="200" rx="50" ry="40" fill="#1c1917" stroke="#78716c" stroke-width="1.2" opacity=".6"/>'
            '<circle cx="588" cy="195" r="8" fill="#1c1917" stroke="#78716c" stroke-width="1" opacity=".5"/>'
            '<circle cx="612" cy="195" r="8" fill="#1c1917" stroke="#78716c" stroke-width="1" opacity=".5"/>'
            '<text x="600" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a8a29e">no insulin</text>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a8a29e">Islet destroyed, no insulin output</text>'
        ),
        'Beta cells secrete insulin', 'T-cells enter islet (insulitis)', 'Beta cell mass eliminated, T1D onset',
    ) + '''
<h2>What is happening in the body</h2>
<p>The pancreas contains clusters of hormone-producing cells called islets of Langerhans. Within each islet, beta cells are responsible for synthesising and secreting insulin in response to rising blood glucose. In type 1 diabetes, these beta cells are specifically targeted and destroyed by autoreactive CD8+ cytotoxic T-cells in a process called insulitis — immune cell infiltration of the islet.</p>
<p>The autoreactive T-cells recognise beta cell antigens — most notably insulin itself, as well as glutamic acid decarboxylase (GAD65) and zinc transporter 8 (ZnT8) — as foreign. This misdirected recognition is established years before clinical diagnosis. In the pre-diabetic phase, beta cell mass is progressively depleted. When approximately 80–90% of beta cells have been destroyed, insulin secretion falls below the threshold needed to maintain glucose homeostasis and clinical T1D presents — usually abruptly, often as diabetic ketoacidosis in children.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Polyuria and polydipsia (frequent urination, extreme thirst)</li>
<li>Rapid, unexplained weight loss</li>
<li>Fatigue and weakness</li>
<li>Diabetic ketoacidosis at onset in many cases: nausea, vomiting, deep laboured breathing</li>
<li>Blurred vision from osmotic changes in the lens</li>
<li>Long-term: retinopathy, nephropathy, neuropathy, cardiovascular disease</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Molecular mimicry between bovine serum albumin (BSA) in cow's milk and the beta cell surface protein ICA69 was among the first food-autoimmune connections studied in T1D. Children who were breast-fed longer and introduced to cow's milk later have consistently lower T1D incidence. Wheat gliadin has been shown to increase zonulin and intestinal permeability in people with and without coeliac disease — and T1D patients have two to three times the rate of coeliac disease of the general population, sharing the same gut-driven immune priming mechanism.</p>

<h2>What the clinical data shows</h2>
<p>Paleomedicina's case series includes children with new-onset T1D whose C-peptide — the marker of residual beta cell function — was preserved and in some cases increased on the PKD, suggesting that when the autoimmune attack is halted early, beta cell regeneration may occur. In longer-standing T1D, the protocol typically results in dramatically reduced insulin requirements due to the near-zero dietary carbohydrate load, with no further autoimmune progression. The PKD's elimination of dairy, wheat, and all permeability-promoting foods removes the antigens driving the molecular mimicry that sustains the autoimmune attack.</p>

<h2>A life with this condition</h2>
<p><strong>Liam, 14.</strong> His parents brought him to the emergency department after three weeks of constant thirst and unexplained weight loss. His breath smelled sweet. His blood glucose was 34 mmol/L and he was in diabetic ketoacidosis. The diagnosis took six minutes. He was told he would need insulin for the rest of his life, but no one mentioned the years of silent beta cell destruction that had preceded that night — the T-cells entering his islets one by one, the progressive depletion of insulin-producing mass down to the 10% threshold at which the body can no longer maintain glucose control. The crisis was the last chapter, not the first.</p>
<p><strong>Naomi, 31.</strong> She was initially diagnosed with type 2 diabetes at 28, given metformin, and told to lose weight. She lost weight — twelve kilograms in six months — and her glucose control deteriorated anyway. Her GP noted that her BMI had always been in the healthy range and referred her to an endocrinologist who tested her GAD65 antibodies. They were strongly positive. She had LADA — latent autoimmune diabetes in adults — a slower-onset form of type 1 where the beta cell destruction unfolds over years rather than months. She had been given advice for a metabolic disease when she actually had an autoimmune one.</p>
<p><strong>Ben, 5.</strong> His mother noticed the wet nappies first — heavier than they had ever been, even as a newborn. Then she noticed he was thirsty at night in a way that seemed wrong. She looked up the symptoms on a Saturday afternoon and drove him to the emergency department without waiting for Monday. His glucose was 28 mmol/L; he was starting to slip toward ketoacidosis. The paediatric endocrinologist told her she had probably caught it early enough to avoid the worst of the presentation. Ben was started on insulin that evening. He has worn a continuous glucose monitor every day since. He is now eleven, and the monitor is simply part of his body as far as he is concerned.</p>
''',
})

# 7. HASHIMOTO'S THYROIDITIS ──────────────────────────────────────────────────
ARTICLES.append({
    'title': "Hashimoto's Thyroiditis: When the Immune System Silences the Thyroid",
    'slug': 'hashimotos-thyroiditis-autoimmune',
    'summary': (
        "Hashimoto's thyroiditis is the most common cause of hypothyroidism in the developed world. "
        "Lymphocytes infiltrate the thyroid gland, destroying follicles and replacing functional tissue "
        "with fibrosis — progressively silencing the gland's ability to produce thyroid hormone."
    ),
    'content': svg(
        "Hashimoto's Thyroiditis: Lymphocytic Infiltration of the Thyroid",
        '#14b8a6',
        'Normal Thyroid Follicles', 'Lymphocyte Infiltration', 'Fibrosis & Hypothyroidism',
        (
            '<circle cx="100" cy="190" r="20" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3"/>'
            '<circle cx="100" cy="190" r="11" fill="#0f766e" stroke="#5eead4" stroke-width="1"/>'
            '<circle cx="140" cy="200" r="18" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3"/>'
            '<circle cx="140" cy="200" r="10" fill="#0f766e" stroke="#5eead4" stroke-width="1"/>'
            '<circle cx="118" cy="218" r="16" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3"/>'
            '<circle cx="118" cy="218" r="9" fill="#0f766e" stroke="#5eead4" stroke-width="1"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#5eead4">Colloid-filled follicles</text>'
        ),
        (
            '<circle cx="340" cy="190" r="20" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3" opacity=".6"/>'
            '<circle cx="380" cy="200" r="18" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3" opacity=".6"/>'
            '<circle cx="358" cy="218" r="16" fill="#134e4a" stroke="#14b8a6" stroke-width="1.3" opacity=".6"/>'
            '<circle cx="328" cy="205" r="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>'
            '<circle cx="345" cy="215" r="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>'
            '<circle cx="362" cy="205" r="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>'
            '<circle cx="375" cy="215" r="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>'
            '<circle cx="352" cy="195" r="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#5eead4">T- and B-cells flood gland</text>'
        ),
        (
            '<rect x="550" y="170" width="100" height="60" rx="8" fill="#1c1917" stroke="#78716c" stroke-width="1.2"/>'
            '<line x1="560" y1="182" x2="640" y2="182" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="192" x2="640" y2="192" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="202" x2="640" y2="202" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="212" x2="640" y2="212" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="222" x2="640" y2="222" stroke="#57534e" stroke-width="1.2"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a8a29e">Fibrotic gland, low T4/T3</text>'
        ),
        'Follicles produce T3 and T4', 'Germinal centres form, TPO antibodies', 'Follicle destruction, fibrosis, hypothyroid',
    ) + '''
<h2>What is happening in the body</h2>
<p>The thyroid gland is organised into spherical follicles, each lined with thyrocytes and filled with colloid — a gel containing thyroglobulin, the precursor from which T3 and T4 are cleaved. In Hashimoto's, this architecture is progressively dismantled by lymphocytic infiltration. Both CD4+ helper T-cells and CD8+ cytotoxic T-cells accumulate within the gland, forming germinal centres — the organised lymphoid structures normally found in lymph nodes — within the thyroid tissue itself.</p>
<p>B cells within those germinal centres produce the antibodies that are the clinical hallmarks of the disease: anti-thyroid peroxidase (anti-TPO) and anti-thyroglobulin (anti-TG). Thyroid peroxidase is the enzyme that iodinates thyroglobulin, the first step in thyroid hormone synthesis; antibodies against it impair hormone production. The cellular immune attack simultaneously destroys follicular cells. Over years, functional follicular tissue is replaced by fibrosis, the gland shrinks, and the hypothalamic-pituitary axis compensates by driving TSH higher — producing the elevated TSH that typically first signals the disease.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Fatigue disproportionate to rest (often the first symptom)</li>
<li>Weight gain despite unchanged diet</li>
<li>Cold intolerance</li>
<li>Slow pulse, constipation</li>
<li>Brain fog and depression</li>
<li>Dry skin and hair loss</li>
<li>Goitre (enlarged thyroid) in some patients; atrophic gland in others</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Hashimoto's shares the autoimmune terrain of increased intestinal permeability and molecular mimicry. Gliadin and thyroid antigens share structural peptide sequences, and the correlation between coeliac disease and Hashimoto's — approximately three times the expected coeliac rate among Hashimoto's patients — points to shared gut-mediated immune activation. A published randomised trial showed that a strict gluten-free diet significantly reduced anti-TPO and anti-TG titres in Hashimoto's patients without coeliac disease, confirming the wheat-thyroid immune axis.</p>

<h2>What the clinical data shows</h2>
<p>Paleomedicina case series document Hashimoto's patients tapering and eventually discontinuing levothyroxine after antibody normalisation on the PKD. In one published case, a woman with 16 years of Hashimoto's thyroiditis and dependence on thyroid supplementation achieved normal TSH, T3, and T4 levels without medication after eight months on PKD, with anti-TPO declining from several hundred to within normal range. The mechanism is removal of all dietary triggers for gut permeability and thyroid-cross-reactive immune activation.</p>

<h2>A life with this condition</h2>
<p><strong>Claire, 34.</strong> She had been told she was depressed for two years before her new GP ordered a thyroid panel. She was not depressed. She was cold when no one else was cold, exhausted after eight hours of sleep, gaining weight on a diet that should have maintained her. Her brain felt like it was running through mud. Her TSH came back at 18; her anti-TPO antibodies were 640 IU/mL. The thyroid ultrasound showed a gland with the moth-eaten texture of established Hashimoto's. She had not been depressed. She had had a slowly failing organ, and had been sent to psychiatrists instead of endocrinologists.</p>
<p><strong>Sandra, 38.</strong> Her Hashimoto's was triggered, her endocrinologist believed, by the immune rebound after pregnancy. She had been fine throughout her pregnancy — thyroid autoimmune conditions often improve during gestation as immune tolerance increases. Six weeks postpartum, the suppression lifted, the immune system surged, and her anti-TPO antibodies quadrupled. She had attributed the exhaustion, the hair falling out in the shower, and the inability to feel warm to having a newborn. It was only when her baby was six months old and the symptoms had not improved that her midwife ordered the test.</p>
<p><strong>Michael, 62.</strong> His Hashimoto's had been managed on levothyroxine for eleven years when he developed a goitre large enough to cause mild difficulty swallowing. His endocrinologist explained that some Hashimoto's patients develop enlargement rather than atrophy — the immune infiltration provoking a paradoxical growth response. His TSH was controlled on medication, his antibodies remained elevated, and his thyroid was simultaneously being attacked and attempting to compensate by growing. He found the contradiction difficult to explain to family members who assumed that being "on medication for it" meant the disease was resolved.</p>
''',
})

# 8. GRAVES' DISEASE ──────────────────────────────────────────────────────────
ARTICLES.append({
    'title': "Graves' Disease: Antibodies That Force the Thyroid Into Overdrive",
    'slug': 'graves-disease-autoimmune',
    'summary': (
        "Graves' disease is the mirror image of Hashimoto's: instead of destroying the thyroid, "
        "the immune system produces antibodies that mimic TSH and lock the gland into permanent stimulation. "
        "The result is uncontrolled hyperthyroidism — a runaway metabolic acceleration."
    ),
    'content': svg(
        "Graves' Disease: TSI Antibodies Drive Continuous Thyroid Stimulation",
        '#84cc16',
        'Normal TSH Receptor', 'TSI Antibody Binding', 'Hyperthyroid State',
        (
            '<rect x="80" y="170" width="80" height="60" rx="8" fill="#1a2e05" stroke="#84cc16" stroke-width="1.3"/>'
            '<rect x="100" y="156" width="14" height="18" rx="4" fill="#3f6212" stroke="#84cc16" stroke-width="1.2"/>'
            '<text x="107" y="148" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#a3e635">TSH</text>'
            '<line x1="107" y1="156" x2="107" y2="170" stroke="#84cc16" stroke-width="1.2" stroke-dasharray="2 2"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a3e635">TSH binds, then releases</text>'
        ),
        (
            '<rect x="320" y="170" width="80" height="60" rx="8" fill="#1a2e05" stroke="#84cc16" stroke-width="1.3"/>'
            '<line x1="352" y1="152" x2="340" y2="170" stroke="#a3e635" stroke-width="1.5"/>'
            '<line x1="352" y1="152" x2="364" y2="170" stroke="#a3e635" stroke-width="1.5"/>'
            '<line x1="352" y1="152" x2="352" y2="132" stroke="#84cc16" stroke-width="2"/>'
            '<circle cx="352" cy="127" r="10" fill="#365314"/>'
            '<text x="352" y="131" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#a3e635">TSI</text>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a3e635">TSI locks on, never releases</text>'
        ),
        (
            '<rect x="560" y="155" width="80" height="80" rx="8" fill="#1a2e05" stroke="#84cc16" stroke-width="2.5"/>'
            '<circle cx="580" cy="175" r="6" fill="#65a30d"/>'
            '<circle cx="600" cy="170" r="6" fill="#65a30d"/>'
            '<circle cx="620" cy="175" r="6" fill="#65a30d"/>'
            '<circle cx="580" cy="195" r="6" fill="#65a30d"/>'
            '<circle cx="600" cy="195" r="6" fill="#65a30d"/>'
            '<circle cx="620" cy="195" r="6" fill="#65a30d"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a3e635">Enlarged, overactive thyroid</text>'
        ),
        'Pulsatile TSH briefly stimulates', 'TSI antibody binds, cannot be cleared', 'Continuous hormone excess, goitre',
    ) + '''
<h2>What is happening in the body</h2>
<p>The thyroid gland is regulated by a feedback loop: the pituitary secretes TSH, which binds to TSH receptors on thyrocytes, stimulates hormone synthesis, then releases. Circulating T3 and T4 feed back to suppress TSH when levels are adequate. In Graves' disease, the immune system produces thyroid-stimulating immunoglobulins (TSI) — antibodies that bind the TSH receptor in the same site as TSH but cannot be cleared by the normal feedback mechanism.</p>
<p>Unlike TSH, which binds and releases as levels fluctuate, TSI stays bound. It constitutively activates the receptor's downstream signalling cascade — adenylyl cyclase, cAMP, PKA — driving thyroid hormone synthesis continuously and without restraint. The pituitary responds by suppressing TSH to almost undetectable levels, but the antibody-driven stimulation ignores that suppression. The gland enlarges (diffuse goitre), vascularity increases, and T3 and T4 rise to levels that accelerate every metabolic process in the body.</p>
<p>Graves' ophthalmopathy — the eye protrusion characteristic of the disease — is caused by TSI cross-reacting with TSH receptors in orbital fibroblasts, causing glycosaminoglycan accumulation and inflammatory expansion of the retroorbital tissue.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Palpitations and rapid heart rate (tachycardia, sometimes atrial fibrillation)</li>
<li>Heat intolerance and excessive sweating</li>
<li>Weight loss despite increased appetite</li>
<li>Tremor in the hands</li>
<li>Proptosis (exophthalmos) — protruding, staring eyes</li>
<li>Anxiety, irritability, insomnia</li>
<li>Diarrhoea and frequent bowel movements</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Graves' and Hashimoto's share the same underlying terrain of thyroid autoimmunity and can coexist in the same patient or family. The TSI-producing B cells require T cell help — specifically Th2-polarised responses — suggesting the same gut-mediated immune dysregulation that drives other autoimmune conditions. Iodine excess is an established environmental trigger, as is psychological stress, through cortisol-mediated immune modulation. Gut permeability and molecular mimicry between gut-derived antigens and thyroid tissue remain the upstream drivers.</p>

<h2>What the clinical data shows</h2>
<p>Graves' disease is less extensively studied in the PKD literature than Hashimoto's, but Paleomedicina has documented cases of TSI normalisation and hyperthyroidism remission in patients adopting the PKD. The diet eliminates the dietary triggers of both permeability and Th2 immune skewing while providing the nutrient density (selenium, zinc, iodine through seafood and organ meats) required for normal thyroid function. Several patients have avoided radioiodine ablation or thyroidectomy by achieving immunological remission through dietary intervention.</p>

<h2>A life with this condition</h2>
<p><strong>Tom, 45.</strong> His wife asked why his eyes looked different. He had noticed his heart racing but attributed it to caffeine; he had dropped six kilograms while eating more than usual, which he had found gratifying. His optometrist noticed the proptosis during a routine check — both eyes slightly prominent, lids retracted — and referred him immediately. TSH was undetectable; TSI antibodies were strongly positive. Antibodies that mimicked TSH but never released from the receptor were driving his thyroid continuously, regardless of how high his hormone levels climbed. He had felt energetic. He had been burning himself from the inside.</p>
<p><strong>Lucy, 32.</strong> She had been treated for panic disorder for eight months when her cardiologist finally ordered a thyroid panel. She had presented repeatedly with palpitations, racing heart, and anxiety so severe she had stopped going to social events. The psychiatrist had started her on an SSRI. Her T3 was 9.2 pmol/L — nearly double the upper limit. Her TSI antibodies confirmed Graves'. The "panic attacks" were thyrotoxicosis — her hyperstimulated thyroid flooding her body with hormone that accelerated every cardiac and neurological process she had. The SSRI was stopped. Carbimazole was started. Within three months she felt, for the first time in a year, like herself.</p>
<p><strong>Paul, 59.</strong> He had known about his Graves' disease and was stable on low-dose carbimazole when he needed a contrast CT scan for an unrelated matter. Within 72 hours of the iodine contrast injection, he was in the emergency department with a heart rate of 148 and a temperature of 39.2°C. His endocrinologist confirmed thyroid storm — an acute, life-threatening surge of thyroid hormone triggered by the iodine load hitting a gland that was already autonomously overactive. He spent four days in the ICU. It was the first time he understood that his disease, which had felt managed and minor, could still kill him without warning.</p>
''',
})

# 9. PSORIASIS ────────────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Psoriasis: The Skin That Cannot Stop Growing',
    'slug': 'psoriasis-autoimmune',
    'summary': (
        'Psoriasis is driven by IL-17 and IL-23 cytokines that lock the skin into a state of '
        'hyperproliferation. Keratinocytes that normally renew over 28 days complete the cycle in 3–4 days, '
        'piling up as the characteristic silver-scaled plaques of the disease.'
    ),
    'content': svg(
        'Psoriasis: IL-17 Drives Keratinocyte Hyperproliferation',
        '#f43f5e',
        'Normal Skin Turnover', 'IL-17/IL-23 Cascade', 'Plaque Formation',
        (
            '<rect x="70" y="165" width="100" height="8" rx="2" fill="#be185d" stroke="#f43f5e" stroke-width="1" opacity=".5"/>'
            '<rect x="70" y="175" width="100" height="14" rx="2" fill="#9d174d" stroke="#f43f5e" stroke-width="1" opacity=".7"/>'
            '<rect x="70" y="191" width="100" height="16" rx="2" fill="#831843" stroke="#e879a0" stroke-width="1"/>'
            '<rect x="70" y="209" width="100" height="20" rx="2" fill="#500724" stroke="#9d174d" stroke-width="1"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f9a8d4">28-day renewal cycle</text>'
        ),
        (
            '<circle cx="360" cy="178" r="9" fill="#7c1034" stroke="#f43f5e" stroke-width="1.2"/>'
            '<text x="360" y="182" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fda4af">DC</text>'
            '<line x1="360" y1="187" x2="360" y2="196" stroke="#f43f5e" stroke-width="1.2"/>'
            '<text x="375" y="200" font-family="system-ui,sans-serif" font-size="8" fill="#fda4af">IL-23</text>'
            '<circle cx="348" cy="208" r="8" fill="#7c1034" stroke="#f43f5e" stroke-width="1.2"/>'
            '<text x="348" y="212" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" fill="#fda4af">Th17</text>'
            '<line x1="348" y1="216" x2="348" y2="224" stroke="#f43f5e" stroke-width="1.2"/>'
            '<text x="358" y="228" font-family="system-ui,sans-serif" font-size="8" fill="#fda4af">IL-17</text>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f9a8d4">Dendritic→Th17→IL-17 cascade</text>'
        ),
        (
            '<rect x="550" y="148" width="100" height="30" rx="2" fill="#be185d" stroke="#f43f5e" stroke-width="1.4"/>'
            '<rect x="550" y="180" width="100" height="14" rx="2" fill="#9d174d" stroke="#f43f5e" stroke-width="1"/>'
            '<rect x="550" y="196" width="100" height="16" rx="2" fill="#831843" stroke="#e879a0" stroke-width="1"/>'
            '<rect x="550" y="214" width="100" height="16" rx="2" fill="#500724" stroke="#9d174d" stroke-width="1"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f9a8d4">Plaque: 3-day cycle, thick scale</text>'
        ),
        'Normal 28-day keratinocyte cycle', 'IL-23 activates Th17 → IL-17 flood', 'Hyperproliferation → silvery plaque',
    ) + '''
<h2>What is happening in the body</h2>
<p>Psoriasis begins not in the skin but in the dendritic cells of the dermis. Plasmacytoid dendritic cells, activated by self-DNA or microbial triggers, produce interferon-alpha and IL-12/IL-23. IL-23 drives the differentiation of naive T-cells into Th17 cells, which secrete IL-17A, IL-17F, and IL-22. These cytokines act on keratinocytes — the cells that form the skin's outer layers — and trigger a profound shift in their behaviour.</p>
<p>Normal keratinocytes in the epidermis take approximately 28 days to mature, migrate from the basal layer to the surface, and shed. Under sustained IL-17 stimulation, that cycle compresses to 3–4 days. The hyperproliferating keratinocytes do not have time to mature properly — they retain their nuclei (parakeratosis) and pile up in the characteristic silvery scale above the inflamed dermis. The dilated, tortuous capillaries of the dermal papillae produce the punctate bleeding (Auspitz sign) when scale is removed.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Well-demarcated, raised plaques with silvery-white scale on elbows, knees, scalp, lower back</li>
<li>Itching, burning, soreness at plaque sites</li>
<li>Nail changes: pitting, onycholysis, oil-drop discolouration</li>
<li>Psoriatic arthritis in 20–30% of patients (can be erosive)</li>
<li>Koebner phenomenon: new plaques appearing at sites of skin trauma</li>
<li>Significantly elevated cardiovascular disease risk (shared inflammatory terrain)</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Psoriasis flares reliably following gut dysbiosis events — antibiotic courses, gastrointestinal infections, alcohol excess. Streptococcal pharyngitis triggers guttate psoriasis in children through molecular mimicry between streptococcal M-protein and keratin. The same gut permeability mechanism that drives other autoimmune conditions creates the systemic IL-23 and IL-17 dysregulation that characterises psoriasis. Patients with psoriasis have measurably increased intestinal permeability compared to controls.</p>

<h2>What the clinical data shows</h2>
<p>Case reports and series document dramatic clearance of psoriatic plaques on the PKD, with some patients achieving complete skin clearance within weeks of eliminating grains, legumes, and processed foods. The mechanism is dual: removal of the gut permeability drivers that fuel the IL-23/Th17 axis, combined with the direct anti-inflammatory effect of ketone bodies on NLRP3-mediated IL-1 and IL-18 release. Psoriatic arthritis has shown parallel improvement in the same patients, confirming shared upstream drivers.</p>

<h2>A life with this condition</h2>
<p><strong>Amara, 22.</strong> She noticed the first plaques on her elbows and waited three months before seeing a doctor, embarrassed by what they looked like. By then her scalp was involved and she was wearing her hair differently to cover the scale at her hairline. What her dermatologist showed her on a diagram changed how she thought about it: normal skin renews in 28 days; her affected patches were completing that cycle in three. The IL-17 flooding her dermis had locked her keratinocytes into a proliferation they could not stop. The scale was the skin's failed attempt to shed what it was producing too fast to control. Understanding this did not make it less visible. But it made it less shameful.</p>
<p><strong>James, 35.</strong> His psoriasis arrived two weeks after streptococcal tonsillitis — hundreds of small teardrop-shaped spots across his trunk and limbs almost overnight, the guttate pattern that follows streptococcal infection in susceptible people. His GP diagnosed it immediately. The bacterial M-protein had triggered a T-cell response that cross-reacted with keratin in his skin; his immune system had learned to attack his own skin surface while fighting an infection in his throat. Most guttate episodes clear within months. His did not fully clear; it evolved into chronic plaque psoriasis, as if the infection had unlocked something that could not be fully locked again.</p>
<p><strong>Rosa, 48.</strong> She had managed her psoriasis for twenty years with topical treatments when her fingers began swelling at the joints in a pattern her rheumatologist recognised immediately as psoriatic dactylitis — "sausage fingers," where the entire digit swells because both the joint and the tendon sheath are inflamed simultaneously. Her nail pitting had been present for years; she had not known it was a marker of joint involvement risk. Twenty percent of psoriasis patients develop psoriatic arthritis, and the skin disease almost always precedes the joint disease by years. She had been carrying a warning in her fingernails for a decade without anyone reading it.</p>
''',
})

# 10. CELIAC DISEASE ──────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Celiac Disease: How Gluten Destroys the Intestinal Villi',
    'slug': 'celiac-disease-autoimmune',
    'summary': (
        'Celiac disease is the one autoimmune condition with a completely identified dietary trigger: gliadin, '
        'the alcohol-soluble fraction of wheat gluten. In genetically susceptible individuals, gliadin '
        'initiates an immune cascade that flattens the intestinal villi and impairs absorption of nearly '
        'every nutrient.'
    ),
    'content': svg(
        'Celiac Disease: Gliadin-Triggered Villous Atrophy',
        '#f59e0b',
        'Normal Villi', 'tTG/Antibody Cascade', 'Villous Atrophy',
        (
            '<rect x="80" y="220" width="80" height="10" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<rect x="88" y="178" width="8" height="44" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="100" y="170" width="8" height="52" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="112" y="175" width="8" height="47" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="124" y="172" width="8" height="50" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<rect x="136" y="178" width="8" height="44" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="1"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">Tall villi, large surface area</text>'
        ),
        (
            '<text x="360" y="168" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">gliadin fragment</text>'
            '<rect x="348" y="171" width="24" height="10" rx="3" fill="#92400e" stroke="#f59e0b" stroke-width="1.2"/>'
            '<line x1="360" y1="181" x2="360" y2="192" stroke="#f59e0b" stroke-width="1.2"/>'
            '<text x="380" y="200" font-family="system-ui,sans-serif" font-size="8" fill="#fcd34d">tTG</text>'
            '<circle cx="360" cy="198" r="8" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>'
            '<line x1="360" y1="206" x2="360" y2="215" stroke="#f59e0b" stroke-width="1.2"/>'
            '<line x1="348" y1="221" x2="356" y2="215" stroke="#fcd34d" stroke-width="1.3"/>'
            '<line x1="356" y1="215" x2="364" y2="221" stroke="#fcd34d" stroke-width="1.3"/>'
            '<line x1="356" y1="215" x2="356" y2="205" stroke="#f59e0b" stroke-width="1.5"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">tTG deamidates → anti-tTG IgA</text>'
        ),
        (
            '<rect x="550" y="220" width="100" height="10" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<rect x="570" y="212" width="60" height="10" rx="2" fill="#166534" stroke="#22c55e" stroke-width="1" opacity=".5"/>'
            '<text x="600" y="208" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#86efac">blunted</text>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fcd34d">Flat mucosa, malabsorption</text>'
        ),
        'Finger-like villi, high surface area', 'Gliadin → tTG deamidation → IgA anti-tTG', 'Villous flattening, crypt hyperplasia',
    ) + '''
<h2>What is happening in the body</h2>
<p>In celiac disease, the immune trigger is precisely identified: alpha-gliadin, a protein in wheat (and related prolamins in rye and barley). In genetically susceptible individuals carrying HLA-DQ2 or HLA-DQ8 — present in 98% of celiac patients — gliadin peptides that survive digestion enter the lamina propria through a leaky epithelial barrier. There, the enzyme tissue transglutaminase (tTG) deamidates gliadin peptides, converting glutamine residues to glutamate and increasing their affinity for HLA-DQ2/DQ8 molecules on antigen-presenting cells.</p>
<p>The resulting T-cell activation drives a dual immune response: a Th1-mediated cytotoxic attack on enterocytes and a B-cell antibody response producing the IgA anti-tTG antibodies used for diagnosis. CD8+ intraepithelial lymphocytes kill villous enterocytes, while cytokine release drives crypt hyperplasia — a compensatory but inadequate attempt to replace the destroyed absorptive surface. Over time, the villi flatten (partial to total villous atrophy), drastically reducing the absorptive surface area of the small intestine.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Chronic diarrhoea and steatorrhea (fatty, malodorous stools)</li>
<li>Abdominal bloating, pain, and distension</li>
<li>Weight loss and failure to thrive in children</li>
<li>Iron-deficiency anaemia unresponsive to supplementation</li>
<li>Osteoporosis from calcium malabsorption</li>
<li>Dermatitis herpetiformis — the skin manifestation</li>
<li>Peripheral neuropathy and ataxia (gluten neuropathy)</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Celiac disease is the autoimmune condition that most directly validates the leaky gut model because the sequence is fully established: wheat → intestinal permeability increase (via zonulin) → gliadin entry → tTG deamidation → immune activation → villous destruction. Remove wheat entirely and the immune response resolves, the villi regenerate, and the antibodies normalise. Celiac disease demonstrates that the same dietary factors proposed as drivers of other autoimmune conditions can, in the right genetic context, directly cause autoimmune tissue destruction.</p>

<h2>What the clinical data shows</h2>
<p>Unlike most autoimmune conditions, celiac disease has an established, guideline-recommended dietary treatment: strict lifelong gluten elimination. Mucosal healing confirmed by repeat biopsy occurs in 80–95% of patients who achieve complete dietary compliance. The PKD, which eliminates all grains by design, achieves this as a baseline. In Paleomedicina patients with co-existing celiac and another autoimmune condition, both conditions have been shown to respond simultaneously to the PKD protocol.</p>

<h2>A life with this condition</h2>
<p><strong>Noah, 14.</strong> He had anaemia from age 11 that no iron supplement could hold. He was tired, short, not thriving in sports. At 14 a new paediatrician tested anti-tTG IgA and called his mother the same day. The biopsy showed total villous atrophy — the intestinal absorptive surface reduced to a fraction of normal. His immune system had been attacking his own intestinal cells every time he ate bread, and he had been eating bread with every meal for as long as he could remember. He stopped eating wheat completely. Within a year he was in the 60th percentile for height and his ferritin stayed normal without supplementation for the first time in his life.</p>
<p><strong>Diana, 41.</strong> Her celiac disease presented not with gut symptoms but with ataxia — a progressive unsteadiness when walking that had baffled three neurologists over two years. Her brain MRI was normal; her nerve conduction studies showed a mild peripheral neuropathy. It was a fourth neurologist who knew about gluten ataxia — the neurological form of celiac disease, in which anti-gliadin antibodies damage the cerebellum and peripheral nerves rather than the intestine — who ordered the anti-tTG panel. Her titre was 340 U/mL. She had never had significant diarrhoea. Her gut was her warning sign that no one had read.</p>
<p><strong>Patrick, 54.</strong> He was asymptomatic. He only tested because his sister had been diagnosed with celiac disease the month before, and his gastroenterologist recommended first-degree relatives be screened. His anti-tTG came back positive; his biopsy showed partial villous atrophy. He had no gut symptoms, no fatigue he had attributed to anything specific, no anaemia. What he did have, his GP noted on reviewing his records, was a DEXA scan from three years earlier showing osteoporosis — unexplained at the time — in a man with no obvious calcium deficiency. The malabsorption had been silently removing calcium from his bones for years while he felt entirely well.</p>
''',
})

# 11. SJÖGREN'S SYNDROME ──────────────────────────────────────────────────────
ARTICLES.append({
    'title': "Sjögren's Syndrome: The Slow Drying Out of Glands",
    'slug': 'sjogrens-syndrome-autoimmune',
    'summary': (
        "Sjögren's syndrome targets the exocrine glands — particularly the salivary and lacrimal glands — "
        "with lymphocytic infiltration that destroys the cells responsible for producing saliva and tears. "
        "The resulting dryness is progressive, and the systemic inflammation extends beyond the glands."
    ),
    'content': svg(
        "Sjögren's Syndrome: Lymphocytic Destruction of Salivary Glands",
        '#0ea5e9',
        'Functional Acini', 'Lymphocyte Infiltration', 'Gland Destruction',
        (
            '<ellipse cx="95" cy="192" rx="20" ry="16" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3"/>'
            '<ellipse cx="130" cy="185" rx="18" ry="14" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3"/>'
            '<ellipse cx="110" cy="212" rx="18" ry="14" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3"/>'
            '<line x1="108" y1="208" x2="108" y2="225" stroke="#38bdf8" stroke-width="2"/>'
            '<line x1="125" y1="199" x2="115" y2="225" stroke="#38bdf8" stroke-width="2"/>'
            '<line x1="108" y1="225" x2="115" y2="225" stroke="#38bdf8" stroke-width="2"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#7dd3fc">Acini secrete saliva</text>'
        ),
        (
            '<ellipse cx="335" cy="192" rx="20" ry="16" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3" opacity=".5"/>'
            '<ellipse cx="370" cy="185" rx="18" ry="14" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3" opacity=".5"/>'
            '<ellipse cx="350" cy="212" rx="18" ry="14" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.3" opacity=".5"/>'
            '<circle cx="325" cy="185" r="5" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<circle cx="342" cy="178" r="5" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<circle cx="358" cy="182" r="5" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<circle cx="370" cy="202" r="5" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<circle cx="342" cy="206" r="5" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#7dd3fc">CD4+ T-cells, B cells surround ducts</text>'
        ),
        (
            '<rect x="550" y="175" width="100" height="55" rx="6" fill="#1c1917" stroke="#78716c" stroke-width="1.2"/>'
            '<line x1="560" y1="192" x2="640" y2="192" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="204" x2="640" y2="204" stroke="#57534e" stroke-width="1.2"/>'
            '<line x1="560" y1="216" x2="640" y2="216" stroke="#57534e" stroke-width="1.2"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#a8a29e">Fibrosis, xerostomia, xerophthalmia</text>'
        ),
        'Acinar cells produce fluid', 'Lymphocytic periductal infiltration', 'Acinar loss, dry mouth and dry eyes',
    ) + '''
<h2>What is happening in the body</h2>
<p>Sjögren's syndrome is classified as an exocrinopathy — a disease of exocrine glands. The salivary glands (parotid, submandibular, sublingual) and lacrimal glands are the primary targets, but any exocrine gland can be involved, including the pancreatic exocrine glands, bronchial mucous glands, and vaginal glands. The glands fill with periductal lymphocytic infiltrates — characteristic foci of 50 or more lymphocytes surrounding each duct — that progressively replace secretory acinar tissue with fibrosis.</p>
<p>The antibodies that define primary Sjögren's — anti-Ro/SSA and anti-La/SSB — target RNA-binding proteins that are exposed on the surface of apoptotic cells. Their pathogenic significance extends beyond the glands: anti-Ro antibodies cross the placenta and can cause congenital heart block in the fetus of a pregnant woman with Sjögren's. Systemically, Sjögren's produces fatigue and arthralgia, and carries a 10–44-fold increased risk of non-Hodgkin lymphoma arising from the chronically activated B cells within the infiltrated glands.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Xerostomia — dry mouth, difficulty swallowing, dental decay from reduced saliva</li>
<li>Keratoconjunctivitis sicca — dry, gritty, painful eyes</li>
<li>Parotid gland enlargement</li>
<li>Fatigue, often severe</li>
<li>Arthralgia and myalgia</li>
<li>Vaginal dryness</li>
<li>Peripheral neuropathy and autonomic dysfunction in some patients</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Sjögren's shares the anti-Ro/SSA autoantibody signature with lupus, and the two conditions frequently co-occur. The periductal lymphocytic infiltration suggests a pattern of antigen presentation at ductal epithelial surfaces, primed — as in other autoimmune conditions — by the systemic immune activation that follows intestinal permeability. HTLV-1 and EBV infections are known triggers for Sjögren's through molecular mimicry with salivary gland proteins, demonstrating that the same mechanism operates whether the priming antigen comes from gut or from a pathogen.</p>

<h2>What the clinical data shows</h2>
<p>Sjögren's syndrome is less frequently reported in the PKD case series than conditions like RA or Crohn's, but patients with secondary Sjögren's (occurring alongside another autoimmune condition) have shown improvement in sicca symptoms when the primary condition responds to PKD. The rationale is reduction in systemic immune activation — the reduction in anti-Ro and anti-La titres parallels the reduction seen in anti-dsDNA in lupus patients, suggesting the same upstream permeability-driven priming mechanism is being addressed.</p>

<h2>A life with this condition</h2>
<p><strong>Patricia, 52.</strong> She started keeping a water bottle on her desk, then one at her bedside, then one in her car. Her mouth was structurally dry — saliva barely coating the surface, food sticking to the roof of her mouth. Her dentist was alarmed by three new cavities in one year. The lip biopsy her rheumatologist ordered found 47 lymphocytes surrounding each salivary gland duct — immune cells patiently replacing her secretory tissue with scar. She would not produce more saliva than she currently had. She had attributed the dryness to age and air conditioning, not to an immune system quietly dismantling her glands year by year.</p>
<p><strong>Helen, 44.</strong> Her Sjögren's presented as fatigue so profound she had reduced her working hours, and a burning, electric pain in her feet she had been told was idiopathic small-fibre neuropathy. The dry mouth and dry eyes she had — she mentioned them almost as an afterthought to her rheumatologist. They were not afterthoughts; they were the diagnostic key. Her anti-Ro/SSA antibodies came back positive; the nerve damage was Sjögren's neuropathy, one of its most debilitating systemic features. For two years she had been treated for symptoms without a named disease. The name, when it arrived, was a relief even though it changed nothing about what had already been damaged.</p>
<p><strong>Anna, 47.</strong> She had been managing primary Sjögren's for six years when a neck lump appeared that her rheumatologist could not reassure her about. The lymphadenopathy in Sjögren's patients carries a real and elevated lymphoma risk — the chronically activated B cells within infiltrated glands can undergo malignant transformation. The excision biopsy showed reactive lymphoid hyperplasia, not lymphoma. She was told she had been lucky, and that she would need surveillance indefinitely. Sjögren's had moved from a disease about dryness, which she had learned to manage, to a disease about cancer risk, which she had not anticipated at diagnosis.</p>
''',
})

# 12. ANKYLOSING SPONDYLITIS ──────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Ankylosing Spondylitis: When the Spine Fuses Itself Shut',
    'slug': 'ankylosing-spondylitis-autoimmune',
    'summary': (
        'Ankylosing spondylitis targets the sacroiliac joints and spine with a unique perversity: '
        'instead of merely destroying joints, it replaces them with new bone. '
        'The final outcome, without treatment, is a fused, immobile spine — '
        'the "bamboo spine" of advanced disease.'
    ),
    'content': svg(
        'Ankylosing Spondylitis: Enthesitis to Spinal Fusion',
        '#a855f7',
        'Normal Sacroiliac Joint', 'Enthesitis & Inflammation', 'Syndesmophytes / Fusion',
        (
            '<rect x="95" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="100" y="168" width="15" height="60" fill="#4c1d95" stroke="none"/>'
            '<rect x="122" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="118" y="178" width="10" height="40" rx="2" fill="#7c3aed" fill-opacity=".3"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#d8b4fe">Joint space intact</text>'
        ),
        (
            '<rect x="335" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="362" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="358" y="172" width="10" height="52" rx="2" fill="#dc2626" fill-opacity=".5" stroke="#f87171" stroke-width="1"/>'
            '<circle cx="345" cy="190" r="5" fill="#7c2d12"/>'
            '<circle cx="345" cy="205" r="5" fill="#7c2d12"/>'
            '<circle cx="345" cy="220" r="5" fill="#7c2d12"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#d8b4fe">TNF, IL-17, bone marrow oedema</text>'
        ),
        (
            '<rect x="575" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="602" y="168" width="25" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.3"/>'
            '<rect x="598" y="165" width="10" height="68" rx="3" fill="#7c3aed" stroke="#a855f7" stroke-width="1.4"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#d8b4fe">Syndesmophyte bridges joint</text>'
        ),
        'Cartilage cushions SI joint', 'Enthesitis: inflammation at bone insertion', 'New bone bridges gap → ankylosis',
    ) + '''
<h2>What is happening in the body</h2>
<p>Ankylosing spondylitis begins at the entheses — the sites where ligaments, tendons, and joint capsules attach to bone. The sacroiliac joints are the initial target in over 90% of cases, producing the characteristic buttock pain and morning stiffness that may precede diagnosis by years. The entheseal inflammation (enthesitis) is driven by IL-17, IL-23, and TNF-alpha, produced by innate-like lymphocytes (ILC3 cells and MAIT cells) that reside at entheseal sites and respond to microbial signals from the gut.</p>
<p>What distinguishes AS from all other inflammatory arthritides is the osteoproliferative response. Instead of bone erosion (as in RA), AS triggers new bone formation. The entheseal inflammation stimulates osteoblast activity, and the repair response lays down new bone at the inflamed insertion sites. In the spine, this produces syndesmophytes — bony bridges growing from the vertebral body edges — that progressively span the disc spaces. Over decades, adjacent vertebrae fuse completely, producing the "bamboo spine" on plain X-ray: a single calcified column with no disc spaces visible.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Inflammatory back pain: worse in the morning, improves with exercise, not rest</li>
<li>Sacroiliac joint pain — buttock pain alternating sides</li>
<li>Progressive loss of spinal mobility — reduced lumbar flexion, chest expansion</li>
<li>Fatigue</li>
<li>Anterior uveitis — eye inflammation, the most common extra-articular feature</li>
<li>Peripheral arthritis (hip, shoulder in more severe cases)</li>
<li>Increased fracture risk from spinal rigidity</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>AS is the autoimmune condition most directly linked to gut inflammation. Over 60% of AS patients have subclinical gut inflammation on ileocolonoscopy, and 5–10% develop clinically manifest IBD. The Klebsiella pneumoniae hypothesis proposes that pullulanase — a starch-degrading enzyme produced by Klebsiella — mimics HLA-B27 (present in 90% of AS patients) and triggers the inflammatory response. Starch feeds Klebsiella selectively, and a low-starch diet has been shown in clinical studies to reduce Klebsiella counts, IgA anti-Klebsiella antibodies, and disease activity in AS patients.</p>

<h2>What the clinical data shows</h2>
<p>The low-starch diet was pioneered specifically for AS by Alan Ebringer at King's College London, based on the Klebsiella hypothesis. Clinical trials demonstrated significant reduction in acute-phase reactants and disease activity scores. The PKD, which is zero-starch by design, represents the maximally effective implementation of this principle. Paleomedicina patients with AS have shown MRI improvement in sacroiliac joint inflammation and reduction in BASDAI (disease activity) scores, with some achieving complete clinical remission.</p>

<h2>A life with this condition</h2>
<p><strong>Marcus, 26.</strong> His GP diagnosed a muscle strain and recommended rest. But rest made it worse — he was stiffest after long nights in bed, loosening up only after an hour of movement. He described his mornings as "rusting open." Three years later, an X-ray showed the first syndesmophytes bridging his lower lumbar vertebrae. The MRI of his sacroiliac joints lit up with bone marrow oedema — enthesitis. His immune system was attacking the ligament insertion points, and his repair response was building new bone in their place, slowly fusing his spine from the bottom up. His rheumatologist told him that without a DMARD he would likely have a bamboo spine by 50.</p>
<p><strong>Nadia, 24.</strong> Her AS took four years to diagnose partly because she was a young woman. Ankylosing spondylitis is still widely perceived as a disease of young men; women with axial spondyloarthritis tend to have more peripheral joint involvement and less classical sacroiliac changes on plain X-ray, making the diagnosis less obvious. Her rheumatologist eventually found her HLA-B27 positive and her MRI showed sacroiliac oedema that plain X-ray had missed entirely. She had been told repeatedly that her pain was related to her menstrual cycle. It was not.</p>
<p><strong>Richard, 34.</strong> His AS was found through his eye, not his spine. He had his third episode of anterior uveitis — a sudden, painful red eye with sensitivity to light — when his ophthalmologist asked if he had back stiffness in the mornings. He did, but had not mentioned it because he thought it was unrelated. The rheumatology referral produced a positive HLA-B27, an MRI showing established sacroiliitis, and a diagnosis of ankylosing spondylitis. The eye inflammation had been his body's recurring announcement of a spinal disease he had been living with unknowingly for years.</p>
''',
})

# 13. VITILIGO ────────────────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Vitiligo: The Immune System Erases the Skin\'s Color',
    'slug': 'vitiligo-autoimmune',
    'summary': (
        'Vitiligo is the selective destruction of melanocytes — the cells that produce skin pigment — '
        'by cytotoxic CD8+ T-cells that recognise melanocyte antigens as foreign. '
        'The resulting depigmented patches are a visible record of an ongoing immune assault '
        'on a completely harmless cell type.'
    ),
    'content': svg(
        'Vitiligo: CD8+ T-Cell Destruction of Melanocytes',
        '#8b5cf6',
        'Normal Melanocytes', 'Cytotoxic Attack', 'Depigmented Patch',
        (
            '<rect x="70" y="215" width="100" height="12" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<rect x="70" y="200" width="100" height="17" rx="2" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1"/>'
            '<circle cx="90" cy="209" r="7" fill="#7c3aed"/>'
            '<circle cx="108" cy="207" r="7" fill="#7c3aed"/>'
            '<circle cx="126" cy="209" r="7" fill="#7c3aed"/>'
            '<circle cx="144" cy="207" r="7" fill="#7c3aed"/>'
            '<rect x="70" y="180" width="100" height="22" rx="2" fill="#312e81" stroke="#818cf8" stroke-width="1" opacity=".7"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd">Melanocytes in basal layer</text>'
        ),
        (
            '<rect x="310" y="215" width="100" height="12" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<rect x="310" y="200" width="100" height="17" rx="2" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1"/>'
            '<circle cx="330" cy="209" r="7" fill="#7c3aed" opacity=".4"/>'
            '<circle cx="348" cy="207" r="7" fill="#7c3aed"/>'
            '<circle cx="366" cy="209" r="7" fill="#7c3aed" opacity=".2"/>'
            '<circle cx="384" cy="207" r="7" fill="#7c3aed"/>'
            '<circle cx="326" cy="192" r="7" stroke="#8b5cf6" stroke-width="1.2" fill="#3730a3"/>'
            '<line x1="323" y1="186" x2="319" y2="180" stroke="#8b5cf6" stroke-width="1"/>'
            '<line x1="329" y1="185" x2="332" y2="179" stroke="#8b5cf6" stroke-width="1"/>'
            '<line x1="333" y1="188" x2="338" y2="184" stroke="#8b5cf6" stroke-width="1"/>'
            '<line x1="326" y1="199" x2="330" y2="202" stroke="#8b5cf6" stroke-width="1.2"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd">CD8+ T-cells kill melanocytes</text>'
        ),
        (
            '<rect x="550" y="215" width="100" height="12" rx="2" fill="#374151" stroke="#6b7280" stroke-width="1"/>'
            '<rect x="550" y="200" width="100" height="17" rx="2" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>'
            '<rect x="550" y="180" width="100" height="22" rx="2" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" opacity=".7"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#c4b5fd">No melanocytes, no pigment</text>'
        ),
        'Melanocytes produce melanin', 'IFN-γ activates CD8+ T-cells vs TYRP1/2', 'Melanocytes eliminated, white patch forms',
    ) + '''
<h2>What is happening in the body</h2>
<p>Melanocytes are the pigment-producing cells of the skin's basal layer, responsible for synthesising melanin and transferring it to keratinocytes. In vitiligo, CD8+ cytotoxic T-cells recognise melanocyte-specific antigens — particularly tyrosinase, TYRP1, and TYRP2 — and eliminate melanocytes from discrete patches of skin. The T-cells are activated by IFN-gamma signalling and express the CXCR3 receptor, homing to skin in response to the CXCL9 and CXCL10 chemokines produced by keratinocytes under IFN-gamma stimulation.</p>
<p>The autoimmune recognition of melanocyte antigens is thought to begin with cellular stress responses in the melanocytes themselves. Reactive oxygen species (ROS) within melanocytes — particularly elevated in vitiligo lesions — cause protein oxidation and the exposure of neoantigens that activate innate immune signalling via DAMP pathways. Stressed melanocytes upregulate NKG2D ligands on their surface, marking themselves for elimination by NK cells and cytotoxic T-cells. The initial trigger appears to require a systemic immune activation event — consistent with the observation that vitiligo onset frequently follows infection, psychological stress, or chemical exposure.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Depigmented, chalk-white patches on skin — typically at periorificial areas (around eyes, mouth), dorsal hands, wrists, knees</li>
<li>Koebner phenomenon: patches appearing at sites of skin injury</li>
<li>Accelerated depigmentation following sunburn in affected areas</li>
<li>Premature greying of hair in involved areas</li>
<li>No pain or physical impairment, but significant psychological impact</li>
<li>Association with other autoimmune conditions: thyroid disease, type 1 diabetes, Addison's disease</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>The co-occurrence of vitiligo with thyroid autoimmunity, type 1 diabetes, and other organ-specific autoimmune conditions in the same patients and families reveals a shared predisposition to autoimmune tissue destruction driven by common upstream mechanisms. The melanocyte-specific T-cell response requires the same breakdown in peripheral tolerance that drives all autoimmune conditions. The gut, as the site of largest immune activation surface area, is the most likely site of initial tolerance disruption — and the dietary removal of permeability-promoting antigens reduces the systemic IFN-gamma and IL-15 signalling that sustains the melanocyte-directed T-cell response.</p>

<h2>What the clinical data shows</h2>
<p>Vitiligo is among the more difficult autoimmune conditions to reverse because melanocytes, once destroyed, must be replaced by migration from hair follicle reservoirs — a slow process. Early-stage vitiligo, before complete melanocyte depletion in affected areas, shows the best response to immune intervention. Patients adopting PKD with active vitiligo have reported stabilisation of existing lesions and some repigmentation, particularly in areas with remaining follicular melanocytes. The mechanism is reduction in IFN-gamma-driven CXCL9/CXCL10 chemokine expression that maintains the cytotoxic T-cell homing to skin.</p>

<h2>A life with this condition</h2>
<p><strong>Priya, 17.</strong> Her mother had vitiligo on her hands; she knew what the patch above her eyebrow was immediately. What she did not expect was the speed — both wrists within six months, patches around both eyes, a streak of white appearing in her dark hair. The patches were painless. That was the strange cruelty of it: an immune assault visible to anyone who looked at her that she felt not at all. Her CD8+ T-cells had identified something in her melanocytes and were eliminating them systematically. Each white patch was a cleared zone, meticulously produced by an immune system that had confused harmless pigment-makers for a threat that did not exist.</p>
<p><strong>James, 29.</strong> His vitiligo appeared within two months of the most stressful period of his life — a business collapse, a relationship ending, six weeks of almost no sleep. He had read that psychological stress could trigger autoimmune conditions but had always found that idea vague and unscientific until depigmented patches appeared on both hands and wrists, places where stress-induced cortisol dysregulation is thought to lower the threshold for melanocyte-directed immune activation. His dermatologist said the timing was consistent. The patches were permanent. The stress had passed. The record of it remained on his skin.</p>
<p><strong>Fatima, 42.</strong> Her vitiligo was confined to one side of her face — the segmental pattern, which follows a dermatomal distribution and behaves differently from the generalised form. It is faster to spread initially but then typically stops, unlike generalised vitiligo which can continue expanding for life. What her dermatologist found on routine workup was more concerning than the skin: her TSH was elevated and her anti-TPO antibodies were 480 IU/mL. She had Hashimoto's thyroiditis alongside her vitiligo — two autoimmune conditions targeting two different cell types, driven by the same underlying immune terrain. She had come in for her skin and left with a second diagnosis.</p>
''',
})

# 14. MYASTHENIA GRAVIS ───────────────────────────────────────────────────────
ARTICLES.append({
    'title': 'Myasthenia Gravis: When Signals Can No Longer Reach the Muscles',
    'slug': 'myasthenia-gravis-autoimmune',
    'summary': (
        'Myasthenia gravis is caused by antibodies that block acetylcholine receptors at the neuromuscular '
        'junction. The nerve fires normally, but the signal cannot be received by the muscle. '
        'The hallmark is fatigable weakness — muscles that work at rest but fail progressively with use.'
    ),
    'content': svg(
        'Myasthenia Gravis: AChR Antibodies Block Neuromuscular Transmission',
        '#06b6d4',
        'Normal NMJ', 'AChR Antibody Blockade', 'Muscle Transmission Failure',
        (
            '<rect x="80" y="160" width="80" height="16" rx="4" fill="#164e63" stroke="#06b6d4" stroke-width="1.3"/>'
            '<line x1="95" y1="176" x2="95" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<line x1="110" y1="176" x2="110" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<line x1="125" y1="176" x2="125" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<line x1="140" y1="176" x2="140" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<circle cx="95" cy="194" r="4" fill="#0e7490"/>'
            '<circle cx="110" cy="194" r="4" fill="#0e7490"/>'
            '<circle cx="125" cy="194" r="4" fill="#0e7490"/>'
            '<circle cx="140" cy="194" r="4" fill="#0e7490"/>'
            '<rect x="78" y="200" width="84" height="25" rx="4" fill="#083344" stroke="#06b6d4" stroke-width="1.2"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#67e8f9">ACh binds receptor → contraction</text>'
        ),
        (
            '<rect x="320" y="160" width="80" height="16" rx="4" fill="#164e63" stroke="#06b6d4" stroke-width="1.3"/>'
            '<line x1="335" y1="176" x2="335" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<line x1="365" y1="176" x2="365" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<line x1="395" y1="176" x2="395" y2="190" stroke="#06b6d4" stroke-width="1.5"/>'
            '<circle cx="335" cy="194" r="4" fill="#0e7490"/>'
            '<circle cx="365" cy="194" r="4" fill="#0e7490"/>'
            '<circle cx="395" cy="194" r="4" fill="#0e7490"/>'
            '<line x1="328" y1="192" x2="342" y2="200" stroke="#f87171" stroke-width="1.8"/>'
            '<line x1="342" y1="192" x2="328" y2="200" stroke="#f87171" stroke-width="1.8"/>'
            '<line x1="358" y1="192" x2="372" y2="200" stroke="#f87171" stroke-width="1.8"/>'
            '<line x1="372" y1="192" x2="358" y2="200" stroke="#f87171" stroke-width="1.8"/>'
            '<rect x="318" y="203" width="84" height="25" rx="4" fill="#083344" stroke="#06b6d4" stroke-width="1.2"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#67e8f9">Anti-AChR IgG blocks binding site</text>'
        ),
        (
            '<rect x="560" y="160" width="80" height="16" rx="4" fill="#164e63" stroke="#06b6d4" stroke-width="1.3" opacity=".6"/>'
            '<line x1="575" y1="176" x2="575" y2="190" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="2 2"/>'
            '<line x1="600" y1="176" x2="600" y2="190" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="2 2"/>'
            '<line x1="625" y1="176" x2="625" y2="190" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="2 2"/>'
            '<rect x="558" y="200" width="84" height="25" rx="4" fill="#1c1917" stroke="#78716c" stroke-width="1.2"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#67e8f9">Signal fails → fatigable weakness</text>'
        ),
        'Vesicles release ACh → muscle fires', 'IgG anti-AChR blocks, degrades receptor', 'Reduced receptor density → fatigue on use',
    ) + '''
<h2>What is happening in the body</h2>
<p>Voluntary muscle contraction requires a reliable chain of communication from nerve to muscle. At the neuromuscular junction (NMJ), a motor nerve terminal releases acetylcholine (ACh) vesicles into the synaptic cleft when an action potential arrives. ACh diffuses across the cleft and binds to acetylcholine receptors (AChR) on the muscle end-plate, triggering the ion flux that initiates muscle contraction. In myasthenia gravis, IgG antibodies directed against the AChR's alpha subunit — the ACh binding site — occupy and block those receptors. They also activate complement at the NMJ, degrading the receptor density of the post-synaptic membrane over time.</p>
<p>The clinical hallmark — fatigable weakness — reflects the physiological consequence of reduced receptor density. At rest, enough receptors remain unblocked for adequate transmission. With repeated use, the vesicle release per stimulus declines (normal synaptic fatigue), but with a reduced receptor density there is no margin to compensate. Transmission fails progressively within the same muscle contraction sequence. Resting restores some capacity, explaining why MG patients are weakest at the end of a task and strongest after sleep.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Ptosis — drooping eyelids, typically asymmetric and worse at day's end</li>
<li>Diplopia — double vision from asymmetric extraocular muscle involvement</li>
<li>Dysarthria and dysphagia — slurred speech, difficulty swallowing</li>
<li>Proximal limb weakness — difficulty raising arms or climbing stairs</li>
<li>Myasthenic crisis: respiratory muscle failure requiring ventilation</li>
<li>Symptoms worsen with heat, illness, and exertion</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>The AChR-specific B cells that produce the pathogenic IgG require thymus-based T cell help — which is why the thymus is abnormal in 75% of AChR-positive MG patients (thymoma in 10%, thymic hyperplasia in 65%). Thymectomy is the only curative intervention and confirms the thymic origin of the autoimmune breach. The gut-thymus axis and the shared mechanisms of gut-driven autoimmunity connect MG to the same upstream permeability terrain. IgG anti-AChR titres correlate with systemic inflammatory markers and fall when the systemic immune burden is reduced.</p>

<h2>What the clinical data shows</h2>
<p>MG is less frequently documented in the PKD literature, reflecting the rarer presentation of thymoma-associated cases. However, ocular MG — the limited form affecting only eye muscles — and generalised MG in patients without thymoma have shown improvement in disease activity scores on anti-inflammatory diets. The primary therapeutic value of dietary intervention is reduction of the systemic inflammatory drive that maintains AChR-directed B cell activity, potentially reducing antibody titres and disease severity over time.</p>

<h2>A life with this condition</h2>
<p><strong>Fiona, 41.</strong> She first noticed her left eyelid drooping on a photograph. Within a week she was wearing an eye patch to drive. Her neurologist performed an edrophonium test and watched her eyelid lift completely for ninety seconds before falling again — a brief, chemical reversal of the antibody blockade. The mechanism he described was almost offensively mechanical: antibodies sitting in the docking ports of her muscle receptors, blocking the acetylcholine trying to land. Her nerves were firing. The messages were arriving. There was simply nowhere to deliver them. By evening every day she had used up whatever the morning had given her.</p>
<p><strong>George, 68.</strong> His MG diagnosis came via a CT scan ordered for an unrelated cough, which found a thymoma — a tumour of the thymus gland that is present in 10% of MG patients. He had been having mild swallowing difficulties for months that he had attributed to reflux. The thymoma was removed surgically; the myasthenia gravis, which the tumour had been generating, was confirmed by anti-AChR antibody testing during his admission. His surgery was successful, and his antibody titres declined over the following year. Thymectomy is the only intervention that addresses the source of AChR-directed B cell activation rather than managing its downstream effects.</p>
<p><strong>Emma, 24.</strong> She spent eight months being investigated for a functional neurological disorder before a neurologist thought to test acetylcholine receptor antibodies. Her drooping eyelid had been attributed to stress; her swallowing difficulty had been attributed to anxiety. She had been referred for psychotherapy. Her anti-AChR titre came back at 18 nmol/L — markedly elevated. She started pyridostigmine that week. The eyelid lift was visible within an hour of the first dose. She had been offered an explanation for a physical disease that reduced its cause to her psychology. The antibody test ended eight months of that.</p>
''',
})

# 15. ANTIPHOSPHOLIPID SYNDROME ───────────────────────────────────────────────
ARTICLES.append({
    'title': 'Antiphospholipid Syndrome: The Clotting Disorder No One Sees Coming',
    'slug': 'antiphospholipid-syndrome-autoimmune',
    'summary': (
        'Antiphospholipid syndrome is an autoimmune thrombophilia: antibodies directed at phospholipid-binding '
        'proteins trigger clotting in arteries and veins throughout the body. '
        'It is the most common acquired cause of recurrent miscarriage and unexplained stroke in young adults, '
        'yet most patients have no warning before the first thrombotic event.'
    ),
    'content': svg(
        'Antiphospholipid Syndrome: aPL Antibodies Trigger Thrombosis',
        '#e11d48',
        'Normal Vessel Wall', 'aPL Antibody Binding', 'Thrombosis',
        (
            '<ellipse cx="120" cy="200" rx="52" ry="36" fill="none" stroke="#e11d48" stroke-width="1.5" opacity=".5"/>'
            '<ellipse cx="120" cy="200" rx="38" ry="22" fill="#450a0a" stroke="#e11d48" stroke-width="1.2" opacity=".7"/>'
            '<ellipse cx="108" cy="198" rx="7" ry="4" fill="#fca5a5" fill-opacity=".5"/>'
            '<ellipse cx="124" cy="196" rx="7" ry="4" fill="#fca5a5" fill-opacity=".5"/>'
            '<ellipse cx="116" cy="206" rx="6" ry="3.5" fill="#fca5a5" fill-opacity=".5"/>'
            '<text x="120" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fda4af">Blood flows freely</text>'
        ),
        (
            '<ellipse cx="360" cy="200" rx="52" ry="36" fill="none" stroke="#e11d48" stroke-width="1.5" opacity=".5"/>'
            '<ellipse cx="360" cy="200" rx="38" ry="22" fill="#450a0a" stroke="#e11d48" stroke-width="1.2" opacity=".7"/>'
            '<line x1="345" y1="182" x2="333" y2="182" stroke="#fda4af" stroke-width="1.3"/>'
            '<line x1="333" y1="182" x2="337" y2="190" stroke="#fda4af" stroke-width="1.3"/>'
            '<line x1="333" y1="182" x2="341" y2="188" stroke="#fda4af" stroke-width="1.3"/>'
            '<circle cx="345" cy="182" r="6" fill="#9f1239" stroke="#e11d48" stroke-width="1"/>'
            '<line x1="372" y1="215" x2="384" y2="215" stroke="#fda4af" stroke-width="1.3"/>'
            '<line x1="384" y1="215" x2="380" y2="207" stroke="#fda4af" stroke-width="1.3"/>'
            '<line x1="384" y1="215" x2="376" y2="209" stroke="#fda4af" stroke-width="1.3"/>'
            '<circle cx="372" cy="215" r="6" fill="#9f1239" stroke="#e11d48" stroke-width="1"/>'
            '<text x="360" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fda4af">aPL binds β2-GPI on endothelium</text>'
        ),
        (
            '<ellipse cx="600" cy="200" rx="52" ry="36" fill="none" stroke="#e11d48" stroke-width="1.5" opacity=".5"/>'
            '<path d="M562,200 Q575,195 588,202 Q600,210 612,200 Q624,190 638,200" fill="#7f1d1d" stroke="#e11d48" stroke-width="1.5"/>'
            '<path d="M570,204 Q582,208 594,204 Q604,200 616,204" fill="#991b1b" fill-opacity=".7"/>'
            '<text x="600" y="255" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#fda4af">Clot occludes vessel lumen</text>'
        ),
        'Endothelium repels clotting', 'aPL activates endothelium and platelets', 'Arterial or venous thrombosis',
    ) + '''
<h2>What is happening in the body</h2>
<p>Antiphospholipid syndrome (APS) is caused by autoantibodies — antiphospholipid antibodies (aPL) — that target phospholipid-binding plasma proteins, most importantly beta-2 glycoprotein I (β2-GPI) and prothrombin. β2-GPI is a natural anticoagulant protein that binds to phospholipids exposed on cell membranes under conditions of cellular stress. When aPL antibodies bind β2-GPI on endothelial cells, monocytes, and platelets, they trigger an activation cascade: endothelial cells upregulate tissue factor and adhesion molecules; monocytes produce procoagulant microparticles; platelets aggregate. The net effect is a shift from the normal anticoagulant surface of blood vessels to a prothrombotic one.</p>
<p>The clinical consequence is arterial and venous thrombosis — blood clots forming in vessels where none should form. Deep vein thrombosis and pulmonary embolism are the most common venous manifestations. Stroke and transient ischaemic attack are the most dangerous arterial manifestations, particularly in young patients who have no traditional cardiovascular risk factors. In pregnancy, aPL antibodies interfere with placental implantation and perfusion, causing recurrent miscarriage, intrauterine growth restriction, and pre-eclampsia.</p>

<h2>The symptoms this produces</h2>
<ul>
<li>Deep vein thrombosis — swollen, painful, red leg</li>
<li>Pulmonary embolism — sudden breathlessness, chest pain, collapse</li>
<li>Stroke or TIA in young adults without obvious cardiovascular risk</li>
<li>Recurrent pregnancy loss (particularly second-trimester miscarriage)</li>
<li>Livedo reticularis — mottled, net-like skin discolouration</li>
<li>Thrombocytopenia (low platelets, paradoxically)</li>
<li>Catastrophic APS: simultaneous thrombosis in multiple organs — a rare, life-threatening variant</li>
</ul>

<h2>How this fits the autoimmune pattern</h2>
<p>Antiphospholipid antibodies are frequently triggered by infection — particularly by Gram-negative bacteria expressing phospholipid-mimicking antigens that prime cross-reactive B-cells, and by EBV and CMV that expose β2-GPI during cellular lysis. The gut is the largest reservoir of Gram-negative organisms, and increased intestinal permeability provides the systemic exposure to bacterial lipopolysaccharide and cell membrane phospholipids that generates aPL antibodies. APS frequently co-occurs with SLE — a relationship that underscores the shared upstream immune activation environment — and shares with lupus the anti-phospholipid/nuclear antigen antibody signature.</p>

<h2>What the clinical data shows</h2>
<p>APS management typically requires long-term anticoagulation with warfarin or direct oral anticoagulants (DOACs) — drugs that manage the thrombotic risk but do not address the underlying aPL antibody production. Dietary intervention targeting the gut permeability and dysbiosis that drives aPL production is an emerging complement to pharmacological management. Several APS patients in clinical practice have shown declining aPL titres on anti-inflammatory dietary protocols, suggesting that the immunological driver is accessible to dietary modification, even when pharmacological management of thrombotic risk remains necessary.</p>

<h2>A life with this condition</h2>
<p><strong>Kezia, 34.</strong> She had her third miscarriage, all in the second trimester. Each had been explained individually — chromosomal abnormality, cervical incompetence, suboptimal luteal support. After the third loss, her obstetrician ordered a thrombophilia screen. All three antiphospholipid markers came back positive, confirmed on repeat testing twelve weeks later. The syndrome had probably also caused the brief left arm numbness she had had at 29 and attributed to a trapped nerve. Her immune system had been producing antibodies that turned her blood vessels into clot-forming surfaces. She had been one thrombotic event away from a stroke for years and had not known it.</p>
<p><strong>Oliver, 29.</strong> He woke up unable to move his right arm and with slurred speech. In the emergency department, the stroke team worked quickly — clot-busting medication within the window, MRI confirming a left middle cerebral artery territory infarct. He was 29, did not smoke, had normal cholesterol, normal blood pressure, no family history of early stroke. The haematology workup ordered during his admission found lupus anticoagulant and anti-cardiolipin IgG antibodies. He had had a stroke from a condition that had been generating a clot-prone vascular environment for years before anyone thought to look for it.</p>
<p><strong>Sophie, 45.</strong> Her APS was discovered after her second DVT in three years, the second of which threw a pulmonary embolism that was found incidentally on a CT scan ordered for chest pain. Her haematologist tested her for thrombophilia and found antiphospholipid antibodies; further investigation found she also had lupus — secondary APS, occurring in the context of another autoimmune disease. She was told she would need anticoagulation for life and was referred to a lupus clinic. She had spent three years being told her DVTs were unprovoked, which had shaped her treatment. They were not unprovoked. They had a cause, and the cause had a treatment.</p>
''',
})


class Command(BaseCommand):
    help = 'Load 15 autoimmune disease articles with process SVG illustrations'

    def handle(self, *args, **options):
        pillar, _ = Pillar.objects.get_or_create(
            slug='autoimmune-disease',
            defaults={
                'name': 'Autoimmune Disease',
                'description': (
                    'How autoimmune diseases start, why your immune system attacks your own body, '
                    'and what the clinical evidence says about reversing them through diet.'
                ),
                'order': 5,
            }
        )

        for data in ARTICLES:
            obj, created = Article.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'summary': data['summary'],
                    'content': data['content'],
                    'pillar': pillar,
                    'published': True,
                }
            )
            verb = 'Created' if created else 'Updated'
            self.stdout.write(f'{verb}: {data["title"]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone. {len(ARTICLES)} articles loaded.'
        ))
