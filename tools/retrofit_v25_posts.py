"""v25 one-off (2026-09-17): give every generated post a click hero + label, and move the map/diagram INTO
the article as `figure`. Edits the dicts in tools/posts_*.py in place, then build_post.py rebuilds.

    python tools/retrofit_v25_posts.py
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OSM = "Boundaries &copy; OpenStreetMap contributors."
ILL = "Illustration in the style of Sabre's story frames, not a photograph of the real street."

# slug -> (hero alt, hero caption, label (kicker, big), figure-after h2 id or None)
# The old image_alt / image_caption become the figure's alt / caption.
NEW = {
    "is-wynnum-a-good-place-to-live": ("The Wynnum foreshore: the jetty, the wading pool, the pines and the old highsets", ILL, ("The Bayside suburbs", "Wynnum"), "who-lives-here"),
    "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family": ("Three panels: Wynnum's jetty, Manly's boat harbour, Lota's mangrove foreshore", ILL, ("Which suits which family", "Wynnum &middot; Manly &middot; Lota"), "numbers"),
    "whats-the-difference-between-manly-and-manly-west": ("Looking down a Manly hill street to the boat harbour, the flatter suburb inland behind", ILL, ("One suburb until 1975", "Manly or Manly West"), "how-they-split"),
    "lota-the-quiet-one-between-wynnum-and-manly": ("A quiet Lota foreshore street: mangroves, the creek mouth, two old highsets and a heron", ILL, ("The Bayside suburbs", "Lota"), "what-it-is"),
    "wakerley-and-gumdale-the-newer-bayside": ("A wide new street of two-storey homes with bushland at the end, a parent and child on bikes", ILL, ("The newer Bayside", "Wakerley &amp; Gumdale"), "what-they-are"),
    "ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside": ("An acreage block: a long gravel drive, post-and-rail fences, big gums, a horse, the house set well back", ILL, ("The acreage edge", "Ransome &middot; Tingalpa &middot; Gumdale"), "ransome"),
    "rebuilding-on-a-flood-overlay-block-on-the-bayside": ("A new home raised on posts on a low block by a tidal drain, the older lowset neighbour on the ground", ILL, ("What changes for a rebuild", "Flood overlay"), "the-design"),
    "how-far-is-wynnum-from-brisbane-cbd": ("A train pulling into a small Bayside station, commuters on the platform, the bay between the houses", ILL, ("By train and by road", "Wynnum to the city"), "by-train"),
    "does-wynnum-flood": ("A king tide up to the top of the esplanade seawall, the road and the houses dry above it", ILL, ("Reading council's map", "Does Wynnum flood?"), "which-water"),
    "schools-on-the-bayside-catchments": ("Three children in school hats walking a Bayside footpath toward the school gate", ILL, ("Catchments, in plain words", "Bayside schools"), "the-schools"),
    "what-to-do-in-wynnum-and-manly-with-kids": ("Kids paddling in the tidal wading pool beside the jetty, bikes and towels on the grass", ILL, ("Wynnum &amp; Manly", "With kids"), "the-water"),
    # illustrated posts keep their hero; label only
    "what-asbestos-removal-means-for-a-knockdown-rebuild": (None, None, ("Knockdown rebuild", "Asbestos"), None),
    "what-are-bayside-houses-made-of": (None, None, ("Four eras, one street", "What they're made of"), None),
    "why-are-so-many-bayside-houses-being-knocked-down": (None, None, ("Knockdown rebuild", "Why so many come down"), None),
    "what-is-the-qbcc-and-what-to-check-on-a-builders-licence": (None, None, ("Dealing with a builder", "The QBCC check"), None),
    "who-are-the-small-independent-builders-on-brisbanes-bayside": (None, None, ("Dealing with a builder", "Small builders"), None),
    "bayside-storm-season-roof-trees-insurance": (None, None, ("October to March", "Storm season"), None),
}


def patch(path):
    s = path.read_text(encoding="utf-8")
    n = 0
    for slug, (alt, cap, label, after) in NEW.items():
        m = re.search(r'    slug="' + re.escape(slug) + r'",\n(.*?)    card_title=', s, flags=re.S)
        if not m:
            continue
        block = m.group(1)
        if "label=(" in block:
            continue
        old_alt = re.search(r'    image_alt="(.*?)",\n', block).group(1)
        old_cap = re.search(r'    image_caption="(.*?)",\n', block).group(1)
        new = block
        if alt:
            new = new.replace(f'image="blog/{slug}.png"', f'image="blog/{slug}.jpg"')
            new = new.replace(f'    image_alt="{old_alt}",\n', f'    image_alt="{alt}",\n')
            new = new.replace(f'    image_caption="{old_cap}",\n', f'    image_caption="{cap}",\n')
        add = f'    label=({label[0]!r}, {label[1]!r}),\n'
        if after:
            add += f'    figure=dict(image="blog/{slug}.png", alt={old_alt!r}, caption={old_cap!r}, after={after!r}),\n'
        new = re.sub(r'(    image_caption=".*?",\n)', lambda mm: mm.group(1) + add, new, count=1)
        s = s.replace(block, new, 1)
        n += 1
    path.write_text(s, encoding="utf-8")
    return n


if __name__ == "__main__":
    total = sum(patch(f) for f in sorted(HERE.glob("posts_*.py")))
    print("posts patched:", total)
