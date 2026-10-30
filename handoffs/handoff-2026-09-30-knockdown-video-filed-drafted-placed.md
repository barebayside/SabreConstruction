# Handoff — 2026-09-30 — Knock down video: filed, editor ask drafted, live on the preview site (silent)

## Session Focus
Sabre's videographer sent `04. Knock down.mov` (Nathan at the Knockdown Rebuilds banner, then
demolition, then logo + 0422 end card). Filed it, worked out why it can't run, asked for a clean
version, and placed it on the site.

## What Got Done
- **Filed on WorkDrive** per `docs/reference/asset-storage.md`:
  `X:\General\BBL Customers\Sabre Constructions — noid\VIDEO\2026-09-30 — Knock down rebuild\01 original from videographer\04. Knock down.mov`
  (moved out of Downloads) + `README.txt` in the job folder.
- **Source:** 21 s, 2160×3840 portrait 9:16, 60 fps HEVC, 94 MB. Speech ends ~11.5 s; demolition ~12–18 s; end card last ~3 s.
- **Blocker found:** "Sweet Child O' Mine" plays under the whole video, voice included. It can't run as a
  Meta ad (commercial music gets blocked or muted, and muting kills Nathan's voice) and shouldn't be an
  organic post from the Sabre page either. Length is not the issue; no length of a commercial track is safe.
- **Transcript (whisper medium):** "Hi, I'm Nathan. I'm the owner of Sabre Constructions. We're here at
  another knockdown rebuild that we've just started. We're a family-owned building company. If you're
  after a builder to do the same thing for you, get in contact with us today."
- **Editor-package plan written:** `docs/emails/2026-09-30-knockdown-editor-package.md`. Ask the editor for
  pieces, not just a re-edit: no-music edit · Nathan's voice as its own WAV · a version with no end card
  and no captions + SRT · logo/font/colours. Then we make the end card (and later the opener) variants ourselves.
- **Zoho draft to Nathan** (NOT sent), messageId `1790726745609010200`, subject "Knock down video: one fix
  needed before we can run it". Includes a forward-to-videographer section + the HeyGen avatar consent ask.
  ⚠️ Edward then said he'll get the no-music version **from the videographer (a woman) directly**, so the
  draft may be redundant. He decides whether to send or delete it.
- **On the real site, LIVE on the preview address** (commits `a8b896f`, `5d8562a`, pushed to `main` of
  `Sabre-Constructions/sabre-constructions-web-site-`):
  - Home page: new "Who you'll talk to" strip directly above `#book` (video left, "The person who rings you
    back is the one on site." right).
  - `blog/knockdown-rebuild-on-brisbanes-bayside-the-whole-path/`: video after the short-answer box, 300 px wide.
  - The video is a **silent stand-in** (music version with all audio stripped). Captions carry the words.
  - Verified: mp4 returns 200 on the live site and both pages reference it.
  - Preview URL: https://sabre-constructions.github.io/sabre-constructions-web-site-/ (noindex, no CNAME yet).

## Files Changed / Created
| Path | What |
|---|---|
| WorkDrive `VIDEO\2026-09-30 — Knock down rebuild\` | original + README.txt |
| `docs/emails/2026-09-30-knockdown-editor-package.md` (workshop) | plan, what to ask for, message text, draft record |
| real repo `index.html` | new video strip above `#book` |
| real repo `blog/knockdown-rebuild-on-brisbanes-bayside-the-whole-path/index.html` | `figure.vid.art-vid` after the answer box |
| real repo `css/site.css` | `.art-vid` rule; **v28 → v29 on all 64 pages** |
| real repo `assets/video/knockdown-nathan.mp4` | SILENT stand-in, 720×1280, 3.7 MB (pushed) |
| real repo `assets/video/knockdown-nathan.en.vtt` | captions, timed to the original (0–11.5 s) |
| real repo `assets/img/knockdown-nathan-poster.jpg` | poster at 1.5 s |
| Zoho Drafts | email to nathan@sabreconstructions.com.au, not sent |

## Decisions Made
1. The original goes to WorkDrive, not the repo's `assets/` (the asset-storage rule: public repos never hold masters).
2. Don't ask the editor for unused takes, uncut clips or the project file (Edward: too much to go through).
   Claude can't open a CapCut project anyway; variants are made from the pieces with ffmpeg.
3. New opening lines come from Nathan re-recording on his phone or from his HeyGen avatar. **HeyGen can't be
   built from old footage without Nathan:** it needs his on-camera consent clip plus ~2 min of steady, quiet
   footage, and `video-profile.md` says no consent is on file.
4. Site placement: the knockdown guide + the home page above the booking form. Not the team page (it's a sales clip, not a family one).
5. Edward chose to push now with the silent stand-in so he could see it.

## What's NOT Done — TODO
1. 🔴 **Nathan's "I'm the owner" line.** `client-facts.md` says owners = Stewart + Cathy; Nathan = carpenter.
   The home page and team page say the same. Now live in the captions on the preview. Nathan must confirm
   (update facts + pages) or the line gets cut/re-recorded. **Blocks the real-domain launch of this video.**
2. 🟠 **The no-music version from the videographer** (Edward getting it). When it lands in Downloads:
   copy into `01 original…` (or `02 editor package\`), encode 720×1280 H.264 → replace
   `assets/video/knockdown-nathan.mp4` (drop the silent stand-in), re-time the VTT, new poster if needed, push.
3. 🟡 **Ad variant builder** (Edward asked to "set it up" for 3–4 versions). Not built. Plan: a
   `tools/` script taking the no-end-card edit + a variants list → a Sabre end card per variant (copy shape of
   `tools/finish_testimonial_vertical.sh`; facts from `client-facts.md`, **phone 0422 831 306, QBCC 15486557**,
   not the old 07 / 328475 in that script) → 1080×1920 per code into WorkDrive `03 …`. Codes via `/bbl-asset-code`.
   Needs the editor's pieces (no-end-card version) to finish; can be built and tested on the stand-in now.
4. 🟡 Zoho draft to Nathan: send (HeyGen part at least) or delete, Edward's call.
5. Carried over: Leanne paid-ads consent, DNS cutover + noindex removal, GBP, Nathan's voice-note answers.

## Quick Context for Next Session
- Workshop: `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\` (read `CLAUDE.md`, then this handoff).
- Real site: `C:\Users\edast\OneDrive\Desktop\sabre-constructions-website\` (read its `CLAUDE.md`; facts in `docs/client-facts.md`).
- Most likely next task: the videographer's no-music file arrives → TODO 2, then TODO 3.
- Transcriber: `C:\Users\edast\.transcriber\venv\Scripts\python.exe C:\Users\edast\.transcriber\transcribe.py <wav> medium en`.
- `gh` CLI is not logged in; check the deploy with curl on the preview URL (Pages published within ~1 min).
