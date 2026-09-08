"""Cutaway frames for the home-page story section — STAGE 01 ONLY (frames, cents each).

Three states: (1) the OLD house the family lives in now, front wall away, tired rooms visible;
(2) the architect's drawings; (3) the NEW family home, front wall away, finished rooms visible.

State 1 is a generic 1960s Bayside house — nobody's real house, and not presented as Sabre's
work. State 3 must be a Sabre design or a plan Sabre may show; until Nathan supplies one, this
script only makes state-1 candidates so Edward can pick a STYLE (illustrated vs photoreal).

Run with SABRE'S key, per terminal. Costs ≈ 8c per frame on nano-banana-2.
    $env:FAL_KEY = (Get-Content "$HOME\\.keys\\sabre-fal.key" -Raw).Trim()
    python tools/gen_cutaway_frames.py
"""
import os, pathlib, sys, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img" / "cutaway"
OUT.mkdir(parents=True, exist_ok=True)

SCENE = (
    "A modest single-storey 1960s Australian suburban house in Brisbane's Bayside: low-pitched tiled "
    "roof, pale brick walls, aluminium windows, a concrete driveway, a Hills hoist in the backyard, a "
    "jacaranda tree, a neat green front lawn with a kids' bike and a football on it. The entire front "
    "wall of the house has been cut away cleanly like a dollhouse so we see inside every room at once: "
    "a small but clean kitchen, a cosy living room with a normal flat-screen TV and a family couch, "
    "three small bedrooms with bunk beds and kids' toys, one bathroom, a narrow hallway with school bags "
    "hung up. The house is well kept, loved and full of family life. It is simply too small for the "
    "family in it: bunks in every bedroom, toys spilling into the hall, one bathroom for everyone. "
    "Nothing broken, no stains, no damage, no clutter beyond a busy family. Warm late-afternoon light. "
    "No people. No text, no labels, no logos."
)

STYLES = {
    "illustrated": ("Architectural cutaway illustration, clean isometric-ish three-quarter view slightly "
                    "from above, soft watercolour-and-ink style, muted warm palette, friendly and "
                    "explanatory like a children's picture-book cross-section. "),
    "photoreal":   ("Photorealistic architectural cutaway render, three-quarter view slightly from above, "
                    "natural daylight, shallow depth of field, the cut edges of the walls crisp and clean. "),
}

NEG = "people, faces, text, watermark, logo, signage, cartoonish exaggeration, dark, gloomy, stains, damage, leaks, cracks, old CRT television, rubbish, mess, decay"


def gen(style: str, prompt: str, seed: int) -> pathlib.Path:
    out = OUT / f"old-house-{style}-{seed}.jpg"
    if out.exists():
        print("exists:", out.name); return out
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2",
        arguments={"prompt": prompt, "negative_prompt": NEG, "aspect_ratio": "4:3",
                   "num_images": 1, "output_format": "jpeg", "seed": seed},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved:", out.name)
    return out


if __name__ == "__main__":
    if not os.environ.get("FAL_KEY"):
        sys.exit("FAL_KEY not set — load Sabre's key for this terminal first")
    for style, lead in STYLES.items():
        gen(style, lead + SCENE, seed=11)
    print("stage 01 done — show Edward before any video.")


# ---- state 2: the drawings, derived from the chosen state-1 frame so the camera holds ----
DRAW_PROMPT = (
    "Keep this exact photograph unchanged. Over the house, add translucent white architectural line "
    "drawings, like a blueprint sketch, of a larger two-storey family home that would replace it: "
    "clean thin white lines showing the new outline, the upper storey, larger windows, a covered "
    "entry, drawn in perspective to sit on the same block. The old house stays visible beneath the "
    "lines. Subtle, elegant, no text, no labels, no dimensions, no logos."
)


def state2(src: pathlib.Path) -> pathlib.Path:
    out = OUT / "drawings-over-old-house.jpg"
    if out.exists():
        print("exists:", out.name); return out
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2/edit",
        arguments={"prompt": DRAW_PROMPT, "image_urls": [fal_client.upload_file(str(src))],
                   "num_images": 1, "output_format": "jpeg"},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved:", out.name); return out


if __name__ == "__main__" and os.environ.get("CUTAWAY_STATE2"):
    state2(OUT / "old-house-photoreal-11.jpg")
