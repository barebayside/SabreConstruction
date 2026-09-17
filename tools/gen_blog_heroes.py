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
