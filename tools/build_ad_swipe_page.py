"""Build index.html for a Sabre ad swipe folder from its ads.json (see pull_ad_swipe.py).

Top: the models we'd copy the STRUCTURE of for Sabre (never the words or footage).
Below: every long-running builder ad, filterable.
Usage: python tools/build_ad_swipe_page.py marketing/research/<date>-builder-ad-swipe
"""
import json, sys, pathlib, html

D = pathlib.Path(sys.argv[1])
ads = json.loads((D / "ads.json").read_text(encoding="utf-8"))
by = {a["id"]: a for a in ads}
e = html.escape

# Each model: the example ads, why it lasts, and the Sabre remake. Hook numbers = marketing/walkthrough.html doors.
MODELS = [
    dict(name="Same street, new house", ids=["1836736863963761", "1363829652019149", "1043873818658103", "3373454689525760"],
         why="Five different builders run this one idea right now (SJD, Henley, Simonds, Carlisle, Fairhaven). When rivals all keep paying for the same line, it's a template, not a fluke.",
         shape="A finished home on a real-looking street, family in shot, three or four words on top. Copy: you love the suburb, the house doesn't fit any more, rebuild where you are.",
         sabre="<b>“You picked this street. Don't let the house decide you have to leave it.”</b> (door 2) over a Sabre-built home on a Bayside street. Name the suburb in the copy: Wynnum, Manly, Birkdale.",
         need="A real Sabre home photo on a Bayside street (we have the Clarence and gallery shots). No AI after-shots."),
    dict(name="The owner talks to camera", ids=["1216526503779358"],
         why="286 days running. The builder himself, phone-style video, greets the area by name: “Hi Inner Sydney… I'm Kurt.” People hire the person.",
         shape="Opens on a local greeting + his name, one problem he solves, a no-obligation first meeting. Shot on site, not in a studio.",
         sabre="<b>“G'day Wynnum. I'm Nathan from Sabre.”</b> → “I only take a handful of homes at a time, so the builder who walks your old house is the one who answers the phone the day you get the keys.” (door 1) → Book a walk-through.",
         need="20–30 seconds of Nathan on his phone, on a site. Nathan confirms “a handful at a time” in his words. We do NOT copy Kurt's cash guarantees."),
    dict(name="Limited number of builds this year", ids=["742645148203054"],
         why="495 days running, in Brisbane. “For a LIMITED number of new home projects…” plus a cheeky “5 reasons you should NEVER build with us” list that's really five benefits.",
         shape="Local call-out (BRISBANE…), scarcity that's true, one included extra, a click to “see if your build qualifies”.",
         sabre="Fits the <b>2027 build slots</b> push already planned: “Nathan books a handful of 2027 homes. Here's what's included…” The playful reverse list can carry Sabre's real points (same builder start to finish, since 1990, Bayside only).",
         need="The real number of 2027 slots and the upgrade pack contents from Nathan (both owed in the push brief). No invented dollar values."),
    dict(name="Worst house, best street (before → after)", ids=["1240761314748271", "2954247028058662"],
         why="788 days (Homes by Ivy story) and Metricon's “From the past to the present” (188 days). The old house is the hook; the new one is the reward.",
         shape="Carousel or short video: the tired old house first, then the finished home on the same block. One line of story.",
         sabre="<b>“Same block. The old house out, a home that fits the family in.”</b> Built from a real Sabre job: the knockdown video and the job photos Nathan has.",
         need="A real before + after pair from one Sabre job, and the owners' OK to show it."),
    dict(name="Read this first (guide or warning)", ids=["1713960296301513", "1332411935494434", "1652829292534083"],
         why="Harwood (142 days), Valor (158), Appex (190): “Thinking of renovating? Read this first”, “Avoid these mistakes”, a free knockdown-rebuild guide. They catch people early, before they've picked a builder.",
         shape="A warning or a question in the headline, then a free guide or a free chat. Gives first, asks second.",
         sabre="<b>“Some houses in Wynnum can't legally be knocked down. Do you know if yours is one?”</b> (door 3) → the character-overlay check post that's already live on the new site.",
         need="Nothing. This one can be made now."),
    dict(name="Free block check", ids=["963360129403115", "1311873613607931"],
         why="Fairhaven (191 days) and Carlisle (161 days): “Don't move, rebuild” + a free block check or site assessment. A small, low-risk first step.",
         shape="Headline = don't move; offer = free check of your block; button = get started.",
         sabre="Sabre already has the free block check on the contact page. Ad: <b>“Before you sell, find out what your block can take.”</b> → block check form.",
         need="Nathan confirms who does the check and how fast he replies."),
]


def media(a, big=False):
    if a.get("vid"):
        return f'<video src="{a["vid"]}" poster="{a.get("img") or ""}" controls preload="none" playsinline></video>'
    if a.get("img"):
        return f'<img src="{a["img"]}" loading="lazy" alt="">'
    return '<div class="none">no preview</div>'


def card(a):
    return (f'<div class="c" data-fmt="{e(a["fmt"])}" data-days="{a["days"]}" data-kdr="{1 if "rebuild" in (a["text"]+a["title"]).lower() or "knock" in (a["text"]+a["title"]).lower() else 0}">'
            f'<div class="m">{media(a)}</div><div class="meta"><b>{e(a["page"])}</b><br>'
            f'<span class="tag d">{a["days"]} days</span><span class="tag">{e(a["country"])}</span><span class="tag">{e(a["fmt"])}</span>'
            + (f'<span class="tag v">{a["versions"]} versions</span>' if a.get("versions", 1) > 1 else "")
            + f'</div>' + (f'<h4>{e(a["title"])}</h4>' if a["title"] and a["title"] != a["page"] else "")
            + f'<p>{e(a["text"])}</p><a href="{e(a["lib"])}" target="_blank" rel="noopener">Open in Ad Library ↗</a></div>')


models_html = []
for i, m in enumerate(MODELS, 1):
    ex = [by[x] for x in m["ids"] if x in by]
    lead = ex[0]
    more = "".join(f'<a href="{e(a["lib"])}" target="_blank" rel="noopener">{e(a["page"])} · {a["days"]}d</a>' for a in ex)
    models_html.append(f'''<section class="model"><div class="mm">{media(lead)}</div><div class="mt">
<div class="num">Model {i}</div><h3>{e(m["name"])}</h3>
<p class="q">“{e(lead["title"] if lead["title"] and lead["title"] != lead["page"] else lead["text"][:110])}”<span> · {e(lead["page"])}</span></p>
<dl><dt>Why it's worth copying</dt><dd>{e(m["why"])}</dd>
<dt>The shape</dt><dd>{e(m["shape"])}</dd>
<dt>Sabre's version</dt><dd class="s">{m["sabre"]}</dd>
<dt>What we need</dt><dd>{e(m["need"])}</dd></dl>
<div class="ex">Examples: {more}</div></div></section>''')

n_kdr = sum(1 for a in ads if "rebuild" in (a["text"]+a["title"]).lower() or "knock" in (a["text"]+a["title"]).lower())
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Builder ads that last</title>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F8F7F4;--card:#fff;--ink:#1B1C1F;--mute:#6b6b6b;--red:#EB2227;--line:#e6e3dd}}
*{{box-sizing:border-box}} body{{margin:0;font:15px/1.5 Figtree,system-ui,sans-serif;background:var(--bg);color:var(--ink)}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 16px}}
header{{padding:36px 0 20px;border-bottom:1px solid var(--line)}} h1{{font-weight:600;font-size:30px;margin:0 0 8px}}
.lede{{color:var(--mute);max-width:760px;margin:0}} .lede b{{color:var(--ink)}}
h2{{font-weight:600;font-size:22px;margin:40px 0 6px}} h2+p{{color:var(--mute);margin:0 0 18px}}
.model{{display:grid;grid-template-columns:300px 1fr;gap:24px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin:0 0 18px}}
.mm{{background:#000;border-radius:10px;overflow:hidden;aspect-ratio:4/5;display:flex}} .mm img,.mm video{{width:100%;height:100%;object-fit:cover}}
.num{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--red);font-weight:600}}
h3{{margin:2px 0 6px;font-size:21px;font-weight:600}} .q{{margin:0 0 12px;font-style:italic}} .q span{{font-style:normal;color:var(--mute);font-size:13px}}
dl{{margin:0}} dt{{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin-top:10px}} dd{{margin:2px 0 0}}
dd.s{{border-left:3px solid var(--red);padding-left:10px}}
.ex{{margin-top:12px;font-size:13px;color:var(--mute)}} .ex a{{color:var(--ink);margin-right:10px;white-space:nowrap}}
.rules{{background:#1B1C1F;color:#f3f1ec;border-radius:14px;padding:18px 20px;margin:24px 0}} .rules b{{color:#fff}} .rules ul{{margin:6px 0 0;padding-left:18px}}
.f{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:12px}} select{{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:#fff}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;padding-bottom:40px}}
.c{{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column}}
.c .m{{background:#000;aspect-ratio:4/5;display:flex}} .c .m img,.c .m video{{width:100%;height:100%;object-fit:contain}} .none{{color:#999;margin:auto}}
.meta{{padding:10px 12px 0;font-size:14px}} .tag{{display:inline-block;font-size:11px;background:#efece6;border-radius:99px;padding:1px 8px;margin:4px 4px 0 0}}
.tag.d{{background:var(--red);color:#fff}} .tag.v{{background:#1B1C1F;color:#fff}}
.c h4{{margin:8px 12px 0;font-size:14px;font-weight:600}} .c p{{padding:0 12px;margin:6px 0;font-size:12.5px;color:#444;flex:1;max-height:9em;overflow:auto;white-space:pre-line}}
.c>a{{padding:0 12px 12px;color:var(--red);font-size:12.5px}}
@media (max-width:720px){{.model{{grid-template-columns:1fr}} .mm{{max-width:360px}} h1{{font-size:24px}}}}
</style></head><body><div class="wrap">
<header><h1>Builder ads that have lasted, and the ones we'd model for Sabre</h1>
<p class="lede">{len(ads)} builder ads from Meta's Ad Library, all <b>live and running 30+ days</b> as of 30 Oct 2026 ({n_kdr} about knockdown rebuild). Run time is the only public sign an ad works, because nobody keeps paying for a loser. Longest-running first. Searched: knockdown rebuild, custom home builder, new home builder, home extension builder (AU), plus US/UK/NZ. <a href="sabre-mockups/index.html" style="color:#EB2227">See the Sabre image ad options →</a></p></header>
<div class="rules"><b>How we use these.</b> We copy the <b>shape</b> of an ad that's lasting (the angle, the format, the kind of offer), never another builder's words, photos or claims. Every Sabre version uses Sabre's own homes, Nathan's own voice, and only facts Nathan has confirmed.</div>
<h2>Six models for Sabre</h2><p>Each one: the ad that's lasting, why, and what the Sabre version would look like.</p>
{"".join(models_html)}
<h2>Every builder ad in the pull</h2><p>Click any ad to see it live in the Ad Library.</p>
<div class="f"><select id="fm"><option value="">All formats</option><option>VIDEO</option><option>IMAGE</option><option>CAROUSEL</option><option>DCO</option></select>
<select id="dy"><option value="30">30+ days</option><option value="90">90+ days</option><option value="180">180+ days</option><option value="365">1 year+</option></select>
<select id="kd"><option value="">Any topic</option><option value="1">Knockdown rebuild only</option></select><span id="n" style="color:var(--mute);font-size:13px"></span></div>
<div class="g" id="g">{"".join(card(a) for a in ads)}</div></div>
<script>
const g=[...document.querySelectorAll('#g .c')],fm=document.getElementById('fm'),dy=document.getElementById('dy'),kd=document.getElementById('kd'),n=document.getElementById('n');
function f(){{let k=0;g.forEach(c=>{{const s=(!fm.value||c.dataset.fmt==fm.value)&&+c.dataset.days>=+dy.value&&(!kd.value||c.dataset.kdr==kd.value);c.style.display=s?'':'none';k+=s}});n.textContent=k+' ads'}}
[fm,dy,kd].forEach(x=>x.onchange=f);f();
</script></body></html>'''
(D / "index.html").write_text(page, encoding="utf-8")
print("wrote", D / "index.html", len(ads), "ads,", len(MODELS), "models")
