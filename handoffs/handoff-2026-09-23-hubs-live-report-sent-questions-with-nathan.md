# Handoff — 2026-09-23 — Three hubs live, competitor report republished and sent, voice-note questions with Nathan

## Session Focus
Finished the last writing job that needed nobody (the three hub pages), then got Sabre's competitor report actually onto
Nathan's link. It had not updated since 8 Sep. Sent it, plus a question list for Nathan's voice note. Also answered
Catalyst cost questions for a future quoting app and a Catalyst-hosted form.

## What Got Done
**Website: Phase 6, the hubs (pushed, live on the preview, still noindex)**
- `blog/knockdown-rebuild-on-brisbanes-bayside-the-whole-path/` (3,013 w), `blog/living-on-brisbanes-bayside-an-honest-guide/`
  (3,010 w) and `blog/how-to-choose-a-builder-in-queensland-the-whole-checklist/` (3,004 w). Each links every spoke in its
  spiral plus the other two hubs, and claims nothing a spoke doesn't. Proof quotes are copied verbatim from the spokes. 5 FAQs each, Article + FAQPage schema.
- **Every spoke now links UP to its hub** ("Part of a bigger picture") under the short answer. It's generated for all 48 module posts and
  hand-added to the 4 hand-built posts. 55 posts total.
- Heroes on Sabre's fal key, v2 of each picked (v1 of the knockdown hero showed a legible "Bobcat" on the excavator).
- Real repo `4d8dbc8`, pushed (no GCM prompt this time). Workshop commit `c84556f`.
- Confirmed the BBL footer credit was already on all 64 pages (links barebaysidelabs.com, live). Nothing to do.

**Competitor report `795000000099330`: republished and SENT to Nathan**
- The live link was still the **8 Sep** file. The 09-11 and 09-22 rebuilds never published.
- Fixed and published (see Resolved failures), then verified on the live link: Google AI Mode ×26, 0 `[your service]`,
  "Reviewed on" row, 68/68 media 200, every "Video" label has a playing player.
- Instagram wording corrected in `prose.json`. It had said "no Instagram account was found" and recommended opening one.
  Now: @sabreconstructions exists, the old site didn't link it, so this run never measured it.
- Data is still **5 Sep by design** (the case-study baseline). No new scrape exists. The last Apify run was 22 Sep 17:57, and the Apify cap resets 28 Sep.

**Nathan**
- `docs/nathan-voice-note-questions.md`: 23 questions in sections A–G, each mapped to the posts/pages it unblocks. **Sent by Edward 09-23** with the report link.

**Advice given (not built)**
- Quoting app on Catalyst: Catalyst itself ≈ $0–5/mo. Its own LLMs (small Qwen models, US/IN/EU only, not in the AU data centre) aren't fit for the job.
  AI via an outside model ≈ US$10–40/mo plus transcription ≈ $2/mo. The rule: every quote line traces to Nathan's spreadsheet; no invented prices.
- Form on Catalyst instead of Formspree: possible and worth it (ledger + future app in one account), but a card is needed even on the free tier,
  and it follows the OOP pattern (fetch not beacon, text/plain POST, keep Formspree until a real enquiry proves it). Not started.

## Files Changed / Created
| Path | What |
|---|---|
| WS `tools/posts_phase6_hubs.py` | NEW: the 3 hubs; links as `[[key|text]]` expanded via `SLUGS` |
| WS `tools/build_post.py` | `HUBS`, `SECTION_HUB`, `hub_line`, `place_hub_line`: spoke → hub link under the answer |
| WS `tools/gen_blog_heroes.py` | 3 hub hero prompts |
| WS `assets/img/blog-alternates/` | hub hero variants |
| WS `docs/reference/article-bank.md` | Phase 6 section |
| WS `docs/engagement.md` | 2026-09-23 entry |
| WS `docs/nathan-voice-note-questions.md` | NEW, sent |
| WS `docs/sessions/2026-09-23-competitor-report-795000000099330-PREVIEW.html` | = what's live (loads the same stored media) |
| WS `docs/sessions/2026-09-23-competitor-report-795000000099330-authored-stratus.v4.json` | the published v4. **Push THIS one, never the 09-22 file** |
| WS `docs/sessions/2026-09-23-BACKUP-live-report-as-of-2026-09-08.html` | the old live page, kept |
| REAL `blog/*` (3 new + 52 with hub line), `blog/index.html`, `sitemap.xml`, `assets/img/blog/` (3 heroes) | pushed `4d8dbc8` |
| BBL `scripts/.analyst/795000000099330/remap_media_to_stratus.py` | NEW (see BBL handoff) |
| BBL `scripts/.analyst/795000000099330/prose.json` | Instagram fix; backup `prose.before-instagram-fix.json` |

## Decisions Made
1. Hubs claim nothing their spokes don't; every spoke links up to its hub (`article-bank.md` § Phase 6).
2. The report keeps its **5 Sep data** as Sabre's baseline; a fresh run goes the day the new site goes live (the "after").
3. **BBL Catalyst spend ≤ US$30/month**. Edward added a card and set a Budget in Catalyst Billing (memory `sabre-constructions-project`).
4. Sabre's own socials in the report are "not measured", never "not found" (report prose).
5. A video post we only hold a still for is labelled "Video post (still frame shown)" (remap script).

## Resolved failures
- **Live report link stuck on 8 Sep** · WHY: BBL's Catalyst project had used up the free Data Store read allowance
  (`FREE_USAGE_LIMIT_REACHED`, no payment method), so every publish job died after `POST /report-v4` returned 202. The
  202 only means "queued", and earlier sessions recorded "pushed" on the 202 · FIX: Edward added a card · FOUND BY: `curl -I` the
  customer link (Last-Modified 08 Sep), then `/debug/list-reports` returned the error. **Lesson: a push is done when the
  live page's Last-Modified moves and its content greps right, never on the 202.**
- **Direct Stratus upload failed** · WHY: the MCP `Create_Upload_Signature` issues an `stsPolicy` signature that returned 400
  `invalid_request_parameter` for every PUT/multipart form tried, and the Catalyst CLI has no Stratus upload · not needed once the card was on.
- **Ads/posts would have published blank** · WHY: Meta/Instagram CDN URLs in a v4 expire (69/91 were 403 by 09-23) and the
  publish job re-hosts media by downloading it · FIX: `remap_media_to_stratus.py` maps each old URL to the copy the 09-08
  publish already stored. The 09-05 local render and the 09-08 live page come from the same v4, so their media lists align
  1:1 (82 = 82, 0 conflicts). 61 remapped; 8 section-04 posters unrecoverable (dropped).
- **Black video boxes in section 04** · WHY: for over-cap videos the 09-08 publish stored only a still, so the remap put a JPEG
  into a `<video>` · FIX: stills move to `image`, `video` cleared, `format` relabelled. Proven by playing each remaining video in Edge (3/3 play).
- **Headless "broken image" counts were false alarms** · WHY: `loading=lazy` plus big files; force `loading='eager'` and wait before counting.
- **Bash heredoc + apostrophes broke the hub patch** (again, as the 09-17 handoff warned) · use the Write tool for Python patch files.

## What's NOT Done — TODO
1. **Wait for Nathan's voice note** → S3, S5, R5, R8, R10, `/wynnum/` `/manly/` rewrites, contract type, the four operating
   claims, the "one thing Nathan said" line per post. Map in `docs/nathan-voice-note-questions.md`.
2. **Chase Nathan for:** the Google Business Profile login (address still Capalaba) and who holds the domain (iSonic / Melbourne IT).
   These gate going live (DNS, noindex off, robots, Search Console).
3. **Lead ledger:** decide Zoho Flow + Sheet (original plan) vs Catalyst in Sabre's own account. Either way, switch the site's
   ledger send from `sendBeacon` to `fetch` (the OOP lesson).
4. Fresh competitor run for Sabre **after DNS cutover** (Apify resets 28 Sep). Add a social read of @sabreconstructions + the Facebook page.
5. Carried: LocalBusiness schema, `llms.txt`, optional Spiral 3 diagrams, real drone footage, AI testimonial stand-ins, agreement entity (two ABNs).

## Quick Context for Next Session
- Workshop `Desktop\Sabre Constructions` · real site `Desktop\sabre-constructions-website` (pushed, in sync at `4d8dbc8`).
- Read this file, then `docs/engagement.md` (top entry). If Nathan's answers are in, open `docs/nathan-voice-note-questions.md`
  for the map, then `docs/reference/article-bank.md` for which posts they feed.
- Post pattern: dict in `tools/posts_*.py` → `python tools/build_post.py <module>` (verifies links, rebuilds the index,
  adds the hub line). Rebuilding every module is deterministic (zero diff), so it's safe.
- Report re-publish: `POST …/report-v4/795000000099330` with the 09-23 `authored-stratus.v4.json`, then confirm the customer
  link's Last-Modified moved and grep the content.
