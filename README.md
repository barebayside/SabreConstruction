# Sabre Constructions

Client demo build for Sabre Constructions, a family-owned builder in Capalaba QLD.
Static site, no build step.

**Live:** https://barebayside.github.io/SabreConstruction/

| | |
|---|---|
| `index.html` | Main site page |
| `ads.html` | Ad concepts showcase |
| `lp-rebuild.html` | LP 1 · Meta Reels 9:16 |
| `lp-raise.html` | LP 2 · Meta Feed 1:1/4:5 |
| `lp-story.html` | LP 3 · Google Ads desktop |

## Working in this repo

**Start at [`CLAUDE.md`](CLAUDE.md).** It's the router — find your task in its
table, open the one file it points at, and stop there.

Documentation is structured to the Interpreted Context Methodology, so nothing
loads that a task doesn't need:

```
CLAUDE.md          router — always read first
CONTEXT.md         task → workspace dispatcher
docs/
  open-items.md    what's blocked, fake or waiting — read every session
  tasks/           one contract per job (Inputs · Process · Outputs)
  reference/       canonical sources: facts, design, copy, form, media, BBL links
handoffs/          dated session snapshots
```

## Before you touch anything

Read [`docs/open-items.md`](docs/open-items.md). Several things on these pages
are deliberately fake and must not go public as-is — the testimonial videos are
AI-generated people, the star ratings are empty slots, and the lead form doesn't
go anywhere yet.

Preview locally:

```
py -3 tools/shoot.py     # screenshots, desktop + mobile
```
