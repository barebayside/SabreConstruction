"""Screenshot any page in the project. `?still` forces every scroll-animation
open so the full page renders in one shot (same hook the BBL site uses).

    py -3 tools/shoot.py                      # index.html, desktop + mobile
    py -3 tools/shoot.py lp-raise ads         # named pages, .html optional
    py -3 tools/shoot.py --all                # every page in the project
    py -3 tools/shoot.py --live               # no ?still, viewport only
    py -3 tools/shoot.py --mobile lp-story    # one viewport only

Output lands in shots/{page}-{viewport}.png, which is gitignored.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHOTS = ROOT / "shots"
SHOTS.mkdir(exist_ok=True)

ALL_PAGES = ["index", "ads", "lp-rebuild", "lp-raise", "lp-story", "rebuild-render"]
VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}

args = sys.argv[1:]
live = "--live" in args
pages = [a.removesuffix(".html") for a in args if not a.startswith("--")]
if "--all" in args or not pages:
    pages = ALL_PAGES if "--all" in args else ["index"]

wanted = [v for v in VIEWPORTS if f"--{v}" in args] or list(VIEWPORTS)

with sync_playwright() as p:
    b = p.chromium.launch()
    for page_name in pages:
        src = ROOT / f"{page_name}.html"
        if not src.exists():
            print("!! no such page:", src.name)
            continue
        url = src.as_uri() + ("" if live else "?still")
        for name in wanted:
            w, h = VIEWPORTS[name]
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg.goto(url)
            pg.wait_for_timeout(3500)
            out = SHOTS / f"{page_name}-{name}{'-live' if live else ''}.png"
            pg.screenshot(path=str(out), full_page=not live)
            print("saved", out.name)
            pg.close()
    b.close()
