"""Knockdown-rebuild hero video, generated as two controlled segments.

    seg1  old lowset brick-and-tile  ->  cleared block   (demolition)
    seg2  cleared block              ->  their REAL photo (assembly)

Two segments rather than one, because a single clip asked to demolish AND
rebuild spends its whole budget on the transition and lands nowhere. Each
segment here has a fixed start and end frame, so the story beats are exact
and segment 2 is guaranteed to converge on the real house.
"""
import pathlib, urllib.request
from PIL import Image
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

FRAME_A = IMG / "rb-a-old-house.jpg"
FRAME_B = IMG / "rb-b-cleared.jpg"
REAL = IMG / "home-slide011607.jpg"
FRAME_C = IMG / "rb-c-real.jpg"

MODEL = "fal-ai/kling-video/v3/pro/image-to-video"

DEMO_PROMPT = (
    "Locked-off wide shot, camera does not move. The small old brick-and-tile house "
    "is demolished in front of us: roof tiles slide and collapse inward, the timber "
    "roof frame folds down, the brick walls crumble and topple in on themselves in a "
    "billowing cloud of grey dust, the carport buckles and drops. The rubble is then "
    "cleared away and the ground is levelled to bare sandy earth, the chain-wire fence "
    "comes down, and a clean new concrete slab is revealed. Dust drifts across frame "
    "and settles. Photorealistic construction documentary footage, overcast daylight, "
    "no people, no text."
)

BUILD_PROMPT = (
    "Locked-off wide shot, camera does not move. A new two-storey white weatherboard "
    "home assembles itself on the empty slab, piece by piece, like precision machinery. "
    "In sequence: timber wall frames fly in from off screen and lock upright onto the "
    "slab; floor joists and the upper storey frame snap into place above them; white "
    "weatherboard cladding panels slide in and click flat onto the frames; pale grey "
    "Colorbond roof sheets sweep in and lock together across the rafters; windows and "
    "plantation shutters drop into their openings; the porch posts, gable and front "
    "door swing into position; white picket fence palings fly in one after another "
    "along the front boundary; finally the concrete driveway, green lawn and a small "
    "tree drop into place. Components arrive fast and precise and click into position, "
    "faint dust puffs at each connection. Photorealistic architectural visualisation, "
    "clearing to bright blue sky with white clouds, no people, no machinery, no text."
)

NEGATIVE = (
    "blur, distortion, low quality, text, watermark, logo, people, workers, cars, "
    "camera shake, camera movement, warping geometry, melting architecture, "
    "changing camera angle"
)


def normalise():
    """All three frames must share one size for start/end pairing."""
    a = Image.open(FRAME_A)
    size = a.size
    for src, dst in [(REAL, FRAME_C)]:
        im = Image.open(src).convert("RGB")
        if im.size != size:
            im = im.resize(size, Image.LANCZOS)
        im.save(dst, quality=95)
    b = Image.open(FRAME_B)
    if b.size != size:
        b.convert("RGB").resize(size, Image.LANCZOS).save(FRAME_B, quality=95)
    print("frames normalised to", size)


def segment(start: pathlib.Path, end: pathlib.Path, prompt: str,
            duration: str, out: pathlib.Path):
    if out.exists():
        print("skip", out.name)
        return
    res = fal_client.subscribe(
        MODEL,
        arguments={
            "start_image_url": fal_client.upload_file(str(start)),
            "end_image_url": fal_client.upload_file(str(end)),
            "prompt": prompt,
            "negative_prompt": NEGATIVE,
            "duration": duration,
            "generate_audio": False,
            "cfg_scale": 0.5,
        },
        with_logs=False,
    )
    urllib.request.urlretrieve(res["video"]["url"], out)
    print("saved", out.name, out.stat().st_size, "bytes")


if __name__ == "__main__":
    normalise()
    segment(FRAME_A, FRAME_B, DEMO_PROMPT, "5", VID / "rb-seg1-demo.mp4")
    segment(FRAME_B, FRAME_C, BUILD_PROMPT, "10", VID / "rb-seg2-build.mp4")
    print("done")
