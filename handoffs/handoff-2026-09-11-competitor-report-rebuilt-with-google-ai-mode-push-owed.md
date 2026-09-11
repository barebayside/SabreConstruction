# Handoff — 2026-09-11 — Competitor report rebuilt with a Google AI Mode column; the push is owed

## Session Focus

Sabre's competitor-intel report (`795000000099330`): fix the `[your service]` strings, add the
"best builder in <suburb>" AI questions, add Google AI Mode as a fifth AI column. All BBL-side
work is in the BBL handoff of the same date; this note is the Sabre-side state.

## What Got Done

- Report rebuilt: 13 AI questions × 5 engines (Perplexity, ChatGPT, Claude, Gemini, **Google AI
  Mode**). Prose rewritten to match. Both delivery gates pass.
- **What the AI data says about Sabre** (use in the site/GBP work):
  - Named **once in 65 checks** — ChatGPT, "best builder in Capalaba" — and it read the **old Steel
    Street, Capalaba address** off the Google listing. The GBP move to 40 Molle Rd, Ransome is now a
    report finding, not just a to-do.
  - Google AI Mode names **Tide on 7 of 13** questions and lists Google Business Profile cards: Pro
    Builder (5.0/68), Bay Built (5.0/15), OJ Pippin (4.5/96), Oceanview (Lota), Line and Form (Manly
    KDR) hold Wynnum/Manly. Reinforces `docs/reference/search-and-ai-visibility-plan.md`: the map box
    + suburb pages ARE the AI play.
  - Edward's own app/phone answers differ from the report's — the report asks the APIs with no
    location; each answer is one sample. The report's §02 intro now says so.
- Files kept here: `docs/sessions/2026-09-11-competitor-report-795000000099330-authored-ai-lane.v4.json`
  (**the file to push**) + `.html` (local render; ad images/videos 403 locally — Meta CDN — fine on the live page).

## Decisions Made

1. Google AI Mode is a permanent report lane (BBL `actor_map`), not a one-off for Sabre.
2. The Steel St address finding stays in the report; tell Nathan it is the one thing to close today.

## What's NOT Done — TODO

1. [ ] **Edward runs the POST** (auto mode blocks it) — command in the BBL handoff / `docs/STATE.md`
   top entry. Then verify the live page: `[your service]` = 0, `<suburb>` = 0, "Google AI Mode" ≈ 26,
   §3 media present. Then send Nathan the (unchanged) link.
2. [ ] GBP: address → Ransome, Services field, review asks naming the suburb — now with the AI receipt.
3. [ ] Nathan still hasn't been asked about the BBL footer credit / being named on BBL's about page (09-10).

## Quick Context for Next Session

Report link (unchanged): `https://barebayside-reports.zohostratus.com.au/r/f9Vmproivc-gxGiIztJHgEWVcSCM9elf/report.html`.
BBL-side detail: `Marketing AI content for Bare Bayside Labs/handoffs/handoff-2026-09-11-sabre-report-google-ai-mode-column-and-three-generator-fixes.md`.
Site work is unchanged from `handoff-2026-09-10b-…` — start there for anything on the website.
