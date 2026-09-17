"""v23 retrofit for the REAL repo, 2026-09-17.

1. Every page: site.css ?v=22 -> ?v=23; footer "Facebook" text link -> Facebook + Instagram icons
   (Instagram stays `hidden` until Nathan confirms the handle - the only public @sabreconstruction is a
   different, civil-works business).
2. The four HAND-BUILT posts (R1, R2, R15, Wynnum) get the article layout the builder now emits:
   header figure, art-grid with a sticky right-hand "On this page" rail, article.js.
   The 17 generated posts get it by re-running build_post.py.

    python tools/retrofit_v23.py
"""
import pathlib, re

REAL = pathlib.Path(__file__).resolve().parent.parent.parent / "sabre-constructions-website"

FB = ('<a href="https://www.facebook.com/sabreconstructions" aria-label="Sabre Constructions on Facebook" rel="noopener">'
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8.2h2.8l.4-3.3h-3.2V8.4c0-.9.3-1.6 1.6-1.6h1.7V3.9c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.3h2.8V22h3.4z"/></svg></a>')
IG = ('<a href="#" hidden data-note="Instagram handle not yet confirmed by Nathan - do not guess it" aria-label="Sabre Constructions on Instagram" rel="noopener">'
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM12 3.8c2.7 0 3 0 4.1.1 2.7.1 4 1.4 4.1 4.1.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c-.1 2.7-1.4 4-4.1 4.1-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-2.7-.1-4-1.4-4.1-4.1C3.8 15 3.8 14.7 3.8 12s0-3 .1-4.1C4 5.2 5.3 3.9 8 3.8c1.1-.1 1.4-.1 4-.1zM12 2C9.3 2 8.9 2 7.9 2.1 4.2 2.2 2.2 4.2 2.1 7.9 2 8.9 2 9.3 2 12s0 3.1.1 4.1c.1 3.7 2.1 5.7 5.8 5.8 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c3.7-.1 5.7-2.1 5.8-5.8.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.1-3.7-2.1-5.7-5.8-5.8C15.1 2 14.7 2 12 2z"/></svg></a>')

# hand-built posts: slug -> (image file under assets/img/, alt, caption)
HAND = {
    "can-we-knock-down-our-house": ("blog/can-we-knock-down-our-house.png", "The three dates that decide it: before 1911, 1946 or earlier, after 1946", "The three dates Brisbane's character rules turn on."),
    "check-if-your-street-is-in-the-character-overlay": ("blog/check-if-your-street-is-in-the-character-overlay.png", "The two checks: council's overlay map for the street, the archives for the year", "Two checks, two sources: the street and the year."),
    "what-is-a-knockdown-rebuild-package": ("blog/what-is-a-knockdown-rebuild-package.jpg", "A house plan from a range held up against a sloping Bayside block", "A plan from a range meets a real block. Illustration made from Sabre's photography."),
    "rebuilding-in-wynnum-or-manly": ("blog/rebuilding-in-wynnum-or-manly.png", "Map of Wynnum and Manly with the stations, the schools and the foreshore", "Wynnum and Manly. Boundaries &copy; OpenStreetMap contributors."),
}


def social(page):
    page = page.replace(' &middot; <a href="https://www.facebook.com/sabreconstructions">Facebook</a></p>',
                        '</p>\n      <div class="social">' + FB + IG + '</div>')
    return page


def layout(page, img, alt, cap, rel):
    if 'art-grid' in page:
        return page
    # header figure after the meta row
    page = re.sub(r'(<div class="art-meta">.*?</div>)',
                  lambda m: m.group(1) + f'\n      <figure class="art-hero"><img src="{rel}assets/img/{img}" alt="{alt}"><figcaption class="small">{cap}</figcaption></figure>',
                  page, count=1, flags=re.S)
    m = re.search(r'<section class="section-tight">\s*<div class="wrap prose">(.*?)</div>\s*</section>', page, flags=re.S)
    inner = m.group(1)
    nav = re.search(r'<nav class="onpage"[^>]*>.*?</nav>', inner, flags=re.S).group(0)
    inner2 = inner.replace(nav, nav.replace('<nav class="onpage"', '<nav class="onpage inline"', 1), 1)
    cta = re.search(r'<section class="band-red">.*?<p class="lede">(.*?)</p>', page, flags=re.S).group(1)
    grid = ('<section class="section-tight">\n    <div class="wrap art-grid">\n      <div class="prose">' + inner2.rstrip() +
            '\n      </div>\n      <aside class="art-side">\n' + nav +
            f'\n        <div class="side-cta"><p>{cta}</p><a class="btn" href="{rel}contact/">Book a walk-through</a></div>\n      </aside>\n    </div>\n  </section>')
    page = page[:m.start()] + grid + page[m.end():]
    if "js/article.js" not in page:
        page = page.replace("</body>", f'<script src="{rel}js/article.js?v=1" defer></script>\n</body>')
    return page


def index_cards():
    idx = REAL / "blog" / "index.html"
    s = idx.read_text(encoding="utf-8")
    for slug, (img, alt, cap) in HAND.items():
        s = re.sub(r'(<a class="post" href="\.\./blog/' + re.escape(slug) + r'/">\s*<img src=")[^"]*(" alt=")[^"]*(")',
                   lambda m: m.group(1) + f'../assets/img/{img}' + m.group(2) + alt + m.group(3), s, count=1)
    idx.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    index_cards()
    n = 0
    for f in REAL.rglob("index.html"):
        s = f.read_text(encoding="utf-8")
        t = s.replace("site.css?v=22", "site.css?v=23")
        t = social(t)
        slug = f.parent.name
        if f.parent.parent.name == "blog" and slug in HAND:
            img, alt, cap = HAND[slug]
            t = layout(t, img, alt, cap, "../../")
        if t != s:
            f.write_text(t, encoding="utf-8"); n += 1
    print("pages touched:", n)
