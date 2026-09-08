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


# ---- state 3: the new two-storey home on the SAME block, same camera, derived from state 1 ----
NEW_PROMPT = (
    "Keep the exact same camera angle, the same block, the same jacaranda tree, the same fence "
    "line, the same neighbours, the same lawn with the red bike and the football, the same late "
    "afternoon light. Replace the old single-storey house with a brand new, complete, two-storey "
    "Hamptons-style family home: crisp white weatherboard cladding, a pale grey Colorbond roof, "
    "large white-framed windows, a covered front porch with white posts, a white picket fence, a "
    "new concrete driveway. The house is finished and whole, not cut away. Photorealistic, no "
    "people, no text, no logos."
)


def state3(src: pathlib.Path) -> pathlib.Path:
    out = OUT / "new-home-same-block.jpg"
    if out.exists():
        print("exists:", out.name); return out
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2/edit",
        arguments={"prompt": NEW_PROMPT, "image_urls": [fal_client.upload_file(str(src))],
                   "num_images": 1, "output_format": "jpeg"},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved:", out.name); return out


if __name__ == "__main__" and os.environ.get("CUTAWAY_STATE3"):
    state3(OUT / "old-house-photoreal-11.jpg")


# ---- states 3b and 4: the build going up, and the family running into the finished home ----
BUILD_PROMPT = (
    "Keep the exact same camera angle, block, jacaranda tree, fence line, neighbours and late "
    "afternoon light. Replace the house with the SAME two-storey Hamptons-style family home part "
    "way through construction: the new concrete slab, the timber wall frames and roof trusses up, "
    "some white weatherboard cladding started on the ground floor, the roof sheets half on, a neat "
    "site with a skip bin and a stack of timber, orange safety fencing along the front. No people, "
    "no text, no logos. Photorealistic."
)
FAMILY_PROMPT = (
    "Keep this exact photograph unchanged: same house, same camera, same garden, same light. Add a "
    "family of four seen from behind, running up the front path toward the front door of the house "
    "together: a mum and dad and two young kids, with a golden retriever bounding beside them. They "
    "are seen from the back, faces not visible, mid-stride, joyful. The red bike and the football "
    "stay on the lawn. Photorealistic, no text, no logos."
)


def derive(src: pathlib.Path, prompt: str, name: str) -> pathlib.Path:
    out = OUT / name
    if out.exists():
        print("exists:", out.name); return out
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2/edit",
        arguments={"prompt": prompt, "image_urls": [fal_client.upload_file(str(src))],
                   "num_images": 1, "output_format": "jpeg"},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved:", out.name); return out


if __name__ == "__main__" and os.environ.get("CUTAWAY_STAGES"):
    derive(OUT / "new-home-same-block.jpg", BUILD_PROMPT, "build-same-block.jpg")
    derive(OUT / "new-home-same-block.jpg", FAMILY_PROMPT, "family-running-in.jpg")


# ---- "Your design" page scenes: the walk-through and the table, both from behind (no faces) ----
WALK_PROMPT = (
    "Photorealistic, 16:9. Inside a modest 1960s Australian family home, a hallway opening into a small "
    "living room, warm morning light through the windows. Seen from BEHIND: a builder in a plain dark "
    "polo shirt and work shorts with a notebook, walking slowly through the house alongside a mum and "
    "dad, all three with their backs to the camera, looking into a small bedroom with bunk beds. Kids' "
    "shoes by the door, school bags on hooks. No faces visible, no text, no logos."
)
TABLE_PROMPT = (
    "Photorealistic, 16:9. A kitchen table in an Australian family home, late afternoon light. "
    "Architectural floor plans and elevation drawings spread across the table with a coffee mug and a "
    "pencil. Seen from above and slightly behind: the hands and forearms of three adults pointing at "
    "the plans, one sleeve a plain dark polo. A child's drawing of a house sits at the corner of the "
    "table. No faces visible, no readable text on the plans, no logos."
)


def scene(prompt: str, name: str) -> pathlib.Path:
    out = OUT / name
    if out.exists():
        print("exists:", out.name); return out
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2",
        arguments={"prompt": prompt, "negative_prompt": "faces, text, watermark, logo, signage, cartoon",
                   "aspect_ratio": "16:9", "num_images": 1, "output_format": "jpeg", "seed": 21},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved:", out.name); return out


if __name__ == "__main__" and os.environ.get("DESIGN_SCENES"):
    scene(WALK_PROMPT, "design-1-walk.jpg")
    scene(TABLE_PROMPT, "design-2-table.jpg")
