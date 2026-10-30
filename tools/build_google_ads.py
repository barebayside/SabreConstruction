"""Build Sabre's general Google Ads campaign from one source of truth (this file).

Outputs (all regenerated, never hand-edit them):
  marketing/google-ads/general-campaign.md        the plan, for Edward + Nathan
  marketing/google-ads/general-campaign.html      sign-off page (OK / change per ad group)
  marketing/google-ads/editor/*.csv               Google Ads Editor import (campaign, ad groups,
                                                  keywords, negatives, ads) - all PAUSED
  BBL docs/registry/marketing-assets/<CODE>/      one registry record per ad group (--registry)

Facts used in ads come only from ../sabre-constructions-website/docs/client-facts.md.
Research behind the keywords: docs/sessions/2026-10-30-gads-*.json (pulled 2026-10-30).

Run:  python tools/build_google_ads.py            (plan + html + csv)
      python tools/build_google_ads.py --registry (also writes/updates the BBL registry records)
"""
import csv, html, json, pathlib, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "marketing" / "google-ads"
BBL = pathlib.Path.home() / "OneDrive" / "Desktop" / "Marketing AI content for Bare Bayside Labs"
REG = BBL / "docs" / "registry" / "marketing-assets"
TODAY = "2026-10-30"

CAMPAIGN = "sab-knockdown-rebuild-2026"
SITE = "https://sabreconstructions.com.au"
MOBILE = "0422 831 306"

SUBURBS = ["Wynnum", "Wynnum West", "Manly", "Manly West", "Lota", "Wakerley", "Gumdale",
           "Capalaba", "Birkdale", "Hemmant", "Murarrie", "Tingalpa", "Ransome"]
POSTCODES = {"4154": "Gumdale, Ransome, Wakerley", "4157": "Capalaba", "4159": "Birkdale",
             "4172": "Murarrie", "4173": "Tingalpa", "4174": "Hemmant",
             "4178": "Wynnum, Wynnum West", "4179": "Manly, Manly West, Lota"}

SETTINGS = [
    ("Campaign name", CAMPAIGN),
    ("Type", "Search only. Display Network OFF, Search partners OFF"),
    ("Locations", "The 13 suburbs by name (postcode fallback below). Presence: people IN or regularly in these places, NOT 'interested in'"),
    ("Language", "English"),
    ("Bidding, week 1", "Maximise clicks with a max CPC cap (set from Nathan's budget on build day). Switch to Maximise conversions once ~15 form/call conversions are recorded"),
    ("Daily budget", "From Nathan's monthly budget ÷ 30.4. Proposal was ~$30–50/day across Google + Meta"),
    ("Ad schedule", "All days. Calls go to Nathan's mobile: call asset limited to the hours he'll answer (ask)"),
    ("Turn OFF", "AI Max / automatically created assets / final URL expansion / auto-apply recommendations / broad match"),
    ("Conversions (before any spend)", "Submit lead form (page-load snippet on the form's success state) · Calls from ads · Clicks on the phone number"),
    ("Status", "Everything built PAUSED. Turned on only after the gates (real domain, test enquiry, conversions firing)"),
]

# ---------------------------------------------------------------- ad groups
# Each ad group = one registry code. keywords: (text, match) with match in {"P","E"}.
def kw(terms, both=True):
    out = []
    for t in terms:
        out.append((t, "P"))
        if both:
            out.append((t, "E"))
    return out

def per_suburb(templates, subs):
    return [t.format(s=s.lower()) for s in subs for t in templates]

BUILDER_T = ["builders {s}", "home builders {s}", "house builders {s}", "new home builders {s}",
             "builder {s}", "local builders {s}", "small builders {s}", "custom home builder {s}"]

COMMON_H = ["Family Builder Since 1990", "Master Builders QLD Member", "QBCC Licence 15486557",
            "Family-Owned, Based in Ransome", "Book a Walk-Through", "Stay on the Street You Love",
            "Rated 4.5 From 12 Reviews", "Bayside and Redlands Only"]
COMMON_D = [
    "Family-owned builder on Brisbane's Bayside since 1990. Book a walk-through today.",
    "Master Builders Queensland member. QBCC 15486557. Building across Bayside and Redlands.",
    "Keep the street, the school and the neighbours. Rebuild the house around your family.",
]

GROUPS = [
    dict(
        code="SAB-SOL-KDR-2.0A_GOOGLE_SEARCH", name="Knockdown rebuild",
        why="The main buying search. Nobody types a suburb with it (Google suggests 'knock down rebuild builders brisbane', never '… wynnum'), so we bid on the Brisbane-wide words and let the 13-suburb location setting do the narrowing. Rivals bidding these pay for all of Brisbane; Sabre only pays for its pocket.",
        page="/", page_code="SAB-AWR-KDR-1.0A_WEB_HOMEPAGE",
        keywords=kw(["knockdown rebuild", "knock down rebuild", "knock down and rebuild",
                     "knockdown rebuild brisbane", "knock down rebuild brisbane",
                     "knock down and rebuild brisbane", "knock down rebuild builders",
                     "knockdown rebuild builders brisbane", "knock down rebuild builders brisbane",
                     "knockdown rebuild bayside", "knock down rebuild bayside",
                     "knockdown rebuild brisbane southside", "demolish and rebuild",
                     "demolish and rebuild brisbane", "knock down rebuild near me",
                     "knockdown rebuild builder near me", "best knockdown rebuild brisbane",
                     "knockdown rebuild brisbane reviews"]),
        negatives=["cost", "costs", "price", "prices", "calculator", "how much"],
        neg_why="Cost searches go to their own ad group (the cost article), not the home page.",
        pin1=["Knockdown Rebuild Builders", "Knock Down & Rebuild", "Knockdown Rebuild, Bayside"],
        headlines=["Knockdown Rebuild Brisbane", "Same Street. Whole New House", "Build Your Family Home"],
        descs=["Knock down the old house, keep the street. A Bayside family builder since 1990."],
        path=("rebuild", "bayside"), enable="week 1"),
    dict(
        code="SAB-SOL-KDR-3.0A_GOOGLE_SEARCH", name="Builders · Wynnum side",
        why="'builders <suburb>' is where the long tail lives: almost no ads on these in our check, and the related searches are buyers ('small builders wynnum qld', 'builders wynnum qld reviews', 'independent home builders wynnum qld'). Lands on the Wynnum page so the ad and page say the same suburb.",
        page="/wynnum/", page_code="SAB-AWR-KDR-2.0A_WEB_PAGE",
        keywords=kw(per_suburb(BUILDER_T, ["Wynnum", "Wynnum West", "Hemmant", "Murarrie", "Tingalpa"])
                    + ["builders wynnum manly", "builders wynnum qld reviews", "best builders wynnum",
                       "independent home builders wynnum", "builders wynnum qld"]),
        negatives=[], neg_why="",
        pin1=["Builders in Wynnum", "Wynnum Home Builders", "Tingalpa & Murarrie Builder"],
        headlines=["Local Builder, Wynnum West", "Hemmant & Wynnum Builder", "Small Family Builder"],
        descs=["A small family builder minutes from Wynnum. New homes and knockdown rebuilds."],
        path=("builders", "wynnum"), enable="week 1"),
    dict(
        code="SAB-SOL-KDR-4.0A_GOOGLE_SEARCH", name="Builders · Manly side",
        why="Same long-tail play for Manly, Manly West and Lota, on the Manly page.",
        page="/manly/", page_code="SAB-AWR-KDR-3.0A_WEB_PAGE",
        keywords=kw(per_suburb(BUILDER_T, ["Manly", "Manly West", "Lota"])
                    + ["builders manly qld", "builders manly qld reviews", "best builders manly",
                       "home builders manly qld"]),
        negatives=["nsw", "sydney", "northern beaches", "manly vale", "manly beach"],
        neg_why="Manly NSW (Sydney) is the bigger Manly. Location settings stop most of it; these stop the rest.",
        pin1=["Builders in Manly", "Manly Home Builders", "Manly & Lota Builder"],
        headlines=["Local Builder, Manly West", "Lota Home Builders", "Small Family Builder"],
        descs=["A small family builder minutes from Manly. New homes and knockdown rebuilds."],
        path=("builders", "manly"), enable="week 1"),
    dict(
        code="SAB-SOL-KDR-5.0A_GOOGLE_SEARCH", name="Builders · Capalaba, Birkdale, Ransome side",
        why="The Redlands edge and Sabre's own suburb (Ransome). The only suburb searches where a rival ad showed (Gumdale, Birkdale: Orbit, Meadan) are volume builders; a local family builder stands out next to them.",
        page="/", page_code="SAB-AWR-KDR-1.0A_WEB_HOMEPAGE",
        keywords=kw(per_suburb(BUILDER_T, ["Capalaba", "Birkdale", "Ransome", "Gumdale", "Wakerley"])
                    + ["builders capalaba qld", "small builders capalaba"]),
        negatives=[], neg_why="",
        pin1=["Builders in Capalaba", "Birkdale Home Builders", "Ransome & Gumdale Builder"],
        headlines=["Wakerley Home Builders", "Based Right Here in Ransome", "Small Family Builder"],
        descs=["Based in Ransome, building across Capalaba, Birkdale, Gumdale and Wakerley."],
        path=("builders", "capalaba"), enable="week 1"),
    dict(
        code="SAB-SOL-KDR-6.0A_GOOGLE_SEARCH", name="Bayside + Redlands home builders",
        why="The area-wide words families use ('bayside builders brisbane', 'home builders redlands', 'custom home builders brisbane bayside'). Shown only inside the 13 suburbs. 'Small' and 'independent' are the avatar's own words from the 09-05 research.",
        page="/", page_code="SAB-AWR-KDR-1.0A_WEB_HOMEPAGE",
        keywords=kw(["bayside builders", "bayside builders brisbane", "home builders brisbane bayside",
                     "custom home builders brisbane bayside", "custom home builders bayside",
                     "builders brisbane bayside", "home builders redlands", "builders redlands",
                     "new home builders redlands", "custom home builders redlands",
                     "house builders redlands", "builders brisbane southside",
                     "small builders brisbane", "independent builders brisbane",
                     "family builder brisbane", "local builder brisbane", "builders near me",
                     "home builders near me", "new home builders near me"]),
        negatives=["bayside council", "bayside vic", "bayside melbourne", "brighton"],
        neg_why="'Bayside' is also a Melbourne council.",
        pin1=["Bayside Home Builders", "Custom Home Builder, Bayside", "Redlands Home Builder"],
        headlines=["Independent Local Builder", "Small Family Builder", "Build Your Family Home"],
        descs=["An independent family builder, not a volume builder. Bayside and Redlands only."],
        path=("builders", "bayside"), enable="week 1"),
    dict(
        code="SAB-SOL-KDR-7.0A_GOOGLE_SEARCH", name="Sabre's own name",
        why="Cheap insurance. When someone sees a Sabre sign or Facebook ad and Googles the name, a rival can't sit above Sabre on its own name. Sabre isn't on page one for anything yet (the new site is hidden until the domain moves).",
        page="/", page_code="SAB-AWR-KDR-1.0A_WEB_HOMEPAGE",
        keywords=kw(["sabre constructions", "sabre construction", "sabre builders",
                     "sabre constructions ransome", "sabre constructions capalaba",
                     "sabre constructions brisbane", "sabre homes brisbane"]),
        negatives=["sabre sports", "sword", "lightsaber", "fencing club"],
        neg_why="Other 'Sabres'.",
        pin1=["Sabre Constructions", "Sabre Constructions, Ransome"],
        headlines=["Official Site", "Talk to Nathan Directly", "Bayside Home Builder"],
        descs=["Sabre Constructions: family-owned Bayside builder since 1990. Call or book online."],
        path=("sabre",), enable="week 1"),
    dict(
        code="SAB-CON-KDR-6.0A_GOOGLE_SEARCH", name="Knockdown rebuild cost (long tail)",
        why="Cost is the biggest question in every search we've pulled ('knock down rebuild brisbane cost' and 'cost calculator' top the related searches; 11 of 16 'People also ask' on 09-05 were cost). Volume builders answer it with a price; Sabre answers it with the article 'what decides the cost', never a number. A cheap research click that starts the relationship. A TEST: if it brings clicks but no enquiries, pause it.",
        page="/blog/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/", page_code=None,
        keywords=kw(["knock down rebuild cost", "knockdown rebuild cost", "knock down rebuild brisbane cost",
                     "knockdown rebuild brisbane cost", "knock down rebuild prices brisbane",
                     "knockdown rebuild prices", "how much does a knock down rebuild cost",
                     "cost to knock down and rebuild a house", "is it cheaper to knock down and rebuild"]),
        negatives=["calculator", "sydney", "melbourne", "gold coast"],
        neg_why="'Calculator' searchers want a tool we don't have.",
        pin1=["What Decides Rebuild Cost?", "Knockdown Rebuild Costs", "Rebuild Costs, Explained"],
        headlines=["Before You Price a Rebuild", "Plain-English Answers", "Written by a Local Builder"],
        descs=["No price lists. What actually decides the cost of a knockdown rebuild in Brisbane."],
        path=("rebuild", "cost"), enable="stage 2, or week 1 if budget allows"),
    dict(
        code="SAB-CON-KDR-7.0A_GOOGLE_SEARCH", name="Can we knock it down?",
        why="The question before the rebuild: Brisbane's character overlay stops some pre-1947 houses coming down. Few builders answer it; Sabre's page does, then offers a block check. Brisbane City Council rules only, so it mostly matters on the Wynnum/Manly side.",
        page="/can-we-knock-it-down/", page_code="SAB-AWR-KDR-4.0A_WEB_PAGE",
        keywords=kw(["can i knock down my house brisbane", "can i demolish my house brisbane",
                     "can i knock down my house", "character overlay brisbane",
                     "traditional building character overlay", "pre 1947 house demolish",
                     "demolition approval brisbane", "can you knock down a pre 1947 house",
                     "is my house in a character overlay"]),
        negatives=["renovate", "extension", "heritage grant"],
        neg_why="",
        pin1=["Can You Knock It Down?", "Can We Knock Down Our House?", "Character Overlay Check"],
        headlines=["Pre-1947 House? Read This", "Check Before You Demolish", "Ask a Bayside Builder"],
        descs=["Some Brisbane houses can't legally come down. See what decides it for yours first."],
        path=("knock-it-down",), enable="stage 2"),
]

# ---------------------------------------------------------------- negatives (campaign list)
NEGATIVES = {
    "Jobs and training": ["job", "jobs", "career", "careers", "apprentice", "apprenticeship", "salary",
                          "hiring", "employment", "labourer", "course", "training", "tafe",
                          "how to become", "seek"],
    "Meaning / DIY": ["definition", "meaning", "diy", "how to build", "specifications", "owner builder",
                      "free plans", "free house plans"],
    "Other trades (people in these suburbs search all of these)":
        ["boat", "boats", "engine", "pool", "pools", "shed", "sheds", "patio", "patios", "pergola",
         "deck", "decking", "fence", "fencing", "kitchen", "kitchens", "bathroom", "carport",
         "roof", "roofing", "gutter", "concrete", "retaining wall", "landscaping", "cabinet",
         "cabinet maker", "plumber", "electrician", "painter", "tiler", "handyman", "carpenter",
         "repairs", "repair", "maintenance"],
    "Not a new home (Nathan to confirm)": ["renovation", "renovations", "renovate", "granny flat",
                                           "granny flats", "extension", "extensions"],
    "Wrong product": ["kit home", "kit homes", "transportable", "prefab", "tiny house", "container home",
                      "house and land", "house and land package", "townhouse", "apartment", "unit",
                      "commercial", "industrial", "warehouse", "fitout", "shopfitting", "developer",
                      "developers", "subdivision", "display home", "display homes"],
    "Supplies": ["merchants", "builders merchants", "supplies", "hardware", "bunnings", "timber"],
    "Price shoppers": ["cheap", "cheapest", "budget builder"],
    "Wrong place": ["sydney", "melbourne", "gold coast", "sunshine coast", "toowoomba", "ipswich",
                    "logan", "north brisbane", "brisbane north", "northside", "western suburbs",
                    "nsw", "victoria", "vic", "perth", "adelaide", "birmingham", "uk", "california",
                    "chennai"],
    "Volume builders' names (no conquesting yet)":
        ["metricon", "mccarthy", "hutchinson", "cj homes", "plantation homes", "coral homes", "stroud",
         "ownit", "creation homes", "clarendon", "gj gardner", "g j gardner", "orbit homes",
         "meadan", "dixon homes", "hotondo"],
    "Trouble, not buyers": ["liquidation", "insolvency", "qcat", "lawyer", "dispute", "complaint",
                            "complaints"],
    "Other jobs that aren't building": ["demolition contractor", "demolition company", "asbestos removal",
                                        "excavation", "bobcat", "skip bin", "rubbish removal",
                                        "building inspection", "building inspector", "pest inspection",
                                        "certifier"],
    "Not a builder at all": ["gym", "fitness", "physio", "lego", "minecraft", "game", "pc build",
                             "computer"],
}

SITELINKS = [("Book a Walk-Through", "/contact/", "Meet Nathan at your house", "No cost, no obligation"),
             ("Meet the Team", "/meet-the-team/", "The family behind Sabre", "Building since 1990"),
             ("Client Testimonials", "/testimonials/", "What our clients said", "In their own words"),
             ("Our Home Designs", "/designs/", "Six family home designs", "Start from a plan"),
             ("Can We Knock It Down?", "/can-we-knock-it-down/", "Check the rules first", "Character overlay")]
CALLOUTS = ["Family Owned Since 1990", "Master Builders Member", "QBCC 15486557", "Bayside & Redlands",
            "Based in Ransome", "Knockdown Rebuilds"]
SNIPPETS = [("Neighbourhoods", ["Wynnum", "Manly", "Lota", "Capalaba", "Birkdale", "Gumdale", "Wakerley"]),
            ("Models", ["Killarney", "Waderbird", "Belmont", "Chelsea", "Clarence"])]

RESEARCH = """\
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
"""

# ---------------------------------------------------------------- checks
def check():
    errs = []
    for g in GROUPS:
        for h in g["pin1"] + g["headlines"] + COMMON_H:
            if len(h) > 30: errs.append(f"{g['code']} headline >30: {h} ({len(h)})")
        for d in g["descs"] + COMMON_D:
            if len(d) > 90: errs.append(f"{g['code']} description >90: {d} ({len(d)})")
        for p in g["path"]:
            if len(p) > 15: errs.append(f"{g['code']} path >15: {p}")
        if len(g["pin1"] + g["headlines"] + COMMON_H) > 15: errs.append(f"{g['code']} >15 headlines")
        if len(g["descs"] + COMMON_D) > 4: errs.append(f"{g['code']} >4 descriptions")
        neg = {n for v in NEGATIVES.values() for n in v} | set(g["negatives"])
        for t, _ in g["keywords"]:
            words = f" {t} "
            hit = [n for n in neg if f" {n} " in words]
            if hit: errs.append(f"{g['code']} keyword '{t}' blocked by negative {hit}")
    for t, _, a, b in SITELINKS:
        if len(t) > 25 or len(a) > 35 or len(b) > 35: errs.append(f"sitelink too long: {t}")
    for c in CALLOUTS:
        if len(c) > 25: errs.append(f"callout >25: {c}")
    if errs:
        sys.exit("CHECK FAILED\n" + "\n".join(errs))


def url(g):
    return (f"{SITE}{g['page']}?utm_source=google&utm_medium=cpc&utm_campaign={CAMPAIGN}"
            f"&utm_content={g['code']}")


def all_h(g):
    return g["pin1"] + g["headlines"] + COMMON_H


def all_d(g):
    return g["descs"] + COMMON_D

# ---------------------------------------------------------------- outputs
def write_md():
    L = [f"# Sabre · general Google Ads campaign (`{CAMPAIGN}`)", "",
         f"`status: draft for sign-off` · built {TODAY} by `tools/build_google_ads.py` (edit the script, not this file)",
         "", "Edward signs off → Nathan's account is linked → Claude builds it in Google Ads, **paused**.",
         "", "## What the research found", "", RESEARCH, "## Campaign settings", "",
         "| Setting | Value |", "|---|---|"]
    L += [f"| {a} | {b} |" for a, b in SETTINGS]
    L += ["", "**The 13 suburbs:** " + " · ".join(SUBURBS), "",
          "**Postcode fallback** (if a suburb isn't in Google's list): " +
          " · ".join(f"{k} ({v})" for k, v in POSTCODES.items()), "",
          "## Google Maps", "",
          "1. **Ads on Maps** need a *location asset*: link Sabre's Google Business Profile to the Ads account "
          "(Assets → Location → link the Business Profile). Without it, ads never show on Maps.",
          "2. **The free map box** is the Business Profile itself: primary category *Home builder*, secondary "
          "*Custom home builder*, the 13 suburbs as the service area, address **40 Molle Rd, Ransome QLD 4154** "
          "(it still says Capalaba), phone matching the site, the new website link, photos. Needs Edward as manager.",
          "", "## Ad groups (ad group name = the code)", ""]
    for g in GROUPS:
        L += [f"### {g['name']} · `{g['code']}`", "", g["why"], "",
              f"- **Lands on:** `{g['page']}` · **turn on:** {g['enable']}",
              f"- **Final URL:** `{url(g)}`",
              f"- **Keywords** ({len(g['keywords'])}, \"phrase\" and [exact]): " +
              ", ".join(f'"{t}"' if m == "P" else f"[{t}]" for t, m in g["keywords"]), ""]
        if g["negatives"]:
            L += [f"- **Ad-group negatives:** {', '.join(g['negatives'])}" + (f". {g['neg_why']}" if g['neg_why'] else ""), ""]
        L += ["- **Headlines** (pin 1 = first three):"]
        L += [f"  {i}. {h} ({len(h)}){' [pin 1]' if h in g['pin1'] else ''}" for i, h in enumerate(all_h(g), 1)]
        L += ["- **Descriptions:**"] + [f"  {i}. {d} ({len(d)})" for i, d in enumerate(all_d(g), 1)]
        L += [f"- **Display path:** sabreconstructions.com.au/{'/'.join(g['path'])}", ""]
    L += ["## Negative keywords (one shared list on the campaign, phrase match)", ""]
    for k, v in NEGATIVES.items():
        L += [f"- **{k}:** {', '.join(v)}"]
    L += ["", "## Assets (whole campaign)", "",
          "- **Sitelinks:** " + " · ".join(f"{t} → `{p}`" for t, p, _, _ in SITELINKS),
          "- **Callouts:** " + " · ".join(CALLOUTS),
          "- **Structured snippets:** " + " · ".join(f"{h}: {', '.join(v)}" for h, v in SNIPPETS),
          f"- **Call:** {MOBILE} (Nathan's mobile, per client-facts)",
          "- **Location:** the Business Profile (see Google Maps above)", "",
          "## Before it turns on", "",
          "1. Site on sabreconstructions.com.au, `noindex` off (ads never point at github.io)",
          "2. Google tag + *Submit lead form* conversion firing on the form's success state; call conversions on",
          "3. One real test enquiry lands in admin@",
          "4. Keyword Planner run inside Sabre's account: real volumes + bids; drop anything with no volume",
          "5. Nathan confirms the claims in the ads: \"Talk to Nathan Directly\" (brand group) and the walk-through",
          "6. Nathan decides: renovations / extensions / granny flats stay blocked?", ""]
    (OUT / "general-campaign.md").write_text("\n".join(L), encoding="utf-8")


def write_csv():
    d = OUT / "editor"
    d.mkdir(parents=True, exist_ok=True)
    rows = lambda name, head, body: _w(d / name, head, body)
    rows("1-campaign.csv", ["Campaign", "Campaign Type", "Networks", "Campaign Status", "Languages", "Bid Strategy Type"],
         [[CAMPAIGN, "Search", "Google search", "Paused", "en", "Maximize clicks"]])
    rows("2-ad-groups.csv", ["Campaign", "Ad Group", "Ad Group Status"],
         [[CAMPAIGN, g["code"], "Paused"] for g in GROUPS])
    rows("3-keywords.csv", ["Campaign", "Ad Group", "Keyword", "Criterion Type", "Status"],
         [[CAMPAIGN, g["code"], t, "Phrase" if m == "P" else "Exact", "Enabled"] for g in GROUPS for t, m in g["keywords"]]
         + [[CAMPAIGN, g["code"], n, "Negative Phrase", ""] for g in GROUPS for n in g["negatives"]])
    rows("4-campaign-negatives.csv", ["Campaign", "Keyword", "Criterion Type"],
         [[CAMPAIGN, n, "Campaign Negative Phrase"] for v in NEGATIVES.values() for n in v])
    head = (["Campaign", "Ad Group", "Ad type", "Status", "Final URL", "Path 1", "Path 2"]
            + [f"Headline {i}" for i in range(1, 16)] + [f"Headline {i} position" for i in range(1, 16)]
            + [f"Description {i}" for i in range(1, 5)])
    body = []
    for g in GROUPS:
        hs, ds = all_h(g), all_d(g)
        p = list(g["path"]) + [""] * (2 - len(g["path"]))
        body.append([CAMPAIGN, g["code"], "Responsive search ad", "Paused", url(g), p[0], p[1]]
                    + hs + [""] * (15 - len(hs))
                    + ["1" if h in g["pin1"] else "" for h in hs] + [""] * (15 - len(hs))
                    + ds + [""] * (4 - len(ds)))
    rows("5-ads.csv", head, body)
    rows("6-locations.csv", ["Campaign", "Location", "Postcode fallback"],
         [[CAMPAIGN, f"{s}, Queensland, Australia", next((k for k, v in POSTCODES.items() if s in v), "")] for s in SUBURBS])


def _w(path, head, body):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(body)


def write_html():
    e = html.escape
    cards = []
    for g in GROUPS:
        kws = "".join(f'<span class="k">{e(t)}</span>' for t, m in g["keywords"] if m == "P")
        hs = "".join(f"<li>{e(h)}{' <b class=pin>pin 1</b>' if h in g['pin1'] else ''}</li>" for h in all_h(g))
        ds = "".join(f"<li>{e(d)}</li>" for d in all_d(g))
        neg = f'<p class="sm"><b>Also blocked here:</b> {e(", ".join(g["negatives"]))}</p>' if g["negatives"] else ""
        cards.append(f"""
<div class="card" data-q="{e(g['code'])}">
  <div class="top"><div><div class="code">{e(g['code'])}</div><h3>{e(g['name'])}</h3></div>
  <span class="on">On: {e(g['enable'])}</span></div>
  <p>{e(g['why'])}</p>
  <div class="ad"><div class="sp">Sponsored</div><div class="url">sabreconstructions.com.au › {e(' › '.join(g['path']))}</div>
  <div class="hl">{e(g['pin1'][0])} | {e(g['headlines'][0])} | {e(COMMON_H[0])}</div>
  <div class="ds">{e(g['descs'][0])} {e(COMMON_D[2])}</div></div>
  <p class="sm"><b>Lands on</b> <code>{e(g['page'])}</code> · <b>{len(g['keywords'])//2}</b> searches, each as "phrase" and [exact]</p>
  <details><summary>Keywords</summary><div class="ks">{kws}</div>{neg}</details>
  <details><summary>All 15 headlines + 4 descriptions</summary><ol>{hs}</ol><ol>{ds}</ol></details>
  <div class="q"><span class="opts"><button class="ok">OK</button><button class="ch">Change</button></span><input placeholder="Notes"></div>
</div>""")
    negs = "".join(f"<div class='box'><h4>{e(k)}</h4><p>{e(', '.join(v))}</p></div>" for k, v in NEGATIVES.items())
    sets = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in SETTINGS)
    research = "".join(f"<li>{e(x.strip('- ').replace('**',''))}</li>" for x in RESEARCH.split("\n- ")[1:])
    subs = "".join(f"<span>{e(s)}</span>" for s in SUBURBS)
    n_kw = sum(len(g["keywords"]) for g in GROUPS)
    n_neg = sum(len(v) for v in NEGATIVES.values())
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sabre Google Ads Plan</title>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#F8F7F4;--ink:#1B1C1F;--soft:#5d5f66;--line:#e3e0d8;--red:#EB2227;--green:#1f8a4c;--amber:#b7791f}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 Figtree,Arial,sans-serif}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 16px}}header{{background:var(--ink);color:#fff;padding:36px 0 28px}}
.eyebrow{{color:#ff8b8e;font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600}}
h1{{font-size:31px;margin:8px 0;font-weight:600}}header p{{color:#c9cad0;margin:0;max-width:760px}}
.stats{{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}}.stats span{{background:#2c2d31;border-radius:99px;padding:5px 12px;font-size:14px}}
.bar{{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--line)}}.bar .wrap{{display:flex;gap:8px;padding:10px 16px;overflow-x:auto;align-items:center}}
.bar a{{white-space:nowrap;text-decoration:none;color:var(--ink);font-size:14px;padding:6px 12px;border-radius:99px;border:1px solid var(--line);background:#fff}}.bar .sp{{flex:1}}
button{{font:inherit;font-size:14px;font-weight:600;border:1px solid var(--line);background:#fff;border-radius:8px;padding:6px 12px;cursor:pointer}}
button.primary{{background:var(--red);border-color:var(--red);color:#fff;white-space:nowrap}}
section{{padding:30px 0 4px;scroll-margin-top:60px}}h2{{font-size:24px;margin:0 0 8px;font-weight:600}}
.card{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin-bottom:16px}}
.top{{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}}.code{{font-family:Consolas,monospace;font-size:12.5px;color:var(--soft)}}
h3{{margin:2px 0 6px;font-size:19px;font-weight:600}}.on{{font-size:12.5px;font-weight:700;background:#e4f4ea;color:var(--green);border-radius:99px;padding:3px 10px;white-space:nowrap}}
.ad{{border:1px solid #dadce0;border-radius:10px;padding:12px 14px;font-family:Arial,sans-serif;margin:10px 0;max-width:620px}}
.ad .sp{{font-size:12px;font-weight:700}}.ad .url{{font-size:12.5px;color:#4d5156}}.ad .hl{{color:#1a0dab;font-size:18px;line-height:1.3}}.ad .ds{{color:#4d5156;font-size:14px}}
.sm{{font-size:14.5px;color:var(--soft);margin:6px 0}}details{{margin:6px 0}}summary{{cursor:pointer;font-weight:600;font-size:14.5px}}
.ks{{display:flex;flex-wrap:wrap;gap:5px;margin:8px 0}}.k{{font-size:13px;background:#f1efe9;border-radius:6px;padding:2px 8px}}
.pin{{font-size:11px;background:#fde8e8;color:var(--red);border-radius:4px;padding:1px 5px}}ol{{font-size:14.5px;margin:6px 0}}
.q{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;border-top:1px dashed var(--line);padding-top:10px}}.q input{{flex:1 1 260px;font:inherit;font-size:14.5px;padding:6px 10px;border:1px solid var(--line);border-radius:8px}}
.q button.on.ok{{background:var(--green);border-color:var(--green);color:#fff}}.q button.on.ch{{background:var(--amber);border-color:var(--amber);color:#fff}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:12px}}.box{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px}}
.box h4{{margin:0 0 4px;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--soft)}}.box p{{margin:0;font-size:14px}}
table{{width:100%;border-collapse:collapse;font-size:14.5px;background:#fff}}td{{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}}td:first-child{{font-weight:600;width:28%}}
.tw{{border:1px solid var(--line);border-radius:10px;overflow:hidden}}.subs{{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}}.subs span{{background:var(--ink);color:#fff;border-radius:99px;padding:4px 11px;font-size:14px}}
.flag{{background:#fff6e5;border:1px solid #f1d9a8;border-radius:10px;padding:12px 16px;font-size:15px;margin:10px 0}}
ul.r li{{margin:5px 0}}.toast{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);background:var(--ink);color:#fff;padding:10px 16px;border-radius:8px;opacity:0;transition:.2s}}.toast.show{{opacity:1}}
footer{{color:var(--soft);font-size:13px;padding:20px 0 40px}}
</style></head><body>
<header><div class="wrap"><div class="eyebrow">Sabre Constructions · Google Ads · general campaign · for sign-off</div>
<h1>Be found by families searching for a builder in the pocket</h1>
<p>13 suburbs, 8 ad groups, every ad group named by its registry code. Built paused, and turned on only when the real domain, tracking and a test enquiry are proven.</p>
<div class="stats"><span>{len(SUBURBS)} suburbs</span><span>{len(GROUPS)} ad groups</span><span>{n_kw} keywords</span><span>{n_neg} negative keywords</span><span>campaign: {e(CAMPAIGN)}</span></div></div></header>
<div class="bar"><div class="wrap"><a href="#research">Research</a><a href="#where">Where</a><a href="#groups">Ad groups</a><a href="#neg">Negatives</a><a href="#maps">Google Maps</a><a href="#settings">Settings</a><span class="sp"></span><button class="primary" id="copy">Copy sign-off</button></div></div>
<main class="wrap">
<section id="research"><h2>What the research found</h2><div class="card"><ul class="r">{research}</ul></div></section>
<section id="where"><h2>Where the ads show</h2><div class="card"><div class="subs">{subs}</div>
<p class="sm">Only people <b>in</b> these suburbs or regularly there. That's the cheap trick: we can bid on Brisbane-wide words like "knockdown rebuild brisbane", and Google only shows (and charges for) the ad inside the pocket.</p></div></section>
<section id="groups"><h2>The 8 ad groups</h2>{''.join(cards)}</section>
<section id="neg"><h2>Negative keywords: searches we never pay for</h2><div class="grid">{negs}</div>
<div class="flag">Nathan to decide: should <b>renovations, extensions and granny flats</b> stay blocked? Leanne's job was an extension.</div></section>
<section id="maps"><h2>Google Maps</h2><div class="grid">
<div class="box"><h4>Ads on Maps</h4><p>Link Sabre's Google Business Profile to the Ads account as a location asset. Without it, ads never appear on Maps.</p></div>
<div class="box"><h4>The free map box</h4><p>The Business Profile itself: category Home builder (+ Custom home builder), the 13 suburbs as the service area, address 40 Molle Rd Ransome (it still says Capalaba), the new website, photos, reviews. Needs Edward as manager.</p></div></div>
<div id="mapfind"></div></section>
<section id="settings"><h2>Campaign settings</h2><div class="tw"><table>{sets}</table></div></section>
</main>
<footer class="wrap">Generated by <code>tools/build_google_ads.py</code> on {TODAY}. Plan: <code>marketing/google-ads/general-campaign.md</code> · import files: <code>marketing/google-ads/editor/</code></footer>
<div class="toast" id="toast"></div>
<script>
const KEY='sabre-gads-signoff';let st={{}};try{{st=JSON.parse(localStorage.getItem(KEY))||{{}}}}catch(e){{}}
const save=()=>{{try{{localStorage.setItem(KEY,JSON.stringify(st))}}catch(e){{}}}};
document.querySelectorAll('.card[data-q]').forEach(c=>{{const id=c.dataset.q,s=st[id]||{{}};const[ok,ch]=c.querySelectorAll('.opts button');const i=c.querySelector('.q input');i.value=s.note||'';
const paint=()=>{{ok.classList.toggle('on',s.pick==='ok');ch.classList.toggle('on',s.pick==='ch')}};paint();
ok.onclick=()=>{{s.pick=s.pick==='ok'?null:'ok';st[id]=s;save();paint()}};ch.onclick=()=>{{s.pick=s.pick==='ch'?null:'ch';st[id]=s;save();paint()}};i.oninput=()=>{{s.note=i.value;st[id]=s;save()}}}});
document.getElementById('copy').onclick=async()=>{{let o='# Google Ads sign-off\\n';document.querySelectorAll('.card[data-q]').forEach(c=>{{const s=st[c.dataset.q]||{{}};o+=`- ${{c.dataset.q}} (${{c.querySelector('h3').textContent}}): **${{s.pick==='ok'?'OK':s.pick==='ch'?'CHANGE':'—'}}**${{s.note?' — '+s.note:''}}\\n`}});
const t=document.getElementById('toast');try{{await navigator.clipboard.writeText(o);t.textContent='Copied. Paste it back to Claude'}}catch(e){{t.textContent='Copy failed'}}t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1800)}};
</script></body></html>"""
    (OUT / "general-campaign.html").write_text(page, encoding="utf-8")


def write_registry():
    for g in GROUPS:
        code = g["code"]
        d = REG / code
        d.mkdir(exist_ok=True)
        mp = d / "meta.json"
        old = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else None
        stage, prod = code.split("-")[1], code.split("-")[2]
        seq, rest = code.split("-")[3].split(".", 1)
        body = ("HEADLINES\n" + "\n".join(f"{i}. {h} ({len(h)}){' [pin 1]' if h in g['pin1'] else ''}" for i, h in enumerate(all_h(g), 1))
                + "\n\nDESCRIPTIONS\n" + "\n".join(f"D{i}. {x} ({len(x)})" for i, x in enumerate(all_d(g), 1)))
        meta = {
            "code": code, "business_line": "SAB", "stage": stage, "product": prod,
            "sequence": int(seq), "version": f"{seq}.{rest[0]}", "variant": rest[1], "platform": "GOOGLE",
            "format": "SEARCH", "campaign": CAMPAIGN, "strategy": "SAB-CONTROL",
            "leads_to": [g["page_code"]] if g["page_code"] else ["SAB-LEAD"], "funding": "PAID",
            "status": "Draft", "launched_date": None, "paused_date": None, "winner_decided_date": None,
            "linked_landing_page_code": g["page_code"], "linked_from_assets": [],
            "paired_with": [x["code"] for x in GROUPS if x is not g], "variant_change": None,
            "utm_content": code, "creative_file": None, "creative_master": None,
            "headline": g["pin1"][0], "body": body,
            "cta_text": f"(search ad - no button; call asset {MOBILE})", "cta_destination": url(g),
            "subject": None, "preview_text": None, "day_in_sequence": None,
            "scoring_hooks": g["name"], "analytics_embed_url": None,
            "lead_mechanism": "search-intent-in-the-pocket", "tests_targeted": ["Fit", "Proof", "Now"],
            "test_failed": None, "results": [],
            "status_history": [{"date": TODAY, "status": "Draft", "reason": "Created - code issued before the ad group exists in Google (registry rule). Built by Sabre tools/build_google_ads.py from the 2026-10-30 keyword research."}],
            "change_log": [],
        }
        if old:  # keep history and results; refresh the content fields
            for k in ("status", "launched_date", "paused_date", "winner_decided_date", "results",
                      "status_history", "change_log", "test_failed"):
                meta[k] = old.get(k, meta[k])
        mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        kws = ", ".join(f'"{t}"' if m == "P" else f"[{t}]" for t, m in g["keywords"])
        (d / "copy.md").write_text(
            f"# {code}\n\n**Status:** {meta['status']}\n**Created:** {TODAY}\n**Campaign:** {CAMPAIGN} · "
            f"**Name on the platform:** `{code}` (ad group name)\n\n## Headline\n\n{g['pin1'][0]}\n\n"
            f"**Ad group:** {g['name']}\n**Keywords:** {kws}\n"
            + (f"**Ad-group negatives:** {', '.join(g['negatives'])}\n" if g["negatives"] else "")
            + f"\n## Body\n\n{body}\n\n## CTA\n\n{meta['cta_text']}\n\n**Final URL:** {url(g)}\n", encoding="utf-8")
        (d / "notes.md").write_text(
            f"# {code} — notes\n\n{g['why']}\n\nTurn on: {g['enable']}. Campaign negatives, sitelinks, callouts, "
            f"snippets and settings: Sabre `marketing/google-ads/general-campaign.md` (built by "
            f"`tools/build_google_ads.py`). Research: Sabre `docs/sessions/2026-10-30-gads-*.json`.\n", encoding="utf-8")


if __name__ == "__main__":
    check()
    OUT.mkdir(parents=True, exist_ok=True)
    write_md(); write_csv(); write_html()
    if "--registry" in sys.argv:
        write_registry()
    print(f"OK: {len(GROUPS)} ad groups, {sum(len(g['keywords']) for g in GROUPS)} keywords, "
          f"{sum(len(v) for v in NEGATIVES.values())} campaign negatives")
