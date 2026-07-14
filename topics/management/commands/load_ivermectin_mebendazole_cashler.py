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

FIG_BENEFIT = """<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/ivermectin-mebendazole-clinical-benefit.svg" alt="Diagram of a compounded daily capsule combining ivermectin 25mg and mebendazole 250mg, next to a bar showing the 6-month outcome breakdown: 32.8% no evidence of disease, 15.6% regression, 36.1% stable, 15.6% progressed" style="width:100%;border-radius:16px;display:block;">
</figure>"""

ARTICLE = {
    "title": "Ivermectin and Mebendazole in Cancer: A 197-Patient Real-World Study",
    "slug": "ivermectin-mebendazole-cancer-clinical-benefit",
    "summary": (
        "A prospective observational cohort of 197 cancer patients taking daily ivermectin 25mg "
        "and mebendazole 250mg for 90 days reported an 84.4% clinical benefit ratio at six months, "
        "with no significant dose-response relationship observed."
    ),
    "order": 3,
    "published": True,
    "content": f"""{FIG_BENEFIT}

<p>A new paper — "Real-World Clinical Outcomes of Ivermectin and Mebendazole in Cancer Patients: Results from a Prospective Observational Cohort," led by Nick Cashler — reports an 84.4% clinical benefit ratio in cancer patients taking the two drugs together. It has not yet been through full peer review. Dr. John Campbell covered the paper's findings in detail; this article follows his account of it.</p>

<h2>Study Design</h2>
<p>This was a prospective observational cohort study, meaning patients were enrolled and then followed forward in time as data was collected, rather than being assigned to a treatment arm in a randomized trial. It is not a randomized controlled trial.</p>
<p>197 cancer patients were prescribed ivermectin and mebendazole off-label — described as "compassionate prescribing" — through telemedicine by registered US providers. Participants received compounded oral capsules combining both drugs. Data were collected through voluntary standardized digital surveys at baseline and at approximately six months of follow-up.</p>
<p>Of the 197 baseline participants, 122 completed the six-month follow-up, a 61.9% response rate. Mean age was 67, and the cohort was roughly half male and half female. The most common cancer type was prostate, followed by breast, lung, colon, and liver cancer, along with a range of other cancer types. Median time since initial diagnosis was 1.2 years. At baseline, 37.1% of patients had active disease progression (metastasis).</p>

<h2>The Dosage Protocol</h2>
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
<table>
<thead><tr><th>Component</th><th>Dose</th><th>Frequency</th><th>Duration</th></tr></thead>
<tbody>
<tr><td>Ivermectin</td><td>25 mg</td><td>Once daily</td><td>90 days</td></tr>
<tr><td>Mebendazole</td><td>250 mg</td><td>Once daily</td><td>90 days</td></tr>
</tbody>
</table>
</div>
<p>Both drugs were combined into a single compounded capsule taken once a day for 90 days. Nearly 87% of patients adhered to the full course, taking all 90 capsules.</p>

<h2>Results at Six Months</h2>
<p>The paper's central measure is the clinical benefit ratio — a standard cancer-treatment outcome measure combining complete response, partial response, and disease stability. Among the 122 patients who completed follow-up, the clinical benefit ratio was 84.4%, broken down as:</p>
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
<table>
<thead><tr><th>Outcome</th><th>Share of cohort</th></tr></thead>
<tbody>
<tr><td>No current evidence of disease</td><td>32.8%</td></tr>
<tr><td>Tumor regression</td><td>15.6%</td></tr>
<tr><td>Stable disease</td><td>36.1%</td></tr>
<tr><td>Disease progression</td><td>15.6%</td></tr>
</tbody>
</table>
</div>
<p>Nearly 87% of the cohort was stable or improving at six months, and just 15.6% progressed — notable given that, left untreated, cancer is by definition a progressive disease.</p>

<h2>No Clear Dose-Response Relationship</h2>
<p>The paper reports that no significant dose-response association was observed for cancer outcomes, with only a 9% probability of that finding being due to chance (91% confidence). Patients on lower doses did about as well as patients on higher doses. The single best response came from patients taking two capsules a day, but the difference from the standard one-capsule dose was small. The paper describes this as encouraging that lower doses may be effective, though it does not establish a lower bound.</p>

<h2>Safety and Tolerability</h2>
<p>Side effects were reported as mild, mostly gastrointestinal. Nearly 94% of patients who experienced side effects were able to continue treatment, with some dose adjustments. Ivermectin has separately demonstrated a strong safety record in cancer patients, including those undergoing chemotherapy concurrently.</p>

<h2>Concurrent Conventional Treatment</h2>
<p>Patients in the cohort were not using ivermectin and mebendazole in isolation from conventional care. Among participants, 27.9% were also receiving chemotherapy, 21.3% radiotherapy, and 19.7% underwent surgery during the six-month period. Close to half were also taking dietary supplements, and just over a third made dietary modifications.</p>

<h2>Cost</h2>
<p>The paper notes that standard chemotherapy regimens average roughly $111,000 per patient per year. By comparison, it estimates the ivermectin-mebendazole protocol at approximately $1,200 per year — both drugs are generic and inexpensive to produce.</p>

<h2>Proposed Mechanisms</h2>
<p>Ivermectin and mebendazole are antiparasitic drugs, but the paper is explicit that any anti-cancer effect is not attributed to killing parasites — cancer is not a parasitic disease. Instead, it points to separate, multi-target biochemical mechanisms for each drug:</p>
<p><strong>Ivermectin</strong> has been shown to exert more than 14 distinct anti-cancer mechanisms across 12 cancer types, including inhibiting cancer cell proliferation, reducing metastasis, inhibiting angiogenesis (new blood vessel growth that tumors need to grow beyond a small size), reducing mitochondrial function in cancer cells, and selectively targeting cancer stem cells.</p>
<p><strong>Mebendazole</strong> (a close relative of fenbendazole, and its human-approved form) works primarily through microtubule disruption, which blocks the spindle formation cancer cells need to separate their chromosomes during division — arresting the cell cycle. It has also been linked to induction of apoptosis (programmed cell death), significant inhibition of tumor growth, inhibition of angiogenesis, and disruption of glucose uptake in cancer cells.</p>
<p>Used together, the paper describes the two drugs as targeting nonoverlapping pathways, producing synergistic tumor regression rather than simply additive effects. Both drugs are described as well bio-distributed throughout body tissues (with the central nervous system noted as a possible exception), and the combination has been linked in prior in vivo and in vitro models to reduced cancer stem cell populations and reversal of multidrug resistance — attacking cancer cells through enough distinct mechanisms simultaneously that resistance to all of them at once becomes harder to develop.</p>

<h2>Limitations, in the Paper's Own Words</h2>
<p>The study's conclusion states that the combination "was associated with high rates of self-reported clinical benefit, with nearly half of participants reporting tumor regression or no current evidence of disease," across a heterogeneous population of cancer patients. But the authors are explicit about the limitations: this was an observational design relying on self-reported outcomes, with potential for selection bias and uncontrolled confounding variables. The paper describes its own findings as "hypothesis generating" rather than confirmatory, and calls for further validation to define an optimal dosing strategy.</p>

<p><em>Based on Dr. John Campbell's video covering the paper "Real-World Clinical Outcomes of Ivermectin and Mebendazole in Cancer Patients: Results from a Prospective Observational Cohort," led by Nick Cashler. Not yet peer-reviewed. Not medical advice.</em></p>
""",
}


class Command(BaseCommand):
    help = "Load the Cashler ivermectin+mebendazole 197-patient cancer cohort article into the Cancer pillar"

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
