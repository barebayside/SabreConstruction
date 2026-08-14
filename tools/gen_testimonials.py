"""Three AI talking-head testimonial clips for the carousel.

⚠️ THESE ARE NOT REAL CUSTOMERS. They are AI-generated people saying scripted
lines, built as a proof of concept only. They are labelled on the page and a
burned-in "AI DEMO" tag is added by tools/label_testimonials.sh so the files
can't be mistaken for real testimonials if they ever leave the page.
"""
import pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
VID = ROOT / "assets" / "video"
VID.mkdir(parents=True, exist_ok=True)

MODEL = "fal-ai/veo3.1"

SHARED = (
    "Filmed as a real customer testimonial: handheld documentary look, shallow depth "
    "of field, natural daylight, the person looks slightly off-camera at an unseen "
    "interviewer and speaks warmly and naturally, Australian accent. "
)

CLIPS = [
    {
        "file": "testimonial-1.mp4",
        "prompt": SHARED + (
            "A woman in her late thirties with shoulder-length brown hair, in a linen "
            "shirt, standing on the front lawn of a new white weatherboard two-storey "
            "home in suburban Queensland. She says: "
            "\"We'd never built before. Stewart walked us through every single decision, "
            "and the price we signed at the start is exactly what we paid.\""
        ),
    },
    {
        "file": "testimonial-2.mp4",
        "prompt": SHARED + (
            "A man in his early fifties with short greying hair and a navy polo shirt, "
            "standing on the timber front porch of a newly finished home, arms relaxed. "
            "He says: "
            "\"Nathan was on site constantly. Any question I had, I got a straight answer "
            "the same day. I never had to chase anyone.\""
        ),
    },
    {
        "file": "testimonial-3.mp4",
        "prompt": SHARED + (
            "A woman in her fifties with short blonde hair, leaning against the island "
            "bench of a bright white newly built kitchen with pendant lights behind her. "
            "She says: "
            "\"We changed the kitchen halfway through and Nathan sorted it without a fuss. "
            "Handed over on time. Genuinely lovely people to deal with.\""
        ),
    },
]

NEGATIVE = "on-screen text, subtitles, captions, watermark, logo, distorted face, extra fingers"


def main():
    for c in CLIPS:
        out = VID / c["file"]
        if out.exists():
            print("skip", out.name)
            continue
        res = fal_client.subscribe(
            MODEL,
            arguments={
                "prompt": c["prompt"],
                "negative_prompt": NEGATIVE,
                "duration": "8s",
                "aspect_ratio": "16:9",
                "resolution": "720p",
                "generate_audio": True,
            },
            with_logs=False,
        )
        urllib.request.urlretrieve(res["video"]["url"], out)
        print("saved", out.name, out.stat().st_size, "bytes")
    print("done")


if __name__ == "__main__":
    main()
