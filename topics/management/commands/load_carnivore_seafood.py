from django.core.management.base import BaseCommand
from django.utils.text import slugify
from topics.models import Pillar, Article


PILLAR = {
    "name": "Carnivore Diet",
    "slug": "carnivore-diet",
    "description": (
        "Evidence, expert protocols, and real-world n=1 experiences on the carnivore "
        "and animal-based diet — from strict lion-diet practitioners to seafood-inclusive "
        "flexible approaches. Sourced from physician transcripts, community testimonials, "
        "and clinical observations."
    ),
    "icon": "🥩",
    "color": "crimson",
    "order": 10,
}


ARTICLES = [
    {
        "title": "Seafood on Carnivore: Overview & Spectrum",
        "slug": "carnivore-seafood-overview",
        "summary": (
            "Where does seafood fit in a carnivore diet? From lion-diet purists to "
            "flexible animal-based eaters, this overview maps the full spectrum and "
            "explains why fish and shellfish are widely accepted as carnivore foods."
        ),
        "content": """<h2>Overview</h2>
<p>Seafood — fish, shellfish, and other marine animals — sits in an interesting position within the carnivore community. It is universally accepted as animal food and therefore "technically" carnivore, yet debates persist about whether it belongs alongside beef as a primary food or is treated as a peripheral add-on.</p>

<p>The transcripts across four major carnivore channels (Anthony Chaffee MD, Shawn Baker MD, ZeroCarb community, Metabolic Mind) reveal a clear spectrum:</p>

<h3>The Carnivore Spectrum on Seafood</h3>
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
<table>
<thead><tr><th>Approach</th><th>Who</th><th>Seafood Role</th></tr></thead>
<tbody>
<tr><td><strong>Lion diet</strong></td><td>Mikhaila Peterson style</td><td>Zero seafood — red meat + salt + water only</td></tr>
<tr><td><strong>Beef-first carnivore</strong></td><td>Chaffee personally</td><td>Beef dominant; fish acknowledged, not pushed</td></tr>
<tr><td><strong>Flexible carnivore</strong></td><td>Shawn Baker MD</td><td>Fish is his #4 food; shrimp + salmon regular</td></tr>
<tr><td><strong>Animal-based</strong></td><td>ZeroCarb community</td><td>Seafood freely included; variety encouraged</td></tr>
<tr><td><strong>Therapeutic carnivore</strong></td><td>Metabolic Mind clinical</td><td>Meat + fish + eggs as standard patient menu</td></tr>
</tbody>
</table>
</div>

<h3>Why People Add Seafood to Carnivore</h3>
<ul>
<li><strong>Omega-3s</strong> — especially important when eating predominantly grain-finished beef (high omega-6)</li>
<li><strong>Vitamin D</strong> — fatty fish is one of the densest dietary sources</li>
<li><strong>Zinc &amp; testosterone</strong> — oysters, crab, lobster are the richest zinc foods on earth</li>
<li><strong>Copper for iron retention</strong> — shellfish copper helps the body retain ferritin (iron storage)</li>
<li><strong>Iodine</strong> — seafood is the primary whole-food iodine source; 100% of Australians not eating seafood test deficient (Chaffee data)</li>
<li><strong>Convenience</strong> — smoked salmon can be eaten straight from the package</li>
<li><strong>Affordability &amp; access</strong> — in countries where beef is expensive, fish is the primary carnivore protein</li>
<li><strong>Social dining</strong> — seafood restaurants are one of the easiest places to eat carnivore when out</li>
</ul>

<h3>The "Fish as Vegetable" Debate</h3>
<p>The Ron Swanson (Parks &amp; Recreation) quote — <em>"Fish for sport only, not for meat. Fish meat is practically a vegetable"</em> — is referenced in the community with humor. Shawn Baker acknowledges it but does not endorse it; he actively eats fish regularly. Most practitioners treat it as a joke, not a guiding principle.</p>

<h3>Ancestral Argument</h3>
<p>A ZeroCarb community member invokes the grizzly bear: <em>"There is a project in Canada where they follow grizzly bears... this bear sitting in the river eating salmon all day long and I said — okay, if a bear is a carnivore and it eats salmon..."</em> Apex carnivores in nature routinely eat fish; the same logic extends to human ancestral diets.</p>

<p><strong>Sources:</strong> Anthony Chaffee MD transcripts, Shawn Baker MD transcripts, ZeroCarb community transcripts, Metabolic Mind transcripts</p>""",
        "order": 1,
    },
    {
        "title": "Shawn Baker MD: Fish & Shellfish in His Carnivore Protocol",
        "slug": "shawn-baker-seafood-carnivore",
        "summary": (
            "Dr. Shawn Baker makes fish his 4th most common food on carnivore — after beef, "
            "eggs, and dairy. Wild-caught salmon, shrimp, oysters, and shellfish all feature "
            "regularly. Here are his direct quotes and reasoning."
        ),
        "content": """<h2>Shawn Baker MD on Seafood</h2>
<p>Dr. Baker is one of the most prominent carnivore advocates and a practicing physician. His personal protocol is practical and not dogmatic — fish and shellfish feature regularly.</p>

<h3>Fish as His #4 Carnivore Food</h3>
<blockquote>
<p><em>"After dairy, then fish would be my fourth most common. And more often than not, I just — because I'm relatively minimalist and fairly lazy when it comes to cooking — I'll often eat things like smoked salmon 'cuz I can just open it up and eat it directly out of the packaging. Try to get wild-caught when I can... a little bit of steak every day, some cottage cheese and salmon."</em></p>
<footer>— Shawn Baker, Top 5 Foods on Carnivore Diet (Video: wHI1XkH3E7k)</footer>
</blockquote>

<blockquote>
<p><em>"I have a lot of things like salmon and shrimp as a sort of sometimes as a side to my meals."</em></p>
</blockquote>

<h3>Refrigerator Tour: Wild-Caught Salmon from Costco</h3>
<blockquote>
<p><em>"For the sake of variety, I'm expanding my normal palette a little just for the sense of displaying what potentially is possible on a carnivore diet. For a little snack, I'm going to have some of this salmon. This is a smoked salmon, just a wild-caught Alaskan salmon... I'll probably eat about half that. That's probably about 4 ounces of salmon."</em></p>
<p><em>"Got some wild-caught salmon also again from Costco."</em></p>
<footer>— Shawn Baker, Refrigerator Tour (Video: CgGIeRMRBBM)</footer>
</blockquote>

<h3>Shellfish for Testosterone &amp; Sexual Health</h3>
<blockquote>
<p><em>"Shellfish is another food — now shellfish has a lot of zinc and we know that zinc has a significant relationship with testosterone and sexual function... things like crab, lobster, oysters — great sources of those."</em></p>
</blockquote>

<blockquote>
<p><em>"Fatty fish like salmon has a number of very important compounds from the omega-3 fats EPA, DHA, proteins, selenium, vitamin D — all these things are important."</em></p>
<footer>— Shawn Baker, Testosterone &amp; Red Meat (Video: 6ZkGXWBDUjY)</footer>
</blockquote>

<h3>Naturally Occurring Glutamates in Shellfish</h3>
<p>Baker notes that oysters, clams, scallops, anchovies, and sardines are natural sources of MSG (monosodium glutamate) — a non-concern for carnivores eating whole foods.</p>

<h3>Key Takeaways from Baker</h3>
<ul>
<li>Wild-caught over farmed when possible; Costco is a cited accessible source</li>
<li>Smoked salmon = the most convenient carnivore fish (open and eat)</li>
<li>Shellfish (oysters, crab, lobster) = the best dietary zinc sources, supporting testosterone</li>
<li>Fatty fish (salmon, mackerel) = vitamin D + omega-3 EPA/DHA + selenium</li>
<li>Fish is not ideologically inferior to red meat in Baker's protocol</li>
</ul>

<p><strong>Sources:</strong> Shawn Baker MD YouTube transcripts — Videos: wHI1XkH3E7k, JKkmwIUk0ds, CgGIeRMRBBM, 6ZkGXWBDUjY, 34l8HMFaEqE</p>""",
        "order": 2,
    },
    {
        "title": "Anthony Chaffee MD: The Case for Fish on Carnivore (Iodine, Omega-3, Iron)",
        "slug": "anthony-chaffee-seafood-carnivore",
        "summary": (
            "Dr. Chaffee personally prefers beef but raises compelling micronutrient arguments "
            "for fish: iodine deficiency in non-seafood eaters, omega-3 gaps on grain-finished "
            "beef, and a guest's n=1 copper-shellfish fix for ferritin. Plus: 7–14 day sardine "
            "fast DEXA data."
        ),
        "content": """<h2>Anthony Chaffee MD on Seafood</h2>
<p>Dr. Chaffee (Plant Free MD) personally feels best on beef and doesn't push fish — but his show surfaces some of the most scientifically grounded arguments for including seafood on carnivore.</p>

<h3>Chaffee's Own Position</h3>
<blockquote>
<p><em>"I'm in the position that I can sort of eat whatever meat I want, but I always feel best eating just beef and that sort of thing. But there are others that have to be more careful with it and so there are different sorts of things that complement each other — there's different meats and organs and seafood."</em></p>
<footer>— Anthony Chaffee, Video: bCtJCOOEuv8</footer>
</blockquote>

<h3>Iodine: The Overlooked Gap</h3>
<blockquote>
<p><em>"Most soils are actually pretty deficient in iodine, especially in Australia. 100% of the people that I check — check their iodine in Australia on a standard diet unless they eat a lot of seafood — they're low. A lot of fish can sort that out, but a lot of people aren't doing that."</em></p>
<footer>— Anthony Chaffee, Video: F6r7xoJCSrc</footer>
</blockquote>
<p><strong>Implication:</strong> Beef-only carnivore without iodized salt creates a real iodine gap. Seafood is the primary whole-food solution.</p>

<h3>Omega-3s When Eating Grain-Finished Beef</h3>
<blockquote>
<p><em>"Adding in some fish, things like that — you have to think about those omega-3s if you're predominantly eating grain-finished."</em></p>
<footer>— Anthony Chaffee, Video: F6r7xoJCSrc</footer>
</blockquote>
<p>Grass-fed beef has a favorable omega-3:omega-6 ratio; grain-finished shifts toward omega-6 dominance. Fish corrects this without supplementation.</p>

<h3>n=1 Guest: Surf-and-Turf After Grief, Then Shellfish for Iron Retention</h3>
<blockquote>
<p><em>"Before he passed, I was eating a lot of red meat. And then after he passed and after things sort of shifted for me, I started eating more fish. And now I do like a surf-and-turf kind of thing."</em></p>
</blockquote>
<blockquote>
<p><em>"I'm sorry — the iron from the meat. And so that's why I added in shellfish because copper helps retain iron and ferritin and that was very important to me. And ever since I made those changes really it's been smooth sailing from there."</em></p>
<footer>— Chaffee guest, Video: bCtJCOOEuv8</footer>
</blockquote>
<p><strong>Mechanism:</strong> Copper (abundant in oysters and shellfish) is required for ceruloplasmin — the protein that loads iron into red blood cells. Low copper = poor iron retention even with adequate iron intake. This guest fixed their ferritin problem by adding shellfish as a copper source.</p>

<h3>n=1 Experiment: 7–14 Day Sardine-Only Fasts</h3>
<blockquote>
<p><em>"I've done a lot of sardine-related. So I've done like 7, 10, 14-day sardine fasts where that's all I ate. I did before and after blood work and DEXA scans just to see what would happen."</em></p>
<p><em>"Very interesting visceral fat loss on a sardine fast. It's basically a protein sparing modified fast."</em></p>
<footer>— Chaffee guest, Video: GC9SVt5fNn8</footer>
</blockquote>
<p><strong>Finding:</strong> Sardines alone (high protein, moderate fat, complete amino acids, rich in EPA+DHA) drove measurable visceral fat loss on DEXA. The mechanism: high protein + lower calories = protein-sparing modified fast effect while maintaining muscle.</p>

<h3>Histamine Warning for Sensitive Individuals</h3>
<blockquote>
<p><em>"It could be that you need to go low-histamine carnivore... how fresh is it? Is it aged? Is it smoked? You can't — if you have histamine issues — you can't be eating a bunch of smoked brisket... even fish."</em></p>
<footer>— Anthony Chaffee transcripts</footer>
</blockquote>
<p><strong>Caution:</strong> Smoked, canned, or aged fish (smoked salmon, sardines in cans) is high histamine. People with histamine sensitivity should use fresh fish only.</p>

<h3>Fish as an On-Ramp for Ex-Vegetarians</h3>
<blockquote>
<p><em>"Half of them decided to start eating eggs and fish and chicken etc. So you know, you're not always going to get everyone full carnivore but you're moving them in the right direction."</em></p>
<footer>— Chaffee guest, Video: qd2WDow8ltM</footer>
</blockquote>

<p><strong>Sources:</strong> Anthony Chaffee MD transcripts — Videos: bCtJCOOEuv8, GC9SVt5fNn8, F6r7xoJCSrc, qd2WDow8ltM, VgfGo8zK0_0</p>""",
        "order": 3,
    },
    {
        "title": "ZeroCarb Community: Real-World Testimonials on Carnivore + Seafood",
        "slug": "zerocarb-community-seafood-testimonials",
        "summary": (
            "With 1,092 seafood mentions, the ZeroCarb community channel has the richest "
            "real-world testimony on how everyday carnivores incorporate fish, shellfish, "
            "and seafood — from steak-and-shrimp celebrations to Thailand fish-only protocols "
            "and oyster fritter cooking discoveries."
        ),
        "content": """<h2>ZeroCarb Community: Seafood on Carnivore</h2>
<p>The ZeroCarb community channel has over 1,000 mentions of seafood — the highest volume of any source — with wide-ranging protocols from strict lion-diet members to flexible animal-based eaters who freely include fish and shellfish.</p>

<h3>How Community Members Define Carnivore (Including Seafood)</h3>
<blockquote>
<p><em>"Just saying carnivore instead of, you know, only eating meats and eggs and possibly seafood and fish — that was different. But she wasn't opposed to it."</em></p>
<footer>— ZeroCarb, Video: PceuXaqVjq0</footer>
</blockquote>
<blockquote>
<p><em>"You can make carnivore pizza. You can eat chicken or pork or seafood if you'd like."</em></p>
</blockquote>

<h3>Real Diet Example: 70% Beef / 30% Mixed Animal Foods</h3>
<blockquote>
<p><em>"My diet consists of fatty beef with the other 30% consisting of chicken, pork, lamb, tripe, eggs, cheese, fish, and shrimp. All of which I buy at conventional grocery stores. I generally eat twice a day and only drink water, unflavored salts, and bone broth."</em></p>
<footer>— ZeroCarb community member</footer>
</blockquote>
<p>This is a practical, real-world flexible carnivore — beef-dominant but with fish and shrimp as regular variety proteins, sourced from ordinary grocery stores.</p>

<h3>Steak + Shrimp: The Carnivore Celebration Meal</h3>
<blockquote>
<p><em>"When we were a year into carnivore, all my girlfriends went out to celebrate my year being carnivore and every single person did not drink and ordered steak and shrimp."</em></p>
<footer>— ZeroCarb, Video: Qi2adEZVkGk</footer>
</blockquote>
<p>Steak + shrimp is the de facto social "carnivore celebration meal" — achievable at virtually any restaurant.</p>

<h3>Eating Out: Seafood Restaurants Are Carnivore-Friendly</h3>
<blockquote>
<p><em>"We've gone to her favorite restaurants, which are seafood restaurants, and I just have — I can have fish and all any seafood — I gladly feast on and still maintain my carnivore diet."</em></p>
<footer>— ZeroCarb, Video: pBbUwQ6Jidw</footer>
</blockquote>

<h3>Cooking Discovery: Oysters and Crab for the First Time</h3>
<blockquote>
<p><em>"I never cooked before really. But ever since I started carnivore, I cook — and now I cook all the meat and I'm making crab cakes and I'm making oyster fritters. I'm like, 'Oh, wow.'"</em></p>
<footer>— ZeroCarb, Video: sxnYqjZXwrI</footer>
</blockquote>
<p>Carnivore pushed someone to cook for the first time; shellfish variety increased culinary engagement and enjoyment.</p>

<h3>Thailand: Sustained High Training on Fish + Chicken Carnivore</h3>
<blockquote>
<p><em>"They provided carnivore food for me, which was in Thailand, as you can imagine, a lot of chicken, a lot of fish and a bit of beef. But I trained 6, 7 hours a day."</em></p>
<footer>— ZeroCarb, Video: pJMS6asEQx8</footer>
</blockquote>
<p><strong>Real-world adaptation:</strong> In countries where beef is expensive or scarce, fish becomes the primary carnivore protein. High athletic training volume sustained on fish + chicken.</p>

<h3>Grizzly Bear Ancestral Argument</h3>
<blockquote>
<p><em>"There is a project in Canada where they follow grizzly bears watching them get fed going into hibernation... this bear sitting in the river eating salmon all day long and I kind of said — okay, well if bear is a carnivore and it eats salmon..."</em></p>
<footer>— ZeroCarb, Video: jJD86UVQE9Y</footer>
</blockquote>

<h3>Dr. Boz (Annette Bosworth): Oily Fish for Ketosis</h3>
<blockquote>
<p><em>"She very much advocates for a carnivore diet. She very much advocates for using lots of oily fish and things like that to up [fat and omega-3 content]."</em></p>
<footer>— Referenced in ZeroCarb transcripts</footer>
</blockquote>
<p>Dr. Boz's approach: sardines, salmon, and mackerel as fat and omega-3 vehicles to deepen ketosis on carnivore.</p>

<h3>Shrimp When Protein Is Hard to Hit</h3>
<blockquote>
<p><em>"I find it hard. I have to add things like shrimp sometimes... so sometimes I'll do things like that [to hit protein targets]."</em></p>
<footer>— ZeroCarb, Video: hnYnaqOsw3U</footer>
</blockquote>

<h3>Exotic Seafood Exploration</h3>
<blockquote>
<p><em>"And now with carnivore, I see a fish I didn't know yet or I see — oh my gosh, jellyfish, silk worms, sago grubs, horse shoe crabs, all this — I love them. Like I never had that before, so cool."</em></p>
<footer>— ZeroCarb, Video: d4VUXD6m-EU</footer>
</blockquote>

<h3>Beginner Advice from the Community</h3>
<blockquote>
<p><em>"Lots of people saying: just eat meat and fat and fish and eggs and that's all you need — it is all you need. But then I see 'I failed, I'm not feeling well, I've got diarrhea...'"</em></p>
<footer>— ZeroCarb, Video: zFYoaKy7P3o</footer>
</blockquote>
<p>Meat + fat + fish + eggs is the community's standard beginner recommendation. Adaptation issues (diarrhea, fatigue) are common in weeks 1–4 regardless of protein source.</p>

<p><strong>Sources:</strong> ZeroCarb YouTube community transcripts — Videos: PceuXaqVjq0, Qi2adEZVkGk, pBbUwQ6Jidw, sxnYqjZXwrI, pJMS6asEQx8, jJD86UVQE9Y, hnYnaqOsw3U, d4VUXD6m-EU, zFYoaKy7P3o, B6oviPigRdk, vdqAN8qSAz0</p>""",
        "order": 4,
    },
    {
        "title": "Metabolic Mind: Clinical Carnivore + Fish in Psychiatric & Memory Care Settings",
        "slug": "metabolic-mind-clinical-seafood-carnivore",
        "summary": (
            "Metabolic Mind documents physicians using meat + fish + eggs protocols for "
            "memory care residents and psychiatric patients — with conventional grocery "
            "store fish producing real clinical results. Premium sourcing is not required."
        ),
        "content": """<h2>Metabolic Mind: Clinical Carnivore + Seafood</h2>
<p>Metabolic Mind focuses on the therapeutic application of low-carb and carnivore diets for neurological and psychiatric conditions. Seafood appears consistently in clinical settings, with physicians reporting positive patient outcomes.</p>

<h3>Clinical Implementation: Memory Care Residents</h3>
<blockquote>
<p><em>"I thought this is going to be a little hard to convince my residents and their family that hey, you're just going to eat meat and fish and eggs and that's all we're going to do. So as I looked into more of the carnivore diet..."</em></p>
</blockquote>
<blockquote>
<p><em>"You don't always have to buy grass-fed beef — we're seeing changes with our residents with grocery store beef. Same with fish. And you can use chicken as well."</em></p>
<footer>— Physician, Metabolic Mind transcripts</footer>
</blockquote>

<h3>Key Clinical Observations</h3>
<ul>
<li><strong>Conventional grocery store fish works.</strong> Premium (wild-caught, organic) is not required to see clinical benefit in patients.</li>
<li><strong>Meat + fish + eggs</strong> is the standard menu template used in a residential care setting.</li>
<li><strong>Family buy-in</strong> was a perceived barrier but was managed by showing results.</li>
<li>Positive outcomes reported for memory and cognitive function on this protocol.</li>
</ul>

<h3>Advocacy Framing</h3>
<blockquote>
<p><em>"You don't have to go carnivore, but animal source foods have a role. Meat, fish, eggs, and dairy are nutritious foods."</em></p>
<footer>— Metabolic Mind transcripts</footer>
</blockquote>
<p>Fish is positioned alongside meat, eggs, and dairy as a foundational animal food — not an afterthought.</p>

<h3>Relevance for Home Practitioners</h3>
<p>If a clinical setting using standard grocery store fish produces measurable improvements in memory care patients, the bar for fish quality in a healthy self-experimenter is even lower. The key variable is <em>inclusion</em>, not sourcing tier. Wild-caught is ideal; conventional grocery store fish is effective.</p>

<p><strong>Sources:</strong> Metabolic Mind YouTube transcripts</p>""",
        "order": 5,
    },
    {
        "title": "Carnivore + Seafood: Best Choices, Cautions & Practical Protocol",
        "slug": "carnivore-seafood-practical-guide",
        "summary": (
            "A practical synthesis: the best seafood for carnivore, when to add it, "
            "histamine cautions, the iodine gap, how to use seafood restaurants, and "
            "a self-experiment framework for testing your own response."
        ),
        "content": """<h2>Practical Guide: Carnivore + Seafood</h2>

<h3>Best Seafood Choices for Carnivore</h3>
<p>Based on what practitioners and community members actually eat and recommend:</p>
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
<table>
<thead><tr><th>Seafood</th><th>Why It Works</th><th>Best Form</th></tr></thead>
<tbody>
<tr><td><strong>Wild-caught salmon</strong></td><td>Omega-3 EPA+DHA, vitamin D, selenium, protein</td><td>Smoked (open and eat); fresh fillet; Costco frozen</td></tr>
<tr><td><strong>Sardines</strong></td><td>Omega-3, calcium (from bones), vitamin D; portable</td><td>Canned in water or olive oil; fresh preferred for histamine issues</td></tr>
<tr><td><strong>Oysters</strong></td><td>Highest zinc food on earth; copper, B12, iron</td><td>Fresh raw; canned as a convenient option</td></tr>
<tr><td><strong>Shrimp</strong></td><td>Lean protein, easy to cook, hits protein targets when appetite is low</td><td>Frozen wild-caught; grilled or butter-sautéed</td></tr>
<tr><td><strong>Mackerel</strong></td><td>Very high omega-3, vitamin D; oily fish for ketosis</td><td>Fresh fillet; canned (watch for sauces)</td></tr>
<tr><td><strong>Crab / Lobster</strong></td><td>Zinc, selenium, lean protein; excellent for testosterone support</td><td>Fresh steamed; restaurant-safe</td></tr>
<tr><td><strong>Anchovies</strong></td><td>High omega-3, calcium, natural glutamates; concentrated nutrition</td><td>Canned in olive oil; use as a flavor base</td></tr>
</tbody>
</table>
</div>

<h3>When to Add Seafood to Your Carnivore Protocol</h3>
<ul>
<li><strong>Eating grain-finished beef</strong> → add fatty fish (salmon, mackerel, sardines) for omega-3 balance</li>
<li><strong>Not using iodized salt</strong> → add seafood 2–3x/week as dietary iodine source</li>
<li><strong>Low ferritin despite adequate iron intake</strong> → add shellfish (oysters specifically) for copper</li>
<li><strong>Low testosterone or zinc deficiency</strong> → prioritize oysters, crab, lobster</li>
<li><strong>Struggle to hit protein targets</strong> → shrimp is lean, quick-cooking, easy to eat</li>
<li><strong>Eating out</strong> → seafood restaurants are the easiest carnivore-compatible dining option</li>
<li><strong>Traveling internationally</strong> (especially Asia) → fish replaces beef as primary protein</li>
</ul>

<h3>Cautions</h3>
<h4>Histamine Sensitivity</h4>
<p>Smoked, canned, or aged fish is <strong>high histamine</strong>. If you have histamine sensitivity:</p>
<ul>
<li>Avoid: smoked salmon, canned sardines, aged fish, dried anchovies</li>
<li>Use: fresh fish cooked immediately after purchase; freeze fresh fish promptly</li>
</ul>

<h4>Mercury</h4>
<p>High-mercury fish (swordfish, king mackerel, tilefish, shark) should be limited, especially in pregnancy. Salmon, sardines, shrimp, oysters, and crab are all low-mercury and safe for regular consumption.</p>

<h4>Adaptation Period</h4>
<p>The community consistently notes that digestive adaptation issues (diarrhea, fatigue) occur in weeks 1–4 of carnivore regardless of protein source. Adding fish does not cause this — it's a transition effect from eliminating plant foods.</p>

<h3>Using Seafood Restaurants on Carnivore</h3>
<p>Seafood restaurants are among the most carnivore-friendly dining options:</p>
<ul>
<li>Grilled fish fillet with butter: universally available</li>
<li>Steamed or grilled shellfish (crab, lobster, shrimp): available everywhere</li>
<li>Raw oysters: pure animal food, zero additives</li>
<li>Request: butter instead of sauces; no breading; ask about marinades</li>
</ul>

<h3>n=1 Self-Experiment Framework</h3>
<p>If you want to test whether adding seafood improves your carnivore results:</p>
<ol>
<li><strong>Baseline labs:</strong> Ferritin, zinc, iodine (if accessible), omega-3 index (OmegaQuant), fasting lipids, testosterone</li>
<li><strong>Intervention:</strong> Add 2–3 servings/week of mixed seafood (1 serving oily fish, 1 serving shellfish)</li>
<li><strong>Track subjectively:</strong> Energy, mood, joint comfort, dry eyes, skin quality — weekly notes</li>
<li><strong>Retest at 3 months:</strong> Same labs panel</li>
<li><strong>Interpret:</strong> Compare ferritin, zinc, testosterone, omega-3 index before vs. after</li>
</ol>

<h3>Notable n=1 Experiments from Transcripts</h3>
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
<table>
<thead><tr><th>Experimenter</th><th>Experiment</th><th>Finding</th></tr></thead>
<tbody>
<tr><td>Chaffee guest (GC9SVt5fNn8)</td><td>7–14 day sardine-only fasts with DEXA + bloodwork</td><td>Measurable visceral fat loss; functions as protein-sparing modified fast</td></tr>
<tr><td>Chaffee guest (bCtJCOOEuv8)</td><td>Added shellfish for copper → iron retention</td><td>Resolved ferritin problem; "smooth sailing from there"</td></tr>
<tr><td>Shawn Baker</td><td>Regular wild-caught salmon as a daily carnivore food</td><td>Sustained long-term; fish is his #4 most consumed food</td></tr>
<tr><td>ZeroCarb (Thailand)</td><td>Fish + chicken carnivore during 6–7 hrs/day training</td><td>Sustained high athletic output without beef</td></tr>
<tr><td>MetabolicMind clinical</td><td>Meat + fish + eggs for memory care residents (grocery store fish)</td><td>Positive outcomes; premium sourcing not required</td></tr>
</tbody>
</table>
</div>

<p><strong>Sources:</strong> Compiled from Anthony Chaffee MD, Shawn Baker MD, ZeroCarb community, and Metabolic Mind transcripts</p>""",
        "order": 6,
    },
]


class Command(BaseCommand):
    help = "Load carnivore + seafood knowledge as a Pillar and Articles in the topics app"

    def add_arguments(self, parser):
        parser.add_argument(
            "--publish",
            action="store_true",
            help="Mark all articles as published immediately",
        )
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing carnivore-diet pillar and all its articles before loading",
        )

    def handle(self, *args, **options):
        if options["reset"]:
            deleted, _ = Pillar.objects.filter(slug="carnivore-diet").delete()
            self.stdout.write(self.style.WARNING(f"Deleted existing carnivore-diet pillar and related data ({deleted} rows)."))

        pillar, created = Pillar.objects.update_or_create(
            slug=PILLAR["slug"],
            defaults={k: v for k, v in PILLAR.items() if k != "slug"},
        )
        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{action} pillar: {pillar.name}"))

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
            f"\nDone. Pillar: '{pillar.name}' | {len(ARTICLES)} articles loaded "
            f"({'published' if publish else 'draft — run with --publish to make live'})."
        ))
