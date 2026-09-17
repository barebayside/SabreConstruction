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
FIG_V = 2   # in-article maps/diagrams; 2 = rail symbol + key (2026-09-17)
SHELL = REAL / "blog" / "what-is-a-knockdown-rebuild-package" / "index.html"


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def word_count(body_html):
    b = re.sub(r'<nav class="onpage".*?</nav>', "", body_html, flags=re.S)
    return len(text(b).split())


def nice_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {['','January','February','March','April','May','June','July','August','September','October','November','December'][int(m)]} {y}"


def label_html(p):
    """v25: the topic/suburb label sits OVER the image as HTML (post `label` = (kicker, big)), never in the pixels."""
    if not p.get("label"):
        return ""
    k, b = p["label"]
    return f'<span class="label"><span>{k}</span><b>{b}</b></span>'


def figure_html(p, rel_img):
    """v25: the explanatory map/diagram (post `figure` = dict(image, alt, caption, after=<h2 id>)) kept inside the body."""
    f = p.get("figure")
    if not f:
        return ""
    # ?v= on the figure: browsers and the Pages CDN hold images for 10 min; bump FIG_V when a map/diagram is re-rendered
    return (f'\n      <figure class="art-fig"><img src="{rel_img}{f["image"]}?v={FIG_V}" alt="{f["alt"]}" loading="lazy">'
            f'<figcaption class="small">{f["caption"]}</figcaption></figure>')


def place_figure(body, p, rel_img):
    """Insert the figure after the first paragraph that follows the H2 named in figure.after."""
    fig = figure_html(p, rel_img)
    if not fig:
        return body
    m = re.search(r'<h2 class="h2" id="' + re.escape(p["figure"]["after"]) + r'".*?</h2>', body, flags=re.S)
    assert m, f'{p["slug"]}: figure.after #{p["figure"]["after"]} not found'
    end = body.find("</p>", m.end())
    at = end + 4 if end != -1 else m.end()
    return body[:at] + fig + body[at:]


def card(p, rel_img):
    return (f'        <a class="post" href="{p["href"]}">\n'
            f'          <span class="thumb"><img src="{rel_img}{p["image"]}" alt="{p["image_alt"]}" loading="lazy">{label_html(p)}</span>\n'
            f'          <h3 class="h3">{p["card_title"]}</h3>\n'
            f'          <p>{p["card_blurb"]}</p>\n        </a>\n')


def build(p, all_posts):
    shell = SHELL.read_text(encoding="utf-8")
    words = word_count(p["body"])
    mins = max(1, round(words / 200))
    related = "".join(card({**all_posts[k], "href": f"../{k}/"}, "../../assets/img/") for k in p["related"])
    nav = re.search(r'<nav class="onpage"[^>]*>.*?</nav>', p["body"], flags=re.S).group(0)
    body = p["body"].rstrip().replace(nav, nav.replace('<nav class="onpage"', '<nav class="onpage inline"', 1), 1)
    body = place_figure(body, p, "../../assets/img/")
    side_nav = nav
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
      <figure class="art-hero"><span class="thumb"><img src="../../assets/img/{p["image"]}" alt="{p["image_alt"]}">{label_html(p)}</span><figcaption class="small">{p.get("image_caption","")}</figcaption></figure>
    </div>
  </section>

  <section class="section-tight">
    <div class="wrap art-grid">
      <div class="prose">
{body}
      </div>
      <aside class="art-side">
{side_nav}
        <div class="side-cta"><p>{p["cta"]}</p><a class="btn" href="../../contact/">Book a walk-through</a></div>
      </aside>
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
    if "js/article.js" not in page:
        page = page.replace("</body>", '<script src="../../js/article.js?v=1" defer></script>\n</body>')
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
    """Sitemap row only - blog/index.html is rebuilt in sections by build_blog_index.py."""
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
        "check-if-your-street-is-in-the-character-overlay": dict(image="blog/check-if-your-street-is-in-the-character-overlay.jpg", image_alt="Checking council's overlay map on a phone in front of a street of pre-war Queenslanders", label=("Two free checks", "Character overlay"), card_title="How to check if your house is in the character overlay", card_blurb="Two free checks and about fifteen minutes. One tells you about your street, the other the year your house went up."),
        "can-we-knock-down-our-house": dict(image="blog/can-we-knock-down-our-house.jpg", image_alt="A couple on the footpath looking at a pre-war Queenslander", label=("Brisbane's rules, in plain words", "Can we knock it down?"), card_title="Can we knock down our house? Brisbane's rules in plain words", card_blurb="The pre-1947 rule, straight from council's own page, and when a protected house can still come down."),
        "what-is-a-knockdown-rebuild-package": dict(image="blog/what-is-a-knockdown-rebuild-package.jpg", image_alt="A plan from a range held up against a sloping Bayside block", label=("Knockdown rebuild", "The package"), card_title="What is a knockdown rebuild package, and is it the right way to build?", card_blurb="What an advertised package bundles, who it suits, and six questions worth asking any builder."),
        "rebuilding-in-wynnum-or-manly": dict(image="blog/rebuilding-in-wynnum-or-manly.jpg", image_alt="A tired highset on a Bayside street that runs down to the water", label=("Five things to know first", "Wynnum & Manly"), card_title="Thinking of rebuilding in Wynnum or Manly? Five things to know first", card_blurb="The pre-1947 rule, what the block decides, where you live while it happens, and who's on the phone in month four."),
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
    import build_blog_index; build_blog_index.build()
