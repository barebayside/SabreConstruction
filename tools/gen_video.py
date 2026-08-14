"""Hero transformation video: the run-down 'before' frame morphs into Sabre's
real finished build. Start frame = hero-before.jpg, end frame = the actual
photo of the completed home, so the payoff shot is genuinely their work.
"""
import pathlib, urllib.request
from PIL import Image
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

BEFORE = IMG / "hero-before.jpg"
AFTER = IMG / "home-slide011607.jpg"
OUT = VID / "hero-transform.mp4"

PROMPT = (
    "Slow steady cinematic push-in toward the house, camera moving forward on a dolly. "
    "As the camera moves the house restores itself in one continuous seamless morph: "
    "the rusted corrugated roof becomes a new pale grey Colorbond roof, the weathered "
    "peeling grey cladding is reclad and repainted crisp bright white weatherboard, the "
    "broken sagging fence straightens into a clean white picket fence, the stained render "
    "wall becomes freshly painted white, the cracked weedy driveway becomes smooth new "
    "concrete, the dead brown lawn turns lush green with tidy new landscaping, and the "
    "dull overcast sky clears to bright blue with white clouds. "
    "Photorealistic architectural film, natural daylight, no cuts, no people, no cars."
)

NEGATIVE = (
    "blur, distortion, low quality, text, watermark, logo, people, cars, camera shake, "
    "warping architecture, melting geometry, changing house shape, extra windows"
)


def match_size():
    """Kling wants the start and end frames to share dimensions."""
    b = Image.open(BEFORE)
    a = Image.open(AFTER).convert("RGB")
    if a.size != b.size:
        a = a.resize(b.size, Image.LANCZOS)
        p = IMG / "hero-after.jpg"
        a.save(p, quality=95)
        return p
    return AFTER


def main():
    after = match_size()
    start_url = fal_client.upload_file(str(BEFORE))
    end_url = fal_client.upload_file(str(after))
    print("start:", start_url)
    print("end:  ", end_url)

    result = fal_client.subscribe(
        "fal-ai/kling-video/v3/pro/image-to-video",
        arguments={
            "start_image_url": start_url,
            "end_image_url": end_url,
            "prompt": PROMPT,
            "negative_prompt": NEGATIVE,
            "duration": "6",
            "generate_audio": False,
            "cfg_scale": 0.5,
        },
        with_logs=True,
    )
    print("result keys:", list(result.keys()))
    url = result["video"]["url"]
    print("video:", url)
    urllib.request.urlretrieve(url, OUT)
    print("saved:", OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
