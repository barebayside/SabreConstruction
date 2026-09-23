"""The CLICK images: a photographic hero for the posts whose header was a map or a diagram (2026-09-17).

Why: the card image has one job - make a Bayside family want to read. Maps and diagrams explain; they
don't pull. So every post now has TWO images: this hero on the card and at the top, and the map or
diagram kept INSIDE the article as a figure (build_post.py `figure`). The suburb name / topic goes on
as an HTML overlay (post `label`), never baked into the pixels.

Same rules as gen_blog_images.py: Sabre's key, Sabre's frame as the style reference, no faces, no text,
no logos, scale anchors, two variants and LOOK at both. These are illustrations of real places and are
captioned as such - never presented as photographs of the real street.

    set FAL_KEY from ~/.keys/sabre-fal.key for THIS terminal only, then:
    python tools/gen_blog_heroes.py            # all
    python tools/gen_blog_heroes.py lota       # substring match on the slug
Outputs: <workshop>/assets/img/blog-alternates/<slug>-hero-v<N>.jpg. Copy the pick to
<real>/assets/img/blog/<slug>.jpg (the map/diagram stays as <slug>.png).
"""
import os, pathlib, sys, urllib.request
import fal_client
from gen_blog_images import STYLE, RULES, REF

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "img" / "blog-alternates"

BAY = ("Moreton Bay on Brisbane's bayside at low tide: wide flat sand and shallow water stretching out to a "
       "hazy island horizon, mangroves at the edges; ")

HEROES = {
    # ---- suburbs: the place itself, the way a family remembers it ----
    "is-wynnum-a-good-place-to-live":
        BAY + "seen from the grassy esplanade: a long low timber jetty running straight out over the sand and "
        "shallow water, a tidal wading pool with a low concrete wall beside it, tall old Norfolk pines and a "
        "spreading fig tree along the foreshore road, a row of old timber highset houses facing the water; a "
        "family far off on the sand at true scale, backs to camera.",
    "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family":
        "a single wide frame split into three tall vertical panels with thin white gaps, same warm light in all "
        "three: LEFT a long timber jetty over low-tide sand with Norfolk pines; MIDDLE a small-boat harbour "
        "crowded with yacht masts behind a rock breakwater, a hill of houses above it; RIGHT a quiet mangrove "
        "foreshore with a tidal creek, one old timber house and a heron. No people.",
    "whats-the-difference-between-manly-and-manly-west":
        "from a hill street of timber houses, looking down over a small-boat harbour full of yacht masts and "
        "rock breakwaters on Moreton Bay; the street in the foreground runs steeply down to the water; in the "
        "far background, inland and flatter, a spread of 1970s brick and tile suburban rooftops among gum "
        "trees. No people.",
    "lota-the-quiet-one-between-wynnum-and-manly":
        "a quiet dead-end foreshore street on Moreton Bay: mangroves and a tidal creek mouth, low-tide mudflats "
        "beyond, two small old timber highset houses with iron roofs, an empty road, a heron standing in the "
        "shallows, soft warm light; no cars, no people.",
    "wakerley-and-gumdale-the-newer-bayside":
        "a wide curving street in a newer Brisbane suburb built in the 2000s: large two-storey rendered houses "
        "with tile roofs and double garages, neat lawns, young street trees on stakes, a bushland reserve of "
        "tall gums at the end of the street, a bike path; a parent and child on bikes far down the footpath at "
        "true scale, backs to camera.",
    "ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside":
        "a semi-rural acreage block on the edge of Brisbane: a long gravel driveway between post-and-rail "
        "fences, a paddock of dry grass, huge old spreading gum trees, a low house set far back from the road "
        "with a shed beside it, a horse under a tree, wetland and mangroves faintly in the distance; no people.",
    "rebuilding-in-wynnum-or-manly":
        "a flat bayside residential street that runs straight down to the water: an old tired timber highset "
        "house in the foreground with a rusting iron roof and a sagging verandah, a jacaranda in flower, and at "
        "the end of the street Moreton Bay at low tide with a jetty; no people, no cars.",
    # ---- rules: the moment the question gets asked ----
    "can-we-knock-down-our-house":
        "a pre-war timber Queenslander on tall stumps, verandah with timber balustrade, corrugated iron roof, "
        "seen front-on from the footpath in warm late light; in the immediate foreground, out of focus, the "
        "backs of a couple's heads and shoulders as they stand on the footpath looking at it, at true human "
        "scale; a jacaranda; no faces.",
    "check-if-your-street-is-in-the-character-overlay":
        "over the shoulder of a person on a footpath, no face, holding up a phone in front of a street of "
        "pre-war timber Queenslanders; the phone screen shows a plain pale street map with a hatched grey zone "
        "over some blocks and NO words or numbers; the real houses beyond match the map; warm light.",
    "rebuilding-on-a-flood-overlay-block-on-the-bayside":
        "a brand-new pale weatherboard family home raised high on slender steel posts with an open undercroft "
        "and a stair, on a flat low block near mangroves and a tidal drain with water in it, beside an older "
        "lowset 1960s neighbour sitting on the ground; a king-tide morning, warm light; no people.",
    # ---- living: the day itself ----
    "how-far-is-wynnum-from-brisbane-cbd":
        "a small suburban railway station on a Brisbane commuter line: a timber-and-iron station building, two "
        "platforms, a modern electric passenger train pulling in, a handful of commuters at true scale seen from "
        "behind, Moreton Bay glimpsed between the houses, early morning light; no legible signs.",
    "does-wynnum-flood":
        "a king-tide morning on a bayside esplanade: Moreton Bay right up to the top of the stone seawall, the "
        "road and the old highset houses across it dry and clearly above the water, mangroves half submerged, "
        "calm and bright; no people.",
    "schools-on-the-bayside-catchments":
        "three primary-school children with wide-brimmed school hats and backpacks, seen from behind at true "
        "scale, walking along a bayside footpath past an old highset house toward a school fence and shade "
        "trees, a jacaranda, morning light; no faces, no logos, no words.",
    "what-to-do-in-wynnum-and-manly-with-kids":
        BAY + "a tidal wading pool with a low concrete wall beside a timber jetty, children paddling in the "
        "shallow water seen from behind and far enough away that no face shows, towels and bikes on the grass "
        "under a fig tree, parents sitting on the wall, all at true scale; warm afternoon light.",
}

# ---- Phase 5 (Spiral 1 finish, 2026-09-17): the moment each question gets asked ----
HEROES.update({
    "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane":
        "an open builder's notebook and a tape measure on the bonnet of a plain white ute parked in front of an old 1960s highset "
        "Queensland house, the block visibly sloping down behind it toward mangroves and the bay, a jacaranda; no people, no words on the page.",
    "knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is":
        "two neighbouring bayside blocks side by side from an elevated three-quarter angle: on the left an old timber highset lifted on "
        "steel props with scaffolding for a renovation, on the right a block cleared to a fresh concrete slab with a small excavator "
        "parked at true scale; a jacaranda between them; no people.",
    "does-a-knockdown-rebuild-need-a-development-application":
        "a rolled set of house plans and a folded official-looking document with no legible text resting on the timber verandah rail "
        "of an old Queenslander, warm afternoon light, the street and a jacaranda soft behind; no people.",
    "what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild":
        "a cleared suburban block with one enormous old gum tree in the middle, protected by orange temporary fencing at its drip line, "
        "a new concrete slab poured in an L-shape around it, a small excavator parked at true scale to one side; no people.",
    "fixed-price-or-cost-plus-what-do-builders-mean":
        "a close top-down view of a Queensland kitchen table with two printed contracts side by side, both with only blank lines and no "
        "legible words, one pen, a mug of tea, a pair of reading glasses; warm afternoon light through a window; hands at the edge only.",
    "what-is-a-soil-test-and-why-does-it-change-the-price":
        "a small tracked drilling rig taking a soil sample in the front yard of a cleared bayside block, a technician in hi-vis seen "
        "from behind at true scale, a row of labelled soil core samples laid out on the grass in trays, an old house next door; no faces, no words.",
    "buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign":
        "a couple seen from behind at true human scale standing on the footpath in front of a small tired 1950s bayside cottage with a "
        "blank real-estate sign board on the fence, one holding a phone up, the bay glimpsed at the end of the street; no faces, no words.",
    "can-you-knock-down-and-rebuild-on-a-small-or-narrow-block-in-brisbane":
        "a narrow two-storey timber-framed house at frame stage squeezed between two old single-storey bayside cottages, the frame tight "
        "to both boundaries, scaffolding, a jacaranda in the street; no people.",
    "can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild":
        "a cleared bayside block seen from above at three-quarter angle: the old in-ground swimming pool kept and fenced off with "
        "temporary fencing, a new concrete slab poured beside it, the old timber front fence still standing along the footpath; no people.",
    "what-does-highset-mean-on-a-bayside-block":
        "a classic post-war Queensland highset house on tall timber stumps, open underneath with a car parked under it at true scale, "
        "a timber staircase up to the front door, a hills hoist in the yard, bay glimpsed behind; late warm light; no people.",
    "can-we-build-a-two-storey-house-on-our-block-in-manly":
        "a new pale two-storey home on a steep hill street of older timber houses, its upper-floor deck looking out over rooftops to a "
        "small-boat harbour full of yacht masts on Moreton Bay; the street falling steeply away in the foreground; no people.",
    "how-much-of-the-old-house-can-be-reused":
        "salvaged materials stacked neatly on a cleared block: wide old hardwood floorboards, timber casement windows, panelled doors "
        "and a set of timber stairs, de-nailed and sorted on bearers, the old house half demolished behind; no people.",
    "do-we-need-to-move-out-before-demolition-and-when-do-the-services-get-cut":
        "an emptied old bayside cottage with its front door open onto bare rooms, the electricity meter box open on the outside wall "
        "with the meter removed, a removals truck driving away down the street at true scale; no people, no words.",
    "knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less":
        "a close view of a kitchen table with two neat piles: on one side printed property listings with photos of houses and no legible "
        "words, on the other a set of house plans and a calculator; a coffee; two pairs of hands at the edge only; warm light.",
    "what-questions-should-we-ask-a-builder-before-we-sign":
        "across a timber verandah table, seen from behind a couple's shoulders, a builder in a plain work shirt seen from the chest down "
        "at true scale pointing at a printed document with no legible words; a hard hat on the table; no faces.",
    "weve-outgrown-the-house-but-we-love-the-street-what-are-the-options":
        "the front steps of a small post-war bayside cottage crowded with three kids' bikes, a scooter and a pram, a tricycle on the "
        "lawn, a huge jacaranda in flower over the quiet street, the bay at the end of it; no people.",
})

# ---- Phase 5 Spiral 3 (dealing with a builder, 2026-09-17) ----
HEROES.update({
    "what-does-master-builders-membership-actually-mean-for-you":
        "a temporary site fence in front of a house at frame stage on a bayside street, two blank white plaques fixed to the fence side by "
        "side with NO lettering, a plain white ute parked at the kerb; warm late light; no people.",
    "progress-payments-what-you-pay-and-when-on-a-queensland-house-build":
        "a new house at frame stage seen from the street, the roof trusses just on; in the foreground a single printed page with only blank "
        "lines and a pen on the bonnet of a plain white ute; no people, no words.",
    "variations-why-the-price-changed-and-when-it-shouldnt-have":
        "close on a site table in front of a house frame: two hands from opposite sides, one in a work shirt cuff and one in a plain "
        "sleeve, each holding a pen over one single-page document with only blank lines; no faces, no words.",
    "what-insurance-should-a-builder-have-and-what-does-it-cover-you-for":
        "a half-built house at lock-up stage on a bayside street under a dark grey-green afternoon storm sky, temporary site fencing around "
        "it, a plastic document folder on the site table in the foreground; dramatic but real; no people, no words.",
    "what-is-a-defects-liability-period":
        "close on a hand running a finger along a fine hairline crack in a freshly painted white interior wall beside a new window, a set "
        "of house keys on the windowsill, morning light; no face, no words.",
    "whats-in-a-queensland-building-contract-in-plain-english":
        "a thick bound building contract open on a timber kitchen table, a hand turning to a front page that shows only blank ruled lines "
        "and empty boxes with NO legible words, reading glasses and a mug beside it; warm light; no face.",
    "what-happens-if-a-builder-goes-under-mid-build":
        "a house abandoned at frame stage on a quiet bayside street: the timber frame greying, weeds growing up through the concrete slab, "
        "the temporary fence gate padlocked with a chain, a faded blank corflute sign; overcast soft light; no people, no words.",
    "should-we-be-an-owner-builder":
        "a homeowner in a hi-vis vest seen from behind at true human scale, standing alone in the middle of a fresh concrete slab holding a "
        "clipboard, a bundle of timber wall frames delivered on the ground beside the slab, no trades in sight, an old house next door; no face.",
    "how-do-progress-inspections-and-certifiers-work-in-queensland":
        "a building certifier in a white collared shirt and a white hard hat, seen from behind at true scale, holding a clipboard and "
        "looking up at the roof trusses inside a new timber house frame, bracing and tie-downs visible; warm light through the frame; no face.",
    "what-is-a-building-and-pest-inspection-worth-on-a-house-you-plan-to-knock-down":
        "under an old timber highset house: a torch beam lighting up the timber stumps and bearers and the dry earth, a gloved hand holding a "
        "moisture meter against a bearer, ant caps on the stumps, daylight at the far edge; no face, no words.",
    "can-you-get-a-construction-loan-for-a-knockdown-rebuild":
        "a new house at lock-up stage on a bayside street seen through the windscreen of a parked car from the driver's seat, a clipboard "
        "with only blank lines on the passenger seat, a lanyard hanging from the mirror with no text; warm light; no people, no words.",
    "what-should-be-in-a-builders-quote-line-by-line":
        "close top-down on a site table: a multi-page printed quote fanned out, each page showing only blank ruled lines and empty boxes with "
        "NO legible words, a finger running down one page, a coffee and a white hard hat at the edge; warm light; no face.",
})

# ---- Phase 5 Spiral 2 stragglers (2026-09-17) ----
HEROES.update({
    "moving-to-brisbanes-bayside-from-interstate-what-nobody-tells-you":
        "a removals truck with its rear door open unloading outside an old timber highset on a flat bayside street, cardboard boxes on "
        "the footpath, a family of three seen from behind at true scale carrying a box up the front stairs, Moreton Bay at low tide at "
        "the end of the street; no faces, no words or logos on the truck.",
    "what-is-the-wynnum-manly-foreshore-actually-like-to-live-near":
        "an esplanade street at dusk on Moreton Bay: the stone seawall and the bay beyond at high tide, a haze of salt spray in the air, "
        "a row of old timber houses facing the water with weathered rusting iron roofs and salt-stained paint, Norfolk pines bending in a "
        "stiff onshore wind; moody warm light; no people.",
    "is-the-bayside-a-good-place-to-retire":
        "an older couple seen from behind at true human scale walking on a flat paved foreshore path at dawn, a timber jetty and the wide "
        "calm low-tide bay ahead, a bicycle leaning on the rail, Norfolk pines, soft pink light; no faces.",
})

# ---- Phase 6: the three hubs (2026-09-23) ----
HEROES.update({
    "knockdown-rebuild-on-brisbanes-bayside-the-whole-path":
        "a flat bayside residential street running straight down to Moreton Bay at low tide: on the left an old tired timber lowset "
        "cottage with a rusting iron roof and a faded front fence; on the block beside it a new two-storey family house at frame and "
        "roof stage behind temporary site fencing, a small excavator parked on the kerb; a single worker in hi-vis on the frame at true "
        "scale, standing beside a door opening, back to camera; jacaranda in flower; warm late light; no words or logos.",
    "living-on-brisbanes-bayside-an-honest-guide":
        BAY + "seen from the grassy foreshore park: a long low timber jetty, tall Norfolk pines along the esplanade, a row of old "
        "timber highset houses with iron roofs facing the water, a family of three walking on the foreshore path far off at true scale, "
        "backs to camera, a bicycle on the grass; soft golden morning light; no words.",
    "how-to-choose-a-builder-in-queensland-the-whole-checklist":
        "close on a timber kitchen table: a thick bound building contract open to a page of only blank ruled lines and empty boxes with "
        "NO legible words, a rolled house plan and a white hard hat beside it, two pairs of hands from opposite sides of the table, one "
        "in a work shirt cuff, one in a plain sleeve, a pen between them; a window behind with a bayside street softly out of focus; "
        "warm light; no faces, no words.",
})


def gen(slug, prompt, n=2):
    res = fal_client.subscribe("fal-ai/nano-banana-2/edit",
                               arguments={"prompt": STYLE + prompt + RULES, "image_urls": [fal_client.upload_file(str(REF))],
                                          "num_images": n, "output_format": "jpeg", "aspect_ratio": "3:2"},
                               with_logs=False)
    for i, im in enumerate(res["images"]):
        out = OUT / f"{slug}-hero-v{i+1}.jpg"
        urllib.request.urlretrieve(im["url"], out)
        print("saved", out.name)


if __name__ == "__main__":
    assert os.environ.get("FAL_KEY"), "set FAL_KEY from ~/.keys/sabre-fal.key for this terminal"
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, prompt in HEROES.items():
        if len(sys.argv) > 1 and sys.argv[1] not in slug:
            continue
        gen(slug, prompt)
