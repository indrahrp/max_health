from django.core.management.base import BaseCommand

SLUG = 'lipoprotein-cascade-vldl-ldl-apob'
TITLE = 'From VLDL to LDL: How Your Liver Packages, Transforms, and Clears Fat in Your Blood'
SUMMARY = (
    'Your blood cannot dissolve fat — so the liver wraps it in protein shells called lipoproteins. '
    'VLDL leaves the liver loaded with triglycerides, gradually shrinks into IDL and then LDL as '
    'fuel is offloaded to tissues, and finally docks onto LDL receptors to be cleared. '
    'ApoB marks the particle itself; cholesterol is just the cargo inside. '
    'Understanding the difference changes how you read a lipid panel.'
)

CONTENT = '''<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/lipoprotein-cascade.svg" alt="Animated diagram showing the lipoprotein cascade: liver produces VLDL, which sheds triglycerides via LPL to become IDL then LDL, which binds the LDL receptor. Bottom panels show ApoB as particle count vs cholesterol as cargo." style="width:100%;border-radius:16px;display:block;">
</figure>

<p>Fat cannot dissolve in water, and blood is mostly water. The body solves this with a clever workaround: it wraps fat in a protein shell that <em>can</em> travel through the bloodstream. These protein-wrapped fat carriers are called lipoproteins, and the journey from liver to tissue and back again — from VLDL to IDL to LDL — is one of the most important biochemical processes in metabolic health.</p>

<h2>Why lipoproteins exist</h2>

<p>When you eat fat, or when the liver makes fat from carbohydrates, that fat needs to reach tissues that need it: muscle cells that will burn it for fuel, adipose tissue that will store it, cells that will use it to make hormones. None of this is possible without packaging. The lipoprotein is the packaging: a spherical particle with a protein coat on the outside and a fat payload on the inside.</p>

<p>The proteins on the outside — called apolipoproteins — do more than just hold the particle together. They act as molecular ID tags and communication signals, telling receptors on different cells what the particle is carrying, where it came from, and whether it should be taken up.</p>

<h2>VLDL: what the liver releases</h2>

<p>The liver produces VLDL — Very Low Density Lipoprotein. It is large, buoyant, and packed mostly with triglycerides (TG), which are the storage form of fatty acids. The liver makes VLDL either from dietary fat arriving from the gut or from fat it has synthesised itself — a process called <em>de novo lipogenesis</em>, which ramps up on high-carbohydrate diets.</p>

<p>VLDL carries one molecule of a protein called <strong>ApoB-100</strong> on its surface. This is the key structural protein — the particle cannot exist without it. Every VLDL particle has exactly one ApoB-100.</p>

<p>VLDL also carries ApoC-II and ApoE on its surface, which it will use later. ApoC-II activates an enzyme called lipoprotein lipase (LPL) at the walls of blood vessels, and ApoE signals to liver receptors for partial clearance of IDL.</p>

<h2>LPL and the transformation: VLDL → IDL → LDL</h2>

<p>As VLDL circulates through capillaries in muscle and fat tissue, LPL on the capillary walls cleaves the triglycerides out of the particle, releasing free fatty acids for the cells to use as fuel or to store. As the triglycerides are stripped away, the particle shrinks and becomes denser — because density is the ratio of protein to fat, and now there is less fat.</p>

<p>The intermediate particle — IDL, or Intermediate Density Lipoprotein — is VLDL that has lost much of its triglyceride cargo but still retains a substantial amount. IDL has two fates: it can be taken up by the liver directly (via ApoE binding to liver receptors), or it can continue to be processed by LPL and hepatic lipase until it becomes LDL.</p>

<p>LDL — Low Density Lipoprotein — is the end result of this stripping process. It has lost almost all of its triglycerides. What remains is a small, dense particle carrying mostly cholesterol — specifically cholesterol esters — with its one ApoB-100 still on the surface. LDL is the primary cholesterol delivery vehicle in circulation.</p>

<h2>How the liver clears LDL</h2>

<p>LDL is cleared from the bloodstream primarily by <strong>LDL receptors</strong> — proteins embedded in the surface of liver cells (and other cells). The LDL receptor binds to the ApoB-100 protein on the surface of the LDL particle. Once bound, the entire particle is pulled inside the cell through a process called <em>receptor-mediated endocytosis</em>.</p>

<p>Inside the cell, the LDL particle is broken down in a lysosome. The cholesterol is released and used by the cell — for membrane building, hormone synthesis (cortisol, sex hormones), or bile acid production. The LDL receptor itself is recycled back to the cell surface to bind more LDL particles.</p>

<p>The number of LDL receptors on liver cells is a key control mechanism: when cells have enough cholesterol, they reduce LDL receptor expression, leaving more LDL in circulation. When cholesterol is needed, receptor expression increases and LDL clearance accelerates. Statins work partly by upregulating LDL receptor expression, increasing the liver's rate of LDL clearance.</p>

<h2>HDL and ApoA-1: the reverse route</h2>

<p>HDL — High Density Lipoprotein — travels in the opposite direction. It is small and dense, with a protein called <strong>ApoA-1</strong> on its surface instead of ApoB-100. HDL scavenges excess cholesterol from peripheral tissues and arterial walls and returns it to the liver for disposal — a process called reverse cholesterol transport.</p>

<p>The key distinction: ApoB-containing particles (VLDL, IDL, LDL) deliver cholesterol and fat <em>to</em> tissues. ApoA-1-containing particles (HDL) collect cholesterol <em>from</em> tissues and return it to the liver. This is why high HDL and low LDL are generally associated with lower cardiovascular risk — you want more retrieval and less accumulation.</p>

<h2>The ApoB versus cholesterol distinction</h2>

<p>This is the point that Dave Feldman and a growing number of lipidologists emphasise: <strong>the standard LDL-cholesterol test measures the amount of cholesterol inside LDL particles — not the number of particles.</strong></p>

<p>Think of it this way. If you measure how many people are on a bus, you are counting passengers — the cargo. If you count the buses themselves, you are counting vehicles. ApoB counts the vehicles. LDL-C counts the passengers.</p>

<p>Why does this matter? Because you can have a high LDL-C with relatively few particles (large, buoyant LDL particles, each carrying more cholesterol), or a lower LDL-C with many more particles (small, dense LDL, each carrying less cholesterol). The number of particles circulating — measured directly by ApoB — is thought to be a stronger predictor of cardiovascular risk than the cholesterol content, because it is the particles, not the cholesterol inside them, that can get lodged in arterial walls.</p>

<p>ApoB is a direct particle count: every VLDL, IDL, and LDL particle carries exactly one ApoB-100. So measuring serum ApoB gives you the total number of atherogenic particles in circulation. LDL-C, by contrast, is an estimate of cholesterol content — calculated rather than measured directly in most labs — and gives no information about particle number.</p>

<h2>Triglycerides complete the picture</h2>

<p>Triglycerides in the blood reflect how much VLDL is circulating — and how effectively the liver and LPL are clearing it. High fasting triglycerides generally mean the liver is producing more VLDL than LPL can clear, or that LPL activity is impaired. This is commonly driven by excess carbohydrate intake, insulin resistance, or both.</p>

<p>High triglycerides also tend to correlate with small dense LDL, because when triglyceride levels are elevated, cholesteryl ester transfer protein (CETP) swaps triglycerides into LDL particles in exchange for cholesterol esters — making LDL particles more TG-rich, then depleted back to small, dense particles after the TG is removed. So elevated triglycerides are not just a standalone finding: they signal that the whole lipoprotein system is under metabolic stress.</p>

<h2>Reading a lipid panel differently</h2>

<p>A standard lipid panel gives you: total cholesterol, LDL-C (usually calculated), HDL-C, and triglycerides. This tells you something, but it misses particle count. A more complete picture includes:</p>

<ul>
<li><strong>ApoB</strong> — directly counts all atherogenic particles (VLDL + IDL + LDL)</li>
<li><strong>ApoA-1</strong> — counts HDL particles (reverse transport capacity)</li>
<li><strong>Triglycerides</strong> — proxy for VLDL burden and insulin sensitivity</li>
<li><strong>Fasting insulin or HOMA-IR</strong> — metabolic context for why VLDL may be elevated</li>
</ul>

<p>The ApoB-to-ApoA-1 ratio captures the balance between particle delivery and retrieval — more particles arriving (ApoB) relative to retrieval (ApoA-1) is a higher-risk profile than the reverse.</p>

<p>Understanding the lipoprotein cascade does not just make a blood test easier to interpret. It makes clear that the question is not simply "how much cholesterol is in my blood" but "how many particles are circulating, what are they carrying, and is the system clearing them efficiently." The particle is the vessel. The cholesterol is the cargo. Counting cargo without counting vessels gives you an incomplete map.</p>'''


def create_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Pillar = apps.get_model('topics', 'Pillar')

    pillar = Pillar.objects.filter(slug='carnivore-diet').first()
    if not pillar:
        return
    if Article.objects.filter(slug=SLUG).exists():
        return

    Article.objects.create(
        slug=SLUG,
        title=TITLE,
        summary=SUMMARY,
        content=CONTENT,
        pillar=pillar,
        order=50,
        published=True,
    )


def reverse_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug=SLUG).delete()


class Command(BaseCommand):
    help = 'Load lipoprotein cascade article'

    def handle(self, *args, **options):
        from topics.models import Article, Pillar
        pillar = Pillar.objects.filter(slug='carnivore-diet').first()
        if not pillar:
            self.stderr.write('carnivore-diet pillar not found')
            return
        if Article.objects.filter(slug=SLUG).exists():
            self.stdout.write('Article already exists')
            return
        Article.objects.create(
            slug=SLUG, title=TITLE, summary=SUMMARY,
            content=CONTENT, pillar=pillar, order=50, published=True,
        )
        self.stdout.write(self.style.SUCCESS(f'Created: {SLUG}'))
