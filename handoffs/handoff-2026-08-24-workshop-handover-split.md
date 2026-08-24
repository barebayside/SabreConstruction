# Handoff — 2026-08-24 — Split the workshop from the handover site

## Session Focus

Nathan sent through a Joomla login. Working out what that login actually
controls led to mapping who runs Sabre's domain, DNS, hosting and email — and
from there to a much bigger reframe: **the end goal is handing the website repo
to Nathan so his own AI can maintain it.** That decision reshaped the structure.

## What Got Done

**Established who runs what** (all verified live, not assumed):

| Layer | Provider |
|---|---|
| Registrar | **Melbourne IT** (domain last modified 2026-08-15) |
| DNS + web hosting | **iSonic** — `ns1/2/3.isonicsites.com`, `103.26.236.198` (`hyperspeed.isonic.io`), LiteSpeed |
| CMS | **Joomla** + YOOtheme template |
| Email | **Microsoft 365** — MX → `sabreconstructions-com-au.mail.protection.outlook.com` |

- The Joomla login Nathan sent is the **website editor only**. It has no control
  over DNS. Its username is **Cathy's address**, so anything edited in there
  looks like Cathy did it.
- `.com.au` registrant details are redacted from public lookup, so **who owns the
  domain is still unknown** and can only be answered by Sabre logging into
  Melbourne IT.

**Crawled the live site** — six pages, all 200, no `sitemap.xml`:
`/` · `/contact` · `/designs` · `/gallery` · `/meet-the-team` · `/testimonials`
~2,250 words total. Every page shares one meta description, the string
"Sabre Construction". Titles say "Construction" singular; the business is plural.

**Built the handover site skeleton** — `site/`, deliberately self-contained:
six page stubs at the **same six URLs**, own stylesheet and assets, `CLAUDE.md`
plus five docs (client-facts, rules, design-system, how-it-works,
making-changes) written for a non-developer and for whatever AI Nathan uses.

**Built `review/index.html`** — one link to send Nathan, splitting "the website"
from "ad concepts" so he stops being told which tabs to ignore.

**Wrote two task contracts** — `docs/tasks/dns-cutover.md` (exact records, SEO
carryover) and `docs/tasks/site-migration-map.md` (what replaces what, lead
capture without Zoho). Both added to the routing table.

**Collapsed duplicate docs to one source** — see Decisions 6.

**Zoho drafts** — four written, three deleted, one refined down to a single
question. ✅ **SENT 2026-08-24**, delivery confirmed:
*"One thing to find out for me"* to `nathan@sabreconstructions.com.au`.
Asks only who to contact about the domain. The fal.ai and Formspree asks were
deliberately held back so this email asks one thing.

## Files Changed / Created

⚠️ **Committed to `main` (`618c9b6`, `77be4cc`). NOT pushed.**

| Path | What |
|---|---|
| `site/` (13 files) | NEW. Handover website + CLAUDE.md + 5 docs |
| `review/index.html` | NEW. Client review index, two clearly-labelled sections |
| `docs/tasks/dns-cutover.md` | NEW. DNS records, mail records to protect, SEO checklist |
| `docs/tasks/site-migration-map.md` | NEW. Software swap, URL map, lead capture |
| `docs/reference/client-facts.md` | Now a **pointer** — content moved to `site/docs/` |
| `docs/reference/design-system.md` | Palette/type removed; keeps demo components + motion |
| `CLAUDE.md` · `CONTEXT.md` · `docs/CONTEXT.md` | Routing repointed, 2 new task rows |
| `docs/engagement.md` | Fresh-repo decision, two-repo rationale, fal.ai plan |
| `docs/open-items.md` + 4 task contracts | Stale pointers repaired |
| `.gitignore` | `docs/emails/` excluded — repo is public, drafts carry staff addresses |
| `docs/emails/` (3 files) | Local only, gitignored. Email drafts + reasoning |

## Decisions Made

1. **The real website gets a fresh repo**, not an evolution of this one. This
   repo stays the workshop: demo, ad concepts, LPs, `tools/`. → `engagement.md`
2. **Two repos, not one.** Not tidiness — **GitHub Pages serves every file in the
   repo.** AI testimonial videos in the same repo as the live site would be
   reachable at `sabreconstructions.com.au/assets/video/testimonial-1.mp4`
   whether or not anything links them. Unlinked ≠ unpublished. → `engagement.md`
3. **Build the website inside this repo at `site/`, promote when finished.**
   Previews at `…/site/`, so Nathan approves the real thing before DNS moves.
4. **`site/` must be self-contained.** Nothing reaches above it — that is what
   makes promotion a clean folder lift and stops AI assets travelling.
5. **Formspree for the form, in Sabre's account.** Reversed an earlier Catalyst
   recommendation once handover became the goal: a Catalyst function would leave
   Sabre's leads flowing through Edward's infrastructure forever. Chosen over
   Web3Forms/FormSubmit despite smaller free tier **because it keeps a copy** —
   forward-and-forget loses a six-figure lead with no record.
   → `site-migration-map.md`
6. **One source of truth.** `site/docs/client-facts.md` and
   `site/docs/design-system.md` are canonical; workshop copies became pointers.
   Design system split rather than merged — the workshop file still owns the
   demo's motion engine and components, which `site/` does not have.
7. **Sabre gets their own fal.ai account.** Removes the `FAL_KEY` dependency on
   `BBL/products/image-pipeline/.env`. → `engagement.md`
8. **Rule 7 added to the handover docs** — generated imagery of buildings.
   Written down precisely because after handover nobody supervises that account.

## Resolved failures

**Zoho Mail sidebar showed no Drafts folder.** Root cause: **the left folder pane
goes stale** — Drafts, Outbox and custom folders all missing at once while
existing fine. A **page refresh** fixed it. Wasted several exchanges hunting a
per-folder visibility setting that does not exist; the only checkbox on
Settings → Folders is "View in IMAP client", which is unrelated. Recorded in
[[zoho-mail-account-id]].

**Drafts came out with a typed sign-off instead of Edward's signature.** Root
cause: `ZohoMail_sendEmail` has `includeSignature`, default `false`, html only.
Fixed by passing `includeSignature: true` and ending the body at "Cheers,".
Also confirmed: there is no `createDraft` tool — use `mode: "draft"`. Recorded in
[[zoho-mail-account-id]] along with the folder IDs.

**Nearly leaked staff addresses into a public repo.** Root cause: wrote email
drafts into `docs/`, which is tracked, in a repo that is public. Caught before
any commit. Fixed with `.gitignore`.

**Collapse left seven dead pointers.** Root cause: moved the canonical files
without sweeping for references. Caught by a pre-commit grep. All repaired —
worth repeating that sweep after any future move.

## What's NOT Done — TODO

### Blocked on Sabre
- [x] ~~Who to contact about the domain — iSonic or Melbourne IT.~~ **ASKED
      2026-08-24.** ⏳ Awaiting reply. Everything DNS waits on it
- [ ] **Does Sabre own their own domain?** Registrant is redacted. Only a
      Melbourne IT login answers it. Ask early — easier while relations are good
- [ ] **Reference sites — actual URLs, not adjectives.** All design work blocked
- [ ] **Keep or drop `/gallery` and `/meet-the-team`?** Nathan indicated he may
      not want them. ⚠️ Recommendation on record: **keep the URLs, slim the
      content.** Deleting a page drops its Google address
- [ ] Google Ads account · real team photo · first filmed build
- [ ] fal.ai account with credit (cost anchor for the ask: the 16.5s rebuild clip
      cost **$2.97**)

### Ours — blocking go-live
- [ ] ⛔ **Wire the lead form.** Currently shows success and sends nothing
      (open item 2). Cutting over before this is fixed loses every enquiry
      silently. **First job, above everything else**
- [ ] ⛔ Replace AI testimonial videos (item 1) and AI team photo (item 7)
- [ ] ⛔ Strip `noindex` from `site/` at promotion. **Left on, Sabre disappears
      from Google entirely** — the biggest single risk in the whole cutover
- [ ] Build the six real pages; `/designs` has nothing at all yet
- [ ] Add `sitemap.xml` — they have never had one
- [ ] Titles must use **Constructions**, plural. Real meta description per page

### Not started
- [ ] Meta + Google campaign structures (unblocked, could start any time)
- [ ] BBL asset-line registration for this site — deliberately not invented;
      run the `bbl-asset-code` skill properly when wanted

## Quick Context for Next Session

**Project:** `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`

**Read first:** `CLAUDE.md` → `docs/engagement.md` → `docs/open-items.md`.
For the switch-over: `docs/tasks/dns-cutover.md`. For structure:
`docs/tasks/site-migration-map.md`.

**Most likely next task:** Nathan replies with reference sites → design the real
pages into the `site/` stubs. The skeleton, the URLs and the rules are already
correct, so that work starts on a sound base.

**Fastest path to done if he goes quiet:** wire the lead form (Formspree, ten
minutes) and build `/designs`, which has no content at all. Neither needs
anything from Sabre.

**The one thing not to get wrong:** their **email is Microsoft 365 running off
iSonic's DNS zone**. At cutover, change only the website records. Never move
nameservers, never let anyone tidy the zone. Everything else in this job is
reversible; broken mail is the one that actually costs them.
