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

FIG_ORIGIN = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-origin-streptomyces.svg" alt="Timeline showing Streptomyces avermitilis soil bacterium producing avermectin, chemically modified into ivermectin, culminating in the 2015 Nobel Prize" style="width:100%;border-radius:16px;display:block;">
</figure>"""

FIG_SELECTIVITY = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-parasite-selectivity.svg" alt="Side-by-side diagram of a parasite neuron with an open glutamate-gated chloride channel flooding with chloride ions, versus a mammalian neuron lacking that channel and protected by the blood-brain barrier" style="width:100%;border-radius:16px;display:block;">
</figure>"""

FIG_MITO = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-complex1-ampk-mtor.svg" alt="Diagram of a mitochondrion showing ivermectin blocking Complex I of the electron transport chain, ATP falling, AMPK activating, and mTOR being suppressed, leading to growth arrest" style="width:100%;border-radius:16px;display:block;">
</figure>"""

FIG_APOPTOSIS = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-cancer-apoptosis.svg" alt="Cancer cell diagram showing collapsing membrane potential, rising reactive oxygen species, and the cell entering intrinsic apoptosis" style="width:100%;border-radius:16px;display:block;">
</figure>"""

FIG_INFLAMMATION = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-nfkb-inflammation.svg" alt="Cell diagram showing ivermectin blocking NF-kB from entering the nucleus, reducing cytokine production, reinforced by AMPK activation" style="width:100%;border-radius:16px;display:block;">
</figure>"""

FIG_METABOLISM = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-fxr-insulin-glucose.svg" alt="Diagram of ivermectin binding the FXR bile-acid receptor in the liver and gut, lowering fasting glucose, improving insulin sensitivity, and reducing fat cell differentiation" style="width:100%;border-radius:16px;display:block;">
</figure>"""

ARTICLE = {
    "title": "What Ivermectin Actually Does Inside Your Cells",
    "slug": "ivermectin-mitochondria-cancer-metabolism",
    "summary": (
        "Originally isolated from a soil bacterium and Nobel Prize-winning as an antiparasitic, "
        "ivermectin also inhibits mitochondrial Complex I — a mechanism tied to AMPK activation, "
        "cancer cell apoptosis, reduced inflammation, and improved glucose and insulin metabolism."
    ),
    "order": 1,
    "published": True,
    "content": f"""{FIG_ORIGIN}

<p>Ivermectin is usually introduced to the public as a livestock dewormer, and dismissed just as quickly. That framing skips over the fact that it is a Nobel Prize-winning medicine with more than three decades of safe use in hundreds of millions of people, and a growing body of peer-reviewed research into effects far beyond parasites — reaching into mitochondria, cancer metabolism, inflammation, and glucose regulation.</p>

<h2>Where Ivermectin Comes From</h2>
<p>The story starts in a patch of soil in Japan in 1975, where a bacterium called <em>Streptomyces avermitilis</em> was isolated and cultured. That bacterium produced a compound named avermectin, which turned out to have extraordinarily effective anti-parasitic properties. Avermectin was then chemically modified into a more potent derivative — ivermectin.</p>
<p>The discovery was significant enough to earn the 2015 Nobel Prize in Physiology or Medicine, the Nobel committee's first award for an infectious-disease treatment in over six decades, recognized specifically for radically lowering the incidence of parasitic diseases like river blindness and lymphatic filariasis. In 2014 alone, the World Health Organization reported reaching 139 million people with ivermectin through its lymphatic filariasis elimination program. It remains on the WHO's list of essential medicines and is FDA-approved for human use, with several U.S. states recently allowing it to be sold over the counter.</p>

{FIG_SELECTIVITY}

<h2>How It Kills Parasites — and Why It Leaves Mammals Alone</h2>
<p>Ivermectin's classical mechanism involves binding to glutamate-gated chloride channels found in invertebrate parasites. When it binds, it forces those channels open and keeps them open, flooding the parasite's cells with chloride ions. That paralyzes the parasite's nervous and muscular systems, killing it.</p>
<p>The reason this is safe in mammals is straightforward: those specific chloride channels are essentially absent in our nervous system, and a functioning blood-brain barrier keeps ivermectin from accumulating in the brain under normal conditions anyway. That combination gives the drug a wide therapeutic window against parasites — but it also isn't the whole story. Over the past two decades, research has found that ivermectin interacts with several mammalian cellular targets too, which is where its metabolic effects begin.</p>

{FIG_MITO}

<h2>What It Does to Mitochondria: Complex I, AMPK, and mTOR</h2>
<p>Cancer cells often depend on altered mitochondrial function to fuel rapid growth and proliferation, which means disrupting that already-altered function can be selectively lethal to them. Multiple peer-reviewed studies have found that ivermectin inhibits mitochondrial Complex I — the first and largest enzyme complex in the electron transport chain, and the entry point where NADH feeds electrons into the system that produces ATP.</p>
<p>When Complex I is inhibited, the electron transport chain stalls. In glioblastoma cells, this produces a dose-dependent drop in oxygen consumption and respiratory capacity, a decline in mitochondrial membrane potential, and a rise in reactive oxygen species and mitochondrial superoxide — a state of significant mitochondrial dysfunction. Because cancer cells have unusually high metabolic demand, they are disproportionately sensitive to this kind of disruption compared to normal cells: studies comparing leukemia cells to normal bone marrow, and kidney cancer cells to normal kidney tissue, both found the cancerous cells substantially more affected.</p>
<p>As ATP falls, cells experience an energy crisis that activates AMPK (AMP-activated protein kinase) — the cell's energy sensor, which switches on when the ratio of AMP to ATP rises. Once active, AMPK suppresses mTOR, a major driver of cancer cell growth and proliferation. The sequence runs: Complex I slows → ATP drops → AMPK activates → mTOR is suppressed → cancer cells are pushed toward growth arrest.</p>

{FIG_APOPTOSIS}

<h2>A Death Signal From Inside the Cancer Cell</h2>
<p>There's a second dimension to the mitochondrial story. When the membrane potential collapses following Complex I inhibition, it can trigger intrinsic apoptosis — programmed cell death initiated from within the cell rather than by an external signal. This exact sequence, membrane potential collapse followed by rising reactive oxygen species and a shift toward pro-apoptotic signaling, has been documented in studies of cervical cancer, esophageal carcinoma, leukemia, and glioblastoma.</p>
<p>Two additional mechanisms reinforce this anti-cancer picture. First, ivermectin promotes the degradation of PAK1, a kinase overactive in most human cancers — notably, one study found it reduced PAK1 only in cancerous breast cells, not in non-tumorigenic ones, echoing the same selectivity seen with parasites. Second, in pancreatic cancer — a notoriously treatment-resistant disease — one study found that combining ivermectin with the chemotherapy drug gemcitabine produced significantly more cancer cell death than gemcitabine alone, through the same oxidative-stress route from mitochondrial disruption, and suppressed tumor growth in living models.</p>

{FIG_INFLAMMATION}

<h2>Turning Down the Inflammatory Signal</h2>
<p>Chronic low-grade inflammation is a major driver of cardiometabolic disease and insulin resistance, so any compound that meaningfully modulates it is metabolically relevant. Multiple studies show ivermectin suppresses activation of NF-κB, the master transcription factor that drives production of pro-inflammatory cytokines — blocking its entry into the cell nucleus and reducing the downstream cytokine response.</p>
<p>In animal studies, ivermectin reduced inflammatory markers and significantly improved survival after a lethal dose of lipopolysaccharide (a bacterial molecule that triggers a sepsis-like inflammatory cascade). In allergic-asthma models, therapeutic doses reduced immune cell recruitment into the airway, lowered circulating cytokine levels, and suppressed IgE production. AMPK — the same energy sensor activated via Complex I inhibition — is itself a potent suppressor of NF-κB, which means the mitochondrial, anti-cancer, and anti-inflammatory effects may be more unified than they first appear.</p>

{FIG_METABOLISM}

<h2>The Glucose and Insulin Connection</h2>
<p>The most surprising thread in ivermectin's expanding story may be its influence on insulin resistance and glucose metabolism. Ivermectin binds FXR (the farnesoid X receptor), a nuclear hormone receptor expressed in the liver, intestine, kidneys, and adrenal glands, sometimes called the bile-acid receptor because of its established role in bile-acid signaling — a role already known to regulate glucose homeostasis and insulin sensitivity.</p>
<p>In a preclinical model of diet-induced obesity, mice treated with ivermectin showed reduced fasting glucose and fasting insulin compared to controls. A follow-up rat study using a high-fat, high-carbohydrate diet found ivermectin prevented the rise in fasting blood glucose, improved glucose tolerance test results, reduced blood pressure, and improved liver enzyme markers — leading the study authors to describe ivermectin as a promising candidate for combating metabolic syndrome. In cultured fat cells, ivermectin inhibited the differentiation of pre-adipocytes into mature fat cells and reduced triglyceride accumulation, an effect mediated through the PPAR-gamma pathway. Once again, AMPK activation and NF-κB suppression both plausibly contribute — AMPK directly improves insulin signaling and glucose uptake, while lower inflammation removes one of the known drivers of insulin resistance.</p>
<p>This mechanistic profile — Complex I engagement, AMPK activation, NF-κB suppression, improved insulin signaling — closely parallels metformin, the world's most widely prescribed insulin-sensitizing medication. The human evidence for ivermectin is far more preliminary than for metformin: one published report described four type 2 diabetics whose HbA1c improved with daily ivermectin over several months to a couple of years, but there have been no large-scale clinical trials of ivermectin's effects on insulin resistance or glycemic control.</p>

<h2>What This Does and Doesn't Mean</h2>
<p>Nearly all of the cancer and metabolic evidence described here comes from cell and animal studies, not large human trials. None of it means ivermectin is a cure for cancer or any metabolic condition — it might turn out to matter clinically, or it might not. What the evidence does show is a molecule with a coherent, underexplored mechanistic story spanning mitochondria, cancer metabolism, inflammation, and glucose regulation, built on a drug with an already well-established safety record at standard human therapeutic doses. That combination is what makes further rigorous, large-scale human research worth pursuing — not a reason to self-treat based on preclinical findings.</p>

<p><em>Based on Dr. Ben Bikman's Metabolic Classroom, lecture 142, "Ivermectin Explained: The Science Behind the Controversy."</em></p>
""",
}


class Command(BaseCommand):
    help = "Load the Bikman ivermectin mitochondria/cancer/metabolism article into the Cancer pillar"

    def handle(self, *args, **options):
        pillar, created = Pillar.objects.get_or_create(
            slug=PILLAR["slug"],
            defaults=PILLAR,
        )
        if not created:
            for k, v in PILLAR.items():
                setattr(pillar, k, v)
            pillar.save()
        action = "Created" if created else "Updated"
        self.stdout.write(f"{action} pillar: {pillar.name}")

        article, created = Article.objects.get_or_create(
            slug=ARTICLE["slug"],
            defaults={**ARTICLE, "pillar": pillar},
        )
        if not created:
            # Do NOT overwrite `content` on repeat runs — preserves manual edits.
            for k, v in ARTICLE.items():
                if k == "content":
                    continue
                setattr(article, k, v)
            article.pillar = pillar
            article.save()
        action = "Created" if created else "Updated (content preserved)"
        self.stdout.write(f"{action} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
