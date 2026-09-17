"""Build a Sabre blog post into the REAL repo from a dict in tools/posts_*.py.

    python tools/build_post.py posts_phase1            # builds every post in that module
    python tools/build_post.py posts_phase1 r9-asbestos # one post, by key

The page shell (head, header, footer) is copied from an existing live post so the
kit stays identical; only <main> and the JSON-LD block are generated. After building:
add the card to blog/index.html and the row to sitemap.xml (this script does both),
then bump ?v= only if site.css changed. Article-kit classes: docs/design-system.md.
"""
import html, importlib, json, pathlib, re, sys

WORKSHOP = pathlib.Path(__file__).resolve().parent.parent
REAL = WORKSHOP.parent / "sabre-constructions-website"
BASE = "https://www.sabreconstructions.com.au"
SHELL = REAL / "blog" / "what-is-a-knockdown-rebuild-package" / "index.html"


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def word_count(body_html):
    b = re.sub(r'<nav class="onpage".*?</nav>', "", body_html, flags=re.S)
    return len(text(b).split())


def nice_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {['','January','February','March','April','May','June','July','August','September','October','November','December'][int(m)]} {y}"


def card(p, rel_img):
    return (f'        <a class="post" href="{p["href"]}">\n'
            f'          <img src="{rel_img}{p["image"]}" alt="{p["image_alt"]}" loading="lazy">\n'
            f'          <h3 class="h3">{p["card_title"]}</h3>\n'
            f'          <p>{p["card_blurb"]}</p>\n        </a>\n')


def build(p, all_posts):
    shell = SHELL.read_text(encoding="utf-8")
    words = word_count(p["body"])
    mins = max(1, round(words / 200))
    related = "".join(card({**all_posts[k], "href": f"../{k}/"}, "../../assets/img/") for k in p["related"])
    main = f'''<main>

  <section>
    <div class="wrap">
      <p class="eyebrow">Your questions answered &middot; {p["category"]}</p>
      <h1 class="h1">{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
      <div class="art-meta">
        <span class="by"><img src="../../assets/img/team-nathan.jpg" alt=""><span><b>Nathan Brain</b>, carpenter and builder at Sabre</span></span>
        <span>{nice_date(p["date"])}</span>
        <span>{mins} min read</span>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="wrap prose">
{p["body"].rstrip()}
    </div>
  </section>

  <section class="related">
    <div class="wrap">
      <h2 class="h2">Keep reading</h2>
      <div class="posts">
{related.rstrip()}
      </div>
    </div>
  </section>

  <section class="band-red">
    <div class="wrap">
      <p class="eyebrow">Where most families start</p>
      <h2 class="h2">A walk through your house with Nathan.</h2>
      <p class="lede">{p["cta"]}</p>
      <p><a class="btn" href="../../contact/">Book your walk-through with Nathan</a> <a class="btn btn-ghost" href="tel:+61422831306">Call 0422 831 306</a></p>
      <p class="small">Already thinking about a rebuild? The free block check is on the same page.</p>
    </div>
  </section>
</main>'''
    page = re.sub(r"<main>.*?</main>", lambda m: main, shell, flags=re.S)
    page = re.sub(r"<title>.*?</title>", f'<title>{p["title"]} | Sabre Constructions</title>', page)
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{p["description"]}">', page)

    faqs = re.findall(r'<p class="q">(.*?)</p>\s*<p>(.*?)</p>', p["body"], flags=re.S)
    graph = [{
        "@type": "Article", "@id": f"{BASE}/blog/{p['slug']}/#article",
        "mainEntityOfPage": f"{BASE}/blog/{p['slug']}/",
        "headline": html.unescape(p["title"]), "description": html.unescape(p["description"]),
        "image": f"{BASE}/assets/img/{p['image']}",
        "datePublished": p["date"], "dateModified": p["date"], "inLanguage": "en-AU", "wordCount": words,
        "author": {"@type": "Person", "name": "Nathan Brain", "jobTitle": "Carpenter and builder",
                   "url": f"{BASE}/meet-the-team/", "worksFor": {"@id": f"{BASE}/#org"}},
        "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "Sabre Constructions", "url": BASE + "/",
                      "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/img/sabre-logo.png"}},
        "about": p["about"],
    }]
    if faqs:
        graph.append({"@type": "FAQPage", "@id": f"{BASE}/blog/{p['slug']}/#faq",
                      "mainEntity": [{"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}} for q, a in faqs]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    page = re.sub(r'<script type="application/ld\+json">.*?</script>\n', "", page, flags=re.S)
    page = page.replace("</head>", f'<script type="application/ld+json">\n{ld}\n</script>\n</head>')

    out = REAL / "blog" / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

    return words, mins, len(faqs)


def verify(p):
    """Links and anchors, checked after EVERY post in the run is on disk (posts link to each other)."""
    out = REAL / "blog" / p["slug"] / "index.html"
    page = out.read_text(encoding="utf-8")
    json.loads(re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', page, re.S).group(1))
    ids = set(re.findall(r'id="([^"]+)"', page))
    for a in re.findall(r'href="#([^"]+)"', page):
        assert a in ids, f"{p['slug']}: missing anchor #{a}"
    for href in re.findall(r'(?:href|src)="([^"#]+)"', page):
        if href.startswith(("http", "tel:", "mailto:")):
            continue
        t = out.parent / href.split("?")[0]
        if t.is_dir():
            t = t / "index.html"
        assert t.exists(), f"{p['slug']}: broken link {href}"


def add_to_index_and_sitemap(p):
    idx = REAL / "blog" / "index.html"
    s = idx.read_text(encoding="utf-8")
    if f'href="../blog/{p["slug"]}/"' not in s:
        c = (f'        <a class="post" href="../blog/{p["slug"]}/">\n'
             f'          <img src="../assets/img/{p["image"]}" alt="{p["image_alt"]}" loading="lazy">\n'
             f'          <p class="small">{nice_date(p["date"])}</p>\n'
             f'          <h2 class="h3">{p["card_title"]}</h2>\n'
             f'          <p>{p["card_blurb"]}</p>\n        </a>\n')
        s = s.replace('      <div class="posts">\n', '      <div class="posts">\n' + c, 1)
        idx.write_text(s, encoding="utf-8")
    sm = REAL / "sitemap.xml"
    t = sm.read_text(encoding="utf-8")
    loc = f"  <url><loc>{BASE}/blog/{p['slug']}/</loc></url>\n"
    if loc not in t:
        t = t.replace(f"  <url><loc>{BASE}/contact/</loc></url>", loc + f"  <url><loc>{BASE}/contact/</loc></url>")
        sm.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    sys.path.insert(0, str(WORKSHOP / "tools"))
    mod = importlib.import_module(sys.argv[1])
    posts = mod.POSTS
    keys = sys.argv[2:] or list(posts)
    # live posts that new ones may link to in "Keep reading"
    live = {
        "check-if-your-street-is-in-the-character-overlay": dict(image="design-3-site.jpg?v=2", image_alt="Checking a Bayside block on site", card_title="How to check if your house is in the character overlay", card_blurb="Two free checks and about fifteen minutes. One tells you about your street, the other the year your house went up."),
        "can-we-knock-down-our-house": dict(image="cut-1-old-house.jpg", image_alt="An older Bayside house, cut open", card_title="Can we knock down our house? Brisbane's rules in plain words", card_blurb="The pre-1947 rule, straight from council's own page, and when a protected house can still come down."),
        "what-is-a-knockdown-rebuild-package": dict(image="design-2-table.jpg", image_alt="Choosing a design at the table", card_title="What is a knockdown rebuild package, and is it the right way to build?", card_blurb="What an advertised package bundles, who it suits, and six questions worth asking any builder."),
        "rebuilding-in-wynnum-or-manly": dict(image="proj2x-killarney79.jpg", image_alt="Killarney 79, a Sabre build", card_title="Thinking of rebuilding in Wynnum or Manly? Five things to know first", card_blurb="The pre-1947 rule, what the block decides, where you live while it happens, and who's on the phone in month four."),
    }
    # every post in every tools/posts_*.py can be a "Keep reading" card, whichever module is being built
    all_posts = dict(live)
    for f in sorted((WORKSHOP / "tools").glob("posts_*.py")):
        m = importlib.import_module(f.stem)
        all_posts.update({q["slug"]: q for q in m.POSTS.values()})
    for k in keys:
        p = posts[k]
        w, m, f = build(p, all_posts)
        add_to_index_and_sitemap(p)
        print(f"{p['slug']}: {w} words, {m} min, {f} FAQs")
    for k in keys:
        verify(posts[k])
    print("links, anchors and schema verified on", len(keys), "posts")
