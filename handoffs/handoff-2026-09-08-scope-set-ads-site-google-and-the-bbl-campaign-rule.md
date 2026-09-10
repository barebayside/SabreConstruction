# Handoff — 2026-09-08 — Scope set: ads + site + Google, under the BBL campaign rule

## Session Focus

A short BBL-side planning session in which Edward set the working scope for the two client
engagements (Sabre and Oodles of Paws) and the rule they both run under. Nothing was built for
Sabre today. This note exists so a dedicated Sabre session can start from it.

## What Got Done

- **Scope confirmed for Sabre:** BBL does the **ads** and the **website build**. Leads go to
  Nathan's inbox through the Formspree form on the real site. **No CRM** for Sabre.
- **Google added to the scope:** Meta ads PLUS Google Ads (search, modest spend) PLUS work on
  how Sabre shows up in Google search and in AI answers. The competitor report already measured
  the baseline: Sabre absent from all 13 searches and all 5 map boxes; no AI assistant names
  anyone for Wynnum/Manly rebuild questions.
- **The BBL campaign rule now binds this client** (memory `bbl-client-campaigns-follow-the-registry`):
  every Sabre ad gets a BBL registry code (brand code **SAB**), the code is the ad name in Meta
  and Google exactly, and results (spend, impressions, CTR, clicks, leads, CPL, five-tests
  verdict) are logged on the asset record weekly from Ads Manager. The registry lives in
  `BBL/docs/registry/`; the philosophy in `BBL/docs/THE-CAMPAIGN-SYSTEM.md`; metrics in
  `BBL/docs/reference/paid-ads-playbook.md`.
- **fal for Sabre = Sabre's own key**, `~/.keys/sabre-fal.key`, set per terminal only
  (`$env:FAL_KEY = (Get-Content "$HOME\.keys\sabre-fal.key" -Raw).Trim()`). Download every
  generated file into this repo's assets (or the client's OneDrive) — fal's hosted links expire.
- **Meta:** Sabre's portfolio invite reached Edward's Hotmail account on 09-07 and is accepted.
  Log in with Hotmail in Chrome for anything Meta.

## Files Changed / Created

| Path | What |
|---|---|
| this file | the only change in this repo today |
| BBL memory `bbl-client-campaigns-follow-the-registry.md` | the campaign rule (new) |
| BBL memory `oop-meta-business-portfolio.md` | OOP scope (for the other session) |

Nothing deployed. This demo repo is still 9+ commits ahead of origin (unpushed since 09-05).

## Decisions Made

1. **Sabre = ads + site, leads to inbox, no CRM.** → this handoff; `docs/engagement.md` still
   needs a 2026-09-08 line saying so.
2. **Google Ads + search/AI visibility are in scope**, at modest spend. → this handoff.
3. **Sabre ads run under the BBL registry with brand code SAB.** → memory
   `bbl-client-campaigns-follow-the-registry`. The SAB row in `brands.csv` and the results block on
   asset records are **not built yet** (awaiting Edward's "go" in the BBL session).
4. **Sabre uses Sabre's fal key; BBL's key never touches Sabre work.** → memory `sabre-constructions-project`.

## What's NOT Done — TODO

**Carried from 09-05 (unchanged, still first):**
1. [ ] Edward: Catalyst Console promote Development → Production (Serverless only, Generate Diff first).
2. [ ] Claude, after promote: Production flags → 1; re-push the authored v4 to
       `/report-v4/795000000099330`; confirm the §01 search table live; guard on the live page.
3. [ ] Only then give Nathan the report link.
4. [ ] Run sheet leftovers: Zoho Sign for the agreement (entity check first — 29 107 425 703 vs
       29 673 587 472), **Google Ads manager link** (now more urgent — it is in scope), Formspree
       inbox check, Melbourne IT / iSonic / HeyGen / GBP / shared folder, reference sites, the two
       numbers (value of a build, monthly ad budget), the three voice-of-customer questions,
       gallery/team keep-or-slim, confirm 1990.
5. [ ] Website build proper: Wynnum + Manly pages first, homepage title, Services field,
       block-check page — per the campaign plan and the report.
6. [ ] Push this demo repo.

**New today:**
7. [ ] Add a 2026-09-08 scope line to `docs/engagement.md` (ads + site + Google; no CRM).
8. [ ] Google Ads: confirm Nathan's account exists, get the customer ID, put it in the BBL
       `brands.csv` SAB row alongside the Meta ad account ID.
9. [ ] First ad set: codes via `/bbl-asset-code` (SAB-AWR-…), creative per the campaign plan,
       landing on the real site's Wynnum/Manly pages or the contact form. Do not build the ads
       before the registry rows exist — the rule is code first.
10. [ ] Search/AI visibility plan: the head terms from the report ("builders <suburb>",
        "knockdown rebuild <suburb>", "custom home builders Brisbane bayside"), GBP access, the
        suburb pages, and what an AI assistant would need to name Sabre. Ties to item 5.

**Still blocked** — open items 1, 6, 7 (AI testimonials, other practice's design, AI team photo).

## Quick Context for Next Session

**Two folders.** Demo/workshop: `Desktop\Sabre Constructions\` (this repo). Real site:
`Desktop\sabre-constructions-website\` (own `CLAUDE.md`). Read this repo's `CLAUDE.md` →
`docs/engagement.md` → `docs/open-items.md` → the 09-05 handoff for the report story.

**Before any fal job:** load Sabre's key per terminal. **Before any PDF:** Edge headless, not
Chrome (TotalAV). **Before any Meta screen:** Hotmail login, Chrome.

**Most likely next task:** the Google Ads account link and the first SAB ad set, in that order,
with the report's search findings driving which suburb pages get built first. The Catalyst
promote (item 1) is independent and can happen any time Edward is in the Console.

## Addendum (later 09-08, from the BBL session) — the report is live; the Google link never completed

- ✅ Catalyst promoted; Sabre's report link now carries the §01 search table and passed both gates.
  **The link can go to Nathan.**
- ⛔ **Google Ads: the manager account (775-584-9139) shows NO client accounts.** The 09-05
  "a bit funny" access was never an accepted manager link. Need Nathan's 10-digit customer ID →
  link request from the manager → Nathan accepts (Admin → Access and security → Managers → Accept).
- Meta: check Business settings → Partners on the Hotmail login first; Sabre should still be there
  (invite accepted 09-07). If not, Nathan re-shares via Partners → Add → BBL business portfolio ID.
  Instructions were written in the BBL session chat (see BBL handoff 09-08 Part 2).
- Record the customer ID + `act_` id in BBL `brands.json` SAB row when they arrive.
