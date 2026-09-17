# Handoff — 2026-09-17 — Article kit v22→v23: 21 posts, sticky rail, a made image per article, footer social

## Session Focus

Edward asked for the Sabre blog pages brought up to the Project 24 / BBL / Tried & Traded
standards, and for the list of articles that will help Sabre rank locally per the competitor
report. The list already existed (`docs/reference/article-bank.md`, canonical since 09-10); this
session built the standards into the pages.

## What Got Done

**`css/site.css` v22 — the article kit** (appended, nothing above it changed)
`.art-meta` byline row (Nathan's photo, date, reading time) · `.answer` the self-contained
short-answer card · `.onpage` on-this-page list · `.proof` attributed proof point (ink hairline,
`<cite>`) · `.pts` point lists · `.takeaways` · `.qa` common questions · `.sources` · `.related`
keep-reading cards (reuses `.posts`). Hairlines and paper only; red stays on the button.

**All four posts rebuilt in place** (`<main>` replaced; header/footer untouched):

| Post | Words | Answer block | Proof points | Notes |
|---|---|---|---|---|
| what-is-a-knockdown-rebuild-package (R15) | 1,406 | 154 | Lesley W review Apr 2020 · QBCC $3,300 Home Warranty | "genuinely" ×5 → 0; H2s now questions |
| check-if-your-street-is-in-the-character-overlay (R2) | 1,283 | 136 | Council overlay purpose · Archives register gaps | "other ways to date a house" → points |
| can-we-knock-down-our-house (R1) | 912 | 133 | Council overlay wording · Roselia Finlay Jan 2022 | date 8 Sep + byline added; FAQ (4) + takeaways added; demolition-code cases → points |
| rebuilding-in-wynnum-or-manly | 1,072 | 140 | Council overlay purpose · Jason Turner Jun 2025 | date + byline added; block factors → points |

Every post: H2 every ~200 words and phrased as a question · 1–3 sentence paragraphs · key
takeaways · common questions · one CTA band · Nathan Brain byline with a real date · updated
17 Sep on the two older ones. Quotes are verbatim from `client-facts.md` "cleared for use".

**First JSON-LD on the site.** `Article` + `FAQPage` `@graph` on all four posts — author Person
Nathan Brain → `/meet-the-team/`, publisher Organization `#org`, dates, wordCount, image, canonical
URLs on `www.sabreconstructions.com.au` (matches `sitemap.xml`). Article-bank §7 item 8 CLOSED.
LocalBusiness on the home page is still owed.

**Blog index** carries real dates (8 Sep) on the two older cards. **Cache-buster v21 → v22 on
all 13 pages.** Verified: JSON parses, every internal link and anchor resolves, no `overflow:hidden`
on any band, screenshots at 1400 and 520 clean top to bottom.

**Committed `4d4d11d`, push started in the background** (this repo's push hangs then lands — check
`git status -sb` before assuming).


## Later the same day — Phase 1 written and built (six new posts), the giant builder fixed

**The image.** Edward: one card image had "the man twice as tall as the building" and asked
whether an old fal model was used. It was `fal-ai/nano-banana-2` (current); the fault was the
09-08 edit prompt with no scale anchor. Regenerated `design-3-site.jpg` from the same source
frame with the door-height anchor (2 variants, ~16c on Sabre's key; one came back ant-sized —
this model needs the anchor AND a look). Swapped on all six pages with `?v=2`. Prompt fixed in
`tools/gen_cutaway_frames.py`; giant original kept as `design-3-site-v1-giant.jpg`. Pushed `4c10188`.

**Six posts** (R9, R19, S9, R33, S12, R16) written, built, verified, committed `8b36752`, push
started (this repo's push hangs — check `git status -sb`). Sources were fetched and quoted
verbatim on the day: asbestos.qld.gov.au, BCC FloodWise Property Reports, QBCC (About, registers,
Home Warranty), SLQ *Housing a growing state* 2014. The fetched text sits in the session
scratchpad only; the quotes are in `tools/posts_phase1.py` with their source lines.

**The builder is now in the repo:** `tools/build_post.py` + `tools/posts_phase1.py`. Content is
the Python dict; the page shell is copied from the package post; schema, index card and sitemap
row are generated; links/anchors/JSON verified in a second pass. **Edit the dict and rebuild;
don't hand-edit the six HTML files** (the reverse of the BBL rule, because here the generator
IS the source).

**Honest lengths:** S9 1,379 and S12 1,279 words — response length, not the bank's staple
length. Extending them needs Nathan's material. R16 names no rival builder (ACL, same as R15).
Real project photos on the six new cards; the four older cards keep the story frames.

**Article bank updated:** Phase 1 marked done, ten rows flagged live, §7 item 8 closed.

## Later still — Phase 3, the place cluster: eleven more posts (21 on the site)

Built from `tools/posts_phase3a.py` (S7, S8, S10, R23, R24, R25) and `posts_phase3b.py` (R27, R28,
R29, R31, R35). Committed `9bdddad` in the real repo, **NOT pushed** — the push is blocked by Git
Credential Manager, which pops a window this session can't see; **Edward runs `git push origin main`
in his own terminal.** That is also the real cause of every "push hangs" note in earlier handoffs:
stale `git-credential-manager.exe` processes waiting on a prompt. `taskkill` them before retrying.

Research that went in: ABS 2021 Census read directly for Wynnum, Manly, Lota, Manly West;
qld.gov.au catchment wording; BCC FloodWise; BCC Severe Weather Alert ("October to March");
Get Ready Queensland "Protect your home"; one Translink midday timetable sample (Central 12:17 →
Wynnum Central 12:57); Wikipedia suburb histories, attributed as such. Prices, rents and mortgage
figures deliberately excluded everywhere. One invented car-time range was caught and removed
before build — the rule bites even in a commute post.

Not written: R26 and R34 (price posts — no honest path), R30, R32. `builder` change: cards are
read from every `posts_*.py` so modules can cross-link; cross-module links need the other module
built first (build b, then re-run a).


## v23 — Edward's correction and what it produced

Edward, after seeing the 21 posts: **(1)** the right-hand "On this page" menu was missing — he wants
the BBL / T&T sticky rail, not a list under the answer; **(2)** "stop recycling the images" — every
article gets its own image; **(3)** images follow Sabre's existing visual language and colour construct;
**(4)** each image is a *concept for the topic* (his example: a map with Ransome/Tingalpa/Gumdale
outlined and acreage shown); **(5)** the image appears on the article page itself, not just the card.
Plus **(6)** Facebook and Instagram icons in the footer. Repeated back, confirmed "that's correct".

**Built (commit `cdd5826`, push waiting on the GitHub sign-in window):**
- `css/site.css` v23: `.art-grid` (66ch prose + 232px sticky `.art-side`), `.art-hero` (2:1 header,
  3:2 on phones), `.social`. `js/article.js` = scroll-spy for the rail. Rail hides ≤1040px; the inline
  `.onpage.inline` list shows instead. Builder emits both from one nav; `tools/retrofit_v23.py` did the
  four hand-built posts + footer + cache-buster on all 30 pages.
- **14 maps and diagrams** — `tools/gen_blog_maps.py`. Real suburb polygons from OSM Nominatim (cached
  in the session scratchpad `geo/` — refetch if needed, ~1 s per suburb, UA header required), Sabre
  palette + one water tone, Figtree via an HTML wrapper rendered by headless Edge (fonts don't load in
  an `<img>` SVG). ODbL attribution drawn into every map. **No flood extents or catchment lines drawn —
  pins and boundaries only.** Diagrams (commute, flood sources, floor level, three dates, two checks)
  are schematic and say so.
- **7 illustrations** — `tools/gen_blog_images.py`, nano-banana-2/edit on SABRE's key with
  `cutaway/build-same-block.jpg` as the style reference, scale anchors, no faces/text/logos, 2 variants
  each and picked by eye (~$1.20). Alternates in the workshop `assets/img/blog-alternates/`. All show
  people only from behind or in PPE — same line as the accepted story frames; rule 3 still means no
  AI person presented as a client.
- Footer: Facebook icon live. **Instagram icon is in the markup but `hidden`** — the only public
  handle Google finds, `@sabreconstruction`, is a civil/earthworks company, not Nathan. Ask him.
- Blog index cards and the four hand-built posts' related cards repointed; schema `image` updated.

**Lesson:** `class="wrap art-grid"` — a guard that greps for `class="art-grid"` misses it. Grep for
the token, not the attribute.

## Decisions Made

1. **R1 stays at 912 words, not the 1,000+ the bank asks for.** The only honest way past 1,000 is
   Nathan's own material (his DA timeframe, a job). Padding it with unsourced approvals prose would
   break rule 1. → wait for the voice note.
2. **A named Google review counts as one of the two proof points** — the bank allows it, and it is
   the only Sabre-specific evidence on the site until Nathan speaks.
3. **The FAQ is visible text (`.qa`), not `<details>`** — AI assistants and Google read visible Q&A;
   the existing `.faq details` component stays for the home page.
4. **FAQPage schema included** despite Google's rich-result restriction — it costs nothing and the AI
   lane reads it.

## What's NOT Done — TODO

1. [ ] **Confirm the push landed** (`git status -sb` → `## main...origin/main`, no "ahead").
2. [ ] **"Nathan takes on a handful of homes at a time"** (Wynnum post §4) is one of the five
       positioning claims he has never confirmed — carried from 09-08, not introduced today.
3. [ ] **Every post still lacks "one thing Nathan actually said."** Voice note owed (bank §7 item 6).
3b. [ ] **Nathan: the Instagram handle** — the icon is built and hidden; unhide by removing `hidden` + `href` in every footer (30 pages, sed).
4. [ ] `LocalBusiness` schema on the home page, robots.txt, llms.txt, Google tag — plan §7.
5. [x] ~~Phase 1~~ and ~~Phase 3~~ DONE (21 posts). Next that needs nobody: Phase 4 trust posts
       (R37 defects period, R45 what's in a quote, R36 insurance, R39 contracts, R40 builder goes under,
       R41 owner-builder, R42 certifiers, R43 building and pest) — `posts_phase4.py`.
6. [ ] Registry: log v22 on the SAB records (v9–v21 also still unlogged).
7. [ ] Everything in the 09-10b handoff's Edward/Nathan lists still stands (GBP → Ransome, DNS,
       test enquiry, Google Ads link, the credit question).

## Quick Context for Next Session

The kit is the pattern and **`tools/build_post.py` is the generator** — a new post is a dict in a
`tools/posts_*.py` module (see `posts_phase1.py` for the shape), then `python tools/build_post.py
posts_x`. It writes the page, the index card, the sitemap row and the schema, and verifies links.
The four original posts (R1, R2, R15, Wynnum) are hand-built HTML — edit those in place. Bump
`?v=` on all 19 pages after any CSS change. Preview: `python -m http.server 8765` in the real repo.

## v25 — click heroes, labels, maps inside (later on 2026-09-17)

Nathan-side feedback via Edward: the card image has one job — make someone click. Maps and diagrams
explain, they don't pull. So every post now carries **two images**:

- **Hero/card** — a photographic scene in Sabre's frame style (`tools/gen_blog_heroes.py`, 14 scenes,
  two variants each, picked by eye from contact sheets; alternates in `assets/img/blog-alternates/*-hero-v*.jpg`).
  Real places (Wynnum jetty, Manly harbour, Lota creek, the acreage, a station) are captioned
  *"Illustration in the style of Sabre's story frames, not a photograph of the real street."*
- **Label** — post field `label=(kicker, big)`, e.g. `("The Bayside suburbs", "Wynnum")`. Rendered as HTML
  (`.label` inside `.thumb`) on the card and the hero — never baked into the pixels.
- **Figure** — post field `figure=dict(image, alt, caption, after=<h2 id>)`; the old map/diagram PNG is
  placed after the first paragraph under that H2 (`build_post.place_figure`). All 14 PNGs kept.

Pipeline: `tools/retrofit_v25_posts.py` patched the 17 dicts (one-off, idempotent);
`tools/retrofit_v25_hand.py` did the four hand-built posts in place; `build_post.py` / `build_blog_index.py`
now emit `<span class="thumb"><img>{label}</span>`. CSS v25 appended; cache-buster on all 30 pages.
Commit `a45817c` pushed (no GCM prompt this time). The seven earlier illustrations kept, labels added.

Known: headless-Edge phone screenshots at 420px show the page wider than the window on EVERY page
including the untouched home page — a screenshot artifact, not a v25 regression. Instagram still hidden.
