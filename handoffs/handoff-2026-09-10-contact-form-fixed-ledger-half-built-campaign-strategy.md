# Handoff — 2026-09-10 — The contact form fixed and wired for the ledger; the Zoho Flow build written; the campaign strategy

## Session Focus

Edward asked for three things: start the Zoho Flow (the lead ledger + Meta loop agreed 09-09),
finish the website, and start designing the campaign strategy. Reading the real site first turned
up a live bug that came before all three: **the contact page's form could not be submitted.**

## What Got Done

**The website (real repo `Desktop/sabre-constructions-website`, v18 → v19)**
- **Found:** `contact/index.html` had the three-step form markup but **no `<script>` at all** — the
  home page's form script was inline and never copied across. Steps 2 and 3 were `position:absolute;
  opacity:0; pointer-events:none`, so nobody could reach suburb/name/email/mobile. This is the page
  every "Book a walk-through" floating button leads to. Live on the preview since the 09-08 push.
- **Fixed:** new shared `js/enquiry.js`, loaded (deferred) on all 11 pages. It does three jobs:
  the three-step slide on any page with the form; **visit capture** (`utm_source/medium/campaign/
  content/term`, `fbclid`, `gclid`, first landing page, referrer — kept in `sessionStorage` so an ad
  click on `/wynnum/` still carries its code when they enquire on `/contact/`); and on submit a
  **form-encoded copy of the row to `FLOW_URL`** (the Zoho Flow webhook; empty today, so nothing is
  sent) before the unchanged Formspree POST. Formspree now receives the hidden fields too, so
  Nathan's email shows the asset code.
- Both forms carry eleven hidden inputs (`utm_*`, `fbclid`, `gclid`, `landing_page`, `referrer`,
  `page`, `fill_seconds`). Home page's inline script removed. CSS: `.js .wiz-step…` so the steps
  hide only when JavaScript runs (`html.js` set in `<head>`); without JS all three show and the
  form posts normally. `site.css?v=19` on every page.
- **Tested for real** in headless Edge over the DevTools protocol (scratchpad `test_enquiry.mjs`):
  land on `/wynnum/?utm_…&fbclid=…` → `/contact/` carries every value; steps forward/back; mobile
  field visible + clickable on step 3; the Formspree body contains describes/built/suburb + codes +
  `fill_seconds`; success line; **deliberate 500 → error line + button re-enabled** (rule 4's second
  half); home form too; no-JS render. **23/23.** Screenshots at 1400 and 500 wide look right.
  No real submission was sent (fetch stubbed).
- Committed `6a1ec4c`. **NOT pushed** (memory rule: commits only). One push puts the fix on the preview.

**The Zoho Flow (lead ledger + Meta loop) — the parts that can be built without Edward's login**
- `docs/tasks/lead-ledger-build.md` — click-by-click, UI labels checked against Zoho's help pages
  today: the Sheet (25 columns, `outcome` as a validated list), **Flow 1** (Webhook trigger set to
  **form data** → Zoho Sheet **Create row** → email to Edward → Decision "qualified?" →
  `meta_capi_event` → Update row `meta_lead_sent`), the Meta plumbing Nathan must do (ad account
  assign, dataset, system-user token, verification), **Flow 2** (Zoho Sheet **Row updated in a
  column** `outcome` → Won and not yet sent → `Purchase` event → stamp `meta_won_sent`), the
  sample payload to paste into the trigger's Test, proofs for every step, a what-can-go-wrong table.
- `tools/flow/meta_capi_event.dg` — the Deluge custom function (9 string inputs, returns
  `sent n` / `error …` so the Sheet cell shows what happened). Phone → digits, `61` prefix,
  `zoho.encryption.sha256` (hex by default, verified on Zoho's page); email lowercased + hashed;
  `fbc` built from `fbclid`; `test_event_code` passed through while testing. ⚠️ **Not yet run
  against a real dataset.**

**Campaign strategy — `docs/reference/campaign-strategy.md` (canonical from today)**
- Reconciles the 09-03 plan to what changed: the walk-through is the front door (block check second,
  on the contact page and in the Google "Can I" group); Nathan not Stewart; **Tide already runs the
  "love your street, outgrown the house" Meta line**, so Sabre's cold open carries the thing Tide
  can't say — the builder who walked your old house answers the phone to the keys; the Wynnum/Manly
  rebuild **search is unbought** (Fiteni = estates, Blueneer = roofing); the ledger + CAPI replace
  "a Google Sheet by hand"; Nathan's mobile on the site makes call tracking a decision, not a default.
- Six doors re-cut with build state (two 🟢, two 🟠, two 🔴). Google: 4 campaigns, 7 ad groups **=
  7 proposed codes** (`SAB-SOL-KDR-2.0A…7.0A_GOOGLE_SEARCH`, `SAB-CON-KDR-5.0A_GOOGLE_SEARCH`),
  keywords, landing pages, negatives, Presence targeting, auto-tagging, conversion actions. Meta:
  1 campaign, ABO, 3 ad sets, ads with proposed codes (`AWR-KDR-7..9`, `CON-KDR-6..7`,
  `SOL-KDR-8..9`), the settings to switch off. Measurement chain drawn. Budget phases (proposal).
  Targets. Search/AI visibility (GBP first). **Ten launch gates — eight are ⛔ today.** The first
  afternoon of building, in order.
- Codes are **proposed, not scaffolded** — the registry rule is code-before-build, and nothing gets
  built before Nathan's two numbers. `/bbl-asset-code` scaffolds them in five minutes when he does.

**Housekeeping**
- `CLAUDE.md` router: two new rows (ledger build; campaign strategy). `engagement.md`: 09-10 block +
  ledger to-dos ticked where done. `open-items.md`: the form bug in Resolved. `lead-ledger-and-meta-loop.md`:
  status note (form data, not JSON). Registry: `change_log` + `status_history` entries on
  `SAB-SOL-KDR-1.0A_WEB_LP` and `SAB-AWR-KDR-1.0A_WEB_HOMEPAGE`; `_regen.py` run.

## Files Changed / Created

| Where | What | State |
|---|---|---|
| real repo `js/enquiry.js` (new), `css/site.css`, all 11 `index.html` | v19 as above | committed `6a1ec4c`, **1 ahead, not pushed** |
| `docs/tasks/lead-ledger-build.md` (new) | the Zoho build, click by click | committed (this repo) |
| `tools/flow/meta_capi_event.dg` (new) | Deluge CAPI function | committed |
| `docs/reference/campaign-strategy.md` (new) | canonical campaign structure | committed |
| `CLAUDE.md`, `docs/engagement.md`, `docs/open-items.md`, `docs/reference/lead-ledger-and-meta-loop.md` | routing + state | committed |
| BBL `docs/registry/marketing-assets/SAB-SOL…/meta.json`, `SAB-AWR-KDR-1.0A…/meta.json`, regenerated index/csv | change logs | on BBL's working tree (branch `feat/report-charts-and-clusters`), not committed |
| Memory `sabre-constructions-project.md` | 09-10 block | updated |
| Scratchpad `test_enquiry.mjs`, `wire_enquiry.py`, `update_docs.py` | the test + the two edit scripts | gone next session; the test is worth copying into `tools/` if the form changes again |

Pre-existing, left alone: this repo's uncommitted 09-08 leftovers (the 09-08 handoff addendum, the
re-rendered drone posters/videos, `design/problem-section.html`).

## Decisions Made

1. **The ledger row goes as form-encoded data, not JSON** — `URLSearchParams` via `sendBeacon` is a
   "simple" request (no CORS preflight) and matches Zoho's webhook "form data" mode exactly.
   → `enquiry.js`, `lead-ledger-build.md`, `lead-ledger-and-meta-loop.md`.
2. **One shared script for the form on every page**, not inline per page — the inline copy is how
   the contact page lost it. → `enquiry.js`.
3. **The form must work without JavaScript** (steps hide only under `html.js`). → `site.css`.
4. **Leave Nathan's real mobile on the site; track calls from ads with Google call assets and
   `tel:` taps as a soft conversion** — recommendation, Nathan's call. → strategy §6.
5. **Ad codes proposed in the strategy, scaffolded only when the budget exists.** → strategy §4–5, §11.
6. **`Purchase` is the Won event** unless the Meta campaign later uses the Conversion Leads
   objective (one string to rename). → `lead-ledger-build.md` step 5.

## Resolved failures

- **Contact form unsubmittable since 09-08** · no script on the page; the wizard CSS hid steps 2–3 ·
  shared `enquiry.js` + JS-gated CSS · found by grepping `<script` in `contact/index.html` (0 hits)
  before touching anything. *Lesson: after a generator writes N pages, check the one page whose
  behaviour matters most, not just the one the generator was written on.*
- **DevTools `/json/new?url` truncated the URL at the first `&`** · only `utm_source` reached the
  page · open `about:blank`, then `Page.navigate` with the full URL.
- **Background headless tab throttles `setTimeout` to ~1 s** · step checks read the state a beat
  early and "failed" while the detail column showed the right state · wait ≥ 2 s per step, launch
  Edge with `--disable-background-timer-throttling`.
- **Python `print` of the campaign-plan text died on cp1252** · `PYTHONIOENCODING=utf-8` on the call.

## What's NOT Done — TODO

**Edward, in order**
1. [ ] `git push` the real repo (v19) so the preview's contact form works — before Nathan is sent the link.
2. [ ] Send ONE real test enquiry from the preview (rule 4) and confirm the email lands in admin@.
3. [ ] Build the Sheet + Flow 1 (`docs/tasks/lead-ledger-build.md` steps 1–2, ~30 min) → **send Claude
       the webhook URL** → Claude pastes it into `FLOW_URL`, pushes, tests with `?utm_content=TEST-FLOW`,
       reads the row back, and confirms Formspree still delivers.
4. [ ] Google Ads: Nathan's customer ID → link from manager 775-584-9139 → Nathan accepts.
5. [ ] Meta: Sabre's ad account assigned to BBL; dataset + token (build doc step 3).

**Nathan (ask in one conversation)**
6. [ ] The two numbers: what a build is worth; the monthly ad budget.
7. [ ] The five claims (`positioning.md`), which QBCC number, the 20-second phone clip (strategy §5).

**Claude, when unblocked**
8. [ ] `FLOW_URL` + the Google tag into `enquiry.js`; conversion actions; Flow 1's Decision + function.
9. [ ] `/bbl-asset-code` scaffolds the 7 Google + first 4 Meta codes; then the ads, per strategy §11.
10. [ ] LocalBusiness schema on the site; GBP once access exists (strategy §9).

**Carried**
- Catalyst/report: done 09-08 — the link can go to Nathan. DNS (Melbourne IT / iSonic) still unanswered.
- Real footage replaces the drone hero, the 3 AI testimonial placeholders, the AI family frames.
- Registry: log v9–v18 on the SAB records; push this workshop repo (≈40 ahead).

## Quick Context for Next Session

Two folders. Workshop `Desktop\Sabre Constructions` (this): `CLAUDE.md` → `docs/engagement.md` (09-10
block) → for ads `docs/reference/campaign-strategy.md`, for the ledger `docs/tasks/lead-ledger-build.md`.
Real site `Desktop\sabre-constructions-website`: preview with `python -m http.server 8765`; after any
change to `js/enquiry.js` run `node --check`, bump `?v=` on every page, and re-run a functional test
(the scratchpad one is described above — rebuild it from this handoff if it is gone: headless Edge with
`--remote-debugging-port`, Node's built-in WebSocket, `Runtime.evaluate`).

**Most likely next task:** Edward comes back with the Flow webhook URL → paste, push, prove the row.
Or Nathan's numbers arrive → scaffold the codes and build the Google campaigns.
