# Task — build the lead ledger (Zoho Sheet + two Zoho Flows) and the Meta loop

> **Layer 3 task contract.** The *why* and the shape are in
> `../reference/lead-ledger-and-meta-loop.md`. This file is the *build*: what Edward clicks,
> what Claude pastes, and how each step is proved. Written 2026-09-10. UI labels checked
> against Zoho's help pages that day (webhook trigger; Zoho Sheet actions).
>
> **Where the site side stands (done 2026-09-10):** `js/enquiry.js` in the real repo already
> captures `utm_*`, `fbclid`, `gclid`, landing page and referrer on every page, puts them in
> hidden fields on both forms, and on submit sends one copy of the row to `FLOW_URL` as
> **form-encoded data** (no CORS preflight) before the normal Formspree POST. `FLOW_URL` is
> empty until step 2 below, so today nothing is sent anywhere but Formspree.

## Inputs

| Need | Where |
|---|---|
| The shape and the columns | `../reference/lead-ledger-and-meta-loop.md` |
| The page code that sends the row | real repo `js/enquiry.js` (top: `FLOW_URL`) |
| The Deluge function for Meta | `../../tools/flow/meta_capi_event.dg` |
| Flow custom-function gotchas | `~/.claude/skills/zoho-flow-custom-functions/SKILL.md` |

## The row the page sends (the contract)

Form-encoded, one key per field. This is exactly what the Flow's Webhook trigger sees.
Paste the sample below into the trigger's **Test** so every key becomes a variable:

```
submitted_at=2026-09-10T03:12:44.000Z&describes=I%20own%20a%20house%20I'd%20like%20to%20replace&built=Before%201947&suburb=Wynnum&name=Test%20Person&email=test%40example.com&mobile=0400000000&address=&utm_source=meta&utm_medium=paid&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-AWR-KDR-1.0A_META_VIDEO&utm_term=&fbclid=IwAR0test&gclid=&landing_page=https%3A%2F%2Fsabreconstructions.com.au%2Fwynnum%2F%3Futm_source%3Dmeta&referrer=(direct)&page=%2Fcontact%2F&fill_seconds=41
```

Keys, in order: `submitted_at`, `describes`, `built`, `suburb`, `name`, `email`, `mobile`,
`address`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `fbclid`,
`gclid`, `landing_page`, `referrer`, `page`, `fill_seconds`. Formspree's own `_subject` and
the `_gotcha` honeypot are NOT sent to the Flow.

---

## Step 1 — Edward: the Zoho Sheet

1. Zoho Sheet → **New spreadsheet**. Name it **`Sabre — Lead Ledger`**.
2. Rename the first worksheet **`Leads`**.
3. Row 1, one column each, exactly these headers (the Flow maps by header name):

```
row_id | submitted_at | describes | built | suburb | name | email | mobile | address | utm_source | utm_medium | utm_campaign | utm_content | utm_term | fbclid | gclid | landing_page | referrer | page | fill_seconds | outcome | outcome_date | notes | meta_lead_sent | meta_won_sent
```

4. Column `outcome` (U): **Data → Data validation → List** with `New,Contacted,Quoting,Won,Lost`.
   Nathan picks from the list; the Won trigger in Flow 2 depends on the exact word.
5. Freeze row 1. Share later (step 6) — not yet.

## Step 2 — Edward: Flow 1 "Sabre lead → ledger"

1. Zoho Flow → **My Flows → Create Flow**. Name: `Sabre lead → ledger`. **Create**.
2. Trigger: choose **Webhook**. In the Webhook trigger box click **Configure**.
3. Click **Copy** on the webhook URL. **Send that URL to Claude** — it goes into
   `js/enquiry.js` as `FLOW_URL`, then the site is re-pushed.
4. Data format: **form data**. **Next**.
5. **Test** with the sample row above (paste it as the body). Every key should appear as a
   variable. **Done**.
6. Action 1: **Zoho Sheet → Create row**. Spreadsheet `Sabre — Lead Ledger`, worksheet `Leads`.
   Map every column to the variable of the same name (`submitted_at` ← `${webhookTrigger.payload.submitted_at}` and so on). Leave `row_id`, `outcome`, `outcome_date`, `notes`, `meta_lead_sent`, `meta_won_sent` empty. (If the connection asks, sign in as the BBL Zoho One account — the Sheet is BBL's; it holds no CRM data.)
7. Action 2: **Zoho Mail → Send email** (or Email → Send email): to Edward, subject
   `Sabre lead — ${webhookTrigger.payload.suburb} — ${webhookTrigger.payload.utm_content}`, body
   = the fields, one per line. This is Edward's copy; Nathan's copy still comes from Formspree.
8. **Turn the Flow on.**

### Proof for step 2 (both must be true before anything else)

- [ ] Claude pastes the URL into `FLOW_URL`, pushes, and submits ONE test on the live preview with
      `?utm_content=TEST-FLOW&fbclid=TEST` on the landing page → **the row appears in the Sheet**
      with `utm_content = TEST-FLOW`, **and** Formspree's email still lands in admin@ (Nathan) —
      tell him a test is coming. Both, or it is not done (real-repo rule 4).
- [ ] Deliberately break it once: Edward turns the Flow off, Claude submits again → the Formspree
      email still arrives, no row. (Proves the ledger can never block an enquiry.)

## Step 3 — Nathan / Edward: the Meta plumbing (can run in parallel)

Nothing below sends anything until this exists. Order matters:

1. Nathan's Meta portfolio → **Business settings → Accounts → Ad accounts** → Sabre's ad
   account → **Assign partner** → BBL's portfolio ID, with **Manage campaigns**. (Edward is in
   the portfolio already; the ad account is not assigned to him.)
2. **Business settings → Data sources → Datasets** — if Sabre has none: **Add → Create a new
   dataset**, name `Sabre website`. Same portfolio as the ad account. Assign BBL as partner
   on the dataset too (**Manage dataset**).
3. **Events Manager → the dataset → Settings → Conversions API → Generate access token**
   (needs a system user — Meta walks through creating one). Copy it once. Store it in
   `~/.keys/sabre-meta-capi.token` on Edward's machine. **Never in the repo, never in chat.**
4. Note the **Dataset ID** (Events Manager → the dataset → Settings, top).
5. Business verification on Sabre's portfolio (Security Centre) — not blocking, but Meta
   trusts server events more once it is done.

Record ids in BBL `docs/registry/brands.json` → SAB row (`meta_ad_account_id`, plus a new
`meta_dataset_id` key) the day they exist.

## Step 4 — Edward: the custom function (once) and Flow 1's Meta step

1. Zoho Flow → **Settings → Custom Functions → Create Custom Function**.
   - **Function Name:** `meta_capi_event`
   - **Return Type:** `string`
   - **Input Parameters** (all `string`, this order): `event_name`, `event_id`, `mobile`,
     `email`, `fbclid`, `event_source_url`, `dataset_id`, `access_token`, `test_event_code`
2. **Create**, paste the code from `tools/flow/meta_capi_event.dg`, **Save**. Then **Execute**
   once with dummy data so Flow registers the output (skill gotcha 3).
   ⚠️ Return type and parameters cannot be changed after creation — recreate if wrong.
3. Back in Flow 1, add after "Create row": **Logic → Custom Functions → meta_capi_event**:
   - `event_name` = `Lead`
   - `event_id` = `${webhookTrigger.payload.submitted_at}` + the email (any string unique per
     submission; the Sheet row id is better once step 6's `row_id` exists)
   - `mobile` / `email` / `fbclid` / `event_source_url` (← `landing_page`) from the trigger
   - `dataset_id`, `access_token`: pasted values (Flow has no secret store; the Flow is
     private to the BBL account)
   - `test_event_code`: the code shown in **Events Manager → Test events** while testing;
     **blank** once live
4. Add **Zoho Sheet → Update row** after it: set `meta_lead_sent` = the function's output
   (it returns `sent <events_received>` or `error <message>`). A blank cell = never attempted.

### Pixel conditioning — do NOT skip (campaign plan §9)

Only send `Lead` when the answers are worth a lead. Put a **Decision** before the function:
`describes` ≠ `Just researching` **AND** `suburb` ≠ `Somewhere else`. Everything else still goes
to the Sheet and to email; it just isn't reported to Meta as a lead, or Meta will go and find
thousands more like it.

### Proof for step 4

- [ ] With `test_event_code` set, submit a test on the live preview → **Events Manager → Test
      events** shows a `Lead` from `website` within a minute, with `fbc` matched. Cell
      `meta_lead_sent` reads `sent 1`.
- [ ] Clear `test_event_code`. Now live.

## Step 5 — Edward: Flow 2 "Sabre lead won → Meta"

1. **Create Flow**: `Sabre lead won → Meta`.
2. Trigger: **Zoho Sheet → Row updated in a column**. Spreadsheet `Sabre — Lead Ledger`,
   worksheet `Leads`, column `outcome`.
3. **Decision**: `outcome` equals `Won` AND `meta_won_sent` is empty.
4. **meta_capi_event** with `event_name` = `Purchase`, `event_id` = `won-` + the same id used in
   Flow 1, the row's `mobile`, `email`, `fbclid`, `landing_page`, the dataset id and token.
   (Meta's Conversion Leads optimisation reads later-stage events; `Purchase` is the plain
   "this one bought" signal. If Edward later switches the campaign to the *Conversion Leads*
   objective, rename the event to what that setup asks for — one string in one place.)
5. **Zoho Sheet → Update row**: `meta_won_sent` = the function output, `outcome_date` = today
   if empty.

### Proof for step 5

- [ ] Set a test row's `outcome` to `Won` (with `test_event_code` back on) → Test events shows
      `Purchase`; `meta_won_sent` fills. Set it back to `New`; nothing fires twice
      (`meta_won_sent` guard).

## Step 6 — weekly

- Share the Sheet with Nathan: **Share → anyone with the link can edit** is the low-friction
  option (no Zoho login). Send the link once; remind him weekly to fill `outcome`.
- Monday: the Sheet's new rows are the `leads` count per `utm_content` for the registry's
  weekly results row (`/bbl-asset-code` → weekly results). No CPL on a zero-lead week.

## What can go wrong

| Symptom | Cause | Fix |
|---|---|---|
| Row appears with everything in one cell | Trigger format set to JSON | Set the Webhook trigger to **form data**; re-test with the sample |
| No row, no error | `FLOW_URL` blank or wrong on the page | View source of the live page → `js/enquiry.js` top |
| Row appears, Formspree email doesn't | Nothing to do with the Flow — the site's POST failed | The page shows the red "That didn't send" line; check Formspree's dashboard |
| Meta says `Invalid parameter` on `fbc` | `fbclid` empty (organic visit) | Expected: the function omits `fbc` when there is no click id; match is on hashed phone/email |
| Meta 190 error | Token expired/revoked | Regenerate in Events Manager; paste into both Flows |
| Function output not in the variable panel | Return type or no params | Skill gotchas 1–3: recreate the function |
