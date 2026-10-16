# Sabre Constructions — next

Updated 2026-10-16 · Source: handoffs 09-30, 09-30b, 10-12 + `docs/engagement.md` (full state and history live there)

## Goal
- **Serves:** Branch 2, the engine. A BBL client and test bench; its results become an anonymised case study. The Family Plan: `dev-studio/FAMILY-PLAN.md`.
- **Purpose:** A BBL client paid in kind: win building leads for Sabre through the website, Meta ads and Google ads.
- **Success looks like:** Real enquiries from the ads and site, tracked to the source. It also becomes a BBL case study (without naming Sabre in BBL content).
- **Target:** ❓ Edward to set (a number and a date)

## Next

1. **Google Ads: get the business check through.** Nathan's ASIC certificate was asked for by
   16 Oct. When it arrives, confirm which company trades. It must match the Google Ads payments
   profile and the unsigned agreement. Then get Nathan's 10-digit Customer ID and link the account
   to the MCC with `/bbl-google-ads-link` (check the account is active first). Then advertiser
   verification. Plan: `docs/reference/campaign-strategy.md`.
2. **Knockdown video: finish it.** When the videographer's no-music version arrives, swap it in for
   the silent stand-in, re-time the captions and push. Nathan's "I'm the owner" line must be
   confirmed (`client-facts.md` says the owners are Stewart and Cathy) or cut before this video goes
   on the real domain. Footage inbox: `docs/reference/asset-storage.md`.
3. **Build the ad variant tool** for 3–4 versions of the knockdown ad: one Sabre end card per variant,
   facts from `client-facts.md` (not the old phone and QBCC numbers in the testimonial script).
   Register each code with `/bbl-asset-code` first.
4. **Website work waits on Nathan's voice-note answers** (`docs/nathan-voice-note-questions.md`). When
   they land: the held pages, the `/wynnum/` and `/manly/` rewrites, the contract type and the four
   operating claims (`docs/reference/article-bank.md`, `docs/open-items.md`).
5. **Cut over to the real domain.** Point DNS at the new site, take off `noindex` and the preview
   chrome, then run the Search Console and Bing routine. Needs the domain login (`docs/tasks/dns-cutover.md`).
6. **Fix the Google Business Profile address** (still Capalaba, should be Ransome). Needs Nathan's login.

## Waiting on Edward

- Send the drafted email to Nathan asking for the ASIC certificate (text in the 10-12 handoff), if it hasn't gone, and log the send in `docs/engagement.md`.
- Get the no-music knockdown version from the videographer.
- Launch the 3 PageSense heatmaps (filter to Draft, click Launch on each), then tap the phone number on the preview over mobile data to prove the goal fires.
- The Zoho draft to Nathan (HeyGen part): send it or delete it.
- Still to ask Nathan: Google Business Profile login, who holds the domain (iSonic or Melbourne IT), Leanne's consent for paid ads.
- Lead ledger: build the Zoho Sheet and Flow 1, and send the webhook URL (`docs/tasks/lead-ledger-build.md`).

## Parked

- **Lead ledger, the rest:** paste `FLOW_URL`, push, the test row, and the Meta dataset in Sabre's
  portfolio. Waits on the webhook URL above.
- **Google Drive for desktop** with a shortcut to Nathan's "Ed" folder, so footage reads from disk. Offered, not installed.
- **Watch Nathan's 15 GB Drive quota** once raw 4K starts arriving.
- **Put the in-kind deal in writing** (what "at cost" covers, the deck, scope growth) and sign the agreement. In `docs/engagement.md`; no date set.
- **PageSense scroll depth**, once the heatmaps have visits after the cutover.
