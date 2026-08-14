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

## Screenshots

```
py -3 tools/shoot.py          # full-page desktop + mobile (uses ?still)
py -3 tools/shoot.py --live   # viewport only, animations running
```

## Encoding rules of thumb

- Hero / background loops: `crf 29`, 1440px wide, `-an`, `+faststart`
- Reels: `crf 30`, 1080×1920, AAC 96k
- Always `tpad=stop_mode=clone` a beat on the last frame so the payoff lands
  before the loop restarts.
- Raw model output is gitignored; only the encoded cut ships.
