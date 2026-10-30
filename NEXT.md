# Sabre Constructions — next

Updated 2026-10-20 · Source: handoffs 09-30, 09-30b, 10-12 + `docs/engagement.md` (full state and history live there)

## Goal
- **Serves:** Goal 1, through the **business engine**. A BBL client paid in kind; its results become an anonymised case study. The Family Plan: `dev-studio/FAMILY-PLAN.md`.
- **Purpose:** A BBL client paid in kind: win building leads for Sabre through the website, Meta ads and Google ads.
- **Success looks like:** Real enquiries from the ads and site, tracked to the source. It also becomes a BBL case study (without naming Sabre in BBL content).
- **Target:** ❓ Edward to set (a number and a date)

## Next

⭐⭐ **THE PLAN agreed with Nathan, 2026-10-30.** Budget **~A$1,000/month across Meta + Google** (Sabre pays both direct).
In order:
1. **Nathan is getting the logins** (agreed with him in person 2026-10-30): iSonic (DNS + hosting) and the Microsoft 365
   admin. Then Edward moves the DNS to a host he manages, copying every record first (email = Microsoft 365, not iSonic;
   keep every MX/TXT/autodiscover record), then cuts the site over (noindex off, preview chrome out, Search Console +
   Bing). `docs/tasks/dns-cutover.md` (its "never move nameservers" rule predates this plan; update it at the move).
   Every ad waits on this.
2. **Quick photos + videos once the site is up** (Nathan loads them into his Google Drive "Ed " folder, which we can
   read) → turn them into Meta ads. Starting set already drafted: 5 image ads + the knockdown video with new music
   (`marketing/research/2026-10-30-builder-ad-swipe/sabre-mockups/`; swipe of 54 long-running builder ads beside it).
3. **Edward shows Nathan the Meta ads for approval** before anything runs. Register codes with `/bbl-asset-code` first.
4. **Google Ads campaign** (`marketing/google-ads/general-campaign.md`): ✅ **BUILT PAUSED 2026-10-30** in 240-650-1798:
   `sab-knockdown-rebuild-2026` (campaign id 24407491653), A$25/day, Maximise clicks, Search only, 8 ad groups,
   354 keywords, 8 RSAs, 183 negatives (157 campaign + 26 ad group), 12 suburbs + postcode 4179 (Manly isn't a
   Google location), Presence only, AI Max / auto assets / broad match OFF, EU political ads = No (no red block this
   time). Bulk file: `marketing/google-ads/editor/sabre-bulk-upload-no-negatives.csv` (web bulk upload rejects
   'Negative Phrase' rows; adding an ad-group negative silently removes the same word at campaign level, so re-add it).
   Still to add: sitelinks / callouts / snippets / call asset, Keyword Planner check. On after the gates.
   **Conversions = the goal (Edward 10-30).** Three Google Ads conversion actions, all Primary: (1) enquiry form sent
   (fire beside the Meta `Lead` in `js/enquiry.js`, after Formspree accepts), (2) tap on the phone number on the site
   (`tel:` link click), (3) calls from the ad's call button (needs Nathan's hours). Google tag on all 64 pages. Can be
   built before DNS; prove each one fires on the real domain before switching on.
   ✅ **10-30 DONE (1)+(2):** tag `AW-18431104209` on all 64 pages (site commit `e81917f`, enquiry.js v=4).
   "Sabre - Enquiry form sent" (label `PViaCLXh2a4dENGp0dRE`) + "Sabre - Phone tap on website" (`p25lCLjh2a4dENGp0dRE`),
   both Primary, count One. Phone tap proven on the preview site (googleadservices 200). Form one NOT yet proven: needs the
   real test enquiry. Enhanced conversions left OFF until a privacy page. (3) waits on the call asset + Nathan's hours. Bidding: Maximise clicks first, then
   Maximise conversions once ~15–30 conversions are in. Nathan still to give: call hours, renovations/extensions in or out, OK on the ad claims.
   Skip Google's "A$1.2K credit if you spend A$600 by 4 Nov" offer: the gates won't be met by then.
5. **Metricool:** Edward sets up Sabre in Metricool and asks Nathan whether BBL posts for him (organic,
   `/organic-posts sabre`). Note: the BBL rule had client pages staying in the client's own accounts.
6. **Meta Conversions API:** Edward was clicking "Set up with Meta" (Meta-hosted, one click) on 10-30; confirm it's on.
   Turn it off when the lead-ledger Flow route sends leads to Meta itself (avoid double counting).

**Access, all DONE 2026-10-30:** Google Ads `240-650-1798` linked under the BBL MCC (accepted by Nathan's Google login;
Owner: Yes not seen from our side). Meta: ad account `2340740500090945` created by Nathan in Sabre's portfolio, Edward
full access, payment on; Page `1216840691766822` + Instagram `17841448162632602` full access; ad account connected to
the Instagram profile. Dataset `4588724778070847` ("Sabre Constructions website") created; pixel on all 64 pages +
Lead on the form's success (site commit `a288b82`). Automatic Advanced Matching left OFF until the site has a privacy
page. All IDs in BBL `docs/registry/brands.json` SAB. Edward's portfolio role is still Partial (fine: assets are Full).

0. ✅ **Nathan visit 2026-10-30, done (see the plan above).** Was: List: `docs/sessions/2026-10-30-nathan-visit-checklist.md`
   (Google Ads link + verification, Meta ad account, Metricool, domain + DNS, Bigin, the offer's numbers, his
   claims). Then finish the offer (`marketing/pushes/2026-10-29-2027-build-slots/03-offer.md`) and go to step 04.
   Marketing plan: `marketing/plan.md` (customer = young families who already own an older house).
   **Also: record a couple of Nathan talking-to-camera takes for later ads.** OBS collection `Sabre Constructions` is
   built (10-30): Ctrl+Alt+7 = his real room, softly blurred; Ctrl+Alt+1 = cut out over a real Sabre home
   (`obs_setup.py backdrop --pick kitchen|living|front|brighton`); Ctrl+Alt+R records. Nathan stands or sits on a
   stool (a chair back stays sharp). Plug in the Yeti and make it the Windows default mic first.
   How: `docs/reference/video-profile.md` → Look.
   **10-30: recorded.** 13½ min on green (OBS scene "Me key"): 5 script lines + 10 answers to Edward's questions.
   Cut into 15 clips, filed on WorkDrive `VIDEO\2026-10-30 — Nathan to camera\` (`review.html` there to
   Keep/Trim/Cut; `README.txt` lists the claims to confirm: years 20 vs 30 vs 1990, Gumdale vs Ransome, "90%").
   Set aside for now; maybe show Nathan.

0a. **Turn Nathan's takes into proper ads (Edward's idea 10-30).** Nathan talking, with cutaways to real Sabre
   builds, action footage and photos behind or between him, in place of the soft house backdrop. Work out the process
   from BBL `docs/pipelines/video-production/ad-build-process.md` + the video engine. Needs: which clips to keep
   (review.html), the claims confirmed, and the build footage/photos to cut to.
   **10-30: two 9:16 drafts made** (WorkDrive `…Nathan to camera\04 ad drafts\`): A "custom = built around you"
   (clip 07 + real Sabre homes), B "knockdown rebuild" (clip 14 + the real excavator footage). Sabre `talk` look added
   to `docs/brand-kit.json`; recipes `marketing/video/talk-recipes/`. Waiting on Edward's view. Then: licence name on
   the end card, asset codes, Nathan's OK.

0b. ⭐ **Google Ads general campaign drafted 2026-10-30, waiting on Edward's sign-off.** Plan + sign-off page
   `marketing/google-ads/general-campaign.md/.html`, Editor import files in `marketing/google-ads/editor/`,
   8 registry records (Draft). Fast track: warm push week of 2 Nov, one-week check ~9 Nov, the 2027 offer from ~16 Nov
   (`marketing/runsheet-with-nathan.html`). Once the account is linked, Claude builds it **paused**, runs Keyword Planner
   first, then turns on only after the gates in the plan.
1. **Google Ads: get the business check through.** **10-21: Nathan sent an ASIC "Company Summary"
   (free database extract), not the Certificate of Registration Google names. Saved (gitignored) at
   `docs/company-docs/sabre-asic-extract.pdf`. Entity = SABRE CONSTRUCTIONS QLD PTY LTD, ACN 673 587 472,
   ABN 29 673 587 472, registered office Yeerongpilly (not Ransome).** Ask for the real certificate as
   well, plus Nathan's photo ID. Confirm which company trades. It must match the Google Ads payments
   profile and the unsigned agreement. Then get Nathan's 10-digit Customer ID and link the account
   to the MCC with `/bbl-google-ads-link` (check the account is active first). Then advertiser
   verification. Plan: `docs/reference/campaign-strategy.md`.
2. **Knockdown video: finish it.** When the videographer's no-music version arrives, swap it in for
   the silent stand-in, re-time the captions and push. Nathan's "I'm the owner" line must be
   confirmed (`client-facts.md` says the owners are Stewart and Cathy) or cut before this video goes
   on the real domain. Footage inbox: `docs/reference/asset-storage.md`.
   **10-20: the no-music version is in Nathan's Drive** ("Video ads" → `04. Knock down - Raw.mov`,
   15 Oct, plus a duplicate "Copy of…"). The Drive connector lists it but can't download video:
   Edward downloads it in Brave.
3. **Build the ad variant tool** for 3–4 versions of the knockdown ad: one Sabre end card per variant,
   facts from `client-facts.md` (not the old phone and QBCC numbers in the testimonial script).
   Register each code with `/bbl-asset-code` first.
4. **Website work waits on Nathan's voice-note answers** (`docs/nathan-voice-note-questions.md`). When
   they land: the held pages, the `/wynnum/` and `/manly/` rewrites, the contract type and the four
   operating claims (`docs/reference/article-bank.md`, `docs/open-items.md`).
5. **Cut over to the real domain.** Point DNS at the new site, take off `noindex` and the preview
   chrome, then run the Search Console and Bing routine. Needs the domain login (`docs/tasks/dns-cutover.md`).
6. **Nathan as a lip-synced presenter (Edward's idea 10-20). Ready tool, on request only.** Route proven on Edward: real raw
   footage + new script in a cloned voice, ~$2 per 15 s (BBL `docs/pipelines/video-production/presenter-lipsync.md`).
   Photo avatars were rejected. Before anything: Nathan's consent recording + written likeness
   release + a raw take (3–4 looks × 20–30 s, calm, on real sites). He approves every script.
   Runs on **Sabre's** fal key. Ask in the same message as the voice note chase.
7. **Fix the Google Business Profile address** (still Capalaba, should be Ransome). Needs Nathan's login.

## Waiting on Edward

- Ask Nathan for the actual ASIC **Certificate of Registration** for Sabre Constructions QLD Pty Ltd (his accountant will have it) + a clear colour photo of his driver's licence. The summary he sent 20 Oct is the fallback.
- Get the no-music knockdown version from the videographer.
- Launch the 3 PageSense heatmaps (filter to Draft, click Launch on each), then tap the phone number on the preview over mobile data to prove the goal fires.
- The Zoho draft to Nathan (HeyGen part): send it or delete it.
- Still to ask Nathan: Google Business Profile login, Leanne's consent for paid ads.
- Lead ledger: build the Zoho Sheet and Flow 1, and send the webhook URL (`docs/tasks/lead-ledger-build.md`).

## Parked

- **Lead ledger, the rest:** paste `FLOW_URL`, push, the test row, and the Meta dataset in Sabre's
  portfolio. Waits on the webhook URL above.
- **Google Drive for desktop** with a shortcut to Nathan's "Ed" folder, so footage reads from disk. Offered, not installed.
- **Watch Nathan's 15 GB Drive quota** once raw 4K starts arriving.
- **Put the in-kind deal in writing** (what "at cost" covers, the deck, scope growth) and sign the agreement. In `docs/engagement.md`; no date set.
- **PageSense scroll depth**, once the heatmaps have visits after the cutover.
