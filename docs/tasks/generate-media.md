# Task: make a video, image or reel

> **Layer 3 contract.** Scope: `tools/`, `assets/`. This is the one genuinely
> sequential pipeline in the project.

## Inputs

| Source | File | Section / Scope |
|---|---|---|
| Blockers | `../open-items.md` | Full file |
| How every existing asset was made | `../reference/media-pipeline.md` | Full file |
| Model limits — length, sequencing, cost | `../reference/fal-video-capabilities.md` | Full file |
| API key + model rationale + cost | see `../reference/bbl-links.md` | § *Media generation* |
| Existing scripts | `../../tools/` | The one closest to your job — copy its shape |

## Process — the stages

```
01 frames  →  02 generate  →  03 encode  →  04 publish
```

**01 · Frames.** Derive every start and end frame from the client's own photo or
footage. Never generate a frame from scratch when one can be derived — that's
what keeps the camera locked and the output honest.
Scripts: `tools/gen_rebuild_frames.py`, `tools/gen_raise_after.py`

**02 · Generate.** Pin both `start_image_url` and `end_image_url`. A clip with
only a start frame drifts and lands nowhere. Split multi-beat stories into
segments — one clip asked to do two things does neither.
Scripts: `tools/gen_rebuild_video.py`, `tools/gen_raise_reels.py`, `tools/gen_testimonials.py`

**03 · Encode.** Raw model output is 20–40 MB and never ships.
Scripts: `tools/stitch_reels.sh`, `tools/brand_reel.sh`. Rules in `../reference/media-pipeline.md`.

**04 · Publish.** Poster frame, then `deploy.md`.

## Checkpoint

**After stage 01, stop and show Edward the frames.** They're cheap; video is not.
A wrong frame generates a wrong video and the money's gone.

## Audit

| Check | Pass condition |
|---|---|
| Camera holds | Street, trees and neighbours in the same place across every frame |
| Lands on something real | The final frame is a genuine Sabre photo, or the output is captioned as a visualisation |
| Source aspect | Phone clips are 1080×1920 — `ffprobe` lies because of the rotation flag. Never crop on its word |
| File size | Hero under ~2 MB, reels under ~3.5 MB |
| Honesty label | AI people carry a burned-in label. AI "finished houses" carry a caption |
| Raw output gitignored | Only the encoded cut is tracked |

## Outputs

| Artifact | Location |
|---|---|
| Derived frames | `assets/img/` (or `assets/img/raise/`) |
| Raw generation | `assets/video/` — **gitignored** |
| Encoded cut | `assets/video/{name}.mp4` |
| Poster | `assets/img/{name}-poster.jpg` |
| New script | `tools/{verb}_{noun}.py` or `.sh` |
| Pipeline note | append to `../reference/media-pipeline.md` |
