# Task — migration map: what replaces what

> **Layer 3 task contract.** Written 2026-08-24. Read this together with
> `dns-cutover.md`, which covers the DNS switch itself and the SEO checklist.
>
> This file answers two questions: **which software gets replaced by what**, and
> **which URLs must exist on the new site so Google doesn't drop them.**

## Part 1 — the software swap

| What they use now | Who runs it | What replaces it | Do they still pay? |
|---|---|---|---|
| **Joomla** (CMS) | free software on iSonic's server | plain HTML files in this repo | no |
| **YOOtheme** (Joomla template) | bundled with the above | `css/sabre.css` | no |
| **iSonic** (web hosting) | iSonic | **GitHub Pages** | ⛔ **no — this is the bill that goes away** |
| **iSonic** (DNS) | iSonic | ⚠️ **stays with iSonic** — we only edit records | probably, small |
| **Melbourne IT** (domain name) | Melbourne IT | **stays** — unchanged | yes, annual |
| **Microsoft 365** (email) | Microsoft | **stays** — untouched | yes |
| **Google Business Profile** | Google | **stays** — untouched | free |
| Joomla contact form | iSonic mail relay | ⛔ **NOT YET BUILT** — see open item 2 | — |

⚠️ **Two of these often get confused.** iSonic do two separate jobs: they *host
the website* (goes away) and they *run the DNS* (stays, unless the nameservers
are moved). Killing the hosting does not automatically kill the DNS.

⛔ **The contact form is the live gap.** Their current Joomla site has a working
contact form that sends through iSonic. Ours (`js/qualify.js`) has no endpoint —
it shows success and sends nothing. **Cutting over before this is wired means
every enquiry from that day is lost silently.** Open item 2.

## Part 2 — the URL map

Their live site is **six separate pages**. Our build is **one long page with
sections**, plus demo-only extras. That mismatch is the whole indexing risk.

| Live URL (must keep working) | What we have now | Gap |
|---|---|---|
| `/` | `index.html` | ✅ fine |
| `/contact` | `#start` section on index | ⛔ needs a real page at `/contact/` |
| `/designs` | nothing | ⛔ **nothing exists.** Their 2nd-deepest page (~625 words) |
| `/gallery` | "Have a look around" section on index | ⛔ needs a page at `/gallery/` |
| `/meet-the-team` | `team.html` | ⚠️ exists but at the wrong address, and the photo is AI |
| `/testimonials` | `#voices` section on index | ⛔ needs a page, and the videos are AI |

**GitHub Pages cannot do server-side redirects.** So we do not redirect — we
build a folder with an `index.html` at each of those exact paths. `/contact/` is
the file `contact/index.html`. Do that and no link ever breaks.

A section on a long page is **not** a substitute for a page. `/designs` as an
anchor `#designs` is a different URL, and Google drops the old one.

## Part 3 — pages that must NOT ship

These are demo and review scaffolding. They were built to win the job, not to be
a real builder's website.

| File | What to do |
|---|---|
| `ads.html` | internal only — keep `noindex`, remove from public nav |
| `lp-rebuild.html` · `lp-raise.html` · `lp-story.html` | ad landing pages — keep `noindex`, keep out of nav and sitemap |
| `rebuild-render.html` | ⛔ blocked by open item 6 — another practice's design |
| `team.html` | ⛔ AI people. Rebuild at `/meet-the-team/` with the real photo |

## To do — in order

### Before anything else
- [ ] Wire the lead form to a real address (open item 2). Nothing ships without it
- [ ] Replace the AI testimonial videos (open item 1)
- [ ] Replace the AI team photo (open item 7)

### Build the missing pages
- [ ] `contact/index.html` — must carry the real phone, address, hours, QBCC
      licence 328475 from `../../site/docs/client-facts.md`
- [ ] `designs/index.html` — nothing exists yet. Their design range: Alexander,
      Belmont, Chelsea, Waderbird
- [ ] `gallery/index.html` — projects: Brighton, Clarence, Alexandra,
      Killarney 78, Killarney 79, Clapton, Marcoola
- [ ] `meet-the-team/index.html` — the real six, real photo
- [ ] `testimonials/index.html` — the ten real Google reviews already cleared in
      `../../site/docs/client-facts.md`. **4.5 from 11, never rounded to 5**

### Then, and only then
- [ ] Strip `noindex` from the six public pages
- [ ] Add `sitemap.xml` — they have never had one
- [ ] Follow `dns-cutover.md`

## Notes

- Every asset path in this repo is **relative**, so pages in subfolders need
  `../` prefixes on their CSS, JS and image links. Check each one after moving.
- Their current titles read "Sabre Construction" **singular**. The business is
  "Sabre Construction**s**". Fix it on the new pages.
- Every current page shares one meta description: the string "Sabre Construction".
  Write a real one per page — it is free ranking.

---

# Lead capture without Zoho

Decided 2026-08-24. This site sits **outside the BBL Zoho universe** — it is a
website / blogging / ranking asset, not a CRM funnel. So no ZMA, no Catalyst
inbound capture, no CRM writes.

## The problem

GitHub Pages serves static files. There is **no server**, so a form has nowhere
to post to. It needs a third-party endpoint that receives the post and emails it
on to `admin@sabreconstructions.com.au`.

## Recommendation: Formspree

| Service | Free tier | Keeps a copy? |
|---|---|---|
| **Formspree** ✅ | 50 submissions/month | **yes — dashboard archive** |
| Web3Forms | ~250/month | ⛔ no. Email forward only |
| FormSubmit | unlimited | ⛔ no. Email forward only |

**Take the smaller free tier for the archive.** Web3Forms and FormSubmit forward
and forget: if the email bounces, lands in junk, or Microsoft eats it, the lead is
gone with no record anywhere. One Sabre lead is potentially a $500k build. A
second copy is worth more than 200 extra monthly submissions they will never use.

50/month is comfortably above a Bayside builder's enquiry volume. If it is ever
exceeded, the paid tier is cheap and the decision can be revisited then.

⚠️ **`docs/reference/lead-capture.md` currently points at
`edasturner@gmail.com`.** Leads go to Edward until Sabre agree the handover —
that decision is in `open-items.md`. Switch to `admin@sabreconstructions.com.au`
at cutover, not before.

## Non-negotiable: prove it actually arrives

Open item 2 exists because the current form **shows success and sends nothing**.
That failure must not be rebuilt.

- [ ] Submit a real test enquiry end to end and confirm the email lands
- [ ] Confirm it is not in junk — a first-time sender to Microsoft 365 often is.
      Whitelist the sending domain
- [ ] Confirm the Formspree dashboard shows the same submission
- [ ] Break it on purpose — wrong endpoint — and confirm the page shows an
      **error**, not a success message
- [ ] Add a honeypot field. Builders' forms attract spam

See [[verify-data-arrived]]: an empty inbox and a broken form look identical.

## Click to call

Already working in the demo topbar. Use the **international format** — more
reliable across handsets and it survives roaming:

```html
<a href="tel:+61738233200">07 3823 3200</a>
```

Display the friendly local number, dial the international one. Already applied in
the `site/` scaffold header and footer.

Worth adding a sticky call bar on mobile — for a trade, a thumb-reachable phone
number usually beats a form.
