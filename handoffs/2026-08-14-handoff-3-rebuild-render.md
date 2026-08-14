# Handoff — 2026-08-14 (session 3) — fal.ai video capability + the Rebuild render page

> Third session on 2026-08-14. Sessions 1 and 2 are the build-from-zero + ICM
> restructure, and the reviews/nav round. **History, not context** — rules live
> in `docs/reference/`, blockers in `docs/open-items.md`.

## Session Focus

Two things. First, work out what fal.ai can actually do on video **length and
sequencing**, checked against the live API rather than memory. Then use it: turn
a real Sabre client's site photo and architect's plans into a knockdown-rebuild
clip, and put it on the site as its own page.

## What Got Done

**fal.ai capabilities, checked live (`docs/reference/fal-video-capabilities.md`).**
Pulled every video model's input schema and the current price list off fal's own
API on 2026-08-14. Headlines: the longest single call on the platform is 15–16s
(Kling v3/O3, Vidu, PixVerse, Wan, MiniMax); Veo 3.1 is only 8s and the most
expensive; **LTX extend adds up to 20s per call and can extend from the front**;
Kling takes a `multi_prompt` list for multi-shot in one call; Luma Ray 3.2 pins
up to 64 keyframes at exact frame numbers. Costs per finished second are in the
file. **Veo 3.1 Lite is 8c/s vs full Veo's 40c/s** — test scripts on Lite.

**The rebuild clip — first time the pipeline has been pointed at a real job.**
Client is Chant House job WD2637, a corner block at 48 Osterley Rd / 17 Anita St,
Yeronga. Source photo, plans, scripts and raw output live at
`Y:\My Folders\Nathan\ai-video\` — **deliberately outside this repo, which is
public**. Final 16.5s clip, 1.5 MB, shipped to `assets/video/rebuild-render.mp4`
and a playable copy at `Y:\My Folders\Nathan\Osterley Rd - demolish and rebuild.mp4`.

**Read the plan set properly before prompting anything.** 15 A1 sheets. Rendered
them with `pypdfium2` (no poppler on this machine — `Read` on a PDF fails).
Sheets 9.22/9.23/9.24 are real coloured interior renders; 9.01 is only a white
massing model. Site plan 1.01 is what settled the garage question.

**The page.** `rebuild-render.html`, a sixth nav tab. Built out first with a
three-frame breakdown and use-case cards, then **stripped on Edward's call to
just the headline, the concept-visualisation note and the video.**

**Everything is pushed and verified live** against the server, including that
the video itself returns 200 at 1.53 MB — not just the HTML.

## Files Changed / Created

**Pushed. 3 commits, `2778ec9..98c7252`.**

| Path | What changed |
|---|---|
| `rebuild-render.html` | **NEW.** The page. Now headline + warning + video only |
| `assets/video/rebuild-render.mp4` | **NEW.** 16.5s, 1440x810, silent, 1.5 MB |
| `assets/img/render/poster.jpg` | **NEW.** Final frame. The only still left in the repo |
| `css/ads.css` | Added then removed the page's blocks; **now at `?v=7`** on both pages that load it |
| `index.html` · `ads.html` · `lp-*.html` | Nav link added. The mobile drawer picked it up on its own — `nav.js` builds itself from `.tb-nav` |
| `tools/shoot.py` | Knows `rebuild-render` |
| `docs/reference/fal-video-capabilities.md` | **NEW.** Model limits, sequencing methods, costs |
| `docs/reference/media-pipeline.md` | New section for this clip + the two traps below |
| `docs/open-items.md` | **New blocker 6** — permission for the design |
| `docs/CONTEXT.md` · `docs/tasks/generate-media.md` | Route to the new reference |

**Not in this repo, by design:** `Y:\My Folders\Nathan\ai-video\tools\` —
`gen_frames.py`, `gen_video.py`, `stitch.sh`.

## Decisions Made

1. **Client material stays out of this repo.** It's public GitHub Pages and the
   drawings are another practice's copyright. Scripts and source live with the
   client's files on `Y:`. Recorded in `media-pipeline.md`.
2. **Frame C is derived from frame B, not from the original photo.** That makes
   the construction segment pixel-locked and confines any camera drift to the
   demolition half, where it reads as a pull-back.
3. **The build segment is 10s, not 5s.** See resolved failures.
4. **No names, no address on the page.** Blocker 6 in `open-items.md` still
   requires written permission from Chant House and the owners before it runs
   anywhere public.
5. **The page is the video.** Edward stripped the explanatory sections; the clip
   is the pitch. Its CSS and the three build stills went with them.
6. **Kling v3 Pro over Veo for this job.** 11c/s silent vs 40c/s, and the job
   needs pinned start/end frames, not dialogue.

## Resolved failures

| What was broken | Root cause | Fix | What led to it |
|---|---|---|---|
| **The build segment skipped the build** — bare dirt cut straight to a finished house | 5s is not enough room for the model to pass through stages; it spent the whole budget on the transition | Doubled to 10s **and numbered the eight stages in the prompt**. Now shows footings, slab, wall frames, trusses, sheeting, brickwork | Edward watching it and saying it "zoomed in really quickly" |
| **Invented a garage door on the street face** | I read "garage under on the low side" off the elevation without checking which face was the street | Site plan 1.01: it's a **corner block** — Anita St is the frontage in the photo, Osterley Rd runs down the left, garage is at the far corner off that side street. Regenerated frame C with "NO GARAGE DOOR on the street-facing front" | Edward knowing the design. **Read the site plan before the elevation** |
| **`git push` blocked by the tool classifier, twice** | Environment, not the repo | Edward granted permission, then it pushed clean | Session 2's lesson held: it was reported as the headline, not a footnote |
| **fal.ai returned 403 mid-job** | Not a code fault — `"User is locked. Reason: Exhausted balance."` The error only shows if you POST the storage token endpoint directly | Edward topped up | POSTing `rest.fal.ai/storage/auth/token` and reading the body. **A 403 from fal is a billing message, not an auth bug** |
| **Frame 03 rendered black in the screenshot** | `loading="lazy"` on an image far down the page; Playwright shot it before it loaded | Dropped lazy — only three images and they were the point of the page | Screenshotting instead of trusting the markup |
| **`xfade` refused to run** | Kling returned the two segments at different sizes — 1920x1080 and **1928x1072** | Normalise both to 1920x1080 before the filter | Reading the ffmpeg error instead of retrying |
| **`Read` can't open PDFs here** | No poppler/pdftoppm on this machine | `py -3 -m pip install pypdfium2`, render pages to PNG | — |

## What's NOT Done — TODO

1. 🟡 **The Sabre end card was asked for and not built.** 3s on the end of the
   clip: black card, white logo, Bebas headline in Sabre red, then 07 3823 3200 /
   Capalaba / QBCC 328475. **Reuse `tools/finish_testimonial_vertical.sh`** —
   it already does exactly this for Concept 03, just at 9:16. Font is at
   `tools/fonts/BebasNeue-Regular.ttf`. Every line must come from
   `client-facts.md`.
2. 🔴 **Confirm 17 Anita St and 48 Osterley Rd are the same property.** The site
   plan says corner block, which explains two numbers, but Nathan should confirm
   rather than us assuming.
3. 🔴 **Blocker 6** — written permission from Chant House and the owners.
4. 🔴 Blockers 1–5 in `open-items.md` are untouched. The lead form still goes
   nowhere and the testimonial videos are still AI people.
5. 🟢 **Video 2, the first-person walkthrough,** was scoped and not started.
   Estimated $15–25 for 40–50s as a shot-by-shot walk anchored to stills.
   **It will not be dimensionally accurate** — if Nathan needs that, Chant House
   already has the 3D model that made those renders and a flythrough export from
   it would be cheaper and correct. Worth one phone call first.

## Quick Context for Next Session

- **Project:** `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`
- **Client material:** `Y:\My Folders\Nathan\ai-video\` — never copy it in here
- **Live:** https://barebayside.github.io/SabreConstruction/rebuild-render.html
  — clean tree, nothing unpushed
- **Read first:** `CLAUDE.md`, then `docs/open-items.md`. For any video work,
  `docs/reference/fal-video-capabilities.md` before you pick a model.
- **Spend this session: $2.97.** 6 images and 3 clips. Frames are 8–12c, so
  always approve frames before paying for video — that checkpoint is in
  `docs/tasks/generate-media.md` and it earned its keep twice.
- **Cache-busters:** `sabre.css?v=7` · `lp.css?v=7` · `ads.css?v=7` ·
  `qualify.js?v=5` · `nav.js?v=1` · `sabre.js?v=3/4`
- **Fastest path to value:** the end card is 20 minutes and makes the clip
  usable as an actual ad. Then film the testimonials and wire the form —
  unchanged from session 2.
