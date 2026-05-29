from django.core.management.base import BaseCommand

SLUG = 'authenticity-attachment-abandoning-self-gabor-mate'
TITLE = 'The Choice That Broke You: Gabor Maté on Why You Abandoned Your Authentic Self'
SUMMARY = (
    'Every child faces a version of the same impossible dilemma: be yourself, or be loved. '
    'When being authentic — expressing anger, fear, sadness, need — triggers rejection or '
    'withdrawal from a parent, the child learns to suppress what is real in order to preserve '
    'the attachment. Gabor Maté traces the emptiness and disconnection adults carry to this '
    'original, unconscious surrender of the self.'
)

CONTENT = '''<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/authenticity-attachment-gabor-mate.svg" alt="Two figures side by side: authentic self glowing with open arms and inner light vs compliant self grey and hollow with strings of attachment pulling from above" style="width:100%;border-radius:16px;display:block;">
</figure>

<p>There is a conflict at the root of most adult suffering that begins before the person can name it, before they even understand they are making a choice. Gabor Maté calls it the tragedy of childhood: the collision between two things a child absolutely needs — attachment and authenticity — when having one threatens the loss of the other.</p>

<h2>Two survival needs</h2>

<p>"A human being has two fundamental needs apart from the physical needs in infancy in childhood," Maté explains. "One is for attachment. But we have another need which is authenticity. Authenticity — auto, self — means being connected to ourselves: just knowing what we feel and being able to act on it."</p>

<p>Attachment is obvious: an infant who is not attached to a caregiver does not survive. But authenticity is equally a survival need — the capacity to know what you are feeling, to trust your internal signals, to act from your genuine state. Without it, a person cannot navigate their own life accurately.</p>

<p>"Both of these are survival needs," Maté says. "But what happens if your authenticity threatens your attachment relationships?"</p>

<h2>The dilemma</h2>

<p>He walks through an example that is so common it becomes almost invisible: "As a two-year-old, you get angry because you can't get that cookie before dinner. But your parents can't handle anger — because they grew up in homes where there was rage-aholism and they're terrified of the very expression of anger. So they give you the message that good little kids don't get angry."</p>

<p>The child does not receive this as: "good little kids don't get angry." They receive it as something far more consequential: "angry little kids don't get loved." Because the parents are now sullen, they won't look at you, they speak harshly — in that moment, love is withdrawn. Not permanently. But for a child, the threat of losing attachment is existential.</p>

<p>"You got to stay attached," Maté says. "Guess what you're going to suppress? The authenticity — every time."</p>

<h2>How we lose ourselves</h2>

<p>The suppression is not a conscious decision. This is the part Maté is most emphatic about: "The repression of emotions that a child engages in is not conscious, is not deliberate — it's an automatic response, it's unconscious." The child does not think: I will stop feeling this to protect my relationship with my mother. The feeling is simply cut off, rerouted, buried before it reaches full expression.</p>

<p>Done once, this is adaptation. Done habitually — as it must be, in homes where emotional expression consistently triggers withdrawal — it becomes character. The child learns, at the deepest level, that their authentic interior life is dangerous. That their real feelings, needs, and reactions cannot be trusted to land safely. That being themselves is a threat to the thing they cannot survive without.</p>

<p>"This is how we lose connection to ourselves and to our gut feelings," Maté says. "That very dynamic which is essential for human survival in a natural setting becomes a threat to our survival in this more modern setting — where to stay authentic is to threaten attachment."</p>

<h2>And then we wonder</h2>

<p>The consequence arrives in adulthood as a mystery: "So we give up our authenticity — and then we wonder who the hell we are. And whose life is this? And who's experiencing all this? And this life doesn't feel like mine. And who am I really?"</p>

<p>This is the inner emptiness. Not an absence of experience, but an absence of felt ownership of experience — the sense of watching your life from behind glass, of going through motions that belong to a role rather than a self. The person is present. The self is not.</p>

<p>Maté describes the central wound succinctly: "The biggest calamity is not what happened to you as a child, but that as a result of what happened, you lost the connection to yourself. That lost connection to yourself will have many potential outcomes — one of which is addiction. It's not the only one, but it certainly is one of the major ones."</p>

<h2>The forms it takes</h2>

<p>The surrender of authenticity to preserve attachment takes different shapes depending on the child's temperament and the specific emotional demands of the household. Some children become chronically agreeable — "yes" people, people-pleasers, those who cannot tolerate conflict because conflict once meant the withdrawal of love. Some become high achievers who work to be needed when being wanted was unreliable. Some become emotionally numb, finding that the fastest way to avoid the unbearable is to stop feeling altogether.</p>

<p>Maté describes his own version: "Why do I become a workaholic later? Because if they don't want me, at least they are going to need me." The strategy makes perfect sense as a child's adaptation. It becomes a problem when it runs the adult life of someone who is no longer a child.</p>

<h2>Separation from essence</h2>

<p>At its most fundamental, Maté frames all of this as separation — not a dramatic rupture, but a slow erosion. "It's always about separation from your essence, from other people, from society, from culture. The reason we suffer is because our true nature cannot be expressed under circumstances that deny our true nature."</p>

<p>"If we were wired for disconnect, we wouldn't suffer when we're disconnected. So it's just the opposite — we're wired for attachment, we're wired for connection, for belonging, for unity. That's our nature. And I think our suffering occurs when our true nature cannot manifest itself."</p>

<h2>The reconnection</h2>

<p>The healing is, in Maté's framing, a reconnection — not to something new, but to what was always there before it was suppressed. "That's where the reconnection has to happen. That's what healing is — reconnection with that."</p>

<p>This is not a comfortable process. The feelings that were suppressed did not disappear — they were held. Reaching them means tolerating what the child could not afford to tolerate, with the resources of an adult who no longer faces the same existential stakes. But it is the only direction in which the authentic self, and the life that belongs to it, can be found.</p>

<p>The tragedy of the original dilemma — be yourself or be loved — is that the child who chose attachment in order to survive eventually becomes an adult who has both, and still cannot find themselves. The choice made sense then. It does not have to govern now.'''


def create_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Pillar = apps.get_model('topics', 'Pillar')

    pillar = Pillar.objects.filter(slug='psychological-origin').first()
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
        order=31,
        published=True,
    )


def reverse_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug=SLUG).delete()


class Command(BaseCommand):
    help = 'Load Gabor Maté authenticity-attachment article'

    def handle(self, *args, **options):
        from topics.models import Article, Pillar
        pillar = Pillar.objects.filter(slug='psychological-origin').first()
        if not pillar:
            self.stderr.write('psychological-origin pillar not found')
            return
        if Article.objects.filter(slug=SLUG).exists():
            self.stdout.write('Article already exists')
            return
        Article.objects.create(
            slug=SLUG, title=TITLE, summary=SUMMARY,
            content=CONTENT, pillar=pillar, order=31, published=True,
        )
        self.stdout.write(self.style.SUCCESS(f'Created: {SLUG}'))
