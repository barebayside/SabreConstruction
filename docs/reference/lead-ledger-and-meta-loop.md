# Lead ledger + Meta closed loop

> **Layer 4.** Agreed 2026-09-09 (Edward, in chat). Why the form feeds a Zoho Flow, what the
> ledger is for, and how the "won / lost" answer gets back to Meta. Nothing here is built yet.
>
> ⚠️ **Two repos, two forms.** The LIVE enquiry form is in Sabre's own repo
> (`Desktop\sabre-constructions-website\`, `index.html` + `contact/index.html`): a plain HTML POST
> to Formspree `f/mwlkqyqn`, **no JavaScript, no UTM / fbclid capture at all**. The demo landing
> pages in THIS repo use `js/qualify.js`, which does capture them, via formsubmit.co. The work
> below targets the LIVE repo; `qualify.js` is the reference for the capture code.

## Why

Sabre is a BBL client and must **never** be connected to BBL's CRM (BBL `docs/LAUNCH-LIST.md`).
Today the live form posts to Formspree (free tier, 50/month, no webhooks below the $99 Gold plan)
and emails admin@sabreconstructions.com.au. That works and stays. Two things are missing:

1. **A record.** Nobody can say what happened to a lead. Edward wants to go back to Nathan with a
   list and ask *won / lost / moving forward* — transparency for both sides.
2. **Feedback to Meta.** Meta only learns what the browser tells it. A server-side Lead event on
   submit, and a later Won event from the ledger, teach Meta's optimiser who actually buys.

## The shape

```
live form ──POST──▶ Formspree ──▶ email to Nathan  (unchanged)
    │
    └─ on submit, sendBeacon ──▶ Zoho Flow webhook (BBL's Zoho One)
                                    │
                                    ├─▶ Zoho Sheet "Sabre — Lead Ledger"   (one row per submit)
                                    ├─▶ email copy to Edward
                                    └─▶ Meta Conversions API — event "Lead"  → SABRE's dataset
                                                                    (fbclid + hashed mobile)

Nathan / Edward set Outcome = Won  in the Sheet
                        │
                        └─▶ Flow 2 (Sheet row updated) ─▶ Meta CAPI — event "Purchase" → Sabre's dataset
```

Two Flows, one Sheet. **Formspree keeps doing the email** — it is tested and Nathan already
receives it. A ~30-line inline script is added to both live pages: fill hidden `utm_*`, `fbclid`,
`gclid`, `landing_page`, `referrer` fields from the URL (persist in sessionStorage so a click-through
from another page still carries them — copy from `qualify.js` L182), and on submit fire
`navigator.sendBeacon(FLOW_URL, JSON)` before the normal POST continues. Beacon = text/plain, no CORS
preflight, no change to the user's flow (BBL memory `catalyst-answers-cors-preflight-itself`).
Formspree also receives the hidden fields, so the email carries the asset code too.

## Ledger columns (Zoho Sheet, shared with Nathan by link)

| Column | Source |
|---|---|
| submitted_at | Flow |
| describes · built · suburb · name · phone/email (as on the live form) | form |
| page · landing_page · referrer · fill_seconds | form |
| utm_source · utm_medium · utm_campaign · utm_content · utm_term | form (asset code lives in `utm_content`) |
| fbclid · gclid | form — the Meta / Google matching keys |
| **outcome** | Nathan: `New` / `Contacted` / `Quoting` / `Won` / `Lost` |
| outcome_date · notes | Nathan |
| meta_lead_sent · meta_won_sent | Flow — stamped when the event went to Meta, so a gap is visible |

Zoho Sheet over Excel: it is in Zoho One, Flow has native Sheet actions, and a share link needs
no Microsoft login from Nathan. Bigin is the upgrade if Nathan ever wants a pipeline view.

## What Meta needs before either event can be sent

1. Sabre's **ad account** assigned to Edward (he is in the portfolio; the account is not assigned).
2. A **dataset** in Sabre's portfolio, same portfolio as the ad account. Sabre has none today.
3. A **system-user access token** for that dataset, issued from Sabre's portfolio.
4. Business verification on Sabre's portfolio (Meta trusts server events more once verified).

The Flows can be built and tested against a test dataset before 1–4 exist.

## Event details (for the Flow custom function)

- `event_name`: `Lead` on submit, `Purchase` on Won. `action_source`: `website`.
- `user_data.ph`: mobile → digits only, `61` prefix, SHA-256. `user_data.fbc`: `fb.1.<ms
  timestamp>.<fbclid>`. `event_source_url`: `landing_page`.
- `event_id`: the Sheet row id — lets Meta de-duplicate if a browser pixel is added later.
- Endpoint: `POST https://graph.facebook.com/v21.0/<DATASET_ID>/events?access_token=<TOKEN>`.

## Order of work

> **2026-09-10:** step 2's page work and step 4's function are DONE (`js/enquiry.js` in the live repo;
> `tools/flow/meta_capi_event.dg`). The row goes as **form-encoded data**, not JSON — set the Webhook
> trigger to "form data". Build steps, click by click: `../tasks/lead-ledger-build.md`.

1. Edward: create the Zoho Sheet + Flow 1 (webhook trigger → Sheet row → email). Copy the webhook URL.
2. Claude: hidden fields + capture/beacon script on BOTH live pages (`index.html`, `contact/index.html`
   in the live repo), push, submit a test with `?utm_content=TEST&fbclid=TEST`, **read the Sheet row
   back** and check Nathan's Formspree email still arrives.
3. Edward → Nathan: partner access must include the **dataset**; create one if none exists.
4. Claude: write the CAPI custom function; Edward pastes it into Flow 1 and Flow 2.
5. Test event → Meta Events Manager → Test Events tab shows it. Then live.
6. Weekly: Edward sends Nathan the Sheet link; Nathan fills `outcome`.
