"""Screenshot the landing page. `?still` forces every scroll-animation open
so the full page renders in one shot (same hook the BBL site uses).

    py -3 tools/shoot.py            # desktop + mobile full page
    py -3 tools/shoot.py --live     # no ?still, viewport only (motion check)
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHOTS = ROOT / "shots"
SHOTS.mkdir(exist_ok=True)

url = (ROOT / "index.html").as_uri()
still = "--live" not in sys.argv
if still:
    url += "?still"

with sync_playwright() as p:
    b = p.chromium.launch()

    for name, w, h in [("desktop", 1440, 900), ("mobile", 390, 844)]:
        page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        page.goto(url)
        page.wait_for_timeout(3500)
        out = SHOTS / f"{name}{'' if still else '-live'}.png"
        page.screenshot(path=str(out), full_page=still)
        print("saved", out)
        page.close()

    b.close()
