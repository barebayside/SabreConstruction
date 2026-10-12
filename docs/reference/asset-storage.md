# Where Sabre's files live

> **Layer 4. Canonical from 2026-09-25.** Every video, photo and ad file has ONE
> home. This page says which. The ad *records* live somewhere else, on purpose.

## Two places, two jobs

| | **WorkDrive: the files** | **BBL registry: the records** |
|---|---|---|
| Where | `X:\General\BBL Customers\Sabre Constructions — noid\` | `BBL/docs/registry/marketing-assets/SAB-…/` |
| Holds | Original footage, finished videos, ad masters, captions, thumbnails, brand files | One folder per ad/page code: `meta.json` (copy, status, weekly results), `copy.md`, a small `creative.jpg` |
| Why there | Big binary files, backed up, shareable with Nathan, never in a public git repo | Small text, in git, one code joins Meta/Google/UTMs/results |
| Link | Each registry record's `creative_master` names its WorkDrive folder | |

**The ad's code is the join.** The same string (e.g. `SAB-CON-KDR-5.0A_META_VIDEO`)
is the registry folder name, the Meta ad name, the `utm_content`, and the file
name inside WorkDrive. Search any one of them and you find the rest.

## WorkDrive layout

```
Sabre Constructions — noid\
  COMP\       competitor-intel runs. Written by the Catalyst pipeline; never hand-edit
  VIDEO\      filmed footage and every cut made from it
  WEBSITE\    site-level files (favicon, logos made for the web)
  ADS\        ad-only creative that has no filmed source (static images, carousels)
```

One dated folder per job: `<AREA>\YYYY-MM-DD — <what>\`, with a plain-English
`README.txt` (what it is, what was changed and why, where it's live, what's
still to confirm). Example, the first one:

```
VIDEO\2026-09-25 — Leanne Chandler testimonial\
  01 original from videographer\   exactly as received. Never overwritten
  02 website version\              the file on the site + captions + poster
  03 ad version (Meta)\            <CODE>.mp4 · <CODE>.en_US.srt · <CODE>-thumbnail.jpg
  README.txt · transcript.txt
```

## The rules

1. **Originals go to WorkDrive first**, into `01 original…`, before any editing.
   Downloads and the desktop are not storage.
2. **Every cut gets its own numbered subfolder.** A new ad variant (1.0B, a
   20-second cut) = a new `03b …` subfolder in the same job folder, file named
   with its code.
3. **The public repos never hold masters.** The real site repo holds only the
   web encode (small, `assets/video/`). This workshop's `assets/ads/` is a
   scratch copy and is gitignored; WorkDrive is the copy that counts.
4. **Register the code first, then file.** New ad → `bbl-asset-code` skill gives
   the code → the WorkDrive files carry that code → set `creative_master` on
   the record.
5. **`COMP\` belongs to Catalyst.** Don't add, move or rename inside it; the
   pipeline finds folders by exact name.

## Where Sabre drops footage: Nathan's Google Drive (the inbox)

Logged 2026-10-12. This is the **inbox**, not the archive. Nathan and his
videographer upload here; WorkDrive above stays the home for everything we keep.

| | |
|---|---|
| Folder | **"Ed "** (trailing space in the name). https://drive.google.com/drive/folders/1hhgEEuCKyRcbi8ALkPnulnl3DxN_GmIo |
| Owner | `nathanbrain27@gmail.com`: Nathan's personal Google account, free 15 GB tier. Raw 4K fills this fast; he may need Google One |
| Access | `edasturner@gmail.com` = **Editor**. Nobody else. Checked 2026-10-12 |
| Inside (10-12) | `03. Client Testimony - Chandler (1).MOV` (391 MB) · `Video ads/04. Knock down.mov` (94 MB). Both already used |
| Storage | Nathan's uploads count against HIS quota; anything Edward uploads counts against EDWARD's |

**How Claude reaches it:** the claude.ai Google Drive connector (signed in as
`edasturner@gmail.com`) can **list and search** the folder (`parentId =
'1hhgEEuCKyRcbi8ALkPnulnl3DxN_GmIo'`) and read permissions. It **cannot pull
video**: downloads come back as base64 text, which is useless at 100+ MB.
So Edward downloads the file in Brave → Claude works from that copy. If Google
Drive for desktop is ever installed (with a shortcut to this folder in My Drive),
Claude can read it straight from disk and the manual download goes away.

## When Sabre sends new footage

0. Claude lists the Google Drive inbox above and names what's new; Edward
   downloads it in Brave.
1. Copy the original into `VIDEO\<date> — <what>\01 original…\`.
2. Check it (`ffprobe`, loudness, captions legible at phone size): see
   `docs/tasks/generate-media.md`.
3. Web encode into the real repo; ad master + SRT into `03 …`; README.
4. Code in the registry; `creative_master` pointing here.
