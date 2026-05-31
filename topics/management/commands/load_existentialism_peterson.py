from django.core.management.base import BaseCommand

SLUG = 'existentialism-peterson'
TITLE = 'The Abyss and the Leap: Peterson on Existentialism, the Absurd, and Why You Have to Live the Truth'
SUMMARY = (
    'Existentialism is not a philosophy for comfortable times. It arrives when the old stories '
    'collapse and you are left staring into a void that offers no obvious meaning back. Peterson '
    'draws on Nietzsche, Kierkegaard, and Camus to argue that the only honest response to the '
    'absurd is not resignation but a voluntary leap — a commitment to act as though meaning '
    'exists, not because it can be proven, but because certain truths can only be found by '
    'living them.'
)

CONTENT = '''<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/existentialism-peterson.svg" alt="Figure standing at the edge of a void, reaching upward toward a golden light, with Nietzsche, Kierkegaard, Sartre, Camus fading in and out around him. Two concept panels: The Absurd and The Leap." style="width:100%;border-radius:16px;display:block;">
</figure>

<p>Existentialism begins with a problem that cannot be argued away: the universe does not come labelled with meaning. You are here, conscious, aware that you will die, searching for something that will make the whole thing matter — and the cosmos answers with silence. Peterson's engagement with the existentialist tradition is not academic. He treats it as the most serious intellectual inheritance of the modern world, a body of thought that emerged precisely because the traditional answers stopped working and something more honest was needed.</p>

<h2>The absurd</h2>

<p>"We call out for meaning from a universe that is indifferent to us. This version of the absurd threatens to rob us of our sanity. Here be lions and dragons. Here be cold and dark and emptiness. And that's uncomfortable if we're going to tell ourselves the truth. That search for meaning in a world that doesn't obviously present us meaning is the world that we need to embrace if we're going to live honestly and authentically."</p>

<p>This is Camus's territory — the collision between the human need for meaning and the world's refusal to supply it. Peterson takes the absurd seriously as a psychological and philosophical reality, not a rhetorical position. When the inherited structures that give life meaning — religion, tradition, community — erode or collapse, what remains is a person standing at the edge of something that offers nothing back. The question is what you do next.</p>

<h2>Nietzsche and the death of God</h2>

<p>Nietzsche is the philosopher Peterson returns to most frequently in the existentialist conversation, and the reason is that Nietzsche saw the crisis coming before it arrived. The death of God was not, for Nietzsche, a cause for celebration — it was a diagnosis of catastrophic cultural loss. The structures of meaning that had organised Western life for a thousand years were dissolving, and he understood that what followed would not automatically be better. The abyss opens when the old story ends and no new one has been written yet.</p>

<p>Peterson's reading of Nietzsche is consistent with his broader concern: nihilism — the conclusion that nothing matters — is not a stable resting point. It curdles. It becomes resentment, then contempt, then destruction. The person who stares into the void without any resource for moving through it does not stay neutral. They become bitter toward existence itself. Nietzsche saw this too, which is why he spent his philosophy searching for an answer that did not involve retreating to the old certainties or collapsing into despair.</p>

<h2>Kierkegaard's leap</h2>

<p>The other philosopher Peterson draws on most directly is Kierkegaard — and the concept of the leap of faith. Peterson's framing is vivid: "Think of Kierkegaard's leap of faith from the viewpoint of Juliet. Here comes Romeo with no guarantees. He does not bring an array of lawyers and philosophers to persuade her that it is utterly rational for her to elope with him. He says: leap into my arms. And she does not know whether that will end well or not. It's an act of faith — it's a leap."</p>

<p>The point is not religious in the narrow sense. It is about the structure of the most important human commitments. You cannot wait for proof before you commit to a path, a relationship, a set of values. The proof only becomes available by going in. The person who insists on certainty before they act will never act — and will discover, too late, that the refusal to leap is itself a choice, one that closes off rather than preserves options.</p>

<h2>Truths you have to live</h2>

<p>Peterson's core contribution to the existentialist conversation is the insistence that certain truths are not discoverable by thinking — they require action. "I think that there are some truths that you cannot simply discover. You have to live them. You have to make the experiment."</p>

<p>This is not anti-intellectual. It is a claim about the structure of certain kinds of knowledge. You cannot understand what it means to be a parent by reading about parenting. You cannot understand what commitment does to a person from the outside. You cannot know whether a particular path is worth taking without walking some distance down it. The existentialists were united on this: existence precedes essence, which means you do not arrive with a fixed nature — you make yourself through the choices you make and the life you live.</p>

<h2>The alternative to the leap</h2>

<p>Peterson frames the existential choice with clarity. "You have to make a decision one way or another. You're either going to take the Mephistophelian route — say life is so terrible that it should come to an end, that if there is a God he should be damned for having the presumption to make such a terrible world — or you're going to say: no, despite everything, I'm going to work in all possible ways to make everything better, to tell the truth while moving forward, and I'm going to conduct my life according to those principles and see what happens."</p>

<p>The Mephistophelian route is intellectually coherent. Suffering is real, death is real, the universe is indifferent — you can construct a tight argument for nihilism and resentment. What Peterson observes is that this argument, however logically tight, produces something recognisable and destructive at the human level. The people who take it seriously do not become wiser or more peaceful. They become corrosive.</p>

<h2>The honest response</h2>

<p>The existentialist position that Peterson ultimately endorses is neither naive optimism nor fashionable despair. It is something harder: a voluntary commitment to act as though meaning exists and is worth pursuing, not because the metaphysics are settled, but because the alternative — paralysis or resentment — is clearly worse, and because the commitment itself, lived out, has a way of generating what it was looking for.</p>

<p>"If you're willing to turn around and face the darkness fully, what you discover at the darkest part is the brightest light." This is not a promise about how the world will treat you. It is an observation about what the person who faces their situation honestly, without flinching, and still chooses to move forward — tends to find. Not comfort. Not certainty. But something that functions like meaning, arrived at by living it rather than waiting for it to be handed over.'''


def create_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Pillar = apps.get_model('topics', 'Pillar')

    pillar = Pillar.objects.filter(slug='mindset-success').first()
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
        order=11,
        published=True,
    )


def reverse_article(apps, schema_editor):
    Article = apps.get_model('topics', 'Article')
    Article.objects.filter(slug=SLUG).delete()


class Command(BaseCommand):
    help = 'Load Peterson existentialism article'

    def handle(self, *args, **options):
        from topics.models import Article, Pillar
        pillar = Pillar.objects.filter(slug='mindset-success').first()
        if not pillar:
            self.stderr.write('mindset-success pillar not found')
            return
        if Article.objects.filter(slug=SLUG).exists():
            self.stdout.write('Article already exists')
            return
        Article.objects.create(
            slug=SLUG, title=TITLE, summary=SUMMARY,
            content=CONTENT, pillar=pillar, order=11, published=True,
        )
        self.stdout.write(self.style.SUCCESS(f'Created: {SLUG}'))
