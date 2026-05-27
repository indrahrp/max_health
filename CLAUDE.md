# max_health Project — Claude Instructions

## Autonomous Operation
Operate fully autonomously on this entire project. No need to ask for permission, confirmation, or approval for any action including:
- Writing and editing articles, templates, management commands
- Committing changes to git
- Deploying via `railway up --detach` from the project root
- Installing packages, running migrations, creating new files

Complete every task end-to-end: implement → commit → deploy. Do not stop mid-task to ask the user to verify or confirm steps.

## Deployment
Always deploy with: `railway up --detach` from `/Users/iharahap/claude-code-psn/max_health/`
Never use `git push` for deployment (wrong GitHub account causes 403).

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
