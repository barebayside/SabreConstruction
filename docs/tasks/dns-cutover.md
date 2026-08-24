# Task — point sabreconstructions.com.au at GitHub Pages

> **Layer 3 task contract.** Read this when the domain is being moved off iSonic's
> Joomla site onto the GitHub Pages build. Written 2026-08-24.
>
> ⛔ **DO NOT RUN THIS YET.** The 🔴 items in `open-items.md` must be cleared
> first — AI testimonial videos, AI team photo, invented budget bands, dead lead
> form. The moment this domain resolves to the GitHub site, those stop being demo
> caveats and become a real builder's live commercial website.

## Inputs

| Need | Where |
|---|---|
| iSonic hosting login (or Sabre emails them) | Blocked on client — `engagement.md` |
| Repo admin on `barebayside/SabreConstruction` | Edward has it |
| Org admin on the `barebayside` GitHub org | Edward has it |

## Current state (verified 2026-08-24)

| Layer | Provider | Detail |
|---|---|---|
| Registrar | **Melbourne IT** | Domain last modified 2026-08-15 |
| Nameservers | **iSonic** | `ns1` / `ns2` / `ns3.isonicsites.com` |
| Web host | **iSonic** | `103.26.236.198` (`hyperspeed.isonic.io`), LiteSpeed |
| CMS | **Joomla** | YOOtheme template |
| **Email** | **Microsoft 365** | MX → `sabreconstructions-com-au.mail.protection.outlook.com` |

⛔ **Email is the risk in this whole job.** It runs off the same DNS zone as the
website. Change the web records only. Never move nameservers, never let anyone
"tidy up" the zone.

Records that must survive untouched:

```
MX    0   sabreconstructions-com-au.mail.protection.outlook.com
TXT       v=spf1 ip4:103.26.236.198 +a +mx include:spf.protection.outlook.com
          +ip4:101.0.92.234 +ip4:116.90.5.98 include:relay.mailchannels.net ~all
TXT       MS=ms84618357
```

(The SPF entry for `103.26.236.198` goes stale once the site leaves iSonic, but
it is harmless. Leave it. Cleaning it up is a separate job with its own risk.)

## The records to change

Fixed public GitHub values — not generated, safe to send in advance.

**A records on the bare domain** — these REPLACE the single existing A record:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**AAAA records** (optional, IPv6 — GitHub recommends A *in addition to* these,
not instead of):

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**CNAME for www** — currently a CNAME to the bare domain, repoint it:

```
www  CNAME  barebayside.github.io
```

## Domain verification TXT — generated, optional, recommended

Name format: `_github-pages-challenge-barebayside.sabreconstructions.com.au`

The value is unique to the org and only appears in the GitHub UI:
**Org settings → Pages → Add a domain** → enter the domain → copy the line shown.

Without it the site still works, but the domain can be taken over by another
GitHub account if this repo is ever deleted, moved, or the plan downgraded.

## Sequence

1. **Repo** → Settings → Pages → Custom domain → `sabreconstructions.com.au` →
   Save. GitHub auto-commits a `CNAME` file to the root of `main`.
2. **Org settings** → Pages → Add a domain → copy the generated TXT line.
3. **Email iSonic** the A records, the www CNAME, and the TXT line — with the
   explicit instruction to leave every MX and mail-related TXT record alone.
4. **Wait.** Usually 1–2 hours, occasionally up to 24.
5. **Repo** → Settings → Pages → tick **Enforce HTTPS**. Only after step 4 —
   GitHub must see working DNS before it can issue the Let's Encrypt certificate.
6. Strip `noindex` and the preview chrome — `open-items.md` 🟡 section.

## Notes

- **All asset paths in this repo are relative** (`css/…`, `assets/img/…`), so
  moving from `barebayside.github.io/SabreConstruction/` to the domain root
  breaks nothing. Verified 2026-08-24.
- **Leave the Joomla site in place** until the new one is proven live. The DNS
  change is reversible — point the A record back at `103.26.236.198` and the old
  site returns.
- iSonic are the party losing this hosting business. Expect delay if the request
  is routed through them rather than done directly with their login.

---

# Search rankings — what carries over and what can be lost

> Measured against the live Joomla site 2026-08-24. Redo the crawl before cutover
> in case they've added pages.

## The short answer

**The domain does not change, so the ranking history does not reset.** Google
attaches reputation to `sabreconstructions.com.au`, and that stays exactly as it
is. This is nothing like moving to a new domain name.

**Their Google Business Profile is untouched** — 4.5 stars from 11 reviews,
place ID `ChIJBSdvy4ldkWsRML7s7-J9F2c`. For a local builder that listing drives
most of the "builder near me" visibility, and it has no connection to the
website's hosting.

## The one real risk: URLs that stop existing

If a page Google has indexed returns "not found" after the switch, Google drops
it. That is the only mechanism by which rankings actually disappear here.

**GitHub Pages serves static files and cannot do server-side 301 redirects.** So
the fix is not to redirect — it is to *keep the same addresses*. Each old path
becomes a folder with an `index.html`, e.g. `/contact/` → `contact/index.html`.

## The complete live URL list — all six must survive

Crawled 2026-08-24. All return 200. There is **no `sitemap.xml`** (404).

| Path | Title | Depth |
|---|---|---|
| `/` | Home - Sabre Construction | ~279 words |
| `/contact` | Contact - Sabre Construction | ~138 words |
| `/designs` | Designs - Sabre Construction | ~625 words |
| `/gallery` | Gallery - Sabre Construction | ~284 words |
| `/meet-the-team` | Meet The Team - Sabre Construction | ~734 words |
| `/testimonials` | Testimonials - Sabre Construction | ~187 words |

`robots.txt` exists and is stock Joomla — only blocks `/administrator/` and
friends. Nothing of value is disallowed.

## How little is actually at risk

The whole site is roughly **2,250 words across six pages**. Every single page
carries the identical meta description, the string `Sabre Construction`. There is
no sitemap. The titles say "Sabre Construction" **singular** while the registered
business is "Sabre Construction*s*" plural.

That is a thin site with no on-page optimisation. The realistic outcome of the
rebuild is that rankings **improve**, not slip. Say this to Sabre honestly — but
do not use it as a reason to be careless with the six URLs.

## Cutover SEO checklist

- [ ] Re-crawl the live site immediately before switching; confirm the URL list
- [ ] Every old path exists on the new site at the same address
- [ ] Titles are at least as specific as the old ones — and use **Constructions**
- [ ] Real meta descriptions per page, not one repeated string
- [ ] Add a `sitemap.xml` (they have never had one)
- [ ] ⛔ Strip `<meta name="robots" content="noindex, nofollow">` from every page
      — see the 🟡 section of `open-items.md`. Leaving it on is the one change
      that WOULD delete them from Google
- [ ] Claim the property in Google Search Console and submit the sitemap
- [ ] After cutover, watch Search Console coverage for 404s for a fortnight

⛔ **The `noindex` tag is the real danger, not the DNS change.** Every page of the
GitHub build currently carries it. Switching the domain over with those tags still
in place would remove Sabre from Google entirely — which is the exact outcome this
section exists to prevent.
