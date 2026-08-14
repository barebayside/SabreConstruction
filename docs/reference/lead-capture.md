# Lead capture

> **Layer 4.** Canonical source for the qualifying form. Code lives in
> `js/qualify.js`; this file explains why it's built that way.

## The five questions

Set by Edward. Order matters — easy first, phone number last.

| # | Question | Type |
|---|---|---|
| 1 | What are you looking to do? | Tap · Knockdown rebuild / House raise / Renovation or bathroom reno / Not sure yet |
| 2 | Do you have plans drawn? | Tap · Yes, done / Started, not finished / No, not yet |
| 3 | Where's the block? | Type · suburb |
| 4 | Roughly what budget? | Tap · ⚠️ see below |
| 5 | Best mobile to reach you on? | Type · `inputmode="tel"` |

**Only two of five need typing.** Everything else is a 56px-minimum tap target.

## ⚠️ The budget bands are placeholders

Currently: Under $300k / $300–450k / $450–650k / $650k+ / Still working it out.

**Nobody has confirmed these against Sabre's real job sizes.** A bathroom reno
and a knockdown rebuild aren't remotely the same range. Getting them wrong either
scares off good leads or fills the pipeline with people who can't afford it.

## Why five screens, not one form

Five fields on a single screen costs 10–25% of completions at this count. So:
one question per screen, progress bar, back button, sensitive field last. That's
straight out of the form-CRO methodology.

## Inline vs modal

`js/qualify.js` drives **two hosts off one state machine with shared answers**:

- **Inline** — `<div data-qualify-inline></div>` renders open on question one.
  This is the primary. No click needed.
- **Modal** — fallback only. Fires if someone reaches the bottom of the page
  without having touched the form, and never once they've started.

A `[data-qualify]` button scrolls to the inline form and flashes it rather than
stacking a modal over the identical thing.

## ⚠️ Where the leads go

GitHub Pages has no server, so the form posts to a relay which emails the lead on.

**One line controls it:**

```js
var LEAD_EMAIL = 'edasturner@gmail.com';   // js/qualify.js
```

It points at **Edward, not Sabre**. Real leads must not land in a client's office
inbox before they've agreed to any of this. Sabre's real address is in
`client-facts.md` for when that changes.

The relay sends one confirmation email on the first submission. Until someone
clicks the link in it, **nothing arrives anywhere.**

If this goes live properly, Zoho Forms is the better home — that's Edward's stack.

## What gets sent

`project_type`, `has_plans`, `suburb`, `budget`, `mobile`, plus `page`,
`landing_page`, `referrer`, `fill_seconds`, and any UTM / `fbclid` / `gclid`
present on the URL.

## The three Meta routes

The same five questions can be asked in three places. Which one is set by the
campaign objective, not by design choice. `ads.html` shows all three side by side.

| Route | Where the questions appear | Trade-off |
|---|---|---|
| Instant Form | Inside Facebook/Instagram, profile-prefilled | Cheapest leads, lowest intent — they never see the page |
| Click to Message | Messenger/WhatsApp, tappable buttons | Costs more, quality higher |
| Landing page + form | Our pages | Recommended. Page builds trust, form qualifies |

Meta's own figure: instant forms **and** Messenger together give ~8% lower cost
per lead and 48% more reach than instant forms alone.
