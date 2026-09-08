# Design brief — the look, done properly this time

> **Layer 4. Canonical for the visual direction from 2026-09-08.** Supersedes the "one
> adjustment, no redesign" line in the campaign plan §13. Edward (2026-09-08): "I'm not
> confident on the design at all. I want us to go through a proper design setup as well as a
> website structure." The eight pages built on 09-08 keep their CONTENT and STRUCTURE; the
> SKIN is not accepted and changes when this brief is decided.

## 1. The brand tokens — read off Sabre's own signage, not chosen by us

Source: the fence mesh banner proof, Wild Web Print & Sign job 8574, 27 Aug 2026
(`brand/2026-08-27-mesh-banner-proof-wildweb-8574.pdf`). Pixel-sampled at 4x render.

| Token | Value | Where it comes from |
|---|---|---|
| **Black** | `#090305` (use `#0A0A0A`) | The banner's ground. **The brand is black-first**, not off-white-first |
| **Red** | `#EB2227` | The headline, the diagonal bands, the icons. This is the print red. The site's current `#FF1A1A` came from a screen PNG and is hotter. Replace it |
| **White** | `#FFFFFF` | The wordmark, the contact line, the credentials |
| Grey | `#C8C8C8` | Only the QR code and the Master Builders mark. Not a brand colour |

Two colourways exist on the proof: headline in red (page 1) and headline in white (page 2).
Everything else identical. Either is on-brand.

**Type, as actually printed:**

| Role | What it is | On the web |
|---|---|---|
| Messaging headline ("Knock Down Rebuilds"), contact line | **Arial Bold**, sentence case, tight. Straight-leg R and cut terminals say Arial, not Helvetica | System `Arial, "Helvetica Neue", Helvetica, sans-serif` at weight 700. Nothing to load, matches the signage exactly |
| Wordmark "Sabre" | A heavy squared-rounded extended sans (Eurostile / Microgramma family), white | **Never set in live text.** Always the logo file. Ask Wild Web or Nathan for the vector |
| "CONSTRUCTIONS" | Extended uppercase sans, wide tracking, white | Same: logo file only. If a label style is wanted that echoes it, **Michroma** (Google Fonts) is the closest free extended face |

What this means against the current `site/docs/design-system.md`: Bebas Neue, Plus Jakarta Sans
and DM Mono were the DEMO's choices. None of them is on anything Sabre has printed. The banner
says: Arial Bold for headlines, black ground, one red, white text. That is a stronger, plainer
brand than the demo, and it is theirs.

## 2. Structure — what is settled and what is not

Settled (campaign plan §12, built 09-08): the six inherited URLs stay, plus
`/can-we-knock-it-down/`, `/wynnum/`, `/manly/`. Every page ends in the block check.
Content on those pages is fact-checked against `site/docs/client-facts.md` and stays.

Not settled: page rhythm, hero treatment, how photography is used, navigation style, whether the
site is dark-first (the banner says yes) or light with dark bands (the demo says yes), and
motion. These come from the reference sites, below.

## 3. Reference sites — Edward is collecting these

Add one row per site. "Steal" means the specific feature, not the whole look.

| URL | What to steal | Which Sabre page it belongs on | Notes |
|---|---|---|---|
| https://hedgerconstructions.com.au/ | The hero: a full-bleed drone flyover, no headline shouting over it. Then calm alternating white/black bands, image one side, words the other, one "learn more" each | Home, and the band rhythm for every page | Edward 2026-09-08: "I love the hero being the flyover video and not having the page so much in your face." Thin white nav on the video |
| https://www.yamavans.com/ | Zoomed-out scale: small headline top-left, huge air, the video BELOW the headline, a ruled three-number row (5 / 30+ / 100+), model showcase with specs, one dark image mosaic, one wide photo with a single line on it, testimonials as plain text | Home (scale and air), Designs (the showcase) | Edward: "you have to zoom out a bit so you can see the different sections as you work down" |

**Built from these, 2026-09-08 — `design/index.html` in this repo (open it in a browser):**
`option-a.html` = the Hedger read (dark-first, alternating bands) · `option-b.html` = the Yama read (light,
editorial, stat row, design showcase) · `option-c.html` = the signage (black, red diagonals, one red word
per headline). Same content on all three: the BBL conversion spine (hero + one CTA → checkable proof →
the problem in their words → three benefits → four steps → real reviews → fair questions → the free
block check), the five tests per section, CTA formula "Check my block, free" with the cost stated
("two questions, no address needed, no obligation"). Hero video on every option = Nathan's real phone
clip from a Sabre site (14 Aug 2026, a Queenslander being raised): portrait on phones, a wide crop on
desktop, in a labelled slot until the drone flyover exists. Generator lived in the session scratchpad;
the HTML is plain and self-contained.

**Requested feature: the house cutaway.** A view where the house "cuts away" so you see inside:
rooms, structure, the build under the skin. Edward has seen it done with AI image generation.
How it can be built, honestly:

- **Scroll-scrubbed image sequence.** 8 to 24 frames of the same house progressively cut away,
  scrubbed by scroll position. Plain HTML plus a few lines of JS, no 3D engine, works on phones.
  The frames are the hard part.
- **Where the frames come from.** Generated from one of **Sabre's own designs** (Killarney,
  Waderbird, Alexander, Belmont, Chelsea, Clarence; their renders are in the real repo as
  `assets/img/design-*.jpg`) with an image-edit model on Sabre's fal key, camera locked, each
  frame derived from the last. **Rule 7 applies:** it must be a Sabre design, and it is labelled
  a visualisation, never a finished build. Not another practice's plans (open item 6).
- **A true 3D model** (Three.js, orbitable, clip-plane cutaway) is possible but needs a real
  model of the design from Sabre's designer, and is heavier on phones. Second option, not first.
- Budget anchor: the 16.5 s rebuild clip cost $2.97 on fal. A frame set is of that order.

## 4. The process from here

1. Edward brings the reference sites. They go in §3 as rows.
2. Claude builds **two or three homepage options** as static mock pages in the workshop repo
   (this one, public, so no client data): same content, different skins, each using the §1 tokens.
   Screenshots at desktop and phone before anyone looks (memory: screenshot before presenting).
3. Nathan picks. The campaign plan's brief is "let him choose, not present one and defend it".
4. `site/docs/design-system.md` is rewritten from the chosen option. Only then are the real
   pages re-skinned. Content does not change in that step.
5. The cutaway is built after the skin, as its own registry asset, on the design Nathan names.

**State 2026-09-08 evening: steps 1–4 DONE.** Edward chose **Option A**. `site/docs/design-system.md`
rewritten from it; `site.css` v4; all nine real pages re-skinned; content unchanged; committed, not
pushed; noindex. Nathan has not seen it yet. Step 5 (the cutaway) is next, on the design Nathan names.
