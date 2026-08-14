# Handoff — 2026-08-14 (session 2) — Real Google reviews, shared header, mobile nav

> Second session on 2026-08-14. The first is `2026-08-14-handoff.md` (the build
> from zero + ICM restructure). **History, not context** — rules live in
> `docs/reference/`, blockers in `docs/open-items.md`.

## Session Focus

Edward walked through fixes to the demo. Five rounds of changes: real Google
reviews, one consistent header, a vertical Concept 03, clearer ad destinations,
a main-page restructure, and a mobile menu. Everything is deployed and verified
against the live server.

## What Got Done

**Sabre's Google reviews are real and they're on the pages.**
`client-facts.md` said "no verifiable public rating found." That was wrong.
Scraped their Google Business Profile (Apify `compass/crawler-google-places`,
place ID `ChIJBSdvy4ldkWsRML7s7-J9F2c`): **4.5 stars from 11 reviews** — 8×5★,
2×4★, 1×1★. Ten have text. The full cleared quote list is now in
`docs/reference/client-facts.md`.

⚠️ **It is 4.5, NOT 5.** There is a genuine 1-star (Jessica Ferreira, Jan 2022,
a build that ran six months over). Every strip reads 4.5/11, `--gfill` on
`.grev` is 90%, and LP 3 + index say out loud that the bad one is in the count.

**Main page restructured.**
- Hero is now `rebuild-hero.mp4`, not a still.
- The old section 3 ("Old house in / New home out") is **deleted** — it held the
  same clip that's now the hero.
- Testimonials moved up to sit directly under the hero.
- Below the three AI clips, in the same section: the 4.5 strip and six verbatim
  Google quotes. The AI clips **stay** with their warning — Edward's call, this
  is a mock-up of how the section will look.

**One header everywhere.** All three LPs use the same `.topbar` as `index.html`
and `ads.html`, pinned with `.always`. The old `.lp-bar` is gone.

**Mobile menu (`js/nav.js`, new).** Below 520px there was no way to reach Ad
concepts or the LPs on a phone at all. Burger + drawer, loaded on all five
pages. It **builds the drawer from the `.tb-nav` already in the page** — nothing
hard-coded, so the menu can't drift from the desktop nav.

**Concept 03 is vertical and playable.** Regenerated natively 9:16 with Veo 3.1,
pans onto a Sabre end card. See "Resolved failures" — it was also unplayable.

**No more form popup.** The bottom-of-page catch that threw the five questions
into a modal is gone, and all modal machinery with it.

**Ad destinations rewritten.** Each card now names the platform (META/GOOGLE
badge), the ad that sends them, the audience and the campaign goal.

## Files Changed / Created

**All pushed and verified live.** 5 commits, `706d182..d6b6134`.

| Path | What changed |
|---|---|
| `index.html` | Hero → video · section 3 deleted · testimonials moved up · 6 real reviews added |
| `lp-rebuild/raise/story.html` | Shared `.topbar` · real rating + quotes · `id="start"` · nav.js |
| `ads.html` | Concept 03 → vertical + play button · destinations rewritten |
| `js/nav.js` | **NEW.** Burger + drawer, built from `.tb-nav` |
| `js/qualify.js` | Modal + bottom-of-page catch removed entirely |
| `css/sabre.css` | Review components (moved from lp.css) · burger + drawer |
| `css/lp.css` | LP topbar rules · `.lp-one` strip · bigger LP2 video |
| `css/ads.css` | `.plat`/`.spec` on destination cards · concept media keeps 9:16 on mobile |
| `assets/video/testimonial-vertical.mp4` | **NEW.** 1080×1920, 11.3s, 1.2 MB |
| `tools/gen_testimonial_vertical.py` | **NEW.** Veo 3.1 at `aspect_ratio: "9:16"` |
| `tools/finish_testimonial_vertical.sh` | **NEW.** AI label + Sabre end card + `xfade=slideleft` |
| `tools/shoot_lp_cards.py` | **NEW.** Regenerates the ads.html thumbnails |
| `tools/shoot.py` | Now takes page + viewport arguments |
| `docs/reference/client-facts.md` | Google reviews section + cleared quotes |
| `docs/open-items.md` | Star-rating blocker resolved; items renumbered |
| `docs/reference/media-pipeline.md` | Concept 03 vertical + screenshot tooling |

## Decisions Made

1. **Show 4.5, never round to 5** — recorded in `client-facts.md` and as an audit
   row in `docs/tasks/edit-landing-pages.md`. Rounding up is what the ACCC treats
   as misleading, and it's checkable in one click.
2. **Don't quote the 1-star, but don't hide that it exists.** Named on LP 3 and
   index. Reasoning in `client-facts.md`.
3. **AI testimonial clips stay next to the real reviews.** Edward's call — this
   is a mock-up of the section. Item 1 in `open-items.md` still governs them.
4. **Concept 03's scripted line is NOT a real Google review.** Putting a real
   customer's words in an AI actor's mouth is worse than a generic script.
   Recorded in `media-pipeline.md` and the script docstring.
5. **The mobile drawer is generated, not written.** The header had already
   drifted twice; generation makes drift impossible.
6. **Two facts under the LP 2 video, not three.** "Since 1990" and "36 years on
   the Bayside" are the same number twice.

## Resolved failures

| What was broken | Root cause | Fix | What led to it |
|---|---|---|---|
| **Edward asked 3× for the LP header and it kept looking unfixed** | The fix was real but **never deployed** — my push was blocked by the tool classifier and I reported it in one line at the bottom of a long message | Pushed; verified with `curl` that the live server returns `class="topbar always"` | Curling the live page and diffing it against local. **Lesson: "done" means verified on the server, and a blocked deploy is the headline, not a footnote** |
| **Concept 03 could not be played at all** | `<video>` had no `autoplay`, no `controls` and no play button — it rendered its poster and did nothing. True of the old 16:9 clip too | Wired to the existing `.vwrap`/`.vplay` handler in `sabre.js`. It's the only clip with audio, so muted-autoplay is wrong for it | Edward asking "will they be able to play them?" — a question about deployment, not code |
| **Burger was off-screen on `index.html`** | `.topbar` is `translateY(-100%)` until `.show` is added on scroll past the hero. On a phone that's the entire first screen | Pinned `.topbar` below 520px | Playwright click failing with "element is outside of the viewport" |
| **Both navs visible at once on the LPs** | `lp.css` loads after `sabre.css`, so an earlier `body.lp .tb-nav{display:flex}` override beat the new `display:none` | Removed the override; left a comment saying why | Testing burger + desktop-nav visibility at 5 widths × 5 pages |
| **Destination card rows broke onto two lines** | `<b>` sat directly in a `display:grid` row, becoming a third grid item | Wrapped each value in one `<em>` | Screenshotting the element instead of trusting the markup |
| **`ads.html` thumbnails showed the old LP 2** | Nothing regenerated them | `tools/shoot_lp_cards.py` + a note in `media-pipeline.md` | Reading the card previews in a screenshot |
| **Concept videos squashed to 16:9 on mobile** | A blanket `aspect-ratio:16/9` override at ≤820px | Keep 9:16, cap the width instead | Reviewing 9:16 ads on the device they run on |

## What's NOT Done — TODO

Full list in `docs/open-items.md`. In order:

1. 🔴 **Lead form goes nowhere.** `LEAD_EMAIL` in `js/qualify.js` points at
   Edward and the formsubmit relay has **never been confirmed** — nothing
   arrives until someone clicks the confirmation email. Blocks any real traffic.
2. 🔴 **Testimonial videos are AI people.** All four (three carousel + the new
   vertical). Needs 2–3 real families filmed on a phone, 15 min each.
3. 🔴 **Raise reels are an artist's impression** on a real, identifiable Sabre
   site with their signage on the fence.
4. 🔴 **Budget bands invented** — `js/qualify.js`. Needs Sabre's real job sizes.
5. 🔴 **Unconfirmed claims** — fixed price, one point of contact, the free site
   visit. Sabre has to confirm these match how they operate.
6. 🟡 **Preview chrome** — `.prev-bar`, the `previewing` class, medium pills and
   `noindex` all come off before real ads run.

## Quick Context for Next Session

- **Project:** `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`
- **Live:** https://barebayside.github.io/SabreConstruction/ — clean tree, nothing unpushed
- **Read first:** `CLAUDE.md`, then `docs/open-items.md`. Nothing else until you know the task.
- **Check every fact** against `docs/reference/client-facts.md`. There is still a
  lot on these pages that looks real and isn't.
- **Deploying:** follow `docs/tasks/deploy.md`, including polling for a string
  that only exists in the new build. **If the push is blocked, say so first, not
  last** — the header fix sat undeployed through three rounds of feedback.
- **Bump `?v=N`** if you touch CSS or JS. Current: `sabre.css?v=7` · `lp.css?v=7`
  · `ads.css?v=5` · `qualify.js?v=5` · `nav.js?v=1` · `sabre.js?v=3/4`.
- **Fastest path to a real campaign:** film the testimonials and wire the form.
  Everything else on the page is finished enough to show a client.
