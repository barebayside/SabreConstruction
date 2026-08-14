# Dispatcher

> **Layer 2.** Routing only. No rules, no reference material — those live in
> `docs/reference/`.

## What is this folder?

The Sabre Constructions demo build: one main site page, one ad-concepts page,
three ad landing pages, and the scripts that generated the media.

## Where do I go?

| Work type | Contract | Touches |
|---|---|---|
| Main site page | `docs/tasks/edit-main-site.md` | `index.html`, `css/sabre.css`, `js/sabre.js` |
| Ad landing pages + lead form | `docs/tasks/edit-landing-pages.md` | `lp-*.html`, `css/lp.css`, `js/qualify.js` |
| Ad concepts showcase | `docs/tasks/edit-ad-concepts.md` | `ads.html`, `css/ads.css` |
| Video / image generation | `docs/tasks/generate-media.md` | `tools/`, `assets/` |
| Publishing | `docs/tasks/deploy.md` | git, GitHub Pages |

## What loads on every task, regardless

| Source | File | Scope |
|---|---|---|
| Router | `CLAUDE.md` | Full file — already loaded |
| Blockers | `docs/open-items.md` | Full file |

Everything else is named in the contract for your specific task. Load nothing
that isn't listed there.

## Reference material (Layer 4)

Do not read these speculatively. A task contract will tell you which sections
you need.

| File | Holds |
|---|---|
| `docs/reference/client-facts.md` | Every verified fact about Sabre + its source |
| `docs/reference/design-system.md` | Palette, type, motion, components |
| `docs/reference/page-structure.md` | Section order and the reasoning behind it |
| `docs/reference/copy-rules.md` | Voice, what may and may not be claimed |
| `docs/reference/lead-capture.md` | The five questions, the relay, the config |
| `docs/reference/media-pipeline.md` | How every video and image was made |
| `docs/reference/bbl-links.md` | Where this plugs into Bare Bayside Labs — method, skills, pricing, keys |

## Handoffs

`handoffs/` holds dated session snapshots. They are **history, not context** —
read the newest one to catch up on what happened, never as a source of rules.
Rules live in `docs/reference/`.
