# Task: change the ad concepts page

> **Layer 3 contract.** Scope: `ads.html`, `css/ads.css`. This page is a
> **review deliverable for Edward and the client**, not a customer-facing page.

## Inputs

| Source | File | Section / Scope |
|---|---|---|
| Blockers | `../open-items.md` | Full file |
| Facts | `../reference/client-facts.md` | Only the rows you're about to state |
| Voice | `../reference/copy-rules.md` | Full file |
| The three Meta routes | `../reference/lead-capture.md` | § *The three Meta routes* |
| How each asset was made | `../reference/media-pipeline.md` | The relevant asset's section |
| Paid ads method | see `../reference/bbl-links.md` | `BBL/docs/reference/paid-ads-playbook.md` |
| The page | `../../ads.html` | The section you're changing |

## Process

1. Read the blockers.
2. Edit the relevant block. The page has five: who it's for, video concepts,
   where the questions go, the three LPs, image ads, copy bank, production notes.
3. Keep every honesty flag intact — the AI-visualisation note on Concept 02 and
   the AI-stand-in note on Concept 03 are not decoration.
4. If an LP changed visibly, regenerate its card preview (see
   `edit-landing-pages.md` Outputs).
5. Bump `?v=N` if you touched `css/ads.css`.

## Audit

| Check | Pass condition |
|---|---|
| Every status is honest | "Built — ready" only where it genuinely is |
| Character counts | Copy bank counts match the actual strings |
| Card previews | Letterboxed, not cropped. Each labelled with its medium |
| No unflagged AI content | Every generated asset carries its caveat |

## Outputs

| Artifact | Location |
|---|---|
| Edited page | `ads.html` |

Then follow `deploy.md`.
