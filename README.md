# Sabre Constructions — landing page

A single-page pitch/landing page for Sabre Constructions (Capalaba QLD).
Self-contained: no build step, no dependencies, no CDN except Google Fonts.

**Live:** https://barebayside.github.io/SabreConstruction/

## What's here

```
index.html              the page
css/sabre.css           all styling
js/sabre.js             motion, before/after slider, FAQ, form
assets/img/             photos (client's own + the AI 'before' frame)
assets/video/           hero transformation video (1 MB, web-encoded)
tools/                  the scripts that generated the assets
shots/                  QA screenshots (gitignored)
```

## Design system

Structure follows the BBL landing-page pattern in
`Marketing AI content for Bare Bayside Labs/site/` — the "sealed room" LP
(no nav, one CTA path repeated), the `.reveal` IntersectionObserver system,
and the Bebas Neue / Plus Jakarta Sans / DM Mono type stack.

The **look** is Sabre, not BBL: hot red `#FF1A1A` and black `#0B0B0C`, both
sampled from their logo PNG. Loud, blocky, high-motion — full-bleed red and
black bands instead of BBL's light editorial calm.

Motion classes: `.reveal` (fade up), `.pop` (drops in from above with an
overshoot), `.slide-l` / `.slide-r`, `.zoom`, staggered by `.d1`–`.d6`.
All of it collapses under `prefers-reduced-motion`.

**`?still` hook:** add `?still` to the URL and every animation snaps open and
the hero collapses — for full-page screenshots. Inert for real visitors.
Same trick as the BBL site.

## Who it's aimed at

**Bayside families weighing up moving against rebuilding.** The page was
originally aimed at nobody in particular; it was rebuilt against Workflow C of
`playbook/foundations.md` in the BBL repo, whose headline finding was that it
never passed **Fit** — it named a service and a postcode but never a person.

Section order now maps to the five tests:

```
1   Hero                    Notice + Fit
2   Suburb strip            Fit / Unity
3   The reveal video        Notice + Proof
4   The problem             Fit + loss framing
5   Four steps              Effort
6   Meet the family         Liking + Unity + Proof
7   Testimonials + quote    Proof
8   Gallery + lightbox      Proof
9   Credentials strip       Proof
10  FAQ                     Effort
11  CTA + form              Effort + Now
```

Two rules that came out of that pass and should survive future edits:

- **No fabricated scarcity.** The "Now" test is carried by honest loss framing
  (the school term you're losing), never a countdown or a fake cap.
- **Concrete over rounded.** Their old site said "25+ years"; they were founded
  in 1990, which is 36. Cut "100% family owned" and "1 point of contact" —
  slogans wearing a number's clothes.

## Pages

| Page | What it is |
|---|---|
| `index.html` | The landing page |
| `ads.html` | Instagram/Facebook ad concepts — 9:16 reels, Meta ad mock-ups, copy bank |

Both share `css/sabre.css` and `js/sabre.js`; the ads page adds `css/ads.css`.
The nav lives in the sticky top bar. On the landing page the bar slides in
after the hero; on the ads page `.topbar.always` pins it open.

## The hero video — knockdown rebuild

Not stock, and not one generation. Built as two segments so each story beat
has a fixed start and end frame:

```
A (old lowset brick-and-tile)  ->  B (cleared block)       segment 1, demolition
B (cleared block)              ->  C (their REAL photo)    segment 2, assembly
```

1. `tools/gen_rebuild_frames.py` — derives **A** and **B** from their real
   photo via `fal-ai/nano-banana-2/edit`. A replaces the two-storey home with a
   small 1970s lowset; B clears the block to bare earth and a slab. Because
   both come from photo C, the camera position, street, neighbouring house and
   driveway stay locked across all three frames.
2. `tools/gen_rebuild_video.py` — two `fal-ai/kling-video/v3/pro/image-to-video`
   calls with `start_image_url` / `end_image_url` pinned to those frames.
   Segment 2's end frame is their actual photograph, so the assembly is forced
   to converge on a house they really built.
3. Stitched with a 0.4s crossfade and a 1.8s hold on the final frame:

```
ffmpeg -i rb-seg1-demo.mp4 -i rb-seg2-build.mp4 -filter_complex \
  "[0:v]scale=1600:-2,fps=25,setpts=PTS-STARTPTS[a];\
   [1:v]scale=1600:-2,fps=25,setpts=PTS-STARTPTS[b];\
   [a][b]xfade=transition=fade:duration=0.4:offset=4.6,\
   tpad=stop_mode=clone:stop_duration=1.8[v]" \
  -map "[v]" -c:v libx264 -pix_fmt yuv420p -crf 29 -preset slow -an \
  -movflags +faststart rebuild-hero.mp4
```

56 MB of raw segments down to 1.7 MB. `rebuild-9x16.mp4` is the same master
letterboxed onto a 1080x1920 canvas for Reels.

The hold on the last frame is deliberate — the payoff needs a beat before the
loop restarts.

## The three raise reels — ⚠️ artist's impression

`assets/video/reel-1..3.mp4` are Edward's own phone footage of a real Sabre
raise-and-build-under, continued by an AI transformation into a finished
Hamptons Queenslander with a family walking in.

**The source clips are natively 1080x1920.** `ffprobe` reports 1920x1080 because
of a rotation flag — the decoded frames are portrait. Don't crop them.

Pipeline: `tools/gen_raise_after.py` derives the finished-house frame from the
**last frame** of each real clip (so camera, street and trees carry through),
`tools/gen_raise_reels.py` generates the transformation between the two, and
`tools/stitch_reels.sh` joins them with a 0.35s crossfade. The real audio fades
out across the join; the AI half is silent.

**There is no design or render for that job.** The finished half is therefore a
visualisation sitting on top of a real, identifiable site with Sabre's signage
on the fence. Before these run they need "concept visualisation" on screen, or
a re-cut landing on one of Sabre's genuinely finished homes. This is flagged on
`ads.html` in the concept's *How it's made* box and in the status table.

`tools/brand_reel.sh` wraps the wide knockdown-rebuild master into a branded
9:16 Reel — logo, headline, CTA button — rather than cropping away three
quarters of the frame. Needs `tools/fonts/BebasNeue-Regular.ttf`.

`tools/upscale_gallery.py` crisp-upscales their 376x251 gallery thumbnails
to ~1500px (`fal-ai/recraft/upscale/crisp` — resolution only, no generative
reinvention, so we never fabricate architecture they didn't build).

Set `FAL_KEY` before running any of those:

```bash
export FAL_KEY="$(grep -E '^FAL_KEY=' "<BBL>/products/image-pipeline/.env" | cut -d= -f2-)"
```

## Screenshots

```
py -3 tools/shoot.py          # full-page desktop + mobile (uses ?still)
py -3 tools/shoot.py --live   # viewport only, animations running
```

## ⚠️ Before this takes real leads

**The form does not go anywhere yet.** `#sabreForm` has an empty
`data-webhook-url`. With it empty the page shows the success state and logs a
console warning — fine for a demo, **not** fine for live traffic. Set it to a
Zoho Forms / CRM webhook endpoint before this page is advertised:

```html
<form id="sabreForm" data-webhook-url="https://...">
```

The submitted payload includes `full_name`, `phone`, `email`, `suburb`,
`project_type`, `message`, plus `submitted_at`, `fill_seconds` (bot speed-trap),
`landing_page` and `referrer`. There's a honeypot field named `website` —
non-empty means bot, and the submit is silently dropped.

## Facts on the page — where each came from

Everything factual is from Sabre's own site. Nothing invented.

| Claim | Source |
|---|---|
| 25+ years, family-owned, domestic + commercial | sabreconstructions.com.au home/about |
| QBCC Builders Licence 328475 | their contact page |
| 07 3823 3200 · fax 07 3823 1121 | their contact page |
| 3/73-75 Steel St, Capalaba QLD 4157 · Mon–Fri 8am–4pm | their contact page |
| Katrina Field testimonial (verbatim) | their testimonials page |
| Project names: Brighton, Clarence, Alexandra, Killarney, Clapton, Marcoola | their gallery page |

## ⚠️ The testimonial carousel is AI — it cannot go live

The three clips in the "People who've built with us" carousel are
**AI-generated people reading a script** (`fal-ai/veo3.1`, see
`tools/gen_testimonials.py`). They are a proof of concept for the format only.

Three separate safeguards, all of which must stay until real footage replaces
them:

- a yellow warning panel above the carousel
- an "AI demo" chip on every slide
- a burned-in `AI DEMO - NOT A REAL CUSTOMER` bar across the top of each video
  file, so a clip can't be mistaken for real if it ever leaves this page

Publishing AI-generated customer testimonials as genuine is misleading conduct
under Australian Consumer Law and breaches Meta and Google ad policy. Replace
them with real clients filmed on a phone — fifteen minutes each — before this
page is shown to the public as a live site.

The written Katrina Field quote further down the page **is** real, taken
verbatim from Sabre's own testimonials page.

**Still needed from the client:**

- Form endpoint (above)
- Email address — theirs is JavaScript-obfuscated, so the page uses phone + form only
- More testimonials — only one is published on their current site
- The year they were established, if they want it stated instead of "25+ years"
- Confirmation the "fixed price before you commit" and "one point of contact"
  claims in the copy match how they actually operate

`<meta name="robots" content="noindex, nofollow">` is set, so this page won't
compete with their real site in search. Remove it if it ever becomes the
primary page.
