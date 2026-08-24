# Client facts — MOVED

> **Layer 4. This file is no longer the source. Do not add facts here.**

⛔ **The canonical client facts now live in the handover repo:**

```
site/docs/client-facts.md
```

## Why it moved

`site/` is the real website, and it gets **handed to Sabre**. It has to work as a
self-contained island — Nathan's AI assistant will read `site/CLAUDE.md` and the
docs beside it, and it can never reach anything above that folder.

That made this file a second copy of the same truth. Two copies is how the truth
gets lost: a fact gets confirmed, goes into one file, misses the other, and
somebody puts a wrong number on a page while technically following the rules.

So there is now **one** source, and it is the one that ships.

## What that means for you

- **Adding or correcting a fact about Sabre?** Edit `site/docs/client-facts.md`.
- **Writing an ad concept or a landing page in this workshop?** Read
  `site/docs/client-facts.md`. Same rules apply here — the 4.5 rating, the
  cleared quote list, no invented numbers.

## After the handover

Once `site/` is promoted to its own repo, those docs are published with it and
readable at:

```
https://sabreconstructions.com.au/docs/client-facts.md
```

Point at that URL from here rather than making a copy. Still one source.
