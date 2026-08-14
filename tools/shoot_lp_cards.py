"""Regenerate the three landing-page preview thumbnails used by ads.html.

Run this whenever an LP changes visibly, or the "Ad destinations" cards on
ads.html quietly keep showing an old build — which is worse than showing
nothing, because it looks current.

    py -3 tools/shoot_lp_cards.py

The two Meta pages are shot at phone size and the Google page at desktop,
because that's the device each one is actually the destination for. The cards
letterbox rather than crop, so the shapes are meant to differ.
"""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img" / "lp"
OUT.mkdir(parents=True, exist_ok=True)

# page, output name, viewport, capture height (full page is far too tall to read
# as a thumbnail — the top two screens are what the card is showing)
CARDS = [
    ("lp-rebuild", "lp-rebuild.jpg", 430, 860),
    ("lp-raise",   "lp-raise.jpg",   430, 860),
    ("lp-story",   "lp-story.jpg",  1280, 800),
]

with sync_playwright() as p:
    b = p.chromium.launch()
    for page_name, out_name, w, h in CARDS:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        pg.goto((ROOT / f"{page_name}.html").as_uri() + "?still")
        pg.wait_for_timeout(3500)
        pg.screenshot(path=str(OUT / out_name), quality=88, type="jpeg")
        print("saved", out_name)
        pg.close()
    b.close()
