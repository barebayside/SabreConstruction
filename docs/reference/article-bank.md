# The article bank — every question Sabre answers, in the Project 24 shape

> **Layer 4 reference. Canonical from 2026-09-10.** This replaces §7 of
> `search-and-ai-visibility-plan.md`, which now points here. The plan still owns the
> technical side (robots, schema, GBP, measurement); this file owns *what gets written,
> in what order, and why*.
>
> Read `../../../sabre-constructions-website/docs/client-facts.md` (the REAL repo — the only
> copy) before writing a single line of any post.
> Rule 1 stands: **never invent a number.** Not a price, not a band, not a timeline.

---

## 0 · What is measured, and what is estimated

Two different kinds of number appear in this document. Do not confuse them.

### ✅ MEASURED — the 2026-09-05 SERP scrape

**39 real Google searches** were run and captured on 2026-09-05, Brisbane-anchored: 18
knockdown-rebuild-intent (`knockdown rebuild builder <suburb>`) and 21 builder-intent
(`builders <suburb>`, `custom home builders brisbane bayside`), across Wynnum, Manly, Lota,
Capalaba, Wakerley and the Bayside. Raw data:
`docs/sessions/2026-09-05-rank-check-knockdown-rebuild-top30.json` and
`…-builders-suburb-top30.json`. Google surfaced **104 unique related queries** and
**16 People Also Ask questions** across them.

**What it showed, in order of weight:**

| Theme | Queries | Appearances | The headline |
|---|---|---|---|
| **Cost and price** | 31 of 104 | **130** | The most-surfaced related query in the entire set is **"knock down rebuild cost calculator" (20)**, then **"knock down rebuild Brisbane cost" (16)**. And **11 of the 16 People Also Ask questions are cost questions** — the top one being *"Can I build a house for $300,000 in Australia?"* (5 SERPs) |
| **Suburb-anchored** | 62 of 104 | 192 | Every theme below repeats itself per suburb — "… capalaba", "… wynnum", "… manly qld", "… lota qld", "… wakerley". The suburb pages are not optional |
| **Reviews and "best"** | 15 | 46 | "builders wynnum reviews" (6), "knockdown rebuild builders brisbane bayside reviews" (6), "best custom home builders brisbane bayside" (4). People search a builder's reviews as a *query*, not just on the listing |
| **Packages and volume builders** | 5 | 38 | "knock down and rebuild packages" (12) and **"Metricon knockdown rebuild" (12)**. A named national competitor is inside the local search |
| **Small / independent / local** | 7 | 24 | "independent builders capalaba" (6), "small builders manly qld" (4), "small home builders wynnum" (4). Sabre's exact category, actively searched |

⚠️ **What an appearance count is, and is not.** It counts how often Google itself chose to
surface that query as "related" across the 39 SERPs. It is a **demand signal, not a search
volume** — it says Google associates the query with this topic strongly, not that N people
typed it. A high count means the query is central to how Google understands the topic, which
is what a content bank should be built around. It is not a number to bid against.

⚠️ **The scrape only covered builder-intent searches.** It says nothing about the living
cluster (Spiral 2) or the national contract cluster (Spiral 3). Every number attached to those
is an estimate.

### ≈ ESTIMATED — the bands

Everything not backed by the scrape is a band, not a measurement. **BBL has no keyword tool on
this account.** Google Ads is still not linked to manager 775-584-9139 (launch gate 3), so
Keyword Planner will not open until it is. The bands come from the shape of the query, the size
of the population that could ask it (Wynnum ≈ 12,000 people, Manly ≈ 3,000, Lota ≈ 2,500,
Brisbane 2.7 million, Australia 27 million), and what already holds page one.

| Band | Est. searches/month | What it means for us |
|---|---|---|
| **A** | 1,000+ | National head term. We will not rank soon; we write it for the topical spine and the AI answer |
| **B** | 300–1,000 | Contested. Worth a staple, not a response post |
| **C** | 100–300 | The sweet spot. A good post can own this inside six months |
| **D** | 30–100 | Long tail. Easy wins, real intent |
| **E** | 10–30 | Local long tail. Low volume, very high intent — a Wynnum family typing this is *months* from a decision |
| **F** | <10 | Almost no volume. Written only when it answers a real objection, or for the AI assistant that has no other source |

Confidence: **H** = the band is right. **M** = right band or one either side. **L** = a guess.
✅ in the Conf. column means **the 09-05 scrape backs this one** — those are not guesses.

⚠️ **Nothing here justifies an ad budget.** Bands decide *writing order*, nothing else. The
moment Keyword Planner opens, re-run this table and replace them with real ranges — a one-hour
job, worth doing before any pillar is written.

### What the measured data changes about the plan

1. **Cost is not one article, it is the spine.** Write S1 first, and make cost the thread that
   runs through the service page, the suburb pages and the FAQ blocks. Rule 1 still holds — what
   *decides* the cost, never a number.
2. **The calculator searchers are the biggest single group, and they are being badly served.**
   A calculator prices someone else's block. That is the hook, and the draft already carries it.
3. **"Metricon knockdown rebuild" sits inside the local search.** R15 is not a nice-to-have.
4. **Reviews are a query.** `/testimonials/` needs dates, names and a review link, and one of
   the suburb pages should carry a Wynnum review. Not a blog job — but it came out of this data.
5. **"Small" and "independent" are how the avatar describes what they want.** Use those words
   on the page. R16 targets them directly.

## 1 · The method — three spirals, three centrepieces

Income School's content spiral: pick a narrow topic, write ten posts that circle it,
put a centrepiece in the middle that links to all ten, then spiral outward to the next
topic. You do not start with the pillar. **The centrepiece is written last**, when the
spokes already exist and it has something to link to.

Sabre has three spirals. They overlap on purpose — that overlap is what makes a site
look like an authority on one subject rather than a blog about everything.

```
        SPIRAL 2                SPIRAL 1                 SPIRAL 3
     Living on the           Knocking it down        Dealing with a builder
       Bayside            and starting again           in Australia
          |                       |                          |
   "should we stay?"      "can we? how? what      "how does this actually
                            decides the cost?"        work, legally?"
          \_______________________|__________________________/
                                  |
                     every one of them ends at the
                          same door: the walk-through
```

**Spiral 1 is the money.** It is the search Sabre wants to be found for.
**Spiral 2 is the audience.** It catches the family a year *before* they search for a
builder, and it is the cluster that makes Sabre a local entity that AI assistants name.
**Spiral 3 is the trust.** It is national, generic, and it is what makes Sabre citable —
these are the passages an AI assistant lifts when someone asks "what should I check
before signing with a builder in Queensland?"

### The rules that apply to all three

- **One question per post. The title is the question. The answer is in the first 60 words.**
- A **134–167-word self-contained answer block** near the top. That is the passage an AI
  assistant lifts. It must make sense with nothing around it.
- H2 every 200–300 words, every H2 a question. A reader must get the whole article from
  the headings alone.
- 1–3 sentence paragraphs. Year 8 reading level. Australian English. "You" throughout.
- **Two attributed proof points per post** — Brisbane City Council's own wording, QBCC,
  Master Builders Queensland, the ABS, a named Google review. Never an unsourced number.
- A **Common questions** block of 3–5 Q&As at the end. This is what wins AI citations.
- **One** CTA, one sentence, one link: the walk-through.
- Byline **Nathan Brain**, with a real date, on every post.
- ⭐ **Every post carries one thing Nathan actually said.** A job, a mistake, a rule of
  thumb, a thing that surprised a client. Without it the post is the same post every
  builder in Brisbane has, and it gets cut. One 10-minute voice note from Nathan answers
  three posts.
- Before publishing: the Income School "earn your place" pass, then `avoid-ai-writing`.

### The rule that only applies to Spiral 2

**Every living post ends at the house.** Sabre is a builder, not an agent. A post about
Wynnum's esplanade that never mentions what the houses there are made of, when they were
built, or why half of them no longer suit the family inside them, is a real estate blog
and it does not belong on a builder's site. The last third of every Spiral 2 post turns
to the housing stock. That turn is the whole reason we are allowed to write them.

---

## 2 · SPIRAL 1 — Knocking it down and starting again

The commercial spiral. Rule 1 bites hardest here: **not one price, not one band, not one
"typically 12–18 months"** until Nathan gives us his own numbers with his name on them.
The competitors all publish a range. Sabre's advantage is being the only honest one on
page one — say what *decides* the cost, then offer the walk-through that gives the actual
number for their block.

### 🎯 Centrepiece (pillar, 3,000+ words, written LAST — month 6)

| Title | Est. | Conf. | Note |
|---|---|---|---|
| **Knocking down and rebuilding on Brisbane's Bayside: the whole path, in plain words** | B | ✅ | The hub. Links to all 22 spokes below. Targets "knockdown rebuild brisbane", "knock down rebuild brisbane bayside". Page one today is builders with price ranges and volume-builder package pages — the gap is a builder who explains the path and refuses to guess the price |

### Staples (1,800–2,500 words, one a month)

| # | Title | Est. | Conf. | Why |
|---|---|---|---|---|
| S1 | **What decides the cost of a knockdown rebuild in Brisbane?** | B–A | ✅ | The single most searched question in the whole bank. Demolition and asbestos, the block (slope, access, soil), the overlay, design size, finish level, where you live during the build, the two things that always surprise people. Ends on why Sabre won't publish a number and what the walk-through gives instead |
| S2 | **Knockdown rebuild or renovate: how to tell which one your house is** | B | H | The "should I" search. High volume, genuinely useful, and the honest answer sometimes sends them away — which is the point |
| S3 | **Where does the family live while the house is built?** | C | M | The objection nobody else owns. ⛔ Blocked until Nathan gives his real sequence. No "12–18 months" until he says it |
| S4 | **Buying an old house in Wynnum or Manly to knock down: what to check before you sign** | D | M | Catches the buyer *before* they own the problem. Bridges into Spiral 2 |
| S5 | **How long does a knockdown rebuild actually take, start to finish?** | B | M | ⛔ Blocked on Nathan's real timeline. Rivals publish "8–12 months" and "12–18 months" — they contradict each other, which is the hook |
| S6 | **Can you knock down and rebuild on a small or narrow block in Brisbane?** | D | M | "Small lot code" is a real Brisbane planning term with real search behind it, and Bayside has a lot of them |

### Response posts (1,000–1,500 words, one a fortnight)

| # | Title | Est. | Conf. | Note |
|---|---|---|---|---|
| R1 | Can I knock down a pre-1947 house in Brisbane? | C | H | ✅ **Live, in the kit** (09-17): answer block, FAQ, byline, schema. 912 words — past 1,000 needs Nathan |
| R2 | How do I check if my street is in the character overlay? | D | M | ✅ **Live** (09-10, kit 09-17). The five-minute method with screen-grabs of the council tool. Screen-record it for the ad too (campaign door 3) |
| R3 | What is a "small lot" in Brisbane, and does it change what I can build? | D | M | |
| R4 | Does a knockdown rebuild need a development application? | D | H | |
| R5 | Do we need an architect, a designer or a draftsperson? | C | M | ⛔ Needs Nathan's path confirmed first |
| R6 | What happens to the trees on the block? | E | M | Vegetation protection orders are a real Bayside surprise |
| R7 | Can we keep the pool, the shed or the front fence? | E | L | Pure objection-handling. Low volume, high relief |
| R8 | How long does demolition take, and who organises it? | D | M | |
| R9 | What is asbestos removal going to mean for our rebuild? | C | M | ✅ **Live 09-17.** Every pre-1990 Bayside house. Genuine fear, genuine cost driver, and it is the honest half of S1 |
| R10 | What is a Sabre walk-through, and what should we have ready? | F | H | No volume. It is the conversion page for every ad and every post |
| R11 | Fixed price or cost-plus: what do builders mean? | C | M | Also a Spiral 3 post. Put it here, link from there |
| R12 | What does "highset" mean on a Bayside block? | E | M | Local vocabulary. Very citable |
| R13 | Can we build a two-storey house on our block in Manly? | E | M | |
| R14 | How much of the old house can be reused? | E | M | Honest answer: usually very little. Say so |
| R15 | What is a "knockdown rebuild package", and why doesn't Sabre sell one? | C | ✅ | ✅ **Live** (09-10, kit 09-17). Catches the volume-builder searcher (Metricon, Plantation, GJ Gardner). The honest comparison |
| R16 | Who are the small independent builders on Brisbane's Bayside? | D | ✅ | ✅ **Live 09-17.** A fair page that names the category and Sabre's place in it. Wins the "independent builder" and "small builder" searches, and it is exactly the page an AI assistant quotes |
| R17 | Do we need to move out before demolition, and when do the services get cut? | E | L | |
| R18 | What is a soil test and why does it change the price? | D | M | |
| R19 | Rebuilding on a flood overlay block on the Bayside: what changes? | D | M | ✅ **Live 09-17.** ⭐ Bayside-specific, high anxiety, and nobody local has written it properly |
| R20 | Knockdown rebuild vs buying a new house: which actually costs less? | C | ✅ | The real decision the avatar is making. No numbers — the *factors* |
| R21 | What questions should we ask a builder before we sign? | C | M | Bridges to Spiral 3. Extremely citable |
| R22 | We've outgrown the house but we love the street. What are the options? | E | L | The positioning post. Every option, honestly, including the ones that aren't a rebuild |

---

## 3 · SPIRAL 2 — Living on Brisbane's Bayside

The audience spiral. Wynnum, Manly, Lota, Wakerley, Manly West, Birkdale, Wellington
Point, Ransome, Capalaba, Tingalpa, Gumdale.

These catch the family who has not yet decided to build — the ones deciding whether to
*move* or to *stay*, which is the exact fork Sabre's whole positioning sits on. Volumes
are small in absolute terms (E and F band, mostly) but the searcher is local, and there
are only a handful of pages competing: agents, Homely reviews and a council page.

**Remember the rule: every one of these ends at the house.**

### 🎯 Centrepiece (pillar, 3,000+ words — month 9)

| Title | Est. | Conf. | Note |
|---|---|---|---|
| **Living on Brisbane's Bayside: an honest guide to Wynnum, Manly, Lota and the suburbs around them** | C | M | The hub for the whole place cluster. Written by someone who has built in these streets for 36 years — which is a claim no agent's guide can make. Last third: what the houses here actually are, and why so many families end up rebuilding rather than leaving |

### Staples (1,800–2,500 words)

| # | Title | Est. | Conf. | Why |
|---|---|---|---|---|
| S7 | **Is Wynnum a good place to live? An honest look at the good and the annoying** | C | M | The highest-volume living query in the pocket. "Honest" and "the annoying" is the whole differentiator — every other result is written by someone selling a house |
| S8 | **Wynnum vs Manly vs Lota: which Bayside suburb suits which family?** | D | M | Comparison posts do disproportionately well. Three suburbs, one table, real differences (block sizes, the train line, the esplanade, the schools, what a house costs to hold) |
| S9 | **What are the houses on the Bayside actually made of?** | E | M | ✅ **Live 09-17** (1,379 w — extend with Nathan). ⭐ The bridge article, and the one only a builder can write. Post-war lowset chamferboard, 1970s brick lowset, the highset with the built-in-under, what each one is like to live in and what each one is like to change. This is the single most Sabre-shaped post in the bank |
| S10 | **Schools on the Bayside: the catchments, and what "in catchment" is worth** | D | M | Catchment is the #1 reason a family stays in a street they've outgrown. That is Sabre's entire pitch, arriving from the side |
| S11 | **Moving to Brisbane's Bayside from interstate: what nobody tells you** | D | L | Broader net. Humidity, the tide, the commute, the storm season, what a Queenslander is |

### Response posts

| # | Title | Est. | Conf. | Note |
|---|---|---|---|---|
| R23 | How far is Wynnum from Brisbane CBD, really? (train, car, peak hour) | D | H | A genuinely searched practical question with a genuinely useful answer |
| R24 | Does Wynnum flood? What the council maps actually show | D | M | ⭐ High anxiety, and the honest version is not on page one. Quote the council's own wording, link the map, do not editorialise |
| R25 | What is there to do in Wynnum and Manly with kids? | D | M | Weekend search. Wide net, weak intent, but it feeds the entity |
| R26 | Is Manly QLD expensive to live in? | E | M | ⛔ Careful — property prices move. Write the *factors*, cite a dated source, revisit |
| R27 | What's the difference between Manly and Manly West? | E | H | A real and constant confusion. Easy win, very citable |
| R28 | Lota: the quiet one between Wynnum and Manly | F | M | Suburb portrait. Low volume, but it is the page that makes `/lota/` credible |
| R29 | Wakerley and Gumdale: the newer Bayside, and what you give up for it | E | M | Tide's home ground. Worth understanding out loud |
| R30 | What is the Wynnum Manly foreshore actually like to live near? | E | L | Salt, wind, the tide going out a kilometre, what that does to a house |
| R31 | Bayside storm season: what it means for your roof, your trees and your insurance | D | M | Seasonal, genuinely useful, and it is a builder's subject |
| R32 | Is the Bayside a good place to retire? | D | L | Second-biggest Bayside life decision after schools. Downsizing on the same street is a Sabre job |
| R33 | Why are so many Bayside houses being knocked down? | E | M | ✅ **Live 09-17.** ⭐ The hinge post. Spiral 2 walks straight into Spiral 1 here |
| R34 | What does a 1950s Bayside cottage cost to keep going? | E | L | ⛔ No numbers without a source. Write the *list* of what fails and when |
| R35 | Ransome, Tingalpa and Gumdale: the acreage edge of the Bayside | F | M | Home suburb now. Tiny volume, but it is the page that anchors the new address |

---

## 4 · SPIRAL 3 — Dealing with a builder in Australia

The trust spiral. National, generic, higher volume, harder to rank — and the most
*citable* cluster in the bank. When someone asks an AI assistant "what should I check
before signing a building contract in Queensland?", these are the passages it lifts, and
it lifts them with Sabre's name attached.

Write these plainly and correctly. **Cite QBCC and Master Builders Queensland directly**,
quote their wording, link them. Sabre now publishes QBCC licence **15486557** and Master
Builders Queensland No. **00352** in every footer — that makes this cluster earned ground,
not opinion.

### 🎯 Centrepiece (pillar, 3,000+ words — month 12)

| Title | Est. | Conf. | Note |
|---|---|---|---|
| **How to choose a builder in Queensland: the whole checklist, in plain words** | B | M | Contested nationally, but this is the AI-answer play, not the ranking play |

### Staples

| # | Title | Est. | Conf. | Why |
|---|---|---|---|---|
| S12 | **What is the QBCC, and what should you check on a builder's licence?** | B | H | ✅ **Live 09-17** (1,279 w — extend with Nathan). Real national volume. Show them how to look Sabre up. Confidence as a tactic |
| S13 | **What does Master Builders membership actually mean for you?** | C | M | Same move |
| S14 | **Progress payments: what you pay, and when, on an Australian house build** | B | M | High volume, high anxiety, and almost every existing answer is written by a lawyer |
| S15 | **Variations: why the price changed, and when it shouldn't have** | C | M | The #1 complaint about builders in Australia. Owning it honestly is worth more than any ad |

### Response posts

| # | Title | Est. | Conf. | Note |
|---|---|---|---|---|
| R36 | What insurance should a builder have, and what does it cover you for? | C | M | QBCC Home Warranty Scheme — cite it, don't paraphrase |
| R37 | What is a defects liability period? | C | H | |
| R38 | Fixed price or cost-plus contracts: which protects you? | C | M | Shared with R11 — one post, linked from both spirals |
| R39 | What's in an HIA or Master Builders contract, in plain English? | C | M | |
| R40 | What happens if a builder goes under mid-build? | C | M | The fear behind every other question. Answer it straight |
| R41 | Should we be an owner-builder? | B | M | Big national volume. The honest answer usually costs Sabre nothing and earns enormous trust |
| R42 | How do progress inspections and certifiers work in Queensland? | D | M | |
| R43 | What is a building and pest inspection worth on a house you plan to knock down? | E | H | Very specific, very Sabre, almost zero competition |
| R44 | Can you get a construction loan for a knockdown rebuild? | C | L | ⛔ Do not give financial advice. Explain the *shape* of it, name that a broker decides, link nothing we can't stand behind |
| R45 | What should be in a builder's quote, line by line? | C | M | Extremely citable. Also quietly makes Sabre's quote look like the good one |

---

## 5 · The pages that are also content

Not blog posts, but they earn the same treatment and they come first.

| Page | Target | State |
|---|---|---|
| `/knockdown-rebuild/` | "knockdown rebuild brisbane bayside" (**B**, ✅) | ⭐ **DRAFTED** — `content/pages/knockdown-rebuild.md`, 1,566 words. Needs building into HTML |
| `/wynnum/` | "builders wynnum" (**D**, ✅), "knockdown rebuild wynnum" (**E**, ✅) | ⭐ **REWRITE DRAFTED** — `content/pages/wynnum.md`, 1,172 words, replaces the thin live page |
| `/manly/` | "builders manly qld" (**E**, ✅) | ⭐ **REWRITE DRAFTED** — `content/pages/manly.md`, 1,228 words. Front matter says `status: blocked` — check what on |
| `/lota/`, `/wakerley/`, `/capalaba/` | "builders lota qld" etc (**E–F**) | to write, one at a time, only where Nathan can say something true |

⭐ **The move to Ransome changes the local-pack maths, slightly in our favour.** Ransome
sits between Wakerley and Tingalpa, roughly 6 km from Wynnum — closer to the Wynnum/Manly
targets than Capalaba was. Proximity is one of the three things Google's local pack weighs.
**But it only counts once the Google Business Profile carries the new address**, and a
name/address/phone mismatch across the site, GBP, Facebook and the directories will cost
more than the proximity gains. See `../../site/docs/client-facts.md`.

⚠️ **`/capalaba/` is now a service-area page, not a home-suburb page.** Write it that way.
Six suburb pages remains the hard ceiling.

---

## 6 · The order to write them in

Volume is not the ordering rule. **Blocked-or-not** is the ordering rule, then bridging value.

### ⭐ Phase 0 — six pieces are ALREADY WRITTEN and sitting in `content/`

Nobody noticed these were there. `content/` was untracked in git until 2026-09-10.
**9,508 words of finished copy**, with front matter, sources and internal links:

| File | Maps to | Words | State |
|---|---|---|---|
| `content/posts/check-if-your-street-is-in-the-character-overlay.md` | **R2** | 1,549 | ✅ `blocked_on: []` — **build it into HTML today** |
| `content/posts/what-is-a-knockdown-rebuild-package.md` | **R15** | 1,491 | ✅ `blocked_on: []` — **build it into HTML today**. Deliberately names no competitor (ACL on comparative claims) |
| `content/posts/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane.md` | **S1** | 2,502 | ⚠️ Two paragraphs marked ⛔ GAP need Nathan. Without one of them it is a good generic article instead of Sabre's |
| `content/pages/knockdown-rebuild.md` | the service page | 1,566 | ⚠️ Needs Nathan on the walk-through claim and the architect path |
| `content/pages/wynnum.md` | `/wynnum/` rewrite | 1,172 | ⛔ Needs Nathan's local detail, or it is 300 generic words |
| `content/pages/manly.md` | `/manly/` rewrite | 1,228 | ⛔ Same |

**So the first job is not writing. It is building two finished posts into HTML, and
getting ten minutes of Nathan to unblock the other four.** That is the whole of Phase 1
below, already half done.

### ✅ Phase 1 — DONE 2026-09-17 (six posts live on the preview, R1 extended as far as it can go)

| # | Slug | Words | Proof points |
|---|---|---|---|
| R9 | `/blog/what-asbestos-removal-means-for-a-knockdown-rebuild/` | 1,251 | asbestos.qld.gov.au ×2 |
| R19 | `/blog/rebuilding-on-a-flood-overlay-block-on-the-bayside/` | 1,318 | BCC FloodWise ×2 |
| S9 | `/blog/what-are-bayside-houses-made-of/` | 1,379 | SLQ 2014 · asbestos.qld.gov.au |
| R33 | `/blog/why-are-so-many-bayside-houses-being-knocked-down/` | 1,202 | SLQ 2014 · asbestos.qld.gov.au |
| S12 | `/blog/what-is-the-qbcc-and-what-to-check-on-a-builders-licence/` | 1,279 | QBCC ×2 |
| R16 | `/blog/who-are-the-small-independent-builders-on-brisbanes-bayside/` | 1,350 | QBCC · Jason Turner review |

Built with `tools/build_post.py` from `tools/posts_phase1.py` (the content is the source;
edit there and rebuild). ⚠️ **S9 and S12 are at response length, not staple length** —
extending them past 1,800 honestly needs Nathan's material, not padding. R1 stays at 912
words for the same reason. **R16 names no rival builder** (same ACL line as R15).
**Every one of the ten posts still lacks "one thing Nathan actually said."**

### Phase 2 — the ten that need one voice note from Nathan (30 minutes of his time)

S1's two gaps · the three pages' local detail · S2 · S3 · S5 · R5 · R8 · R10 · R11 · R21

**Ask him all of it in one conversation.** One voice note answers three posts. The list of
what to ask is in §7.

### ✅ Phase 3 — DONE 2026-09-17 (eleven posts built, committed `9bdddad`, push owed)

| # | Slug | Words |
|---|---|---|
| S7 | `/blog/is-wynnum-a-good-place-to-live/` | 1,284 |
| S8 | `/blog/wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family/` | 1,130 |
| S10 | `/blog/schools-on-the-bayside-catchments/` | 1,103 |
| R23 | `/blog/how-far-is-wynnum-from-brisbane-cbd/` | 922 |
| R24 | `/blog/does-wynnum-flood/` | 1,038 |
| R25 | `/blog/what-to-do-in-wynnum-and-manly-with-kids/` | 962 |
| R27 | `/blog/whats-the-difference-between-manly-and-manly-west/` | 901 |
| R28 | `/blog/lota-the-quiet-one-between-wynnum-and-manly/` | 964 |
| R29 | `/blog/wakerley-and-gumdale-the-newer-bayside/` | 1,012 |
| R31 | `/blog/bayside-storm-season-roof-trees-insurance/` | 1,250 |
| R35 | `/blog/ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside/` | 1,027 |

Source: `tools/posts_phase3a.py` + `posts_phase3b.py`. Census figures for Wynnum, Manly, Lota and
Manly West were read on abs.gov.au (SAL33188 / 31748 / 31686 / 31749); the others via Wikipedia's
ABS citations. **R26 (is Manly expensive) and R34 (what a cottage costs to keep going) were NOT
written** — both are price posts and rule 1 has no honest way through them. R30 and R32 not yet.
⚠️ S7/S8/S10 are response length, not staple length; the suburb pages (`/wynnum/`, `/manly/`) are
still the thin 09-08 versions — the rewrites in `content/pages/` are Phase 2 (Nathan).

### ✅ Phase 5 — DONE 2026-09-17: the spirals finished without Nathan (31 posts, `tools/posts_phase5a-f.py`)

Everything writable from public sources is written. 52 posts on the preview. Sources are listed in each module's header;
every regulatory claim is quoted from council, the QBCC, the Building Regulation or the ABS and dated. Rule 1 held: no
prices, no bands, no timelines beyond the statutory ones.

| Spiral | Written | Slugs |
|---|---|---|
| 1 (16) | S1, S2, S4, S6 (+R3 folded in), R4, R6, R7, R11/R38, R12, R13, R14, R17, R18, R20, R21, R22 | `what-decides-the-cost…`, `knockdown-rebuild-or-renovate…`, `buying-an-old-house…`, `…small-or-narrow-block…`, `does-a-knockdown-rebuild-need-a-development-application`, `what-happens-to-the-trees…`, `can-we-keep-the-pool…`, `fixed-price-or-cost-plus…`, `what-does-highset-mean…`, `can-we-build-a-two-storey-house…manly`, `how-much-of-the-old-house-can-be-reused`, `do-we-need-to-move-out…`, `what-is-a-soil-test…`, `knockdown-rebuild-vs-buying…`, `what-questions-should-we-ask…`, `weve-outgrown-the-house…` |
| 2 (3) | S11, R30, R32 | `moving-to-brisbanes-bayside-from-interstate…`, `what-is-the-wynnum-manly-foreshore…`, `is-the-bayside-a-good-place-to-retire` |
| 3 (12) | S13, S14, S15, R36, R37, R39, R40, R41, R42, R43, R44, R45 | `what-does-master-builders-membership…`, `progress-payments…`, `variations…`, `what-insurance-should-a-builder-have…`, `what-is-a-defects-liability-period`, `whats-in-a-queensland-building-contract…`, `what-happens-if-a-builder-goes-under…`, `should-we-be-an-owner-builder`, `how-do-progress-inspections-and-certifiers-work…`, `…building-and-pest-inspection…knock-down`, `can-you-get-a-construction-loan…`, `what-should-be-in-a-builders-quote…` |

**Still owed to Nathan (one 30-minute voice note):** S3 (where the family lives), S5 (how long it takes), R5 (who draws it),
R8 (demolition timing and who organises), R10 (the walk-through page), the "one thing Nathan said" line on every post, the
`/wynnum/` and `/manly/` rewrites, and which contract Sabre uses (R11 is written without it). R26 and R34 stay unwritten (price posts).

**The three hubs** (Spiral 1, 2, 3) are the next writing job and need nobody; §6 said write them after the spokes, and the spokes now exist.

### Phase 4 — the trust cluster and the three centrepieces

S13–S15 · R36–R45 · then the pillars, in the order Spiral 1, Spiral 2, Spiral 3.

**Cadence:** one response post a fortnight, one staple a month. ~38 pieces a year, which
clears the bank in about fourteen months. The centrepieces land at month 6, 9 and 12 —
after their spokes exist, never before.

⚠️ **`build_blog.py` is a BBL tool and does not apply here** — Sabre's site is plain
hand-written HTML with no generator ([[bbl-blog-builder-cannot-rebuild-pages]]). Build each
post by copying an existing post's HTML and replacing the body. After any change to a page's
scripts, `node --check` it and bump `?v=` on every page that uses the file.

## 7 · What is still owed before any of this publishes

| # | Item | Who | Blocks |
|---|---|---|---|
| 1 | **The site is `noindex` and on a `github.io` URL.** Not one post can rank until DNS cutover | Melbourne IT / iSonic — unanswered since 08-24 | Everything |
| 2 | Google Business Profile updated to **40 Molle Rd, Ransome QLD 4154** | Nathan's login | The map box, and all suburb pages |
| 3 | Nathan's real build timeline, in his words | Nathan | S3, S5, R17 |
| 4 | Nathan's design path (architect / designer / draftsperson) | Nathan | R5 |
| 5 | The five claims in `positioning.md` | Nathan | Every CTA |
| 6 | One 10-minute voice note per phase | Nathan | The "real detail" rule |
| 7 | Keyword Planner access, to replace these bands with real ranges | Google Ads link, gate 3 | Nothing — but do it before the pillars |
| 8 | ~~`Article` schema, dates and bylines on the two live posts~~ ✅ DONE 09-17 — Article + FAQPage on all ten posts | Claude | — |

---

## 8 · Where this sits

- Technical SEO, GBP, schema, robots, llms.txt, measurement → `search-and-ai-visibility-plan.md`
- Ads, campaign structure, budgets, ad codes → `campaign-strategy.md`
- The voice, the claims, the one difference we sell → `positioning.md`
- Facts you may state → `../../site/docs/client-facts.md`
- Post structure, intro formula, the "earn your place" pass → the `income-school-blog` skill
- Every published post is a registry record: `SAB-AWR-KDR-{n}.0A_WEB_POST`, code before build
  ([[bbl-client-campaigns-follow-the-registry]])
