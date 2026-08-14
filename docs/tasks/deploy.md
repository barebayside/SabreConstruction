# Task: publish and verify

> **Layer 3 contract.** Scope: git and GitHub Pages. Runs at the end of every
> other task.

## Inputs

| Source | File | Section / Scope |
|---|---|---|
| Repo + URL | `../../CLAUDE.md` | § *What this is* |
| Custom domain, if one is ever needed | see `../reference/bbl-links.md` | § *Build and deploy patterns* |

## Process

1. `git status --short` — check nothing unexpected is staged.
2. Confirm raw media is gitignored: `git ls-files | xargs du -ch | tail -1`
   should stay in the tens of MB, not hundreds.
3. Commit. Write what changed **and why**, not just what.
4. `git push origin main`.
5. Verify — see below. GitHub Pages takes roughly a minute.

## ⚠️ How to verify properly

**Poll for a string that only exists in the NEW build.** This has produced a
false pass before: a check for text present in both the old and new versions
passed instantly against a stale cache and reported a deploy that hadn't
happened.

```bash
until curl -s "https://barebayside.github.io/SabreConstruction/" \
  | grep -q "SOME-NEW-STRING"; do sleep 8; done
```

Then check the actual assets return 200 with a sensible byte count:

```bash
for u in "" ads.html lp-rebuild.html lp-raise.html lp-story.html \
         css/sabre.css js/qualify.js; do
  printf "%-22s " "$u"
  curl -s -o /dev/null -w "%{http_code}  %{size_download}b\n" \
    "https://barebayside.github.io/SabreConstruction/$u"
done
```

A 200 on the HTML is not proof the CSS and video shipped. Check them.

## Audit

| Check | Pass condition |
|---|---|
| New string live | Present in the fetched page, not just the local file |
| Every changed asset | 200 with a non-trivial byte count |
| Cache-busters | `?v=N` in the live HTML matches what you bumped |
| Repo size | Raw model output still excluded |

## Outputs

| Artifact | Location |
|---|---|
| Commit | `main` |
| Live site | https://barebayside.github.io/SabreConstruction/ |
