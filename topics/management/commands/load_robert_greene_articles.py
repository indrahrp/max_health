from django.core.management.base import BaseCommand
from topics.models import Pillar, Article

# ── Article 1: Laws of Human Nature ──────────────────────────────────────────

CONTENT_LOHN = """<p>Robert Greene spent years reading thousands of historical biographies, case studies, and psychological research before writing The Laws of Human Nature. His conclusion was uncomfortable: humans are far less rational, far more self-deceived, and far more driven by primal forces than we like to believe. The book is not cynical — it is diagnostic. You cannot defend yourself against forces you refuse to acknowledge in yourself first.</p>
<p>What follows are the core laws Greene identifies, drawn directly from his talks and lectures.</p>

<h2>We Are All Irrational — Especially When We Think We Are Not</h2>
<blockquote><p>"I write about irrationality, envy, aggression, narcissism. People say, 'Oh, they're a narcissist — I'm not a narcissist, I'm not self-absorbed, but they are.' Well, damn it — every single human being has self-absorption traits. We can't help it. We naturally think of ourselves first."</p></blockquote>
<p>The first and most foundational law is that our emotions hijack our reasoning constantly, and we are the last to notice. Greene calls this the Law of Irrationality. When we feel threatened, envious, or anxious, our thinking narrows. We rationalise what we have already decided emotionally, then present it to ourselves as cool logic.</p>
<p>The antidote is what Greene calls the rational self — not an absence of emotion, but the discipline to pause before reacting, trace the feeling back to its source, and ask whether it is telling you something true or merely something convenient. The irrational move is to trust your first response. The rational move is to distrust it.</p>

<h2>Everyone Has an Inflated Self-Opinion</h2>
<blockquote><p>"One law of human nature is that we humans have what I call a self-opinion — an opinion about ourselves. And people who have done studies have shown that that opinion is generally more elevated than the reality. We tend to think of ourselves as intelligent — at least in our field. We like to think of ourselves as autonomous, that we just make our own decisions."</p></blockquote>
<p>The gap between how people see themselves and how they actually are is one of the most documented findings in psychology. Greene uses it to explain why feedback feels like attack, why people resist learning from failure, and why so many careers plateau — the person believes they have already arrived.</p>
<p>The practical implication: when dealing with others, never directly assault their self-opinion. You will create an enemy. Instead, find ways to help them see reality while preserving their dignity. And when dealing with yourself, actively seek out evidence that contradicts your self-image. That is the information most worth having.</p>

<h2>You Have a Shadow — and It Controls You If You Ignore It</h2>
<blockquote><p>"Everybody has a dark side. I don't care if you're Mahatma Gandhi — you have a dark side. It comes out in ways you're not even aware of. The idea was: you need to understand your dark side, confront it, and make it work for you. I had to come to terms with my irrationality, my grandiosity, my aggressive instincts. But it's the only way to change yourself — to be aware that you have these issues."</p></blockquote>
<p>Carl Jung called it the shadow — the part of our personality we refuse to acknowledge and so push underground. Greene's contribution is showing how the shadow expresses itself in daily life: the person who is aggressively anti-conflict who secretly seethes with resentment; the political crusader who is driven by unacknowledged envy; the generous benefactor who needs control.</p>
<p>Repressing the shadow does not make it disappear. It makes it stronger and more unpredictable. Greene's instruction is to do the uncomfortable work of examining what you most deny about yourself — and then integrate it consciously, direct it, use it. The shadow contains energy. The question is whether you control it or it controls you.</p>

<h2>Envy Is Everywhere, Hidden Under Other Names</h2>
<blockquote><p>"We attracted to it because we envy people who have that kind of confidence. We wish we could have that, and we find it very compelling. We want to know them — we think that some of it, perhaps, will rub off on us."</p></blockquote>
<p>Envy is the emotion people are least willing to name in themselves. It masquerades as moral indignation ("they don't deserve it"), concern ("I just worry about them"), or criticism ("their work isn't really that good"). Greene argues that recognising envy — especially your own — is one of the most clarifying things you can do.</p>
<p>The person who triggers your envy is showing you what you actually want. That is valuable information. The person whose envy you trigger is dangerous — they will work against you while smiling. Greene's practical advice: never flaunt your advantages in front of people who don't have them. And when you feel that corrosive, contracting feeling toward someone else's success, name it honestly. The name takes some of its power away.</p>

<h2>We Are Tribal Animals — and Our Tribe Distorts Our Thinking</h2>
<blockquote><p>"What leads to extreme tribalism is scapegoating. Our minds are so narrow and constricted right now — I'm hoping that young people particularly, the generation coming up, are going to create something new, are going to see beyond it."</p></blockquote>
<p>Human beings evolved in small groups and carry that wiring intact. We instinctively sort the world into us and them, then unconsciously distort information to confirm whatever our group believes. The tribal mind sees nuance as betrayal and complexity as weakness.</p>
<p>Greene's advice is to deliberately cultivate relationships and information sources outside your natural tribe — not to be contrarian, but to retain the ability to think. The most dangerous leaders throughout history have been those who successfully activated tribal feeling and directed it. Understanding the mechanism is the first line of defence against being used by it.</p>

<h2>People Wear Masks — Learn to Read What's Underneath</h2>
<blockquote><p>"To get along with people you have to play a role, you have to wear a mask, and you have to be good at that. Really successful artists — people who are also massively creative — learn how to play that game to some extent. It's a myth that you can just be completely authentic all the time."</p></blockquote>
<p>Greene is not endorsing dishonesty — he is describing reality. Everyone performs. Everyone manages their presentation. The question is whether you are doing it consciously and effectively, or unconsciously and poorly.</p>
<p>The skill Greene emphasises is reading past masks — noticing the gap between what people say and how they behave, paying attention to body language and microexpressions, watching patterns over time rather than reacting to single moments. People reveal themselves gradually and involuntarily. The patient observer learns more than the eager questioner.</p>

<h2>We Are All Shortsighted — We Overvalue the Present</h2>
<p>One of Greene's most practically useful observations is what he calls the Law of Shortsightedness: humans consistently overweight immediate rewards and underweight long-term consequences. The diet abandoned after a hard day. The investment missed because it required waiting. The relationship sacrificed for a moment's satisfaction.</p>
<p>The antidote is deliberate long-term thinking — asking not just "what does this get me now?" but "where does this path lead in five years?" Greene draws on military strategy, chess, and business history to make the same point: the actor who thinks three moves ahead almost always defeats the one thinking one move ahead, even if the latter is more intelligent or better resourced.</p>

<h2>The Law of Death Denial</h2>
<blockquote><p>"The last chapter of the book — chapter 18 — is the law of death denial. Greene delves into the human tendency to deny or avoid the reality of death. He explores how this denial shapes our behaviour, influences our decisions, and impacts our psychological wellbeing."</p></blockquote>
<p>Greene ends The Laws of Human Nature with what he considers the most fundamental human irrationality: we know we will die, and we spend enormous energy not thinking about it. This denial warps our priorities — we pursue status, comfort, and distractions rather than meaning, because meaning requires confronting what actually matters before time runs out.</p>
<p>Greene's instruction, drawing on the Stoics and on his own experience with a serious stroke, is to use the awareness of death as a clarifying lens. Ask: if I knew I had a limited time, would I still be doing this? The people and work that survive that question are what your life should be built around. Everything else is noise.</p>

<h2>What the Laws Add Up To</h2>
<p>Greene's project across The Laws of Human Nature is not to make you cynical about people — it is to make you accurate. The person who understands these forces in themselves is harder to manipulate, more effective in their relationships, and more honest about their own motivations. The person who ignores them is the easiest target in every room.</p>
<p>Self-knowledge, in Greene's framework, is not a luxury. It is the most practical skill there is.</p>"""

# ── Article 2: Mastery ────────────────────────────────────────────────────────

CONTENT_MASTERY = """<p>Robert Greene spent years studying the lives of masters — Leonardo da Vinci, Mozart, Charles Darwin, Benjamin Franklin, John Coltrane — searching for what they had in common. His finding was counterintuitive: mastery is not a gift. It is a process. A specific, learnable, replicable process that any person of normal intelligence can follow, given enough time and the right orientation.</p>

<h2>The Primal Inclination: Your Unique Starting Point</h2>
<blockquote><p>"These primal inclinations exist in every single individual — they're like a genetic marker. This is what makes you unique. Our culture thrives on people who mine this uniqueness and become highly creative. I believe there's actually a purpose for this uniqueness."</p></blockquote>
<p>Every person is born wired differently. Greene calls this the primal inclination — the deep, pre-verbal pull toward certain kinds of problems, materials, or activities that shows itself in childhood before social conditioning has fully taken hold. The child who takes apart every machine in the house. The one who obsessively draws, or who memorises every statistic about a sport, or who cannot stop asking why.</p>
<p>Most people lose contact with this signal. School, family pressure, and the demand to be practical route them away from it. Greene argues this is a catastrophic error. The primal inclination is not mere preference — it is the direction your nervous system is optimised to develop in. Working against it means fighting your own biology. Working with it means everything is easier.</p>

<h2>The Apprenticeship Phase: The Price of Mastery</h2>
<blockquote><p>"It begins with an apprenticeship — and before you start the path, people are disillusioned about how long it takes to experience that embodied sense of mastery. We want it now. We look at others and say, 'They must have been born that way.' We know at some level that we need to put in work — but a definite process leads to the 10,000 hours, the 20,000 hours, and a genuine change in level of thinking and consciousness which I would call mastery."</p></blockquote>
<p>The apprenticeship phase typically spans five to ten years. Greene draws on historical evidence and contemporary research to show that there are no exceptions to this timeline — not Mozart, not Tiger Woods, not any of the figures we call prodigies. What looks like natural talent is almost always early, intense, disciplined practice that we have simply been told was effortless.</p>
<p>The apprenticeship has three components: deep observation (watching how the field actually works before trying to change it), skill acquisition through repetition and feedback, and the development of what Greene calls the self-directed apprentice's mindset — treating every setback as information and every tedious task as an essential building block rather than an obstacle.</p>

<h2>The Mentor: Accelerating the Path</h2>
<blockquote><p>"I didn't really have a mentor growing up — I was pretty much left to my own. But I had writers and philosophers and thinkers and novelists that I gravitated to, who taught me a lot, who basically raised me."</p></blockquote>
<p>The mentor relationship is Greene's most powerful accelerant. A great mentor compresses decades of learning into years by transmitting not just skills but the tacit knowledge embedded in a field — the unwritten rules, the mistakes worth avoiding, the subtle patterns that take a lifetime to accumulate independently.</p>
<p>Greene's advice on mentors is practical: choose them for the depth of their knowledge, not the prestige of their name. Make yourself valuable to them — don't just take. Observe how they think, not just what they produce. And know when to leave: the apprentice who stays too long in a mentor's shadow develops competence without originality.</p>

<h2>The Creative Active Phase: Where You Become Yourself</h2>
<blockquote><p>"You enter what I call the creative active phase — which could be anywhere from after 10 years of apprenticeship or a little bit less. In that phase you start taking the knowledge you've accumulated and experimenting with it, trying things out, starting your own project, and bringing that individual, unique quality that you have into play — which was sort of lying dormant."</p></blockquote>
<p>After the apprenticeship comes the creative active phase. You stop imitating and start synthesising. The deep skills become internals — automatic, below the level of conscious thought — and the creative mind is freed to experiment with them. This is the phase where originality emerges, where you start making connections no one has made before, where the work begins to feel like yours.</p>
<p>Greene is careful to note that this phase requires a willingness to look foolish. You will try things that fail. You will make work that is not yet as good as your ambition. The people who reach mastery are those who absorb these failures as data and continue experimenting. The people who stop here are those who found a formula that worked adequately and never moved beyond it.</p>

<h2>High-Level Intuition: What Mastery Actually Feels Like</h2>
<blockquote><p>"I ended up calling it high-level intuition — and it intrigued me. Nobody really writes a book about this. It's almost as if it doesn't exist. Words are — it's impossible to sort of explain or describe. I wanted to really explain and describe it."</p></blockquote>
<p>At the summit of the process is what Greene calls mastery itself — a state of mind where the practitioner perceives the field with a richness and depth unavailable to beginners. The chess grandmaster who sees twenty moves ahead is not calculating consciously — they are pattern-recognising at a level built through decades of absorbed experience. The master surgeon who detects what is wrong before the scan confirms it. The master writer who feels the wrong word before they can articulate why.</p>
<p>Greene argues that this intuition is not mystical. It is the accumulated pattern library of thousands of hours made available instantly, below the threshold of deliberate thought. It cannot be shortcut. It can only be earned.</p>

<h2>Finding Your Vocation: The Question Mastery Starts With</h2>
<blockquote><p>"When you're in your vocation, you're passionate about it, you love what you're doing — and so you're going to naturally be more inclined to be great at it, because you're going to put way more energy, way more passion into it. Think about the people who have achieved greatness in any field."</p></blockquote>
<p>The word vocation comes from the Latin for calling. Greene takes it literally: the path to mastery begins with identifying what you are actually called to do — not what pays well, not what your parents approved of, not what seems prestigious, but what your own nature is pulling you toward.</p>
<p>This is the most difficult step for most people, because culture teaches us to distrust what we love. Greene's evidence from hundreds of masters' lives shows the opposite: love is not a distraction from serious work. It is the energy that makes serious work possible. The person who hates what they are doing will never outwork the person who loves it — because the one who loves it works when no one is watching, works through failure, works for its own sake.</p>

<h2>What the Book Is Really About</h2>
<p>Mastery is not a book about shortcuts. It is a book about the long game — and about why the long game is worth playing. Greene's argument is that the person who finds their calling, submits to the apprenticeship, works with great mentors, and sustains creative experimentation through failure will eventually develop something no amount of intelligence or luck can replicate: a mind shaped by decades of deep engagement with a field they love.</p>
<p>That mind perceives the world differently. It solves problems others cannot even see. It creates work that lasts. And the path to it — though long — is the most reliable one available to any human being who is willing to take it.</p>"""

# ── Article 3: The Art of Seduction ──────────────────────────────────────────

CONTENT_SEDUCTION = """<p>Robert Greene wrote The Art of Seduction because he believed seduction was being completely misunderstood — reduced to pickup tactics and physical technique when it is actually a comprehensive theory of human desire, attention, and influence. The book draws on history's greatest seducers, from Cleopatra to Casanova to Marilyn Monroe, to extract the principles that made them so difficult to resist.</p>
<p>Greene's central claim: seduction is not manipulation. It is the art of making people feel something they want to feel — and giving them an experience of life that their ordinary reality doesn't provide.</p>

<h2>Seduction Is About Pleasure — Not Appearance</h2>
<blockquote><p>"The weakness that we all have is that we don't have enough pleasure and things that raise us out of the finalities of everyday life. If you're a man or a woman and you know how to give people a taste of that pleasure and get them eating out of your hand — you are a master seducer or seductress."</p></blockquote>
<p>Greene's first and most important observation is that seduction works not by targeting someone's desires but by targeting their deprivations. What are they not getting enough of in their daily life? Excitement? Genuine attention? The feeling of being deeply understood? Adventure? The seducer becomes the source of whatever that missing thing is.</p>
<p>This is why physical attractiveness, though helpful, is not the core of seduction. History's most compelling seducers were frequently unremarkable in appearance. What they offered was an experience — a feeling of being fully alive — that their targets could not find elsewhere.</p>

<h2>The Seductive Character: You Either Have It or You Build It</h2>
<blockquote><p>"The source of your power — I don't care who you are or wherever you grew up — is being different from other people. If you have a skill that makes you different and unique, then you have power, because you can't be replaced."</p></blockquote>
<p>Greene identifies several seductive character types across the book — the Siren, the Rake, the Ideal Lover, the Dandy, the Coquette, the Charmer, the Charismatic, the Star. Each works through a different mechanism. The Siren amplifies sexuality and danger. The Rake offers total, unconditional desire. The Ideal Lover mirrors back to the target their own idealised self-image. The Coquette creates desire through calculated withdrawal.</p>
<p>What they share is distinctiveness. The seductive character is never interchangeable with the crowd. They carry something specific, something that cannot be easily found elsewhere, something that creates a sense of scarcity. Greene's practical instruction: identify and amplify what is most genuinely unusual about you, rather than trying to conform to a generic template of attractiveness.</p>

<h2>Charisma: The Energy That Reads Before You Speak</h2>
<blockquote><p>"It's this energy of self-belief, of confidence, of wanting people to like them. It's the kind of power that Marilyn Monroe had before the camera — and it's extremely powerful. You can read it in people. So it's very important for a political figure or an actor or somebody in the public eye to have that quality."</p></blockquote>
<p>Charisma in Greene's framework is not charm or likability — it is a quality of presence that reads as power. It comes from deep self-belief, from the sense that the person is fully inhabiting themselves rather than performing for approval. Monroe had it not because of how she looked but because of how she related to the camera — as if she were fully, comfortably herself, and slightly amused by the attention.</p>
<p>Greene's most important insight about charisma: insecurity is anti-seductive and readable before a word is spoken. The body language of someone seeking approval — the slight forward lean, the excessive smiling, the anxious laughter — communicates need rather than abundance. The seductive energy is the opposite: self-contained, interested but not desperate, comfortable in silence.</p>

<h2>Mystery: Never Let Them Know Everything</h2>
<blockquote><p>"You can't be completely yourself, because there's no mystery involved. There's no interest. There's no spark going on. You have to create a little bit of mystery. The person can't know exactly who you are. If you just tell them everything about yourself and give them everything on social media — they know everything about you. There's no imagination involved."</p></blockquote>
<p>One of Greene's most practically applicable principles is the maintenance of mystery. Desire lives in the gap between what is known and what is not — in the imagination of the other person, working to complete the picture. The moment that gap closes, desire fades. This is why total transparency, however emotionally honest, is seductively destructive.</p>
<p>The practical implication is counterintuitive: withhold. Not information strategically designed to deceive, but the sense of completeness. Leave things unsaid. Suggest more than you reveal. Let the other person's imagination do the work — their imagination will always build something more compelling than the reality you could offer, because it is calibrated to exactly what they want.</p>

<h2>Absence: The Most Underused Seductive Tool</h2>
<blockquote><p>"It takes time, and it takes some absence — the ability to say you're not in their face all the time. You disappear for a couple of days. You let them think about you. You let that spell work — because seduction and love is kind of a spell that you're casting."</p></blockquote>
<p>Constant availability destroys seductive tension. When someone can have you whenever they want, they stop wanting you. Greene draws on the Coquette type — historically, the most reliably successful seducers — who understood that presence must be rationed to remain powerful.</p>
<p>This is not game-playing. It is the management of desire's psychology. Longing is only possible in absence. The person who is always available gives nothing for the mind to work on. The person who disappears gives the other person's imagination two days to run — and imagination is always more vivid than reality.</p>

<h2>Reading the Target: Desire Hides in Weakness</h2>
<blockquote><p>"Her weaknesses and her vulnerability — what she's missing. If you touch upon a subject and you see that they get nervous, or they laugh a lot, or there's some kind of reaction — that tells you so much. Start taking note of that."</p></blockquote>
<p>Greene's most practically useful seduction principle is also his most psychologically penetrating: desire is produced by lack. The person who seems to need nothing is seductively inert. The person whose vulnerabilities, fantasies, and longings you can identify — and address — holds your complete attention.</p>
<p>The great seducers were skilled interviewers. They listened more than they spoke. They paid attention to what made the target animated, what made them nervous, what they seemed to want most and had least. Then they positioned themselves as the answer to that need. Not manipulatively — seduction at its best is a genuine offer: I can give you what you are missing.</p>

<h2>The Long Game: Seduction Versus Conquest</h2>
<blockquote><p>"I'm more about the long-term — how you can take that woman, or it can be a woman seducing a man, and play a mind game so that in the course of three months she doesn't want to just sleep with you — she wants to give you everything she has."</p></blockquote>
<p>Greene distinguishes sharply between seduction and conquest. Conquest is about getting something. Seduction is about creating a state of mind. The conqueror wins and moves on. The seducer transforms how the target experiences the world — and themselves. The difference is time, patience, and genuine attention to the other person as a full human being.</p>
<p>The long-game seducer is not in a hurry. They are building something — an atmosphere, a set of associations, a narrative in the target's mind in which the seducer becomes central to their experience of life. This takes months, not evenings. But what it produces is qualitatively different from anything a faster approach can achieve.</p>

<h2>What the Book Is Really Teaching</h2>
<p>The Art of Seduction is not a book about manipulation. At its core, it is a book about attention — the quality and depth of the attention you pay to other people, and the power that comes from truly seeing what someone wants and genuinely offering it.</p>
<p>Greene's deepest observation is that most people are lonely in a specific way: they are not truly seen. They perform a version of themselves and receive back a generic response. The seducer breaks this pattern by offering the rarest of all social goods — the feeling of being fully noticed, fully interesting, fully desired. That feeling, Greene argues, is irresistible. It always has been.</p>"""

# ── Command ───────────────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Load three Robert Greene articles (Laws of Human Nature, Mastery, Art of Seduction) into mindset-success pillar"

    def handle(self, *args, **options):
        pillar = Pillar.objects.get(slug="mindset-success")

        articles = [
            {
                "slug": "robert-greene-laws-of-human-nature",
                "title": "Robert Greene's Laws of Human Nature: Why People Do What They Do",
                "summary": (
                    "Greene spent years studying history's most consequential figures to map the hidden forces "
                    "that drive human behaviour — irrationality, envy, the shadow, tribal thinking, and the denial "
                    "of death. The book is not cynical. It is diagnostic. You cannot defend against forces you "
                    "refuse to see in yourself."
                ),
                "content": CONTENT_LOHN,
                "order": 3,
                "ai_summary": (
                    "Covers the 18 laws: irrationality, self-opinion, shadow/dark side, envy, tribalism, "
                    "role-playing and masks, shortsightedness, and death denial. Based on Greene's lectures "
                    "and interviews about the book."
                ),
            },
            {
                "slug": "robert-greene-mastery",
                "title": "Robert Greene on Mastery: The Path Every Master Has Followed",
                "summary": (
                    "Greene studied hundreds of masters — Leonardo, Darwin, Coltrane, Franklin — and found the "
                    "same process in all of them. Mastery is not a gift. It is a specific, learnable sequence: "
                    "primal inclination, apprenticeship, mentorship, creative experimentation, and the "
                    "high-level intuition that emerges from decades of deep work."
                ),
                "content": CONTENT_MASTERY,
                "order": 4,
                "ai_summary": (
                    "Covers the five phases of mastery: finding your primal inclination/life task, the "
                    "apprenticeship phase (5-10 years, 10,000+ hours), working with mentors, the creative active "
                    "phase, and mastery-level intuition. Drawn from Greene's lectures and interviews."
                ),
            },
            {
                "slug": "robert-greene-art-of-seduction",
                "title": "Robert Greene's Art of Seduction: The Psychology of Desire and Influence",
                "summary": (
                    "Greene studied history's greatest seducers — Cleopatra, Casanova, Marilyn Monroe — to find "
                    "what made them irresistible. The answer was never looks. It was a deep understanding of what "
                    "people lack, a mastery of mystery and absence, and the rare ability to make another person "
                    "feel fully seen."
                ),
                "content": CONTENT_SEDUCTION,
                "order": 5,
                "ai_summary": (
                    "Covers seductive character types, charisma as self-belief, mystery and withholding, "
                    "the power of absence, reading vulnerability/desire, the long game vs conquest, and "
                    "the psychology of attention. Based on Greene's lectures and interviews about the book."
                ),
            },
        ]

        for data in articles:
            article, created = Article.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "title": data["title"],
                    "summary": data["summary"],
                    "content": data["content"],
                    "pillar": pillar,
                    "order": data["order"],
                    "published": True,
                    "ai_summary": data["ai_summary"],
                },
            )
            self.stdout.write(f"{'Created' if created else 'Updated'}: {article.title}")

        self.stdout.write(self.style.SUCCESS("Done."))
