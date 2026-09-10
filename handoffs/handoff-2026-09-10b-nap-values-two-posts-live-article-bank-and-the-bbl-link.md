# Handoff — 2026-09-10 (second session) — Nathan's three values, two posts built and live, the article bank, and the BBL link

## Session Focus

Edward asked what had been left half-finished on Sabre, then gave Nathan's confirmed licence
numbers and new address, asked for the site pushed, and asked for the blog content built out
following Project 24 with search estimates. Ended on cross-linking Sabre and Bare Bayside Labs.

## What Got Done

**The audit — what was actually unfinished**
- v19 (the 09-10 contact-form fix) was **committed and never pushed**. The contact form had been
  unsubmittable on the live preview since 09-08 — on the page every "Book a walk-through" button
  leads to. This was the highest-value item on the list and nobody had noticed.
- Ledger: site side done, Zoho side written but not built (`FLOW_URL` still empty).
- No robots.txt, no llms.txt, **no schema on any page** (0 JSON-LD blocks), no analytics tag.
- Eight of ten campaign launch gates still ⛔. Workshop repo 40 commits ahead, unpushed.

**Nathan's three values — replaced across the whole site (real repo v20)**
- **QBCC 15486557** replaced 328475 in 15 places. This closes the "two QBCC numbers" flag from
  09-08 — the banner proof's number was the right one.
- **Master Builders Queensland 00352** confirmed (already on the pages).
- **40 Molle Rd, Ransome QLD 4154** replaced 3/73–75 Steel St, Capalaba QLD 4157 in every footer,
  the contact page, the contact meta description and both suburb pages' "home base" blocks.
- Location prose that named Capalaba as home now says Ransome or "Brisbane's Bayside". Capalaba
  stays in the service-area lists and the suburb dropdowns — they still build there.
- **PUSHED.** v19 + v20 both live on the preview. Verified on the live page.

**Two blog posts built and pushed (v21)**
- `content/` was **untracked in git** and held **9,508 words of finished copy** nobody knew was
  there. Two posts had `blocked_on: []` and had simply never been built.
- `/blog/check-if-your-street-is-in-the-character-overlay/` — the two free checks (council's City
  Plan mapping for the overlay; Brisbane City Archives for the build year), a four-row table of
  what each combination means, the archive gaps (1934–36, 1937, 1939, 1941 index-only).
- `/blog/what-is-a-knockdown-rebuild-package/` — what an advertised package bundles, who it suits,
  where it stops, six questions worth asking any builder including Sabre.
- Both: date, Nathan's byline, self-contained short answer at the top, Common questions block,
  one CTA. In the blog index, in `sitemap.xml`, cross-linked to the existing posts.
- **The two ⛔ GAP markers were CUT, not filled.** The DA-timeframe FAQ is out until Nathan gives
  his own number — the draft's own instruction, and rule 1.
- `site.css`: prose tables and lists had **no styling at all**. Added, table in an `overflow-x`
  wrapper. Cache-buster v=19 → v=21 across all 13 pages.
- Corrected both older posts: council's tool is the **Maps Tools** panel and the **Overlays**
  layer, and it generates a **property report** — not "Map Layers menu" / "Property Lot Report".
  Flagged in the draft's own `corrections_to_live_pages`.

**`docs/reference/article-bank.md` — new, canonical (§7 of the search plan now points at it)**
- **Three spirals**, 48 pieces: Spiral 1 knockdown rebuild (22 + pillar), Spiral 2 living on the
  Bayside (13 + pillar), Spiral 3 dealing with a builder in Australia (14 + pillar).
- Centrepieces written **last** — months 6, 9, 12 — after their spokes exist.
- ⭐ **Grounded in real data that was already in the repo.** `docs/sessions/` held 39 Brisbane
  SERPs scraped 09-05: 104 related queries, 16 People Also Ask. **Cost dominates** — 31 of 104
  queries / 130 appearances, the top query in the whole set is "knock down rebuild cost
  calculator" (20), and **11 of 16 PAA questions are cost questions**. 62 of 104 are
  suburb-anchored. Reviews are searched as a query (15 q / 46 app). "Metricon knockdown rebuild"
  (12) sits inside the local search. "Small"/"independent" are the avatar's own words.
- Section 0 separates **MEASURED** from **ESTIMATED** and marks scrape-backed rows ✅.
- Four-phase writing order, ordered by what's blocked, not by volume.

**`docs/reference/bbl-cross-linking.md` — new**
- Edward asked for articles about BBL inside Sabre's posts with links back. Direction turned
  around, and he agreed: articles about BBL belong on BBL's blog linking out to Sabre.
- **Sabre → BBL:** one footer credit, branded anchor, all 13 pages. **DONE and pushed and live.**
- **BBL → Sabre:** five articles the engagement has already paid for (the 39-SERP research
  write-up; the unsubmittable contact form; why we won't price a builder's site; suburb pages
  worth having; the case study once there are numbers). Two need nothing from anybody.

**BBL's site**
- `/pages/about/` — a "Working on now · Building" block naming Sabre, saying what the work is,
  leading on the research, linking to **sabreconstructions.com.au** (their live domain, not the
  noindex preview). Claims **no results**: "engagement in progress — results when there are
  results". Verified in a real browser over the DevTools protocol.
- **Committed, NOT deployed.**

**Housekeeping**
- The workshop's `site/docs/client-facts.md` was a **stale duplicate** of the real repo's copy
  (missing the mobile, the banner proof, MBQ 00352, the QBCC resolution, the new address). Now a
  pointer; the real repo's `docs/client-facts.md` is the only copy. Both CLAUDE.md routers fixed.

## Files Changed / Created

| Where | What | State |
|---|---|---|
| real repo — 13 × `index.html`, `css/site.css`, `docs/client-facts.md`, `CLAUDE.md` | v20 values, v21 posts + credit | **PUSHED**, live on preview |
| real repo `blog/check-if-your-street-is-in-the-character-overlay/`, `blog/what-is-a-knockdown-rebuild-package/` | two new posts | **PUSHED**, live |
| workshop `docs/reference/article-bank.md` | new, canonical | committed |
| workshop `docs/reference/bbl-cross-linking.md` | new | committed |
| workshop `docs/reference/search-and-ai-visibility-plan.md` §7 | now points at the bank | committed |
| workshop `CLAUDE.md`, `docs/engagement.md`, `docs/open-items.md`, `site/docs/client-facts.md` | routing + state | committed |
| workshop `content/` | was untracked, 9,508 words | now committed |
| BBL submodule `site/pages/about/index.html` | Sabre block | committed, **NOT deployed** |
| Memory `sabre-constructions-project.md` | 09-10 (later) block | updated |

## Decisions Made

1. **QBCC 15486557 is the number to publish** — Nathan. → `client-facts.md`, all 13 pages.
2. **Address changes to Ransome; Capalaba stays in the service-area lists** — a builder is not
   "in" a suburb they've left, but they still build there. → all pages, `client-facts.md`.
3. **The two GAP markers get cut, not filled with anyone else's numbers.** → both posts.
4. **The real repo's `docs/client-facts.md` is the only canonical facts file.** → both routers.
5. **Volume bands decide writing order, nothing else** — an appearance count is a demand signal,
   not a search volume, and must never be bid against. → `article-bank.md` §0.
6. **BBL articles go on BBL's site, not Sabre's.** Sabre's blog holds its topical focus; one
   branded footer credit is the only BBL presence on it. → `bbl-cross-linking.md`.
7. **The BBL about-page block claims no results** — there are none yet. → the block itself.

## Resolved failures

- **v19 sat unpushed for a day** with the contact form broken behind it · the 09-10 handoff listed
  the push as Edward's job and nobody did it · pushed · found by reading the handoff's TODO list
  before touching anything. *Lesson: a commit that fixes a live bug is not a fix until it is
  pushed. Push it in the session that writes it.*
- **`content/` was untracked and invisible** · `git status` showed `?? content/` and it had been
  scrolled past on 09-08 and 09-10 · committed · found when a draft's front matter cited "the
  09-05 related-query data", which prompted a look at what else was in there. *Lesson: `??` in
  git status can be a whole deliverable, not noise.*
- **The first article bank was all guesses** · wrote estimated bands before checking whether real
  data existed · `docs/sessions/` already held 39 scraped SERPs from 09-05 · rewrote §0 around
  them. *Lesson: check `docs/sessions/` for measured data before estimating anything.*
- **The workshop's facts file had silently gone stale** against the real repo's · two copies, one
  router pointing at the wrong one · collapsed to a pointer. *Lesson: two copies of a canonical
  file is one copy and one trap.*
- **Headless Edge screenshots of BBL's about page come out blank** · the `.reveal` scroll engine
  never fires for a headless full-height capture · verified geometry and opacity over the DevTools
  protocol instead (scrollIntoView, wait 1.8s, read computed style). *Not a page bug.*
- **`git push` on the Sabre repo hung repeatedly** (3 attempts, ~2 min each) then went through on
  its own · cause unknown, GitHub side · it does land; run it in the background and check
  `git status -sb` rather than assuming failure.

## What's NOT Done — TODO

**Edward, in order**
1. [ ] **Ask Nathan two things in one conversation:** is he happy with the footer credit, and may
       BBL name Sabre as a client on barebaysidelabs.com. Both are built and ready to show.
2. [ ] Deploy BBL's about page once he says yes (committed in the `site` submodule, not deployed).
3. [ ] **Send ONE real test enquiry** from the preview and confirm it lands in admin@ (rule 4,
       owed since 09-08 and still owed).
4. [ ] Build the Sheet + Flow 1 (`docs/tasks/lead-ledger-build.md`, ~30 min) → send Claude the
       webhook URL → it goes into `FLOW_URL`.
5. [ ] **Google Business Profile → 40 Molle Rd, Ransome QLD 4154.** The site says Ransome and GBP
       still says Capalaba. A NAP mismatch costs more than the move gains. Same for Facebook and
       every directory listing.
6. [ ] Google Ads: Nathan's customer ID → link from manager 775-584-9139 → Nathan accepts.
7. [ ] Meta: Sabre's ad account assigned to BBL; dataset + token.

**Nathan (one conversation, ~30 minutes)**
8. [ ] The two numbers: what a build is worth, the monthly ad budget.
9. [ ] The five claims in `positioning.md`.
10. [ ] His real build timeline, and his design path (architect / designer / draftsperson).
11. [ ] Local detail for Wynnum and Manly — without it those two rewrites stay blocked.
12. [ ] One 10-minute voice note. It unblocks S1's two gaps and three response posts.

**Claude, when unblocked**
13. [ ] Article bank Phase 1 — seven posts that need nothing from anyone: R9 asbestos, R19 flood
        overlay, S9 what the houses are made of, R33 why so many get knocked down, S12 QBCC,
        R16 small independent builders, R1 extend the pre-1947 post.
14. [ ] BBL articles A and B (`bbl-cross-linking.md` §3) — neither needs anything.
15. [ ] Build the S1 cost staple and the `/knockdown-rebuild/` service page once Nathan answers.
16. [ ] **LocalBusiness + Article schema — still zero JSON-LD on the whole site.** robots.txt,
        llms.txt, the Google tag.
17. [ ] `/bbl-asset-code` scaffolds the 7 Google + 4 Meta codes once the budget exists.

**Carried**
- DNS (Melbourne IT / iSonic) unanswered since 08-24. Nothing ranks until cutover.
- Real footage replaces the drone hero, the 3 AI testimonial placeholders, the AI team photo.
- Registry: log v9–v21 on the SAB records. Workshop repo now ~45 ahead, unpushed.

## Quick Context for Next Session

Two folders. **Workshop** `Desktop\Sabre Constructions`: `CLAUDE.md` → `docs/engagement.md` →
for content `docs/reference/article-bank.md`, for ads `campaign-strategy.md`, for the ledger
`docs/tasks/lead-ledger-build.md`, for the BBL link `docs/reference/bbl-cross-linking.md`.
**Real site** `Desktop\sabre-constructions-website`: preview with `python -m http.server 8765`;
facts live in its own `docs/client-facts.md` (the workshop copy is a dead pointer). After any JS
change `node --check` it and bump `?v=` on every page — currently **v21**.

**Fastest path to done:** the seven Phase 1 posts need nothing from anybody and the pattern is now
set — copy an existing post's HTML, replace the body, add the card to `blog/index.html` and the
row to `sitemap.xml`, check every internal link resolves, screenshot at 1400 and 520.

**Most likely next task:** Nathan answers on the credit and the naming → deploy BBL's about page,
then write BBL articles A and B. Or his voice note arrives → S1 and the service page go up.
