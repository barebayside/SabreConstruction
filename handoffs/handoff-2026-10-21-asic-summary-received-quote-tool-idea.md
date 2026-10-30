# Handoff — 2026-10-21 — ASIC summary received and checked; quote-tool idea parked

## Session Focus
Nathan's ASIC document arrived. Checked it against Google Ads advertiser verification rules.
Edward also floated an AI "quote machine" for Sabre on Catalyst. Discussed it, then dropped it.

## What Got Done
- **Found Nathan's email** "Fw: asic" (20 Oct, from nathan@, forwarding Cathy's) in edward@ inbox.
  The Zoho Mail connector cannot download attachments. Edward saved the PDF to Downloads.
- **Moved the PDF** to `docs/company-docs/sabre-asic-extract.pdf`.
- **Read it.** It is an ASIC "Company Summary" (free database extract, 20/10/2026), NOT the
  Certificate of Registration:
  - SABRE CONSTRUCTIONS QLD PTY LTD · ACN 673 587 472 · ABN 29 673 587 472
  - Registered 12/12/2023 · status Registered · next review 12/12/2026
  - Registered office locality: **Yeerongpilly QLD 4105** (not Ransome; probably the accountant)
- **Checked Google's rules (AU):** org document = "Certificate of Incorporation or Registration"
  (ABN may also be given) + government photo ID of an account/payments-profile admin. Details must
  "exactly match your payments profile info". Mismatch or missing info = the usual failure. Each
  check can take up to 5 working days. Source: support.google.com/adspolicy/answer/9872280
- **Answered the quote-machine question** (Catalyst Data Store price sheets + function + Claude API,
  Nathan talks to it by voice/photo/chat). Design rule given: Claude reads and itemises, code does the
  sums from Sabre's own rate table, never an invented rate. Pitfalls covered: audio needs
  speech-to-text first, stale rates, 300-row query cap, ~30 s / 512 MB function limits (empty 200 on
  OOM), browser CORS trap, dev 5,000-row cap, must sit behind a login.

## Files Changed / Created
| Path | What |
|---|---|
| `.gitignore` | Added `docs/company-docs/`. Committed locally (3e6928d), **not pushed** |
| `docs/company-docs/sabre-asic-extract.pdf` | The ASIC summary. Gitignored, verified with `git check-ignore` |
| `NEXT.md` | Item 1 records the summary + entity; "Waiting on Edward" now asks for the real certificate + licence |

## Decisions Made
1. **The company is SABRE CONSTRUCTIONS QLD PTY LTD** (ABN 29 673 587 472), the one Nathan sent. Not
   the older Sabre Constructions (ABN 29 107 425 703). Recorded in `NEXT.md` item 1.
2. **Plan A = the real Certificate of Registration; the summary is the fallback.** Recorded in `NEXT.md`.
3. **Company documents live in `docs/company-docs/`, gitignored.** The repo is public.
4. **Quote machine: NOT pursued.** Edward: good idea, no time. If revived, it would run on Sabre's own
   Catalyst and Anthropic key, and start with a paper test (price sheet + 3 past quotes). Not added to NEXT.md
   at Edward's request ("leave it as is").

## What's NOT Done
`NEXT.md` updated.

## Quick Context for Next Session
- Project: `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`. Read `CLAUDE.md` → `NEXT.md`.
- Most likely next: once Nathan sends the certificate + licence, check the Google Ads payments
  profile is **Organisation** with the name exactly **SABRE CONSTRUCTIONS QLD PTY LTD**, then get his
  Customer ID → `/bbl-google-ads-link` → advertiser verification.
- The ABN Lookup PDF in Downloads (ABN 25 611 087 373) is **Oodles of Paws**, not Sabre. Ignore it.
