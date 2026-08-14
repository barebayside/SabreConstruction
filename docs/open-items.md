# Open items — what's blocked, fake, or waiting

> **Layer 4.** Read this at the start of any session. Say `status` to get it
> summarised. Everything here is a real blocker or a real risk, not a wishlist.

## 🔴 Must be resolved before ANY of this goes public

| # | Item | Where | Who resolves |
|---|---|---|---|
| 1 | **The three testimonial videos are AI-generated people.** Not customers. Publishing them as real is misleading conduct under Australian Consumer Law and breaches Meta and Google ad policy | `assets/video/testimonial-*.mp4`, carousel in `index.html` | Film 2–3 real families on a phone, 15 min each |
| 2 | **The lead form goes nowhere.** `LEAD_EMAIL` points at Edward and the relay has never been confirmed — nothing arrives until someone clicks the confirmation email | `js/qualify.js` | Edward, then switch to Sabre's address |
| 3 | **The raise reels are an artist's impression** sitting on footage of a real, identifiable Sabre site with their signage on the fence | `assets/video/reel-*.mp4` | Caption "concept visualisation", or re-cut to land on a genuinely finished home |
| 4 | **Budget bands are invented.** Under $300k / $300–450k / $450–650k / $650k+ | `js/qualify.js` | Sabre confirms against real job sizes |
| 5 | **Claims Sabre has not confirmed** — "fixed price before you commit", "one point of contact", "we'll tell you if it's not your year", the free site visit itself | `index.html`, all LPs | Sabre confirms these match how they actually operate |
| 6 | **The rebuild render uses another practice's design.** The drawings are stamped NOT FOR CONSTRUCTION and their own note says visualisations are indicative only. The finished house on that page is an AI image derived from their elevation | `rebuild-render.html`, `assets/img/render/*`, `assets/video/rebuild-render.mp4` | Written OK from the designer **and** the owners. Address and owners' names stay off the page either way |

## ✅ Resolved

| Item | What happened |
|---|---|
| **Star ratings were empty slots** with a "needs real rating" chip | 2026-08-14. Sabre's Google Business Profile does exist: **4.5 from 11 reviews**. Real rating and real quotes are now on all three LPs, and the cleared quote list is in `reference/client-facts.md`. ⚠️ It is **4.5, not 5** — there's a genuine 1-star on the listing. Never round it up |
| **Concept 03 was 16:9** in a 9:16 placement | 2026-08-14. Regenerated natively vertical and ends on a Sabre card. Still an AI stand-in, still labelled — item 1 above still applies to it |
| **The LPs had their own header** | 2026-08-14. All three now use the same `.topbar` as `index.html` and `ads.html`, so there's always a way back to the main site |

## 🟡 Review scaffolding to strip before real ads run

| Item | Where |
|---|---|
| Preview switcher (`<nav class="prev-bar">` + `previewing` class on `<body>`) | all three `lp-*.html` |
| `LP 1 / LP 2 / LP 3` tabs in the main nav | `index.html`, `ads.html` |
| Medium pills (`LP 1 · Meta Reels · 9:16`) | all three `lp-*.html` |
| `<meta name="robots" content="noindex, nofollow">` — remove only if a page becomes the real primary | all pages |

## 🟢 Waiting on the client

| Item | Why it matters |
|---|---|
| **Real photos of Stewart, Cathy and Nathan** — on site, hard hat, on the tools | Current shots are cut-outs on white and read as ID photos. No better ones exist publicly: their judo club site is down (HTTP 508) and Facebook is behind a login |
| Their real email address for leads | Have it — `admin@sabreconstructions.com.au` — deliberately not wired |
| More **filmed** testimonials | Ten written ones now exist — their Google reviews, quoted on the LPs. What's still missing is footage. See item 1 |
| Vertical footage of Stewart or Nathan talking to camera, 8s | The only thing standing between ad Concept 03 and a live campaign |
| The year they'd like stated | 1990 founding is on their own team page; their homepage rounds to "25+ years" |

## Decisions already made — don't relitigate

| Decision | Reasoning |
|---|---|
| Section order on `index.html` | See `reference/page-structure.md`. Trust finishes by section 6 |
| Form embedded, not popup | They already opted in by tapping the ad |
| Landing pages: one per medium | Reels, Feed and Google need different shapes |
| The knockdown reel is letterboxed, not cropped | Its master is 2.38:1 from Sabre's own wide photo; a 9:16 crop loses three quarters of the frame |
| Underline, not strike-through, under "New home out" | A line through the payoff reads as crossing it out |
| Leads go to Edward, not Sabre | Client's inbox stays clean until they've agreed |
