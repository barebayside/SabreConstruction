"""Concept 03 — vertical (9:16) talking-head stand-in for the retargeting ad.

The 16:9 clip in the carousel was the wrong shape for the placement Concept 03
actually runs in: Reels, Stories and vertical feed. This regenerates it natively
at 9:16 rather than cropping a landscape frame.

⚠️ NOT A REAL CUSTOMER. Same rule as tools/gen_testimonials.py — this is an
AI-generated person reading a scripted line so the format can be reviewed. The
burned-in label is added by tools/finish_testimonial_vertical.sh and stays until
a real family is filmed.

The scripted line is deliberately NOT taken from Sabre's real Google reviews.
Putting a real customer's words in an AI actor's mouth would be worse than a
generic script, not better.
"""
import pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

MODEL = "fal-ai/veo3.1"
OUT = VID / "testimonial-v-raw.mp4"

PROMPT = (
    "Vertical portrait video filmed on a phone as a real customer testimonial: "
    "handheld documentary look, shallow depth of field, natural daylight, the "
    "person is framed from the chest up in the centre of a tall vertical frame "
    "with headroom above them, they look slightly off-camera at an unseen "
    "interviewer and speak warmly and naturally with an Australian accent. "
    "A man in his early fifties with short greying hair and a navy polo shirt, "
    "standing on the timber front porch of a newly finished Queensland home, "
    "arms relaxed. He says: "
    "\"Nathan was on site constantly. Any question I had, I got a straight "
    "answer the same day. I never had to chase anyone.\""
)

NEGATIVE = (
    "on-screen text, subtitles, captions, watermark, logo, letterboxing, "
    "black bars, distorted face, extra fingers"
)


def main():
    if OUT.exists():
        print("skip", OUT.name, "— delete it to regenerate")
        return
    res = fal_client.subscribe(
        MODEL,
        arguments={
            "prompt": PROMPT,
            "negative_prompt": NEGATIVE,
            "duration": "8s",
            "aspect_ratio": "9:16",
            "resolution": "720p",
            "generate_audio": True,
        },
        with_logs=False,
    )
    urllib.request.urlretrieve(res["video"]["url"], OUT)
    print("saved", OUT.name, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
