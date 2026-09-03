# Handoff — 2026-09-03 — Working agreement, Saturday run sheet, campaign plan

## Session Focus

Nathan is coming to Edward's place **Saturday 5 September**. Built the three things
that day needs: a signable working agreement, a run sheet of everything that can only
be done with Nathan present, and a full campaign plan for the knockdown-rebuild avatar.

## What Got Done

**Working agreement (barter, in writing for the first time)**
- Plain-English agreement covering website + Google Ads + Meta ads + content, in exchange
  for materials at cost, point of call, and deck assistance.
- **Sabre's ABN found and verified: 29 107 425 703** (ACN 107 425 703, active 31 Jan 2004,
  postcode 4157 — matches the Steel St address). ⚠️ A second live company exists,
  **Sabre Constructions QLD Pty Ltd, ABN 29 673 587 472** (registered 12 Dec 2023, 4154).
  Must confirm which entity Nathan trades through **before signing**.
- Rendered to `Sabre-BBL-Working-Agreement.pdf` (5 pages, A4) via headless Chrome.
  Signature block built for **Zoho Sign** — two columns, plain white, labels above
  generous blank areas, block set not to split across a page.

**Saturday run sheet** — 12 blocks, ~3 hrs, tickable in the browser and printable.
Covers agreement → domain/DNS → GitHub → fal → HeyGen → Formspree → Google Ads →
Meta → Google Business Profile → shared folder → the conversation → close-out.

**Campaign plan** — avatar, voice of customer, positioning, six ad angles, three SVG
figures (the stuck loop, the five gates, a full client-acquisition schematic with
title block), Google + Meta campaign structures, tracking, KPIs, review cadence.

## Files Changed / Created

| Path | What | State |
|---|---|---|
| `docs/agreement/2026-09-03-sabre-bbl-working-agreement.md` | Editable source | gitignored |
| `docs/agreement/2026-09-03-sabre-bbl-working-agreement.html` | Render source | gitignored |
| `docs/agreement/Sabre-BBL-Working-Agreement.pdf` | **The signable file** | gitignored |
| `docs/sessions/2026-09-05-saturday-setup-runsheet.html` | Run sheet for the day | gitignored |
| `docs/sessions/design-plan-knockdown-rebuild.html` | **The campaign plan** | gitignored |
| `docs/reference/design-plan-knockdown-rebuild.md` | Pointer only — no content | in repo |
| `docs/engagement.md` | Old site stays up until new build accepted | in repo |
| `.gitignore` | Added `docs/agreement/` and `docs/sessions/` | in repo |

⚠️ **Repo is still 5 commits ahead of origin and nothing new has been committed.**
The `site/` skeleton and `review/index.html` from 2026-08-24 remain unpushed.

## Decisions Made

1. **Agreement is 6 months, then month-to-month, 30 days notice.** No materials cap —
   "at cost is what it is" (Edward, this session). → `docs/agreement/`
2. **Ad spend is excluded from the barter.** Sabre pays Google and Meta directly on
   their own card. Closes the open question in `engagement.md`.
3. **Every account opens in Sabre's name**, BBL added as manager/partner, Sabre keeps
   everything on exit. → agreement clause 6.
4. **Review generation removed from scope** — Edward can't deliver it with current
   access. A single ACL clause on accurate ratings was kept.
5. **fal AND HeyGen, both.** The BBL "never both" rule is a BBL decision (Edward films
   himself once); it does not bind Sabre, because nobody there will re-shoot on demand.
   fal = images + build video; HeyGen = presenter volume. → memory `sabre-constructions-project`
6. **HeyGen via the pay-as-you-go API wallet, not the $29 Creator plan.** Creator is
   web-only with one seat, which would mean sharing Nathan's password. API keeps Edward
   on his own machine. → run sheet block 5
7. **Formspree in Sabre's name** over the FormSubmit relay already in `qualify.js` —
   for the record it keeps, not the email it sends.
8. **The real site repo is a free GitHub Organisation owned by Sabre**, Edward added as
   Owner. Not a personal repo.
9. **Old site stays up until the new build is accepted**, then cut over in one go.
10. **Positioning: Sabre sells the postcode, not the house.** Entry offer is a free
    block check against the character overlay. → campaign plan §3

## Resolved failures

**The campaign plan was written without the playbook that already existed.**
- *What was broken:* first draft had a generic media plan, no Meta/Google split, no
  campaign structures, no analytics, and an unexplained colour legend on the ad cards.
- *Why:* only `foundations.md` and `page-structure.md` were read. `BBL/docs/reference/paid-ads-playbook.md`
  and its **critique file** were never opened, despite `bbl-links.md` naming both.
- *What fixed it:* Edward called it out as generic. Reading both files produced the
  campaign structures, the ad-set buckets, the tracking section and the testing windows.
- *Lesson:* `bbl-links.md` is a routing table, not a reading list to skim. When it names
  a canonical source for the task at hand, open it.

**The block-check form opened with an address field.**
- *What was broken:* proposed "type your address" as the first form field.
- *Why:* invented from the offer concept rather than the playbook, which states
  **"the first question is NEVER contact details."** Edward also correctly noted that
  geo-targeting already handles suburb, so the address qualified nothing.
- *What fixed it:* rebuilt as two radio questions — "which best describes you" and
  **"roughly when was the house built"** (pre-1947 = the overlay risk, and the real
  qualifier). Address is now optional at the end. Schematic and §3 updated to match.

**PDF re-render silently failed twice.**
- *Why:* the PDF was open in a viewer, so Chrome could not overwrite it — and the
  command reported success because the old file still existed.
- *What fixed it:* render to `%TEMP%` first, then `Move-Item` with a try/catch that
  reports LOCKED. Reuse this pattern; don't trust a bare `Test-Path` after a render.

**Chrome headless screenshot returned nothing.**
- *Why:* a normal Chrome instance was running and holding the default user-data-dir.
- *What fixed it:* `--user-data-dir="$env:TEMP\chrome-shot-profile"`.

## What's NOT Done — TODO

**Before Saturday**
- [ ] Fill the two remaining agreement blanks — Edward's days per month, Nathan's
      assistance days. Then re-render the PDF.
- [ ] Create Edward's own **Google Ads Manager (MCC)** account if he doesn't have one.
- [ ] Have Meta Business ID and GitHub username written down.

**On Saturday — blocking everything downstream**
- [ ] **Confirm which Sabre entity** trades — 29 107 425 703 vs 29 673 587 472.
- [ ] Sign the agreement.
- [ ] **What is one build worth to Sabre?** Nothing in campaign plan §10 can be judged
      without it.
- [ ] **Agree the monthly ad budget.** Still unagreed since 2026-08-17.
- [ ] Melbourne IT + iSonic logins.
- [ ] The three voice-of-customer questions (campaign plan §2).
- [ ] Nathan's reference sites — URLs, not adjectives.

**After**
- [ ] Push the 5 unpushed commits.
- [ ] Copy `site/` into the new Sabre GitHub org repo, enable Pages.
- [ ] Wire `js/qualify.js` to the Formspree endpoint and change `LEAD_EMAIL` off
      `edasturner@gmail.com` (open item 2).
- [ ] Rebuild the form to the §8 design (radio-first).
- [ ] Set up tracking **before** any ad runs — especially **call tracking**.

**Still blocked**
- [ ] Everything in `open-items.md` items 1, 6 and 7 — the AI testimonials, the
      other practice's design, the AI team photo.

## Quick Context for Next Session

**Project:** `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`

**Read first:** `CLAUDE.md` → `docs/engagement.md` → `docs/open-items.md`. For anything
campaign- or design-related, open `docs/sessions/design-plan-knockdown-rebuild.html`
in a browser — `docs/reference/design-plan-knockdown-rebuild.md` is only a pointer.

**Method sources that must actually be opened** (not skimmed): `BBL/playbook/foundations.md`,
`BBL/docs/reference/paid-ads-playbook.md`, and `BBL/docs/reference/paid-ads-playbook-critique.md`.
The critique matters — it flags "just run one platform" and "stat-sig is for cowards" as
wrong at a small budget.

**Most likely next task:** post-Saturday — fill in the answers Nathan gave, then create
the GitHub org repo and move `site/` into it.

**Fastest path to done:** the two numbers from Nathan (build value, monthly budget)
unblock more of the plan than any other single input.
