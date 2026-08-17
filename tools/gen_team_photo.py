"""Team group photo — AI STAND-IN, not Sabre's actual team.

⚠️ THESE ARE NOT SABRE'S STAFF. Sabre's real team is six named, identifiable
people (Stewart, Cathy, Nathan, Celene, Frank, Jacob) whose cut-out photos are
already in assets/img/team/. This script deliberately generates a GENERIC crew
that resembles none of them.

Why it is deliberately generic: fabricating a photoreal group shot of six real,
named individuals and publishing it on their own company website is a fake
photograph of real people. The generic version is a placeholder that shows what
the slot looks like filled, and it carries the same honesty label as every other
AI person in this repo (see docs/open-items.md item 1).

It must be replaced with a real photo before the site goes public. That photo is
a 20-minute job on a phone and is already logged as "waiting on the client".
"""
import pathlib
import urllib.request

import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)

MODEL = "fal-ai/nano-banana-2"
FALLBACK = "fal-ai/flux-pro/v1.1-ultra"

PROMPT = (
    "Documentary photograph of a six-person Australian residential building crew "
    "standing together in a relaxed row, shoulder to shoulder, all smiling warmly "
    "and looking straight at the camera. Four are in red hi-vis work shirts and "
    "black work trousers with tool belts, two are in black polo shirts as the "
    "office side of the business. A mix of ages from mid-twenties to late fifties, "
    "men and women, ordinary Australian tradespeople, weathered and genuine, not "
    "models. They stand on the driveway in front of a partly built two-storey "
    "Queensland home with timber wall frames and roof trusses visible behind them. "
    "Bright overcast Brisbane daylight, natural colour, shot on a 35mm lens at eye "
    "level, shallow but not extreme depth of field, sharp faces, candid and "
    "unposed feeling. Real photography, not a render."
)

NEGATIVE = (
    "on-screen text, watermark, logo, signage, brand names, distorted faces, "
    "extra fingers, extra limbs, plastic skin, beauty retouching, stock-photo "
    "posing, cgi, 3d render, illustration, cartoon"
)

VARIANTS = 2


def generate(model: str, out: pathlib.Path) -> bool:
    """Generate one image. Returns True on success."""
    res = fal_client.subscribe(
        model,
        arguments={
            "prompt": PROMPT,
            "negative_prompt": NEGATIVE,
            "aspect_ratio": "16:9",
            "num_images": 1,
            "output_format": "jpeg",
        },
        with_logs=False,
    )
    images = res.get("images") or []
    if not images:
        print("no image returned from", model)
        return False
    urllib.request.urlretrieve(images[0]["url"], out)
    print("saved", out.name, out.stat().st_size, "bytes", "via", model)
    return True


def main():
    for i in range(1, VARIANTS + 1):
        out = IMG / f"team-photo-{i}.jpg"
        if out.exists():
            print("skip", out.name)
            continue
        try:
            ok = generate(MODEL, out)
        except Exception as exc:  # noqa: BLE001 - endpoint may not exist on this account
            print(f"{MODEL} failed ({exc}); falling back to {FALLBACK}")
            ok = generate(FALLBACK, out)
        if not ok:
            print("FAILED", out.name)
    print("done")


if __name__ == "__main__":
    main()
