# Sabre · general Google Ads campaign (`sab-knockdown-rebuild-2026`)

`status: draft for sign-off` · built 2026-10-30 by `tools/build_google_ads.py` (edit the script, not this file)

Edward signs off → Nathan's account is linked → Claude builds it in Google Ads, **paused**.

## What the research found

**Pulled 2026-10-30** (files in `docs/sessions/2026-10-30-gads-*.json`): Google's suggested searches for
8 builder phrases × 16 places (119 unique suggestions), 58 Google results pages, and the map listings for
"home builder" around six of the suburbs.

- **Very little paid competition in the pocket.** Only 7 of 58 searches showed any ad, all on "builders /
  home builders <suburb>" (Gumdale, Birkdale, Tingalpa, Murarrie, Manly West, Ransome), all volume builders
  (Orbit Homes, Meadan Homes, Plantation Homes). **No knockdown rebuild search showed an ad at all.**
- **Nobody types "knockdown rebuild" + suburb.** Google only suggests it at Brisbane level ("knock down
  rebuild builders brisbane", "… cost", "… prices"). So the clever play is Brisbane-wide words, shown only
  to people in the 13 suburbs.
- **The long tail is "builders <suburb>"**: Google's related searches are buyers ("small builders wynnum
  qld", "independent home builders wynnum qld", "builders wynnum qld reviews", "best builders manly qld").
- **Cost is the biggest question** ("knock down rebuild brisbane cost" and "… cost calculator" top the
  related searches; the People-also-ask boxes are mostly price). We answer with the cost article, never a number.
- **Sabre is in none of the top 10 results** (expected: the new site is hidden until the domain moves).
  The organic results are mostly realestate.com.au, hipages, Facebook and volume builders.
- **Sabre is in none of the map listings** for "home builder" around Wynnum, Manly, Capalaba, Birkdale,
  Gumdale or Hemmant (49 listings). Wynnum, Manly and Birkdale are held by small builders with 0–11 reviews
  (Saltash Homes 5.0 from 8, NLH 5.0 from 4, BTB and Tierney with none), so a fixed profile with Sabre's
  12 reviews can compete there. Capalaba is crowded: Fiteni 4.8 from 69, CJ Homes 4.3 from 75, Lindon 4.8
  from 19, Dixon 4.6 from 35. The map box follows the address, so the Ransome fix matters.
- ⚠️ **One sample, desktop, not located in the suburbs.** Google shows different ads to someone sitting
  in Wynnum, and this gives no search volumes or click prices. **On build day, run Keyword Planner** inside
  Sabre's account for real volumes and bids before turning anything on.

## Campaign settings

| Setting | Value |
|---|---|
| Campaign name | sab-knockdown-rebuild-2026 |
| Type | Search only. Display Network OFF, Search partners OFF |
| Locations | The 13 suburbs by name (postcode fallback below). Presence: people IN or regularly in these places, NOT 'interested in' |
| Language | English |
| Bidding, week 1 | Maximise clicks with a max CPC cap (set from Nathan's budget on build day). Switch to Maximise conversions once ~15 form/call conversions are recorded |
| Daily budget | From Nathan's monthly budget ÷ 30.4. Proposal was ~$30–50/day across Google + Meta |
| Ad schedule | All days. Calls go to Nathan's mobile: call asset limited to the hours he'll answer (ask) |
| Turn OFF | AI Max / automatically created assets / final URL expansion / auto-apply recommendations / broad match |
| Conversions (before any spend) | Submit lead form (page-load snippet on the form's success state) · Calls from ads · Clicks on the phone number |
| Status | Everything built PAUSED. Turned on only after the gates (real domain, test enquiry, conversions firing) |

**The 13 suburbs:** Wynnum · Wynnum West · Manly · Manly West · Lota · Wakerley · Gumdale · Capalaba · Birkdale · Hemmant · Murarrie · Tingalpa · Ransome

**Postcode fallback** (if a suburb isn't in Google's list): 4154 (Gumdale, Ransome, Wakerley) · 4157 (Capalaba) · 4159 (Birkdale) · 4172 (Murarrie) · 4173 (Tingalpa) · 4174 (Hemmant) · 4178 (Wynnum, Wynnum West) · 4179 (Manly, Manly West, Lota)

## Google Maps

1. **Ads on Maps** need a *location asset*: link Sabre's Google Business Profile to the Ads account (Assets → Location → link the Business Profile). Without it, ads never show on Maps.
2. **The free map box** is the Business Profile itself: primary category *Home builder*, secondary *Custom home builder*, the 13 suburbs as the service area, address **40 Molle Rd, Ransome QLD 4154** (it still says Capalaba), phone matching the site, the new website link, photos. Needs Edward as manager.

## Ad groups (ad group name = the code)

### Knockdown rebuild · `SAB-SOL-KDR-2.0A_GOOGLE_SEARCH`

The main buying search. Nobody types a suburb with it (Google suggests 'knock down rebuild builders brisbane', never '… wynnum'), so we bid on the Brisbane-wide words and let the 13-suburb location setting do the narrowing. Rivals bidding these pay for all of Brisbane; Sabre only pays for its pocket.

- **Lands on:** `/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-2.0A_GOOGLE_SEARCH`
- **Keywords** (36, "phrase" and [exact]): "knockdown rebuild", [knockdown rebuild], "knock down rebuild", [knock down rebuild], "knock down and rebuild", [knock down and rebuild], "knockdown rebuild brisbane", [knockdown rebuild brisbane], "knock down rebuild brisbane", [knock down rebuild brisbane], "knock down and rebuild brisbane", [knock down and rebuild brisbane], "knock down rebuild builders", [knock down rebuild builders], "knockdown rebuild builders brisbane", [knockdown rebuild builders brisbane], "knock down rebuild builders brisbane", [knock down rebuild builders brisbane], "knockdown rebuild bayside", [knockdown rebuild bayside], "knock down rebuild bayside", [knock down rebuild bayside], "knockdown rebuild brisbane southside", [knockdown rebuild brisbane southside], "demolish and rebuild", [demolish and rebuild], "demolish and rebuild brisbane", [demolish and rebuild brisbane], "knock down rebuild near me", [knock down rebuild near me], "knockdown rebuild builder near me", [knockdown rebuild builder near me], "best knockdown rebuild brisbane", [best knockdown rebuild brisbane], "knockdown rebuild brisbane reviews", [knockdown rebuild brisbane reviews]

- **Ad-group negatives:** cost, costs, price, prices, calculator, how much. Cost searches go to their own ad group (the cost article), not the home page.

- **Headlines** (pin 1 = first three):
  1. Knockdown Rebuild Builders (26) [pin 1]
  2. Knock Down & Rebuild (20) [pin 1]
  3. Knockdown Rebuild, Bayside (26) [pin 1]
  4. Knockdown Rebuild Brisbane (26)
  5. Same Street. Whole New House (28)
  6. Build Your Family Home (22)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. Knock down the old house, keep the street. A Bayside family builder since 1990. (79)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/rebuild/bayside

### Builders · Wynnum side · `SAB-SOL-KDR-3.0A_GOOGLE_SEARCH`

'builders <suburb>' is where the long tail lives: almost no ads on these in our check, and the related searches are buyers ('small builders wynnum qld', 'builders wynnum qld reviews', 'independent home builders wynnum qld'). Lands on the Wynnum page so the ad and page say the same suburb.

- **Lands on:** `/wynnum/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/wynnum/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-3.0A_GOOGLE_SEARCH`
- **Keywords** (90, "phrase" and [exact]): "builders wynnum", [builders wynnum], "home builders wynnum", [home builders wynnum], "house builders wynnum", [house builders wynnum], "new home builders wynnum", [new home builders wynnum], "builder wynnum", [builder wynnum], "local builders wynnum", [local builders wynnum], "small builders wynnum", [small builders wynnum], "custom home builder wynnum", [custom home builder wynnum], "builders wynnum west", [builders wynnum west], "home builders wynnum west", [home builders wynnum west], "house builders wynnum west", [house builders wynnum west], "new home builders wynnum west", [new home builders wynnum west], "builder wynnum west", [builder wynnum west], "local builders wynnum west", [local builders wynnum west], "small builders wynnum west", [small builders wynnum west], "custom home builder wynnum west", [custom home builder wynnum west], "builders hemmant", [builders hemmant], "home builders hemmant", [home builders hemmant], "house builders hemmant", [house builders hemmant], "new home builders hemmant", [new home builders hemmant], "builder hemmant", [builder hemmant], "local builders hemmant", [local builders hemmant], "small builders hemmant", [small builders hemmant], "custom home builder hemmant", [custom home builder hemmant], "builders murarrie", [builders murarrie], "home builders murarrie", [home builders murarrie], "house builders murarrie", [house builders murarrie], "new home builders murarrie", [new home builders murarrie], "builder murarrie", [builder murarrie], "local builders murarrie", [local builders murarrie], "small builders murarrie", [small builders murarrie], "custom home builder murarrie", [custom home builder murarrie], "builders tingalpa", [builders tingalpa], "home builders tingalpa", [home builders tingalpa], "house builders tingalpa", [house builders tingalpa], "new home builders tingalpa", [new home builders tingalpa], "builder tingalpa", [builder tingalpa], "local builders tingalpa", [local builders tingalpa], "small builders tingalpa", [small builders tingalpa], "custom home builder tingalpa", [custom home builder tingalpa], "builders wynnum manly", [builders wynnum manly], "builders wynnum qld reviews", [builders wynnum qld reviews], "best builders wynnum", [best builders wynnum], "independent home builders wynnum", [independent home builders wynnum], "builders wynnum qld", [builders wynnum qld]

- **Headlines** (pin 1 = first three):
  1. Builders in Wynnum (18) [pin 1]
  2. Wynnum Home Builders (20) [pin 1]
  3. Tingalpa & Murarrie Builder (27) [pin 1]
  4. Local Builder, Wynnum West (26)
  5. Hemmant & Wynnum Builder (24)
  6. Small Family Builder (20)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. A small family builder minutes from Wynnum. New homes and knockdown rebuilds. (77)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/builders/wynnum

### Builders · Manly side · `SAB-SOL-KDR-4.0A_GOOGLE_SEARCH`

Same long-tail play for Manly, Manly West and Lota, on the Manly page.

- **Lands on:** `/manly/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/manly/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-4.0A_GOOGLE_SEARCH`
- **Keywords** (56, "phrase" and [exact]): "builders manly", [builders manly], "home builders manly", [home builders manly], "house builders manly", [house builders manly], "new home builders manly", [new home builders manly], "builder manly", [builder manly], "local builders manly", [local builders manly], "small builders manly", [small builders manly], "custom home builder manly", [custom home builder manly], "builders manly west", [builders manly west], "home builders manly west", [home builders manly west], "house builders manly west", [house builders manly west], "new home builders manly west", [new home builders manly west], "builder manly west", [builder manly west], "local builders manly west", [local builders manly west], "small builders manly west", [small builders manly west], "custom home builder manly west", [custom home builder manly west], "builders lota", [builders lota], "home builders lota", [home builders lota], "house builders lota", [house builders lota], "new home builders lota", [new home builders lota], "builder lota", [builder lota], "local builders lota", [local builders lota], "small builders lota", [small builders lota], "custom home builder lota", [custom home builder lota], "builders manly qld", [builders manly qld], "builders manly qld reviews", [builders manly qld reviews], "best builders manly", [best builders manly], "home builders manly qld", [home builders manly qld]

- **Ad-group negatives:** nsw, sydney, northern beaches, manly vale, manly beach. Manly NSW (Sydney) is the bigger Manly. Location settings stop most of it; these stop the rest.

- **Headlines** (pin 1 = first three):
  1. Builders in Manly (17) [pin 1]
  2. Manly Home Builders (19) [pin 1]
  3. Manly & Lota Builder (20) [pin 1]
  4. Local Builder, Manly West (25)
  5. Lota Home Builders (18)
  6. Small Family Builder (20)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. A small family builder minutes from Manly. New homes and knockdown rebuilds. (76)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/builders/manly

### Builders · Capalaba, Birkdale, Ransome side · `SAB-SOL-KDR-5.0A_GOOGLE_SEARCH`

The Redlands edge and Sabre's own suburb (Ransome). The only suburb searches where a rival ad showed (Gumdale, Birkdale: Orbit, Meadan) are volume builders; a local family builder stands out next to them.

- **Lands on:** `/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-5.0A_GOOGLE_SEARCH`
- **Keywords** (84, "phrase" and [exact]): "builders capalaba", [builders capalaba], "home builders capalaba", [home builders capalaba], "house builders capalaba", [house builders capalaba], "new home builders capalaba", [new home builders capalaba], "builder capalaba", [builder capalaba], "local builders capalaba", [local builders capalaba], "small builders capalaba", [small builders capalaba], "custom home builder capalaba", [custom home builder capalaba], "builders birkdale", [builders birkdale], "home builders birkdale", [home builders birkdale], "house builders birkdale", [house builders birkdale], "new home builders birkdale", [new home builders birkdale], "builder birkdale", [builder birkdale], "local builders birkdale", [local builders birkdale], "small builders birkdale", [small builders birkdale], "custom home builder birkdale", [custom home builder birkdale], "builders ransome", [builders ransome], "home builders ransome", [home builders ransome], "house builders ransome", [house builders ransome], "new home builders ransome", [new home builders ransome], "builder ransome", [builder ransome], "local builders ransome", [local builders ransome], "small builders ransome", [small builders ransome], "custom home builder ransome", [custom home builder ransome], "builders gumdale", [builders gumdale], "home builders gumdale", [home builders gumdale], "house builders gumdale", [house builders gumdale], "new home builders gumdale", [new home builders gumdale], "builder gumdale", [builder gumdale], "local builders gumdale", [local builders gumdale], "small builders gumdale", [small builders gumdale], "custom home builder gumdale", [custom home builder gumdale], "builders wakerley", [builders wakerley], "home builders wakerley", [home builders wakerley], "house builders wakerley", [house builders wakerley], "new home builders wakerley", [new home builders wakerley], "builder wakerley", [builder wakerley], "local builders wakerley", [local builders wakerley], "small builders wakerley", [small builders wakerley], "custom home builder wakerley", [custom home builder wakerley], "builders capalaba qld", [builders capalaba qld], "small builders capalaba", [small builders capalaba]

- **Headlines** (pin 1 = first three):
  1. Builders in Capalaba (20) [pin 1]
  2. Birkdale Home Builders (22) [pin 1]
  3. Ransome & Gumdale Builder (25) [pin 1]
  4. Wakerley Home Builders (22)
  5. Based Right Here in Ransome (27)
  6. Small Family Builder (20)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. Based in Ransome, building across Capalaba, Birkdale, Gumdale and Wakerley. (75)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/builders/capalaba

### Bayside + Redlands home builders · `SAB-SOL-KDR-6.0A_GOOGLE_SEARCH`

The area-wide words families use ('bayside builders brisbane', 'home builders redlands', 'custom home builders brisbane bayside'). Shown only inside the 13 suburbs. 'Small' and 'independent' are the avatar's own words from the 09-05 research.

- **Lands on:** `/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-6.0A_GOOGLE_SEARCH`
- **Keywords** (38, "phrase" and [exact]): "bayside builders", [bayside builders], "bayside builders brisbane", [bayside builders brisbane], "home builders brisbane bayside", [home builders brisbane bayside], "custom home builders brisbane bayside", [custom home builders brisbane bayside], "custom home builders bayside", [custom home builders bayside], "builders brisbane bayside", [builders brisbane bayside], "home builders redlands", [home builders redlands], "builders redlands", [builders redlands], "new home builders redlands", [new home builders redlands], "custom home builders redlands", [custom home builders redlands], "house builders redlands", [house builders redlands], "builders brisbane southside", [builders brisbane southside], "small builders brisbane", [small builders brisbane], "independent builders brisbane", [independent builders brisbane], "family builder brisbane", [family builder brisbane], "local builder brisbane", [local builder brisbane], "builders near me", [builders near me], "home builders near me", [home builders near me], "new home builders near me", [new home builders near me]

- **Ad-group negatives:** bayside council, bayside vic, bayside melbourne, brighton. 'Bayside' is also a Melbourne council.

- **Headlines** (pin 1 = first three):
  1. Bayside Home Builders (21) [pin 1]
  2. Custom Home Builder, Bayside (28) [pin 1]
  3. Redlands Home Builder (21) [pin 1]
  4. Independent Local Builder (25)
  5. Small Family Builder (20)
  6. Build Your Family Home (22)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. An independent family builder, not a volume builder. Bayside and Redlands only. (79)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/builders/bayside

### Sabre's own name · `SAB-SOL-KDR-7.0A_GOOGLE_SEARCH`

Cheap insurance. When someone sees a Sabre sign or Facebook ad and Googles the name, a rival can't sit above Sabre on its own name. Sabre isn't on page one for anything yet (the new site is hidden until the domain moves).

- **Lands on:** `/` · **turn on:** week 1
- **Final URL:** `https://sabreconstructions.com.au/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-SOL-KDR-7.0A_GOOGLE_SEARCH`
- **Keywords** (14, "phrase" and [exact]): "sabre constructions", [sabre constructions], "sabre construction", [sabre construction], "sabre builders", [sabre builders], "sabre constructions ransome", [sabre constructions ransome], "sabre constructions capalaba", [sabre constructions capalaba], "sabre constructions brisbane", [sabre constructions brisbane], "sabre homes brisbane", [sabre homes brisbane]

- **Ad-group negatives:** sabre sports, sword, lightsaber, fencing club. Other 'Sabres'.

- **Headlines** (pin 1 = first three):
  1. Sabre Constructions (19) [pin 1]
  2. Sabre Constructions, Ransome (28) [pin 1]
  3. Official Site (13)
  4. Talk to Nathan Directly (23)
  5. Family Builder Since 1990 (25)
  6. Family Builder Since 1990 (25)
  7. Master Builders QLD Member (26)
  8. QBCC Licence 15486557 (21)
  9. Family-Owned, Based in Ransome (30)
  10. Book a Walk-Through (19)
  11. Stay on the Street You Love (27)
  12. Rated 4.5 From 12 Reviews (25)
  13. Bayside and Redlands Only (25)
- **Descriptions:**
  1. Sabre Constructions: family-owned Bayside builder since 1990. Call or book online. (82)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/sabre

### Knockdown rebuild cost (long tail) · `SAB-CON-KDR-6.0A_GOOGLE_SEARCH`

Cost is the biggest question in every search we've pulled ('knock down rebuild brisbane cost' and 'cost calculator' top the related searches; 11 of 16 'People also ask' on 09-05 were cost). Volume builders answer it with a price; Sabre answers it with the article 'what decides the cost', never a number. A cheap research click that starts the relationship. A TEST: if it brings clicks but no enquiries, pause it.

- **Lands on:** `/blog/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/` · **turn on:** stage 2, or week 1 if budget allows
- **Final URL:** `https://sabreconstructions.com.au/blog/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-CON-KDR-6.0A_GOOGLE_SEARCH`
- **Keywords** (18, "phrase" and [exact]): "knock down rebuild cost", [knock down rebuild cost], "knockdown rebuild cost", [knockdown rebuild cost], "knock down rebuild brisbane cost", [knock down rebuild brisbane cost], "knockdown rebuild brisbane cost", [knockdown rebuild brisbane cost], "knock down rebuild prices brisbane", [knock down rebuild prices brisbane], "knockdown rebuild prices", [knockdown rebuild prices], "how much does a knock down rebuild cost", [how much does a knock down rebuild cost], "cost to knock down and rebuild a house", [cost to knock down and rebuild a house], "is it cheaper to knock down and rebuild", [is it cheaper to knock down and rebuild]

- **Ad-group negatives:** calculator, sydney, melbourne, gold coast. 'Calculator' searchers want a tool we don't have.

- **Headlines** (pin 1 = first three):
  1. What Decides Rebuild Cost? (26) [pin 1]
  2. Knockdown Rebuild Costs (23) [pin 1]
  3. Rebuild Costs, Explained (24) [pin 1]
  4. Before You Price a Rebuild (26)
  5. Plain-English Answers (21)
  6. Written by a Local Builder (26)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. No price lists. What actually decides the cost of a knockdown rebuild in Brisbane. (82)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/rebuild/cost

### Can we knock it down? · `SAB-CON-KDR-7.0A_GOOGLE_SEARCH`

The question before the rebuild: Brisbane's character overlay stops some pre-1947 houses coming down. Few builders answer it; Sabre's page does, then offers a block check. Brisbane City Council rules only, so it mostly matters on the Wynnum/Manly side.

- **Lands on:** `/can-we-knock-it-down/` · **turn on:** stage 2
- **Final URL:** `https://sabreconstructions.com.au/can-we-knock-it-down/?utm_source=google&utm_medium=cpc&utm_campaign=sab-knockdown-rebuild-2026&utm_content=SAB-CON-KDR-7.0A_GOOGLE_SEARCH`
- **Keywords** (18, "phrase" and [exact]): "can i knock down my house brisbane", [can i knock down my house brisbane], "can i demolish my house brisbane", [can i demolish my house brisbane], "can i knock down my house", [can i knock down my house], "character overlay brisbane", [character overlay brisbane], "traditional building character overlay", [traditional building character overlay], "pre 1947 house demolish", [pre 1947 house demolish], "demolition approval brisbane", [demolition approval brisbane], "can you knock down a pre 1947 house", [can you knock down a pre 1947 house], "is my house in a character overlay", [is my house in a character overlay]

- **Ad-group negatives:** renovate, extension, heritage grant

- **Headlines** (pin 1 = first three):
  1. Can You Knock It Down? (22) [pin 1]
  2. Can We Knock Down Our House? (28) [pin 1]
  3. Character Overlay Check (23) [pin 1]
  4. Pre-1947 House? Read This (25)
  5. Check Before You Demolish (25)
  6. Ask a Bayside Builder (21)
  7. Family Builder Since 1990 (25)
  8. Master Builders QLD Member (26)
  9. QBCC Licence 15486557 (21)
  10. Family-Owned, Based in Ransome (30)
  11. Book a Walk-Through (19)
  12. Stay on the Street You Love (27)
  13. Rated 4.5 From 12 Reviews (25)
  14. Bayside and Redlands Only (25)
- **Descriptions:**
  1. Some Brisbane houses can't legally come down. See what decides it for yours first. (82)
  2. Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today. (81)
  3. Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands. (87)
  4. Keep the street, the school and the neighbours. Rebuild the house around your family. (85)
- **Display path:** sabreconstructions.com.au/knock-it-down

## Negative keywords (one shared list on the campaign, phrase match)

- **Jobs and training:** job, jobs, career, careers, apprentice, apprenticeship, salary, hiring, employment, labourer, course, training, tafe, how to become, seek
- **Meaning / DIY:** definition, meaning, diy, how to build, specifications, owner builder, free plans, free house plans
- **Other trades (people in these suburbs search all of these):** boat, boats, engine, pool, pools, shed, sheds, patio, patios, pergola, deck, decking, fence, fencing, kitchen, kitchens, bathroom, carport, roof, roofing, gutter, concrete, retaining wall, landscaping, cabinet, cabinet maker, plumber, electrician, painter, tiler, handyman, carpenter, repairs, repair, maintenance
- **Not a new home (Nathan to confirm):** renovation, renovations, renovate, granny flat, granny flats, extension, extensions
- **Wrong product:** kit home, kit homes, transportable, prefab, tiny house, container home, house and land, house and land package, townhouse, apartment, unit, commercial, industrial, warehouse, fitout, shopfitting, developer, developers, subdivision, display home, display homes
- **Supplies:** merchants, builders merchants, supplies, hardware, bunnings, timber
- **Price shoppers:** cheap, cheapest, budget builder
- **Wrong place:** sydney, melbourne, gold coast, sunshine coast, toowoomba, ipswich, logan, north brisbane, brisbane north, northside, western suburbs, nsw, victoria, vic, perth, adelaide, birmingham, uk, california, chennai
- **Volume builders' names (no conquesting yet):** metricon, mccarthy, hutchinson, cj homes, plantation homes, coral homes, stroud, ownit, creation homes, clarendon, gj gardner, g j gardner, orbit homes, meadan, dixon homes, hotondo
- **Trouble, not buyers:** liquidation, insolvency, qcat, lawyer, dispute, complaint, complaints
- **Other jobs that aren't building:** demolition contractor, demolition company, asbestos removal, excavation, bobcat, skip bin, rubbish removal, building inspection, building inspector, pest inspection, certifier
- **Not a builder at all:** gym, fitness, physio, lego, minecraft, game, pc build, computer

## Assets (whole campaign)

- **Sitelinks:** Book a Walk-Through → `/contact/` · Meet the Team → `/meet-the-team/` · Client Testimonials → `/testimonials/` · Our Home Designs → `/designs/` · Can We Knock It Down? → `/can-we-knock-it-down/`
- **Callouts:** Family Owned Since 1990 · Master Builders Member · QBCC 15486557 · Bayside & Redlands · Based in Ransome · Knockdown Rebuilds
- **Structured snippets:** Neighbourhoods: Wynnum, Manly, Lota, Capalaba, Birkdale, Gumdale, Wakerley · Models: Killarney, Waderbird, Belmont, Chelsea, Clarence
- **Call:** 0422 831 306 (Nathan's mobile, per client-facts)
- **Location:** the Business Profile (see Google Maps above)

## Before it turns on

1. Site on sabreconstructions.com.au, `noindex` off (ads never point at github.io)
2. Google tag + *Submit lead form* conversion firing on the form's success state; call conversions on
3. One real test enquiry lands in admin@
4. Keyword Planner run inside Sabre's account: real volumes + bids; drop anything with no volume
5. Nathan confirms the claims in the ads: "Talk to Nathan Directly" (brand group) and the walk-through
6. Nathan decides: renovations / extensions / granny flats stay blocked?
