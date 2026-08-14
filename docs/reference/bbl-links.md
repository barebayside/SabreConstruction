# Where this project plugs into Bare Bayside Labs

> **Layer 4.** Sabre is a **client build run out of BBL**. Anything BBL already
> owns — method, voice, pricing, deploy patterns, skills, API keys — lives there
> and is referenced from here.
>
> **One-way only (ICM Convention 3).** This file points *out* to BBL. Nothing in
> BBL points back at Sabre. If BBL ever needs to know about Sabre, that goes in a
> shared location, not a back-reference.
>
> **Canonical sources (ICM Convention 5).** Never copy BBL content into this
> repo. Point at it. If a rule exists in both places, the BBL one wins and the
> Sabre copy gets deleted.

## Root

```
BBL = ~/OneDrive/Desktop/Marketing AI content for Bare Bayside Labs/
```

Start at `BBL/CLAUDE.md` — that's BBL's own Layer 1 router, with its full
routing table.

## Method and strategy

| Need | Canonical source | Load |
|---|---|---|
| **Why marketing works on people** — the 5 tests, 13 mechanisms, the grid | `BBL/playbook/foundations.md` | Sections only. Layer 2 for the tests, Layer 5 for copy/imagery rules |
| **Auditing an existing page** | `BBL/playbook/foundations.md` | § *Workflow C* |
| Picking or chaining strategies | `BBL/playbook/CLAUDE.md` | Index, then one play |
| Ready-made plays | `BBL/playbook/strategies/` | One file |
| Multi-play sequences | `BBL/playbook/chains/` | One file |
| Paid ad creative and iteration | `BBL/docs/reference/paid-ads-playbook.md` | Relevant section |

`page-structure.md` in this folder is the *applied result* of foundations for
Sabre. The method itself is BBL's.

## Commercial

| Need | Canonical source |
|---|---|
| How BBL charges, what it does and doesn't sell | `BBL/docs/strategy/business-model.md` |
| Live prices (flagship) | `BBL/docs/strategy/pricing-2026-06.md` |
| Subscription tiers | `BBL/docs/strategy/product-tiers.md` |

⚠️ BBL has a **no-retainer rule** and prices productised, not hourly. If Sabre
becomes a paying engagement, price it from those files — don't invent a number
here.

## Build and deploy patterns

| Need | Canonical source |
|---|---|
| GitHub Pages + custom domain + DNS for a standalone site | `BBL/.claude/skills/bbl-operator-site/SKILL.md` |
| The design system this build borrows its structure from | `BBL/site/REDESIGN.md` |
| The sealed-room LP pattern | `BBL/site/lp/README.md` + `BBL/site/electricians/index.html` |

Sabre currently sits on `github.io` with no custom domain. If it ever needs one,
that's the operator-site skill, not a fresh solve.

## Media generation

| Need | Canonical source |
|---|---|
| `FAL_KEY` | `BBL/products/image-pipeline/.env` |
| Image/video pipeline, model choice rationale, cost budgeting | `BBL/docs/pipelines/image-video-creation.md` |

The Sabre-specific pipeline is in `media-pipeline.md` here. The keys, the model
rationale and the cost expectations are BBL's.

## Skills to reach for

Project-scoped, in `BBL/.claude/skills/` — these only auto-activate on files
under the BBL folder, so **invoke them by name** when working on Sabre:

| Skill | For |
|---|---|
| `form-cro` | The qualifying form. Field counts, multi-step, mobile |
| `page-cro` | Any page not converting |
| `popup-cro` | The modal fallback |
| `copywriting` / `copy-editing` | Page and ad copy |
| `paid-ads` | Campaign structure, targeting, budget |
| `ab-test-setup` | Testing the three LPs against each other |
| `social-content` | Organic to support the ads |

Global, in `~/.claude/skills/`:

| Skill | For |
|---|---|
| `bbl-copywriting` | Hormozi frameworks, offers, headlines |
| `bbl-handoff` | Writing session handoffs in Edward's format |
| `icm` / `icm-audit` | This structure |
| `avoid-ai-writing` | Humanising copy |
| `fal-generate` | Media generation |

## If leads ever go into Zoho

BBL runs **Zoho One exclusively**. The form currently posts to a third-party
relay, which is fine for a demo and wrong for a real pipeline.

| Need | Canonical source |
|---|---|
| What already exists before you build a new funnel/segment/journey | `BBL/docs/registry/zoho-systems/README.md` |
| CRM field governance | `BBL/docs/architecture/crm/bbl-crm-strategy.md` |
| Marketing automation architecture | `BBL/docs/architecture/marketing/zma-platform-architecture.md` |

⚠️ **Sabre would need its own Zoho org.** Do not put a client's leads into BBL's
CRM. Same rule that keeps OOP separate.

## The boundary

Sabre is a **separate repo, separate brand, separate inbox**. What it shares with
BBL is *method and tooling*, never data, never CRM, never the mailing list.
