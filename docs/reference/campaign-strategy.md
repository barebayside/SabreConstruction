# Campaign strategy — Sabre Constructions, knockdown rebuild, Bayside

> **Layer 4. Canonical for the campaign from 2026-09-10.** It sits on top of the 3 September
> campaign plan (`docs/sessions/design-plan-knockdown-rebuild.html` — avatar, voice of customer,
> the three figures, KPIs) and brings it into line with what has happened since: the 09-05
> competitor report, the 09-08 positioning (`positioning.md`), the BBL registry rule
> (`bbl-links.md` § registry) and the lead ledger (`lead-ledger-and-meta-loop.md`). Where this
> file and the 09-03 plan differ, **this file wins.** Where this file and `positioning.md` or
> `copy-rules.md` differ, **they win** — this is structure, they are the message.
>
> Method sources, opened for this: `BBL/docs/reference/paid-ads-playbook.md` + its critique
> (the critique matters: "just run one platform" and "stat-sig is for cowards" are wrong at this
> budget), `BBL/docs/THE-CAMPAIGN-SYSTEM.md` §3.4 (the eight gates), the `paid-ads` skill.

## 0 · Status — what this can and cannot do yet

**Nothing runs until Nathan supplies two numbers and five confirmations.** Everything below is
built so that the day they land, the campaigns can be created in an afternoon.

| Owed by Nathan | Why it blocks |
|---|---|
| **What one build is worth to Sabre, roughly** | Every target in §8 is a fraction of it. Without it no CPL can be judged |
| **The monthly ad budget** (Sabre pays Google and Meta direct; excluded from the barter) | §7 phases are a proposal until he says yes |
| Nathan walks the house; on call start to finish; how many homes at a time; the architect path; which QBCC number | The claims in every ad and on every page (`positioning.md` § claims) |

**Access still open (Edward):** Google Ads manager link (customer ID → link → Nathan accepts);
Sabre's Meta ad account assigned to BBL; a Meta dataset + token (`docs/tasks/lead-ledger-build.md`
step 3). **Site:** noindex on github.io until DNS cutover. Ads do not run to a `github.io`
address — see §10.

## 1 · The job of each channel

The 09-03 plan's split stands, sharpened by the report:

| | Google Search | Meta (Facebook + Instagram) |
|---|---|---|
| Job | Catch the family that has already typed the question | Put the third door in front of the family that hasn't |
| The searcher/scroller | "knockdown rebuild builders wynnum", "can I demolish my house brisbane" | Owns a 1950s–80s house in the six suburbs, kids at the local school |
| What the report found | **Sabre is absent from all 13 searches and all 5 map boxes.** Fiteni's Google ads are house-and-land estates; Blueneer's are roof-and-gutter ads. **Nobody is buying the Wynnum/Manly rebuild search.** | **Only Tide and Fiteni advertise the rebuild on Meta.** Tide already runs the "love your street, outgrown the house" line |
| Conversion | A walk-through request (the form) or a call | Same, plus the retargeting pool |
| Starts | Month 1 — text ads, nothing to film | Month 2 — when there is real creative to run |

The site does the convincing; the ad buys the visit. That is why the front door is the
**walk-through with Nathan** (positioning), and the **block check** is the second door on the
contact page for people who arrive already thinking about a rebuild.

## 2 · What changed since the 3 September plan

| 09-03 said | Now | Why |
|---|---|---|
| Entry offer = the free block check, everywhere | **Front door = "Book a walk-through with Nathan."** Block check stays on the contact page and in the Google "Can I" group | `positioning.md`, Edward 09-08 |
| Stewart walks the block | **Nathan** walks the house | positioning; needs Nathan's confirmation |
| Angle 1 "You're not moving / you picked the street" is the cold open | Still the truth, but **Tide runs that exact line on Meta today**. Sabre's cold open carries the one thing Tide can't say: *the builder who walked your old house answers the phone to the day you get the keys* | report 09-05 |
| "Sabre sells the postcode" | Sabre sells **staying, with a builder who stays with you.** The postcode is the setting, the family is the subject (`copy-rules.md`, the LJ Hooker lawn) | 09-08 |
| Tracking = GA4 + a Google Sheet by hand | **The lead ledger** (Zoho Sheet via Flow) + Meta Conversions API, with every ad's code in `utm_content`. Weekly numbers go on the BBL registry record | 09-09, 09-10 |
| Header phone = the 07 office line | **Nathan's mobile everywhere.** Call tracking is now a decision, not a default (§6) | client-facts 09-08 |
| Cost group on Google "blocked until Sabre confirms real numbers" | Still blocked. Same for any "12–18 months" line — those are other builders' numbers | rule 1 |

Angles 3 and 6 (real footage) and the filming brief (plan §14) are unchanged and still gated.

## 3 · Message architecture — one spine, six doors

**The spine** (every ad, every page): *Same street. Same school. A whole new house. Nathan walks
your old house with you, an architect Sabre works with draws the new one around your family, Sabre
builds it — and the builder who walked your house is the one on the phone until he hands you the
keys. Since 1990.*

The doors, re-cut. Build state: 🟢 can run now · 🟠 needs creative, nothing blocks it · 🔴 gated.

| # | Door | Hook (draft — judge against the LJ Hooker lawn) | Runs | State |
|---|---|---|---|---|
| 1 | **They stay with you** (the difference) | "The builder who walks your old house is the one who answers the phone the day you get the keys." | Meta cold, Google "Who" | 🟠 needs Nathan on camera *or* his words over real photos. Blocked on the "on call" confirmation |
| 2 | **Same street, same school** (the loss frame, Sabre's voice not Tide's) | "You picked this street. Don't let the house decide you have to leave it." (already the H1) | Meta cold | 🟠 real Wynnum/Manly street footage, phone is fine; no hero house |
| 3 | **Can we even knock it down?** (the block check) | "Some houses in Wynnum can't legally be knocked down. Do you know if yours is one?" | Google "Can I", Meta feed | 🟢 screen-record of the council mapping tool → contact page / the blog post |
| 4 | **Thirty-six years on the same bay** (authority) | "Building on this bay since 1990." + a cleared review line | Google "Who", Meta warm | 🟢 1990 ✓, 4.5 from 12 ✓, reviews ✓. **QBCC number OFF until Nathan says which** |
| 5 | **Where do we live for the build?** (the objection as the hook) | "Nobody tells you where you'll live while they build it. We do — before you sign." | Meta warm; the blog answers it regardless | 🔴 needs Sabre's own timeline, not the RESEARCH 12–18 months |
| 6 | **The renovation that became a rebuild** / **the last day of the old house** | (plan §4 angles 3 and 6) | Meta retargeting | 🔴 first filmed build |

Two voices only: **Nathan's** (real, on his phone, unscripted) and **words on real Sabre photos**.
A HeyGen presenter is allowed for volume (`sabre-constructions-project` memory) as long as it is
plainly a presenter — never implied staff, never "I" as Sabre — and the AI-disclosure box is
ticked. No generated "after" house, ever (rule 5 / open item 6).

## 4 · Google Ads — the structure, with the codes

Four campaigns, own budgets so none can eat the others. **The ad group name is the asset code**
(registry rule); the campaign name in Google is `sab-knockdown-rebuild-2026`. Phrase + exact
match only. Location = **Presence** (people in or regularly in), the nineteen suburbs listed in the
plan §7.2, not a radius. Auto-tagging **ON** (gate G6). Every final URL carries
`?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content={_code}`
with `_code` set as a custom parameter on each ad group.

| Campaign · share | Ad group = code (proposed — scaffold with `/bbl-asset-code` when the budget is agreed) | Keywords (phrase / exact) | Lands on |
|---|---|---|---|
| **1 · Knockdown Rebuild** · 45% | `SAB-SOL-KDR-2.0A_GOOGLE_SEARCH` KDR generic | knockdown rebuild brisbane · knock down rebuild bayside · demolish and rebuild same block | home |
| | `SAB-SOL-KDR-3.0A_GOOGLE_SEARCH` KDR Wynnum | knockdown rebuild wynnum · rebuild wynnum · builders wynnum knockdown | `/wynnum/` |
| | `SAB-SOL-KDR-4.0A_GOOGLE_SEARCH` KDR Manly | knockdown rebuild manly · … manly west · … lota | `/manly/` |
| **2 · Local Builder** · 30% | `SAB-SOL-KDR-5.0A_GOOGLE_SEARCH` builders + suburb | builders wynnum · home builders manly qld · builders capalaba · new home builders redlands | `/wynnum/` or `/manly/` by term; else home |
| | `SAB-SOL-KDR-6.0A_GOOGLE_SEARCH` custom home builder bayside | custom home builders brisbane bayside · custom home builder redlands | home |
| **3 · Can I knock it down** · 15% | `SAB-CON-KDR-5.0A_GOOGLE_SEARCH` character overlay | character overlay brisbane · pre 1947 house demolish · can i demolish my house brisbane · traditional building character overlay | the blog post `/blog/can-we-knock-down-our-house/` (its close is the contact form) |
| **4 · Brand protect** · 10% | `SAB-SOL-KDR-7.0A_GOOGLE_SEARCH` brand | sabre constructions · sabre constructions capalaba · sabre builders | home |

Ad copy per group: the headline is the page's headline (congruence). Responsive search ads:
pin **H1 = the searched thing + suburb**, H2 = "Since 1990", H3 = "Book a walk-through with
Nathan"; descriptions from the spine. Assets: call asset (Nathan's mobile — Google tracks these
calls itself), sitelinks (Your design · Meet the team · Testimonials · Can we knock it down),
callouts (Family owned since 1990 · Bayside and Redlands only · Master Builders member).
**No price, no timeline, no job count** in any asset (rule 1).

**Negatives on day one** (plan §7.2 list, unchanged): jobs, careers, apprentice, salary, course,
diy, how to, free, cheap, kit home, granny flat, shed, carport, deck, pergola, demolition
contractor, asbestos, excavation, commercial, townhouse, developer, sydney, melbourne, gold coast,
sunshine coast, nsw, victoria. Read the search-terms report weekly for the first month.

**Conversion actions** (before the first click): form success (the page's green "Thanks" state —
`js/enquiry.js` fires the Google tag there once the tag exists), calls from ads (call asset),
and a soft one for `tel:` taps on the site. **The Google tag is not on the site yet**; it goes in
the day the account is linked (needs the conversion ID).

## 5 · Meta — the structure, with the codes

One campaign, `sab-knockdown-rebuild-2026`, **Leads** objective, conversion location =
website, event = `Lead` (the CAPI event from the ledger, qualified rows only — plan §9 "pixel
conditioning"). Until the dataset exists, run **Traffic → landing page views** and switch when it
does. Three ad sets, **ad-set budgets (ABO)**, ages 30–60, the suburb list, Advantage+ audience
off for the cold set at this budget (the critique: broad is right *once the pixel is trained*).

| Ad set · share | Who | Doors | Ads = codes (the **ad name** is the code) |
|---|---|---|---|
| **A · Cold** · 60% | Six suburbs, 30–60 | 1, 2, 3 | `SAB-AWR-KDR-7.0A_META_VIDEO` (door 1, Nathan) · `SAB-AWR-KDR-8.0A_META_VIDEO` (door 2, the street) · `SAB-AWR-KDR-9.0A_META_VIDEO` (door 3, the mapping tool) · image variants `…_META_IMAGE` on the same sequence numbers as `.0B` |
| **B · Warm** · 25% | Watched 10 s+ of any Sabre video, or engaged the Page/IG, 365 d | 4, 5 | `SAB-CON-KDR-6.0A_META_VIDEO` (since 1990 + a review) · `SAB-CON-KDR-7.0A_META_IMAGE` (the review card, Roselia's line) |
| **C · Retargeting** · 15% | Site visitors 180 d; started the form and did not finish | 6, reviews | `SAB-SOL-KDR-8.0A_META_VIDEO` (gated on footage) · `SAB-SOL-KDR-9.0A_META_IMAGE` (Google rating + three reviews, the contact page's close) |

Start with **6–8 distinct creatives** across A and B, add rather than replace (the critique on
"12 minimum"). Every link: `?utm_source=meta&utm_medium=paid&utm_campaign=sab-knockdown-rebuild-2026&utm_content=<code>`.

**Settings to change from Meta's defaults** (plan §7.3): Audience Network **off**; every
"Advantage+ creative" enhancement **off** and re-checked monthly (they rewrite a builder's claims);
frequency guardrail — cold above 2.0 = pull the budget back; AI-disclosure box on anything
generated or altered.

**Creative production** (`media-pipeline.md`; Sabre's fal key only): door 3 is a screen
recording; door 2 is a phone on a Wynnum footpath at 8 am; door 1 is **Nathan, phone, 20 seconds,
unscripted** ("what happens when a family rings you?") — one ask, one afternoon, and it is the
single most valuable piece of creative before the filmed build exists. HeyGen presenter versions
only as volume behind those, on the older (cheaper) avatar model.

## 6 · Measurement — the chain, and what fires where

```
ad (name = code) ─▶ link (utm_content = code) ─▶ page ─▶ form
                                                          ├─▶ Formspree → Nathan's inbox     (unchanged)
                                                          ├─▶ Zoho Flow → Lead Ledger (Sheet) → Meta CAPI "Lead" (qualified only)
                                                          │        └─ Nathan sets outcome = Won ─▶ CAPI "Purchase"
                                                          └─▶ Google tag "form success"        (when the account is linked)
Monday: Ads Manager · Google Ads · Search Console · the Sheet ─▶ results[] on each SAB record ─▶ _regen.py ─▶ results.csv
```

- **Built 2026-09-10:** capture + hidden fields + the ledger copy on every page and both forms
  (`js/enquiry.js`); the build guide for the Sheet, the two Flows and the CAPI function
  (`docs/tasks/lead-ledger-build.md`, `tools/flow/meta_capi_event.dg`).
- **Not built:** the Flows themselves (Edward, ~1 hour), the Meta dataset (Nathan), the Google tag.
- **Calls.** A builder gets phoned. Google's call assets are tracked by Google without touching
  the site. On the site, the mobile is Nathan's real number; swapping it for a tracking number
  is a decision for Nathan (it changes what customers see and save). Recommendation: **leave
  the real number on the site, count `tel:` taps as a soft conversion, track calls from ads via
  call assets.** Revisit if the ledger shows enquiries arriving by phone that the form never sees.
- **The five-tests verdict** goes on every weekly row (`Notice / Fit / Proof / Effort / Now`), from
  `BBL/playbook/foundations.md` Layer 6. That is how the method learns across clients.

## 7 · Budget phases — a proposal until Nathan agrees

Unchanged from the plan §7.4; roughly $30–50 a day. **Sabre pays the platforms directly.**

| Month | Google | Meta | What it is for |
|---|---|---|---|
| 1 | campaigns 1, 2, 4 | — | Find which searches convert. Text only, nothing to film |
| 2 | + campaign 3 | ad set A | Meta tests cold with whatever real creative exists |
| 3 | as 2 | + ad sets B, C | Retargeting turns on once there is traffic to retarget |

Minimum **7 days or $1,000** before an opinion on anything. Weekly: write the numbers down, add
negatives, change nothing else. Monthly: kill the worst, back the best, start **one** new test.

## 8 · Targets — the chain

From the plan §10 (benchmarks, not Sabre's numbers). Fix the earliest weak number first.

| Step | Target | If under, it's the… |
|---|---|---|
| Link CTR | 1–2% | message — change the door, not the audience |
| Form completion | 5–10% | page — headline, form position, friction |
| **Cost per qualified enquiry** | set in month 1; judged against the value of a build | hook — filter upstream in the copy |
| Enquiry → walk-through booked | count | reply speed; then whether the answer was useful |
| Hours to first reply | < 24 | Nathan — the only number fully in his control |

## 9 · Search and AI visibility — in scope since 09-08, and mostly free

> **Superseded 2026-09-10 by `search-and-ai-visibility-plan.md`** — the full plan (listing, pages,
> mentions, measurement, the article bank, the technical appendices). The list below is the short form.

The report's baseline: absent from all 13 searches, all 5 map boxes, and no AI assistant names
any builder for "best knockdown rebuild builder in Wynnum". In order of payoff per hour:

1. **Google Business Profile** — get manager access (run-sheet leftover). Primary category
   *Home builder*, secondary *Custom home builder*; service area = the nineteen suburbs; the
   website link to the new site after cutover; a review link Nathan can text to a family at
   handover (the only review generation in scope).
2. **DNS cutover + strip `noindex`** — nothing indexes until then. Sitemap already lists 11 URLs.
3. **The suburb pages** (`/wynnum/`, `/manly/`) and the explainer post are the organic lane
   nobody else is in. Add `LocalBusiness` (HomeAndConstructionBusiness) schema with the address,
   the phone, `areaServed` = the suburbs, `foundingDate` 1990 — facts only.
4. **The AI-answer test** from the report (Wynnum/Manly rebuild questions) — re-run monthly.
   What an assistant needs to name Sabre: the plain-words explainer, the suburb pages, the
   Master Builders / QBCC facts stated in text, and the Google listing agreeing with the site.
5. Later: a post per real build (the filmed ones), which is also the Meta creative.

## 10 · Gates — nothing goes live until every row is true

| # | Gate | State 2026-09-10 |
|---|---|---|
| 1 | Nathan's two numbers (build value, monthly budget) | ⛔ owed |
| 2 | Nathan's five confirmations (`positioning.md`) — the claims in every ad | ⛔ owed |
| 3 | Google Ads linked to BBL's manager (customer ID → link → accepted) | ⛔ never completed |
| 4 | Sabre's Meta ad account assigned to BBL; dataset + token | ⛔ not assigned; no dataset |
| 5 | Site on `sabreconstructions.com.au`, `noindex` gone (ads never land on github.io) | ⛔ Melbourne IT / iSonic unanswered since 08-24 |
| 6 | One REAL test enquiry from the live site lands in admin@ (rule 4) | ⛔ owed (Edward) |
| 7 | The ledger proven: row appears **and** Formspree still arrives; Flow off = email still arrives | ⛔ Flows not built |
| 8 | Every ad has a registry code **before** it is made; ad name = code; `utm_content` = code | ✅ system exists; codes above are proposed |
| 9 | AI testimonial placeholders gone from the home page (they are labelled and served from the demo; a live commercial site cannot carry them) | ⛔ decision + real footage |
| 10 | Meta enhancements off, Audience Network off, negatives loaded, conversion actions verified | not started |

## 11 · The first afternoon of building (when gates 1–5 clear)

1. `/bbl-asset-code` → scaffold the seven Google ad-group codes and the first four Meta ad codes
   from §4–5 (Draft).
2. Google: four campaigns as §4, negatives, call asset, conversion actions; the tag into
   `js/enquiry.js`; **one** `?gclid=TEST` submission read back in the Sheet.
3. Nathan's 20-second clip (door 1) + the mapping-tool screen recording (door 3) + the street
   clip (door 2) → cut to 9:16 and 1:1, captions burned in, AI-disclosure where relevant.
4. Meta: one campaign, ad set A only, three ads named with their codes.
5. Monday after: the first weekly rows on the records. Then hold for three weeks.
