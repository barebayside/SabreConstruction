# Content — drafts written to be built into the real site

> **What this folder is.** Finished page copy, written but not yet built into HTML. The plan it
> comes from is `docs/reference/search-and-ai-visibility-plan.md` (§7 the article bank, §8 the
> fixes to live pages). The build step turns these into pages in the **real** repo
> (`Desktop/sabre-constructions-website`).
>
> **Why drafts live here and not there.** Both repos are public, but only the real one will have
> `sabreconstructions.com.au` pointed at it. Unlinked is not unpublished. Nothing reaches the
> client's domain until it is finished, code-scaffolded and checked.

## The folders

```
content/
  pages/     copy for site pages (service page, suburb pages)
  posts/     copy for "Your questions answered" articles
  patches/   changes to pages that are ALREADY LIVE — what to edit, not a rewrite
```

## Every file has front matter

```yaml
title:           the <title> and the H1 (a post's title IS the question it answers)
slug:            the URL segment
description:     the meta description, under 160 characters
type:            page | post | patch
registry_code:   TBC — assigned by /bbl-asset-code at scaffold time. Never invent one here.
targets:         the searches this is written for (from the 09-05 rank data)
status:          draft | ready | blocked
blocked_on:      what must arrive before it can publish
sources:         every external fact, with its source
gaps:            the ⛔ GAP markers in the body, listed
```

## ⛔ GAP markers — read this before building anything

A block that looks like this:

```
⛔ GAP — Nathan: ...
```

is **a hole, not copy.** It marks a place where the page needs something only Nathan can supply:
a real job, a real number, a confirmation of how Sabre actually works. Rule 1 and
`docs/reference/positioning.md` both say these are drafts until he says so.

**The build must either fill a gap or cut the section. A GAP marker must never reach a page.**
The build script should refuse on finding the string `⛔ GAP` in anything it is about to write.

## The rules these were written under

1. **No invented numbers.** No price, no band, no build duration, no job count. Every fact is in
   `site/docs/client-facts.md` or is attributed to a named outside source on the page.
2. **No claim about how Sabre operates** unless it is confirmed. The unconfirmed ones are listed
   in `docs/reference/positioning.md`; each appears here inside a GAP marker or not at all.
3. **The licence number stays off new pages.** Their contact page says QBCC 328475, the 2026
   signage says 15486557. Until Nathan says which is which, new copy says "QBCC licensed" and
   the footer keeps the number it already has.
4. **Voice:** `docs/reference/copy-rules.md`. Plain Australian, second person, contractions,
   short paragraphs. The builder at the kitchen table, not the brochure.
5. **Shape:** the Project 24 / Income School method — one question per page, the answer in the
   first 60 words, a self-contained 134–167 word block near the top, H2s written as questions,
   a "Common questions" block at the end, **one** call to action.

## What the build step does (not done yet)

1. `/bbl-asset-code` scaffolds a registry record per file → the real code goes in the front matter.
2. Markdown → the site's page template (header, footer, floating button, the closing block).
3. Add per the plan §4: `<link rel="canonical">`, `Article` schema with author + dates, the visible
   byline and date, alt text on every image.
4. Add the URL to `sitemap.xml` with `lastmod`; add the internal links named in each file.
5. Bump `?v=` on `site.css` in every page touched.
6. `node --check` any page script; screenshot at 1400 and 500 wide.
7. Refuse if `⛔ GAP` survives anywhere.

## Order to build

Everything except the suburb pages can be built as soon as Nathan clears the claims it names.
The suburb pages are last because they are the ones that need his local detail most.

| # | File | Why this order |
|---|---|---|
| 1 | `patches/live-post-fixes.md` | Two pages are already live and weakest where it is cheapest to fix |
| 2 | `pages/knockdown-rebuild.md` | The service page the ads and the suburb pages both link to |
| 3 | `posts/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane.md` | The most-searched question in the whole category |
| 4 | `posts/check-if-your-street-is-in-the-character-overlay.md` | The five-minute method; feeds the Google "Can I" ad group |
| 5 | `posts/what-is-a-knockdown-rebuild-package.md` | Catches the "packages" and volume-builder searches |
| 6 | `pages/wynnum.md`, `pages/manly.md` | Blocked on Nathan's local detail |
