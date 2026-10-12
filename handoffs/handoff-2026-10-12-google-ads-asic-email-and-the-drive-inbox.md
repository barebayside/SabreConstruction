# Handoff — 2026-10-12 — Google Ads ASIC email drafted + Nathan's Drive folder logged as the footage inbox

## Session Focus
Restarting the Google Ads setup for Sabre (Google needs proof of business registration) and
settling where Nathan uploads videos so they don't use Edward's storage.

## What Got Done
- **Email to Nathan DRAFTED (not sent).** Asks for the ASIC company registration certificate /
  extract by **Friday 16 Oct**, which of the two companies trades, and what address is on the
  certificate. Also tells him to keep using the "Ed" Drive folder and have the videographer upload
  raw landscape 4K straight into it. Full text below.
- **Google Drive connector connected** (claude.ai Google Drive, signed in as `edasturner@gmail.com`).
- **Nathan's folder found and checked:** "Ed " (trailing space), owner `nathanbrain27@gmail.com`,
  Edward = Editor, nobody else. Contents: `03. Client Testimony - Chandler (1).MOV` (391 MB) and
  `Video ads/04. Knock down.mov` (94 MB). Both already used (Leanne 09-25, knockdown 09-30).
- **Proven:** the connector can list, search and read permissions. **It cannot pull video**:
  downloads come back as base64 text, which doesn't work at 100+ MB.
- Logged the folder as the **footage inbox** in `docs/reference/asset-storage.md` (WorkDrive stays
  the archive); added step 0 to "When Sabre sends new footage".

## Files Changed / Created
| Path | What changed |
|---|---|
| `docs/reference/asset-storage.md` | New section "Where Sabre drops footage: Nathan's Google Drive (the inbox)" + step 0 |
| `CLAUDE.md` (Sabre project router) | Asset-storage row now mentions the Google Drive inbox |
| `handoffs/handoff-2026-10-12-…md` | This file |

Committed `eceead2` in the workshop repo. Not pushed (workshop repo).

## Decisions Made
1. **Nathan's own Google Drive folder is the upload inbox.** No new accounts, no Sabre M365 user
   for Edward (that needs Nathan's IT person, so ruled out). Recorded in `asset-storage.md`.
2. **Workflow for new footage:** Claude lists the folder → Edward downloads in Brave → Claude works
   from that copy → finished files go back into Nathan's folder + WorkDrive. Google Drive for
   desktop would remove the manual download (offered, not installed).
3. **The email asks for one document only**, plus the entity and address questions. The MCC link
   (needs Nathan's 10-digit Customer ID) was left out to keep it a single ask.

## Resolved failures
- None this session. Facts that ruled options out:
  - **OneDrive / Microsoft 365 route ruled out.** Sabre's mail is Microsoft 365 (MX =
    `sabreconstructions-com-au.mail.protection.outlook.com`), but adding a user means going through
    their IT person.
  - **The `Y:` drive is Edward's own WorkDrive**, not Sabre's. Don't treat `Y:\My Folders\Nathan\`
    as a client share.

## What's NOT Done — TODO
1. **Edward: send the email** (text below) to nathan@sabreconstructions.com.au. Log the send in
   `docs/engagement.md`.
2. **When the certificate arrives:** confirm the entity (29 107 425 703 vs Sabre Constructions QLD
   Pty Ltd 29 673 587 472). It must match the Google Ads payments profile **and** the unsigned
   agreement.
3. **Google Ads still unlinked.** Need Nathan's 10-digit Customer ID → MCC `775-584-9139` sends the
   link → Nathan accepts (Admin → Access and security → Managers) → Owner Yes. Run the
   `/bbl-google-ads-link` skill and log in BBL `docs/reference/google-ads-account-structure.md` §6.
   Check the Sabre account is **active** first (OOP's links died because its account went inactive).
4. Advertiser verification (Google's business check) happens inside Sabre's account, possibly done
   by BBL "on behalf of a client"; the certificate is for that step.
5. Watch Nathan's 15 GB free Drive quota once raw 4K starts arriving.
6. Optional: install Google Drive for desktop + add a shortcut to the "Ed" folder in My Drive, so
   Claude reads footage from disk.
7. Carried over: knockdown video no-music version + "I'm the owner" check (09-30), Nathan voice
   note, DNS/noindex cutover, GBP address.

## Quick Context for Next Session
- Project: `C:\Users\edast\OneDrive\Desktop\Sabre Constructions\`. Read `CLAUDE.md` → this handoff.
- Drive folder ID: `1hhgEEuCKyRcbi8ALkPnulnl3DxN_GmIo`. List with search_files
  `parentId = '<id>'` (subfolder `Video ads` = `1rM-QKP6YD1pp-INoNJV0N5ggSqfwouka`).
- Most likely next task: Nathan's certificate arrives → Google Ads link + verification, or new
  footage lands → ad cut (register a SAB code first via `bbl-asset-code`).

### The email (as drafted)

**To:** nathan@sabreconstructions.com.au
**Subject:** Google Ads: one document needed by Friday

Hi Nathan,

We're ready to finish setting up your Google Ads account. Before Google will run any ads, it needs to confirm Sabre is a registered business. To do that I need one thing from you:

**Your ASIC company registration certificate** (or a current ASIC company extract) for the company that will pay for the ads.

Could you send it through by **this Friday, 16 October**? A PDF or a clear phone photo is fine.

Two quick questions as well:
1. **Which company runs the business day to day?** I can see two registered: *Sabre Constructions* (ABN 29 107 425 703) and *Sabre Constructions QLD Pty Ltd* (ABN 29 673 587 472). The certificate, the Google Ads account and the card paying for the ads all need to be under the same company.
2. **What address is on the certificate?** If it still says Steel St, Capalaba, that's fine. I just need the details we give Google to match what's on file.

**Videos and photos:** the Google Drive folder you shared with me ("Ed") is working well. I've already used the Chandler testimonial and the knockdown video from it. Please keep putting everything there, and ask your videographer to upload straight into it too. Raw, unedited clips are the most useful, ideally filmed landscape in 4K, plus any job photos you have. It all stays on your storage, and I'll put the finished ads back in the same folder.

Thanks,
Edward
