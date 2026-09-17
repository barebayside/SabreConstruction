"""Draw the blog's map and diagram images as SVG in Sabre's palette, render to PNG with headless Edge.

Boundaries are real: OpenStreetMap suburb polygons fetched from Nominatim (cached JSON in GEO).
Points are Nominatim geocodes + Wikipedia coordinates. Attribution "© OpenStreetMap contributors"
is drawn into every map (ODbL). No flood extents, catchment lines or anything we did not measure
are drawn - pins and boundaries only. Output: <real repo>/assets/img/blog/<slug>.png, 1600x1067 (3:2).

    python tools/gen_blog_maps.py            # all
    python tools/gen_blog_maps.py lota       # one, by key
"""
import json, math, pathlib, subprocess, sys, html

HERE = pathlib.Path(__file__).resolve().parent
REAL = HERE.parent.parent / "sabre-constructions-website"
OUT = REAL / "assets" / "img" / "blog"
GEO = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(r"C:\Users\edast\AppData\Local\Temp\claude\C--Users-edast\2c4032be-d908-4faf-9241-faa7d286f234\scratchpad\geo")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
W, H = 1600, 1067

# palette - docs/design-system.md, plus one water tone and one soft tint for the featured suburb
PAPER, WHITE, INK, INK2, MUTED, LINE, RED = "#F8F7F4", "#FFFFFF", "#22232A", "#4A4B52", "#8A8B93", "#DDDAD3", "#EB2227"
WATER, TINT = "#D6DFE4", "#EDE9E1"

# ------------------------------------------------------------------ data
def polys(name):
    f = GEO / (name.replace(" ", "_") + ".json")
    if not f.exists():
        return []
    rs = json.load(open(f, encoding="utf-8"))
    rs = sorted(rs, key=lambda r: 0 if r.get("class") == "boundary" else 1)  # suburb boundary before any park/place of the same name
    for r in rs:
        g = r.get("geojson") or {}
        if g.get("type") == "Polygon":
            return [g["coordinates"][0]]
        if g.get("type") == "MultiPolygon":
            return [pp[0] for pp in g["coordinates"]]
    return []

ALL_LAND = ["Wynnum", "Manly", "Lota", "Manly West", "Wakerley", "Gumdale", "Ransome", "Tingalpa", "Wynnum West", "Hemmant",
            "Lytton", "Capalaba", "Birkdale", "Thorneside", "Belmont", "Chandler", "Wellington Point", "Murarrie", "Port of Brisbane",
            "Carindale", "Cannon Hill", "Morningside", "Carina", "Carina Heights", "Mansfield", "Mackenzie", "Burbank", "Sheldon",
            "Alexandra Hills", "Ormiston", "Cleveland", "Mount Cotton", "Rochedale", "Bulimba", "Balmoral", "Hawthorne", "Norman Park",
            "Camp Hill", "Seven Hills", "Wishart", "Upper Mount Gravatt", "Eight Mile Plains", "Priestdale", "Thornlands", "Victoria Point",
            "Redland Bay", "Coorparoo", "Greenslopes", "Holland Park", "Holland Park West", "Mount Gravatt East", "Mount Gravatt"]

PTS = json.load(open(GEO / "points.json", encoding="utf-8")) if (GEO / "points.json").exists() else {}
def pt(k):
    p = PTS[k]; return (p["lon"], p["lat"])

STATIONS = [("Lindum", pt("st_lindum")), ("Wynnum North", pt("st_wynnum_north")), ("Wynnum", pt("st_wynnum")),
            ("Wynnum Central", pt("st_wynnum_central")), ("Manly", pt("st_manly")), ("Lota", pt("st_lota"))]
# Thorneside station (from the Thorneside search) so the line runs on past Lota
def extra_station(name):
    f = GEO / (name + ".json")
    if f.exists():
        for r in json.load(open(f, encoding="utf-8")):
            if r.get("type") == "station":
                return (float(r["lon"]), float(r["lat"]))
    return None
_th = extra_station("Thorneside")
if _th: STATIONS.append(("Thorneside", _th))
_he = extra_station("Hemmant")
if _he: STATIONS.insert(0, ("Hemmant", _he))

# ------------------------------------------------------------------ projection
class Proj:
    def __init__(self, lon0, lon1, lat0, lat1, pad=0.06):
        # fit bbox into W x H keeping metres square
        latm = (lat0 + lat1) / 2
        kx = math.cos(math.radians(latm))
        w_deg = (lon1 - lon0) * kx; h_deg = (lat1 - lat0)
        w_deg *= 1 + 2 * pad; h_deg *= 1 + 2 * pad
        s = min(W / w_deg, H / h_deg)
        self.kx, self.s = kx, s
        self.cx, self.cy = (lon0 + lon1) / 2, (lat0 + lat1) / 2
    def __call__(self, lon, lat):
        x = W / 2 + (lon - self.cx) * self.kx * self.s
        y = H / 2 - (lat - self.cy) * self.s
        return x, y
    def km(self):  # px per km
        return self.s / 111.32

def path(ring, P):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in (P(lon, lat) for lon, lat in ring)) + " Z"

def esc(s): return html.escape(s, quote=False)

# ------------------------------------------------------------------ drawing
def label(x, y, text, size=22, weight=500, fill=INK, anchor="middle", italic=False, tracking=0, upper=False):
    style = f'font-family:Figtree,Arial,sans-serif;font-size:{size}px;font-weight:{weight};fill:{fill};' + ("font-style:italic;" if italic else "") + (f"letter-spacing:{tracking}px;" if tracking else "")
    t = text.upper() if upper else text
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" style="{style}" paint-order="stroke" stroke="{PAPER}" stroke-width="6" stroke-linejoin="round">{esc(t)}</text>'

def pin(x, y, text=None, fill=INK, r=9, side="right", size=20, weight=500):
    s = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{WHITE}" stroke-width="3"/>'
    if text:
        if side == "right": s += label(x + r + 10, y + 7, text, size, weight, INK, "start")
        elif side == "left": s += label(x - r - 10, y + 7, text, size, weight, INK, "end")
        elif side == "above": s += label(x, y - r - 8, text, size, weight, INK, "middle")
        else: s += label(x, y + r + 24, text, size, weight, INK, "middle")
    return s

def school(x, y, text, kind="state", side="right"):
    # state = filled square, independent = hollow square
    if kind == "state":
        s = f'<rect x="{x-8:.1f}" y="{y-8:.1f}" width="16" height="16" fill="{INK}" stroke="{WHITE}" stroke-width="3"/>'
    else:
        s = f'<rect x="{x-8:.1f}" y="{y-8:.1f}" width="16" height="16" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
    if side == "right": s += label(x + 18, y + 6, text, 18, 500, INK2, "start")
    elif side == "left": s += label(x - 18, y + 6, text, 18, 500, INK2, "end")
    elif side == "above": s += label(x, y - 16, text, 18, 500, INK2, "middle")
    else: s += label(x, y + 26, text, 18, 500, INK2, "middle")
    return s

def shift(labs, name, dx=0, dy=0):
    x, y = labs[name]; labs[name] = (x + dx, y + dy); return labs

def rail_symbol(d):
    """The standard map railway: a dark line with a white dashed centreline. Was a plain dotted line until
    2026-09-17, which read as 'some boundary' - Edward asked for it to be identifiable as the train."""
    return [f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="butt"/>',
            f'<path d="{d}" fill="none" stroke="{WHITE}" stroke-width="2.5" stroke-dasharray="14 14"/>']

def rail_key(x, y):
    """Legend entry for the railway, drawn next to the scale bar."""
    return rail_symbol(f"M{x},{y} L{x+70},{y}") + [label(x + 84, y + 7, "Cleveland line (train)", 18, 500, INK2, "start")]

def basemap(P, featured, labels_for, rail=True, bay_label=True, redland=False):
    out = [f'<rect width="{W}" height="{H}" fill="{WATER}"/>']
    for n in ALL_LAND:
        for ring in polys(n):
            out.append(f'<path d="{path(ring, P)}" fill="{PAPER}" stroke="{LINE}" stroke-width="1.5" stroke-linejoin="round"/>')
    for n in featured:
        for ring in polys(n):
            out.append(f'<path d="{path(ring, P)}" fill="{TINT}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    if rail:
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in (P(*ll) for _, ll in STATIONS))
        out += rail_symbol(d)
    for n, (x, y) in labels_for.items():
        big = n in featured
        out.append(label(x, y, n, 34 if big else 19, 600 if big else 500, INK if big else MUTED, "middle", tracking=0 if big else 2, upper=not big))
    if bay_label:
        out.append(label(W - 60, 80, "Moreton Bay", 26, 500, "#7D8B93", "end", italic=True))
    return out

def frame(P, note, rail=True):
    # scale bar, north, attribution, rail key
    k = P.km(); x0, y0 = 60, H - 60
    s = (rail_key(x0, y0 - 52) if rail else []) + [f'<line x1="{x0}" y1="{y0}" x2="{x0+2*k:.1f}" y2="{y0}" stroke="{INK}" stroke-width="3"/>',
         f'<line x1="{x0}" y1="{y0-8}" x2="{x0}" y2="{y0+8}" stroke="{INK}" stroke-width="3"/>',
         f'<line x1="{x0+2*k:.1f}" y1="{y0-8}" x2="{x0+2*k:.1f}" y2="{y0+8}" stroke="{INK}" stroke-width="3"/>',
         label(x0 + k, y0 - 14, "2 km", 16, 500, INK2, "middle"),
         label(W - 60, H - 40, "Boundaries \u00a9 OpenStreetMap contributors \u00b7 " + note, 15, 400, MUTED, "end"),
         f'<text x="{W-70}" y="{H-92}" text-anchor="middle" style="font-family:Figtree,Arial;font-size:16px;font-weight:600;fill:{INK}">N</text>',
         f'<path d="M{W-70},{H-125} l7,20 l-7,-5 l-7,5 z" fill="{INK}"/>']
    return s

def svg(parts):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>"

def centroid(name):
    ring = polys(name)[0]
    xs = [a for a, b in ring]; ys = [b for a, b in ring]
    return (sum(xs) / len(xs), sum(ys) / len(ys))

# ------------------------------------------------------------------ the maps
MAPS = {}

def m_acreage():
    P = Proj(153.10, 153.23, -27.54, -27.42)
    feat = ["Ransome", "Tingalpa", "Gumdale"]
    labs = {n: P(*centroid(n)) for n in feat + ["Wynnum", "Manly", "Lota", "Manly West", "Wakerley", "Capalaba", "Belmont", "Chandler", "Birkdale", "Hemmant", "Murarrie", "Wynnum West"]}
    shift(labs, "Gumdale", -40, 60); shift(labs, "Ransome", 30, -40)
    x, y = P(*pt("molle"))
    parts = basemap(P, feat, labs) + [pin(x, y, "Sabre, 40 Molle Rd", RED, 11, "below", 22, 600)]
    parts += frame(P, "Ransome, Tingalpa and Gumdale")
    return svg(parts)
MAPS["ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside"] = m_acreage

def m_three():
    P = Proj(153.13, 153.215, -27.49, -27.415)
    feat = ["Wynnum", "Manly", "Lota"]
    labs = {n: P(*centroid(n)) for n in feat + ["Manly West", "Wynnum West", "Ransome", "Hemmant", "Wakerley", "Lytton"]}
    parts = basemap(P, feat, labs)
    for n, ll in STATIONS:
        if n in ("Wynnum North", "Wynnum", "Wynnum Central", "Manly", "Lota"):
            x, y = P(*ll); parts.append(pin(x, y, n + " station", INK, 7, "left", 17))
    parts += frame(P, "Wynnum, Manly and Lota")
    return svg(parts)
MAPS["wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family"] = m_three

def m_manly_west():
    P = Proj(153.13, 153.215, -27.495, -27.43)
    feat = ["Manly", "Manly West"]
    labs = {n: P(*centroid(n)) for n in feat + ["Wynnum", "Lota", "Wynnum West", "Wakerley", "Ransome", "Tingalpa", "Gumdale"]}
    shift(labs, "Manly", -30, -70)
    parts = basemap(P, feat, labs)
    x, y = P(*pt("harbour")); parts.append(pin(x, y, "Boat harbour", INK, 8, "right", 18))
    x, y = P(*pt("st_manly")); parts.append(pin(x, y, "Manly station", INK, 7, "below", 17))
    parts += frame(P, "Manly and Manly West, split in 1975")
    return svg(parts)
MAPS["whats-the-difference-between-manly-and-manly-west"] = m_manly_west

def m_lota():
    P = Proj(153.16, 153.21, -27.49, -27.445)
    feat = ["Lota"]
    labs = {n: P(*centroid(n)) for n in feat + ["Manly", "Manly West", "Ransome", "Wakerley"]}
    parts = basemap(P, feat, labs)
    x, y = P(*pt("st_lota")); parts.append(pin(x, y, "Lota station", INK, 8, "left", 19))
    x, y = P(*pt("lota_ss")); parts.append(school(x, y, "Lota State School", "state", "right"))
    x, y = P(*pt("lota_creek")); parts.append(label(x, y, "Lota Creek", 18, 500, "#7D8B93", "middle", italic=True))
    parts += frame(P, "Lota")
    return svg(parts)
MAPS["lota-the-quiet-one-between-wynnum-and-manly"] = m_lota

def m_wakerley():
    P = Proj(153.12, 153.20, -27.51, -27.44)
    feat = ["Wakerley", "Gumdale"]
    labs = {n: P(*centroid(n)) for n in feat + ["Manly West", "Manly", "Lota", "Ransome", "Tingalpa", "Wynnum West", "Belmont", "Chandler", "Capalaba"]}
    shift(labs, "Gumdale", -120, 70); shift(labs, "Wakerley", 0, -20)
    parts = basemap(P, feat, labs)
    for k, t in [("gumdale_ss", "Gumdale State School"), ("manly_west_ss", "Manly West State School"), ("wondall", "Wondall Heights SS"), ("bbsc", "Brisbane Bayside State College")]:
        x, y = P(*pt(k)); parts.append(school(x, y, t, "state", "right"))
    for k, t in [("mbc", "Moreton Bay College"), ("mbbc", "Moreton Bay Boys' College")]:
        x, y = P(*pt(k)); parts.append(school(x, y, t, "indep", "right"))
    parts += frame(P, "Wakerley and Gumdale - no station, no state school inside Wakerley")
    return svg(parts)
MAPS["wakerley-and-gumdale-the-newer-bayside"] = m_wakerley

def m_schools():
    P = Proj(153.135, 153.205, -27.50, -27.425)
    feat = []
    labs = {n: P(*centroid(n)) for n in ["Wynnum", "Manly", "Lota", "Manly West", "Wynnum West", "Wakerley", "Gumdale", "Ransome", "Hemmant", "Tingalpa"]}
    parts = basemap(P, feat, labs)
    S = [("wynnum_ss", "Wynnum State School", "state", "right"), ("wynnum_shs", "Wynnum State High", "state", "right"), ("bbsc", "Brisbane Bayside State College", "state", "left"),
         ("manly_ss", "Manly State School", "state", "right"), ("lota_ss", "Lota State School", "state", "right"), ("manly_west_ss", "Manly West SS", "state", "above"),
         ("wondall", "Wondall Heights SS", "state", "right"), ("wynnum_west_ss", "Wynnum West SS", "state", "left"), ("gumdale_ss", "Gumdale State School", "state", "right"),
         ("iona", "Iona College", "indep", "right"), ("mbc", "Moreton Bay College", "indep", "left"), ("mbbc", "Moreton Bay Boys' College", "indep", "below")]
    for k, t, kind, side in S:
        x, y = P(*pt(k)); parts.append(school(x, y, t, kind, side))
    # legend
    parts += [f'<rect x="60" y="60" width="330" height="86" rx="8" fill="{WHITE}" stroke="{LINE}"/>',
              f'<rect x="80" y="80" width="16" height="16" fill="{INK}"/>', label(108, 94, "State school", 18, 500, INK2, "start"),
              f'<rect x="80" y="114" width="16" height="16" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>', label(108, 128, "Independent school", 18, 500, INK2, "start")]
    parts += frame(P, "School locations only - catchments are on EdMap")
    return svg(parts)
MAPS["schools-on-the-bayside-catchments"] = m_schools

def m_wynnum():
    P = Proj(153.14, 153.20, -27.47, -27.415)
    feat = ["Wynnum"]
    labs = {n: P(*centroid(n)) for n in feat + ["Manly", "Wynnum West", "Manly West", "Lytton", "Hemmant"]}
    parts = basemap(P, feat, labs)
    for n, ll in STATIONS:
        if n in ("Wynnum North", "Wynnum", "Wynnum Central"):
            x, y = P(*ll); parts.append(pin(x, y, n + " station", INK, 7, "left", 17))
    x, y = P(*pt("wading")); parts.append(pin(x, y, "Jetty, wading pool, Pandanus Beach", INK, 9, "right", 19))
    x, y = P(*pt("wynnum_shs")); parts.append(school(x, y, "Wynnum State High", "state", "left"))
    x, y = P(*pt("wynnum_ss")); parts.append(school(x, y, "Wynnum State School", "state", "below"))
    x, y = P(*pt("elanora")); parts.append(pin(x, y, "Elanora Park", INK, 7, "right", 17))
    x, y = P(*pt("memorial")); parts.append(pin(x, y, "Memorial Park", INK, 7, "left", 17))
    parts += frame(P, "Wynnum")
    return svg(parts)
MAPS["is-wynnum-a-good-place-to-live"] = m_wynnum

def m_kids():
    P = Proj(153.16, 153.205, -27.465, -27.43)
    feat = []
    labs = {n: P(*centroid(n)) for n in ["Wynnum", "Manly", "Lota", "Manly West"]}
    parts = basemap(P, feat, labs)
    x, y = P(*pt("wading")); parts.append(pin(x, y, "Wading pool, jetty & Pandanus Beach", INK, 10, "right", 20, 600))
    x, y = P(*pt("eastwood")); parts.append(pin(x, y, "Eastwood Beach & Darling Point", INK, 8, "right", 18))
    x, y = P(*pt("cambridge")); parts.append(pin(x, y, "Cambridge Parade village", INK, 8, "left", 18))
    x, y = P(*pt("harbour")); parts.append(pin(x, y, "Manly Boat Harbour", INK, 9, "below", 19))
    x, y = P(*pt("elanora")); parts.append(pin(x, y, "Elanora Park", INK, 7, "right", 17))
    for n, ll in STATIONS:
        if n in ("Wynnum Central", "Manly", "Wynnum"):
            x, y = P(*ll); parts.append(pin(x, y, n + " station", INK2, 6, "left", 16))
    # foreshore path hint: label along the coast
    parts.append(label(*P(153.192, -27.436), "Foreshore path", 18, 500, "#7D8B93", "middle", italic=True))
    parts += frame(P, "The Wynnum-Manly foreshore")
    return svg(parts)
MAPS["what-to-do-in-wynnum-and-manly-with-kids"] = m_kids

def m_wynnum_manly():
    P = Proj(153.14, 153.205, -27.475, -27.415)
    feat = ["Wynnum", "Manly"]
    labs = {n: P(*centroid(n)) for n in feat + ["Lota", "Wynnum West", "Manly West", "Lytton", "Hemmant"]}
    parts = basemap(P, feat, labs)
    for n, ll in STATIONS:
        if n in ("Wynnum North", "Wynnum", "Wynnum Central", "Manly"):
            x, y = P(*ll); parts.append(pin(x, y, n, INK, 7, "right" if n == "Manly" else "left", 17))
    for k, t, side in [("wynnum_shs", "Wynnum State High", "left"), ("manly_ss", "Manly State School", "right"), ("wynnum_ss", "Wynnum State School", "left")]:
        x, y = P(*pt(k)); parts.append(school(x, y, t, "state", side))
    x, y = P(*pt("harbour")); parts.append(pin(x, y, "Boat harbour", INK, 8, "below", 18))
    x, y = P(*pt("wading")); parts.append(pin(x, y, "Wading pool & jetty", INK, 8, "right", 18))
    parts += frame(P, "Wynnum and Manly")
    return svg(parts)
MAPS["rebuilding-in-wynnum-or-manly"] = m_wynnum_manly

# ------------------------------------------------------------------ diagrams (not geographic)
def d_commute():
    parts = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    stops = [("Central", "12:17", True), ("Roma Street", "12:20", False), ("South Bank", "12:27", False), ("Coorparoo", "12:34", False),
             ("Cannon Hill", "12:42", False), ("Hemmant", "12:49", False), ("Lindum", "12:51", False), ("Wynnum North", "12:54", False),
             ("Wynnum", "12:55", False), ("Wynnum Central", "12:57", True), ("Manly", "1:00", True), ("Lota", "1:03", True)]
    x0, x1, y = 140, W - 140, 520
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    n = len(stops)
    for i, (name, t, big) in enumerate(stops):
        x = x0 + (x1 - x0) * i / (n - 1)
        r = 14 if big else 9
        parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{WHITE if not big else INK}" stroke="{INK}" stroke-width="4"/>')
        up = i % 2 == 0
        ty = y - 60 if up else y + 80
        parts.append(f'<line x1="{x:.1f}" y1="{y - r - 4 if up else y + r + 4}" x2="{x:.1f}" y2="{ty + 14 if up else ty - 34}" stroke="{LINE}" stroke-width="2"/>')
        parts.append(label(x, ty, name, 24 if big else 20, 600 if big else 500, INK if big else INK2))
        parts.append(label(x, ty + 30, t + " pm", 20 if big else 17, 500, MUTED))
    # brackets: minutes
    parts.append(label(W / 2, 150, "Central to Wynnum Central: 40 minutes. Manly 43. Lota 46.", 40, 600, INK))
    parts.append(label(W / 2, 200, "One all-stops midday service, Translink Cleveland line timetable, read 17 September 2026", 20, 400, MUTED))
    parts.append(label(W / 2, H - 140, "22.44 km by rail from Central to Wynnum Central \u00b7 19.6 km by road from the GPO \u00b7 Translink Zone 2", 22, 500, INK2))
    parts.append(label(W - 60, H - 40, "Schematic, not to scale. Your service will differ - check Translink.", 15, 400, MUTED, "end"))
    return svg(parts)
MAPS["how-far-is-wynnum-from-brisbane-cbd"] = d_commute

def d_flood_kinds():
    parts = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    # ground profile: bay (left) -> esplanade -> creek dip -> ridge (right)
    g = "M0,700 L260,700 L300,690 L520,680 L640,672 L720,700 L800,700 L860,670 L1100,600 L1400,520 L1600,500 L1600,1067 L0,1067 Z"
    parts.append(f'<path d="M0,700 L1600,700 L1600,1067 L0,1067 Z" fill="{WATER}"/>')  # bay under everything left
    parts.append(f'<path d="{g}" fill="{TINT}" stroke="{INK}" stroke-width="3"/>')
    parts.append(f'<rect x="0" y="700" width="260" height="367" fill="{WATER}"/>')
    parts.append(label(120, 760, "Moreton Bay", 22, 500, "#7D8B93", "middle", italic=True))
    # storm tide arrow
    parts += [f'<path d="M60,650 Q160,610 300,650" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#a)"/>',
              label(180, 590, "1  Storm tide", 26, 600, INK), label(180, 622, "the bay pushed up by a storm on a high tide", 18, 400, INK2)]
    # creek
    parts += [f'<path d="M760,560 L760,700" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#a)"/>',
              label(760, 500, "2  Creek", 26, 600, INK), label(760, 532, "backs up when the tide is high and the rain is heavy", 18, 400, INK2)]
    # overland flow
    parts += [f'<path d="M1500,470 L1150,560" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#a)"/>',
              label(1330, 430, "3  Overland flow", 26, 600, INK), label(1330, 462, "rain running across land before it reaches a drain", 18, 400, INK2)]
    # river: not here
    parts += [label(1330, 900, "4  River", 26, 600, MUTED), label(1330, 932, "the Brisbane River is not Wynnum's flood source", 18, 400, MUTED)]
    # houses on the profile
    def house(x, y, hs=1.0):
        return (f'<g transform="translate({x},{y}) scale({hs})"><rect x="-40" y="-60" width="80" height="60" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
                f'<path d="M-50,-60 L0,-100 L50,-60 Z" fill="{WHITE}" stroke="{INK}" stroke-width="3"/></g>')
    parts += [house(420, 682), house(600, 674), house(1000, 626), house(1250, 560)]
    parts.append(label(W / 2, 110, "Where Wynnum's water comes from", 40, 600, INK))
    parts.append(label(W / 2, 156, "Four sources Brisbane City Council maps for every lot. Wynnum is on the bay, not the river.", 20, 400, MUTED))
    parts.append(label(W - 60, H - 40, "Schematic section, not a flood map. Read the FloodWise report for your lot.", 15, 400, MUTED, "end"))
    defs = f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>'
    return svg([defs] + parts)
MAPS["does-wynnum-flood"] = d_flood_kinds

def d_floor_level():
    parts = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    gy = 820
    parts.append(f'<rect x="0" y="{gy}" width="{W}" height="{H-gy}" fill="{TINT}"/>')
    parts.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="{INK}" stroke-width="3"/>')
    # flood level line
    fl = 690
    parts.append(f'<line x1="0" y1="{fl}" x2="{W}" y2="{fl}" stroke="#7D8B93" stroke-width="3" stroke-dasharray="14 10"/>')
    parts.append(label(60, fl - 14, "Flood level in the FloodWise report", 18, 500, "#7D8B93", "start", italic=True))
    # habitable floor line
    hf = 600
    parts.append(f'<line x1="0" y1="{hf}" x2="{W}" y2="{hf}" stroke="{INK}" stroke-width="3"/>')
    parts.append(label(60, hf - 14, "Minimum habitable floor level - bedrooms and living above this", 20, 600, INK, "start"))
    # left: old lowset on slab, below the line
    x = 560
    parts += [f'<rect x="{x-170}" y="{gy-130}" width="340" height="130" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>',
              f'<path d="M{x-190},{gy-130} L{x},{gy-230} L{x+190},{gy-130} Z" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>',
              label(x, gy + 50, "1960s lowset on a ground-level slab", 22, 600, INK), label(x, gy + 82, "living areas sit below today's level", 18, 400, INK2)]
    # right: new highset designed to the level
    x = 1150
    parts += [f'<rect x="{x-190}" y="{hf}" width="380" height="{gy-hf}" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-dasharray="8 6"/>',
              label(x, (hf + gy) / 2 + 8, "garage \u00b7 laundry \u00b7 storage - built to be hosed out", 18, 400, INK2),
              f'<rect x="{x-190}" y="{hf-170}" width="380" height="170" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>',
              f'<path d="M{x-210},{hf-170} L{x},{hf-280} L{x+210},{hf-170} Z" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>',
              label(x, hf - 80, "the family lives up here", 20, 600, INK),
              label(x, gy + 50, "A new house designed to the level", 22, 600, INK), label(x, gy + 82, "the report is a design input, like the slope or the soil", 18, 400, INK2)]
    parts.append(label(W / 2, 110, "What a flood overlay does to a house", 40, 600, INK))
    parts.append(label(W / 2, 156, "It usually changes the design, not the answer", 20, 400, MUTED))
    parts.append(label(W - 60, H - 40, "Schematic, not to scale. Levels come from Brisbane City Council's FloodWise report for the lot.", 15, 400, MUTED, "end"))
    return svg(parts)
MAPS["rebuilding-on-a-flood-overlay-block-on-the-bayside"] = d_floor_level

def d_three_dates():
    parts = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    y = 560; x0, x1 = 160, W - 160
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    marks = [(0.18, "Before 1911", "council's position: the house is kept", INK),
             (0.50, "1946 or earlier", "in the overlay: a development application, council decides", INK),
             (0.82, "After 1946", "the character rules almost certainly don't stop you", INK)]
    for f, big, small, col in marks:
        x = x0 + (x1 - x0) * f
        parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="16" fill="{INK}" stroke="{WHITE}" stroke-width="4"/>')
        parts.append(label(x, y - 60, big, 48, 600, INK))
        for i, line in enumerate(wrap(small, 26)):
            parts.append(label(x, y + 80 + i * 36, line, 26, 400, INK2))
    parts.append(label(x0 + (x1 - x0) * 0.5, y - 170, "The overlay is mapped street by street. Check your own block.", 26, 500, MUTED))
    parts.append(label(W / 2, 170, "Can we knock it down? Three dates decide it.", 50, 600, INK))
    parts.append(label(W - 60, H - 40, "Brisbane City Council, Traditional building character overlay, Brisbane City Plan 2014", 15, 400, MUTED, "end"))
    return svg(parts)
MAPS["can-we-knock-down-our-house"] = d_three_dates

def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines

def d_two_checks():
    parts = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    # card 1: map tile with a street, one side shaded
    cx, cy, cw, ch = 120, 250, 620, 560
    parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>')
    # mini street grid
    for i in range(5):
        yy = cy + 90 + i * 95
        parts.append(f'<line x1="{cx+40}" y1="{yy}" x2="{cx+cw-40}" y2="{yy}" stroke="{LINE}" stroke-width="10"/>')
    for i in range(4):
        xx = cx + 90 + i * 150
        parts.append(f'<line x1="{xx}" y1="{cy+50}" x2="{xx}" y2="{cy+ch-50}" stroke="{LINE}" stroke-width="10"/>')
    # overlay hatch on one side of one street
    parts.append(f'<rect x="{cx+95}" y="{cy+190}" width="{cw-190}" height="80" fill="{TINT}" stroke="{INK}" stroke-width="3" stroke-dasharray="8 6"/>')
    parts.append(label(cx + cw / 2, cy + 240, "one side of the street can be in it, the other not", 17, 400, INK2))
    parts.append(label(cx + cw / 2, cy - 40, "Check one: the street", 30, 600, INK))
    parts.append(label(cx + cw / 2, cy + ch + 50, "Council's City Plan mapping \u2192 Overlays \u2192 Traditional building character", 19, 400, INK2))
    # card 2: archive register card
    cx2 = 860
    parts.append(f'<rect x="{cx2}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>')
    for i in range(7):
        yy = cy + 90 + i * 62
        parts.append(f'<line x1="{cx2+50}" y1="{yy}" x2="{cx2+cw-50}" y2="{yy}" stroke="{LINE}" stroke-width="2"/>')
    parts.append(label(cx2 + 60, cy + 70, "BUILDING APPLICATION REGISTER", 16, 600, MUTED, "start", tracking=2))
    parts.append(label(cx2 + 60, cy + 250, "Year built:", 26, 500, INK2, "start"))
    parts.append(label(cx2 + 60, cy + 320, "1946 or earlier?", 40, 600, INK, "start"))
    parts.append(label(cx2 + cw / 2, cy - 40, "Check two: the year", 30, 600, INK))
    parts.append(label(cx2 + cw / 2, cy + ch + 50, "Brisbane City Archives, registers from 1904 and property cards from 1945", 19, 400, INK2))
    parts.append(label(W / 2, 130, "Two free checks. About fifteen minutes.", 42, 600, INK))
    parts.append(label(W - 60, H - 40, "Illustration of the two checks, not a real map or record.", 15, 400, MUTED, "end"))
    return svg(parts)
MAPS["check-if-your-street-is-in-the-character-overlay"] = d_two_checks

# ------------------------------------------------------------------ render
def render(key, s):
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = HERE.parent / "shots"; tmp.mkdir(exist_ok=True)
    h = tmp / f"map-{key}.html"
    h.write_text('<!doctype html><html><head><meta charset="utf-8"><link rel="preconnect" href="https://fonts.googleapis.com">'
                 '<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">'
                 f'<style>html,body{{margin:0;background:{PAPER}}}svg{{display:block}}</style></head><body>' + s + '</body></html>', encoding="utf-8")
    out = OUT / f"{key}.png"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}", "--virtual-time-budget=6000",
                    f"--screenshot={out}", h.resolve().as_uri()], capture_output=True, timeout=120)
    print("wrote", out.name, out.stat().st_size if out.exists() else "MISSING")

if __name__ == "__main__":
    keys = [k for k in MAPS if len(sys.argv) < 2 or sys.argv[1] in k]
    for k in keys:
        render(k, MAPS[k]())
