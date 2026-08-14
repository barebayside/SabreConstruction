# Docs

> **Layer 2 for documentation.** Routing only.

## What is this folder?

Every rule, fact and process for the Sabre build. Code lives at the repo root;
this folder explains it.

## What do I load?

Never read this folder wholesale. Open the contract for your task, and load only
the sections its Inputs table names.

| Task | Contract |
|---|---|
| Main site page | `tasks/edit-main-site.md` |
| Landing pages / lead form | `tasks/edit-landing-pages.md` |
| Ad concepts page | `tasks/edit-ad-concepts.md` |
| Video or image generation | `tasks/generate-media.md` |
| Publishing | `tasks/deploy.md` |

## Reference (Layer 4)

| File | Canonical source for |
|---|---|
| `open-items.md` | What's blocked, fake, or waiting. **Read every session** |
| `reference/client-facts.md` | Every verified fact about Sabre + its source |
| `reference/design-system.md` | Palette, type, motion, components |
| `reference/page-structure.md` | Section order and the reasoning |
| `reference/copy-rules.md` | Voice and claim rules |
| `reference/lead-capture.md` | The five questions, the relay, the config |
| `reference/media-pipeline.md` | How every asset was made |
| `reference/fal-video-capabilities.md` | What fal.ai can do on length, sequencing and cost |
| `reference/bbl-links.md` | Where this plugs into Bare Bayside Labs |

## Rules for this folder

- One home per fact. If something is true in two files, one becomes a pointer.
- Reference files stay under 200 lines. Split anything longer.
- CONTEXT files stay under 80 lines and hold routing only, never content.
- References point **outward**. Nothing points back.
