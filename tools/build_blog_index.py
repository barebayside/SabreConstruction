"""Rebuild the REAL repo's blog/index.html in SECTIONS with a sticky right-hand rail.

Cards come from every tools/posts_*.py (field `section`) plus the four hand-built posts listed
here. Within a section, newest first. Run after any build_post.py run:

    python tools/build_blog_index.py
"""
import importlib, pathlib, re, sys

WORKSHOP = pathlib.Path(__file__).resolve().parent.parent
REAL = WORKSHOP.parent / "sabre-constructions-website"
sys.path.insert(0, str(WORKSHOP / "tools"))
from build_post import nice_date, label_html  # noqa: E402

SECTIONS = [
    ("rules", "Can we knock it down?", "The rules first. Brisbane's character overlay, the year your house was built, and what a flood overlay changes &mdash; the checks that decide whether a rebuild is even on the table."),
    ("rebuild", "The knockdown rebuild, in plain words", "What the Bayside's houses are made of, why so many come down, what a package really is, and what asbestos means for the job."),
    ("suburbs", "The Bayside suburbs", "Wynnum, Manly, Lota, Manly West, Wakerley, Gumdale, Ransome and Tingalpa &mdash; honest portraits, with the census numbers, from a builder who works in all of them."),
    ("living", "Living on the Bayside", "Schools and catchments, the train, the weekends, the flood maps and the storm season. The things families weigh up before they decide to stay."),
    ("builder", "Dealing with a builder", "The QBCC, the licence, the warranty, and what &ldquo;small independent builder&rdquo; actually means. The checks that work on any builder, including us."),
]

# the four hand-built posts (not in a posts_*.py module)
HAND = [
    dict(slug="can-we-knock-down-our-house", section="rules", date="2026-09-08", image="blog/can-we-knock-down-our-house.jpg", label=("Brisbane's rules, in plain words", "Can we knock it down?"),
         image_alt="A couple on the footpath looking at a pre-war Queenslander", card_title="Can we knock down our house? Brisbane's rules in plain words",
         card_blurb="Brisbane's character rules in plain words, straight from council's own page, and the three-step check of your own block."),
    dict(slug="check-if-your-street-is-in-the-character-overlay", section="rules", date="2026-09-10", image="blog/check-if-your-street-is-in-the-character-overlay.jpg", label=("Two free checks", "Character overlay"),
         image_alt="Checking council's overlay map on a phone in front of a street of pre-war Queenslanders", card_title="How to check if your house is in the character overlay",
         card_blurb="Two free checks and about fifteen minutes. Council's mapping tells you about your street. Council's archives tell you the year your house went up."),
    dict(slug="what-is-a-knockdown-rebuild-package", section="rebuild", date="2026-09-10", image="blog/what-is-a-knockdown-rebuild-package.jpg", label=("Knockdown rebuild", "The package"),
         image_alt="A plan from a range held up against a sloping Bayside block", card_title="What is a knockdown rebuild package, and is it the right way to build?",
         card_blurb="What's usually bundled into an advertised package, who they suit, where they stop suiting people, and the six questions worth asking any builder."),
    dict(slug="rebuilding-in-wynnum-or-manly", section="rebuild", date="2026-09-08", image="blog/rebuilding-in-wynnum-or-manly.jpg", label=("Five things to know first", "Wynnum & Manly"),
         image_alt="A tired highset on a Bayside street that runs down to the water", card_title="Thinking of rebuilding in Wynnum or Manly? Five things to know first",
         card_blurb="The pre-1947 rule, what the block decides, where you live while it happens, and how to check your own house in five minutes."),
]


def all_posts():
    posts = list(HAND)
    for f in sorted((WORKSHOP / "tools").glob("posts_*.py")):
        m = importlib.import_module(f.stem)
        posts += list(m.POSTS.values())
    return posts


def card(p):
    return (f'          <a class="post" href="../blog/{p["slug"]}/">\n'
            f'            <span class="thumb"><img src="../assets/img/{p["image"]}" alt="{p["image_alt"]}" loading="lazy">{label_html(p)}</span>\n'
            f'            <p class="small">{nice_date(p["date"])}</p>\n'
            f'            <h3 class="h3">{p["card_title"]}</h3>\n'
            f'            <p>{p["card_blurb"]}</p>\n          </a>\n')


def build():
    posts = all_posts()
    for p in posts:
        assert p.get("section") in dict((k, 1) for k, _, _ in SECTIONS), f'{p["slug"]}: no section'
    idx = REAL / "blog" / "index.html"
    page = idx.read_text(encoding="utf-8")
    secs, rail = [], []
    for key, title, intro in SECTIONS:
        ps = sorted([p for p in posts if p["section"] == key], key=lambda p: p["date"], reverse=True)
        if not ps:
            continue
        rail.append(f'          <li><a href="#{key}">{title}</a></li>')
        secs.append(f'''        <section class="blog-sec" id="{key}">
          <h2 class="h2">{title}</h2>
          <p class="lede">{intro}</p>
          <div class="posts" data-section="{key}">
{"".join(card(p) for p in ps).rstrip()}
          </div>
        </section>''')
    nav = ('<nav class="onpage" aria-label="Sections">\n        <p class="eyebrow">Sections</p>\n        <ol>\n' + "\n".join(rail) + '\n        </ol>\n      </nav>')
    main = f'''<main>

  <section>
    <div class="wrap">
      <p class="eyebrow">Your questions answered</p>
      <h1 class="h1">The things families ask<br>before they build.</h1>
      <p class="lede">Plain words on the questions families ask before they build. Written by the people who build, for people who live here. {len(posts)} articles, in five sections.</p>
    </div>
  </section>

  <section class="section-tight">
    <div class="wrap art-grid blog-grid">
      <div class="blog-main">
        {nav.replace('<nav class="onpage"', '<nav class="onpage inline"', 1)}
{chr(10).join(secs)}
      </div>
      <aside class="art-side">
      {nav}
        <div class="side-cta"><p>Room by room, with the builder who'd build the next one. No obligation.</p><a class="btn" href="../contact/">Book a walk-through</a></div>
      </aside>
    </div>
  </section>

  <section class="band-red">
    <div class="wrap">
      <p class="eyebrow">Where most families start</p>
      <h2 class="h2">A walk through your house with Nathan.</h2>
      <p class="lede">Room by room, with the builder who'd build the next one. No obligation, and no need to know what you want yet. He'll ring to set a time that suits the family.</p>
      <p><a class="btn" href="../contact/">Book your walk-through with Nathan</a> <a class="btn btn-ghost" href="tel:+61422831306">Call 0422 831 306</a></p>
      <p class="small">Already thinking about a rebuild? The free block check is on the same page.</p>
    </div>
  </section>
</main>'''
    page = re.sub(r"<main>.*?</main>", lambda m: main, page, flags=re.S)
    if "js/article.js" not in page:
        page = page.replace("</body>", '<script src="../js/article.js?v=1" defer></script>\n</body>')
    idx.write_text(page, encoding="utf-8")
    print(f"blog index: {len(posts)} cards in {len(secs)} sections")


if __name__ == "__main__":
    build()
