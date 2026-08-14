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

## The hero video

Not stock. Built in two steps from the client's own photo:

1. `tools/gen_before.py` — takes their real finished home
   (`home-slide011607.jpg`) and ages it back into a run-down version with the
   same camera angle, via `fal-ai/nano-banana-2/edit`. Output: `hero-before.jpg`.
2. `tools/gen_video.py` — `fal-ai/kling-video/v3/pro/image-to-video` with
   `start_image_url` = the run-down frame and `end_image_url` = the real
   finished photo, so the payoff shot is genuinely their build, not an
   AI invention.

Then encoded down from 25 MB to ~1 MB:

```
ffmpeg -i hero-transform-source.mp4 \
  -vf "scale=1600:-2,tpad=stop_mode=clone:stop_duration=1.6,fps=25" \
  -c:v libx264 -pix_fmt yuv420p -crf 27 -preset slow -an -movflags +faststart \
  hero-transform.mp4
```

The 1.6s freeze on the last frame is deliberate — it holds on the finished
house before the loop restarts.

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
