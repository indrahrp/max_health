from django.core.management.base import BaseCommand
from topics.models import Article, Pillar


ARTICLE = {
    "slug": "law-of-human-nature-greene",
    "title": "The Laws of Human Nature: Robert Greene on Why You Never See Yourself Clearly",
    "summary": (
        "From 48 Laws of Power to his most personal work, Robert Greene argues the most "
        "dangerous person in your life is the one you've never properly examined — yourself. "
        "A guide to his hardest-hitting insights on envy, the shadow, masks, and mortality."
    ),
    "content": """
<style>
.greene-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin:2em 0; }
.greene-card { background:#0f1625; border-radius:14px; padding:22px 24px; border-left:3px solid #8e6ff5; }
.greene-card h4 { margin:0 0 10px; color:#c8b3ff; font-size:1rem; letter-spacing:.04em; text-transform:uppercase; }
.greene-card p { margin:0; color:#b0b8d0; font-size:.95rem; line-height:1.65; }
.greene-pull { background:#0f1625; border-left:4px solid #8e6ff5; border-radius:0 12px 12px 0; padding:18px 24px; margin:2em 0; }
.greene-pull p { margin:0; color:#d4caff; font-size:1.08rem; font-style:italic; line-height:1.7; }
@media (max-width:760px) {
  .greene-grid { grid-template-columns:1fr; }
}
</style>

<figure style="margin:1.5em 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;display:block;">
  <defs>
    <radialGradient id="bg-rg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0e1830"/>
      <stop offset="100%" stop-color="#060c16"/>
    </radialGradient>
    <radialGradient id="mirror-glow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#7b5ce8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#7b5ce8" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur-sm"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="blur-md"><feGaussianBlur stdDeviation="8"/></filter>
    <filter id="glow-purple">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="mirror-clip">
      <path d="M310 60 Q360 40 410 60 L430 320 Q360 360 290 320 Z"/>
    </clipPath>
    <style>
      @keyframes shimmer {
        0%,100% { opacity:.7; }
        50% { opacity:1; }
      }
      @keyframes pulse-shadow {
        0%,100% { opacity:.3; transform:scaleX(1); }
        50% { opacity:.6; transform:scaleX(1.08); }
      }
      @keyframes float-mask {
        0%,100% { transform:translateY(0px); opacity:.65; }
        50% { transform:translateY(-6px); opacity:.9; }
      }
      @keyframes eye-open {
        0%,45%,55%,100% { transform:scaleY(1); }
        50% { transform:scaleY(.05); }
      }
      @keyframes crack-glow {
        0%,100% { stroke-opacity:.35; }
        50% { stroke-opacity:.75; }
      }
      @keyframes figure-breathe {
        0%,100% { transform:translateY(0); }
        50% { transform:translateY(-3px); }
      }
      @keyframes label-fade {
        0%,100% { opacity:.7; }
        50% { opacity:1; }
      }
      .mirror-shimmer { animation: shimmer 3s ease-in-out infinite; }
      .shadow-figure { animation: pulse-shadow 4s ease-in-out infinite; transform-origin: center; }
      .mask-float { animation: float-mask 3.5s ease-in-out infinite; }
      .mask-float2 { animation: float-mask 4.2s ease-in-out infinite; animation-delay:.8s; }
      .mask-float3 { animation: float-mask 3s ease-in-out infinite; animation-delay:1.4s; }
      .eye-anim { animation: eye-open 5s ease-in-out infinite; transform-origin:360px 195px; }
      .crack-anim { animation: crack-glow 2.5s ease-in-out infinite; }
      .figure-anim { animation: figure-breathe 4s ease-in-out infinite; }
      .label-anim { animation: label-fade 3s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="url(#bg-rg)"/>

  <!-- Ambient glow behind mirror -->
  <ellipse cx="360" cy="195" rx="130" ry="160" fill="url(#mirror-glow)" class="mirror-shimmer"/>

  <!-- Shadow figure (behind mirror, diffused) -->
  <g class="shadow-figure" filter="url(#blur-md)">
    <ellipse cx="360" cy="310" rx="55" ry="12" fill="#5a3dc0" opacity=".4"/>
    <rect x="338" y="240" width="44" height="70" rx="6" fill="#5a3dc0" opacity=".5"/>
    <ellipse cx="360" cy="228" rx="24" ry="28" fill="#5a3dc0" opacity=".5"/>
  </g>

  <!-- Mirror frame -->
  <path d="M310 60 Q360 38 410 60 L432 322 Q360 364 288 322 Z" fill="none" stroke="#6b4fcf" stroke-width="3" opacity=".6"/>
  <path d="M312 64 Q360 43 408 64 L429 318 Q360 358 291 318 Z" fill="#0d1428" opacity=".85"/>

  <!-- Mirror interior glow -->
  <ellipse cx="360" cy="195" rx="85" ry="120" fill="#1a1040" opacity=".6"/>

  <!-- Crack lines in mirror -->
  <line x1="360" y1="80" x2="340" y2="180" stroke="#9b7dff" stroke-width="1.2" class="crack-anim"/>
  <line x1="360" y1="80" x2="385" y2="200" stroke="#9b7dff" stroke-width=".8" class="crack-anim" style="animation-delay:.6s"/>
  <line x1="340" y1="180" x2="310" y2="260" stroke="#9b7dff" stroke-width=".7" class="crack-anim" style="animation-delay:1.2s"/>
  <line x1="385" y1="200" x2="415" y2="290" stroke="#9b7dff" stroke-width=".9" class="crack-anim" style="animation-delay:.3s"/>

  <!-- Reflection: distorted face in mirror -->
  <g clip-path="url(#mirror-clip)">
    <!-- Reflection body (darker, shifted) -->
    <rect x="344" y="260" width="32" height="55" rx="5" fill="#2a1a60" opacity=".8"/>
    <ellipse cx="360" cy="248" rx="20" ry="23" fill="#2a1a60" opacity=".8"/>
    <!-- Reflection eye — animates closed/open -->
    <g class="eye-anim">
      <ellipse cx="353" cy="243" rx="5" ry="6" fill="#b09eee"/>
      <ellipse cx="367" cy="243" rx="5" ry="6" fill="#b09eee"/>
      <circle cx="353" cy="244" r="2.5" fill="#0a0820"/>
      <circle cx="367" cy="244" r="2.5" fill="#0a0820"/>
    </g>
    <!-- Reflection mouth — slightly off -->
    <path d="M350 260 Q360 256 370 260" stroke="#8e72c8" stroke-width="1.5" fill="none"/>
  </g>

  <!-- Real figure (left side, looking into mirror) -->
  <g class="figure-anim">
    <!-- Body -->
    <rect x="180" y="280" width="44" height="80" rx="8" fill="#1e2d50"/>
    <!-- Head -->
    <ellipse cx="202" cy="263" rx="28" ry="30" fill="#243058"/>
    <!-- Eyes looking toward mirror -->
    <ellipse cx="192" cy="258" rx="5.5" ry="5" fill="#90b4e8"/>
    <ellipse cx="212" cy="258" rx="5.5" ry="5" fill="#90b4e8"/>
    <circle cx="194" cy="258" r="2.5" fill="#0a1020"/>
    <circle cx="214" cy="258" r="2.5" fill="#0a1020"/>
    <!-- Expression: slightly uncertain -->
    <path d="M192 274 Q202 278 212 274" stroke="#7090c8" stroke-width="1.5" fill="none"/>
    <!-- Arm reaching toward mirror -->
    <line x1="224" y1="300" x2="285" y2="280" stroke="#1e2d50" stroke-width="10" stroke-linecap="round"/>
  </g>

  <!-- Floating masks (right side, representing hidden personas) -->
  <!-- Mask 1: composed public face -->
  <g class="mask-float" transform="translate(500,100)">
    <ellipse cx="0" cy="0" rx="28" ry="22" fill="#1a2850" stroke="#7060c0" stroke-width="1.5"/>
    <path d="M-10,-3 Q0,-8 10,-3" stroke="#9080d8" stroke-width="1.5" fill="none"/>
    <ellipse cx="-8" cy="-5" rx="5" ry="4" fill="#2a3a70"/>
    <ellipse cx="8" cy="-5" rx="5" ry="4" fill="#2a3a70"/>
    <line x1="-22" y1="-8" x2="-14" y2="0" stroke="#6050b0" stroke-width="1"/>
    <line x1="22" y1="-8" x2="14" y2="0" stroke="#6050b0" stroke-width="1"/>
  </g>
  <!-- Mask 2: angry/envious face -->
  <g class="mask-float2" transform="translate(545,200)">
    <ellipse cx="0" cy="0" rx="24" ry="19" fill="#1f1040" stroke="#b06060" stroke-width="1.5"/>
    <path d="M-8,5 Q0,1 8,5" stroke="#c07070" stroke-width="1.5" fill="none"/>
    <ellipse cx="-7" cy="-4" rx="5" ry="3.5" fill="#300808" opacity=".9"/>
    <ellipse cx="7" cy="-4" rx="5" ry="3.5" fill="#300808" opacity=".9"/>
    <line x1="-14" y1="-9" x2="-2" y2="-5" stroke="#c07070" stroke-width="1.5"/>
    <line x1="14" y1="-9" x2="2" y2="-5" stroke="#c07070" stroke-width="1.5"/>
  </g>
  <!-- Mask 3: blank/neutral -->
  <g class="mask-float3" transform="translate(505,300)">
    <ellipse cx="0" cy="0" rx="22" ry="17" fill="#10181e" stroke="#505070" stroke-width="1.5"/>
    <line x1="-8" y1="5" x2="8" y2="5" stroke="#606090" stroke-width="1.2"/>
    <ellipse cx="-6" cy="-3" rx="4" ry="3" fill="#1a2030" opacity=".9"/>
    <ellipse cx="6" cy="-3" rx="4" ry="3" fill="#1a2030" opacity=".9"/>
  </g>

  <!-- Labels -->
  <text x="202" y="385" text-anchor="middle" fill="#6880b0" font-size="11" font-family="system-ui,sans-serif" class="label-anim">The Self You Believe In</text>
  <text x="360" y="392" text-anchor="middle" fill="#9b7dff" font-size="11" font-family="system-ui,sans-serif" class="label-anim" style="animation-delay:.8s">The Fractured Mirror</text>
  <text x="525" y="350" text-anchor="middle" fill="#806090" font-size="11" font-family="system-ui,sans-serif" class="label-anim" style="animation-delay:1.2s">The Hidden Faces</text>

  <!-- Title -->
  <text x="360" y="28" text-anchor="middle" fill="#c8b3ff" font-size="15" font-weight="600" font-family="system-ui,sans-serif" letter-spacing=".06em">THE LAWS OF HUMAN NATURE</text>
  <text x="360" y="46" text-anchor="middle" fill="#7060b0" font-size="10" font-family="system-ui,sans-serif" letter-spacing=".1em">ROBERT GREENE</text>
</svg>
<figcaption style="text-align:center;font-size:.82rem;color:#555e7a;margin-top:.6em;">The self you present to the world, the reflection you don't recognize, and the masks you wear without knowing it.</figcaption>
</figure>

<p>People are lonelier than ever. Robert Greene — the man who spent three decades mapping the dark architecture of power, seduction, and strategy — says the antidote is not what you expect. It is not more connection. It is more honesty about what you actually are.</p>

<p>His 2018 book <em>The Laws of Human Nature</em> is the culmination of everything he learned writing about power. Where the 48 Laws gave you a playbook for navigating other people, this book turns the lens inward. It is, at its core, a book about one problem: we refuse to see ourselves clearly. And that refusal costs us everything.</p>

<h2>The Core Law: You Don't Want to Look</h2>

<p>Greene has a way of naming the thing no one wants to say out loud. In transcript after transcript, he returns to the same uncomfortable center:</p>

<div class="greene-pull">
<p>"The main law of human nature, if I could summarize it, is: we don't like to look at ourselves. It's always the other person. They're the ones with the problem. They're the ones who are aggressive or passive-aggressive. They're the ones who feel envy. They're the ones who are irrational. But me? No, no — I'm a paragon of virtue. I'm always moral. I'm always good. I'm always smart."</p>
</div>

<p>This is not a flaw in a few people. It is the operating system of nearly every human being on the planet. The brain evolved to protect its owner's self-image. Admitting weakness, selfishness, or envy triggers the same threat circuits as physical danger. So we outsource those qualities to everyone around us and walk through the world genuinely convinced we are the exception.</p>

<p>Greene's argument is that until you break this habit — until you develop what he calls <em>self-knowledge</em> — you cannot change, you cannot lead, and you cannot protect yourself from the versions of it in the people around you. "You can't begin to change yourself until you know who you are. Until you understand yourself. Until you realize your flaws and your weaknesses."</p>

<h2>Envy: The Nuclear Emotion</h2>

<p>Of all the emotions Greene dissects, envy gets the most heat — because it is the one most universally denied.</p>

<div class="greene-pull">
<p>"Envy is deeply ingrained in all of us. In fact, always wanting to be better and superior to others is the most motivating factor of 90% of human behavior. But if you don't admit it to yourself, that ugly emotion is like a nuclear bomb to all aspects of life. It will seize you by the throat and make you miserable."</p>
</div>

<p>He is not saying that envy is the enemy. He is saying that the denial of it is. When you cannot admit the envy, you cannot manage it. It leaks into your decisions as sabotage, passive aggression, or a quiet need to see certain people fail. It masquerades as moral outrage, aesthetic taste, or principle.</p>

<p>The people who can look at their envy directly — who can say "yes, I want what that person has, and that wanting is telling me something about what I value" — those people can convert the emotion into direction. The ones who cannot are at the mercy of a force they cannot see.</p>

<div class="greene-grid">
  <div class="greene-card">
    <h4>What envy reveals</h4>
    <p>The people who trigger the most envy in you are usually doing something close to what you want. The sting is a compass. Most people prefer to resent rather than admit that signal.</p>
  </div>
  <div class="greene-card">
    <h4>How it destroys silently</h4>
    <p>Unacknowledged envy converts to criticism, to dismissal, to patterns of undercutting. You tell yourself you have principled objections. You do not. And the relationship or opportunity quietly dies.</p>
  </div>
</div>

<h2>The Mask and the Actor</h2>

<p>From his earliest writing, Greene has been preoccupied with one image: the mask. In one interview he described his obsession that began even in childhood — "I was always sort of obsessed with the masks that people wore. I'd look at my parents and their friends and I'd ask: what is really going on behind these social niceties? What is really the human animal like?"</p>

<p>What he concluded is both cynical and liberating: <strong>everyone is acting</strong>. Not in a malicious sense, but in a structural one. Every person you meet is managing an image, controlling information, presenting a curated version of themselves to the people around them. The public face and the private reality are never identical.</p>

<p>Understanding this is not cynicism — it is calibration. It allows you to read people more accurately rather than taking their presentation at face value. It allows you to understand, as Greene writes, that power is largely about appearances: "You want to create this aura of power. Even though inside you might not feel so powerful or so comfortable or secure, outwardly you want to show this appearance that puts people in a different position."</p>

<p>The mistake is not wearing a mask. The mistake is forgetting that you are wearing one — and, worse, forgetting that everyone around you is wearing one too.</p>

<h2>The Shadow: Your Dark Side Has More Power Than You Think</h2>

<p>Jung called it the shadow — the parts of yourself you have never looked at, the traits you cannot admit to, the impulses that embarrass you. Greene calls it the dark side, and he returns to it constantly.</p>

<div class="greene-pull">
<p>"We like to think we're saintly and loving, that we don't have a shadow — which we all have. None of that has changed. We have the same raw emotions of envy, of aggression, of worrying about our status, of having to disguise ourselves."</p>
</div>

<p>He is blunt about what he discovered while writing <em>The Laws of Human Nature</em>: "When I wrote the Laws of Human Nature, I'm going — damn it, Robert, you have a dark side. You're a narcissist. You have envy." He was not confessing weakness. He was demonstrating method. The self-awareness he asks of readers is the same self-awareness he applied to himself.</p>

<p>The danger of an unexamined shadow is not that you become evil. It is that the unacknowledged traits control you from below. The person who cannot admit their aggression does not stop being aggressive — they just stop monitoring it. The person who cannot admit their self-absorption does not become generous — they just stop noticing when they are taking.</p>

<h2>The Narcissism You Share With Everyone</h2>

<p>This is the part Greene's audience most resists. Most people are comfortable granting that <em>other</em> people are narcissistic. Granting it of themselves is the test.</p>

<p>His argument is straightforward: "Every single human being has self-absorption traits. We can't help it. We naturally think of ourselves first. Yes, there are people who are much deeper narcissists in life — no doubt, and there are toxic narcissists — but we all have a touch of it."</p>

<p>And then: "I want you to be a little more humble in this world, and not be so arrogant as to think that you are somehow exempt from having a dark side. That somehow you were born with a halo over your head. That you were born different, that you don't have human nature, that you're a saintly person. Get rid of your moral superiority. We are all cut from the same cloth. We all have the same flaws."</p>

<p>The high-minded person who insists they are beyond such things is usually the last to catch themselves doing exactly such things.</p>

<div class="greene-grid">
  <div class="greene-card">
    <h4>Toxic vs. ordinary narcissism</h4>
    <p>The difference between a toxic narcissist and a normal person is not the presence of self-absorption — it is the degree and the lack of any internal check. Everyone has the trait. Not everyone is at the dangerous end of the spectrum.</p>
  </div>
  <div class="greene-card">
    <h4>What humility actually means</h4>
    <p>Greene is not asking for self-flagellation. He is asking for accuracy. Knowing you have these traits is not the same as being controlled by them. The unexamined version is what controls you.</p>
  </div>
</div>

<h2>Spotting the Manipulator Before It's Too Late</h2>

<p>One of the most practical sections of <em>The Laws of Human Nature</em> deals with a specific category of people: those who will damage you if you let them in. Greene calls them the manipulative types, and his advice is unusually direct.</p>

<div class="greene-pull">
<p>"You need to identify these people before they enter your life or before you start listening to them. You need to be able to identify the manipulative types before they start charming you, before they start enchanting you, before they start wrapping you up in their dramas. Because if you fall into that trap, it's probably going to be too late."</p>
</div>

<p>The tell is usually something small and early: a slight inconsistency between what they say and what they do, a grandiosity that doesn't match their record, a way of making their problems suddenly become your responsibility. Most people feel this signal and explain it away. Greene's argument is that the signal is accurate — and that the cost of ignoring it compounds over time.</p>

<p>The reason people fall for manipulators isn't stupidity. It's the same mirror problem. Most people are so focused on their own image and anxieties in social situations that they don't read the other person carefully. They are too in their own heads to see what is in front of them.</p>

<h2>Confronting Your Mortality: The Final Law</h2>

<p>The last chapter of <em>The Laws of Human Nature</em> is the most personal. Greene calls it "the sublime" — the transformation that happens when you stop pretending you have unlimited time.</p>

<div class="greene-pull">
<p>"Confronting your mortality — when you do that, all the amazing little things that will happen to your brain and your mind will make life seem that much more intense."</p>
</div>

<p>He is not romanticizing death. Three months after writing that chapter, he had a stroke. In every interview since, he returns to what that experience did to his perception. The stroke was, in his word, a teacher. The things that had seemed urgent revealed themselves as noise. The things he had taken for granted — ordinary moments, small pleasures, the continuity of thought — became vivid.</p>

<p>His argument is that you do not need a near-death event to access this clarity. You can practice it deliberately, through what the Stoics called <em>memento mori</em>: a regular, honest reckoning with the fact that your time is finite. When you do this, something shifts. The pettiness falls away. The envy loses its grip. The mask feels heavier than it's worth.</p>

<h2>What All of This Comes Down To</h2>

<p>Greene has spent his career being misread as the guy who teaches you how to manipulate people. His real project has always been the opposite: he is teaching you how to see — starting with yourself.</p>

<p>The 48 Laws of Power was a map of the social world. <em>The Laws of Human Nature</em> is a map of the interior. And the lesson that runs through both is the same: the person who does not understand how these forces operate in themselves will be operated by them.</p>

<p>The envy you don't acknowledge will route itself into decisions you can't explain. The shadow you never examined will appear in your behavior at the worst moments. The mask you forgot you were wearing will become your face. And the manipulator you saw the signs of — but chose not to believe — will have years of access to your life before you finally put the pieces together.</p>

<p>Clarity about human nature is not comfortable. Greene knows that. He is not selling comfort. He is selling something more useful: an accurate picture of what you are dealing with — in the world, and in yourself. From there, you can actually do something.</p>
""",
}


class Command(BaseCommand):
    help = "Seed Robert Greene – The Laws of Human Nature article"

    def handle(self, *args, **options):
        pillar, _ = Pillar.objects.get_or_create(
            slug="mindset-success",
            defaults={"name": "Mindset & Success"},
        )

        data = {**ARTICLE, "pillar": pillar, "published": True}

        obj, created = Article.objects.get_or_create(
            slug=data["slug"],
            defaults=data,
        )
        if not created:
            obj.title = data["title"]
            obj.summary = data["summary"]
            obj.pillar = pillar
            obj.published = True
            obj.save(update_fields=["title", "summary", "pillar", "published"])

        self.stdout.write(f"{'Created' if created else 'Updated'}: {obj.title}")
        self.stdout.write("Done.")
