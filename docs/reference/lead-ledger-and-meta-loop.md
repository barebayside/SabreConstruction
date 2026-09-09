# Lead ledger + Meta closed loop

> **Layer 4.** Agreed 2026-09-09 (Edward, in chat). Why the form feeds a Zoho Flow, what the
> ledger is for, and how the "won / lost" answer gets back to Meta. Code change lives in
> `js/qualify.js`; this file explains the shape. Nothing here is built yet.

## Why

Sabre is a BBL client and must **never** be connected to BBL's CRM (BBL `docs/LAUNCH-LIST.md`).
Today the form posts to a free email relay (`formsubmit.co`, one line in `js/qualify.js`) and the
lead dies in Edward's Gmail. Two things are missing:

1. **A record.** Nobody can say what happened to a lead. Edward wants to go back to Nathan with a
   list and ask *won / lost / moving forward* — transparency for both sides.
2. **Feedback to Meta.** Meta only learns what the browser tells it. A server-side Lead event on
   submit, and a later Won event from the ledger, teach Meta's optimiser who actually buys.

## The shape

```
qualify.js ──POST──▶ Zoho Flow webhook (BBL's Zoho One)
                        │
                        ├─▶ Zoho Sheet "Sabre — Lead Ledger"   (one row per submit)
                        ├─▶ email to Edward (as today; later Nathan)
                        └─▶ Meta Conversions API — event "Lead"  → SABRE's dataset
                                                                    (fbclid + hashed mobile)

Nathan / Edward set Outcome = Won  in the Sheet
                        │
                        └─▶ Flow 2 (Sheet row updated) ─▶ Meta CAPI — event "Purchase" → Sabre's dataset
```

Two Flows, one Sheet. The relay can stay as a belt-and-braces email (`_webhook` field) or the
form can post to Flow directly — same pattern as BBL's snapshot form (plain-text body, no CORS
preflight; see BBL memory `catalyst-answers-cors-preflight-itself`).

## Ledger columns (Zoho Sheet, shared with Nathan by link)

| Column | Source |
|---|---|
| submitted_at | Flow |
| project_type · has_plans · suburb · budget · mobile | form |
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

1. Edward: create the Zoho Sheet + Flow 1 (webhook trigger → Sheet row → email). Copy the webhook URL.
2. Claude: add the URL to `js/qualify.js` (or `_webhook` on the relay), deploy, submit a test, **read
   the Sheet row back**.
3. Edward → Nathan: partner access must include the **dataset**; create one if none exists.
4. Claude: write the CAPI custom function; Edward pastes it into Flow 1 and Flow 2.
5. Test event → Meta Events Manager → Test Events tab shows it. Then live.
6. Weekly: Edward sends Nathan the Sheet link; Nathan fills `outcome`.
