"""Generate the blog's photographic header images on SABRE'S fal key, in the style of the site's
existing story frames (a Sabre frame is passed as the style reference), nano-banana-2/edit.

Rules baked in (learned 2026-09-17 on the giant-builder frame):
  * every person gets a scale anchor ("no taller than the front door"), and every output gets LOOKED AT
  * no faces, no text, no logos, no real addresses; illustrations, never presented as photos of a real job
  * num_images=2 and pick - one in two comes back with a scale or content fault

    set FAL_KEY from ~/.keys/sabre-fal.key for THIS terminal only, then:
    python tools/gen_blog_images.py            # all
    python tools/gen_blog_images.py asbestos   # one
Outputs land in <real repo>/assets/img/blog/<slug>-v<N>.jpg for review; copy the chosen one to <slug>.jpg.
"""
import os, pathlib, sys, urllib.request
import fal_client

HERE = pathlib.Path(__file__).resolve().parent
REAL = HERE.parent.parent / "sabre-constructions-website"
OUT = REAL / "assets" / "img" / "blog"
REF = HERE.parent / "assets" / "img" / "cutaway" / "build-same-block.jpg"   # Sabre's frame: warm late light, elevated 3/4 view, Bayside street

STYLE = ("Match the photographic style, warm late-afternoon light, colour palette and elevated three-quarter camera "
         "angle of the reference image, but make a completely different scene: ")
RULES = (" Photorealistic. No people's faces visible. No text, signage lettering or logos anywhere. Any person is at TRUE "
         "HUMAN SCALE, no taller than a front door, correctly small against the house. 3:2 landscape.")

SCENES = {
    "what-asbestos-removal-means-for-a-knockdown-rebuild":
        "an older 1960s highset Queensland house with fibro-clad rooms built in underneath, on a flat suburban block with a jacaranda; "
        "two workers in white disposable coveralls, respirators and gloves, seen from behind or the side, carefully lowering a "
        "wrapped and taped flat sheet from the built-in-under wall onto a stack of plastic-wrapped sheets; a temporary fence and a "
        "covered skip to one side; the house intact, demolition not yet started.",
    "what-are-bayside-houses-made-of":
        "four houses side by side along one quiet flat Brisbane bayside street, seen from an elevated three-quarter angle, each a "
        "different era and clearly different: first a pre-war timber Queenslander on tall stumps with a verandah and corrugated iron "
        "roof; second a small post-war fibro cottage, lowset, hipped roof; third a 1960s highset chamferboard house with rooms built in "
        "underneath; fourth a 1970s brick veneer lowset with a tile roof. Same street, same light, no cars in front, no people.",
    "why-are-so-many-bayside-houses-being-knocked-down":
        "a small tired post-war fibro cottage on a flat bayside block behind temporary construction fencing with shade cloth, a "
        "small excavator parked on the lawn at true scale beside it, not yet working; next door a finished new two-storey family home "
        "in pale weatherboard; a jacaranda in flower; no people, no signage lettering.",
    "what-is-the-qbcc-and-what-to-check-on-a-builders-licence":
        "a close, top-down view of a kitchen table on a Queensland verandah: a printed building contract in a folder with a pen, a "
        "white hard hat, a tape measure, a mug of coffee, and a laptop open showing a plain blank search form with no legible words; "
        "warm afternoon light; hands of two people at the edge of the frame only, no faces.",
    "who-are-the-small-independent-builders-on-brisbanes-bayside":
        "a small family builder's site on a quiet bayside street: a new house at frame stage, a plain white dual-cab ute parked on "
        "the driveway with no lettering, a blank corflute sign on the temporary fence, a builder seen from behind at true human scale "
        "talking with a couple on the footpath, all no taller than the front door opening; a jacaranda; warm light.",
    "bayside-storm-season-roof-trees-insurance":
        "a 1960s highset Queensland house on a bayside street under a dark grey-green afternoon storm sky, heavy rain just starting, "
        "a large gum tree bending in the wind close to the roof, gutters overflowing at one corner, the road wet and reflective; "
        "dramatic but real, no lightning, no people.",
    "what-is-a-knockdown-rebuild-package":
        "a sloping bayside block with an old lowset house on it, seen from the street; in the foreground a person's hands, no face, "
        "holding up a printed A3 house plan sheet with only blank line drawings and no legible text, the flat-block plan visibly not "
        "matching the slope behind it; warm afternoon light.",
}


def gen(slug, prompt, n=2):
    res = fal_client.subscribe("fal-ai/nano-banana-2/edit",
                               arguments={"prompt": STYLE + prompt + RULES, "image_urls": [fal_client.upload_file(str(REF))],
                                          "num_images": n, "output_format": "jpeg", "aspect_ratio": "3:2"},
                               with_logs=False)
    for i, im in enumerate(res["images"]):
        out = OUT / f"{slug}-v{i+1}.jpg"
        urllib.request.urlretrieve(im["url"], out)
        print("saved", out.name)


if __name__ == "__main__":
    assert os.environ.get("FAL_KEY"), "set FAL_KEY from ~/.keys/sabre-fal.key for this terminal"
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, prompt in SCENES.items():
        if len(sys.argv) > 1 and sys.argv[1] not in slug:
            continue
        gen(slug, prompt)
