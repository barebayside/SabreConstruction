# Engagement — what we agreed, what we're waiting on, what's next

> **Layer 4.** The commercial and scope state of the Sabre relationship.
> Facts about *Sabre the business* live in `../site/docs/client-facts.md`.
> Things that are broken or fake live in `open-items.md`.
> This file is about **the deal and the sequence of work**.
>
> Last updated: **2026-09-05**.

## ⭐ 2026-09-05 — the real site exists, in Sabre's own repo

Nathan came to Edward's for the run-sheet day. Result:

| Item | State |
|---|---|
| **Agreement** | Nathan AGREED. Day counts and Schedule A removed. PDF ready for Zoho Sign, not yet sent. Entity still unconfirmed |
| **Real repo** | `github.com/Sabre-Constructions/sabre-constructions-web-site-` — org owned by Nathan, Edward is a pusher. Skeleton in, **Pages LIVE** at `sabre-constructions.github.io/sabre-constructions-web-site-/`, still `noindex` |
| **Enquiry form** | LIVE via Formspree in Sabre's name, notifies admin@. Radio-first §8 design. Test accepted |
| **fal.ai** | Sabre's account + key (`~/.keys/sabre-fal.key`). Killarney 78 upscaled on their billing |
| **Meta** | access confirmed |
| **Google Ads** | NOT confirmed — "a bit funny". Link request still to do |
| **DNS / Melbourne IT / iSonic / HeyGen / GBP / shared folder / reference sites / the two numbers** | still outstanding |

Sequence is now: **2 · Website build + campaign structures + content ← WE ARE HERE.**
**Competitor-intel report DONE the same day** — row `795000000099330`, hand-authored, published:
`https://barebayside-reports.zohostratus.com.au/r/f9Vmproivc-gxGiIztJHgEWVcSCM9elf/report.html`.
It sets the SEO and campaign targets (Wynnum + Manly pages first; search ads on suburb terms;
Tide already owns the "you're not moving" Meta angle). See the handoff addenda.

## Status — this is no longer a pitch

As of **2026-08-17** the conversation with Sabre is finished and the work is on.
Everything in this repo up to now was a speculative demo built to win the job.
It has won it. **The build is now real**, and that changes what the open items
mean — see *What changes now* below.

## Scope

| We do | Detail |
|---|---|
| **Website** | Build out their site. Not the demo — the real one, on their domain |
| **Meta ads** | Campaign structure, creative, copy |
| **Google ads** | Campaign structure, creative, copy |

## Commercial — payment is in kind

Sabre pays in **goods and labour, not cash**:

- **Materials at cost**
- **Help building a deck**

⚠️ **Nothing is in writing.** This is a verbal arrangement from one conversation.
Before serious hours go in, get the exchange written down in an email both sides
have — what "at cost" covers, roughly what the deck involves, and what happens
if either side's scope grows. An unwritten barter is the easiest kind of deal to
end up resenting.

⚠️ This sits outside BBL's productised model. `reference/bbl-links.md` records the
no-retainer rule and points at BBL's pricing files. This is a deliberate
exception — a client build taken on directly, priced in kind. Don't treat it as
a precedent for BBL, and don't let it drift into an open-ended retainer.

## Advertising strategy

**Quick awareness.** The ads exist to make Bayside families aware Sabre exists
and that knockdown-rebuild is a path open to them. They are not expected to close
a build off a click — a new home is a months-long, high-consideration decision.
The ad buys attention; the website does the convincing.

That is why the content engine below matters more than the ad creative does.

## The content engine — Sabre's own builds

On his **big builds**, Sabre will bring in a **professional** to film
**before, during and after**.

That footage becomes the demo on the website: *this is what we do, this is how we
take you through it.* A real process, on a real job, with real people — which is
exactly what every AI stand-in in this repo is currently faking.

**This is the single most valuable thing in the whole engagement.** It replaces
the AI testimonials, it replaces the AI team photo, it fills the process section,
and it feeds the ads. Everything else is scaffolding around it.

## Sequence — why we're waiting

```
1. Sabre hands over access          <- WE ARE HERE
2. Website build + campaign structures + content
3. Campaigns go live
```

Step 2 does not start properly until step 1 lands. Building the real site against
a domain we can't reach, or a campaign structure inside an ad account that doesn't
exist yet, is work that gets thrown away.

## Sent, awaiting reply

Email to Sabre, **2026-08-17**, asking for:

| Ask | Why it's needed |
|---|---|
| **Google Ads account** | Either they create one and grant access, or we create it under their billing. Needed before any campaign structure is real |
| **Access to their existing website** | To see what's there, what's worth keeping, and what the current host is |
| **DNS access** | To point the domain at the new site when it's ready. This is the piece that actually makes the site theirs rather than a `github.io` demo |

## What changes now the build is real

The 🔴 items in `open-items.md` stop being demo caveats and become **obligations**.
Specifically:

| Item | Why it's now urgent |
|---|---|
| 1 · AI testimonial videos | Cannot go on a live commercial site. The filmed builds replace them |
| 7 · AI team photo | Same. A real team photo is a 20-minute phone job |
| 2 · Lead form goes nowhere | The moment the site is live on their domain, a lost enquiry is a lost build |
| 4 · Invented budget bands | Sabre can now confirm these against real job sizes — ask |
| 5 · Unconfirmed claims | Sabre can now confirm how they actually operate — ask |
| 🟡 Preview chrome + `noindex` | All of it comes off before the real site ships |

Ask items 4 and 5 in the same conversation as the access handover. They're five
minutes of his time and they unblock the copy.

## To do

### Blocked on Sabre
- [ ] Google Ads account created / access granted
- [ ] Existing website access — host, CMS, logins
- [ ] DNS access
- [ ] Confirm the budget bands against real job sizes (open item 4)
- [ ] Confirm the operating claims (open item 5)
- [ ] Real team photo — the six of them, on a phone, out front of a live build
- [ ] Reference sites — the other websites and styles he likes *(see below)*
- [ ] First filmed build — before / during / after

### Design direction
- [ ] **Collect his reference sites.** He has other websites and ideas he wants the
      look pulled from. Get the actual URLs, not adjectives
- [ ] Build template / stylistic options from those references for him to choose
      between, rather than presenting one design and defending it
- [ ] Reconcile whatever he picks against `reference/design-system.md` — the red
      and black are sampled from his own logo and shouldn't move without a reason

### Ours, unblocked — can start now
- [ ] Meta campaign structure, drafted against the quick-awareness goal
- [ ] Google campaign structure, same
- [ ] Ad copy and creative concepts — `ads.html` already holds three
- [ ] Plan the process section the filmed build will drop into, so the footage
      lands in a slot that already exists

### Ours, blocked
- [ ] Real site build — needs the domain and hosting picture first
- [ ] Wire the lead form to a real address (open item 2)
- [ ] Strip preview chrome and `noindex` before launch

## Open questions

- Who owns the Google Ads account and who pays the media spend? Not yet agreed
- ✅ **Decided 2026-09-03: the existing site STAYS UP until the new build is accepted**, then cut over in one go.
- Is there a budget for the ad spend itself? The in-kind deal covers our work,
  not Google's and Meta's invoices

---

## ⭐ 2026-08-24 — DECISION: the real site is a FRESH repo

The website gets **rebuilt from scratch in a new repository**, not evolved out of
this one.

**Why.** This repo is a speculative pitch artefact. It carries three ad landing
pages, an ad-concepts showcase, a blocked render page, AI testimonial videos and
an AI team photo, all wired into one long single-page `index.html`. None of that
belongs in a real builder's commercial website. Carrying it forward means
inheriting every open item in `open-items.md`.

**What each repo is for from now on:**

| Repo | Purpose | Status |
|---|---|---|
| `barebayside/SabreConstruction` (this one) | the demo, the ad concepts, the three LPs, the asset pipeline in `tools/` | stays as-is, stays `noindex` |
| **new repo, not yet created** | the real multi-page website that `sabreconstructions.com.au` will point at | ⛔ blocked — see below |

The **ad landing pages stay here.** They serve a different job (paid traffic, one
per medium) and they do not need to live on the client's domain.

### Blocked on

- [ ] **Nathan's reference sites.** He is sending examples of what he likes.
      Nothing gets designed until they arrive — see the standing note above:
      get URLs, not adjectives.
- [ ] Decision on which of the six existing URLs survive (below).

### Scope question raised 2026-08-24 — NOT yet settled

Edward: Nathan "doesn't really care about having the gallery. Maybe not even
have meet the team."

⚠️ **Dropping a page drops its Google URL.** `/meet-the-team` is their deepest
page at ~734 words and holds the entire family story — Stewart on the tools at
17, the Olympic judo careers, Frank's 17 years. `/gallery` carries the seven
named projects.

**Recommendation: keep both URLs, slim the content.** A thin page preserves the
address for near-zero effort. Deleting later is easy; recovering a dropped URL is
not. Confirm with Nathan rather than assuming — it is a five-second question in
the same conversation as the reference sites.

Full URL and software mapping: `docs/tasks/site-migration-map.md`.

### Why two repos and not one — the technical reason

Asked and settled 2026-08-24.

**One repo = one GitHub Pages site = one custom domain.** Subfolders are possible
(`/lp/rebuild/`), two separate sites from one repo are not.

⛔ **The real reason is publication, not tidiness. GitHub Pages serves every file
in the repo.** If the AI testimonial videos and AI team photo live in the same
repo the domain points at, they are reachable at
`sabreconstructions.com.au/assets/video/testimonial-1.mp4` whether or not any
page links to them. **Unlinked is not unpublished.** That alone rules out one
shared repo while `open-items.md` items 1 and 7 are unresolved.

**Promotion between them is a manual copy**, not a link or a submodule. When a
landing page earns its place on the real site, copy the finished page across.
Manual is the feature — it forces a decision each time instead of letting demo
content drift onto the client's domain.

**Future option, not needed yet:** a second custom domain such as
`ads.sabreconstructions.com.au` can point at this repo, putting the ad landing
pages on Sabre's own domain. Better for ad quality scores, since ad and landing
page would share a domain. Revisit only if ad performance argues for it.

### 2026-08-24 — Sabre to get their own fal.ai account

Edward will ask Nathan to open a **fal.ai account and put credit on it**, so
image and video generation runs on Sabre's billing, not BBL's.

**Why it matters beyond cost.** `reference/bbl-links.md` currently sources
`FAL_KEY` from `BBL/products/image-pipeline/.env`. That is a hard dependency on
Edward's infrastructure — fine now, worthless after handover. Their own account
removes it, same principle as putting the form service in their name.

**Cost anchor for the conversation:** the 16.5s knockdown-rebuild clip cost
**$2.97** end to end. A hundred dollars of credit goes a long way. Use the real
number — it stops the ask feeling open-ended.

⚠️ **A fal 403 means the balance is exhausted, not that the key is wrong.** Tell
Nathan up front. See [[fal-access]].

⛔ **The key never enters this repo — it is public.** Environment file only.

**What their account is legitimately for:**

- `recraft/upscale/crisp` on their real photos — non-generative, so it cannot
  invent architecture. Their gallery thumbs are 376px and need it
- Before/after visualisations built from their own photo of a real block, camera
  locked, using a design they own

**What it must never do**, now that nobody is supervising the account: invent a
finished house from a design Sabre does not own (open item 6), or put a person on
a page. Both are written into `site/docs/rules.md` as rules 3 and 7 so the rule
travels with the repo instead of living in Edward's head.

### ✅ 2026-08-24 — SENT: "One thing to find out for me"

Emailed **nathan@sabreconstructions.com.au**, delivery confirmed. Asks **one
question only**: who does Sabre contact about the domain — **iSonic** or
**Melbourne IT** — and send the login if he has one.

Everything DNS now waits on that reply. This supersedes the 2026-08-17 "To do"
email, which asked for the same access alongside Meta and Google Ads and got no
response.

**Deliberately NOT asked yet, will follow separately:**

- [ ] **fal.ai account + credit.** Cost anchor for the ask: the 16.5s rebuild
      clip cost **$2.97**. A fal 403 = exhausted balance, not a bad key
- [ ] **Formspree account in Sabre's name**, for the enquiry form. Must be their
      account so it survives handover — see `site-migration-map.md`

Both were held back on purpose. The sent email asks one thing, which is why it
has a chance of being answered.
