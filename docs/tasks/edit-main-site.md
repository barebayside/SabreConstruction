# Task: change the main site page

> **Layer 3 contract.** Scope: `index.html` only. If you're touching a landing
> page, you're in the wrong contract.

## Inputs

| Source | File | Section / Scope |
|---|---|---|
| Blockers | `../open-items.md` | Full file |
| Facts | `../reference/client-facts.md` | Only the rows you're about to state |
| Voice | `../reference/copy-rules.md` | Full file — it's short |
| Why sections sit where they do | `../reference/page-structure.md` | § *`index.html` — the main site page* |
| Visual tokens | `../reference/design-system.md` | § *Palette*, § *Type*, § *Rules that keep getting broken* |
| The page | `../../index.html` | The section you're changing |
| Shared styles | `../../css/sabre.css` | The component block only |

Do **not** open `ads.html`, `lp-*.html`, `css/lp.css`, `js/qualify.js` or
anything in `tools/`.

## Process

1. Read the blockers. If your change touches a 🔴 item, say so before editing.
2. Find the section in `index.html` — they're numbered in HTML comments
   (`<!-- ============ 4 · TESTIMONIALS — Proof ============ -->`).
3. Check any fact you're about to state against `../reference/client-facts.md`.
4. Make the edit.
5. **If you touched `css/sabre.css` or `js/sabre.js`, bump `?v=N`** in every
   page that links it: `index.html`, `ads.html`, `lp-*.html`.
6. Run the audit below.
7. Screenshot: `py -3 tools/shoot.py` (from the repo root).

## Audit

| Check | Pass condition |
|---|---|
| No invented facts | Every number and claim traces to `../reference/client-facts.md` |
| Cache-buster | `?v=N` bumped on every page linking the edited asset |
| Console | `shoot.py` run reports no console errors |
| Broken images | Zero, excluding the lightbox `<img>` which has no `src` until opened |
| Mobile | Section still works at 390px wide |
| Section still answers a test | If it answers none, cut it |

## Outputs

| Artifact | Location |
|---|---|
| Edited page | `index.html` |
| QA screenshots | `shots/` (gitignored) |

Then follow `deploy.md`.
