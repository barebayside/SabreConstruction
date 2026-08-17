# Media pipeline

> **Layer 4.** How every video and image in `assets/` was made. Scripts in
> `tools/`. Set `FAL_KEY` before running any of them.

```bash
export FAL_KEY="$(grep -E '^FAL_KEY=' \
  "$HOME/OneDrive/Desktop/Marketing AI content for Bare Bayside Labs/products/image-pipeline/.env" \
  | head -1 | cut -d= -f2-)"
```

## The governing principle

**Derive every generated frame from the client's own photo, and land every
transformation on something real.** That's what keeps the output honest and what
keeps the camera from drifting between frames.

## Models used

| Job | Endpoint |
|---|---|
| Edit an existing frame | `fal-ai/nano-banana-2/edit` |
| Video between two fixed frames | `fal-ai/kling-video/v3/pro/image-to-video` |
| Talking head with audio | `fal-ai/veo3.1` |
| Resolution-only upscale | `fal-ai/recraft/upscale/crisp` |

Crisp upscale is deliberate for client photos — it adds resolution without
inventing architecture Sabre didn't build.

## Hero: knockdown rebuild (`rebuild-hero.mp4`)

Two segments, because one clip asked to demolish *and* rebuild spends its whole
budget on the transition and lands nowhere.

```
A (old lowset brick-and-tile)  ->  B (cleared block)      segment 1, demolition
B (cleared block)              ->  C (their REAL photo)   segment 2, assembly
```

1. `tools/gen_rebuild_frames.py` — derives **A** and **B** from photo **C**, so
   camera position, street, neighbouring house and driveway stay locked.
2. `tools/gen_rebuild_video.py` — two Kling calls with `start_image_url` /
   `end_image_url` pinned. Segment 2's end frame is their real photograph, so
   the assembly must converge on a house they actually built.
3. Stitched with a 0.4s crossfade and a 1.8s hold on the last frame.

56 MB of raw segments → 1.7 MB shipped.

`tools/brand_reel.sh` wraps that master into a branded 9:16 Reel — logo,
headline, CTA in the space above and below — rather than cropping three quarters
of the frame away. Needs `tools/fonts/BebasNeue-Regular.ttf`.

## The three raise reels (`reel-1..3.mp4`)

Edward's own phone footage of a real Sabre raise-and-build-under, continued by
an AI transformation into a finished Hamptons Queenslander with a family walking in.

**⚠️ The source clips are natively 1080×1920.** `ffprobe` reports 1920×1080
because of a rotation flag; the decoded frames are portrait. **Do not crop them.**
This was misread once already.

- `tools/gen_raise_after.py` — finished-house frame derived from the **last frame**
  of each real clip, so the AI half starts on the exact pixels the camera stopped on.
- `tools/gen_raise_reels.py` — generates the transformation between the two.
- `tools/stitch_reels.sh` — joins them, 0.35s crossfade, real audio fading out
  across the join, 1.2s hold at the end.

**⚠️ These are an artist's impression.** There is no design or render for that
job, so the finished half is a visualisation sitting on top of a real,
identifiable site with Sabre's signage on the fence. Needs "concept
visualisation" on screen, or a re-cut landing on a genuinely finished home.

## Testimonial videos (`testimonial-1..3.mp4`)

`tools/gen_testimonials.py`, Veo 3.1, 8s each with audio.

**⚠️ These are AI-generated people, not customers.** Three guards, all of which
stay: the warning panel above the carousel, the per-slide chip, and a burned-in
`AI DEMO - NOT A REAL CUSTOMER` bar in the video files themselves — so a clip
can't be mistaken for real if it ever leaves the page.

## Concept 03 vertical (`testimonial-vertical.mp4`)

The clip on `ads.html` used to be one of the 16:9 carousel testimonials, which
was the wrong shape for the placement Concept 03 actually runs in.

1. `tools/gen_testimonial_vertical.py` — Veo 3.1 at **`aspect_ratio: "9:16"`**,
   8s with audio. Generated vertical, not cropped from a landscape frame.
2. `tools/finish_testimonial_vertical.sh` — burns in the AI label, builds the
   Sabre end card, and joins them with an `xfade=slideleft` so the ad pans off
   the person and onto the brand. 11.3s total, 1.2 MB.

The end card sits on Sabre's own photograph (`rb-c-real.jpg`) and every line on
it — 1990, the phone number, QBCC 328475 — is from `client-facts.md`.

**⚠️ Still an AI-generated person.** Same rule as the carousel clips. The label
is at the *bottom* of the frame deliberately: `ads.html` puts its own format
badge in the top-left corner and the two collided.

**The scripted line is deliberately not one of Sabre's real Google reviews.**
Putting a real customer's words in an actor's mouth is worse than a generic
script, not better.

## Team photo (`team-photo.jpg`)

`tools/gen_team_photo.py`, `fal-ai/nano-banana-2`, 16:9, two variants at ~$0.05 each.

The one place in this repo where the governing principle is deliberately
inverted: the image is **not** derived from a client photo, because the only
honest source would be the faces of six real, named employees.

**⚠️ These are AI-generated people and they are generic ON PURPOSE.** Sabre's
team is Stewart, Cathy, Nathan, Celene, Frank and Jacob — real, identifiable,
with cut-out photos already in `assets/img/team/`. Generating a photoreal group
shot that resembles them would be a fake photograph of real people on their own
company's website. The prompt therefore asks for an anonymous crew and the page
says in terms that nobody in it works there.

- Variant 2 was rejected: legible garbled logos on the polo shirts. Variant 1's
  chest marks are small enough to read as generic embroidery. Check this on any
  regeneration — the model wants to invent branding.
- 476 KB raw → 197 KB shipped (`scale=1600:-2`, `-q:v 5`), under the 200 KB gate.
- Raw variants `team-photo-[12].jpg` are gitignored; only `team-photo.jpg` ships.

Replaced by a real photo the moment one exists. See `../open-items.md` item 7.

## Screenshots

```
py -3 tools/shoot.py                    # index.html, desktop + mobile (uses ?still)
py -3 tools/shoot.py --all              # every page
py -3 tools/shoot.py --mobile lp-raise  # one page, one viewport
py -3 tools/shoot.py --live             # viewport only, animations running

py -3 tools/shoot_lp_cards.py           # the three LP thumbnails used by ads.html
```

**Run `shoot_lp_cards.py` whenever an LP changes visibly.** The "Ad destinations"
cards keep serving the old thumbnail otherwise, which is worse than showing
nothing because it looks current.

## Encoding rules of thumb

- Hero / background loops: `crf 29`, 1440px wide, `-an`, `+faststart`
- Reels: `crf 30`, 1080×1920, AAC 96k
- Always `tpad=stop_mode=clone` a beat on the last frame so the payoff lands
  before the loop restarts.
- Raw model output is gitignored; only the encoded cut ships.

## Rebuild render — a client's real job (`rebuild-render.mp4`)

The first time this pipeline was pointed at a **real Sabre job** rather than the
demo site. Source material lives with the client's files, deliberately outside
this repo: `Y:\My Folders\Nathan\ai-video\` (photo, plans, scripts, raw output).

```
A (owner's phone photo)  ->  B (cleared block)   segment 1, demolition
B (cleared block)        ->  C (approved design) segment 2, construction
```

- `tools/gen_frames.py` (in the client folder) — B is a nano-banana-2 edit of the
  photo; **C is derived from B, not from A**, so the construction segment is
  pixel-locked and any camera drift is confined to the demolition half.
- C is built from the designer's street elevation and 3D perspective passed in
  as extra reference images alongside the site photo.
- `tools/gen_video.py` — two Kling v3 Pro calls, audio off, both ends pinned.
  Demolition is 5s; **the build is 10s and has to be.** At 5s the model skipped
  the stages and cut straight to a finished house. At 10s, with the stages
  numbered in the prompt, it actually shows footings, slab, wall frames,
  trusses, roof sheeting, then brickwork.
- `tools/stitch.sh` joins them: 0.4s crossfade, 1.8s hold, 1440 wide.
- 16.5s finished, 1.5 MB. Total spend: **6 images + 3 clips ≈ $3.00.**

**⚠️ The garage is NOT on the street face.** 48 Osterley Road is a corner block
— Anita Street is the frontage in the photo, Osterley Road runs down the left,
and the site plan puts the garage at the far corner off that side street. The
first render invented a garage door on the front and had to be redone.

**⚠️ The design belongs to another practice.** The drawings are stamped NOT FOR
CONSTRUCTION and say in terms that visualisations are indicative only. The page
carries a concept-visualisation panel, and the owners' names and the street
address appear nowhere. Written permission is still required — see
`../open-items.md`.

**⚠️ Kling returns the two segments at different pixel sizes** (1920x1080 and
1928x1072). Both must be normalised before `xfade` or the filter graph fails.
