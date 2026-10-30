"""Pull long-running builder ads from the Meta Ad Library (Apify) for the Sabre swipe file.

Process: BBL paid-ads-playbook § "Finding creative templates" (run time = the conversion proxy).
Writes raw.json + ads.json + media/ into the research folder given as argv[1].
Token is read from BBL's catalyst config; never printed.
"""
import json, sys, time, urllib.parse, urllib.request, pathlib, datetime

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "media").mkdir(exist_ok=True)

BBL = pathlib.Path.home() / "OneDrive/Desktop/Marketing AI content for Bare Bayside Labs"
cfg = json.loads((BBL / "catalyst/functions/competitor_intel_pipeline/catalyst-config.json").read_text())
TOKEN = cfg["deployment"]["env_variables"]["APIFY_API_TOKEN"] if "deployment" in cfg else cfg["env_variables"]["APIFY_API_TOKEN"]

SEARCHES = [
    ("AU", "knockdown rebuild"), ("AU", "knock down rebuild"), ("AU", "custom home builder"),
    ("AU", "new home builder"), ("AU", "build your new home"), ("AU", "home extension builder"),
    ("US", "custom home builder"), ("US", "tear down rebuild"),
    ("GB", "self build home"), ("NZ", "new home builder"),
]
PER_URL = 120


def lib_url(country, q):
    return ("https://www.facebook.com/ads/library/?" + urllib.parse.urlencode({
        "active_status": "active", "ad_type": "all", "country": country, "q": q,
        "search_type": "keyword_unordered", "media_type": "all"}))


def api(path, data=None):
    url = f"https://api.apify.com/v2/{path}{'&' if '?' in path else '?'}token={TOKEN}"
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


raw_path = OUT / "raw.json"
if raw_path.exists():
    items = json.loads(raw_path.read_text())
else:
    run = api("acts/curious_coder~facebook-ads-library-scraper/runs", {
        "urls": [{"url": lib_url(c, q)} for c, q in SEARCHES],
        "count": PER_URL, "scrapeAdDetails": False,
    })["data"]
    print("run", run["id"], flush=True)
    while True:
        time.sleep(20)
        st = api(f"actor-runs/{run['id']}")["data"]
        print(st["status"], flush=True)
        if st["status"] not in ("READY", "RUNNING"):
            break
    items = api(f"datasets/{st['defaultDatasetId']}/items?clean=true&format=json")
    raw_path.write_text(json.dumps(items))
print("raw items", len(items))

today = datetime.datetime.now(datetime.timezone.utc)
by_id, groups = {}, {}
for it in items:
    snap = it.get("snapshot") or {}
    start = it.get("start_date") or it.get("startDate")
    if not start:
        continue
    start = datetime.datetime.fromtimestamp(int(start), datetime.timezone.utc) if str(start).isdigit() \
        else datetime.datetime.fromisoformat(str(start).replace("Z", "+00:00"))
    days = (today - start).days
    cards = snap.get("cards") or []
    body = (snap.get("body") or {}).get("text") or (cards[0].get("body") if cards else "") or ""
    imgs = [i.get("original_image_url") or i.get("resized_image_url") for i in snap.get("images") or []]
    imgs += [c.get("original_image_url") or c.get("resized_image_url") for c in cards]
    vids = [v.get("video_hd_url") or v.get("video_sd_url") for v in snap.get("videos") or []]
    vids += [c.get("video_hd_url") or c.get("video_sd_url") for c in cards]
    posters = [v.get("video_preview_image_url") for v in snap.get("videos") or []]
    posters += [c.get("video_preview_image_url") for c in cards]
    ad_id = str(it.get("ad_archive_id") or it.get("adArchiveID"))
    page = snap.get("page_name") or it.get("page_name") or ""
    country = next((c for c, q in SEARCHES if urllib.parse.quote(q) in (it.get("url") or "")
                    or q.replace(" ", "+") in (it.get("url") or "")), "")
    rec = {"id": ad_id, "page": page, "country": country, "days": days,
           "fmt": (snap.get("display_format") or "").upper(), "text": body.strip(),
           "title": (snap.get("title") or (cards[0].get("title") if cards else "") or ""),
           "cta": snap.get("cta_text") or "", "link": snap.get("link_url") or "",
           "lib": f"https://www.facebook.com/ads/library/?id={ad_id}",
           "media": [u for u in imgs + posters if u], "video": [u for u in vids if u]}
    if ad_id in by_id:
        continue
    by_id[ad_id] = rec
    groups.setdefault((page, body.strip()[:80]), []).append(ad_id)

ads = []
for (page, _), ids in groups.items():
    best = max((by_id[i] for i in ids), key=lambda r: r["days"])
    best["versions"] = len(ids)
    if best["days"] >= 30:
        ads.append(best)
ads.sort(key=lambda r: -r["days"])
print("kept (30+ days, de-duplicated)", len(ads))


def fetch(url, dest):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
            dest.write_bytes(r.read())
        return True
    except Exception:
        return False


for a in ads:
    a["img"] = a["vid"] = None
    if a["media"] and fetch(a["media"][0], OUT / "media" / f"{a['id']}.jpg"):
        a["img"] = f"media/{a['id']}.jpg"
    if a["video"] and fetch(a["video"][0], OUT / "media" / f"{a['id']}.mp4"):
        a["vid"] = f"media/{a['id']}.mp4"
(OUT / "ads.json").write_text(json.dumps(ads, indent=1))
print("saved media for", sum(1 for a in ads if a["img"] or a["vid"]), "ads")
