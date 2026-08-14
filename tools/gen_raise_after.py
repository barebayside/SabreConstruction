"""'Finished' end-frames for the three real raise-and-build-under clips.

Each one is derived from the LAST FRAME of Edward's real footage, so the
camera position, street, trees and neighbouring houses carry straight through
and the AI half starts on the same pixels the real half ended on.

The finished state is a completed double-storey Hamptons-style Queenslander
with a family visibly in it — per the foundations Fit test, the image has to
carry a marker of the viewer's own world, and the segment is families.
"""
import pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAISE = ROOT / "assets" / "img" / "raise"

EDIT = "fal-ai/nano-banana-2/edit"

BASE = (
    "Transform this construction site into the same house fully finished and beautiful. "
    "Keep the EXACT same camera position, height, focal length and framing. Keep the street, "
    "the driveway, the big shade tree, the neighbouring houses and the sky in the same places. "
    "The house is now a completed two-storey Hamptons-style Queenslander: crisp white and soft "
    "dove-grey weatherboard cladding, a fresh pale grey Colorbond roof, white timber posts and "
    "balustrades, a deep shaded verandah across the front with a hanging seat, plantation "
    "shutters, black-framed windows, a wide covered ground floor entertaining area built in "
    "underneath where the steel stumps were. "
    "All temporary construction fencing, safety signage, scaffolding, sand, rubble and building "
    "materials are gone. In their place: a finished concrete driveway, lush green lawn, tidy "
    "coastal landscaping with frangipani and agapanthus, a white picket fence and a paved front "
    "path leading to timber front steps. "
    "Warm late-afternoon golden sunlight, soft shadows, clear blue Queensland sky. "
    "Photorealistic architectural photography, no text, no watermark, no signage. "
)

FAMILY = {
    1: (
        "A young family is walking up the front path towards the steps, seen from behind: a "
        "mother and father side by side, a boy of about seven and a girl of about four holding "
        "their hands, and a golden retriever trotting ahead of them onto the lawn. Natural "
        "candid movement, faces not visible, they are small in frame and the house is the hero."
    ),
    2: (
        "Two young children are playing on the front lawn — one running, one on a small bicycle "
        "on the path — and a golden retriever is running across the grass beside them. A parent "
        "stands on the verandah watching. Natural candid moment, people small in frame, the "
        "house is the hero."
    ),
    3: (
        "A family is gathered on the front verandah: two parents sitting on the hanging seat with "
        "a mug each, two young children on the steps below them, and a golden retriever lying at "
        "the bottom of the steps. Relaxed late-afternoon family scene, people small in frame, the "
        "house is the hero."
    ),
}


def main():
    for i in (1, 2, 3):
        src = RAISE / f"last-{i}.jpg"
        out = RAISE / f"after-{i}.jpg"
        if out.exists():
            print("skip", out.name)
            continue
        res = fal_client.subscribe(
            EDIT,
            arguments={
                "prompt": BASE + FAMILY[i],
                "image_urls": [fal_client.upload_file(str(src))],
                "num_images": 1,
                "output_format": "jpeg",
            },
            with_logs=False,
        )
        urllib.request.urlretrieve(res["images"][0]["url"], out)
        print("saved", out.name)
    print("done")


if __name__ == "__main__":
    main()
