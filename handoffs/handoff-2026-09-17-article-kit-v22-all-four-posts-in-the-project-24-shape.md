# Handoff — 2026-09-17 — The article kit (v22): all four posts in the Project 24 shape, first schema on the site

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
5. [ ] Phase 1 of the bank (seven posts needing nobody): build with the kit — copy any post's
       `<main>`, keep the block order, run the splice checks (schema parses, links, anchors, v= bump).
6. [ ] Registry: log v22 on the SAB records (v9–v21 also still unlogged).
7. [ ] Everything in the 09-10b handoff's Edward/Nathan lists still stands (GBP → Ransome, DNS,
       test enquiry, Google Ads link, the credit question).

## Quick Context for Next Session

The kit is the pattern now. A new post = one of the four `<main>` blocks with the body swapped,
plus the `@graph` block (author, publisher, dates, FAQ) — the splice script that built these lived
in the session scratchpad and is described above; rebuild it in 30 lines if needed rather than
hand-editing schema. Bump `?v=` on all 13 pages after any CSS change. Preview:
`python -m http.server 8765` in the real repo.
