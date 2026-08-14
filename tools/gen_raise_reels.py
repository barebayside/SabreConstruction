"""Three 9:16 reels: Edward's real raise-and-build-under footage, continued by
an AI transformation into the finished family home.

The real clip carries the hook. Its LAST FRAME is the AI's start frame, so the
join is invisible — the generated half literally begins on the same pixels the
camera stopped on. The end frame is the finished-house image derived from that
same frame, so the street, tree and neighbours never move.

Source footage is natively 1080x1920 (phone held vertical — ffprobe reports
1920x1080 because of a rotation flag, the decoded frames are portrait).
"""
import pathlib, urllib.request
from PIL import Image
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAISE = ROOT / "assets" / "img" / "raise"
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

MODEL = "fal-ai/kling-video/v3/pro/image-to-video"

PROMPT = (
    "Locked-off shot, the camera holds still. The construction site completes itself in one "
    "continuous seamless transformation: the temporary mesh fencing and safety signage lift away "
    "and vanish, the steel stumps are enclosed and clad, the new ground floor finishes and opens "
    "up as a wide covered entertaining area, the old weatherboard above is reclad crisp white and "
    "dove grey, a fresh pale grey roof sweeps on, white posts and balustrades appear along a deep "
    "verandah, the sand and rubble becomes a smooth concrete driveway, lush green lawn rolls out, "
    "coastal gardens and a white picket fence grow into place, and the light warms to late "
    "afternoon golden sun. A young family walks up the front path with their children and a "
    "golden retriever as the scene settles. Photorealistic architectural film, no camera "
    "movement, no text, no watermark."
)

NEGATIVE = (
    "blur, distortion, low quality, text, watermark, logo, signage, camera shake, camera movement, "
    "warping geometry, melting architecture, changing camera angle, distorted faces, extra limbs"
)


def main():
    for i in (1, 2, 3):
        out = VID / f"raise-ai-{i}.mp4"
        if out.exists():
            print("skip", out.name)
            continue

        start = RAISE / f"last-{i}.jpg"
        end_src = RAISE / f"after-{i}.jpg"
        end = RAISE / f"after-{i}-fit.jpg"

        # the edit model returns a smaller canvas — match the start frame exactly
        s = Image.open(start)
        Image.open(end_src).convert("RGB").resize(s.size, Image.LANCZOS).save(end, quality=95)

        res = fal_client.subscribe(
            MODEL,
            arguments={
                "start_image_url": fal_client.upload_file(str(start)),
                "end_image_url": fal_client.upload_file(str(end)),
                "prompt": PROMPT,
                "negative_prompt": NEGATIVE,
                "duration": "5",
                "generate_audio": False,
                "cfg_scale": 0.5,
            },
            with_logs=False,
        )
        urllib.request.urlretrieve(res["video"]["url"], out)
        print("saved", out.name, out.stat().st_size, "bytes")
    print("done")


if __name__ == "__main__":
    main()
