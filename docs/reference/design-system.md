# Design system — the workshop (demo + ad landing pages)

> **Layer 4.** Covers `css/sabre.css` and `css/lp.css` — the demo site, the ad
> concepts and the three landing pages. **This is not the real website.**

## ⛔ Palette and type live somewhere else now

The colours and the type stack are **shared with the real website**, so there is
only one source for them:

```
site/docs/design-system.md
```

Read it there. Do not restate the hex codes in this file — two copies of a
palette is how a brand drifts.

Short version so you know what you are dealing with: Sabre red `#FF1A1A` on
near-black `#0B0B0C` over warm off-white `#F6F4F1`, both reds sampled from their
own logo. Bebas Neue for headings, Plus Jakarta Sans for body, DM Mono for
labels.

⚠️ Same gotcha applies here: **heading elements get no size by default.** `h1`
alone renders at browser default. You must add `class="h1"`. The scale lives in
`css/sabre.css` as `.h1` / `.h2` / `.h3` / `.lede`.

## What this file IS still the source for

Everything below — the motion engine, the demo components and the landing-page
components. **None of it exists in `site/`**, which has its own much simpler
stylesheet. Do not copy these classes across.

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
