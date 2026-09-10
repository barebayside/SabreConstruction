# Search + AI visibility plan — how Sabre gets found on Google and named by AI assistants

> **Layer 4. Canonical for organic search and AI search from 2026-09-10.** Sits beside
> `campaign-strategy.md` (paid) and takes over its §9. Method: the `seo-plan` skill (local-service
> template), the `seo-geo` skill, and the Project 24 / Income School method BBL already uses
> (`~/.claude/skills/income-school-blog`, `BBL/site/content/seo-geo-strategy.md`,
> `BBL/site/content/income-school-blog-method.md`). Baseline: the 09-05 competitor report and its
> raw rank / map-box / AI-assistant data in `docs/sessions/`. Site audit: today.
>
> Facts on every page still obey `site/docs/client-facts.md` and rule 1. Nothing here invents a
> number, a price or a claim.

## 0 · Where Sabre stands today

From the report (5 September) and this morning's read of the real site:

| Surface | Baseline | What it means |
|---|---|---|
| Google web results, 13 head searches | Sabre absent from all 13. "builders Wakerley" = Tide #1; "builders Lota" = Tide #25; the rest are directories, Facebook, Reddit and volume builders | The suburb searches are **weakly held** — page one is hipages, Yellow Pages, Instagram. A real 600-word suburb page can take it |
| Google map box, 5 "builders <suburb>" searches | Sabre in none. In **Capalaba, its own suburb**, the box shows Fiteni #3, Tide #15; the rest are tiny builders with 5.0 from a handful of reviews | The listing is weak, not the reviews. Category, service area, hours, photos and the website link decide this box |
| Google **AI Overview** (already live on every "knockdown rebuild builder <suburb>" search) | Names Coral, Plantation, Tide, Integrity New Homes, CJ Homes. Pulls builder names + ratings straight from Google listings and page-one pages | Being in the map box and on page one **is** being in the AI Overview. Same work, second payoff |
| ChatGPT, Perplexity, Claude, Gemini | Named Tide, Nest, Lindon, Fiteni, Blueneer between them. **Never Sabre** | Assistants cite what the web says about you. Today the web says almost nothing |
| The real site (v19) | Static HTML (good — AI crawlers read it without JavaScript). **No `robots.txt`, no `llms.txt`, no schema anywhere, no dates or bylines, every page `noindex`,** sitemap points at `www.` before the host is decided. Wynnum/Manly pages ≈ 300 words | Nothing can index until DNS cutover, so the foundation goes in now and switches on the day the domain does |
| What people actually search (related queries, 45 SERPs) | "knock down rebuild **cost calculator**" (20×), "knock down rebuild brisbane **cost**" (18), "knock down and rebuild **packages**" (12), "**metricon** knockdown rebuild" (12), "builders wynnum **reviews**", "**small builders** manly", "**independent builders** capalaba" | Cost is the question. Sabre has no price to publish (rule 1) — so it answers **what decides the cost**, honestly, which nobody else on page one does |

## 1 · How each surface decides — and what feeds it

```
Google web results  ◀── the page: one question per page, 600+ unique words, the suburb in the title,
                        real detail nobody else has, schema, internal links, a live domain
Google map box      ◀── the Google Business Profile: category, service area, hours, photos, reviews
                        with replies, website link — AND the same name/address/phone everywhere
Google AI Overview  ◀── the two above (92% of AI Overview citations are top-10 pages) + the listing
ChatGPT/Perplexity  ◀── what OTHER sites say: Wikipedia/Wikidata, Reddit, YouTube, directories,
                        news — brand MENTIONS matter about 3× more than backlinks (Ahrefs 2025)
                        + passages on our pages that answer a question in 134–167 self-contained words
```

So the plan has four legs, and they share most of the work: **the listing, the pages, the
mentions, the measurement.**

## 2 · What Sabre has that the rivals don't

Real, verifiable, and unused on the web today:

1. **Two Olympians own the company.** Stewart Brain (Seoul 1988, 1986 Commonwealth bronze) and
   Cathy Grainger-Brain (1992 + 1996 Olympics, 1990 Commonwealth bronze) each have a **Wikipedia
   article, a Wikidata item, an olympics.com.au profile, an Olympedia and a JudoInside page.**
   That is entity presence AI assistants weight heavily, and it is sitting one `sameAs` link away
   from the site. No competitor has anything like it. (It is already true and on client-facts.)
2. **Since 1990.** Every rival on the AI Overview list is younger or a franchise.
3. **Master Builders Queensland member No. 00352** and a QBCC licence — both have public
   registers. A listing there is a citation Google trusts.
4. **Nine cleared, dated, named Google reviews** that name the fears (hidden costs, the builder who
   disappears) and answer them — voice-of-customer that reads as evidence, not marketing.
5. **The plain-words character-overlay explainer.** Thousands of Brisbane owners type "can I knock
   down my house" and page one is volume builders. Ours cites council's own wording.
6. **A static site** the AI crawlers can read whole. Most rivals are JavaScript templates.

## 3 · Site architecture — the URLs and the job of each

Keep the eleven that exist. Add in this order; every page is a registry record (`SAB-…_WEB_PAGE`).

| URL | Job | Search it targets | State |
|---|---|---|---|
| `/` | name the decision, the walk-through | "sabre constructions", "builders capalaba" | live |
| `/wynnum/`, `/manly/` | suburb pages | "builders wynnum", "knockdown rebuild wynnum" | live, **thin (≈300 words) → 600+** |
| **`/knockdown-rebuild/`** (new) | the service page — what the path is, the three steps, where you live, who draws it | "knockdown rebuild brisbane bayside", "knockdown rebuild builders" | to write |
| `/lota/`, `/wakerley/`, `/capalaba/` (new) | suburb pages 3–5. Wakerley is Tide's; still worth the page | "builders lota qld" (page one is directories), "builders wakerley", "builders capalaba" | to write, one at a time |
| `/blog/can-we-knock-down-our-house/` | the overlay explainer | "character overlay brisbane", "can i demolish my house brisbane", "pre 1947 house demolish" | live — add dates, byline, FAQ block |
| `/blog/rebuilding-in-wynnum-or-manly/` | five things first | "rebuild wynnum", "knockdown rebuild manly" | live — same |
| `/blog/…` (bank in §7) | one question per post | the long tail | to write, one a fortnight |
| `/meet-the-team/` | E-E-A-T: who is promising this | "stewart brain builder", the Olympian story | live — becomes the Person-schema page |
| `/testimonials/` | belief from similar others | "sabre constructions reviews", "builders wynnum reviews" | live — add review dates, a review link |
| `/designs/`, `/gallery/`, `/contact/` | as now | — | live |

Stop at **six suburb pages** (Wynnum, Manly, Lota, Wakerley, Capalaba, one of Birkdale/Wellington
Point). The local-service template warns at 30 and hard-stops at 50; the real limit here is that
each page needs 60% content that is genuinely about that suburb — a street, a house Sabre built
there, the overlay pattern, the school, the block sizes. If Nathan can't say something true about
a suburb, it doesn't get a page.

**Internal linking:** every suburb page links to the service page and the overlay post; every post
links to one suburb page and the contact page; the home page links to all of them once. Footer
already carries Wynnum and Manly — add the rest as they go live.

## 4 · Technical foundation — goes in now, switches on at cutover

| # | Item | Detail | When |
|---|---|---|---|
| 1 | **Decide the host** — `sabreconstructions.com.au` or `www.` | The sitemap says `www.`; the DNS task says CNAME `www` → GitHub. Pick one, make the other redirect (GitHub Pages does this when the CNAME file holds the canonical host). Every `<link rel="canonical">`, the sitemap and `llms.txt` must agree | before cutover |
| 2 | **Remove `noindex`** from all 11 pages | Currently a `<meta name="robots">` on every page. One `sed` — but only on cutover day, never before | cutover day |
| 3 | **`robots.txt`** | Allow everything; allow the AI search crawlers by name (`GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`); point at the sitemap. Appendix A | now (harmless while noindex) |
| 4 | **`llms.txt`** | The site in one page for assistants: who Sabre is, the facts, the key pages with one-line descriptions. Appendix B | at cutover (needs the host) |
| 5 | **Schema (JSON-LD)** | Home: `HomeAndConstructionBusiness` with address, phone, hours, `foundingDate: 1990`, `areaServed` (the suburbs), `sameAs` (Facebook, GBP, MBQ listing), `founder` → two `Person`s. Meet the team: `Person` for Stewart and Cathy with `sameAs` → Wikipedia, Wikidata, olympics.com.au. Posts: `Article` with `author`, `datePublished`, `dateModified`. Suburb pages: the business again with `areaServed` = that suburb. Breadcrumbs on subpages. **No `AggregateRating` markup** — Google no longer shows self-serving review stars, and 4.5/12 is already on the page in text. **No `FAQPage` schema** — Google restricted FAQ rich results to government/health sites in 2023; the FAQ *structure* on the page is what AI reads. Appendix C | now |
| 6 | **Dates and bylines** | Every post: "By Nathan Brain · Published 8 Sep 2026 · Updated …" as visible text and in schema. An undated page is a weak citation | now |
| 7 | **`<link rel="canonical">`** on every page | With the chosen host | with #1 |
| 8 | **Sitemap `lastmod`** | Add dates; regenerate when a page changes | now |
| 9 | **Google Search Console + Bing Webmaster Tools** | Verify the domain (DNS TXT — goes in the same iSonic email as the A records). Submit the sitemap. Bing feeds Copilot and ChatGPT search; use IndexNow for instant pings | cutover day |
| 10 | **Speed** | The home hero is a 10-second video (two files). Keep the `poster`, add `preload="none"` on the portrait/wide file that isn't shown, lazy-load below-the-fold images, `width`/`height` on every `<img>`. Fonts already load with `display=swap`. Measure with PageSpeed once live; target LCP < 2.5 s on mobile | now |
| 11 | **Image alt text** | Real descriptions: "Clarence, a Sabre knockdown rebuild in Manly, front elevation" — not "house" | now |

## 5 · Google Business Profile — the biggest single lever, and it needs Nathan's login

Everything in the map box and most of the AI Overview comes from here.

1. **Get manager access** (run-sheet leftover). Until then nothing below can be done.
2. **Primary category: Home builder. Secondary: Custom home builder, General contractor.** Check what it is now — being absent from the Capalaba box suggests a wrong category or an unverified listing.
3. **Service area = the suburbs, named** (Google no longer accepts a whole state): Wynnum, Wynnum West, Manly, Manly West, Lota, Hemmant, Tingalpa, Wakerley, Gumdale, Ransome, Belmont, Chandler, Capalaba, Birkdale, Thorneside, Wellington Point, Ormiston, Cleveland, Thornlands.
4. **Hours accurate** (Mon–Fri 8–4). "Open at time of search" is now a top-5 local ranking factor (Whitespark 2026).
5. **Name / address / phone identical everywhere**: "Sabre Constructions", 3/73–75 Steel St Capalaba QLD 4157, and **one** phone. ⚠️ Decide which: the listing probably shows the 07 line; the site shows Nathan's mobile. Mismatched phones cost map-box trust. Recommendation: primary = 07 3823 3200 on the listing (it's the registered business line), mobile as additional.
6. **Website link** → the new site after cutover; **appointment link** → `/contact/`.
7. **Photos**: the seven finished homes (real), the team photo when it exists, the office front. Volume matters; AI-generated images do not go here (rule 3/5, and Google's own policy).
8. **Services** listed in Google's own fields: Knockdown rebuild, Custom home, Renovation/extension — each with a two-line plain description.
9. **Reviews**: reply to all twelve, including the 1-star, in Nathan's voice. Create the short review link (`g.page/r/…`) and put it on a card Nathan hands over at the keys. That is the whole review programme — and it is the one thing that moves the box fastest.
10. **Posts**: one a month — a finished build, a question answered. Reuse the blog.

## 6 · Citations and brand mentions — what other sites say about Sabre

For assistants this outranks anything on our own pages. In order of value per hour:

| Where | What | Cost |
|---|---|---|
| **Master Builders Queensland** member directory | Confirm the listing shows the website, phone and suburbs. MBQ pages rank on "builders capalaba" already | free, Nathan's login |
| **QBCC licence register** | Public; confirm the trading name and address match | free |
| **Wikipedia / Wikidata** | Do NOT edit either to promote the business. But the site's `Person` schema links *to* them, and the meet-the-team page tells the story in text, which is what an assistant needs to connect "Stewart Brain, Olympian" with "Sabre Constructions, builder" | free |
| **Free directories that already hold page one**: Yellow Pages, Localsearch, TrueLocal, Houzz, hipages (free profile), Oneflare, Service.com.au | Identical NAP, the website, one paragraph, three photos. Skip paid tiers | free, 2 hours |
| **Facebook page** | Already exists. Fill "About" with the same NAP + founded 1990 + the suburbs; post the blog | free |
| **Instagram** | Handle unknown (icon on the banner) — find it, same bio | free |
| **YouTube** | A channel for the filmed builds. YouTube mentions are the strongest AI-visibility signal measured (Ahrefs). Each build video: title with the suburb, description with the story, link to the suburb page | needs the footage |
| **Local news** | "Two Olympians have been building Bayside homes for 36 years" is a real story for the Wynnum Herald / Redland City Bulletin / Bayside Bulletin. One pitch, one photo. A news mention is exactly what Perplexity cites | one email |
| **Ohori Judo Club** | Its About page already names Stewart and Cathy. A line there ("Stewart and Cathy run Sabre Constructions in Capalaba") is a legitimate, true mention on a site they own | free |
| Reddit | Never post about Sabre. If a genuine "builders in Wynnum?" thread exists, Nathan can answer as himself, once | — |

## 7 · Content — the article bank

➡️ **MOVED 2026-09-10 to `article-bank.md`, which is canonical.** It holds the three
spirals (building · living on the Bayside · dealing with a builder in Australia), all 45
titles with estimated search bands, the writing rules, and the four-phase order to write
them in. What was here was the first 22 titles with no volumes and no place cluster.

The rules that governed this section still stand and are restated there: one question per
post, the answer in the first 60 words, a 134–167-word self-contained answer block, two
attributed proof points, a Common questions block, one CTA, Nathan's byline, and one real
detail from Nathan in every post or it gets cut.

## 8 · The existing pages — the fixes that make them citable

| Page | Change |
|---|---|
| Both posts | Date + byline; a 134–167-word "short answer" block at the top that stands alone; "Common questions" (the Wynnum post has one; the overlay post needs one); `Article` schema; the exact council wording kept as a quoted, attributed passage |
| `/wynnum/`, `/manly/` | 300 → 600+ words of true local detail (needs Nathan); title keeps "Builders in Wynnum"; H2s as questions ("Can we knock down a Wynnum house built in the 1930s?"); link to the overlay post and the service page |
| `/meet-the-team/` | The Olympian paragraph becomes explicit and factual (games, years, medals — all sourced); `Person` schema with `sameAs`; "founded Sabre Constructions in 1990" in the same sentence as the names, so the entity link is on the page in text |
| `/testimonials/` | Review dates shown; "4.5 from 12 on Google, read 5 Sep 2026"; link to the Google listing; never a rating in schema |
| `/` | Alt text; `HomeAndConstructionBusiness` schema; one passage that answers "who is Sabre Constructions?" in 60 words for the assistants |

## 9 · Measurement — the monthly read

Reuse what the report already built (Apify Google SERP + Places actors, the four-assistant check):

| What | How | Cadence |
|---|---|---|
| Rank on the 13 head searches + map box on 5 | the two rank-check runs from 09-05, same queries, pinned to Queensland | monthly, first Monday |
| AI Overview — is Sabre named? | read from the same SERP runs (`aiOverview` field) | monthly |
| The four assistants — "best knockdown rebuild builder in Wynnum/Manly/Bayside", "can I knock down my house in Wynnum" | ask ChatGPT, Perplexity, Claude, Gemini; record who is named | monthly |
| Impressions, clicks, queries per page | Search Console | weekly, on the SAB page records with the paid numbers |
| Map-box actions: calls, direction requests, website taps | GBP Insights | monthly |
| Leads that arrived organic | the lead ledger: `utm_source` empty + `referrer` google → organic | weekly |

Success is not traffic. It is: **in the Capalaba and Wynnum map boxes by month 3; page one for
"builders wynnum" and "knockdown rebuild manly" by month 6; named by at least one assistant for a
Bayside rebuild question by month 6; organic enquiries in the ledger.** No target has a number
until Search Console has a baseline month.

## 10 · Roadmap — four phases, gated on the domain

**Phase 1 · Foundation (now → cutover).** Everything in §4 that can go in under `noindex`:
robots.txt, schema, dates/bylines, alt text, canonical prep, speed. Fix the two posts (§8). Write
`/knockdown-rebuild/`. Grow Wynnum + Manly (needs Nathan's detail). Directory NAP audit (§6) and the
MBQ/QBCC checks. **Gate: DNS answer from iSonic / Melbourne IT; the host decision.**

**Phase 2 · Switch-on (cutover week).** `noindex` off, `llms.txt`, canonical host, Search Console +
Bing verified, sitemap submitted, GBP website link updated, GBP category/service area/hours/photos/
review replies (needs Nathan's login). First staple published: *What decides the cost.*

**Phase 3 · Expansion (months 2–4).** Lota, Wakerley, Capalaba pages one at a time; a response post
every fortnight; the review link in Nathan's hand; the local-news pitch; Facebook/Instagram bios;
first monthly measurement read.

**Phase 4 · Authority (months 5–12).** YouTube channel when the first build is filmed; the pillar;
the remaining suburb page; quarterly review of which posts earned an enquiry (ledger) and which
assistant names Sabre. Prune anything that earned nothing.

## 11 · Who does what

| Claude, now, unblocked | Nathan (ten minutes each) | Edward |
|---|---|---|
| robots.txt, schema on all pages, dates/bylines, alt text, speed fixes, canonical prep, the service page draft, the two posts' fixes, the first staple draft, llms.txt ready for the host | GBP login/access; the phone to show on the listing; one voice note per suburb (a street, a job, a house); the cost drivers in his words; confirm the architect path; the review link on a card | DNS/host decision; Search Console + Bing at cutover; directory profiles (2 hrs); the news pitch; the monthly measurement run |

---

## Appendix A · `robots.txt` (drop at the root; harmless while `noindex` is on)

```
User-agent: *
Allow: /

# AI search crawlers — allowed on purpose (visibility, not training)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://sabreconstructions.com.au/sitemap.xml
```
(Change the sitemap host if `www.` wins.)

## Appendix B · `llms.txt` (at the root, after the host is decided)

```
# Sabre Constructions
> Family-owned builder in Capalaba, Queensland, building custom homes and knockdown rebuilds across
> Brisbane's Bayside and the Redlands since 1990. Founded by Stewart and Cathy Brain; Nathan Brain
> walks every house with the family. QBCC licensed, Master Builders Queensland member No. 00352.

## Key pages
- Home -> https://sabreconstructions.com.au/ : who Sabre is and how a rebuild starts (a walk-through with Nathan)
- Knockdown rebuild -> https://sabreconstructions.com.au/knockdown-rebuild/ : the three-step path, the four questions families ask
- Can we knock down our house? -> https://sabreconstructions.com.au/blog/can-we-knock-down-our-house/ : Brisbane's pre-1947 character rules in plain words
- Rebuilding in Wynnum or Manly -> https://sabreconstructions.com.au/blog/rebuilding-in-wynnum-or-manly/ : five things to know first
- Builders in Wynnum -> https://sabreconstructions.com.au/wynnum/
- Builders in Manly -> https://sabreconstructions.com.au/manly/
- Meet the team -> https://sabreconstructions.com.au/meet-the-team/ : Stewart and Cathy Brain (Olympic judoka), Nathan Brain, the team
- Testimonials -> https://sabreconstructions.com.au/testimonials/ : Google reviews, quoted word for word
- Contact -> https://sabreconstructions.com.au/contact/ : 0422 831 306, 3/73-75 Steel St Capalaba QLD 4157

## Facts
- Founded 1990 in Capalaba, Queensland, by Stewart Brain and Cathy Grainger-Brain
- Service area: Wynnum, Manly, Lota, Wakerley, Capalaba, Birkdale, Wellington Point, Cleveland and the Bayside/Redlands
- Google rating 4.5 from 12 reviews (read 5 September 2026)
```
(Only facts from `client-facts.md`. Update the rating line when the count changes.)

## Appendix C · Schema — the two blocks that matter most

Home page (`HomeAndConstructionBusiness`; fill `sameAs` with the real URLs as they are confirmed):

```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Sabre Constructions",
  "url": "https://sabreconstructions.com.au/",
  "telephone": "+61422831306",
  "email": "admin@sabreconstructions.com.au",
  "foundingDate": "1990",
  "founder": [
    {"@type": "Person", "name": "Stewart Brain"},
    {"@type": "Person", "name": "Cathy Grainger-Brain"}
  ],
  "address": {"@type": "PostalAddress", "streetAddress": "3/73-75 Steel St", "addressLocality": "Capalaba", "addressRegion": "QLD", "postalCode": "4157", "addressCountry": "AU"},
  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "16:00"},
  "areaServed": ["Wynnum","Wynnum West","Manly","Manly West","Lota","Hemmant","Tingalpa","Wakerley","Gumdale","Ransome","Belmont","Chandler","Capalaba","Birkdale","Thorneside","Wellington Point","Ormiston","Cleveland","Thornlands"],
  "memberOf": {"@type": "Organization", "name": "Master Builders Queensland"},
  "sameAs": ["https://www.facebook.com/sabreconstructions"]
}
```

Meet the team (`Person`, one each — this is the entity link no rival has):

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Stewart Brain",
  "jobTitle": "Owner and builder, Sabre Constructions",
  "worksFor": {"@type": "Organization", "name": "Sabre Constructions", "url": "https://sabreconstructions.com.au/"},
  "sameAs": [
    "https://en.wikipedia.org/wiki/Stewart_Brain",
    "https://www.wikidata.org/wiki/Q30064129",
    "https://www.olympics.com.au/olympians/stewart-brain/"
  ]
}
```
Cathy: `https://en.wikipedia.org/wiki/Cathy_Grainger-Brain`, `https://www.wikidata.org/wiki/Q30316173`,
`https://www.olympics.com.au/olympians/catherine-brain/`. Verify each URL resolves before it goes in.

Posts: `Article` with `headline`, `author` (Nathan Brain, Person), `publisher` (the business),
`datePublished`, `dateModified`, `mainEntityOfPage`.

## Appendix D · The post brief (one per article, before writing)

```
Question (the title):
Who is asking, at what hour, on what device:
The 60-word answer:
Nathan's real detail (quote or voice-note timestamp):
Two proof points + sources:
Facts used (each must be in client-facts.md or sourced on the page):
Internal links: suburb page / service page / contact
Registry code (SAB-CON-KDR-n.0A_WEB_PAGE):
```
