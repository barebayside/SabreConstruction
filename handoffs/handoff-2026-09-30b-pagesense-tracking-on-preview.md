# Handoff — 2026-09-30 (b) — PageSense tracking on the preview site

## Session Focus
Put Sabre on the same tracking as the other sites, so its visits, goals and heatmaps flow into BBL's Zoho Analytics every night. (Main work was OOP and BBL; see their 2026-09-30b handoffs.)

## What Got Done
- **PageSense snippet on all 64 pages** of the real site repo, before `</head>`: project `sabre-construction` in BBL's portal `yourrentalhomefinders`, script `cdn-au.pagesense.io/js/yourrentalhomefinders/ef153ad74f1543eca885eafa3840102e.js`.
  - `tools/build_post.py` keeps each page's head, so rebuilding a post keeps it.
- **`js/enquiry.js` v2:** after Formspree accepts a send, it pushes `trackEvent sabre_lead_submitted`, waiting for PageSense's push hook (the OOP pattern). `?v=2` on every page.
- Commit `b650bdf`, **pushed and read back live** on the preview (`sabre-constructions.github.io/sabre-constructions-web-site-/`).
- **PageSense goals** (made via MCP):
  - Tap to call (`tap-to-call-2`, contains `422831306`)
  - Email tap (`email-tap`)
  - Lead submitted (`lead-submitted-2`, custom event `sabre-lead-submitted`)
- **Heatmaps (DRAFT until Edward clicks Launch):** Home (regex that matches both the preview and the real domain), Contact page (`/contact/`), Knockdown page (`/can-we-knock-it-down/`).
- Edward set PageSense privacy to **"Do not notify visitors"** and added his IP filter.
- BBL `refresh.py` now picks up Sabre's daily numbers as soon as there are visits.

## Files Changed / Created
| Path | What |
|---|---|
| real repo (`Desktop\sabre-constructions-website`) all 64 `*.html` | PageSense snippet; `enquiry.js?v=2` |
| real repo `js/enquiry.js` | Lead submitted event on successful send |

## Decisions Made
1. Sabre tracking lives in BBL's PageSense portal, like OOP (one BBL Analytics workspace for every managed site).

## Resolved failures
- **MCP `createProjectGoal` (link click) refused.** It needs `goal_url` plus a non-empty `include_urls` value.

## What's NOT Done — TODO
1. **Edward: launch the 3 Sabre heatmaps.** In PageSense Heatmaps, set the filter to Draft, then click Launch on each.
2. **Proof test:** on a phone using mobile data, open the preview and tap the phone number; the Goals screen should show 1. This is still to be done.
3. Numbers stay near zero until the **DNS cutover**; sabreconstructions.com.au is still the old site.
4. Fill scroll depth via MCP once the heatmaps have visits.

## Quick Context for Next Session
- Tracking is in; nothing else changed on the site. Main Sabre threads are unchanged (see `handoff-2026-09-30-knockdown-video-filed-drafted-placed.md`).
