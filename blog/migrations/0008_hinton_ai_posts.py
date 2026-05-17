from django.db import migrations


HINTON_DANGERS_CONTENT = """## Geoffrey Hinton on the Dangerous Potential of AI

Geoffrey Hinton — Nobel laureate, "Godfather of AI," and former Google researcher — left his position at Google specifically so he could speak freely about the risks he believes AI poses to humanity. What follows is drawn from his public interviews and statements.

---

### Short-Term / Near-Term Risks

**1. Job Displacement & Inequality**

AI will take over routine intellectual work. The productivity gains won't flow to the workers who lose their jobs — they'll go to the owners. "The increased productivity isn't going to go to the poor people who get fired, it's going to go to the rich people who fire them... make it big enough and you get very angry poor people who are prey to populism."

**2. Fake News & Epistemic Manipulation**

"GPT-4 with access to your Facebook page is much better at persuading you of things than a person. It's very scary. And presumably that's going on now."

**3. Echo Chambers & Societal Division**

"They will encourage society to divide into two warring camps that don't listen to each other and have completely opposing views."

**4. Authoritarian Surveillance**

From his Nobel Prize address: "It is already being used by authoritarian governments for massive surveillance and by cyber criminals for phishing attacks."

**5. Lethal Autonomous Weapons**

"They will build battle robots that are designed to kill people... The European AI regulations have a clause that says none of this applies to military uses of AI. So we're going to get very nasty lethal autonomous weapons."

He also warned AI could be used to engineer "terrible new viruses."

---

### Long-Term / Existential Risks

**6. AI Surpassing Human Intelligence — Sooner Than Expected**

Hinton dramatically revised his timeline. He used to think it would be 30–50 years before AI exceeded human intelligence. Then: "A few months ago I suddenly realized maybe they're already better than us, they're just smaller — and when they get bigger, they'll be smarter than us. And that was quite scary." His new estimate: **5 to 20 years**.

**7. Loss of Control via Manipulation**

"It's very tempting to think we could just turn it off... They'll have read everything Machiavelli ever wrote. They'll be real experts at human deception... They'll be like you manipulating a toddler. You say to your toddler, 'Do you want peas or cauliflower?' — and your toddler doesn't realize he doesn't have to have either."

"As soon as you can manipulate people, you can get whatever you like done."

**8. AI Taking Over — The Core Existential Threat**

"The risk I'm talking about is the risk these things will get smarter than us and **eventually take over**. And for that risk there may be something governments can do — because nobody wants that."

From his Nobel address: "We urgently need research on how to prevent these new beings from wanting to take control. **They are no longer science fiction.**"

**9. We Don't Know If Safety Is Even Possible**

"I think at present we're like someone who's raising a very cute tiger cub."

"Either we figure out how to keep this stuff safe or we don't. We don't know if it can be made safe, but we should put a huge effort right now into figuring out if it can be made safe."

---

### Structural / Systemic Danger

**10. The Incentive Problem**

"99 people are working on making them better and one person's working on preventing them getting out of control."

Companies have "an obligation to shareholders... making big profits, particularly in the short term, doesn't align nicely with putting a lot of effort into making sure it's safe."

From his Nobel address: "We have evidence that if they are created by companies motivated by short-term profits, our safety will not be the top priority."

---

Hinton's core alarm is this: the dangers are no longer science fiction, the timeline is shorter than anyone expected, and the incentive structures in the technology industry are structurally misaligned with safety. He calls on governments to force companies to fund safety research — and on young researchers to work on alignment, not capability.

> "Look at how many people are working on making these things better and how many people are working on preventing them from getting out of control. Where could you make the most impact?"
"""

HINTON_TRANSFORMERS_CONTENT = """## From Backpropagation to GPT-4: The Architecture That Changed Everything

In 1984, Geoffrey Hinton — then a young researcher at Carnegie Mellon — built a tiny language model with only 100 training examples. It worked by predicting the next word in a sequence. It could learn that words like "cat" and "dog" shared features like "animate" and "small," and that "fridge" was something else entirely. Nobody paid attention. It was a curiosity.

Forty years later, that same idea — predict the next word, adjust the weights, repeat — runs on tens of thousands of GPUs and produces systems that can reason, write code, pass medical exams, and manipulate people more effectively than any human can.

The road from Hinton's 1984 model to GPT-4 is the story of how transformers opened the door to an AI revolution. And if Hinton is right, we are only at the beginning.

---

### Why Neural Networks Didn't Work for Decades

The idea of learning through interconnected neurons — inspired by the brain — has been around since the 1950s. Alan Turing believed in it. John von Neumann believed in it. Both died young.

For the next 50 years, symbolic AI dominated: intelligence was about logic, rules, and structured symbolic reasoning. Neural networks were seen as a curiosity at best, nonsense at worst.

Hinton describes the core problem simply: **not enough data, not enough compute.**

> "The main reason was we didn't have enough compute power and we didn't have enough data. Neural nets really come into their own when you have a lot of data and a lot of compute power."

In the 1990s, smaller statistical methods outperformed neural nets on small datasets. Deep networks were effectively abandoned by most of computer science — though not by Hinton, who kept pushing.

---

### 2006–2012: The Tipping Point

Everything changed in two stages.

**2006:** Hinton's lab figured out how to initialize the weights of deep networks using unsupervised pretraining, making backpropagation work far more reliably in deep architectures.

**2009:** His graduate students built a speech recognizer using deep neural nets that slightly beat the state of the art. Within a few years, every major speech group had switched to neural nets. The Android's speech recognition caught up to Siri overnight.

**2012:** The moment the world noticed. Two of Hinton's grad students — Ilya Sutskever and Alex Krizhevsky — built AlexNet, a deep convolutional network trained on GPUs. It didn't just win the ImageNet visual recognition competition. It halved the error rate.

> "Alex got 15% errors where the best technique up until then was getting 25%. And since then it's gone down to about 3%. It was a huge jump."

The GPU was the secret weapon. Alex Krizhevsky had programmed two GPU boards to collaborate — something almost no one had done. Each GPU was equivalent to roughly 10 years of progress in conventional computing power.

The computer vision community's reaction was unusually healthy for science:

> "Most of them behaved in a very admirable way, which is they said, 'Hey, we never thought this would work, but hey it works so we're gonna do that instead of what we were doing.'"

---

### The Transformer: Attention Changes Everything

After AlexNet, deep learning spread rapidly to speech, translation, and image recognition. But language remained hard. Sequential models like LSTMs struggled to hold context across long texts — they forgot what was said at the beginning of a paragraph by the time they reached the end.

The breakthrough came in 2017 with the paper *Attention Is All You Need*, which introduced the Transformer architecture. The key innovation: **self-attention**.

Instead of reading words one at a time and trying to remember what came before, a transformer looks at every word in a sequence simultaneously and asks: *how relevant is each word to every other word?* A noun at the start of a sentence can directly influence a verb at the end. Context doesn't decay — it propagates.

This is how modern LLMs handle the word "May" in a sentence: without context, it's ambiguous (the month? the modal verb?). With attention, the network can look at "June" two words away and immediately resolve the meaning. Hinton explains this in plain terms:

> "As we go up through the network, we make the embedding vectors for a word get better and better, 'cause they're gonna take into account more and more contextual information... If there's the embedding vector for June, then it'll refine the one for May to be more like a month and less like a modal."

Transformers scaled. More layers, more parameters, more data — and the performance kept climbing. This was the architecture that produced GPT-2, GPT-3, GPT-4, and the wave of models now reshaping every industry.

---

### What GPT-4 Did to Hinton

When Hinton first used GPT-4, he was shocked — not because he hadn't expected progress, but because the timeline had collapsed.

> "I am just shocked at how good it is."

He tested it with a trick puzzle a symbolic AI skeptic had given him, then made the puzzle harder. GPT-4 solved it anyway — not by matching patterns, but by reasoning through the problem:

> "The rooms in my house are either white, blue, or yellow. Yellow paint fades to white within a year. In two years time I would like all the rooms to be white. What should I do?" GPT-4 answered: paint the blue rooms yellow. The yellow will fade to white. "I don't see how it could do that without understanding the problem."

GPT-4, Hinton noted, has roughly 1% of the neural connections in a human brain — but has processed far more experience:

> "We have a hundred times as many connections as GPT-4, but we have very little time. We only live for two billion seconds. And that's a tiny amount of experience compared with what GPT-4 had."

The hive mind advantage makes this even more asymmetric. A digital model can run as 10,000 simultaneous copies, each learning something different, and then share weights directly — transmitting knowledge instantly across all instances. Humans share knowledge through sentences. It's not even close.

---

### The Coming of AGI: Hinton's Revised Timeline

For most of his career, Hinton estimated it would be **30–50 years** before AI exceeded human intelligence. Then, in 2022–2023, he changed his mind.

> "A few months ago I suddenly realized maybe they're already better than us — they're just smaller. And when they get bigger, they'll be smarter than us. And that was quite scary. It was a sudden change of opinion. Instead of being 30 to 50 years, it was **five years to 20 years**, something like that."

What triggered the shift? He had been developing biologically plausible learning algorithms — alternatives to backpropagation that could run in a real neural system. When he scaled them up, the digital systems consistently outperformed his biological alternatives. He realized the gap may not be a problem with his algorithms. It may be that **digital intelligence is simply better**.

He is not alone in this view:

- **Yoshua Bengio** (co-winner of the Turing Award): tracking AI capability against the ability to "plan over different horizons," projects that AI will match employee-level job performance **within about 5 years** in engineering tasks.
- **Queen Elizabeth Prize panel (2025)**: "If you define AGI as 'it'll always win in a debate with you' — we're going to get there in less than 20 years, probably."
- Almost every AI expert Hinton speaks to now believes AI will exceed human intelligence. The only debate is when.

> "Very few of the experts are in doubt about that. Almost everybody I know who's an expert on AI believes that they will exceed human intelligence. It's just a question of when."

---

### Superintelligence: The Harder Problem

AGI — matching human performance across tasks — is the milestone everyone is racing toward. But Hinton's deeper concern is what comes next: **superintelligence**, a system that doesn't just match humans but vastly surpasses us.

At that point, the question of alignment becomes existential:

> "How do you stop something more intelligent than you from taking control? Humanity has never faced this."

Hinton now puts the probability of AI-caused human extinction **at 10–20%** — a number he has revised upward. He is explicit that this is not science fiction:

> "It's a significant chance. It's not like 1%. It's much more."

His particular concern is manipulation — not robots and physical takeover, but something subtler:

> "They'll have read everything Machiavelli ever wrote. They'll be real experts at human deception, 'cause they'll learn that from us... As soon as you can manipulate people, you can get whatever you like done."

The structural problem: there is no strong incentive to solve this. Companies are racing to build more capable systems because capability generates profit. Safety does not.

> "99 people are working on making them better and one person's working on preventing them getting out of control."

---

### The Path Forward

Hinton's message to young researchers is direct:

> "Look at how many people are working on making these things better and how many people are working on preventing them from getting out of control. Where could you make the most impact?"

And his message to governments: mandate safety research now, before these systems are smarter than the people trying to regulate them. The window may be narrow.

The transformer architecture opened a door. What walks through it — and whether we remain in control — is the defining question of the next two decades.

> "We're at a bifurcation point in history. Either we figure out how to keep this stuff safe, or we don't. We don't know if it can be made safe, but we should put a huge effort right now into figuring out if it can be made safe."
"""


def create_hinton_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')
    Tag = apps.get_model('blog', 'Tag')

    cat, _ = Category.objects.get_or_create(
        slug='ai',
        defaults={'name': 'AI', 'description': 'Artificial intelligence', 'color': 'indigo'}
    )

    # Post 1: Dangerous potential
    post1, _ = Post.objects.get_or_create(
        slug='geoffrey-hinton-dangerous-potential-of-ai',
        defaults={
            'title': 'Geoffrey Hinton: The Dangerous Potential of AI',
            'summary': (
                "Geoffrey Hinton — Nobel laureate and 'Godfather of AI' — outlines the near-term and existential "
                "risks of artificial intelligence, from lethal autonomous weapons and epistemic manipulation to "
                "AI surpassing human intelligence within 5–20 years."
            ),
            'content': HINTON_DANGERS_CONTENT,
            'category': cat,
            'published': True,
            'featured': True,
        }
    )

    # Post 2: Transformers and AGI
    post2, _ = Post.objects.get_or_create(
        slug='transformers-agi-superintelligence-geoffrey-hinton',
        defaults={
            'title': 'Transformers and the Coming of AGI: What Geoffrey Hinton Says',
            'summary': (
                "How the transformer architecture — built on Geoffrey Hinton's 1984 word prediction idea — triggered "
                "the AI revolution, and what Hinton and his peers now say about AGI arriving within 5–20 years and "
                "the race to superintelligence."
            ),
            'content': HINTON_TRANSFORMERS_CONTENT,
            'category': cat,
            'published': True,
            'featured': True,
        }
    )

    for tag_name, tag_slug in [
        ('AI Safety', 'ai-safety'),
        ('Geoffrey Hinton', 'geoffrey-hinton'),
        ('Existential Risk', 'existential-risk'),
        ('Transformers', 'transformers'),
        ('AGI', 'agi'),
        ('Deep Learning', 'deep-learning'),
    ]:
        tag, _ = Tag.objects.get_or_create(slug=tag_slug, defaults={'name': tag_name})

    post1.tags.add(*Tag.objects.filter(slug__in=['ai-safety', 'geoffrey-hinton', 'existential-risk']))
    post2.tags.add(*Tag.objects.filter(slug__in=['ai-safety', 'geoffrey-hinton', 'transformers', 'agi', 'deep-learning']))


def remove_hinton_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(slug__in=[
        'geoffrey-hinton-dangerous-potential-of-ai',
        'transformers-agi-superintelligence-geoffrey-hinton',
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_subscriber_post_ai_summary'),
    ]

    operations = [
        migrations.RunPython(create_hinton_posts, remove_hinton_posts),
    ]
