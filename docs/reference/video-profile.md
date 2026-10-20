# Video profile: Sabre Constructions (`SAB`)

> ⭐ **Brand kit (look + voice, read by the BBL video engine and /brand-review):** `docs/brand-kit.json`. Built 2026-10-01 from the real site + positioning.md.

> **Layer 4.** Everything BBL's shorts pipeline needs that is unique to Sabre. The pipeline itself is
> BBL's: `BBL/docs/pipelines/video-production/shorts/CONTEXT.md` (see `bbl-links.md`). This file
> points to Sabre's own files and never copies them.

## Accounts

| What | Where |
|---|---|
| Page, IG, Meta ad account, Google Ads, Postiz group | `BBL/docs/registry/brands.csv`, row `SAB` |
| Asset codes | `/bbl-asset-code`, brand `SAB` |

## Look

| What | Canonical file |
|---|---|
| Colours + fonts | `design-brief.md` §1 (read off Sabre's signage). `site/docs/design-system.md` until the brief is decided |
| Logos, signage | `brand/README.md` |
| What we say (the one difference we sell) | `positioning.md` |

## Assets

| What | Where | Allowed? |
|---|---|---|
| Videographer footage, drone, site clips | WorkDrive `VIDEO\` (see `asset-storage.md`); web cuts in `assets/video/` | Rung 1. ⚠️ Clip picks go to Edward until taste rules exist |
| Job photos | `assets/img/` | Rung 1 |
| Real frame → AI continuation | `docs/tasks/generate-media.md` (start and end frames pinned) | Rung 3. Must land on a real Sabre photo, or be captioned as a visualisation |
| Pure AI (house going up, context) | BBL `templates.yml` copy | Rung 4, fill only. Never shown as a Sabre job |
| AI people | — | ⛔ Only with a burned-in "AI" label (the testimonial rule in `CLAUDE.md`) |

## Presenter

Nathan (owner). Avatar: **not made. No consent on file (2026-09-28).** He needs to supply:

- a 2–5 min neutral take
- a phone consent recording
- a written likeness release

**Route changed 2026-10-20 (trial tool only, not approved for live production):** not a HeyGen/photo avatar. Lip sync on Nathan's REAL raw footage +
his cloned voice (fal sync-3 + MiniMax, ~$2 per 15 s), proven on Edward; still-photo avatars looked
"absolutely horrible". Method + guardrails: BBL `docs/pipelines/video-production/presenter-lipsync.md`.
Voice and footage stay in **Sabre's** accounts (Sabre's fal key). Nathan signs off every script before it
is rendered, and no variant may contradict another. Until then: blog-post shorts use voice-over or text only, with no face.

## Sources

- Blog: `article-bank.md` (55 posts + 3 hubs live)
- Filmed jobs (WorkDrive `VIDEO\`)
- Testimonials (Leanne: consent for paid ads still open)

## Asset types

| Asset type | Source | Presenter | Rungs | Destination / CTA | Extra gates |
|---|---|---|---|---|---|
| Blog-topic short | Blog post | Nathan's avatar (once consented) | 1, 3, 4 | The article → quote form | Facts checked against `client-facts.md`; Nathan approves the script |
| Job / progress reel | Filmed job | None or Nathan (real) | 1, 3 | Landing page | `generate-media.md` audit |
| Testimonial cut-down | Leanne video | Leanne (real) | 1 | Landing page | Her consent for paid ads first |
| Meta video ad | Any of the above | As above | As above | `campaign-strategy.md` | `/bbl-ad-build` gates; AI box ticked |

## Hard rules

- `positioning.md` (what Nathan must confirm)
- `client-facts.md` (canonical in the real repo, per `CLAUDE.md`)
- `open-items.md`

## Storage

Finished files go in WorkDrive `VIDEO\`, named by asset code (`asset-storage.md`). The record goes
in `BBL/docs/registry/marketing-assets/SAB-…/`.
