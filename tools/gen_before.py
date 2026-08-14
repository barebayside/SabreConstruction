"""Make the 'before' frame: take Sabre's real finished home photo and age it
back into a tired, run-down version with the SAME camera angle and framing.
That before-frame becomes the first frame of the hero transformation video.
"""
import os, sys, pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"

SRC = IMG / "home-slide011607.jpg"          # real Sabre build (the 'after')
OUT = IMG / "hero-before.jpg"

PROMPT = (
    "Transform this house into a tired, run-down, neglected version of itself, "
    "as it would have looked before renovation. Keep the EXACT same camera position, "
    "focal length, framing, composition, house footprint, roofline and window positions. "
    "Only the condition changes: peeling and faded grey-brown paint, patchy rust-streaked "
    "old corrugated roof, weathered and cracked timber cladding, dirty stained render, "
    "grimy windows, a sagging and broken picket fence with missing palings, cracked and "
    "stained concrete driveway with weeds through the joints, dead patchy brown lawn, "
    "overgrown weeds, an old rusted letterbox, a dull overcast grey sky. "
    "Photorealistic Australian suburban house, 1980s neglected condition, "
    "documentary real-estate photograph, no people, no text, no watermark."
)


def main():
    endpoint = sys.argv[1] if len(sys.argv) > 1 else "fal-ai/nano-banana-2/edit"
    url = fal_client.upload_file(str(SRC))
    print("uploaded:", url)

    result = fal_client.subscribe(
        endpoint,
        arguments={
            "prompt": PROMPT,
            "image_urls": [url],
            "num_images": 1,
            "output_format": "jpeg",
        },
        with_logs=True,
    )
    print("result keys:", list(result.keys()))
    out_url = result["images"][0]["url"]
    print("image:", out_url)
    urllib.request.urlretrieve(out_url, OUT)
    print("saved:", OUT)


if __name__ == "__main__":
    main()
