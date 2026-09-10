# BBL and Sabre — how the two sites link to each other

> **Layer 4 reference. Written 2026-09-10.** Sabre is BBL's first client site. Whatever
> pattern gets set here gets repeated on the next one, so it is worth setting properly.
>
> BBL's site: **barebaysidelabs.com** (68 blog posts, all local-business marketing).
> It has a `/results/` page and **no case studies, and no mention of Sabre anywhere.**
> Sabre's site credits nobody in its footer today.

---

## 1 · The short version

**Articles about Bare Bayside Labs do not belong on Sabre's blog.** They belong on BBL's,
and they should link *out* to Sabre. That is the direction that does work for both sites.

Sabre's blog exists to be found by Bayside families deciding whether to rebuild. Every post
in the article bank is aimed at that one job, and the whole three-spiral plan is built on
topical focus — being the site that is unmistakably about knocking down and rebuilding on
the Bayside. An article about a marketing agency on that blog serves no reader who lands
there, and it works directly against the thing we are trying to build.

There is also a plainer problem with "slipping in" links. The agreement with Nathan is a
barter with very little in writing. Putting links to your own business inside his site
without telling him is the sort of thing that costs nothing to ask about and a great deal
to be discovered later. **He will almost certainly say yes** — a "site by" credit is what
every builder expects — so ask, and then it is a credit rather than something found.

So: **one honest link out of Sabre, and five real articles on BBL pointing back in.**

---

## 2 · The one link that belongs on Sabre's site

A footer credit. Branded anchor, one link, every page.

```html
<p class="small">Website by <a href="https://barebaysidelabs.com/" rel="noopener">Bare Bayside Labs</a></p>
```

Goes in the third footer column, under the Facebook line, on all 13 pages.

**Why this exact form and not another:**

| Rule | Why |
|---|---|
| Anchor text is **"Bare Bayside Labs"**, the brand | A site-wide footer link with a keyword anchor ("Brisbane marketing agency", "local SEO") is one of the clearest link-scheme signals there is. A branded credit is normal and expected |
| **One** link, not two or three | A footer credit is a credit. A footer block of links is an ad on someone else's site |
| Not `nofollow` | It is a genuine editorial credit for work actually done. Nothing to hide |
| In the footer, never in an article body | Article bodies belong to the reader who came for the article |

⚠️ **Ask Nathan first.** One sentence: *"Standard for us is a small 'website by' credit in
the footer — happy for me to put it on?"* The markup above is ready to apply the moment he
says yes; it is deliberately not on the site until he does.

⛔ **The footprint problem, worth naming now.** One agency-and-client pair linking to each
other, once each, with branded anchors, is ordinary business. Twenty client sites all
carrying the same keyword-anchored footer link is a pattern Google recognises and discounts,
and Sabre is client number one. Set the branded, single-link version now and it scales.

---

## 3 · The five BBL articles the Sabre work has already paid for

This is where "a few articles" actually goes. BBL's blog has 68 posts and **not one case
study** — no proof that any of the method has been run on a real business. The Sabre
engagement has produced five genuinely publishable ones, and every one links to Sabre.

Each is a real BBL post in BBL's existing voice, not a brochure.

### A. What 39 Google searches told us about a builder's market
The 09-05 SERP scrape, written up as method. Cost dominates (31 of 104 related queries,
130 appearances); the top query in the whole set was a *cost calculator*; a national volume
builder's brand sits inside the local search; "small" and "independent" are the words the
customer uses. **Slots against** BBL's existing `how-google-ranks-local-businesses` and
`local-seo-checklist`. **Links to** Sabre as the worked example.
*This is the strongest of the five — nobody else publishes their actual research.*

### B. The contact form that could not be submitted
Found 09-10: a three-step form with no script on the page, live for two days, on the page
every call-to-action pointed at. The lesson is BBL's own — **test the page, not the draft** —
and it is a better trust-builder than any claim about quality. **Slots against**
`fast-site-consistent-details`. **Links to** Sabre's contact page as the fixed version.

### C. Why we won't put a price on a builder's website
Every competitor publishes a range; the ranges contradict each other; the honest answer is
what *decides* the number. The reasoning behind Sabre's cost article, as a positioning piece
about how BBL writes for trades. **Slots against** `knowing-your-cost-per-job`.
**Links to** Sabre's cost post when it publishes.

### D. Suburb pages that are worth having, and suburb pages that are padding
BBL already has `building-suburb-pages`. This is the follow-up with a real case: six pages
maximum, and a suburb only gets one if the owner can say something true about it. **Links
to** Sabre's Wynnum and Manly pages.

### E. A builder who has been on the same bay since 1990 — the first case study
The straight one, for `/results/`. What the site had to do, what was built, what is measured
weekly through the asset registry. **Publish it last**, once there are numbers to put in it.

⚠️ **Nathan sees these before they publish.** Every one names his business, and two of them
(B especially) describe things that went wrong on the way. Send them to him first. A client
who is asked usually enjoys being the case study; a client who finds out usually does not.

⚠️ **No invented numbers, same rule as everywhere.** Article E waits for real results rather
than getting adjectives. [[feedback-no-invented-numbers]]

---

## 4 · Where BBL may appear *inside* a Sabre page

Almost nowhere, and that is deliberate.

| Place | Allowed? |
|---|---|
| Footer credit, branded anchor | ✅ Once Nathan says yes |
| Inside an article body, as a link | ⛔ No. The reader came for the article |
| In an article's source line, if a BBL-published piece is genuinely a source | ✅ But only if it is actually cited, and it almost never will be |
| A "how this site was built" page on Sabre's site | ⛔ No. It is Sabre's site |
| Sabre's blog carrying a post about marketing | ⛔ No. It breaks the topical focus the whole plan runs on |

---

## 5 · The order to do it in

1. Ask Nathan about the footer credit. One sentence. Apply the markup in §2 if yes.
2. Write BBL article **A** — it needs nothing from anyone and the data is already in
   `docs/sessions/`.
3. Write **B**. Also needs nothing.
4. Send Nathan A and B before they go up.
5. **C** and **D** follow their Sabre counterparts.
6. **E** waits for real numbers off the registry.

Each BBL article is a BBL registry record under BBL's own brand code, not `SAB` —
these are BBL's assets, marketing BBL, and they measure BBL's traffic.
[[bbl-client-campaigns-follow-the-registry]]
