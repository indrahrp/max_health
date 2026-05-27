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

## Articles
Every article needs an SVG illustration. Save it as a file at `blog/static/blog/illustrations/<article-slug>.svg`, then reference it in the article `content` field as:
```html
<figure style="margin:1.5em 0 2.5em;">
<img src="/static/blog/illustrations/<article-slug>.svg" alt="..." style="width:100%;border-radius:16px;display:block;">
</figure>
```
Never inline the SVG code into the content field. Always place the figure at the top of the content.

## GitHub
If push to indrahrp repos fails with 403, use the personal token stored at `~/claude-code-psn/.envrc`.
