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
