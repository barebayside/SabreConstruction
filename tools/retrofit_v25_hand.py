"""v25 one-off (2026-09-17) for the four HAND-BUILT posts: swap the diagram/map hero for the click hero + label,
and keep the diagram/map inside the article as an .art-fig after the named H2. Idempotent.

    python tools/retrofit_v25_hand.py
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_post import label_html, place_figure, REAL  # noqa: E402

ILL = "Illustration in the style of Sabre's story frames, not a photograph of the real street."

HAND = {
    "can-we-knock-down-our-house": dict(
        image="blog/can-we-knock-down-our-house.jpg", image_alt="A couple on the footpath looking at a pre-war Queenslander", image_caption=ILL,
        label=("Brisbane's rules, in plain words", "Can we knock it down?"),
        figure=dict(image="blog/can-we-knock-down-our-house.png", alt="The three dates that decide it: before 1911, 1946 or earlier, after 1946",
                    caption="The three dates Brisbane's character rules turn on.", after="what-is-the-overlay")),
    "check-if-your-street-is-in-the-character-overlay": dict(
        image="blog/check-if-your-street-is-in-the-character-overlay.jpg", image_alt="Checking council's overlay map on a phone in front of a street of pre-war Queenslanders", image_caption=ILL,
        label=("Two free checks", "Character overlay"),
        figure=dict(image="blog/check-if-your-street-is-in-the-character-overlay.png", alt="The two checks: council's overlay map for the street, the archives for the year",
                    caption="Two checks, two sources: the street and the year.", after="check-one")),
    "rebuilding-in-wynnum-or-manly": dict(
        image="blog/rebuilding-in-wynnum-or-manly.jpg", image_alt="A tired highset on a Bayside street that runs down to the water", image_caption=ILL,
        label=("Five things to know first", "Wynnum &amp; Manly"),
        figure=dict(image="blog/rebuilding-in-wynnum-or-manly.png", alt="Map of Wynnum and Manly with the stations, the schools and the foreshore",
                    caption="Wynnum and Manly. Boundaries &copy; OpenStreetMap contributors.", after="block")),
    "what-is-a-knockdown-rebuild-package": dict(
        image="blog/what-is-a-knockdown-rebuild-package.jpg", image_alt="A house plan from a range held up against a sloping Bayside block",
        image_caption="A plan from a range meets a real block. Illustration made from Sabre's photography.",
        label=("Knockdown rebuild", "The package")),
}

for slug, p in HAND.items():
    p["slug"] = slug
    f = REAL / "blog" / slug / "index.html"
    s = f.read_text(encoding="utf-8")
    hero = (f'<figure class="art-hero"><span class="thumb"><img src="../../assets/img/{p["image"]}" alt="{p["image_alt"]}">{label_html(p)}</span>'
            f'<figcaption class="small">{p["image_caption"]}</figcaption></figure>')
    s, n = re.subn(r'<figure class="art-hero">.*?</figure>', lambda m: hero, s, count=1, flags=re.S)
    assert n == 1, slug
    if p.get("figure") and "art-fig" not in s:
        s = place_figure(s, p, "../../assets/img/")
    s = s.replace(f'"image": "https://www.sabreconstructions.com.au/assets/img/blog/{slug}.png"',
                  f'"image": "https://www.sabreconstructions.com.au/assets/img/blog/{slug}.jpg"')
    f.write_text(s, encoding="utf-8")
    print(slug, "hero swapped", "+ figure" if p.get("figure") else "")
