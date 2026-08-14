"""The 7 project photos on Sabre's site are 376x251 thumbnails — too soft for
a full-bleed bento tile. Crisp-upscale them (no generative reinvention, so we
don't fabricate architecture that isn't on their real builds).
"""
import pathlib, urllib.request
import fal_client

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"

FILES = [
    "proj-brighton.jpg", "proj-clarence.jpg", "proj-alexandra.jpg",
    "proj-killarney78.jpg", "proj-killarney79.jpg", "proj-clapton.jpg",
    "proj-marcoola.jpg",
]

ENDPOINT = "fal-ai/recraft/upscale/crisp"

for name in FILES:
    src = IMG / name
    out = IMG / name.replace("proj-", "proj2x-")
    if out.exists():
        print("skip", out.name)
        continue
    url = fal_client.upload_file(str(src))
    res = fal_client.subscribe(ENDPOINT, arguments={"image_url": url})
    up = res["image"]["url"]
    urllib.request.urlretrieve(up, out)
    print("saved", out.name)

print("done")
