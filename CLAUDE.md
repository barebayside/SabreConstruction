# Sabre Constructions — client landing pages

> **Layer 1 router.** Always loaded. Find your task in the table, open the ONE
> file it points at, and stop. Do not read the whole folder.

## What this is

A client build for **Sabre Constructions**, a family-owned builder based at
**Ransome QLD** (moved from Capalaba — confirmed 2026-09-10), building across
Brisbane's Bayside and the Redlands. Static site on GitHub Pages. No build step.

**As of 2026-08-17 this is a live engagement, not a pitch** — website, Meta ads
and Google ads, paid in kind. Everything here was built speculatively to win the
job; it has won it. Read `docs/engagement.md` before planning any work, because
the AI stand-ins that were acceptable in a demo are not acceptable on a real
commercial site.

- **Live:** https://barebayside.github.io/SabreConstruction/
- **Repo:** github.com/barebayside/SabreConstruction (main → root)
- **Audience:** Bayside families weighing up moving against rebuilding.

## Folder map

```
CLAUDE.md              you are here — the router
CONTEXT.md             Layer 2 dispatcher (task → workspace)
index.html             the main site page
ads.html               ad concepts showcase
lp-rebuild.html        LP 1 · Meta Reels 9:16
lp-raise.html          LP 2 · Meta Feed 1:1/4:5
lp-story.html          LP 3 · Google Ads desktop
css/                   sabre.css (shared) · ads.css · lp.css
js/                    sabre.js (site) · qualify.js (lead form)
assets/img/            photos · team/ · raise/ · lp/
assets/video/          reels + hero
tools/                 asset generation scripts (fal.ai + ffmpeg)
docs/                  all reference material — see docs/CONTEXT.md
                       (docs/reference/brand/ = logos, signage, print proofs)
handoffs/              dated session snapshots (NOT context — see below)
shots/                 QA screenshots (gitignored)
```

**Code stays at the root.** GitHub Pages serves `index.html` from there, so the
HTML/CSS/JS is deliberately not nested into workspace folders. The routing lives
in `docs/`.

## Routing table

| You want to... | Open first |
|---|---|
| **Know what we agreed, what we're waiting on, what's next** | `docs/engagement.md` |
| **Write ANY Sabre copy, ad or page — the one difference we sell** | **`docs/reference/positioning.md`** — Nathan on call every step; the three-step path; what Nathan must confirm |
| Change the main site page | `docs/tasks/edit-main-site.md` |
| Change a landing page or the lead form | `docs/tasks/edit-landing-pages.md` |
| Change the ad concepts page | `docs/tasks/edit-ad-concepts.md` |
| Make a video, image or reel | `docs/tasks/generate-media.md` |
| Push changes live / check the deploy | `docs/tasks/deploy.md` |
| **Point the domain at GitHub / change DNS** | `docs/tasks/dns-cutover.md` |
| **Know what replaces what / which URLs must exist** | `docs/tasks/site-migration-map.md` |
| **Where leads go, the lead ledger, the Meta feedback loop** | `docs/reference/lead-ledger-and-meta-loop.md` |
| **Build the ledger: Zoho Sheet, the two Flows, the Meta function (click-by-click)** | `docs/tasks/lead-ledger-build.md` + `tools/flow/meta_capi_event.dg` |
| **Get found on Google / the map box / AI assistants — SEO, GEO, GBP, technical** | **`docs/reference/search-and-ai-visibility-plan.md`** — canonical from 2026-09-10 |
| **Write a blog post / pick the next topic / the article bank + search estimates** | **`docs/reference/article-bank.md`** — canonical from 2026-09-10; three spirals, 45 posts, the order to write them in |
| **Plan or build any ad, campaign, budget, keyword list or measurement** | **`docs/reference/campaign-strategy.md`** — canonical from 2026-09-10; the 09-03 plan is its figures |
| Know what's blocked or fake | `docs/open-items.md` |
| Check a fact about Sabre before writing it | **`../sabre-constructions-website/docs/client-facts.md`** (canonical — in the REAL repo; the `site/docs/` copy is a dead pointer) |
| Know why a section is where it is | `docs/reference/page-structure.md` |
| **Design the look / add a reference site / the cutaway** | **`docs/reference/design-brief.md`** — the proper design process, from 2026-09-08 |
| Match colours or type | **`site/docs/design-system.md`** (canonical, but being replaced by the brief above) |
| Match the demo's motion / components | `docs/reference/design-system.md` |
| **Find a logo, signage proof or other brand file** | `docs/reference/brand/README.md` |
| **Find the method, a skill, pricing, or the FAL key** | `docs/reference/bbl-links.md` |
| See what happened last session | newest file in `handoffs/` |
| Anything else | `docs/CONTEXT.md` |

## This project runs out of Bare Bayside Labs

Sabre is a **client build**. The persuasion method, the voice rules, the pricing
model, the deploy patterns, the marketing skills and the fal.ai key all live in
BBL and are referenced from here — never copied.

```
BBL = ~/OneDrive/Desktop/Marketing AI content for Bare Bayside Labs/
```

`docs/reference/bbl-links.md` is the map. References point **outward only**:
nothing in BBL points back at Sabre, and no BBL content is duplicated into this
repo. Where a rule exists in both, BBL wins.

**Separate repo, separate brand, separate inbox.** Sabre shares BBL's method and
tooling — never its data, CRM or mailing list.

## Non-negotiables

These have all been broken at least once. Read them before editing anything.

1. **Never invent a number.** No star ratings, review counts, job counts, years
   or prices unless they're in the real repo's `docs/client-facts.md` with a source.
2. **The three testimonial videos are AI-generated people, not customers.** The
   warning panel, the per-slide chip and the burned-in label all stay until real
   footage replaces them.
3. **The lead form has no live endpoint.** `LEAD_EMAIL` in `js/qualify.js` is
   the only switch. It points at Edward, not Sabre.
4. **Bump the `?v=N` cache-buster** on `css/*.css` and `js/*.js` links in every
   page that uses the file you edited, or browsers serve stale assets.
5. **Preview chrome comes out before real ads run.** See `docs/open-items.md`.

## Naming conventions

- Files and folders: `lowercase-with-hyphens`. No spaces.
- Landing pages: `lp-{angle}.html`
- Generated assets: `{purpose}-{variant}.{ext}` — e.g. `reel-1.mp4`, `after-2.jpg`
- Upscaled originals keep a prefix: `proj2x-` (2x), `t-` (team)
- Handoffs: `handoffs/YYYY-MM-DD-handoff.md`
- Tool scripts: `tools/{verb}_{noun}.py` or `.sh`

## Trigger keywords

- **`status`** — read `docs/open-items.md` and report what's blocked.
- **`handoff`** — write a dated snapshot into `handoffs/`.
