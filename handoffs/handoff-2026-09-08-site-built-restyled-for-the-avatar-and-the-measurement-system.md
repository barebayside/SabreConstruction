# Handoff — 2026-09-08 — The real site built and restyled for the avatar; the measurement system; the drone hero and the one-block story

## Session Focus

One long Sabre session. Started with assets and the measurement system, ended with the real
website rebuilt around the avatar (a Bayside family at the kitchen table, 9pm, phone) in the
"LJ Hooker front lawn" tone, with an AI drone hero, a one-block picture story, a visual
"Your design" journey, a blog, and a form that slides one question at a time. Every page is
committed in the real repo. **The real repo IS PUSHED (late 09-08) and live at the Pages preview:
https://sabre-constructions.github.io/sabre-constructions-web-site-/ (noindex). Nathan has the
link to be sent. This workshop repo is NOT pushed.**

## What Got Done

**Measurement system (BBL registry)**
- Sabre is brand `SAB` in `BBL/docs/registry/brands.json` (client, `in_crm: false`; the brand
  guard skips it). Product slot `KDR`. Ad-account ids still null.
- Results block built: `meta.json → results[]`, one row per asset per week; `_regen.py` derives
  ctr/cpc/cpl (never typed; no CPL on a zero-lead week), validates source/date/five-tests
  vocabulary, renders on asset page + index tile + INDEX.md, emits `docs/registry/results.csv`.
  All five warnings tripped on a throwaway record.
- Found + fixed: every per-asset detail page had been blank since June (generator left a `null`
  after the JSON → SyntaxError).
- Eleven SAB records registered (home, contact/form, Wynnum, Manly, the rules page, testimonials,
  team, gallery, designs, blog index, first post). Every skin change today is logged on the
  homepage record's `status_history` + `change_log`.
- Zoho Analytics: setup doc verified against Zoho's connector help; Meta = one connection per
  ad account; Google joins on AD GROUP name (search ads have no ad name). Edward built the OOP
  Meta import in Analytics; Sabre's waits on ad-account access. Weekly filler script NOT written
  (waits for real columns after the first sync). The Analytics MCP token lacks scope.
- Meta accounts sorted: OOP's real ad account = the one Edward renamed "OOP" (his old "Edtest");
  BBL's = "YRHF1" (to rename); Sabre's ad account not yet assigned to Edward.

**Brand + positioning + tone**
- `docs/reference/brand/` holds the mesh-banner proof (Wild Web job 8574). Palette/type sampled:
  black `#090305`, print red `#EB2227`, Arial Bold. ⚠️ Banner QBCC no. 15486557 ≠ contact page
  328475 — ask Nathan. No vector logo ever supplied.
- `docs/reference/positioning.md` — THE spine: Nathan on call every step, takes a handful of homes
  at a time (number unconfirmed), 36 years, "they stay with you". Three-step path: walk → design
  via an architect Sabre works with → build. Front door = the walk-through, not the block check.
  Knockdown is the target but not the opening line. Problems only raised where answered.
- `docs/reference/copy-rules.md` — tone = the LJ Hooker front lawn. Story, never bullets.
- `docs/reference/design-brief.md` — the process record: 3 options → A chosen → softened → v7
  avatar skin supersedes. Options live in `design/`.

**The real site — `Desktop/sabre-constructions-website` (18 versions today, v18 current)**
- Pages: home, Your design (`/designs/`), meet the team, testimonials, Your questions answered
  (`/blog/` + 2 posts: rebuilding in Wynnum/Manly; can we knock down our house), contact, Wynnum,
  Manly, gallery (out of nav, thin, kept for the old-site URL). "Old houses & the rules" page
  removed; its content is the second post.
- Skin v7+: warm white → clean white, Figtree 400/500/600, medium headings, hairlines, ONE charcoal
  band per page, red = button + stars only. Google mark + gold stars on rating blocks.
- Home order: video hero → reviews + proof strip → "Same street. Same school. A whole new house."
  (hero-sized, Nathan's face above) → the one-block picture story (full width, auto, 4 states +
  Sabre end card, 3.6/3.6/3.6/4.2/2.6 s, words on the picture, no panel) → family (wide) →
  "In their own words" (wide; 3 AI testimonial PLACEHOLDERS served from the demo site's URL,
  labelled, NOT in this repo) → a few more questions → close = Google rating + 3 reviews beside
  the embedded form. Floating red "Book a walk-through" button on every page.
- Hero video: 10 s Kling pull-back over the widened Clarence photo, fades to black; page text
  "Build your new family home. On the street you already love." fades in. Captioned as a
  visualisation. `tools/gen_drone_hero.py`, ~$1.70 on Sabre's key.
- The one-block story frames (`tools/gen_cutaway_frames.py`, all derived from one photoreal
  old-house frame so the block holds): old house → drawings over it → build going up → family
  walking in → end card. Your design page adds: Nathan walking the house (from behind), the plans
  on the table (hands only), Nathan on site, the family at true scale in front of the new home.
  All captioned as visualisations. Sabre fal spend today ≈ $5.
- Form: 3-slide wizard (Q1 → Q2 → details+button), Back links, Formspree endpoint untouched.
  **Found + fixed: the form script had an unescaped apostrophe since 09-05 — it never ran.**
  Page scripts are now `node --check`ed after every regen.
- Phone everywhere = Nathan's mobile 0422 831 306 (from the banner; in client-facts). Council's
  07 3403 8888 untouched.
- Sitemap 11 URLs. All pages noindex.

## Files Changed / Created

| Where | What | State |
|---|---|---|
| `sabre-constructions-website/` (real repo) | everything above; `css/site.css` v18; `docs/design-system.md` rewritten (v7); `docs/client-facts.md` (designs, banner facts, mobile) | **PUSHED 09-08 late; Pages serving v18, verified by curl** |
| `Sabre Constructions/` (this repo) | `docs/reference/{brand/,positioning.md,design-brief.md,copy-rules.md,media-pipeline.md,bbl-links.md}`, `design/` (3 options + problem-section mock), `tools/gen_drone_hero.py`, `tools/gen_cutaway_frames.py`, `assets/img/cutaway/`, `assets/video/drone-clarence-*` | committed, ~35 ahead, NOT pushed |
| `BBL/docs/registry/` | brands.json (SAB), `_regen.py` (results + null fix), templates, 11 SAB records, `results.csv`, `zoho-analytics-setup.md` | committed on `feat/report-charts-and-clusters`, no remote |
| `~/.claude/skills/bbl-asset-code/SKILL.md` | client brands, KDR, weekly results section, where the code goes per platform | edited |
| Memory | sabre project, registry rule, meta accounts, MEMORY.md | updated |
| Page generator | lives ONLY in the session scratchpad (`build_sabre_pages.py`); the HTML is the artifact | ⚠️ gone next session — edit the HTML directly, or rebuild the generator from the pages |

## Decisions Made

1. Client campaigns run under the BBL registry with hand-logged weekly results → memory
   `bbl-client-campaigns-follow-the-registry`, registry README.
2. Sabre generation runs on Sabre's fal key only ("don't use my account") → memory.
3. Option A chosen, then superseded: the site is styled for the avatar, not the signage →
   `design-brief.md`, `design-system.md`.
4. Positioning: Nathan on call every step; walk-through is the front door → `positioning.md`.
5. Tone: the LJ Hooker front lawn; story not bullets; pictures first, words as captions →
   `copy-rules.md`.
6. Gallery out of the menu (URL kept); rules page → blog post; designs → "Your design" journey;
   blog → "Your questions answered" → this handoff + the pages.
7. AI testimonial clips appear on the home page ONLY as a labelled placeholder served from the
   demo site, never copied into Sabre's repo → rule 3.

## Resolved failures

- **Per-asset registry pages blank since June** · `_regen.py` replaced the comment but left the
  template's ` null` → `const ASSET = {...} null;` SyntaxError · marker now includes the null +
  a warning · found by screenshotting (Edge headless console).
- **Contact form script dead since 09-05** · `'That didn't send…'` apostrophe in a single-quoted
  string · double quotes; `node --check` on every page script after regen · found the moment the
  check was added. The form still sent via plain submit, so nobody noticed.
- **Edge headless clips below ~500 px** · Edge's minimum window width, not the layout · screenshot
  at ≥500.
- **`min-height:92vh` beat `max-height`** · CSS: min wins · `height:min(92vh,880px)`.
- **Generator template `%s` slots swallowed** twice · block replacements that spanned the `%s`
  line · replace up to the slot marker only (`repair_templates.py`, `repair_designs2.py`).
- **`git add` of a glob that matched gitignored files aborted the whole commit** · add by
  directory instead.
- **Heredoc python in Bash choked on apostrophes/quotes** repeatedly · write the script to the
  scratchpad with Write, run it with Bash.

## What's NOT Done — TODO

**Before Nathan sees it**
1. [ ] Edward: send ONE real test enquiry from the live preview (rule 4) — the form's behaviour
       changed twice today; confirm the green "Thanks" shows and the email lands in admin@.
2. [x] Pushed. Preview: https://sabre-constructions.github.io/sabre-constructions-web-site-/
       Decide whether the 3 labelled AI placeholder clips stay visible for Nathan's review.
3. [ ] Nathan to confirm: he walks the house; the architect path; "a handful" → the real number;
       walk-through is no-obligation; which QBCC number; the mobile on the site.

**Carried**
4. [ ] Catalyst promote Dev → Production (Edward), then flags → 1, re-push report v4, then send
       Nathan the competitor report link.
5. [ ] Google Ads link; Sabre ad account assigned to Edward; then Zoho Analytics SAB imports;
       then the weekly results filler script (write against real columns).
6. [ ] Real footage replaces: the drone hero, the 3 placeholder testimonial clips, the AI family
       frames. Sharpen the 6 team photos (recraft, Sabre's key). Street photos of Wynnum/Manly.
7. [ ] Design-brief §3 cutaway on a Sabre floor plan — no longer needed for the story; park.
8. [ ] Registry: log v9–v18 on the SAB records (only v8/v9 logged so far); mark the rules page
       record as moved to the blog post.
9. [ ] Strip `noindex`, sitemap domain, DNS cutover — all still waiting on Melbourne IT/iSonic.

## Quick Context for Next Session

Two folders: this workshop (`Desktop\Sabre Constructions`, read `CLAUDE.md` → `positioning.md` →
`copy-rules.md` → `design-brief.md`) and the real site (`Desktop\sabre-constructions-website`,
its own `CLAUDE.md` + `docs/`). Preview it with `python -m http.server 8765` in the real repo →
http://127.0.0.1:8765/. The page generator is NOT on disk any more; edit the HTML in place.
Before any fal job: Sabre's key per terminal. After any HTML/JS change: extract the page scripts
and `node --check` them, then screenshot with Edge headless at 1400 and 500 wide.

Most likely next task: the test enquiry, then Nathan's review of the live preview. Then his five confirmations.
