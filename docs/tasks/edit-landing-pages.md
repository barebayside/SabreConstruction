# Task: change a landing page or the lead form

> **Layer 3 contract.** Scope: `lp-rebuild.html`, `lp-raise.html`,
> `lp-story.html`, `css/lp.css`, `js/qualify.js`.

## Inputs

| Source | File | Section / Scope |
|---|---|---|
| Blockers | `../open-items.md` | Full file |
| The form: questions, relay, config, why it's five screens | `../reference/lead-capture.md` | Full file |
| Which page is for which medium | `../reference/page-structure.md` | § *The three landing pages* |
| Facts | `../reference/client-facts.md` | Only the rows you're about to state |
| Voice | `../reference/copy-rules.md` | Full file |
| Visual tokens | `../reference/design-system.md` | § *Palette*, § *Type* |
| The page | `../../lp-{angle}.html` | Full file — they're 80–130 lines |
| LP styles | `../../css/lp.css` | The component block only |
| Form logic | `../../js/qualify.js` | Only if changing behaviour |

Do **not** open `index.html`, `ads.html` or `css/sabre.css` unless you're
changing a shared token.

## Process

1. Read the blockers.
2. Confirm which medium the page serves — it's in an HTML comment at the top and
   printed on the page as a pill. Reels needs succinct; Google desktop can carry more.
3. Make the edit.
4. If you changed `js/qualify.js` or `css/lp.css`, bump `?v=N` on **all three** LPs.
5. Run the audit.

## Audit

| Check | Pass condition |
|---|---|
| Form is embedded and open | `data-qualify-inline` renders question 1 with no click |
| Modal stays a fallback | Only fires at page bottom, and never once they've started |
| Mobile fit | No horizontal overflow at 390px. Nothing runs past the video |
| Tap targets | 56px minimum on every option and input |
| Five questions intact | Order unchanged: type → plans → suburb → budget → mobile |
| Placeholders still flagged | Budget bands and star strip still carry their warning chips |
| Preview chrome | Switcher and medium pill present for review, listed in `../open-items.md` for removal |

## Outputs

| Artifact | Location |
|---|---|
| Edited page(s) | `lp-*.html` |
| Refreshed card previews | `assets/img/lp/lp-*.jpg` — regenerate if the page changed visibly, `ads.html` uses them |

Then follow `deploy.md`.
