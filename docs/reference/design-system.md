# Design system

> **Layer 4.** Canonical source for anything visual.

## Palette

Both sampled from `assets/img/sabre-logo.png`. Nothing else was invented.

| Token | Value | Use |
|---|---|---|
| `--red` | `#FF1A1A` | The shout colour. Buttons, bands, accents |
| `--red-d` | `#D10E0E` | Error text, hovers |
| `--ink` / `--black` | `#0B0B0C` | Text, dark bands |
| `--ink2` | `#4C4C52` | Body copy |
| `--muted` | `#86868E` | Labels, captions |
| `--paper` | `#F6F4F1` | Page background |
| `--white` | `#FFFFFF` | Cards, tinted sections |
| `--line` | `#E3DFD9` | Hairlines |

## Type

| Face | Role |
|---|---|
| **Bebas Neue** | All headings, buttons, numbers. Uppercase, tight leading |
| **Plus Jakarta Sans** | Body copy |
| **DM Mono** | Eyebrows, labels, metadata, anything in small caps |

Scale lives in `css/sabre.css` as `.h1` / `.h2` / `.h3` / `.lede`.

⚠️ Heading elements get **no size by default** — `h1` alone renders at browser
default. You must add `class="h1"`.

## Motion

Classes in `css/sabre.css`, all driven by one IntersectionObserver in
`js/sabre.js`:

| Class | Behaviour |
|---|---|
| `.reveal` | Fade up |
| `.pop` | Drops in from above with an overshoot |
| `.slide-l` / `.slide-r` | In from the sides |
| `.zoom` | Scale down into place |
| `.d1`–`.d6` | Stagger delays |

All of it collapses flat under `prefers-reduced-motion`.

**`?still` hook:** append `?still` to any URL and every animation snaps open —
for full-page screenshots. Inert for real visitors. Borrowed from the BBL site.

## Components

| Class | What |
|---|---|
| `.topbar` / `.tb-nav` | Sticky header + nav. `.always` pins it open |
| `.hero` / `.hero-media` | Full-bleed hero |
| `.marquee` | Scrolling suburb strip |
| `.reveal-stage` | Framed video player |
| `.carousel` / `.car-slide` | Peek carousel — active centred, neighbours scaled back |
| `.bento` / `.tile` | Mixed-size gallery grid, tiles open the lightbox |
| `.lb` | Lightbox (keyboard, swipe, backdrop close) |
| `.team-lead` / `.tcard` | Team block |
| `.worries` | Three one-line concerns |
| `.steps` / `.step` | Oversized numbered process |
| `.nums` | Credentials strip |
| `.faq` / `.fq` | Accordion |

Landing-page-only components are in `css/lp.css`: `.snap`, `.lpb-*`, `.g-*`,
`.qm-*`, `.lp-facts`, `.next3`, `.stars`, `.prev-bar`.

## Where the design came from

Structure follows the BBL landing-page system in
`Marketing AI content for Bare Bayside Labs/site/` — the sealed-room LP, the
`.reveal` engine, the Bebas/Jakarta/DM Mono stack.

The **look** is deliberately not BBL's. BBL is light editorial and calm; this is
loud, blocky and high-motion, with full-bleed red and black.

## Team photos

The source shots are cut-outs on flat white — which is exactly what an ID photo
looks like. They're knocked out to transparency (`t-*.png`) and sat on a dark
radial field so they read as portraits. Don't put them back on white.

## Rules that keep getting broken

1. **Bump `?v=N`** on every page linking a CSS or JS file you edited.
2. Sections inside `.band-red` inherit white text. Any white card inside one
   needs `color:var(--ink)` or its heading vanishes.
3. `.wide` sets side padding; a later `padding: Y 0` on the same element kills
   it and flushes content to the screen edge.
