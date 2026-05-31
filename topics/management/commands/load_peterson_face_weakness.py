"""
Article: How to Face Your Weakness — Jordan Peterson
Source: pschy/jordan_peterson/transcripts.txt
  - T2fz9ZhmaQA  (There's No Such Thing as a Dragon)
  - Nn1Np7mrFck  (Hero narrative / dragon potential)
  - KM5pf1bQ7ws  (Jocko Willink / self-criticism as strategy)
  - otsOXNidluo  (bitter, resentful, cruel consequences)
  - 1nyVHWu7N2Y  (Jacob — a bad man decides to be good)
  - Wv7lEyck2mg  (Jung / welcome the unknown)
"""
from django.core.management.base import BaseCommand
from topics.models import Article, Pillar


SLUG = "how-to-face-your-weakness-peterson"

CONTENT = """
<figure style="margin:0 0 2.5em;">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:16px;display:block;">
  <defs>
    <radialGradient id="bg-grd" cx="30%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#1a0f2e"/>
      <stop offset="100%" stop-color="#070c18"/>
    </radialGradient>
    <radialGradient id="glow-r" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#c084fc" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow-g" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4ade80" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#4ade80" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur-sm"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="blur-lg"><feGaussianBlur stdDeviation="12"/></filter>
    <style>
      @keyframes flicker {
        0%,100%{opacity:.85} 40%{opacity:.55} 65%{opacity:.9}
      }
      @keyframes rise {
        0%{transform:translateY(0)} 50%{transform:translateY(-8px)} 100%{transform:translateY(0)}
      }
      @keyframes pulse-glow {
        0%,100%{opacity:.4} 50%{opacity:.75}
      }
      @keyframes draw {
        from{stroke-dashoffset:600} to{stroke-dashoffset:0}
      }
      @keyframes fade-in {
        from{opacity:0} to{opacity:1}
      }
      .flame { animation: flicker 3.4s ease-in-out infinite; }
      .figure { animation: rise 5s ease-in-out infinite; }
      .glow-orb { animation: pulse-glow 4s ease-in-out infinite; }
      .path-line { stroke-dasharray:600; animation: draw 3s ease-out forwards; }
      .label { animation: fade-in 1.2s ease-out 1s forwards; opacity:0; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="720" height="420" fill="url(#bg-grd)"/>

  <!-- Ambient glow left (shadow/dark) -->
  <ellipse cx="180" cy="250" rx="160" ry="120" fill="#6d28d9" opacity="0.12" filter="url(#blur-lg)"/>

  <!-- Ambient glow right (potential/light) -->
  <ellipse cx="560" cy="180" rx="140" ry="110" fill="#a78bfa" opacity="0.18" filter="url(#blur-lg)"/>
  <ellipse cx="560" cy="180" rx="80" ry="70" fill="url(#glow-r)" filter="url(#blur-lg)"/>

  <!-- DRAGON (left, dark side) -->
  <!-- Dragon body -->
  <g opacity="0.82">
    <!-- Wings -->
    <path d="M 120 220 Q 60 140 90 100 Q 140 120 160 180" fill="#2d1b4e" stroke="#7c3aed" stroke-width="1.2" opacity="0.9"/>
    <path d="M 200 215 Q 260 140 240 100 Q 195 118 180 180" fill="#2d1b4e" stroke="#7c3aed" stroke-width="1.2" opacity="0.9"/>
    <!-- Body -->
    <ellipse cx="165" cy="235" rx="52" ry="35" fill="#1e0f35" stroke="#7c3aed" stroke-width="1.4"/>
    <!-- Head -->
    <ellipse cx="155" cy="197" rx="26" ry="20" fill="#1e0f35" stroke="#7c3aed" stroke-width="1.4"/>
    <!-- Eye glow -->
    <circle cx="163" cy="193" r="5" fill="#c084fc" class="glow-orb" style="animation-delay:.3s"/>
    <circle cx="163" cy="193" r="3" fill="#f0abfc"/>
    <!-- Tail -->
    <path d="M 213 245 Q 260 280 245 310 Q 230 330 215 315" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round"/>
    <!-- Flame breath -->
    <path d="M 130 200 Q 110 188 95 175 Q 80 162 70 150" fill="none" stroke="#f97316" stroke-width="3" stroke-linecap="round" class="flame" opacity="0.9"/>
    <path d="M 125 205 Q 100 190 82 178" fill="none" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" class="flame" style="animation-delay:.4s"/>
    <circle cx="75" cy="148" r="8" fill="#f97316" opacity="0.6" filter="url(#blur-sm)" class="flame"/>
  </g>

  <!-- Dividing line / chasm -->
  <path d="M 340 60 Q 350 200 330 380" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.35" stroke-dasharray="6 5"/>

  <!-- HUMAN FIGURE (centre, crossing the chasm) -->
  <g class="figure">
    <!-- Shadow form (dark side) -->
    <ellipse cx="305" cy="310" rx="22" ry="6" fill="#4c1d95" opacity="0.5" filter="url(#blur-sm)"/>
    <!-- Legs -->
    <line x1="315" y1="295" x2="308" y2="320" stroke="#a78bfa" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="315" y1="295" x2="322" y2="320" stroke="#a78bfa" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Body -->
    <rect x="307" y="258" width="16" height="40" rx="6" fill="#7c3aed" stroke="#c084fc" stroke-width="1.2"/>
    <!-- Arms extended (reaching toward dragon AND toward light) -->
    <line x1="307" y1="270" x2="280" y2="258" stroke="#a78bfa" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="323" y1="270" x2="350" y2="258" stroke="#c4b5fd" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Head -->
    <circle cx="315" cy="248" r="11" fill="#7c3aed" stroke="#c084fc" stroke-width="1.4"/>
  </g>

  <!-- PATH / JOURNEY LINE -->
  <path d="M 270 310 Q 315 290 360 265 Q 420 235 480 200 Q 530 172 570 150"
        fill="none" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round"
        class="path-line" opacity="0.7"/>

  <!-- LIGHT / POTENTIAL (right side) -->
  <circle cx="570" cy="148" r="42" fill="#a78bfa" opacity="0.08" filter="url(#blur-lg)"/>
  <circle cx="570" cy="148" r="28" fill="#c084fc" opacity="0.15" filter="url(#blur-sm)"/>
  <circle cx="570" cy="148" r="16" fill="#e9d5ff" opacity="0.6" class="glow-orb" style="animation-delay:.8s"/>
  <!-- Star-like spokes -->
  <g stroke="#c084fc" stroke-width="1.2" opacity="0.5">
    <line x1="570" y1="112" x2="570" y2="100"/>
    <line x1="570" y1="184" x2="570" y2="196"/>
    <line x1="534" y1="148" x2="522" y2="148"/>
    <line x1="606" y1="148" x2="618" y2="148"/>
    <line x1="545" y1="123" x2="537" y2="115"/>
    <line x1="595" y1="173" x2="603" y2="181"/>
    <line x1="545" y1="173" x2="537" y2="181"/>
    <line x1="595" y1="123" x2="603" y2="115"/>
  </g>

  <!-- Labels -->
  <text x="148" y="355" font-family="monospace" font-size="10" fill="#7c3aed" opacity="0.8" text-anchor="middle" class="label">THE SHADOW</text>
  <text x="570" y="210" font-family="monospace" font-size="10" fill="#c084fc" opacity="0.8" text-anchor="middle" class="label" style="animation-delay:1.4s">POTENTIAL</text>
  <text x="318" y="240" font-family="monospace" font-size="9" fill="#e9d5ff" opacity="0.65" text-anchor="middle" class="label" style="animation-delay:1.8s">THE CROSSING</text>

  <!-- Title text -->
  <text x="36" y="56" font-family="Georgia, serif" font-size="20" fill="#f5f3ff" opacity="0.92" font-style="italic">How to Face Your Weakness</text>
  <text x="36" y="74" font-family="monospace" font-size="9.5" fill="#a78bfa" letter-spacing="0.12em">JORDAN PETERSON · COGITRA</text>
</svg>
<figcaption style="font-family:var(--font-mono,monospace);font-size:11px;color:#6b7280;margin-top:10px;letter-spacing:0.08em;text-transform:uppercase;">The crossing: between the shadow you avoid and the potential you could become</figcaption>
</figure>

<p>There is a story Peterson returns to again and again in his lectures — a children's book called <em>There's No Such Thing as a Dragon</em> by Jack Kent. A boy named Billy wakes up to find a small dragon in his room, about the size of a kitten. When he tells his mother, she says there is no such thing. His father says the same. Nobody acknowledges it. And so the dragon grows. It grows until it fills the house. It picks up the house and walks down the street with it. Only when Billy finally says "I think there IS a dragon" does it begin to shrink.</p>

<p>Peterson uses this story as the opening lecture in his Maps of Meaning course because it contains a principle he considers foundational to psychological health: <strong>what you refuse to see will not stay small</strong>.</p>

<blockquote>"If you turn a blind eye to something, then it can grow until it becomes an overwhelming and demolishing force. All the anomalies, the unexpected occurrences that could turn themselves into predators with time, have the proclivity to grow if they're ignored."</blockquote>

<p>The dragon is not metaphorical decoration. It is a precise description of what happens when you avoid your weakness — the temper you never disciplined, the dependency you never named, the cowardice you keep rationalising as patience.</p>

<h2>The Cost of Not Facing It</h2>

<p>Peterson is blunt about what avoidance produces over time:</p>

<blockquote>"If you don't have a goal you suffer and then you get cruel and bitter and resentful and then you start to actively try to make the world a worse place — because you can't suffer pointlessly without becoming bitter, and you can't become bitter without becoming cruel."</blockquote>

<p>This is not a moral condemnation. It is a clinical observation. Unaddressed weakness does not stay neutral. It curdles. The person who never addressed their anxiety becomes controlling. The one who never confronted their dishonesty becomes manipulative in ways they no longer see clearly. The weakness does not disappear because you stop looking at it. It disappears into the background, where it operates without your awareness and at greater cost.</p>

<p>Peterson draws here on Carl Jung, who framed the same insight theologically: <em>"Modern people don't see God because they don't look low enough."</em> The thing you are most reluctant to examine — the thing that lives in the basement of your personality — is precisely where the work of transformation is waiting.</p>

<h2>The Dragon and the Treasure</h2>

<p>What makes Peterson's framing unusually useful is that he refuses to treat weakness as simply shameful. He frames it as a door.</p>

<blockquote>"The dragon battle is a narrative condensation of the drama of human beings — the fact that we have to encounter the terrible predatory unknown and to try to gather what's valuable that's hidden in it and to transform ourselves in that pursuit."</blockquote>

<p>In the mythological structure Peterson analyzes across cultures, the treasure is always guarded by the dragon. This is not an accident. It is a description of the structure of experience: the thing you are avoiding is almost certainly adjacent to something you need. The man who is afraid of direct confrontation often avoids it because there is something worth protecting — a principle, a relationship — that he has not yet figured out how to defend without aggression. The woman who cannot tolerate criticism may be protecting a genuine sensitivity that, properly integrated, makes her a better writer or clinician.</p>

<p>The weakness is not just a deficit. It is, as Peterson puts it: <em>"The bigger dragon you confront, the more potential will be released within you. Who knows who you could become."</em></p>

<h2>Self-Criticism Is Not a Verdict</h2>

<p>One of the more practically useful distinctions Peterson makes is between self-criticism as diagnosis and self-criticism as punishment. Most people do the second when they should be doing the first.</p>

<p>He describes a conversation with his daughter, who came home convinced she was stupid because she didn't know her times tables. Peterson's response is the pattern:</p>

<blockquote>"Single points of inadequacy do not indicate general incompetence. You're not born knowing your times tables and you're not born knowing chemistry and you're not born knowing European history. You want to take that self-criticism and narrow it to the point where it turns into a strategy for progress."</blockquote>

<p>This is the operational move. Broad self-condemnation — <em>I am weak, I am broken, I am not enough</em> — is cognitively useless because it has no traction. It produces shame but no plan. The alternative is precise: <em>I failed here, under these conditions, for this probable reason. What would have to change?</em></p>

<p>Narrowing self-criticism to a strategy is not the same as excuse-making. It is the opposite. It requires you to actually look at the problem rather than drowning in generalised self-loathing, which is often its own form of avoidance.</p>

<h2>Jacob: The Coward Who Decided to Be Good</h2>

<p>Peterson finds in the story of Jacob — one of the founding patriarchs of the biblical tradition — a case study in transformation through confronting one's own nature.</p>

<blockquote>"Jacob's a bad guy. He's in collusion with his mother. He's deceived his father. He's betrayed his brother. He's a mama's boy. He's intellectually arrogant. He's a coward. He's a bad guy, an unlikable character. But then he leaves — and he decides that he's going to be good. He's going to try to be good. That's when he has that dream."</blockquote>

<p>Jacob's Ladder appears not at his best moment, but at the turning point where he decides to change direction. The vision of the ladder reaching into the infinite — Peterson's reading of which is that there is always another mountain once you climb the first — is given to a man who has just acknowledged what he is and decided it is not what he wants to be.</p>

<p>The Biblical tradition does not require purity before transformation is possible. It requires the decision. The acknowledgment of the gap — between who you are and who you could be — is the starting point of the entire journey. As Peterson puts it, quoting this structure: <em>"You can either live out your vision or someone else's. There's no no-vision option."</em></p>

<h2>Welcome the Unknown</h2>

<p>The final move — after naming the weakness, after narrowing self-criticism to strategy, after deciding to face the dragon — is a shift in orientation toward the difficulty itself.</p>

<blockquote>"What you want to do is welcome the unknown with open arms because it can teach you and change you into what you could be."</blockquote>

<p>This is not optimism. Peterson is not pretending that facing your weakness is easy or comfortable. He is making a structural point: growth is not possible without the encounter with what is difficult, and the person who approaches that encounter with curiosity and willingness — rather than dread and avoidance — is drawing more information from it than the person who approaches it defensively.</p>

<p>It is also a call to attend carefully to what you are avoiding. Peterson considers this a kind of moral obligation: <em>"It's necessary... to be very aware of your various sins and stupidities."</em> Not as an act of self-flagellation, but as orientation. If you don't know where your weaknesses are, you cannot do anything about them. And if you do know and are ignoring them, the dragon is growing.</p>

<h2>The Practical Structure</h2>

<p>Drawn from Peterson's teachings, the approach to facing weakness has a shape:</p>

<p><strong>Name it precisely.</strong> Not "I have anger issues" but "I respond with disproportionate aggression when I feel I've been publicly embarrassed." The more precise the naming, the smaller and more addressable the problem becomes.</p>

<p><strong>Distinguish the weakness from the person.</strong> Single points of inadequacy do not indicate general incompetence. You are the one who has the weakness, not the thing the weakness says you are.</p>

<p><strong>Acknowledge what the weakness is adjacent to.</strong> The dragon guards something. What is it you are actually protecting by maintaining this avoidance? That thing may be worth protecting, just through a better means.</p>

<p><strong>Make the smallest possible confrontation.</strong> Much of what you're doing as you journey through life, Peterson argues, is to continually expand your personality. Is there something small that you can do on a daily basis that would incrementally improve your ability to function? The confrontation with the dragon does not have to happen all at once.</p>

<p><strong>Treat suffering as a diagnostic, not a verdict.</strong> What you find most difficult reveals the shape of the work left to do. Pain that has no meaning is torture. Pain that is pointing somewhere — toward a specific growth, a specific discipline, a specific honesty — is more bearable, and more useful.</p>

<p>Peterson frames all of this inside a much larger claim about the structure of a good life: that the only life worth living is one that takes seriously both what you are and what you could be, and makes an honest attempt to close the gap. The dragon is not there to humiliate you. It is there to be faced — and it has been guarding something for you all along.</p>
"""


class Command(BaseCommand):
    help = "Load Peterson 'How to Face Your Weakness' article"

    def handle(self, *args, **options):
        pillar, _ = Pillar.objects.get_or_create(
            slug="mindset-success",
            defaults={"name": "Mindset & Success", "icon": "🧠"},
        )

        data = {
            "slug": SLUG,
            "title": "How to Face Your Weakness",
            "summary": (
                "Jordan Peterson on why the weakness you avoid will not stay small — "
                "and why the dragon you refuse to face is almost always guarding "
                "something you need."
            ),
            "content": CONTENT,
            "pillar": pillar,
            "published": True,
        }

        obj, created = Article.objects.get_or_create(
            slug=data["slug"],
            defaults=data,
        )
        if not created:
            obj.title = data["title"]
            obj.summary = data["summary"]
            obj.pillar = data["pillar"]
            obj.published = data["published"]
            obj.save(update_fields=["title", "summary", "pillar", "published"])
            self.stdout.write(f"Updated (content preserved): {obj.title}")
        else:
            self.stdout.write(f"Created: {obj.title}")
        self.stdout.write("Done.")
