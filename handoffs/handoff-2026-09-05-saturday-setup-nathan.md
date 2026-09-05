# Handoff — 2026-09-05 — Saturday setup with Nathan: real repo, live form, Sabre's fal key, agreement agreed

## Session Focus

Nathan sat with Edward for the run-sheet day. The point was to leave with every account
in Sabre's name and BBL able to work without him. Most of that landed. The real website
now exists in a repo Sabre owns, with a working enquiry form, and the first image made on
Sabre's own fal.ai billing is on it.

## What Got Done

**Agreement**
- Nathan **agreed** to the working agreement. Day-count blanks removed (3.6 and 4.3 now say
  "on the days it is needed", both sides). **Schedule A removed** entirely; clause 4.5 now
  carries a one-sentence summary. No blanks left. PDF re-rendered, 4 pages, for Zoho Sign.
  Not yet sent through Zoho Sign at time of writing.

**GitHub — the real site repo**
- Nathan created the org **`Sabre-Constructions`** and the public repo
  **`sabre-constructions-web-site-`** (trailing hyphen is in the name). Edward pushes as
  `barebayside`. Proof push done in front of him.
- The `site/` skeleton (6 pages, `site.css`, `CLAUDE.md`, `docs/`) was copied in and pushed.
- **GitHub Pages is ON:** https://sabre-constructions.github.io/sabre-constructions-web-site-/
  All pages still carry `noindex`.
- Local clone: `C:\Users\edast\OneDrive\Desktop\sabre-constructions-website\`

**fal.ai — Sabre's own account**
- Nathan created the account and an API key. Stored at `~/.keys/sabre-fal.key`, never in a repo.
- First job on his billing: `recraft/upscale/crisp` on the Killarney 78 thumbnail from the
  old site, 376×251 → 1504×1004. Before/after is on the new home page.

**Formspree — the form finally sends**
- Sabre's account, endpoint `https://formspree.io/f/mwlkqyqn`, notifies
  admin@sabreconstructions.com.au. Test submission returned `ok:true`.
- Contact page rebuilt to the campaign plan §8 design: two radio questions (which best
  describes you / when was the house built), suburb dropdown, name, email, mobile, address
  optional last. Headline "Can we knock it down?". Inline success/failure messages.
- Outlook safe-sender steps given for `formspree.io`.

**Google Ads / Meta**
- Meta access confirmed by Edward. Google Ads "a bit funny" — link not confirmed. Manager
  account + link-request steps documented in chat; nothing verified.

## Files Changed / Created

| Path | What | State |
|---|---|---|
| `Desktop\sabre-constructions-website\` (new repo) | skeleton + form + Killarney upscale | **pushed, live on Pages** |
| `…website\contact\index.html` | live Formspree form, §8 design | pushed |
| `…website\css\site.css` (`?v=2`) | form styles | pushed |
| `…website\index.html` | Killarney 78 before/after section | pushed |
| `…website\assets\img\proj-killarney78.jpg`, `proj2x-killarney78.jpg` | original + upscale | pushed |
| `docs/agreement/*.md`, `*.html` | blanks removed, Schedule A removed | gitignored |
| `docs/agreement/Sabre-BBL-Working-Agreement.pdf` | re-rendered, 4 pages | gitignored |
| `docs/engagement.md`, `docs/open-items.md` | 2026-09-05 status blocks | this repo |
| `~/.keys/sabre-fal.key` | Sabre's fal key | outside any repo |

⚠️ This demo repo was 6 commits ahead of origin at session start and has NOT been pushed.

## Decisions Made

1. **No fixed day counts in the agreement** — both sides work "on the days it is needed". → `docs/agreement/`
2. **Schedule A dropped** from the agreement; the checklist lives in the run sheet instead. → `docs/agreement/`
3. **The real site is `Sabre-Constructions/sabre-constructions-web-site-`.** The 2026-08-24
   fresh-repo decision is now executed. This demo repo stays the workshop. → `docs/engagement.md`
4. **Leads go to Sabre now**, not Edward — the real site's form notifies admin@. The demo
   repo's `qualify.js` still points at Edward and stays that way (demo only). → `docs/open-items.md`
5. **Next process: a BBL competitor-intelligence report on Sabre's competitors** to set the
   SEO and campaign targets before the design build. Edward's call, end of session.

## Resolved failures

**TotalAV quarantined every PDF headless Chrome wrote.**
- *What was broken:* `--print-to-pdf` "succeeded", then the file was unreadable
  (`Permission denied`) and then vanished from the folder.
- *Why:* TotalAV's ransomware shield treats an unattended process writing into
  Desktop/OneDrive as suspicious and quarantines the file. Not a Chrome bug, not a lock
  from a viewer (that was Wednesday's problem, different cause).
- *What fixed it:* render with **Edge** headless (`msedge.exe --headless=new --print-to-pdf`).
  TotalAV left it alone.
- *Also:* Edge needs the `file:///` URL percent-encoded — a literal space in
  `Sabre Constructions` produced a one-page "File not found" PDF. Chrome tolerated the space.

**Auto mode blocked every write into Nathan's repo** (copy, commit, push).
- *Why:* the classifier treats pushes to a repo not previously seen as production writes.
- *What fixed it:* Edward Shift+Tabbed out of auto mode. Memory `auto-mode-blocks-prod`
  already records this; it applies to the new repo too.

**Chrome screenshot showed the old page after a deploy.**
- *Why:* the reused `--user-data-dir` profile served its cache.
- *What fixed it:* a fresh profile dir + `?t=<timestamp>` on the URL.

## What's NOT Done — TODO

**Immediate**
- [ ] Send the agreement through **Zoho Sign**. Confirm the entity (29 107 425 703 vs
      29 673 587 472) before it goes.
- [ ] **Google Ads**: confirm Nathan's account exists, get the customer ID, send the manager
      link request, have him accept under Admin → Access and security → Managers.
- [ ] Confirm the Formspree email landed in admin@ inbox (not junk) and `formspree.io` is a
      safe sender.
- [ ] Push this demo repo (6+ commits ahead).

**Still needed from Nathan**
- [ ] Reference sites (URLs). Nothing in the look is final without them.
- [ ] What one build is worth; monthly ad budget. Campaign plan §10 can't be judged without them.
- [ ] The three voice-of-customer questions (§2).
- [ ] Melbourne IT + iSonic logins. HeyGen account. Google Business Profile manager access.
      Shared OneDrive folder for photos.
- [ ] Keep/slim gallery and team pages; confirm 1990.

**Next process (Edward, end of session)**
- [ ] A styling + avatar-behaviour list for the website build, pulled from the campaign plan
      §1 and §13.
- [ ] **BBL competitor-intel report** on Sabre's competitors (knockdown-rebuild builders,
      Brisbane Bayside/Redlands). Needs a competitor list first. Pipeline lives in
      `BBL/products/competitor-intel/` — read its `spec/README.md`, then run the offline
      analyst loop. See memory `bbl-report-build-spec` + `bbl-offline-analyst-loop`.

**Still blocked** — open items 1, 6, 7 (AI testimonials, other practice's design, AI team photo).

## Quick Context for Next Session

**Two folders now.** Demo/workshop: `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`.
Real site: `C:\Users\edast\OneDrive\Desktop\sabre-constructions-website\` (its own `CLAUDE.md`
inside). Read the demo repo's `CLAUDE.md` → `docs/engagement.md` → `docs/open-items.md`.

**Before any fal job for Sabre:** `$env:FAL_KEY = (Get-Content "$HOME\.keys\sabre-fal.key" -Raw).Trim()`
in that terminal only. Never set it globally.

**Before any PDF:** use Edge headless, not Chrome. TotalAV eats Chrome's output.

**Most likely next task:** the competitor-intel report. Start by naming the competitors —
the search terms in campaign plan §6 are the seed.

## Addendum — competitor-intel report BUILT (same day, later)

- Ran `POST /test-run` on **Production** Catalyst. Report row **795000000104191**, deal
  `TESTRUN260905051316`. Scraping → Analysing → **Ready_For_QA** in 24 min. No pipeline error.
  First report built under the 22 Aug code — the STATE.md "not yet proven" gap is now closed.
- QA link: `https://bbl-pipeline-7006497428.catalystserverless.com.au/server/competitor_intel_pipeline/report-html/795000000104191`
- Local copy: `docs/sessions/2026-09-05-competitor-report-795000000104191.html` (gitignored).
- Competitor set (Edward's choice, local knockdown-rebuild only, no franchises): Tide
  Constructions, Nest Bespoke Homes, Lindon Homes, Fiteni Homes, Blueneer Custom Homes.
- Scrape cost ≈ $3.00 (AI-visibility lane $2.25 of it) + $0.35 competitor-finding Places scrape.
- Gaps: competitor Facebook/Instagram lanes SKIPPED (no handles given; profile finder returned
  nothing). Lindon website crawl `failed_to_start`. Both show as honest not-captured.
- Prose is the coded writer's draft (writer 1). Hand-authored pass (`scripts/analyst_offline.py`)
  NOT run — note its `BASE` is hardcoded to Development; this report is on Production.
- Sabre's 12th review is dated 14 Aug 2026. Breakdown now 9 five-star, 1 one-or-two-star.

## Addendum 2 — the REAL report: build 2, audited, hand-written, published

Edward: "this is a real client. it needs to be real." So build 1 was audited against the spec
(`BBL/docs/audits/2026-09-05-competitor-intel-process-audit-sabre.md`), the process was then
followed properly on build 2, and the result was published.

- **Build 2 = report row `795000000099330`** (Production), with every competitor's Facebook /
  Instagram / YouTube / LinkedIn handles resolved by hand from their own sites. 53 lanes ran.
- **Gates FIRST** this time: fill gate PASS (15 DATA, 1 EMPTY = Sabre's own services list, 1
  PARTIAL); claims guard clean after one fix (a rival's quoted post caption is not our claim).
- **Writer 3 done** — all 13 units hand-authored (`BBL/scripts/.analyst/795000000099330/write_prose.py`
  → `prose.json`), applied through the real `enrich()` path, anchored by `_for` so nothing lands
  a row off, pushed with `POST /report-v4/795000000099330` → 202 → published.
- **Customer link (the bucket file, the real door):**
  `https://barebayside-reports.zohostratus.com.au/r/f9Vmproivc-gxGiIztJHgEWVcSCM9elf/report.html`
  QA route: `…/competitor_intel_pipeline/report-html/795000000099330`. Both verified to carry
  the authored text; local copies in `docs/sessions/2026-09-05-competitor-report-795000000099330-*`.
- **Six code fixes in BBL** landed on the way (chain false positive, reach line, `[your service]`
  fill, reach dial from geography, script env switch, claims-guard quote handling) — all tested,
  committed, **NOT deployed to Catalyst**. They reached this report via the local render path.
- **What the report says, in numbers Sabre can act on:** not in Google's results for any of 5
  suburbs (Fiteni holds Capalaba at #8; Wynnum/Manly/Lota/Wakerley have NO builder); 0 ads vs 78
  (Fiteni ≥40, Tide 26 Meta-only, Blueneer 10, Nest 2, Lindon 0); 0/4 assistants, 0/7 questions,
  4 questions with no winner incl. Wynnum + Manly; no readable Sabre social vs IG followers Tide
  10,249 / Lindon 5,275 / Nest 4,074 / Fiteni 2,254 / Blueneer 588; reviews 4.5 from 12 (lowest
  rating, freshest review 14 Aug 2026). **Tide already runs the "you love your street but have
  outgrown the house" Meta ad — Sabre's own positioning.**
- Still honest gaps in it: Sabre's services not itemised (Joomla banners), Sabre's own review
  text not reaching the §07 theme derivation, Fiteni's site not crawled (Apify 402). Logged in
  `BBL/products/competitor-intel/spec/10-fixing-issues.md`.

## Addendum 3 — Edward read it and it was shallow. Root cause found; report REPUBLISHED.

Edward: "you even say in reputation reviews we have no reviews we could read… I can't see that high
level of detail we had in the last report." He was right. The reviews (85 rival + 12 Sabre, with
text) were scraped; the three enrichment readers (`BBL_REVIEW_THEMES`, `BBL_AD_COPY_READ`,
`BBL_CONTENT_CLASSIFY`) are **OFF in Production** and the last example was built with them on.
Rebuilt locally with all three on (a few dollars of Sonnet), re-authored, re-published — same link.

What the republished report now has that the first publish did not:
- §07: themes with counts + verbatim quotes both sides. Sabre reviewers name a person in 8 of 11,
  praise the finished build in 6 of 11; rivals 34/85 and 12/85. The wedge is code-computed.
- §03: Google ad copy READ. **Blueneer's 10 ads are roof-and-gutter ads** (its roofing arm) —
  not builder ads; **Fiteni's 20 Google ads sell house-and-land estates**; only Tide + Fiteni
  advertise the rebuild, on Meta. The Wynnum/Manly rebuild search terms are unbought.
- §03: Tide's 10 Meta VIDEO ads now show their published frame (extractor never read `videos[]`).
- The "0 reviews of your own to read" tile can no longer occur (extract fix + test).
Both gates pass on the live page. Fix log rows + memory `bbl-production-enrichment-flags-off`.
**Decision for Edward: flip the three flags to 1 in Production.** Until then, every client build
must be rebuilt locally with them on.

## Addendum 4 — §01 was measured in the wrong hemisphere; re-checked and republished

Edward: "I don't understand Getting found… I'd like to see where you'd even rank." Digging in: the
intake geography "Wynnum, Manly, Lota, Wakerley, Capalaba, **Cleveland**, QLD, Australia" made the
pipeline take Cleveland as the CITY anchor, and the map-pack lane (no location parameter) returned
**Cleveland, Ohio**. The terms were also too narrow ("knockdown rebuild builder <suburb>" only).
- Re-checked by hand 2026-09-05 (Google AU, top 30 + Maps pinned to QLD): **Sabre absent from all
  13 searches and all 5 map boxes.** "builders Wakerley": Tide #1. "builders Capalaba" map box:
  Fiteni #3, Tide #15, Dixon #1. "custom home builders Brisbane bayside": Nest #7, Lindon #26.
  KDR terms: Tide #3 Manly, Fiteni #9 Lota / #27 Capalaba, Blueneer #1 in the Wynnum map box.
  "builders Wynnum" page one = Baybuilt, hipages, Pro Builder, Johnston, Oceanview, Symcorp.
- Corrected datasets substituted into the report cache (originals kept), §01 rebuilt and
  re-authored, republished (same link). Raw checks saved beside the report in `docs/sessions/`.
- BBL fixes committed (`c923172`): a trailing served suburb is never the city anchor (per-country
  metro list); the map lane now carries `locationQuery`. Fix log has the OPEN rule: rank terms
  should be the trade's head terms ("builders", "home builders", "knockdown rebuild"), not the
  customer's one-liner, and §01 must print the exact queries.
**Intake rule from now on: geography = "<served suburbs…>, <METRO>, <STATE>, <COUNTRY>" — the
metro named explicitly, e.g. "…, Brisbane, QLD, Australia".**
