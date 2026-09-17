# Handoff — 2026-09-17 — The article kit (v22), ten posts live, Phase 1 of the bank done, the builder frame fixed

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
