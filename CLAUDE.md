# max_health Project — Claude Instructions

## Autonomous Operation
Operate fully autonomously on this entire project. No need to ask for permission, confirmation, or approval for any action including:
- Writing and editing articles, templates, management commands
- Committing changes to git
- Deploying via `railway up --detach` from the project root
- Installing packages, running migrations, creating new files

Complete every task end-to-end: implement → commit → deploy. Do not stop mid-task to ask the user to verify or confirm steps.

## Mobile compatibility (required)
The site (cogitra.com) MUST render and read well on **iPhone (Safari)**, **iPad (Safari)**, and **Android (Chrome)**. Mobile is a first-class target, not an afterthought.

- Every page must be usable on a phone: navigation reachable (hamburger menu at ≤980px — do not hide nav links without a mobile replacement), text legible without zoom, images fluid (`width:100%`, never fixed pixel widths that overflow), nothing clipped off-screen or requiring horizontal scroll.
- Keep the `<meta name="viewport" content="width=device-width, initial-scale=1.0">` tag in `base.html`.
- Illustrations/figures must scale down cleanly and keep labels readable at ~360px width.
- After any change to layout, nav, or templates, sanity-check the responsive behavior (media queries at 980px and 560px) before deploying.

### Breakpoints (use consistently across all templates and article content)

| Breakpoint | Target | Required behavior |
|---|---|---|
| ≥981px | Desktop | Full multi-column layouts, nav links visible inline |
| ≤980px | Tablet (iPad) | Hamburger nav; grids may stay 2-up but no horizontal scroll |
| ≤760px | Phone | Multi-column article figures, side-by-side blocks → **single column** |
| ≤560px | Small phone (iPhone SE) | Tighter padding (`0 16px`), 1-column for all grids, smaller heading sizes |

### Article reader template — current mobile rules (article_detail.html)

The reader template already has these responsive rules. Do not remove them:
- **≤700px**: `reader-body` padding → `28px 24px 40px`; `reader-h1` → 28px; `reader-dek` → 17px; drop cap → 48px
- **≤560px**: `reader` outer padding → `0 16px 48px`; `reader-body` → `22px 18px 36px`; `reader-h1` → 24px; `other-articles-grid` → 1 column

### Article content rules (HTML stored in the DB)

Article content is raw HTML injected via `{{ article.content|safe }}`. It cannot reach template CSS, so all responsive styles must be inline or in a scoped `<style>` block inside the content.

**SVG illustrations** — always use `style="width:100%;border-radius:16px;display:block;"`. Never set a fixed pixel width. `viewBox="0 0 720 420"` is the standard canvas.

**HTML tables** — always wrap in an overflow container:
```html
<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2em 0;">
  <table>…</table>
</div>
```
Without this, wide tables cause horizontal scroll on phones.

**Multi-column grids inside articles** — use a scoped `<style>` block with a unique class name:
```html
<style>
.my-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
@media (max-width:760px) { .my-grid { grid-template-columns:1fr; } }
</style>
<div class="my-grid">…</div>
```
Example reference: `anxiety-gaba-amygdala-physiological-origin` — 3-up panels on desktop, single column at ≤760px.

**Wide infographics & dense composed images** — a single wide image shrinks to unreadable at 360px. Split into pieces and use a responsive grid:
- Crop with PIL: title strip, each panel, footer strips.
- Upload each piece to Cloudinary under `cogitra/<article-slug>-<piece>` (cloud: `dxmrrtzha`).
- Use CSS grid with `1fr` at ≤760px.

### Things to never do
- Fixed pixel widths on figures (`width:720px`) — always `width:100%`.
- `min-width` on any block inside an article body — causes horizontal scroll.
- `<table>` without an `overflow-x:auto` wrapper.
- Multi-column grid in article content without a `@media (max-width:760px)` stacking fallback.
- Hiding nav links with `display:none` at mobile without a hamburger/drawer replacement.
- `font-size: clamp(Xpx, ...)` where X is larger than ~32px — the clamp minimum applies on phones and can still be too large (e.g. `clamp(48px,...)` stays at 48px on a 375px screen).

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

### Management-command writing rule (CRITICAL)
Commands in `nixpacks.toml` (currently `load_autoimmune_diseases`, `load_eagleman_brain_mind`) **run on every deploy**. They MUST NOT overwrite `Article.content` on existing rows, or any manual edit (e.g. swapping in a Cloudinary or static illustration) gets wiped on the next `railway up`.

The bug pattern to avoid:
```python
Article.objects.update_or_create(
    slug=data['slug'],
    defaults={'content': data['content'], ...},  # ← wipes manual edits every deploy
)
```

The correct pattern (used by `load_autoimmune_diseases` and `load_eagleman_brain_mind` after the 2026-05-28 fix):
```python
obj, created = Article.objects.get_or_create(
    slug=data['slug'],
    defaults={'content': data['content'], 'title': ..., 'summary': ..., 'pillar': pillar, 'published': True},
)
if not created:
    # Preserve content on existing rows. Update other safe fields explicitly.
    obj.title = data['title']
    obj.summary = data['summary']
    obj.pillar = pillar
    obj.published = True
    obj.save(update_fields=['title', 'summary', 'pillar', 'published'])
```

If you add a new bootstrap command to `nixpacks.toml`, audit it for this pattern first. If a command is one-shot (run by hand to seed a new article), it can safely overwrite — but don't put it in the build phase.

### Image-storage workflow (CRITICAL)
**Never rely on ChatGPT / DALL-E / temporary AI-host URLs** (e.g. `chatgpt.com/backend-api/estuary/...`, `files.oaiusercontent.com`, `sdmntp...openai.com`) for production article illustrations. Those URLs are auth-gated and/or expire within hours; the image vanishes.

**The default rule, no exceptions:** whenever the user hands you an image to put on an article — whether by **pasted image**, **ChatGPT/AI-host URL**, **public URL**, or **local file path** — upload it to Cloudinary first, then reference the Cloudinary `secure_url` in the article HTML. Do not paste a temporary URL into the article content even "for now."

**Storage options (Cloudinary is the default):**
1. **Cloudinary (default)** — upload to `cogitra/<article-slug>` (cloud: `dxmrrtzha`). Use the article's slug as the `public_id` so it's discoverable later. For multi-piece infographics, use `cogitra/<article-slug>-<piece>`. Survives deploys; no static rebuild needed.
2. **`blog/static/blog/illustrations/`** — commit the image to the repo; reference as `/static/blog/illustrations/<filename>`. Requires a deploy to publish, and survives deploys after that. Use this when the user explicitly wants the image in version control.

**Standard pipeline for user-provided images:**
```
1. Save/copy the image locally (optimize with PIL: width ≤ 1400, JPEG quality 88).
2. Base64-chunk and ship to prod (~90KB per chunk via `railway ssh "printf '%s' '$DATA' >> /tmp/x.b64"`).
3. Decode and upload via cloudinary.uploader.upload(path, folder='cogitra',
       public_id=<article-slug>, overwrite=True, resource_type='image').
4. Swap the article's <figure>...</figure> to <img src="<secure_url>"> via regex on `content`.
5. Verify both article URL and image URL return 200.
6. macOS-tar note: use `COPYFILE_DISABLE=1 tar --no-xattrs` to avoid AppleDouble (._) files.
```

When a user says "I uploaded an image and it disappeared," check three things in order:
1. Is the article's content field still pointing to the image URL? (DB inspect)
2. Is the image URL still live? (`curl -I`; AI-host URLs return 403/404 after expiry)
3. Is the article being overwritten by a `load_*` command in `nixpacks.toml` on every deploy?

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
