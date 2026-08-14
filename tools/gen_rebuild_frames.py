"""Frames for the knockdown-rebuild hero video.

The sequence is generated in two segments so each one has a controlled start
and end, rather than asking one clip to tell the whole story:

    A (old lowset brick-and-tile)  ->  B (cleared block)      = segment 1, demolition
    B (cleared block)              ->  C (their REAL photo)   = segment 2, assembly

A and B are both derived from C, so the camera position, street, neighbouring
house and driveway stay locked across all three. That anchoring is what makes
the assembly converge believably on a real house.
"""
import pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"

REAL = IMG / "home-slide011607.jpg"          # C — the real Sabre build
FRAME_A = IMG / "rb-a-old-house.jpg"
FRAME_B = IMG / "rb-b-cleared.jpg"

EDIT = "fal-ai/nano-banana-2/edit"

PROMPT_A = (
    "Replace the large two-storey white weatherboard house with a small, old, "
    "single-storey 1970s Australian lowset brick-and-tile home on the same block. "
    "Keep the EXACT same camera position, height, focal length and framing. Keep the "
    "street, the driveway, the neighbouring house on the left and the sky unchanged. "
    "The replacement house is clearly smaller and lower than what was there: one storey, "
    "faded red-brown face brick walls, a low-pitched dull terracotta tile roof with "
    "moss and cracked ridge caps, small aluminium-framed windows, a narrow concrete "
    "porch with a thin steel post, a rusting carport to one side, faded green trim. "
    "Remove the white picket fence and the white rendered wall completely; put a low "
    "rusted chain-wire fence along the front boundary instead. Patchy dry brown lawn, "
    "an overgrown shrub, a cracked concrete driveway. "
    "Photorealistic Australian suburban street photograph, flat overcast daylight, "
    "no people, no cars, no text, no watermark."
)

PROMPT_B = (
    "Remove the house completely. The block is now cleared and empty, ready to build: "
    "flat bare compacted earth and sand where the house stood, a few tyre tracks, a "
    "clean new grey concrete slab poured in the middle of the block with plumbing "
    "stubs rising out of it, temporary orange safety mesh fencing along the front "
    "boundary. Keep the EXACT same camera position, height, focal length and framing. "
    "Keep the street, the driveway crossover, the neighbouring house on the left and "
    "the sky unchanged. Nothing of the old house remains — no walls, no roof, no rubble. "
    "Photorealistic Australian construction site photograph, flat overcast daylight, "
    "no people, no machinery, no text, no watermark."
)


def edit(src: pathlib.Path, prompt: str, out: pathlib.Path) -> pathlib.Path:
    if out.exists():
        print("skip", out.name)
        return out
    url = fal_client.upload_file(str(src))
    res = fal_client.subscribe(
        EDIT,
        arguments={"prompt": prompt, "image_urls": [url],
                   "num_images": 1, "output_format": "jpeg"},
        with_logs=False,
    )
    urllib.request.urlretrieve(res["images"][0]["url"], out)
    print("saved", out.name)
    return out


if __name__ == "__main__":
    a = edit(REAL, PROMPT_A, FRAME_A)      # real house -> old lowset house
    edit(a, PROMPT_B, FRAME_B)             # old lowset house -> cleared block
    print("done")
