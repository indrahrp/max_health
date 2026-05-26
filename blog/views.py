from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from .models import Post, Project, Category, Tag, BookReview
from .forms import CommentForm, SubscribeForm


# SVG illustrations for Physical Health topic cards — each conveys the disease process at a glance
_HEALTH_ILLUS = {
    'autoimmune': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="60" cy="40" r="17" stroke="currentColor" stroke-width="1.5"/>'
        '<circle cx="60" cy="40" r="6" fill="currentColor" fill-opacity=".25"/>'
        '<circle cx="13" cy="22" r="7" stroke="currentColor" stroke-width="1.3" stroke-opacity=".85"/>'
        '<line x1="13" y1="15" x2="13" y2="9" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="18" y1="17" x2="22" y2="12" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="8" y1="17" x2="4" y2="12" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="20" y1="26" x2="41" y2="35" stroke="currentColor" stroke-width="1.3" stroke-opacity=".9"/>'
        '<polygon points="38,31 45,36 39,40" fill="currentColor" fill-opacity=".9"/>'
        '<circle cx="107" cy="20" r="7" stroke="currentColor" stroke-width="1.3" stroke-opacity=".85"/>'
        '<line x1="107" y1="13" x2="107" y2="7" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="112" y1="15" x2="116" y2="10" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="102" y1="15" x2="98" y2="10" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="101" y1="25" x2="80" y2="35" stroke="currentColor" stroke-width="1.3" stroke-opacity=".9"/>'
        '<polygon points="82,31 75,36 81,40" fill="currentColor" fill-opacity=".9"/>'
        '<circle cx="18" cy="68" r="7" stroke="currentColor" stroke-width="1.3" stroke-opacity=".85"/>'
        '<line x1="18" y1="75" x2="18" y2="80" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="13" y1="72" x2="9" y2="77" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="23" y1="72" x2="27" y2="77" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<line x1="24" y1="62" x2="43" y2="51" stroke="currentColor" stroke-width="1.3" stroke-opacity=".9"/>'
        '<polygon points="41,48 48,53 43,56" fill="currentColor" fill-opacity=".9"/>'
        '</svg>'
    ),
    'heart-disease': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="60" cy="40" r="34" stroke="currentColor" stroke-width="1.5" stroke-opacity=".45"/>'
        '<circle cx="60" cy="40" r="27" stroke="currentColor" stroke-width="1" stroke-dasharray="3 2" stroke-opacity=".35"/>'
        '<path d="M38 20 Q55 11 76 18 Q90 24 89 38 Q90 56 72 62 Q55 66 40 57 Q24 46 38 20Z" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.3"/>'
        '<path d="M40 22 Q57 15 76 22 Q87 29 86 40" stroke="currentColor" stroke-width="1.6" stroke-opacity=".65"/>'
        '<circle cx="75" cy="48" r="11" fill="currentColor" fill-opacity=".07" stroke="currentColor" stroke-width="1" stroke-opacity=".45"/>'
        '<ellipse cx="75" cy="45" rx="5" ry="3" fill="currentColor" fill-opacity=".45"/>'
        '<ellipse cx="81" cy="52" rx="5" ry="3" fill="currentColor" fill-opacity=".38"/>'
        '<ellipse cx="69" cy="52" rx="4" ry="2.5" fill="currentColor" fill-opacity=".38"/>'
        '</svg>'
    ),
    'diabetes': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<rect x="28" y="14" width="64" height="52" rx="16" stroke="currentColor" stroke-width="1.5"/>'
        '<ellipse cx="60" cy="40" rx="14" ry="10" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1"/>'
        '<rect x="87" y="28" width="10" height="22" rx="3" stroke="currentColor" stroke-width="1.4"/>'
        '<line x1="89" y1="34" x2="95" y2="46" stroke="currentColor" stroke-width="1.6" stroke-opacity=".9"/>'
        '<line x1="95" y1="34" x2="89" y2="46" stroke="currentColor" stroke-width="1.6" stroke-opacity=".9"/>'
        '<path d="M5 20 L11 14 L19 14 L23 20 L19 26 L11 26Z" stroke="currentColor" stroke-width="1.2" stroke-opacity=".85"/>'
        '<path d="M100 8 L106 2 L114 2 L118 8 L114 14 L106 14Z" stroke="currentColor" stroke-width="1.2" stroke-opacity=".85"/>'
        '<path d="M3 52 L9 46 L17 46 L21 52 L17 58 L9 58Z" stroke="currentColor" stroke-width="1.2" stroke-opacity=".6"/>'
        '<line x1="109" y1="34" x2="109" y2="25" stroke="currentColor" stroke-width="1.3" stroke-opacity=".7"/>'
        '<line x1="109" y1="25" x2="105" y2="19" stroke="currentColor" stroke-width="1.3" stroke-opacity=".7"/>'
        '<line x1="109" y1="25" x2="113" y2="19" stroke="currentColor" stroke-width="1.3" stroke-opacity=".7"/>'
        '<circle cx="109" cy="34" r="2.5" fill="currentColor" fill-opacity=".7"/>'
        '<line x1="98" y1="39" x2="107" y2="39" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2" stroke-opacity=".6"/>'
        '</svg>'
    ),
    'weight': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="38" cy="42" r="30" stroke="currentColor" stroke-width="1.5"/>'
        '<circle cx="36" cy="40" r="21" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1" stroke-dasharray="3 2"/>'
        '<circle cx="51" cy="25" r="7" fill="currentColor" fill-opacity=".3" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="25" cy="31" r="5" fill="currentColor" fill-opacity=".3" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="22" cy="55" r="6" fill="currentColor" fill-opacity=".3" stroke="currentColor" stroke-width="1"/>'
        '<ellipse cx="57" cy="58" rx="4" ry="3" fill="currentColor" fill-opacity=".55"/>'
        '<line x1="74" y1="42" x2="82" y2="42" stroke="currentColor" stroke-width="1.2" stroke-opacity=".45"/>'
        '<polygon points="80,39 85,42 80,45" fill="currentColor" fill-opacity=".45"/>'
        '<circle cx="98" cy="42" r="16" stroke="currentColor" stroke-width="1.3" stroke-opacity=".7"/>'
        '<circle cx="97" cy="41" r="9" fill="currentColor" fill-opacity=".15" stroke="currentColor" stroke-width="1" stroke-opacity=".6"/>'
        '<ellipse cx="104" cy="52" rx="3" ry="2" fill="currentColor" fill-opacity=".5"/>'
        '</svg>'
    ),
    'alzheimers': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="16" cy="40" r="12" stroke="currentColor" stroke-width="1.4"/>'
        '<circle cx="16" cy="40" r="5" fill="currentColor" fill-opacity=".3"/>'
        '<line x1="16" y1="28" x2="12" y2="14" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<line x1="16" y1="28" x2="20" y2="14" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<line x1="8" y1="36" x2="2" y2="26" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<line x1="28" y1="40" x2="47" y2="40" stroke="currentColor" stroke-width="1.6"/>'
        '<circle cx="59" cy="38" r="5" fill="currentColor" fill-opacity=".38" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="65" cy="44" r="5" fill="currentColor" fill-opacity=".38" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="55" cy="44" r="4.5" fill="currentColor" fill-opacity=".38" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="63" cy="34" r="4" fill="currentColor" fill-opacity=".38" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="57" cy="34" r="4" fill="currentColor" fill-opacity=".38" stroke="currentColor" stroke-width="1"/>'
        '<line x1="49" y1="36" x2="54" y2="44" stroke="currentColor" stroke-width="1.8" stroke-opacity=".75"/>'
        '<line x1="54" y1="36" x2="49" y2="44" stroke="currentColor" stroke-width="1.8" stroke-opacity=".75"/>'
        '<line x1="73" y1="40" x2="92" y2="40" stroke="currentColor" stroke-width="1.6"/>'
        '<circle cx="104" cy="40" r="12" stroke="currentColor" stroke-width="1.4"/>'
        '<circle cx="104" cy="40" r="5" fill="currentColor" fill-opacity=".3"/>'
        '<line x1="104" y1="28" x2="108" y2="14" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<line x1="104" y1="28" x2="100" y2="14" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<line x1="112" y1="36" x2="118" y2="26" stroke="currentColor" stroke-width="1.2" stroke-opacity=".65"/>'
        '<path d="M6 52 Q10 58 7 64 Q4 70 9 74" stroke="currentColor" stroke-width="1.3" stroke-dasharray="2.5 1.5" stroke-opacity=".75"/>'
        '</svg>'
    ),
    'liver-disease': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<polygon points="60,4 88,20 88,60 60,76 32,60 32,20" stroke="currentColor" stroke-width="1.5"/>'
        '<circle cx="48" cy="27" r="9" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="68" cy="23" r="7" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="76" cy="39" r="10" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="54" cy="46" r="11" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="42" cy="55" r="8" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<circle cx="68" cy="58" r="8" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1"/>'
        '<ellipse cx="55" cy="36" rx="4" ry="3" fill="currentColor" fill-opacity=".65"/>'
        '<circle cx="10" cy="30" r="5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5" stroke-opacity=".7"/>'
        '<circle cx="108" cy="26" r="4" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5" stroke-opacity=".6"/>'
        '<circle cx="14" cy="60" r="5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5" stroke-opacity=".6"/>'
        '</svg>'
    ),
    'kidney-disease': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<circle cx="60" cy="40" r="30" stroke="currentColor" stroke-width="1.4" stroke-opacity=".6"/>'
        '<path d="M60 18 C72 20 82 28 84 40 C86 54 76 64 60 66 C44 68 32 58 30 44 C26 30 40 20 60 18" stroke="currentColor" stroke-width="1.6" stroke-opacity=".8" fill="none"/>'
        '<path d="M60 24 C68 27 74 34 72 44 C70 54 62 58 52 54 C42 50 40 42 44 34 C48 26 54 23 60 24" stroke="currentColor" stroke-width="1.2" stroke-opacity=".5" fill="none"/>'
        '<line x1="50" y1="28" x2="56" y2="37" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-opacity=".85"/>'
        '<line x1="64" y1="34" x2="70" y2="45" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-opacity=".85"/>'
        '<line x1="47" y1="48" x2="55" y2="55" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-opacity=".85"/>'
        '<circle cx="30" cy="22" r="2.5" fill="currentColor" fill-opacity=".65"/>'
        '<circle cx="22" cy="38" r="2" fill="currentColor" fill-opacity=".55"/>'
        '<circle cx="28" cy="58" r="2.5" fill="currentColor" fill-opacity=".65"/>'
        '<circle cx="90" cy="18" r="2" fill="currentColor" fill-opacity=".55"/>'
        '<circle cx="94" cy="62" r="2.5" fill="currentColor" fill-opacity=".65"/>'
        '</svg>'
    ),
    'mishaps': (
        '<svg viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<rect x="22" y="16" width="52" height="58" rx="5" stroke="currentColor" stroke-width="1.5"/>'
        '<rect x="38" y="12" width="20" height="9" rx="4" stroke="currentColor" stroke-width="1.4"/>'
        '<line x1="30" y1="32" x2="64" y2="32" stroke="currentColor" stroke-width="1" stroke-opacity=".55"/>'
        '<line x1="30" y1="40" x2="64" y2="40" stroke="currentColor" stroke-width="1" stroke-opacity=".55"/>'
        '<line x1="30" y1="48" x2="52" y2="48" stroke="currentColor" stroke-width="1" stroke-opacity=".55"/>'
        '<line x1="30" y1="57" x2="44" y2="68" stroke="currentColor" stroke-width="2.2" stroke-opacity=".9"/>'
        '<line x1="44" y1="57" x2="30" y2="68" stroke="currentColor" stroke-width="2.2" stroke-opacity=".9"/>'
        '<path d="M90 18 L108 58 L72 58Z" stroke="currentColor" stroke-width="1.5" stroke-opacity=".85" fill="none"/>'
        '<line x1="90" y1="30" x2="90" y2="46" stroke="currentColor" stroke-width="2.2" stroke-opacity=".9"/>'
        '<circle cx="90" cy="52" r="2" fill="currentColor" fill-opacity=".9"/>'
        '</svg>'
    ),
}

# Cogitra section system — 9 sections, each with its own accent + curve + typography
# Curve SVG paths are in viewBox 0 0 200 200
SECTION_CONFIG = {
    'ai': {
        'index': 1, 'short': 'AI',
        'title': 'Artificial Intelligence',
        'tagline': 'Machine learning, deep learning, research, tools, and trends.',
        'note': 'Two decades into the AI summer, the patient work has barely begun. This section covers the architectures, the open questions, and the slow weather that follows the headlines.',
        'editor': 'Lena Okafor',
        'accent_hex': '#5b6cff',
        'curve': 'M 40 30 L 60 30 L 80 90 L 100 70 L 120 130 L 140 110 L 160 170',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.026em',
        'pillar_slugs': ['artificial-intelligence'],
        'category_slugs': ['ai', 'artificial-intelligence'],
    },
    'health': {
        'index': 2, 'short': 'Physical',
        'title': 'Physical Health',
        'tagline': 'The body, its diseases, the medicine, and the institutions around them.',
        'note': 'The body is, properly understood, mostly other people’s problem. We report on disease, medicine, public policy, and the long argument about what the body owes the world.',
        'editor': 'Priya Shah',
        'accent_hex': '#2fbf7c',
        'curve': 'M 30 100 L 70 100 L 80 70 L 95 130 L 110 60 L 125 120 L 150 100 L 175 100',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.02em',
        'pillar_slugs': ['species-appropriate-diet', 'carnivore-diet', 'autoimmune', 'autoimmune-disease'],
        'category_slugs': ['health'],
        'subcategories': [
            {'id': 'autoimmune',     'name': 'Autoimmune Disease',     'short': 'Autoimmune',      'blurb': 'When the immune system mistakes home for elsewhere — lupus, MS, RA, and the long bench of the chronically misread.', 'accent': '#4cc995', 'match_slugs': ['autoimmune', 'autoimmune-disease'], 'illustration': _HEALTH_ILLUS['autoimmune']},
            {'id': 'heart-disease',  'name': 'Heart Disease',          'short': 'Heart',           'blurb': 'The most common killer in the developed world — and the most often misframed. Lipids, inflammation, and the metabolic argument.', 'accent': '#34a366', 'match_slugs': ['heart-disease'], 'illustration': _HEALTH_ILLUS['heart-disease']},
            {'id': 'diabetes',       'name': 'Diabetes',               'short': 'Diabetes',        'blurb': 'Type 1, type 2, type 1.5 — a family of metabolic diseases whose lines keep moving. The clinical and the dietary literature.', 'accent': '#5ecf86', 'match_slugs': ['diabetes', 'type-1-diabetes'], 'illustration': _HEALTH_ILLUS['diabetes']},
            {'id': 'weight',         'name': 'Weight',                 'short': 'Weight',          'blurb': 'Obesity, GLP-1 drugs, set-point theory, and the long contest over what makes a body store and shed.', 'accent': '#43b878', 'match_slugs': ['weight', 'obesity'], 'illustration': _HEALTH_ILLUS['weight']},
            {'id': 'alzheimers',     'name': 'Alzheimer’s Disease','short': 'Alzheimer’s','blurb': 'Amyloid, tau, ApoE, and the slow re-thinking of dementia as a disease of brain metabolism.', 'accent': '#9bdcb6', 'match_slugs': ['alzheimers', 'dementia'], 'illustration': _HEALTH_ILLUS['alzheimers']},
            {'id': 'liver-disease',  'name': 'Liver Disease',          'short': 'Liver',           'blurb': 'Fatty liver, fibrosis, and the silent organ that bears the brunt of modern eating.', 'accent': '#2a8a52', 'match_slugs': ['liver-disease'], 'illustration': _HEALTH_ILLUS['liver-disease']},
            {'id': 'kidney-disease', 'name': 'Kidney Disease',         'short': 'Kidney',          'blurb': 'Diabetic nephropathy, hypertension, and the slow strangling of the body’s filtration system.', 'accent': '#74d49d', 'match_slugs': ['kidney-disease'], 'illustration': _HEALTH_ILLUS['kidney-disease']},
            {'id': 'mishaps',        'name': 'Medical System Mishaps', 'short': 'Mishaps',         'blurb': 'When medicine gets it wrong — misdiagnosis, overtreatment, and the institutions that resist correction.', 'accent': '#86d3a6', 'match_slugs': ['medical-mishaps', 'mishaps'], 'illustration': _HEALTH_ILLUS['mishaps']},
        ],
    },
    'mental': {
        'index': 3, 'short': 'Mental',
        'title': 'Mental Health',
        'tagline': 'Depression, anxiety, trauma, therapy, psychiatry, and what we now know about caring for the mind.',
        'note': 'The mind is a long, patient instrument. We cover the clinical literature, the politics of care, and the slow craft of getting better — in whatever sense that turns out to mean.',
        'editor': 'Dr. Sela Hartmann',
        'accent_hex': '#5ba896',
        'curve': 'M 30 110 C 55 60, 80 60, 100 110 C 120 160, 145 160, 170 110 C 178 95, 178 90, 175 80',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.01em',
        'pillar_slugs': ['mental-health', 'physiological-origin', 'psychological-origin'],
        'category_slugs': ['mental'],
        'subcategories': [
            {'id': 'physiological-origin', 'name': 'Mental Illness · Physiological Origin', 'short': 'Physiological', 'blurb': 'The metabolic, inflammatory, and structural roots of mental illness — mitochondria, gut, sleep, hormones.', 'accent': '#7ec0b0', 'match_slugs': ['physiological-origin']},
            {'id': 'psychological-origin', 'name': 'Mental Illness · Psychological Origin', 'short': 'Psychological', 'blurb': 'Trauma, attachment, cognition, and what the clinical literature still calls the talking cure.', 'accent': '#3d8576', 'match_slugs': ['psychological-origin']},
        ],
    },
    'biology': {
        'index': 4, 'short': 'Biology',
        'title': 'Biology',
        'tagline': 'Cells, evolution, ecology, and biotechnology.',
        'note': 'Life keeps doing improbable things on long enough timescales. We follow cells, ecosystems, and the people doggedly watching them.',
        'editor': 'Mateo Reyes',
        'accent_hex': '#26c2c9',
        'curve': 'M 50 50 C 80 60, 90 110, 60 130 C 30 150, 80 170, 130 160 C 170 152, 165 130, 160 110',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.012em',
        'pillar_slugs': ['biology', 'cancer', 'cancer-metabolic-health', 'life-of-a-cell'],
        'category_slugs': ['biology'],
        'subcategories': [
            {'id': 'origin-of-cancer', 'name': 'Origin of Cancer', 'short': 'Cancer',        'blurb': 'The metabolic theory of cancer, the Warburg effect, and the slow re-thinking of oncology.', 'accent': '#5cd2d8', 'match_slugs': ['cancer', 'cancer-metabolic-health']},
            {'id': 'life-of-a-cell',   'name': 'Life of a Cell',   'short': 'Cells',         'blurb': 'Mitochondria, signalling, autophagy, and the small economies inside every body.', 'accent': '#1ea5ad', 'match_slugs': ['life-of-a-cell']},
        ],
    },
    'mindset': {
        'index': 5, 'short': 'Mindset',
        'title': 'Mindset',
        'tagline': 'Cognition, attention, and the inner life of the thinker.',
        'note': 'The inner life resists optimisation. We file dispatches from that resistance — the science of attention, the practice of slowness, the case for thinking on purpose.',
        'editor': 'Iris Kovac',
        'accent_hex': '#a387ff',
        'curve': 'M 60 30 C 130 60, 50 110, 130 130 C 80 150, 130 170, 90 185',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'italic',
        'type_tracking': '-0.008em',
        'pillar_slugs': ['mindset-success', 'mindset'],
        'category_slugs': ['mindset'],
    },
    'genetics': {
        'index': 6, 'short': 'Genetics',
        'title': 'Genetics',
        'tagline': 'Genomics, gene editing, CRISPR, heritability, and beyond.',
        'note': 'We can finally read what we used to guess at. Genomes, edits, ancestry, and the politics of the alphabet our cells were already using.',
        'editor': 'Dr. Adaeze Williams',
        'accent_hex': '#e0567a',
        'curve': 'M 70 30 C 110 50, 70 80, 110 100 C 70 120, 110 150, 80 180',
        'type_family': 'var(--font-sans)',
        'type_weight': '600',
        'type_style': 'normal',
        'type_tracking': '-0.032em',
        'pillar_slugs': ['genetics'],
        'category_slugs': ['genetics'],
        'subcategories': [
            {'id': 'origin-stories-of-dna',   'name': 'The Origin Stories of DNA',          'short': 'Origins',         'blurb': 'Mendel, Watson, Crick, and the long argument about what heredity actually is.', 'accent': '#ec7a96', 'match_slugs': ['origin-stories-of-dna']},
            {'id': 'dna-ai-future',           'name': 'DNA, AI, and the Future of Humanity','short': 'DNA · AI',   'blurb': 'CRISPR, polygenic prediction, and what we can do now that machines can read at scale.', 'accent': '#c43d62', 'match_slugs': ['dna-ai-future']},
        ],
    },
    'longevity': {
        'index': 7, 'short': 'Longevity',
        'title': 'Longevity',
        'tagline': 'Aging, senescence, and the long arithmetic of human time.',
        'note': 'The slowest field in biology, in a hurry. We cover the science of ageing and the strange new industries it has started.',
        'editor': 'Jonas Bremmer',
        'accent_hex': '#d4a23a',
        'curve': 'M 60 30 C 45 80, 50 140, 110 170 C 145 188, 165 175, 175 150',
        'type_family': 'var(--font-serif)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.008em',
        'pillar_slugs': ['longevity'],
        'category_slugs': ['longevity'],
        'subcategories': [
            {'id': 'supporting-biochemistry', 'name': 'Supporting Biochemistry', 'short': 'Biochemistry', 'blurb': 'NAD+, autophagy, mTOR, senolytics — the molecular knobs and what we know about turning them.', 'accent': '#e6b85e', 'match_slugs': ['supporting-biochemistry']},
            {'id': 'lifestyle',               'name': 'Lifestyle',              'short': 'Lifestyle',    'blurb': 'Sleep, exercise, fasting, sun. The boring interventions that actually have data behind them.',     'accent': '#b8861f', 'match_slugs': ['lifestyle']},
            {'id': 'longevity-research',      'name': 'Longevity Research',     'short': 'Research',     'blurb': 'The labs, the clinical trials, the strange new industries the field has started.',                'accent': '#c89530', 'match_slugs': ['longevity-research']},
        ],
    },
    'physics': {
        'index': 8, 'short': 'Physics',
        'title': 'Physics',
        'tagline': 'Cosmology, particles, condensed matter, and first principles.',
        'note': 'The interesting questions have moved out of the headlines. We follow them — into solid-state matter, the structure of the vacuum, and the patient instruments measuring both.',
        'editor': 'Hana Park',
        'accent_hex': '#6db4d8',
        'curve': 'M 40 110 C 60 60, 140 60, 170 110 C 150 170, 80 170, 50 130',
        'type_family': 'var(--font-sans)',
        'type_weight': '500',
        'type_style': 'normal',
        'type_tracking': '-0.022em',
        'pillar_slugs': ['physics'],
        'category_slugs': ['physics'],
    },
    'books': {
        'index': 9, 'short': 'Books',
        'title': 'Book Review',
        'tagline': 'Long reads on long books — fiction and nonfiction, considered slowly.',
        'note': 'The slow read deserves slow company. We review the books that matter — fiction, science, and the long, patient nonfiction that does not make the news.',
        'editor': 'Naomi Kessel',
        'accent_hex': '#b88a5c',
        'curve': 'M 100 30 C 60 50, 60 130, 60 170 M 100 30 C 140 50, 140 130, 140 170 M 60 170 C 80 175, 120 175, 140 170',
        'type_family': 'var(--font-serif)',
        'type_weight': '400',
        'type_style': 'normal',
        'type_tracking': '-0.01em',
        'pillar_slugs': [],
        'category_slugs': [],
        'is_books': True,  # rendered differently — sources from BookReview, not Article/Post
    },
}


def section_landing(request, key):
    from topics.models import Article
    config = SECTION_CONFIG.get(key)
    if not config:
        raise Http404('Unknown section')

    active_topic_id = request.GET.get('topic')
    # Make a shallow copy so we can attach 'count' without mutating SECTION_CONFIG
    subcategories = [dict(s) for s in config.get('subcategories', [])]
    active_topic = None
    if active_topic_id:
        for s in subcategories:
            if s['id'] == active_topic_id:
                active_topic = s
                break

    if config.get('is_books'):
        books = list(BookReview.objects.filter(published=True).select_related('category'))
        PINNED_FIRST = 'the-song-of-the-cell'
        books.sort(key=lambda b: b.slug != PINNED_FIRST)
        all_items = books
    else:
        articles = list(Article.objects.filter(
            published=True, pillar__slug__in=config['pillar_slugs']
        ).select_related('pillar'))
        posts = list(Post.objects.filter(
            published=True, category__slug__in=config['category_slugs']
        ).select_related('category'))
        all_items = articles + posts

    # Compute essay count per subcategory (always, regardless of filter)
    for s in subcategories:
        match = set(s.get('match_slugs', []))
        n = 0
        for it in all_items:
            slug = getattr(it.pillar, 'slug', None) if hasattr(it, 'pillar') and it.pillar else (
                getattr(it.category, 'slug', None) if hasattr(it, 'category') and it.category else None
            )
            if slug in match:
                n += 1
        s['count'] = n

    # Apply topic filter to displayed items
    if active_topic:
        match = set(active_topic.get('match_slugs', []))
        def _match(it):
            slug = getattr(it.pillar, 'slug', None) if hasattr(it, 'pillar') and it.pillar else (
                getattr(it.category, 'slug', None) if hasattr(it, 'category') and it.category else None
            )
            return slug in match
        items = [it for it in all_items if _match(it)]
    else:
        items = all_items

    item_count = len(items)
    hero_item = items[0] if items else None
    grid_items = items[1:11] if len(items) > 1 else []

    other_sections = [(k, v) for k, v in SECTION_CONFIG.items() if k != key]

    return render(request, 'blog/section_landing.html', {
        'key': key,
        'config': config,
        'subcategories': subcategories,
        'active_topic': active_topic,
        'hero_item': hero_item,
        'grid_items': grid_items,
        'item_count': item_count,
        'other_sections': other_sections,
    })


def home(request):
    from topics.models import Article
    all_published = Post.objects.filter(published=True)
    hero_post = all_published.filter(featured=True).first() or all_published.first()
    secondary_posts = list(all_published.exclude(id=hero_post.id)[:2]) if hero_post else []
    latest_posts = all_published[:4]
    popular_posts = all_published[:4]
    post_count = all_published.count()
    book_count = BookReview.objects.filter(published=True).count()
    currently_reading = BookReview.objects.filter(published=True, status='reading').first()
    featured_articles = Article.objects.filter(published=True).select_related('pillar')[:3]
    categories = Category.objects.all()

    # Health topics — articles from health-related pillars
    HEALTH_PILLARS = ['cancer', 'species-appropriate-diet', 'cancer-metabolic-health', 'carnivore-diet', 'autoimmune-disease', 'biology']
    health_articles = (
        Article.objects
        .filter(published=True, pillar__slug__in=HEALTH_PILLARS)
        .select_related('pillar')[:8]
    )
    health_count = Article.objects.filter(
        published=True, pillar__slug__in=HEALTH_PILLARS
    ).count()

    return render(request, 'blog/home.html', {
        'hero_post': hero_post,
        'secondary_posts': secondary_posts,
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        'post_count': post_count,
        'book_count': book_count,
        'featured_articles': featured_articles,
        'currently_reading': currently_reading,
        'categories': categories,
        'health_articles': health_articles,
        'health_count': health_count,
        'sections': SECTION_CONFIG,
    })


def about(request):
    from .models import Profile
    from topics.models import Article
    profile = Profile.objects.first()
    essays_this_year = Article.objects.filter(published=True).count() + Post.objects.filter(published=True).count()
    sections = SECTION_CONFIG  # for masthead
    return render(request, 'blog/about.html', {
        'profile': profile,
        'sections': sections,
        'essays_this_year': essays_this_year,
    })


def blog_list(request):
    from topics.models import Article
    from itertools import groupby

    selected = request.GET.get('section') or request.GET.get('category')
    selected_tag = request.GET.get('tag')

    posts = Post.objects.filter(published=True).select_related('category')
    articles = Article.objects.filter(published=True).select_related('pillar')

    if selected:
        cfg = SECTION_CONFIG.get(selected)
        if cfg:
            posts = posts.filter(category__slug__in=cfg['category_slugs'])
            articles = articles.filter(pillar__slug__in=cfg['pillar_slugs'])
        else:
            posts = posts.filter(category__slug=selected)
            articles = articles.none()

    if selected_tag:
        posts = posts.filter(tags__slug=selected_tag)
        articles = articles.none()

    # Combined timeline
    combined = []
    for p in posts:
        combined.append({
            'item': p, 'kind': 'post', 'date': p.created_at,
            'title': p.title, 'slug': p.slug,
            'category_slug': p.category.slug if p.category else None,
            'category_name': p.category.name if p.category else None,
            'reading_time': p.reading_time(),
            'url': f'/blog/{p.slug}/',
        })
    for a in articles:
        combined.append({
            'item': a, 'kind': 'article', 'date': a.created_at,
            'title': a.title, 'slug': a.slug,
            'category_slug': a.pillar.slug if a.pillar else None,
            'category_name': a.pillar.name if a.pillar else None,
            'reading_time': a.reading_time(),
            'url': f'/topics/{a.pillar.slug}/{a.slug}/' if a.pillar else None,
        })
    combined.sort(key=lambda x: x['date'], reverse=True)

    # Map every category slug → section accent (for the dots/pills)
    slug_to_section = {}
    for sec_key, sec in SECTION_CONFIG.items():
        for s in sec.get('pillar_slugs', []) + sec.get('category_slugs', []):
            slug_to_section[s] = (sec_key, sec)
    for entry in combined:
        s = entry.get('category_slug')
        if s and s in slug_to_section:
            entry['section_key'], entry['section'] = slug_to_section[s]

    # Group by month (e.g. "May 2026")
    def month_key(e):
        return e['date'].strftime('%B %Y')
    grouped = []
    for month, items in groupby(combined, key=month_key):
        grouped.append((month, list(items)))

    categories = Category.objects.all()
    tags = Tag.objects.filter(posts__published=True).distinct()

    return render(request, 'blog/blog_list.html', {
        'grouped_entries': grouped,
        'total_count': len(combined),
        'sections': SECTION_CONFIG,
        'selected': selected,
        'selected_tag': selected_tag,
        'categories': categories,
        'tags': tags,
    })


def _section_for_slug(slug):
    """Find the SECTION_CONFIG entry that owns a given category or pillar slug."""
    if not slug:
        return None, None
    for key, cfg in SECTION_CONFIG.items():
        if slug in cfg.get('category_slugs', []) or slug in cfg.get('pillar_slugs', []):
            return key, cfg
    return None, None


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    related = Post.objects.filter(
        category=post.category, published=True
    ).exclude(id=post.id)[:3]
    related_topics = post.related_articles.filter(published=True)
    comments = post.comments.filter(approved=True)
    comment_form = CommentForm()
    comment_submitted = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_submitted = True
            comment_form = CommentForm()

    section_key, section = _section_for_slug(post.category.slug if post.category else None)

    # See-also items — 3 most recent from other sections (variety)
    from topics.models import Article
    see_also_posts = list(Post.objects.filter(published=True).exclude(id=post.id).select_related('category')[:6])
    see_also_articles = list(Article.objects.filter(published=True).select_related('pillar')[:6])
    combined = []
    for p in see_also_posts:
        skey, _ = _section_for_slug(p.category.slug if p.category else None)
        combined.append({'title': p.title, 'url': f'/blog/{p.slug}/', 'section_key': skey, 'date': p.created_at, 'reading_time': p.reading_time()})
    for a in see_also_articles:
        skey, _ = _section_for_slug(a.pillar.slug if a.pillar else None)
        combined.append({'title': a.title, 'url': f'/topics/{a.pillar.slug}/{a.slug}/' if a.pillar else None, 'section_key': skey, 'date': a.created_at, 'reading_time': a.reading_time()})
    combined.sort(key=lambda x: x['date'], reverse=True)
    # Variety-weighted: try to take one per unique section first
    see_also = []
    seen_sections = set()
    for c in combined:
        if c['section_key'] not in seen_sections:
            see_also.append(c); seen_sections.add(c['section_key'])
        if len(see_also) >= 3: break
    if len(see_also) < 3:
        for c in combined:
            if c not in see_also:
                see_also.append(c)
            if len(see_also) >= 3: break
    # Attach section config
    for c in see_also:
        c['section'] = SECTION_CONFIG.get(c['section_key'])

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'section_key': section_key,
        'section': section,
        'see_also': see_also,
        'related': related,
        'related_topics': related_topics,
        'comments': comments,
        'comment_form': comment_form,
        'comment_submitted': comment_submitted,
        'comment_count': comments.count(),
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, published=True)
    categories = Category.objects.all()
    tags = Tag.objects.filter(posts__published=True).distinct()
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'selected': slug,
        'category': category,
    })


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'blog/projects.html', {'all_projects': all_projects})


def book_list(request):
    currently_reading = BookReview.objects.filter(published=True, status='reading')
    read = BookReview.objects.filter(published=True, status='read').select_related('category')
    wishlist = BookReview.objects.filter(published=True, status='wishlist')
    categories = Category.objects.filter(book_reviews__published=True).distinct()
    selected_cat = request.GET.get('category')
    if selected_cat:
        read = read.filter(category__slug=selected_cat)
    return render(request, 'blog/book_list.html', {
        'currently_reading': currently_reading,
        'read': read,
        'wishlist': wishlist,
        'book_categories': categories,
        'selected_book_cat': selected_cat,
    })


def book_detail(request, slug):
    book = get_object_or_404(BookReview, slug=slug, published=True)
    return render(request, 'blog/book_detail.html', {'book': book})


def search(request):
    from topics.models import Article
    query = request.GET.get('q', '').strip()
    post_results = []
    article_results = []
    if query:
        post_results = Post.objects.filter(published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query)
        )[:10]
        article_results = Article.objects.filter(published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query)
        )[:10]
    return render(request, 'blog/search_results.html', {
        'query': query,
        'post_results': post_results,
        'article_results': article_results,
    })


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'blog/subscribe_thanks.html')
            except Exception:
                pass
    return redirect('blog:home')
