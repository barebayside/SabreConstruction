"""Drone-style hero clip from Sabre's REAL photo of the finished Clarence build.

    01 frame     widen the 4:3 photo to 16:9 (sky + lawn only, house untouched)  nano-banana-2/edit
    02 generate  pull back, rise, gentle arc — camera moves, the house does not      kling v3 pro i2v
    03 encode    wide 1280x720 + portrait 720x1280 cuts, posters                     ffmpeg (see below)

Honesty: the model invents whatever the photo does not show (roof, sides, the street
behind). That is why the move is a pull-back and rise with a small arc, not an orbit,
and why the clip is a visualisation of a real Sabre build, not footage of it.

Run with SABRE'S key, per terminal:
    $env:FAL_KEY = (Get-Content "$HOME\\.keys\\sabre-fal.key" -Raw).Trim()
Raw model output lands in assets/video/*-source.mp4 (gitignored). Cost ≈ 8c + 5s × $0.168.
"""
import os, pathlib, sys, urllib.request
from PIL import Image
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

SRC = IMG / "proj2x-clarence.jpg"          # 1336x1004, Sabre's own photo, non-generative upscale
WIDE_FRAME = IMG / "drone-clarence-frame.jpg"
RAW = VID / "drone-clarence-source.mp4"    # gitignored (*-source.mp4)
DURATION = os.environ.get("DRONE_SECONDS", "5")

WIDEN_PROMPT = (
    "Extend this photograph to a wider 16:9 frame by adding more of the same scene on the left "
    "and right only: more blue sky with the same white clouds, more of the same green lawn and "
    "concrete driveway, more of the same white fence continuing naturally, the same suburban "
    "street. The house itself must remain exactly as it is, pixel for pixel, same size and "
    "position in the centre. Photorealistic, same lighting, same lens, no new buildings, no "
    "people, no cars, no text."
)

DRONE_PROMPT = (
    "Aerial drone shot. The camera starts at street level facing the white two-storey "
    "Hamptons-style weatherboard house with the white fence and gate, then smoothly pulls back "
    "and rises, climbing above the roofline while gently arcing to the right, revealing the "
    "house, its driveway, the fence and the quiet suburban street from above. Smooth stabilised "
    "gimbal motion, slow and cinematic, one continuous shot, bright daylight, blue sky with white "
    "clouds. The house stays exactly as it is: same shape, same windows, same roof, same colours. "
    "No people, no cars, no text."
)

NEGATIVE = (
    "blur, distortion, low quality, text, watermark, logo, people, cars, camera shake, "
    "warping architecture, melting geometry, changing house shape, extra storeys, extra windows, "
    "different house, cuts, fast motion"
)


def stage01_frame() -> pathlib.Path:
    if WIDE_FRAME.exists():
        print("01 frame exists:", WIDE_FRAME.name); return WIDE_FRAME
    src_url = fal_client.upload_file(str(SRC))
    res = fal_client.subscribe(
        "fal-ai/nano-banana-2/edit",
        arguments={"prompt": WIDEN_PROMPT, "image_urls": [src_url], "aspect_ratio": "16:9",
                   "num_images": 1, "output_format": "jpeg"},
        with_logs=False,
    )
    url = res["images"][0]["url"]
    urllib.request.urlretrieve(url, WIDE_FRAME)
    im = Image.open(WIDE_FRAME); print("01 frame:", WIDE_FRAME.name, im.size)
    return WIDE_FRAME


def stage02_video(frame: pathlib.Path) -> pathlib.Path:
    if RAW.exists():
        print("02 raw exists:", RAW.name); return RAW
    res = fal_client.subscribe(
        "fal-ai/kling-video/v3/pro/image-to-video",
        arguments={
            "start_image_url": fal_client.upload_file(str(frame)),
            "prompt": DRONE_PROMPT,
            "negative_prompt": NEGATIVE,
            "duration": DURATION,
            "generate_audio": False,
            "cfg_scale": 0.5,
        },
        with_logs=False,
    )
    urllib.request.urlretrieve(res["video"]["url"], RAW)
    print("02 raw:", RAW.name, RAW.stat().st_size, "bytes")
    return RAW


if __name__ == "__main__":
    if not os.environ.get("FAL_KEY"):
        sys.exit("FAL_KEY not set — load Sabre's key for this terminal first")
    f = stage01_frame()
    stage02_video(f)
    print("done. Encode with the ffmpeg lines in docs/reference/media-pipeline.md (drone hero).")
