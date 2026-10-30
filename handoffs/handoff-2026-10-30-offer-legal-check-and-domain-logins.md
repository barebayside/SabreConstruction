# Handoff 2026-10-30: offer legal check, domain logins

## Session Focus
Check the 2027 build-slots offer against Australian/Qld law; plan moving the domain off iSonic (Nathan present).
Side task for BBL: scan published Claude skills for ad/landing-page design (parked design playbook).

## What Got Done
- **Legal check of the offer:** `marketing/pushes/2026-10-29-2027-build-slots/03b-legal-check.md`. Verdict: legal as
  designed if every claim is true. Biggest risk = "demolition included" silent on **asbestos**. Also: QBCC licence
  name + number on every ad; "worth $X" = Sabre's real price; real cap and deadline; bonuses written into the
  contract; cooling-off + 5% deposit cap untouched; referral fees to brokers/architects only if disclosed (secret
  commissions); unfair trading practices law starts 1 July 2027. Official sources only, not a lawyer's sign-off.
- `03-offer.md`: questions 9–10 added for Nathan (exact licensee name; what demolition covers).
- **Domain:** live lookup confirmed registrar Melbourne IT, DNS + web = iSonic, **email = Microsoft 365** (not iSonic).
  Agreed with Nathan in person: he gets the iSonic login and the Microsoft 365 admin login; Edward then moves DNS to
  a host he manages (copy every record first, keep all mail records), then cuts the site over.
- **BBL:** skill scan noted under the parked design playbook item in BBL `docs/next/BBL.md`. No agency publishes
  design rules as a skill; packs are good for layout names only.

## Files Changed
- `marketing/pushes/2026-10-29-2027-build-slots/03b-legal-check.md` (new)
- `marketing/pushes/2026-10-29-2027-build-slots/03-offer.md` (Q9–10)
- `NEXT.md` (step 1 = Nathan getting logins; domain question removed from "still to ask")
- BBL `docs/next/BBL.md` (parked design playbook: skill scan note)

## What's NOT Done
- Logins not received yet. `docs/tasks/dns-cutover.md` still says "never move nameservers" (old plan); update it at
  the move.
- Nathan's answers to offer questions 1–10.

## Quick Context for Next Session
NEXT.md updated. When the logins arrive: export the iSonic zone, recreate every record at the new host, check mail
still flows, then switch nameservers and transfer the registration.
