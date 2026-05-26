from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

ARTICLE_CONTENT = """<p>Jordan Peterson spent decades as a clinical psychologist watching people wreck their lives through the same recurring failures — dishonesty, aimlessness, resentment, the refusal to take responsibility. The 12 Rules for Life, drawn from his lectures and clinical practice, are not motivational slogans. They are observations about what actually works, assembled from evolutionary biology, Jungian psychology, ancient mythology, and thousands of hours in the therapy room.</p>
<p>Each rule is a compression of something much larger. What follows is the distilled version — the core of what Peterson says and why it matters.</p>

<h2>Rule 1 — Stand Up Straight with Your Shoulders Back</h2>
<blockquote><p>"The first rule is stand up straight with your shoulders back — and it's really a description of the ancient nature of hierarchies, their almost universal existence among living creatures, and the fact that you have extraordinarily ancient and profound neurological systems that govern your psyche — that process hierarchical information."</p></blockquote>
<p>Peterson opens with lobsters. It is not a joke. Lobsters and humans share a serotonin-based dominance system that is over 350 million years old. When you slump, fold your arms, and avoid eye contact, your nervous system reads that as defeat — and floods you with cortisol, making everything harder. When you stand straight, the same system registers confidence and floods you with serotonin, making competence more likely.</p>
<p>The rule is not about vanity. It is about the fact that your physiology shapes your psychology in real time. How you carry your body tells the world, and your own nervous system, where you stand. Adopt the posture of someone who has somewhere to be and something to say — even before you feel it. The neurochemistry follows.</p>

<h2>Rule 2 — Treat Yourself Like Someone You Are Responsible for Helping</h2>
<blockquote><p>"If your best friend had this concern — how would I treat her? Well, treat yourself that way. There are narcissists who are selfish and then there are agreeable people who are like reverse narcissists. Everyone else comes first. And there is being selfish in the self-centred way — that's not good. But taking advantage of yourself counterproductively and becoming bitter and resentful in the service of others is no virtue either."</p></blockquote>
<p>People are worse at looking after themselves than they are at looking after others. Peterson documents this in clinical practice: people prescribed medication by a physician will follow the instructions carefully for their dog but skip doses for themselves. The self-contempt is often invisible — it masquerades as selflessness.</p>
<p>This rule is not licence for selfishness. It is an instruction to extend the same basic care to yourself that you would extend, without hesitation, to someone else you loved. You are a being of value. Neglecting yourself is not noble — it is a slow corruption that eventually poisons everything around you.</p>

<h2>Rule 3 — Make Friends with People Who Want the Best for You</h2>
<blockquote><p>"The point is not to have peace in your life and surround yourself with people who like you and to have non-disagreeable conversations. Unless you have sanctified suffering in your life, you will not become strong. You will not learn."</p></blockquote>
<p>Bad company is not neutral — it is actively destructive. If the people around you are going nowhere, resent ambition, and celebrate failure, they will pull you down to their level and call it loyalty. Peterson is blunt: the people who encourage your worst tendencies are not your friends.</p>
<p>Real friendship requires that someone care enough to tell you when you are making a mistake. Real community requires that the people around you be genuinely invested in your growth. Choose your associates the way you would choose a business partner — on the basis of whether they make you more capable and honest, not merely more comfortable.</p>

<h2>Rule 4 — Compare Yourself to Who You Were Yesterday, Not to Who Someone Else Is Today</h2>
<blockquote><p>"Compare yourself to who you were yesterday and not to who someone else is today. The idea is your best measure is your previous self, and you should try for incremental improvement at the rate you can manage. You should recognise that incremental improvement in yourself and you should reward it — and you shouldn't denigrate it because it isn't a giant leap."</p></blockquote>
<p>The internet has made comparison pathological. You can now benchmark yourself, in real time, against the most successful person on earth in any domain. This is a recipe for paralysis and contempt. Someone will always be further ahead. That comparison tells you nothing useful about what you should do next.</p>
<p>Your competition is your past self. The question is not "am I better than them?" but "am I better than I was yesterday?" That is a question you can actually answer, and act on. Tiny daily improvements, compounded across years, produce transformations that dwarf the results of intermittent heroic effort.</p>

<h2>Rule 5 — Do Not Let Your Children Do Anything That Makes You Dislike Them</h2>
<blockquote><p>"If you learn to do it right — if you hold them close, but also make them strong — there won't be anything you'd rather do. A well-disciplined child who accompanies you playfully is a very rare and precious thing."</p></blockquote>
<p>This rule is often misread as harsh. It is the opposite. The point is that parents who allow their children to behave badly — through excessive permissiveness, through the refusal to set limits out of misplaced guilt — are not protecting them. They are failing to prepare them for a world that will not be similarly lenient.</p>
<p>Children need constraints to develop self-regulation. A child who has learned that their impulses must be managed, that others must be considered, that there are consequences to behaviour — that child is ready to function in society. A child who has never been told no is not free. They are unprepared.</p>

<h2>Rule 6 — Set Your House in Perfect Order Before You Criticise the World</h2>
<blockquote><p>"If you were willing to maybe clean your room — wouldn't that be something to do? You could start by straightening out what you can straighten out. And you saw on the tour repeatedly the fact that that worked for so many people."</p></blockquote>
<p>Before you fix society, fix your room. Before you fix your room, fix yourself. This is not a call for passivity or indifference to injustice. It is a call for epistemic humility. Most people who are loudest about the failures of the world have not done the hard, unsexy work of getting their own life in order.</p>
<p>Peterson is not saying the world is fine. He is saying that the person who has not managed their own chaos — their finances, their relationships, their habits, their integrity — is not well positioned to redesign civilisation. Start with what is in front of you. Then expand outward from there. You will be surprised how much changes.</p>

<h2>Rule 7 — Pursue What Is Meaningful, Not What Is Expedient</h2>
<blockquote><p>"Pursue what is meaningful, not what is expedient — this is a great thing to know. Expedient might be: we're going to have a conversation and I want something from you. A lot of conversations are like that — you have a goal in mind, this is what I want from this person, and so you talk instrumentally."</p></blockquote>
<p>Expedience is taking the easy path: lying to avoid conflict, choosing the comfortable job over the challenging one, performing kindness for approval rather than giving it out of genuine care. Meaning is harder. It requires sacrifice — the willingness to give up something now in service of something worth having later.</p>
<p>Peterson draws on Carl Jung and the world's mythological traditions to make this point: the universal hero story is about voluntarily taking on a burden, walking into the unknown, facing the thing that frightens you. Meaning emerges from that voluntary confrontation with difficulty. It cannot be obtained by avoiding it.</p>

<h2>Rule 8 — Tell the Truth — Or, at Least, Don't Lie</h2>
<blockquote><p>"If you tell the truth — this could literally be the case — the way you have the adventure that justifies your life is by telling the truth. If you're not telling the truth, then it isn't you having the adventure. It isn't you getting hammered. It isn't you getting better. It isn't you."</p></blockquote>
<p>Lying is not merely a moral failure. It is a practical catastrophe. Every lie requires a network of further lies to sustain it. Every small untruth distorts your map of reality a little further, making it harder to navigate the world accurately. Over time, the liar loses contact with reality itself.</p>
<p>The instruction starts with the negative: at minimum, stop lying. You may not yet know the whole truth, and you may not always be able to say it — but you can stop saying what you know to be false. That alone will change everything. The person who has stopped lying discovers, over time, a clarity about themselves and the world that liars can never access.</p>

<h2>Rule 9 — Assume That the Person You Are Listening to Might Know Something You Don't</h2>
<blockquote><p>"You should listen to people because they might know something more than you do. It's also incumbent on educators to set the motivational frame — to actually explain why what they're teaching is important, not just present it as decoration."</p></blockquote>
<p>Most people do not listen — they wait for their turn to speak. The conversation is an opportunity to confirm what they already believe, not to encounter anything genuinely new. This is a waste of the most efficient learning mechanism available to a human being.</p>
<p>Real listening is an act of humility. It requires you to hold in suspension the possibility that the person in front of you knows something you do not. It requires you to follow a thread even when it contradicts what you expected. The person who has learned to listen well is not just more socially effective — they are genuinely more intelligent, because they have access to information that the non-listener never receives.</p>

<h2>Rule 10 — Be Precise in Your Speech</h2>
<blockquote><p>"Be precise in your speech — and I'm going to weave that together with the question of meaning into something like a general theory of meaning. That's really what I've been working on for 35 years."</p></blockquote>
<p>Vagueness is cowardice. When you leave what you mean imprecise, you leave yourself room to retreat — to deny that you said what you said, to blame others for misunderstanding you, to avoid accountability for your own position. Vagueness in speech is usually preceded by, and produces, vagueness in thought.</p>
<p>When you force yourself to say exactly what you mean, you are forced to know exactly what you mean. That is uncomfortable because it makes you responsible for your own position. It also makes you effective. People who know precisely what they want, and can say it clearly, get it far more often than those who communicate in euphemism and approximation.</p>

<h2>Rule 11 — Do Not Bother Children When They Are Skateboarding</h2>
<blockquote><p>"There won't be anything you'd rather do — a child who is well-disciplined and playfully accompanying you through the world is a rare and precious thing. But the children who are never allowed to take risks — who are perpetually protected from consequence — grow up unable to function."</p></blockquote>
<p>Children skateboard because it is dangerous. The danger is the point. They are developing competence, testing limits, learning to fall and get up, discovering what their bodies can do. The parent or authority figure who stops them — in the name of safety — is not protecting them. They are depriving them of the very experiences that build genuine capability and self-confidence.</p>
<p>This rule extends beyond children. It is an argument against the compulsive need to remove risk from human experience. Challenge, difficulty, and the possibility of failure are not bugs in the design of a meaningful life. They are the mechanism by which growth happens. The sanitised life, the life from which all danger has been carefully removed, is not a safe life. It is an empty one.</p>

<h2>Rule 12 — Pet a Cat When You Encounter One on the Street</h2>
<blockquote><p>"Rule 12 is pet a cat when you encounter one on the street — and it's oddly enough a meditation on fragility. It's a discussion of what you do when you don't know what to do — when things have gone badly for you, when you face a terrible tragedy in your own personal life or in your familial life."</p></blockquote>
<p>This is the rule that people misunderstand most, because it sounds trivial. It is not trivial. It is a rule about how to live in the presence of suffering — about what you do when the weight of existence becomes genuinely hard to bear.</p>
<p>You cannot fix everything. Some tragedies are real and permanent. Some losses cannot be undone. In those moments, Peterson's counsel is to notice the small things — the cat in the street, the afternoon light, the conversation with a friend — and receive them. Not because they solve the problem, but because they are real, and present, and good. The capacity to notice small beauty in the midst of suffering is not escapism. It is the thing that makes continued engagement with life possible.</p>

<h2>What the Rules Add Up To</h2>
<p>Taken together, the 12 Rules are a theory of how to build a life that can bear its own weight. The common thread is responsibility — the willingness to take ownership of yourself, your choices, your relationships, and your effect on the world. Not as a burden, but as the precondition for meaning.</p>
<p>Peterson draws on the same insight that the great philosophical and religious traditions have always converged on: the meaningful life is not found by avoiding difficulty, but by voluntarily taking it on. You become what you repeatedly do. You get what you repeatedly choose. The question is only whether you are choosing consciously — or whether you are letting the chaos choose for you.</p>"""


class Command(BaseCommand):
    help = "Load Jordan Peterson 12 Rules for Life article into mindset-success pillar"

    def handle(self, *args, **options):
        pillar = Pillar.objects.get(slug="mindset-success")

        article, created = Article.objects.update_or_create(
            slug="jordan-peterson-12-rules-for-life",
            defaults={
                "title": "Jordan Peterson's 12 Rules for Life — The Complete Breakdown",
                "summary": (
                    "Peterson spent decades watching people wreck their lives through the same recurring failures. "
                    "The 12 Rules — drawn from evolutionary biology, Jungian psychology, and thousands of hours in "
                    "the therapy room — are not motivational slogans. They are observations about what actually works."
                ),
                "content": ARTICLE_CONTENT,
                "pillar": pillar,
                "order": 2,
                "published": True,
                "ai_summary": (
                    "Covers all 12 rules with quotes from Peterson's lectures: stand up straight (serotonin hierarchies), "
                    "treat yourself responsibly, choose good friends, compare yourself to yesterday's self, discipline children, "
                    "clean your room, pursue meaning not expedience, tell the truth, listen, be precise, allow risk, "
                    "and notice small beauty amid suffering."
                ),
            },
        )
        self.stdout.write(f"{'Created' if created else 'Updated'} article: {article.title}")
        self.stdout.write(self.style.SUCCESS("Done."))
