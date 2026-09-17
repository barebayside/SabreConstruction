# Handoff — 2026-09-17 — Spirals finished (52 posts), click heroes with labels, maps inside, Instagram live

## Session Focus
One long day on the Sabre blog: the article kit (v22) went onto every post, the blog grew from 4 to 52 articles, every
card got a click-worthy hero with an HTML label (maps/diagrams moved *inside* the articles), and the footer got
Facebook + Instagram. The earlier part of the day is journaled in
`handoff-2026-09-17-article-kit-v22-all-four-posts-in-the-project-24-shape.md` (v22 → v25, Phase 1, Phase 3); this file
is the end-of-day snapshot and the on-ramp.

## What Got Done
- **Blog: 52 posts live on the preview** (https://sabre-constructions.github.io/sabre-constructions-web-site-/blog/), five
  sections with a sticky rail. All in the Project 24 shape (answer block, H2 questions, proof quotes, takeaways, FAQs, one CTA,
  byline, Article + FAQPage schema). Rule 1 held throughout: no prices, bands or timelines beyond statutory ones.
  - Phase 1 (6) and Phase 3 (11) earlier in the day; **Phase 5 (31) this afternoon** — Spiral 1 finished (16), Spiral 3
    written in full (12), Spiral 2's last three (3). R26/R34 deliberately unwritten (price posts).
- **v25 image system**: every post has TWO images — a photographic hero (card + article top, generated on Sabre's fal key in
  the story-frame style, two variants, picked from contact sheets, no faces/text, captioned as illustrations) with an HTML
  `label=(kicker, big)` overlay; and, where the post had a map or diagram, that PNG kept inside the body as `.art-fig`.
- **Maps**: railway now drawn with the standard rail symbol and keyed "Cleveland line (train)" beside the scale bar on all 9
  maps; in-article figures cache-busted `?v=2`.
- **Footer**: Facebook + Instagram icons on all 61 pages; Instagram unhidden today → https://www.instagram.com/sabreconstructions/
- **Home hero caption** reworded to "Clarence, built by Sabre. Visualised camera move." (disclosure stays until real drone footage).
- Everything pushed: real repo at `4fbae96`. Workshop committed.

## Files Changed / Created
| Path | What |
|---|---|
| REAL `blog/*/index.html` (52) | 31 new posts + all rebuilt with hero/label/figure |
| REAL `blog/index.html`, `sitemap.xml` | 52 cards in 5 sections; 58 sitemap URLs |
| REAL `css/site.css` (v25) | `.thumb`, `.label`, `.art-fig`; cache-buster v25 on all pages |
| REAL `assets/img/blog/` | 52 hero JPGs + 14 map/diagram PNGs (rail symbol) |
| REAL `docs/client-facts.md` | Instagram handle recorded |
| REAL `docs/design-system.md` | hero caption note |
| WS `tools/build_post.py` | `label_html`, `figure_html`, `place_figure`, `FIG_V=2`, thumb-wrapped hero and cards |
| WS `tools/build_blog_index.py` | cards with label; HAND list updated |
| WS `tools/posts_phase5a.py … posts_phase5f.py` | the 31 Phase 5 posts (sources in each header) |
| WS `tools/gen_blog_heroes.py` | 45 hero prompts (14 original + 31 Phase 5) |
| WS `tools/gen_blog_maps.py` | `rail_symbol`, `rail_key` |
| WS `tools/retrofit_v25_posts.py`, `retrofit_v25_hand.py` | one-offs, idempotent |
| WS `assets/img/blog-alternates/` | every unpicked variant |
| WS `docs/reference/article-bank.md` | Phase 5 marked done; owed list |

## Decisions Made
1. **Card image sells; explanatory image explains inside.** Two slots per post; labels as HTML never pixels. (Edward, confirmed; memory `sabre-constructions-project.md`.)
2. **Generated real places are captioned as illustrations**, never presented as photos of the street. (`gen_blog_heroes.py` docstring.)
3. **No Sabre-history claims without a source** — "we've built plenty…" lines were removed from S2/R6/R12 before build.
4. **Hubs come after spokes** — the three pillar pages are the next writing job, now that every spoke exists. (article-bank §6.)
5. **Instagram = @sabreconstructions** (Edward, 17 Sep). The `.com.au` he typed is the website, not the handle.

## Resolved failures
- **Push "hangs"** — Git Credential Manager opens a GUI sign-in this session can't see. Fix: Edward approves the window (or runs
  `! cd <real repo> && git push origin HEAD`); kill stale `git-credential-manager.exe` first. Happened 4× today; one push went
  through without a prompt, so it's intermittent.
- **Edward couldn't see the rail key after a hard refresh** — the live PNG was correct (checked by curl, 228,298 bytes both sides);
  the Pages CDN (`max-age=600`) and/or his browser held the old image. Fix: `?v=2` on figure `src` (`FIG_V` in `build_post.py`).
  Lesson: **any re-rendered image keeps its filename → bump a query string**, don't wait out the cache.
- **Hero caption sat under the label gradient** — the label was absolute to the `<figure>`, which includes the figcaption.
  Fix: wrap `<img>` + label in `<span class="thumb">` and position to that.
- **Bash heredocs mangle `\n` inside Python patch strings and choke on some apostrophes** — repeated 3×. Use the Write/Edit tools
  for any Python containing backslashes or long quoted HTML.
- **`build_post.py` verify fails on cross-module links when the target module isn't built yet** — by design (HTML is written
  before verify). Build the module whose links are satisfied first, or build A → B → A.
- **`mbqld.com.au` blocks automated reads (Cloudflare, even headless Edge)** — S13 cites the Code of Conduct wording from search
  excerpts only; `qbcc.qld.gov.au` pages 404 frequently — search the site for the live URL first; the Consumer Building Guide PDF
  reads fine via the Read tool after WebFetch saves it.
- **Headless-Edge phone screenshots at 420 px show a wider page on every page including the untouched home** — screenshot
  artefact, not a layout bug. Don't chase it.

## What's NOT Done — TODO
1. **The three hub/pillar pages** (Spiral 1, then 2, then 3) — needs nobody; every spoke exists. Highest-value writing left.
2. **Nathan's 30-minute voice note** → S3 (where the family lives), S5 (how long), R5 (who draws it), R8 (demolition timing/who
   organises), R10 (the walk-through page), the "one thing Nathan said" line on every post, `/wynnum/` `/manly/` rewrites, and
   which contract Sabre uses (R11 written without it). Ask list is article-bank §7.
3. **Go-live gates (nothing ranks until these):** DNS cutover + remove `noindex` + `robots.txt` + Search Console/Bing; GBP to
   40 Molle Rd Ransome with category/hours/photos/review link (Nathan's login).
4. Optional diagrams for Spiral 3 posts (inspection stages, the three defects clocks, payment stages) — same `figure=` slot.
5. Real drone footage of Clarence → swap hero files, delete the caption.
6. Carried: LocalBusiness schema, `llms.txt`, lead ledger, testimonial videos are still AI stand-ins.

## Quick Context for Next Session
- Workshop: `C:\Users\edast\OneDrive\Desktop\Sabre Constructions` · Real site: `…\sabre-constructions-website` (GitHub Pages,
  Sabre-Constructions org). Read `docs/reference/article-bank.md` §Phase 5 and this file.
- To add a post: dict in a `tools/posts_*.py` (fields incl. `label`, optional `figure`), prompt in `gen_blog_heroes.py`,
  `set FAL_KEY` from `~/.keys/sabre-fal.key`, generate, pick, copy to `assets/img/blog/<slug>.jpg`, `python tools/build_post.py <module>`.
- Fastest path to done for the hubs: one module `posts_phase6_hubs.py`, 3,000+ words each, linking every spoke; the `related`
  cards can't hold 20 links so put the spoke links in the body under H2s per theme.
