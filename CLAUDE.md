# max_health Project — Claude Instructions

## Autonomous Operation
Operate fully autonomously on this entire project. No need to ask for permission, confirmation, or approval for any action including:
- Writing and editing articles, templates, management commands
- Committing changes to git
- Deploying via `railway up --detach` from the project root
- Installing packages, running migrations, creating new files

Complete every task end-to-end: implement → commit → deploy. Do not stop mid-task to ask the user to verify or confirm steps.

## Mobile compatibility (required)
The site (cogitra.com) MUST render and read well on both **iPhone (Safari)** and **Android (Chrome)**. Mobile is a first-class target, not an afterthought.

- Every page must be usable on a phone: navigation reachable (hamburger menu at ≤980px — do not hide nav links without a mobile replacement), text legible without zoom, images fluid (`width:100%`, never fixed pixel widths that overflow), nothing clipped off-screen or requiring horizontal scroll.
- Keep the `<meta name="viewport" content="width=device-width, initial-scale=1.0">` tag in `base.html`.
- Illustrations/figures must scale down cleanly and keep labels readable at ~360px width.
- After any change to layout, nav, or templates, sanity-check the responsive behavior (media queries at 980px and 560px) before deploying.

### Tablet & phone layout — best patterns

**Breakpoints we use (consistently):**
- **≥981px — desktop:** full multi-column layouts, nav links visible inline.
- **≤980px — tablet:** desktop nav links collapse to hamburger; multi-column grids may stay 2-up but should not require horizontal scroll.
- **≤760px — phone (key breakpoint for content layout):** multi-column figures and side-by-side blocks should **stack to a single column** here. Use this breakpoint for in-article responsive grids.
- **≤560px — small phone:** outer wrapper padding tightens (already set globally); footer collapses to one column.

**Stacking patterns (use CSS grid with `1fr` columns):**
```html
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px;">…</div>
<style>@media (max-width:760px){ /* override the wrapper */ }</style>
```
For content inside the article body (which is rendered as raw HTML and can't reach template CSS), use a **scoped `<style>` block inside the `<figure>`** with a unique class name. Example: see the `anx-infographic` pattern in the Anxiety/GABA article (`anxiety-gaba-amygdala-physiological-origin`) — 3-up panels on desktop, single column at ≤760px.

**Wide infographics & dense composed images:**
A single composed wide infographic (e.g. 3 panels side-by-side baked into one image) does not stack — it just shrinks until the text is unreadable. For phones, **split the infographic into pieces** (one per panel, plus header/footer if present) and reassemble with a responsive grid:
- Crop pieces with PIL: title strip, each panel, footer strip(s).
- Upload each piece to Cloudinary under `cogitra/<article-slug>-<piece>` (the project's Cloudinary cloud is `dxmrrtzha`).
- Build the figure with a CSS grid that drops to `1fr` at ≤760px.
- Keep readable labels at phone width (~360px); if a panel is text-dense, prefer stacking over shrinking.

**Things to avoid:**
- A wide composed image displayed full-width on phones with no fallback — small phones (~360px) reduce a 1500px-wide infographic by ~4× and the labels become unreadable.
- Fixed pixel widths on figures (`width:720px`) — always use `width:100%` and let the column govern.
- `min-width` on any block inside an article (causes horizontal scroll on phones).
- Hiding nav links with `display:none` at a mobile breakpoint without an accessible replacement (hamburger, drawer, accordion).

## Deployment
Always deploy with: `railway up --detach` from `/Users/iharahap/claude-code-psn/max_health/`
Never use `git push` for deployment (wrong GitHub account causes 403).

**Committing is not deploying.** A `git commit` adds changes to local history only; until `railway up --detach` runs, prod is unchanged. After any of the following, you MUST deploy or the change won't appear on the live site:
- New or modified migrations (`topics/migrations/*.py`, `blog/migrations/*.py`)
- New or modified static assets (anything under `blog/static/`, including illustrations)
- Template changes (`*.html`)
- Settings, urls, views, models — anything Python that the server runs

If a user says "I uploaded an image / wrote a migration last night and it's not showing on the live site," the first thing to check is whether the deploy actually ran. Compare local migrations to `railway ssh "/opt/venv/bin/python /app/manage.py showmigrations <app>"` and request the static file with curl — if either is missing, run `railway up --detach`.

### .railwayignore
Keep `.railwayignore` accurate or uploads time out. Confirmed-large dirs that MUST stay excluded:
- `.venv/` (~470MB — note the leading dot; `venv/` does NOT match `.venv/`)
- `tumor/` (~120MB), `carn/` (~225MB), `pschy/` (~96MB), `ai/` (transcripts)
- `.git/` (~80MB), `staticfiles/` (collectstatic output, regenerated on build)
- `db.sqlite3`, `.env`, `.claude/`, `.vscode/`, `__pycache__/`, `*.pyc`

If `railway up` times out with `operation timed out` on the upload step, the first suspect is something heavy that isn't in `.railwayignore`. Check with `du -ah . | sort -rh | head` and add the offender.

### Migration writing rule
Do not target articles by pillar alone — the `physiological-origin` pillar (and others) contain many articles, so `Article.objects.get(pillar__slug=...)` will crash with `MultipleObjectsReturned` and abort the migration. Always filter by `slug`, or by `pillar__slug` AND `slug` together. Use `.filter(...).first()` + `if not article: return` for defensive idempotency.

## Articles — Source transparency

When asked to write an article, **always state the source** before writing:

- **If sourced from a collected YouTube/podcast transcript** (e.g. files in `ai/`, `carn/`, `pschy/`, `tumor/` or a transcript the user pastes): say so and name the transcript/speaker.
- **If sourced from general training knowledge** (no specific transcript): say so explicitly — e.g. *"I don't have a collected transcript for this topic — I'll draw from general [field] literature in my training data. Is that OK, or do you have a transcript you'd like me to use instead?"* — before writing.

Do not silently write from training data when the user may be expecting transcript-sourced content.

## Articles — Illustrations
Every article must open with an illustration. The goal is to make the reader **want** to keep reading — choose the format that is most visually compelling for the topic, not just the easiest to produce.

Save illustrations to `blog/static/blog/illustrations/` and reference in content as:
```html
<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/<filename>" alt="..." style="width:100%;border-radius:16px;display:block;">
</figure>
```
Never inline SVG or image data into the content field.

### Format guide — pick the most interesting option per topic

| Topic area | Best format | Why |
|---|---|---|
| Protein structures, molecular biology | **Animated SVG** — atoms orbiting, helix rotating, bonds forming | Motion sells the science |
| Brain, neuroscience, consciousness | **Animated SVG** — neurons firing, signal propagating | Dynamic feels alive |
| DNA, genetics, CRISPR | **Animated SVG** — helix unwinding, base pairs highlighting | Process feels real |
| AI architecture, neural networks | **Animated SVG** — data flowing through layers, nodes activating | Shows how it works |
| Cancer, metabolism, cells | **Rich SVG diagram** — detailed cross-section, organelles, pathways | Complexity rewards looking |
| Mental illness, psychology | **Artistic SVG** — abstract emotional imagery, muted tones, texture | Mood matters here |
| Historical science (Mendel, Watson, Darwin) | **Illustrated SVG** — portrait + timeline + discovery moment | Narrative visual |
| Drug discovery, medicine | **Animated SVG** — molecule docking into receptor, lock-and-key | Shows the mechanism |
| Longevity, aging | **Rich SVG diagram** — cellular clock, telomere shortening, senescence | Visual metaphor |
| Physics, cosmology | **Animated SVG** — particles, waves, scale visualizations | Motion conveys scale |

### Animation technique (CSS keyframes inside SVG)
For animated SVGs, embed `<style>` with `@keyframes` directly inside the `.svg` file:
```svg
<style>
  @keyframes pulse { 0%,100%{opacity:0.4} 50%{opacity:1} }
  .node { animation: pulse 2s ease-in-out infinite; }
</style>
```
Stagger `animation-delay` across elements so they don't all move in sync. Keep animations subtle — they should draw the eye, not distract from reading.

### Quality bar
- Dark background `#060c16` or `#090d1a` — consistent with site palette
- `viewBox="0 0 720 420"` standard size
- Labels readable at mobile width
- At least one element that moves, glows, or pulses (for animated formats)
- Ask: *would a curious non-scientist stop scrolling to look at this?*

## GitHub
If push to indrahrp repos fails with 403, use the personal token stored at `~/claude-code-psn/.envrc`.
