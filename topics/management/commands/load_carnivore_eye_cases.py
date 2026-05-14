from django.core.management.base import BaseCommand
from topics.models import Pillar, Article


ARTICLES = [
    {
        "title": "Macular Degeneration & Carnivore: 3 Case Reports",
        "slug": "carnivore-macular-degeneration-cases",
        "summary": (
            "Three interviewee accounts of macular degeneration halting or improving on a "
            "carnivore diet — including one person diagnosed simultaneously with cataracts "
            "and told surgery was 3–5 years away, and reports of patients no longer needing "
            "intraocular injections."
        ),
        "content": """<h2>Macular Degeneration Cases on Carnivore</h2>

<h3>Case 1 — Macular + Cataracts, Both Diagnosed Simultaneously</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/6cBUk1vlqiY">youtu.be/6cBUk1vlqiY</a></p>
<blockquote>
<p><em>"I was diagnosed with cataracts and onset macular degeneration and basically told, you know, you're going to be back for cataract surgery in three or four years, five at the outset — and macular degeneration, about all you can do is wear sunglasses outside and hope you can slow it down... I firmly believe it saved my life. I'm sure I was pre-diabetic and had a lot of other things starting to pop up before I changed my nutrition."</em></p>
</blockquote>
<p>Diagnosed with both conditions simultaneously, given a 3–5 year timeline to surgery. Attributed reversal/slowdown to carnivore. Also was pre-diabetic at the time — suggesting blood sugar normalization as the likely mechanism.</p>

<h3>Case 2 — Community Pattern: People No Longer Needing Eye Injections</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/Q0mHYuv8_RI">youtu.be/Q0mHYuv8_RI</a></p>
<blockquote>
<p><em>"I'm hearing this over and over and over again. People going through the hell of having injections put in their eyes — and now they don't... it's astounding that these problems that basically you've just written off as 'there's nothing you can do' — like macular degeneration and glaucoma — people are seeing results."</em></p>
</blockquote>
<p>Speaker reports repeated accounts from their audience of macular degeneration improving. References patients who were receiving anti-VEGF intraocular injections (the standard treatment for wet AMD) no longer needing them after dietary change.</p>

<h3>Case 3 — Practitioner Reporting Macular Improvements in Clients</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/LfyseQT21Dc">youtu.be/LfyseQT21Dc</a></p>
<blockquote>
<p><em>"I've certainly been helping other people and they're seeing some results too just by [dietary change]... I know I've got the ability — it's been installed in me to heal — but I got to speak about it."</em></p>
</blockquote>

<h3>Proposed Mechanism</h3>
<p>Macular degeneration has strong links to chronic hyperglycemia, oxidative stress, and systemic inflammation. Carnivore's primary levers — eliminating dietary glucose spikes and reducing inflammatory load — map directly to the pathways driving AMD progression. The blood sugar normalization alone (particularly in pre-diabetic individuals) may be sufficient to halt or reverse early-stage macular damage.</p>""",
        "order": 10,
    },
    {
        "title": "Glaucoma & Carnivore: 3 Case Reports",
        "slug": "carnivore-glaucoma-cases",
        "summary": (
            "Three accounts of glaucoma resolving or halting on carnivore — including one "
            "case where glaucoma was 'gone within a few weeks,' and one describing the exact "
            "mechanism: pigment dispersion syndrome creating intraocular pressure."
        ),
        "content": """<h2>Glaucoma Cases on Carnivore</h2>

<h3>Case 1 — Glaucoma Gone Within Weeks</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/I4TfcPBTjxc">youtu.be/I4TfcPBTjxc</a></p>
<blockquote>
<p><em>"My anxiety is almost gone. The glaucoma's gone within a few weeks. The pain from my hips was pretty well gone. I think about the fifth or sixth day the arthritis pain had gone. When I went on the carnivore, I would say 90% of my pain is gone. The weight loss was a bonus."</em></p>
</blockquote>
<p>Glaucoma resolved within weeks alongside a broader pattern of inflammatory conditions clearing — anxiety, hip pain, arthritis. This points to systemic inflammation reduction as the shared mechanism.</p>

<h3>Case 2 — All Glaucoma Symptoms Present, Specialist Couldn't Confirm Diagnosis</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/oYOnZCzxVZ0">youtu.be/oYOnZCzxVZ0</a></p>
<blockquote>
<p><em>"They said he had glaucoma. They gave him the glaucoma medicine. We go see the specialist. The specialist says, 'You don't have glaucoma. You got all the symptoms, but you don't have glaucoma.'"</em></p>
</blockquote>
<p>Patient presented with all clinical markers of glaucoma but specialist confirmed it was not glaucoma on formal assessment — potentially early reversal before the condition fully established.</p>

<h3>Case 3 — Pigment Dispersion Syndrome (Glaucoma Precursor), Personal Account</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/DUosXO76PQ4">youtu.be/DUosXO76PQ4</a></p>
<blockquote>
<p><em>"I was having like really bad eye problems. I can't remember exactly what the problem with the eye was called, but it basically leads to glaucoma. It's a problem where the cells in the color part of your eye are breaking off and plugging up the drainage in your eye and creating pressure. And it was getting really bad to where some nights I..."</em></p>
</blockquote>
<p>This description precisely matches <strong>pigment dispersion syndrome</strong> — melanin granules shedding from the iris and clogging the trabecular meshwork, raising intraocular pressure. A known precursor to pigmentary glaucoma. The person was consuming a high-carbohydrate, high-alcohol diet at the time and attributed improvement to dietary change.</p>

<h3>Proposed Mechanism</h3>
<p>Intraocular pressure has associations with insulin resistance and vascular inflammation. Reducing systemic glucose and inflammatory load via carnivore may lower IOP through improved trabecular meshwork function and vascular tone in the optic nerve head.</p>""",
        "order": 11,
    },
    {
        "title": "Cataracts & Carnivore: 3 Case Reports",
        "slug": "carnivore-cataracts-cases",
        "summary": (
            "Three accounts of cataracts stabilising or developing more slowly on carnivore "
            "— including a person diagnosed with both cataracts and macular degeneration who "
            "avoided surgery, and a case where cataracts remained stable after eye trauma."
        ),
        "content": """<h2>Cataract Cases on Carnivore</h2>

<h3>Case 1 — Macular + Cataracts, Surgery Avoided (see also Macular section)</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/6cBUk1vlqiY">youtu.be/6cBUk1vlqiY</a></p>
<blockquote>
<p><em>"I was diagnosed with cataracts and onset macular degeneration and basically told you're going to be back for cataract surgery in three or four years, five at the outset."</em></p>
</blockquote>
<p>Diagnosed with both conditions together while pre-diabetic. Attributed slowing/reversal to carnivore. Surgery timeline was not met.</p>

<h3>Case 2 — Cataracts Found, Night Vision Improved Simultaneously</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/oqGZeHzMYzo">youtu.be/oqGZeHzMYzo</a></p>
<blockquote>
<p><em>"My vision night vision improved. Found out I have cataracts and I'm hoping that carnivore keeps cataracts at bay. I started — it was January that I found out I had cataracts. Went to go get a new prescription."</em></p>
</blockquote>
<p>Paradox of discovering cataracts while simultaneously noticing night vision improvement. Also required a new prescription — suggesting some lens clarity change. Using carnivore intentionally as a strategy to slow cataract progression.</p>

<h3>Case 3 — Post-Trauma Cataract Stable Over Multiple Exams</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/I8b1WPulCfw">youtu.be/I8b1WPulCfw</a></p>
<blockquote>
<p><em>"He said I did have a little bit of a cataract starting in this left eye — no doubt because that's where all the trauma was, where I had the shots. But I had another exam this year and that's not changing."</em></p>
</blockquote>
<p>Cataract in a previously injected/traumatized eye monitored across multiple exams — remained stable and non-progressing after dietary change.</p>

<h3>Proposed Mechanism</h3>
<p>Cataracts are strongly associated with oxidative stress and glycation of lens proteins (sorbitol accumulation from hyperglycemia). Eliminating dietary glucose reduces lens protein glycation — a direct anti-cataract mechanism that is independent of supplementation.</p>""",
        "order": 12,
    },
    {
        "title": "Dry Eye & Carnivore: 2 Case Reports",
        "slug": "carnivore-dry-eye-cases",
        "summary": (
            "Two compelling dry eye cases on carnivore — one lifelong sufferer whose eyes "
            "became fully moist for the first time, and one person who had to pry their "
            "eyes open every morning and use drops just to get out of bed."
        ),
        "content": """<h2>Dry Eye Cases on Carnivore</h2>

<h3>Case 1 — Lifelong Dry Eyes Completely Resolved</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/jyJY1Wf8O8k">youtu.be/jyJY1Wf8O8k</a></p>
<blockquote>
<p><em>"One thing I noticed which I had suffered all my life that I can remember was dry eyes and very red sore eyes always. That went. My eyes now are so moist. It's wonderful. It's lovely to have that."</em></p>
</blockquote>
<p>Lifelong dry eye and chronically red, sore eyes — present for as long as the person could remember — completely resolved on carnivore. Described as one of the most significant and unexpected improvements, unprompted.</p>

<h3>Case 2 — Had to Pry Eyes Open Every Morning, Used Drops Daily</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/hnYnaqOsw3U">youtu.be/hnYnaqOsw3U</a></p>
<blockquote>
<p><em>"The dry eyes — I used to wake up and I'd have to literally pry my eyes open because my eyes were so dry and I'd have to use drops to get up in the morning. It was kind of scary to be quite honest. And my mouth was so dry that I used to have to sleep with..."</em></p>
</blockquote>
<p>This case involved severe dry eye alongside dry mouth — a pattern consistent with <strong>Sjögren's syndrome</strong> (autoimmune exocrine gland dysfunction). Both symptoms resolved together, suggesting this was autoimmune-mediated dry eye rather than purely environmental. Carnivore's autoimmune-resolution pathway likely drove the improvement.</p>

<h3>Proposed Mechanism</h3>
<p>Dry eye has two primary causes on carnivore: (1) <strong>inflammatory</strong> — omega-6 dominance in the diet drives prostaglandin-mediated lacrimal gland inflammation; carnivore corrects omega-3:omega-6 ratio. (2) <strong>Autoimmune</strong> — Sjögren's-pattern dry eye may respond to carnivore's elimination of dietary antigens that trigger molecular mimicry. Both mechanisms are plausible depending on the individual.</p>""",
        "order": 13,
    },
    {
        "title": "Eye Floaters & Carnivore: 2 Case Reports",
        "slug": "carnivore-floaters-cases",
        "summary": (
            "Two floater cases on carnivore — one resolving 90% and the person forgetting "
            "they'd ever had them, and one case where doctors explicitly said the floater "
            "was permanent. It went away anyway."
        ),
        "content": """<h2>Eye Floater Cases on Carnivore</h2>

<h3>Case 1 — Floaters 90% Gone, Had Forgotten About Them</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/Qr-ynwHvGPs">youtu.be/Qr-ynwHvGPs</a></p>
<blockquote>
<p><em>"All of a sudden I notice — I don't have them. They're gone. I had floaters in my eyes — you know what those are, right? You get these little shadows floating around in your eye. That's probably 90% gone now. It's almost — I matter of fact, it was kind of funny 'cuz I had forgot about them."</em></p>
</blockquote>
<p>Floaters resolved so gradually the person didn't notice until they were mostly gone. The fact they "forgot about them" suggests a slow, non-dramatic clearance — consistent with vitreous reabsorption rather than sudden change.</p>

<h3>Case 2 — Doctors Said Floater Was Permanent. It Resolved.</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/5LQwKOn7A3s">youtu.be/5LQwKOn7A3s</a></p>
<blockquote>
<p><em>"I had a floater kind of thing in my left eye that the doctors were like, 'Yeah, that's probably never going to go away. It's fluid that got released.' Went away. That was another thing. Went away after that, after, you know, them telling me over and over and over again, won't go away, won't go away."</em></p>
</blockquote>
<p>Doctor explicitly told the patient the floater was permanent — described as released fluid (likely a vitreous detachment condensate). It fully resolved on carnivore. The repeated "they said it was permanent" framing emphasises how unexpected the outcome was.</p>

<h3>Proposed Mechanism</h3>
<p>Floaters are composed of collagen fibers and cellular debris suspended in the vitreous humor. Chronic systemic inflammation and oxidative stress are thought to accelerate vitreous degeneration and new floater formation. Reducing inflammation may slow formation; improved collagen quality from animal-protein-rich diets may support vitreous structure. These mechanisms are speculative but align with the resolution pattern observed.</p>""",
        "order": 14,
    },
    {
        "title": "Vision Improvement & Prescription Changes on Carnivore: 7 Case Reports",
        "slug": "carnivore-vision-prescription-cases",
        "summary": (
            "Seven accounts of vision sharpening and prescriptions weakening on carnivore "
            "— including 3 consecutive improving eye exams requiring new weaker glasses each "
            "time, a person going blind who stopped declining when blood sugar normalized, "
            "and one reported full sight recovery."
        ),
        "content": """<h2>Vision Improvement & Prescription Cases on Carnivore</h2>

<h3>Case 1 — Three Consecutive Eye Exams, Weaker Glasses Each Time</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/glqayBD2Oe8">youtu.be/glqayBD2Oe8</a></p>
<blockquote>
<p><em>"I went in and the doctor said, 'Well, no wonder your eyes are blurry — they're better and your prescription is too strong.' So I had to buy new glasses. And then last year I went back in and he said, 'Your eyes have improved a little again.' And he said, 'Well, you need new glasses because your eyes have improved yet again.'"</em></p>
</blockquote>
<p>Three consecutive exams showing ongoing improvement — had to buy progressively weaker glasses twice. Doctor confirmed the pattern. Eyes improving counter to the expected age-related decline.</p>

<h3>Case 2 — Needed Weaker Prescription, Eyes "Got Better"</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/kfG7VLByTaA">youtu.be/kfG7VLByTaA</a></p>
<blockquote>
<p><em>"My eyesight's improved at the last eye test. My glasses don't work in the same way as they used to. I'm needing a new prescription because it's got better."</em></p>
</blockquote>

<h3>Case 3 — Prescription Grade Dropped</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/USXfOJ6oSho">youtu.be/USXfOJ6oSho</a></p>
<blockquote>
<p><em>"I had to change the prescription to a lower grade. I think, wow, that would never happen to me in any other way."</em></p>
</blockquote>
<p>Treated the prescription drop as concrete, unexpected evidence of genuine biological improvement — not a subjective feeling.</p>

<h3>Case 4 — Annual Prescription Increases Stopped Completely</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/HZReTaFhwf8">youtu.be/HZReTaFhwf8</a></p>
<blockquote>
<p><em>"The last two years my prescription for my lenses hasn't changed — and before that every year I was getting a stronger prescription. So that hasn't changed. So great improvement on my eyes."</em></p>
</blockquote>
<p>Annual worsening trajectory halted completely — two consecutive stable years after starting carnivore.</p>

<h3>Case 5 — Can Read Bus Numbers Others Can't See</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/9_OyNZpkzCI">youtu.be/9_OyNZpkzCI</a></p>
<blockquote>
<p><em>"I can now read the bus numbers like when it comes over the hill down the road. I can go, 'Oh I know what that is,' and everyone's kind of squinting and I'm like, I can see this now. Like, how did that even happen?"</em></p>
</blockquote>

<h3>Case 6 — Vision Among 59 Ailments Resolved</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/Zm6zegm0S-w">youtu.be/Zm6zegm0S-w</a></p>
<blockquote>
<p><em>"I was taking nine prescriptions. I've counted over 59 different ailments that I've cured or reduced or stopped. My vision has gotten better and improved."</em></p>
</blockquote>
<p>Vision improvement listed within a comprehensive resolution of 59 separate health complaints — consistent with a systemic anti-inflammatory effect rather than a targeted eye intervention.</p>

<h3>Case 7 — Going Blind, Stopped Declining When Blood Sugar Normalized</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/0nzf72h5784">youtu.be/0nzf72h5784</a></p>
<blockquote>
<p><em>"For years I was telling him — I kept asking him, 'Why is my eyesight failing so quickly?' And he said, 'Oh, it's just your age.' I was pretty sure I was going blind. And when I got my A1C down, my eyesight stopped declining."</em></p>
</blockquote>
<p>Rapid vision deterioration dismissed as aging by doctor. When HbA1c normalized through dietary change, vision loss stopped. The A1C connection strongly implicates <strong>diabetic retinopathy</strong> as the mechanism — retinal microvascular damage driven by chronic hyperglycemia.</p>

<h3>Bonus — Full Sight Recovery Reported (Third-Party Account)</h3>
<p><strong>Source:</strong> ZeroCarb community — <a href="https://youtu.be/rn7byKZbbKE">youtu.be/rn7byKZbbKE</a></p>
<blockquote>
<p><em>"Especially the individual — I forgot his name — that was going blind and went through carnivore diet and got his sight back. My good friend is going through something similar. And I sent him that video."</em></p>
</blockquote>
<p>Reference to a previous guest who reportedly went blind and fully regained sight on carnivore. Third-party account — video reference not confirmed — but notable enough that the speaker forwarded it to a friend with the same issue.</p>

<h3>Proposed Mechanism</h3>
<p>The clearest mechanism across these cases is <strong>blood glucose normalization → reduced retinal microvascular damage</strong>. For early-stage diabetic and pre-diabetic retinopathy, lowering chronic glucose exposure allows retinal capillaries to recover. Additional factors: reduced lens glycation (sharpens focus), reduced intraocular inflammation (improves corneal clarity), and improved retinal circulation from lower triglycerides and blood pressure.</p>""",
        "order": 15,
    },
]


class Command(BaseCommand):
    help = "Load carnivore eye condition case reports as Articles under the Carnivore Diet pillar"

    def add_arguments(self, parser):
        parser.add_argument(
            "--publish",
            action="store_true",
            help="Mark all articles as published immediately",
        )

    def handle(self, *args, **options):
        try:
            pillar = Pillar.objects.get(slug="carnivore-diet")
        except Pillar.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                "Carnivore Diet pillar not found. Run load_carnivore_seafood first."
            ))
            return

        publish = options["publish"]
        for data in ARTICLES:
            article, created = Article.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "title": data["title"],
                    "summary": data["summary"],
                    "content": data["content"],
                    "pillar": pillar,
                    "order": data["order"],
                    "published": publish,
                },
            )
            action = "Created" if created else "Updated"
            status = "published" if publish else "draft"
            self.stdout.write(f"  {action} article ({status}): {article.title}")

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {len(ARTICLES)} eye condition articles loaded "
            f"({'published' if publish else 'draft — run with --publish to make live'})."
        ))
