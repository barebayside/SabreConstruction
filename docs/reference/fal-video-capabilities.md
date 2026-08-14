# fal.ai video — what we can actually make

> **Layer 4.** What the fal.ai video models can do on **length** and **sequencing**.
> `media-pipeline.md` says how *our existing* assets were made. This file says
> what's *available*. Checked live against fal.ai's own model schemas and price
> list on **2026-08-14** — every number below came from the API, not from memory.

## The one-sentence version

No model makes a finished 30-second ad in one go. The longest single call is
**15–16 seconds**; most good ones are 5–10. Long video is made by **joining
short pieces**, and fal gives us four different ways to join them.

## Limit 1 — how long ONE call can be

| Model | Max per call | Audio | Notes |
|---|---|---|---|
| Kling v3 Pro | **15s** (3–15) | yes, native | Our current workhorse. Start + end frame |
| Kling O3 Pro | **15s** (3–15) | yes | Same, plus reference images for consistency |
| Vidu Q3 | **16s** (1–16) | yes | Cheapest long clip |
| PixVerse v6 | **15s** (1–15) | optional | Up to 1080p |
| Wan 2.6 / 2.7 | 5/10/**15s** | music track in | 2.7 can continue from a video |
| MiniMax H3 | **15s** (5–15) | no | Up to 4K |
| LTX 2.3 | 6/8/**10s** | yes | Up to 4K, 24–50 fps |
| Veo 3.1 (all variants) | **8s** (4/6/8) | yes, best dialogue | Shortest — but the best talking heads |
| Luma Ray 3.2 | 5s, or 10s with keyframes | no | See "keyframes" below |
| sync-3 lipsync | **as long as the audio** | the audio you give it | Talking head only |

**Rule of thumb:** anything over 15 seconds is a stitch job, always.

## Limit 2 — the five ways to make it longer

### 1. Pin the end frame (what we already do)
Give the model a start image *and* an end image and it fills the middle. Chain
clips by making clip 2's start frame the same image as clip 1's end frame — the
cut is invisible. Supported by Kling v3/O3, LTX 2.3/2.5, PixVerse Transition,
Vidu Q3, MiniMax H3, Wan 2.7, Veo 3.1 first-last-frame.

**This is still the most reliable method and it's the one the project uses.**

### 2. Multi-shot in a single call — *new to us*
Kling v3 Pro and O3 Pro take a **`multi_prompt`** list instead of one prompt.
Each entry is its own shot with its own prompt and its own length (1–15s), and
the model cuts between them itself. `shot_type: "intelligent"` lets it decide
the shot structure for you.

That means a "wide of the block → close on the frame going up → family walking
in" sequence can come out of **one** call instead of three plus ffmpeg.

⚠️ **Unverified:** whether the shot lengths can add up past the 15s ceiling, or
whether 15s is the total. One cheap test at 3×5s answers it. Don't assume.

### 3. Extend an existing clip
Feed a finished video back in and the model generates what happens next.

| Endpoint | Adds | Input limit |
|---|---|---|
| LTX 2.3 extend | 2–**20s** per go, either end | reads up to 20s of context |
| PixVerse v6 extend | 1–15s | — |
| Veo 3.1 extend | ~7s | **input must be ≤8s** |
| Grok extend | 2–10s | input 2–15s |

**LTX extend is the strongest long-form tool on the platform** — 20 seconds
added per call, and it can extend from the *front* as well, so a finished clip
can have an opening built onto it after the fact.

Veo's 8-second input cap means you can't chain it twice without trimming the
tail back to 8s first.

### 4. Keyframes at fixed positions (Luma Ray 3.2)
`keyframes` takes **1–64 images** and `keyframe_indexes` pins each one to an
exact frame number (5s = frames 0–120, 10s = 0–240). That is storyboard control
— you decide precisely when each image is on screen and the model animates
between them. It's the only model on fal that does this. Also does seamless
loops.

### 5. Stitch in ffmpeg (what `stitch_reels.sh` does)
Still the fallback, still free, and still the only one that gives exact control
over crossfade length and audio.

## Sequencing tools that aren't about length

- **Elements (Kling v3/O3)** — upload a character or object once, then call it
  `@Element1` in the prompt. The same person or the same house appears across
  every clip. This is the fix for "the actor's face changes between shots."
- **Reference-to-video (Veo 3.1, Kling O3, Wan 2.7)** — several reference images
  in, one video out that keeps their look.
- **Motion control (Kling v3)** — a reference *video* drives the movement while
  a reference *image* supplies the character and the background.
- **Wan 2.6/2.7 audio in** — hand it a music track and the cuts land on the beat;
  2.7 also takes driving audio for speech.
- **sync-3 lipsync** — put any script in any face, at any length.
- **Topaz upscale** — 2–4× on a finished cut, $0.01–0.08/sec. Cheap final polish.

## What it costs (per second of finished video, 2026-08-14)

| Tier | Model | $/sec |
|---|---|---|
| Premium | Veo 3.1 (1080p, audio) | **0.40** |
| | Veo 3.1 extend (audio) | 0.40 |
| | Luma Ray 3.2 1080p | 0.24 |
| Mid | Kling v3 Pro (audio) | **0.168** |
| | Kling O3 Pro (audio) | 0.14 |
| | Veo 3.1 Fast (1080p, audio) | 0.15 |
| | Wan 2.6/2.7 1080p | 0.15 |
| | sync-3 lipsync | 0.133 |
| | MiniMax H3 2K | 0.13 |
| | LTX 2.5 Pro 1080p | 0.12 |
| Cheap | PixVerse v6 1080p (no audio) | **0.09** |
| | LTX 2.3 1080p | 0.08 |
| | Kling v3 Standard (audio) | 0.126 |
| | Vidu Q3 540p | 0.07 |
| | Veo 3.1 **Lite** 1080p (audio) | **0.08** |
| Polish | Topaz upscale ≤1080p | 0.01–0.02 |
| Frames | nano-banana-2 edit | 0.08 / image |

Reference points: a **30-second** ad is about **$12** all-Veo, **$5** on Kling
v3 Pro, **$2.40** on LTX 2.3, **$2.40** on Veo Lite. Frames are 8¢ — always
approve frames before spending on video.

## What this changes for Sabre

1. **The hero could run longer.** `rebuild-hero.mp4` is two Kling segments
   stitched. One Kling `multi_prompt` call could do demolish → slab → frame →
   finished in a single pass, cut by the model.
2. **LTX extend can add an opening** to a clip that's already approved, without
   regenerating it.
3. **Elements fixes the testimonial faces** if the AI clips ever need to be more
   than a placeholder — but they're still AI people, and open item 1 still
   governs them. This changes nothing about that.
4. **Veo 3.1 Lite is 1/5 the price of Veo 3.1** for the same 8s with audio. Test
   the script on Lite, spend on the full model only once it's locked.

## Rules that don't change

- Derive every frame from Sabre's own photo. Longer clips make drift worse, not
  better — a 15s generation has more time to invent architecture they didn't build.
- Land on something real. See `generate-media.md`.
- AI people carry a burned-in label. AI "finished houses" carry a caption.
- Check the frames before spending on video. Frames are cents; a 15s Veo clip
  with audio is $6.
