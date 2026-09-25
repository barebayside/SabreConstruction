# Handoff — 2026-09-25 — Leanne's video testimonial live, favicon, WorkDrive storage rule

## Session Focus
Sabre's videographer sent the first REAL client video testimonial. We made it work on the
website (desktop and mobile), registered it as a Meta ad asset, added a favicon, and set
where Sabre's files live from now on (WorkDrive) versus the ad records (BBL registry).

## What Got Done

**The video (Leanne, Chandler)**
- Source: `Downloads/03. Client Testimony - Chandler (1).MOV`, 72 s, 4K 2160×3840 **portrait (9:16, phone-filmed)**,
  60 fps HEVC, 391 MB. Already edited by the videographer: title card, house b-roll, burned captions, 0422 end card.
- Content: extension + granny flat + roof restoration, a 4-year repeat client, found Sabre via friends' reno in
  Wellington Point. **Not a knockdown rebuild.** End-card phone matches client-facts.
- Fixed: HEVC → H.264 (Windows browsers can't play HEVC; GitHub caps files at 100 MB) · loudness −37 → −16 LUFS ·
  new word-timed captions (burned ones ~6 px on a phone, white on white weatherboards) · poster = her face at 15 s.
- Website: replaces the 3 AI placeholder clips on the home page ("In their own words", with her quote beside it) and sits at
  the top of Testimonials (lede reworded: "One client on camera, and the rest from Google").
- Video box sizes from screen height: 319 px wide on a 1366 laptop → 494 px on 1920×1080; phones ≥280 px so it
  clears the ~190 px sticky mobile header.
- Tested LIVE with Playwright + Edge on iPhone 13 / Pixel 7 / iPhone SE: plays, decodes 720×1280, captions showing,
  no horizontal scroll. All 63 pages checked at 320 px: none overflow.

**Mobile bug found and fixed (pre-existing):** the team photo row (4 × 84 px) was wider than a 320 px phone, so the
whole home page zoomed out on an iPhone SE. `.team-row` now wraps.

**Ad asset:** `SAB-CON-KDR-5.0A_META_VIDEO` registered in the BBL registry (Draft). CON = trust proof. Primary text is
Leanne's words only. 1080×1920 master + SRT for Ads Manager.

**Favicon:** Sabre's house mark pulled as VECTORS from the Wild Web banner proof PDF (`docs/reference/brand/…8574.pdf`,
drawing 509 = outline, 510–513 = window panes, red `#EC1F27`). Roof overhang clipped. White house on a red rounded
tile (the Zoho Mail look; chosen over the plain red house, which went faint on dark tabs at 16 px). `favicon.ico/.svg`,
`apple-touch-icon.png`, `icon-192/512.png`, `site.webmanifest` at the real repo root, linked on all 64 pages.

**WorkDrive (`X:` = Zoho WorkDrive)**
- Filed: `X:\General\BBL Customers\Sabre Constructions — noid\VIDEO\2026-09-25 — Leanne Chandler testimonial\`
  (01 original · 02 website version · 03 ad version (Meta) · README.txt · transcript.txt) and `WEBSITE\2026-09-25 — favicon\`.
  Video sizes verified byte for byte.
- Oodles of Paws: 3 folders MERGED into `Oodles of Paws — noid` (247 files / 153,494,569 bytes, exact match).

## Files Changed / Created

| Where | What | State |
|---|---|---|
| Real repo `index.html`, `testimonials/index.html` | video in, AI placeholders out | pushed, LIVE |
| Real repo `assets/video/testimonial-leanne-chandler.mp4` + `.en.vtt`, `assets/img/…-poster.jpg` | web encode, captions, poster | LIVE |
| Real repo `css/site.css` | v26 portrait column · v27 team-row wrap · v28 video sized from screen height | LIVE (all 64 pages on `?v=28`) |
| Real repo root favicon files + icon links on 64 pages | favicon | LIVE |
| Real repo commits | `124557d` `bad18fe` `4e8e720` `8ccbcc0` | in sync with origin |
| Workshop `docs/reference/asset-storage.md` | NEW, canonical storage rule | commit `2ca684f`, NOT pushed (workshop repo ahead 64) |
| Workshop `CLAUDE.md`, `docs/tasks/generate-media.md`, `.gitignore` | router row, output row, `assets/ads/**/*.mp4` ignored | same commit |
| Workshop `assets/ads/SAB-CON-KDR-5.0A_META_VIDEO/` | local working copy (mp4 gitignored) | WorkDrive is the copy that counts |
| BBL `docs/registry/marketing-assets/SAB-CON-KDR-5.0A_META_VIDEO/` | meta.json (+`creative_master`), copy.md, creative.jpg | BBL commit `b252d1b` (branch feat/report-charts-and-clusters) |
| `~/.claude/skills/bbl-asset-code/SKILL.md` | `creative_master` field added to the schema + explanation | saved |

## Decisions Made
1. **WorkDrive holds the FILES; the BBL registry holds the RECORDS; the ad code joins them.** `docs/reference/asset-storage.md`.
2. **Layout:** `<AREA>\YYYY-MM-DD — <what>\` (VIDEO / WEBSITE / ADS; `COMP\` belongs to Catalyst), a README per job,
   originals first into `01 original…`, never overwritten. Same doc.
3. **The testimonial is CON, product slot KDR** (the campaign's slot), even though her job was a reno. Registry copy.md notes this.
4. **Favicon = white house on red tile.** Real repo `favicon.svg` is the master.
5. **Oodles folder kept = `— noid`**, because `bbl_pipeline_job/main.py:729` names folders `{name} — {contact_id or "noid"}`.

## Resolved failures

- **Sabre `git push` hanging (every session since 09-10).** Cause: NOT an expired token. Windows holds two GitHub
  logins (`barebayside`, `EturnerCV`), so Git Credential Manager opens an invisible account picker and waits forever.
  Fix: `git config credential.https://github.com.username barebayside` in the real repo. Found by running
  `GCM_TRACE=1` with `GCM_INTERACTIVE=never` ("Multiple accounts available - prompting user to select one").
  **Pushes now work from Claude directly.** Same fix for any other repo that hangs.
- **Port 8765 is taken by an old BBL preview server**, so the Sabre preview 404'd. Use `python -m http.server 8791 --bind 127.0.0.1`.
- **Headless Edge can't render windows under ~500 px**, which clips small icon renders. Render at 512 and downscale with PIL.
- **Playwright's bundled Chromium can't play H.264.** Launch with `channel: 'msedge'`. playwright-core installed in
  the session scratchpad; the copy at `AppData/Local/Temp/node_modules` is broken (no package.json).
- **My own edit:** I first wrote "filmed September 2026" on the testimonial. The filming date is unknown, so it was changed to "on video, in her own words".

## What's NOT Done — TODO
1. **Ask Nathan: has Leanne agreed to PAID ads** (Facebook/Instagram), not just the website? Blocks running the ad.
2. **Ad can't run yet anyway:** no Meta ad account ids in `brands.json`, site not on the real domain (DNS/noindex).
3. **Brief the videographer for the next shoot:** film **4K landscape** (one clip → wide web + upright Reels), and send the
   raw clips, not just the edit. Text already in the WorkDrive README.
4. Optional, offered, not asked for yet: a **20 s cut-down** (hook at 0:34 "bad experience with a builder") = `1.0B`;
   a **landscape web version** (Leanne centred, blurred sides) or a per-shot 16:9 re-edit from the 4K source.
5. Check whether the **June OOP report's CRM `Raw_Data_URL`** still opens after the merge (WorkDrive may or may not keep
   resource ids on a move via the mapped drive).
6. Carried over: Nathan's voice-note answers (23 Qs, sent 09-23), DNS cutover + noindex removal, GBP address → Ransome.
7. Workshop repo is 64 commits ahead of origin (it's public). Push when wanted; the push should work now if the same
   credential pin is set there too.

## Quick Context for Next Session
- Real site: `Desktop\sabre-constructions-website\` → https://sabre-constructions.github.io/sabre-constructions-web-site-/ (noindex). CSS at **v28**.
- Read first: this handoff → `docs/reference/asset-storage.md` for any new footage.
- New footage from Sabre = fastest path: copy the original to WorkDrive `VIDEO\<date> — <what>\01…` → ffprobe + loudnorm
  (two-pass, target −16 LUFS) → 720p web encode + VTT into the real repo → 1080p ad master + SRT into `03…` →
  `bbl-asset-code` for the code → `creative_master` on the record. The test scripts (`mobtest.js`, `size.js`,
  `sweep.js`, `icons.js`) were in the session scratchpad and are gone; rewrite them with playwright-core + `channel:'msedge'`.
