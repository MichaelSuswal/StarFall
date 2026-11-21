#!/usr/bin/env python3
"""StarFall map tool, painted-map edition. Needs Pillow. Rules: engine/rules/map.md.

  python3 tools/map.py draw <campaign> [--zoom known|landing] [--layer surface|under-N]
  python3 tools/map.py gazetteer <campaign>
  python3 tools/map.py stamp <campaign> [--dry-run]    append [id] after every map name in the sealed .md files
  python3 tools/map.py describe <campaign> (--landing <god> | --region <id> [--god <god>]) [--names]
  python3 tools/map.py reveal <campaign> (--region R | --feature F) --grade G --source "..." --year N
                                        [--told '<json>'] [--name N] [--cell C3] [--force "reason"]
  python3 tools/map.py validate <campaign>     check the sealed map's ids, neighbors, landings and types
  python3 tools/map.py migrate <campaign>      rewrite an older knowledge file to the current rules

<campaign> is a campaign name under campaigns/. The sealed world is read from
SPOILERS_do_not_open/campaigns/<name>/map.json and its paintings from
SPOILERS_do_not_open/campaigns/<name>/map/ (surface.png, under-N.png, clouds.png);
the player's knowledge from campaigns/<name>/player/map-knowledge.json. Outputs go to
campaigns/<name>/player/ (map.png, map-under-N.png, gazetteer.md, map-meta.json).
For tests and examples the paths can be given directly with --world, --paintings,
--knowledge and --out.

The sealed map data is in painting pixel coordinates: x grows rightward, y grows
downward, 0 to the painting's size. The paintings never change; the tool traces the
record onto them and fogs what the god does not know with the cloud painting. It
prints nothing from the sealed file that the knowledge file does not allow. Unknown
ground is cloud, unnamed and unhinted.

The sheet is one letter-number grid, painting.grid {"cols": 5, "rows": 4} by default,
lettered on all four edges; miles_per_pixel is free (a continent on one sheet). Underground layers are separate sheets on the
same grid and fog.

Ids in map.json are opaque (r01 for regions, f03 for features, u01 underground),
never name slugs. The player's knowledge file is keyed by those ids, in a `regions`
dict and a `features` dict, each entry with grade, source, year and told:
  - seen: no told and no coordinates; the truth is drawn from the sealed map.
  - reported: told may carry name, type, terrain and shapes (coords, polygon) in
    painting pixels, because it is the god's belief, not the truth.
  - rumored: told.name and told.cell (a grid cell like "C2"), never `near` or any
    pixel; the faint label is drawn at the cell's center. Regions and features may
    both be rumored; a rumored region carries no pixel either.
Files written before these rules (rumors with `near`, a grid_cell_px grid) are still
drawn; `migrate` rewrites them.

Zoom: `known` crops to the seen and reported ground; `landing` crops to the seen regions plus a
quarter margin, at its own scale bar, with the full sheet's grid letters. On every sheet labels are
laid down by priority and never overprint one another, a settlement mark, the compass or the scale
bar: a label that would collide moves to the nearest free spot (with a faint leader line back to a
point or line it names), then loses its small lines, then shrinks; one that still cannot fit is left
off and named on the command line and counted in map-meta.json (the gazetteer still lists it).

`stamp` appends the bracketed id after every map name (with or without a leading "The", capitalized,
four letters or more) in every .md file of the sealed campaign folder, the rule lockcheck --places
warns by. A name already followed by one of its ids (after any 's or a parenthesis) is left alone, so
running it twice changes nothing. It skips LOCKED.md and the checker's lock-flags*.md, never touches
the public folder, and prints the count per file.

`describe` writes a land description from the sealed data, for the Keeper's use: the region's terrain,
elevation, water, climate and extent; its neighbors with travel days and directions; and what is in
view from the landing point (or the region's middle) by the sight rule in describe()'s docstring. Names
come from the god's knowledge file (the player's public file, or S/gods/<god>/map-knowledge.json);
anything the god has not learned is put plainly ("a river", "a hill country"), free text included.
--names gives every true name.

Coordinates may be whole pixels or tenths (one decimal) or finer; validate fails any that is not a
pair of numbers or lies off the painting.

The sealed map's regions carry elevation, water, climate and neighbors ({id, days});
the sheet carries landings (god label to region id), roads (a feature type, drawn as
a thin line) and a plane section, which the drawer ignores.
"""
import argparse
import datetime
import subprocess
import json
import math
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("map.py: Pillow is required (pip install Pillow)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GRADES = ["none", "rumored", "reported", "seen"]
SETTLEMENT_TYPES = {"town", "city", "village"}
POINT_TYPES = SETTLEMENT_TYPES | {"ruin", "cave", "pass"}
NATURAL_TYPES = {"river", "lake", "sea", "mountain", "pass", "forest", "marsh", "ruin", "cave"}
FEATURE_TYPES = SETTLEMENT_TYPES | NATURAL_TYPES | {"road"}
WATER_TYPES = {"river", "lake", "sea"}
DEFAULT_GRID = (5, 4)   # columns, rows
CELL_RE = re.compile(r"^([A-Z]+)([0-9]+)$")
OPAQUE_RE = re.compile(r"^[a-z][0-9]{2,4}$")
TOLD_KEYS = {"name", "terrain", "type", "cell", "coords", "polygon"}
PIXEL_KEYS = {"coords", "polygon", "near"}
# A rumored region ("the grey wall beyond the hills") is allowed, with told.name and
# told.cell only, never a pixel. Set False to admit region ids only when seen or reported.
RUMORED_REGIONS_ALLOWED = True

# Ink and paper.
PARCHMENT = (239, 227, 196)
PARCHMENT_EDGE = (217, 195, 150)
INK = (90, 58, 28)
INK_LIGHT = (138, 104, 66)
INK_FAINT = (168, 144, 106)
WATER_INK = (70, 86, 102)
ROAD_INK = (112, 78, 44)

# Label priority when labels would collide: higher keeps its place, lower moves or is dropped.
PRIORITY = {"region": 90, "city": 88, "town": 84, "region-reported": 72, "village": 70,
            "sea": 62, "mountain": 62, "river": 58, "lake": 58, "pass": 56, "forest": 54, "marsh": 54,
            "ruin": 52, "cave": 52, "road": 46, "rumored": 30}

REPORTED_BLEND = 0.45   # how much of the painting shows through on reported ground
FEATHER_PX = 5          # blur radius on the fog masks, in painting pixels
DEFAULT_MPP = 2.5       # miles per painting pixel when map.json does not say (a continent; validate fails a missing scale)


def pacific_today():
    """Today's date in America/Los_Angeles, the date every logged real time uses."""
    now = datetime.datetime.now(datetime.timezone.utc)
    try:
        from zoneinfo import ZoneInfo
        return now.astimezone(ZoneInfo("America/Los_Angeles")).date().isoformat()
    except Exception:
        out = subprocess.run(["date", "+%Y-%m-%d"], env={**os.environ, "TZ": "America/Los_Angeles"},
                             capture_output=True, text=True)
        return out.stdout.strip() or now.date().isoformat()


# ---------------------------------------------------------------- paths

def campaign_paths(args):
    """Resolve the world, paintings, knowledge and output paths."""
    name = args.campaign
    sealed = os.path.join(ROOT, "SPOILERS_do_not_open", "campaigns", name)
    world = args.world or os.path.join(sealed, "map.json")
    paintings = getattr(args, "paintings", None) or os.path.join(os.path.dirname(world), "map")
    player = os.path.join(ROOT, "campaigns", name, "player")
    knowledge = args.knowledge or os.path.join(player, "map-knowledge.json")
    out = args.out or player
    return world, paintings, knowledge, out


def load_json(path, default=None):
    if not os.path.exists(path):
        if default is not None:
            return default
        sys.exit(f"map.py: missing {path}")
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


# ---------------------------------------------------------------- geometry

def centroid(poly):
    n = len(poly)
    if n == 1:
        return tuple(poly[0])
    if n == 2:
        return ((poly[0][0] + poly[1][0]) / 2, (poly[0][1] + poly[1][1]) / 2)
    a = cx = cy = 0.0
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % n]
        cross = x0 * y1 - x1 * y0
        a += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    if abs(a) < 1e-9:
        return (sum(p[0] for p in poly) / n, sum(p[1] for p in poly) / n)
    a *= 0.5
    return (cx / (6 * a), cy / (6 * a))


def bbox(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi:
            inside = not inside
        j = i
    return inside


def polyline_length(points):
    return sum(math.dist(points[i], points[i + 1]) for i in range(len(points) - 1))


def extent_across(poly):
    x0, y0, x1, y1 = bbox(poly)
    return max(x1 - x0, y1 - y0)


def bearing_name(dx, dy):
    """dy grows downward (south) in painting coordinates."""
    ang = math.degrees(math.atan2(dx, -dy)) % 360
    names = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]
    return names[int((ang + 22.5) // 45) % 8]


def dist_to_polyline(p, line):
    """Shortest distance from p to the polyline, and the distance along the line to that foot."""
    best = (float("inf"), 0.0)
    run = 0.0
    for i in range(len(line) - 1):
        a, b = line[i], line[i + 1]
        ab = (b[0] - a[0], b[1] - a[1])
        L2 = ab[0] ** 2 + ab[1] ** 2
        t = 0 if L2 == 0 else max(0, min(1, ((p[0] - a[0]) * ab[0] + (p[1] - a[1]) * ab[1]) / L2))
        foot = (a[0] + ab[0] * t, a[1] + ab[1] * t)
        d = math.dist(p, foot)
        if d < best[0]:
            best = (d, run + math.sqrt(L2) * t)
        run += math.sqrt(L2)
    return best


# ---------------------------------------------------------------- the painting's frame

class Painting:
    """Size, scale and grid of the sealed paintings, from map.json's painting block.
    The grid is painting.grid {"cols", "rows"} (default 5 by 4). An older map that gives
    only grid_cell_px keeps its square cells."""

    def __init__(self, world):
        p = world.get("painting", {})
        self.size = tuple(p.get("size", [1024, 1024]))
        self.mpp = float(p.get("miles_per_pixel", DEFAULT_MPP))
        g = p.get("grid")
        if isinstance(g, dict):
            self.ncols, self.nrows = int(g.get("cols", DEFAULT_GRID[0])), int(g.get("rows", DEFAULT_GRID[1]))
        elif isinstance(g, (list, tuple)):
            self.ncols, self.nrows = int(g[0]), int(g[1])
        elif "grid_cell_px" in p:
            c = int(p["grid_cell_px"])
            self.ncols, self.nrows = math.ceil(self.size[0] / c), math.ceil(self.size[1] / c)
        else:
            self.ncols, self.nrows = DEFAULT_GRID
        self.cw = self.size[0] / self.ncols
        self.ch = self.size[1] / self.nrows
        self.folder = None

    def cols(self):
        return self.ncols

    def rows(self):
        return self.nrows

    def cell_of(self, p):
        c = int(max(0, min(p[0], self.size[0] - 1)) // self.cw)
        r = int(max(0, min(p[1], self.size[1] - 1)) // self.ch) + 1
        return f"{col_letters(min(c, self.ncols - 1))}{min(r, self.nrows)}"

    def parse_cell(self, cell):
        """(column index, row index) of a cell like D3, or None if it is not on this grid."""
        m = CELL_RE.match(str(cell).strip().upper())
        if not m:
            return None
        c = 0
        for ch in m.group(1):
            c = c * 26 + (ord(ch) - ord("A") + 1)
        c -= 1
        r = int(m.group(2)) - 1
        if not (0 <= c < self.ncols and 0 <= r < self.nrows):
            return None
        return c, r

    def cell_center(self, cell):
        cr = self.parse_cell(cell)
        if cr is None:
            return None
        return ((cr[0] + 0.5) * self.cw, (cr[1] + 0.5) * self.ch)

    def cells(self):
        return [f"{col_letters(c)}{r + 1}" for r in range(self.nrows) for c in range(self.ncols)]

    def miles(self, px):
        return px * self.mpp


def col_letters(i):
    s = ""
    i = int(i)
    while True:
        s = chr(ord("A") + i % 26) + s
        i = i // 26 - 1
        if i < 0:
            return s


# ---------------------------------------------------------------- knowledge

def grade_of(entry):
    return entry.get("grade", "none") if entry else "none"


def grade_rank(g):
    return GRADES.index(g) if g in GRADES else 0


def all_features(world):
    """Yield (feature, layer) for surface and underground features."""
    for f in world.get("features", []):
        yield f, None
    for layer in world.get("layers", []):
        for f in layer.get("features", []):
            yield f, layer


def rumor_near(told, el, painting):
    """Where a rumor's faint label sits: the center of told.cell; an older file's `near`;
    else the center of the cell the thing is truly in."""
    if painting is not None and told.get("cell"):
        c = painting.cell_center(told["cell"])
        if c:
            return list(c)
    if "near" in told:
        return told["near"]
    true = centroid(el.get("polygon") or el["coords"])
    return list(painting.cell_center(painting.cell_of(true))) if painting is not None else list(true)


def known_feature(f, entry, painting=None):
    """The feature as the god knows it: told values override truth below seen."""
    g = grade_of(entry)
    k = {"id": f["id"], "type": f["type"], "shape": f.get("shape", "point"), "grade": g,
         "source": entry.get("source", ""), "year": entry.get("year", ""), "regions": f.get("regions", [])}
    told = entry.get("told", {}) if g != "seen" else {}
    k["name"] = told.get("name", f["name"])
    k["type"] = told.get("type", f["type"] if g != "rumored" else "")
    if g == "seen":
        k["coords"] = f["coords"]
    elif g == "reported":
        k["coords"] = told.get("coords", f["coords"])
    else:
        k["coords"] = [rumor_near(told, f, painting)]
    k["shape"] = f.get("shape", "point") if g != "rumored" else "point"
    if k["shape"] == "line" and len(k["coords"]) < 2:
        k["shape"] = "point"
    if k["shape"] == "area" and len(k["coords"]) < 3:
        k["shape"] = "point"
    return k


def known_region(r, entry, painting=None):
    g = grade_of(entry)
    told = entry.get("told", {}) if g != "seen" else {}
    k = {"id": r["id"], "grade": g, "source": entry.get("source", ""), "year": entry.get("year", ""),
         "name": told.get("name", r["name"]), "terrain": told.get("terrain", r.get("terrain", ""))}
    if g == "rumored":
        k["polygon"] = None
        k["near"] = rumor_near(told, r, painting)
    else:
        k["polygon"] = told.get("polygon", r["polygon"])
    return k


def gather(world, knowledge, painting=None):
    """Known regions (by id) and known features (id -> (known, layer id or None))."""
    regions_k = {}
    for r, _layer in all_regions(world):
        e = knowledge["regions"].get(r["id"])
        if grade_of(e) != "none":
            regions_k[r["id"]] = known_region(r, e, painting)
    features_k = {}
    for f, layer in all_features(world):
        e = knowledge["features"].get(f["id"])
        if grade_of(e) != "none":
            features_k[f["id"]] = (known_feature(f, e, painting), layer["id"] if layer else None)
    return regions_k, features_k


def all_regions(world):
    """Yield (region, layer) for surface and underground regions."""
    for r in world.get("regions", []):
        yield r, None
    for layer in world.get("layers", []):
        for r in layer.get("regions", []):
            yield r, layer


def index_world(world):
    """id -> (kind, element, layer)."""
    by_id = {}
    for r, layer in all_regions(world):
        by_id[r["id"]] = ("region", r, layer)
    for f, layer in all_features(world):
        by_id[f["id"]] = ("feature", f, layer)
    return by_id


def knowledge_problems(world, knowledge):
    """Breaches of the knowledge file's rules (ids, pixels, region ids below reported)."""
    by_id = index_world(world)
    probs = []
    for table, kind in (("regions", "region"), ("features", "feature")):
        for ident, e in knowledge.get(table, {}).items():
            hit = by_id.get(ident)
            g = grade_of(e)
            t = e.get("told") or {}
            if not hit or hit[0] != kind:
                probs.append(f"{kind} {ident}: not in the sealed map")
                continue
            if g not in GRADES[1:]:
                probs.append(f"{kind} {ident}: grade {g!r}")
            if not OPAQUE_RE.match(ident):
                probs.append(f"{kind} {ident}: id is not opaque")
            if kind == "region" and g not in ("seen", "reported") and not (RUMORED_REGIONS_ALLOWED and g == "rumored"):
                probs.append(f"{kind} {ident}: a region id appears only when seen or reported (grade {g})")
            if g == "seen" and t:
                probs.append(f"{kind} {ident}: seen entries carry no told")
            if g == "rumored":
                if PIXEL_KEYS & set(t):
                    probs.append(f"{kind} {ident}: a rumor carries a cell, never pixels")
                if not t.get("cell") or not t.get("name"):
                    probs.append(f"{kind} {ident}: a rumor needs told.name and told.cell")
                elif Painting(world).parse_cell(t["cell"]) is None:
                    probs.append(f"{kind} {ident}: rumor cell {t['cell']!r} is not on the grid")
            if g == "reported" and "near" in t:
                probs.append(f"{kind} {ident}: `near` is not a reported shape")
    return probs


def plane_ids(world):
    """Ids of every entry in the plane section, whatever lists it holds."""
    plane = world.get("plane") or {}
    out = []
    for v in (plane.values() if isinstance(plane, dict) else [plane]):
        if isinstance(v, list):
            out += [e.get("id") for e in v if isinstance(e, dict)]
    return out


def check_world(world):
    """Problems in the sealed map: duplicate or missing ids, unknown types, neighbors and landings
    that do not resolve. Returns a list of strings."""
    probs = []
    seen_ids = {}
    region_ids = set()
    if "miles_per_pixel" not in (world.get("painting") or {}):
        probs.append("painting: no miles_per_pixel")
    for el, layer in list(all_regions(world)) + list(all_features(world)):
        i = el.get("id")
        if not i:
            probs.append(f"an element with no id: {el.get('name', '?')}")
            continue
        if i in seen_ids:
            probs.append(f"duplicate id {i}")
        seen_ids[i] = el
        if not OPAQUE_RE.match(i):
            probs.append(f"id {i} is not opaque (use r01, f03, u01)")
    for r, _layer in all_regions(world):
        region_ids.add(r["id"])
        if len(r.get("polygon", [])) < 3:
            probs.append(f"region {r['id']}: polygon has fewer than 3 points")
        for field in ("elevation", "water", "climate", "neighbors"):
            if field not in r:
                probs.append(f"region {r['id']}: no {field}")
        for n in r.get("neighbors", []):
            nid = n.get("id") if isinstance(n, dict) else n
            if nid not in seen_ids:
                probs.append(f"region {r['id']}: neighbor {nid} is not in the map")
            if isinstance(n, dict) and not isinstance(n.get("days"), (int, float)) and not n.get("by"):
                probs.append(f"region {r['id']}: neighbor {nid} has no travel days")
    for f, _layer in all_features(world):
        if f.get("type") not in FEATURE_TYPES:
            probs.append(f"feature {f['id']}: unknown type {f.get('type')!r}")
        if f.get("type") == "road" and (f.get("shape") != "line" or len(f.get("coords", [])) < 2):
            probs.append(f"feature {f['id']}: a road is a line of two or more points")
        for rid in f.get("regions", []):
            if rid not in region_ids and rid not in seen_ids:
                probs.append(f"feature {f['id']}: region {rid} is not in the map")
    plane_seen = set()
    for pid in plane_ids(world):
        if not re.fullmatch(r"p[0-9]{2,4}", str(pid)):
            probs.append(f"plane id {pid} is not opaque (use p01)")
        if pid in plane_seen or pid in seen_ids:
            probs.append(f"duplicate id {pid} (plane)")
        plane_seen.add(pid)
    for god, land in (world.get("landings") or {}).items():
        rid = land.get("region") if isinstance(land, dict) else land
        if rid not in region_ids:
            probs.append(f"landing {god}: region {rid} is not in the map")
        at = landing_point(land)
        if at is not None and not is_point(at):
            probs.append(f"landing {god}: point {at!r} is not an [x, y] pair of numbers")
    size = (world.get("painting") or {}).get("size", [1024, 1024])
    for el, _layer in list(all_regions(world)) + list(all_features(world)):
        pts = el.get("polygon") if "polygon" in el else el.get("coords", [])
        bad = [p for p in (pts or []) if not is_point(p)]
        if bad:
            probs.append(f"{el.get('id', '?')}: coordinate {bad[0]!r} is not an [x, y] pair of numbers")
        elif any(not (-1 <= p[0] <= size[0] + 1 and -1 <= p[1] <= size[1] + 1) for p in pts or []):
            probs.append(f"{el.get('id', '?')}: a coordinate lies off the painting")
    return probs


def is_point(p):
    """An [x, y] pair of finite numbers; whole pixels or tenths (one decimal) alike, any precision accepted."""
    return (isinstance(p, (list, tuple)) and len(p) == 2
            and all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in p))


def landing_point(land):
    """The landing's point in painting pixels (`at`, or `point` in older files), or None."""
    if isinstance(land, dict):
        return land.get("at", land.get("point"))
    return None


# ---------------------------------------------------------------- fonts

_FONT_CACHE = {}
_FONT_FILES = None

FONT_CANDIDATES = {
    "regular": ["DejaVuSerif.ttf", "LiberationSerif-Regular.ttf", "FreeSerif.ttf", "NotoSerif-Regular.ttf"],
    "italic": ["DejaVuSerif-Italic.ttf", "LiberationSerif-Italic.ttf", "FreeSerifItalic.ttf", "NotoSerif-Italic.ttf"],
    "bold": ["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf", "FreeSerifBold.ttf", "NotoSerif-Bold.ttf"],
}


def find_font_files():
    global _FONT_FILES
    if _FONT_FILES is not None:
        return _FONT_FILES
    found = {}
    roots = ["/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts"),
             "/System/Library/Fonts", "/Library/Fonts", "C:\\Windows\\Fonts"]
    index = {}
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, _, files in os.walk(root):
            for fn in files:
                index.setdefault(fn, os.path.join(dirpath, fn))
    for style, names in FONT_CANDIDATES.items():
        for n in names:
            if n in index:
                found[style] = index[n]
                break
    _FONT_FILES = found
    return found


def font(size, style="regular"):
    key = (size, style)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    files = find_font_files()
    path = files.get(style) or files.get("regular")
    try:
        f = ImageFont.truetype(path, int(size)) if path else ImageFont.load_default(size=int(size))
    except (OSError, TypeError):
        f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


# ---------------------------------------------------------------- the view

class View:
    """Maps painting pixels to the output canvas: a crop rectangle scaled to size_px on its long side,
    with margins for the grid letters and a bottom strip for notes."""

    def __init__(self, rect, size_px=1024, margins=(56, 56, 56, 92)):
        self.x0, self.y0, self.x1, self.y1 = rect
        w = max(self.x1 - self.x0, 1)
        h = max(self.y1 - self.y0, 1)
        self.scale = size_px / max(w, h)
        self.iw, self.ih = max(1, round(w * self.scale)), max(1, round(h * self.scale))
        self.ml, self.mt, self.mr, self.mb = margins
        self.W = self.iw + self.ml + self.mr
        self.H = self.ih + self.mt + self.mb

    def pt(self, p):
        return (self.ml + (p[0] - self.x0) * self.scale, self.mt + (p[1] - self.y0) * self.scale)

    def pts(self, coords):
        return [self.pt(c) for c in coords]

    def inside(self, p):
        return self.x0 <= p[0] <= self.x1 and self.y0 <= p[1] <= self.y1

    def rect(self):
        return (self.ml, self.mt, self.ml + self.iw, self.mt + self.ih)


LEADER_MIN = 14   # sheet pixels: a label moved farther than this from what it names gets a leader line


class Labeler:
    """Collects labels on two layers, a parchment halo and the ink, and lays them down together.

    `text` draws at once (the grid's letters). `add` queues a label group (a name and its small
    lines beneath) with a priority; `place` then lays the groups down in priority order so that
    no two overprint and none covers a settlement mark, the compass or the scale bar: a group
    that would collide is shifted to the nearest free spot, then loses its small lines, then
    shrinks, and is dropped only when nothing fits (the drop is reported, never overprinted).
    """

    def __init__(self, size, bounds=None):
        self.halo = Image.new("RGBA", size, (0, 0, 0, 0))
        self.ink = Image.new("RGBA", size, (0, 0, 0, 0))
        self.dh = ImageDraw.Draw(self.halo)
        self.di = ImageDraw.Draw(self.ink)
        self.bounds = bounds or (0, 0, size[0], size[1])
        self.queue = []
        self.obstacles = []
        self.placed = []
        self.leaders = []
        self.groups = []
        self.dropped = []
        self.moved = 0

    def obstacle(self, box):
        """A box no label may cover (a settlement mark, the compass, the scale bar)."""
        self.obstacles.append(tuple(box))

    def add(self, xy, lines, priority=50, anchor="mm", marker=None, leader=False):
        """Queue a label group. lines: [(text, size, style, fill, alpha, dy)], the first the name.
        anchor "mm" centers the group on xy; "lm" sets it to the right of a marker at xy (and may
        move it to the left, above or below the marker)."""
        lines = [l for l in lines if l[0]]
        if lines:
            self.queue.append({"xy": xy, "lines": lines, "priority": priority, "anchor": anchor,
                               "order": len(self.queue), "marker": marker, "leader": leader})

    @staticmethod
    def _line_box(xy, s, size, style, anchor):
        f = font(size, style)
        try:
            b = f.getbbox(s, anchor=anchor)
        except (TypeError, ValueError):
            w, h = f.getlength(s), size
            dx = {"l": 0, "m": -w / 2, "r": -w}[anchor[0]]
            b = (dx, -h / 2, dx + w, h / 2)
        pad = max(2, size // 6) + 1
        return (xy[0] + b[0] - pad, xy[1] + b[1] - pad, xy[0] + b[2] + pad, xy[1] + b[3] + pad)

    def _layout(self, g, xy, anchor, lines, scale=1.0):
        """(boxes, draw ops) for a group set at xy with the given anchor."""
        ops, boxes = [], []
        for (s, size, style, fill, alpha, dy) in lines:
            sz = max(8, int(round(size * scale)))
            p = (xy[0], xy[1] + dy * scale)
            ops.append((p, s, sz, style, fill, alpha, anchor))
            boxes.append(self._line_box(p, s, sz, style, anchor))
        return boxes, ops

    @staticmethod
    def _hit(a, b):
        return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]

    def _free(self, boxes):
        l, t, r, b = self.bounds
        for bx in boxes:
            if bx[0] < l or bx[1] < t or bx[2] > r or bx[3] > b:
                return False
            if any(self._hit(bx, o) for o in self.obstacles) or any(self._hit(bx, o) for o in self.placed):
                return False
            if any(self._seg_hits(seg, bx) for seg in self.leaders):
                return False
        return True

    @staticmethod
    def _leader_seg(xy, boxes):
        b = boxes[0]
        return (tuple(xy), (min(max(xy[0], b[0]), b[2]), min(max(xy[1], b[1]), b[3])))

    @staticmethod
    def _seg_hits(seg, box, shrink=1.0):
        (x0, y0), (x1, y1) = seg
        n = max(2, int(math.dist(seg[0], seg[1]) // 2))
        for i in range(1, n):
            x, y = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            if box[0] + shrink < x < box[2] - shrink and box[1] + shrink < y < box[3] - shrink:
                return True
        return False

    def _leader_free(self, g, boxes):
        """A leader may not cross another label or a mark on its way to its own label."""
        seg = self._leader_seg(g["xy"], boxes)
        if math.dist(seg[0], seg[1]) <= LEADER_MIN:
            return True
        others = self.placed + [o for o in self.obstacles if not (o[0] <= g["xy"][0] <= o[2] and o[1] <= g["xy"][1] <= o[3])]
        return not any(self._seg_hits(seg, o) for o in others)

    def _candidates(self, g, lines, scale):
        x, y = g["xy"]
        boxes, _ = self._layout(g, (x, y), "mm" if g["anchor"] == "mm" else "lm", lines, scale)
        x0, y0, x1, y1 = bbox([(b[0], b[1]) for b in boxes] + [(b[2], b[3]) for b in boxes])
        w, h = x1 - x0, y1 - y0
        out = []
        if g["anchor"] == "lm":
            m = 10
            out += [((x + m, y), "lm"), ((x - m, y), "rm"), ((x, y - m - h / 2), "mm"), ((x, y + m + h / 2), "mm"),
                    ((x + m, y - h / 2 - 2), "lm"), ((x + m, y + h / 2 + 2), "lm"),
                    ((x - m, y - h / 2 - 2), "rm"), ((x - m, y + h / 2 + 2), "rm")]
            for k in (2, 3, 4):
                out += [((x + m, y - k * h * 0.6), "lm"), ((x + m, y + k * h * 0.6), "lm"),
                        ((x - m, y - k * h * 0.6), "rm"), ((x - m, y + k * h * 0.6), "rm")]
        else:
            out.append(((x, y), "mm"))
            for k in (1, 2, 3, 4, 5, 6):
                sy, sx = k * (h * 0.55 + 2), k * (w * 0.55 + 2)
                out += [((x, y - sy), "mm"), ((x, y + sy), "mm"), ((x + sx, y), "mm"), ((x - sx, y), "mm"),
                        ((x + sx, y - sy), "mm"), ((x - sx, y - sy), "mm"), ((x + sx, y + sy), "mm"), ((x - sx, y + sy), "mm")]
        return out

    def _leader(self, xy, boxes, fill):
        """A faint ink line from the thing named to its label, when the label had to move off it."""
        b = boxes[0]
        px = min(max(xy[0], b[0]), b[2])
        py = min(max(xy[1], b[1]), b[3])
        if math.dist(xy, (px, py)) > LEADER_MIN:
            self.leaders.append((tuple(xy), (px, py)))
            self.di.line([xy, (px, py)], fill=tuple(fill) + (150,), width=1)
            self.di.ellipse([xy[0] - 1.5, xy[1] - 1.5, xy[0] + 1.5, xy[1] + 1.5], fill=tuple(fill) + (170,))

    def place(self):
        """Lay down every queued group, highest priority first; returns the names dropped."""
        for g in sorted(self.queue, key=lambda g: (-g["priority"], g["order"])):
            tries = [(g["lines"], 1.0)]
            if len(g["lines"]) > 2:
                tries.append((g["lines"][:2], 1.0))
            if len(g["lines"]) > 1:
                tries.append((g["lines"][:1], 1.0))
            tries.append((g["lines"][:1], 0.8))
            done = False
            for lines, scale in tries:
                for i, (xy, anchor) in enumerate(self._candidates(g, lines, scale)):
                    boxes, ops = self._layout(g, xy, anchor, lines, scale)
                    if self._free(boxes) and (not (g["leader"] and i) or self._leader_free(g, boxes)):
                        if g["leader"] and i:
                            self._leader(g["xy"], boxes, lines[0][3])
                        for op in ops:
                            p, s_, sz, style, fill, alpha, anc = op
                            self.text(p, s_, size=sz, style=style, fill=fill, alpha=alpha, anchor=anc)
                        self.placed += boxes
                        self.groups.append(boxes)
                        if i or scale != 1.0 or len(lines) < len(g["lines"]):
                            self.moved += 1
                        done = True
                        break
                if done:
                    break
            if not done:
                self.dropped.append(g["lines"][0][0])
        self.queue = []
        return self.dropped

    def text(self, xy, s, size=14, style="regular", fill=INK, alpha=255, anchor="mm", halo=True):
        f = font(size, style)
        if halo:
            ha = int(min(255, 150 * alpha / 255 + 40))
            self.dh.text(xy, s, font=f, fill=PARCHMENT + (ha,), anchor=anchor,
                         stroke_width=max(2, size // 6), stroke_fill=PARCHMENT + (ha,))
        self.di.text(xy, s, font=f, fill=tuple(fill) + (int(alpha),), anchor=anchor)

    def width(self, s, size=14, style="regular"):
        return font(size, style).getlength(s)

    def flush(self, canvas):
        if self.queue:
            self.place()
        canvas.alpha_composite(self.halo.filter(ImageFilter.GaussianBlur(1.4)))
        canvas.alpha_composite(self.ink)


# ---------------------------------------------------------------- fog and paint

def load_painting(folder, name, size):
    path = os.path.join(folder, name)
    if not os.path.exists(path):
        sys.exit(f"map.py: missing painting {path}")
    im = Image.open(path).convert("RGB")
    if im.size != tuple(size):
        im = im.resize(tuple(size), Image.LANCZOS)
    return im


def fog_mask(regions, size):
    """An L mask of how much painting shows: 255 on seen ground, a part on reported, 0 elsewhere.
    Seen is drawn after reported so it wins where polygons overlap. Feathered so the fog looks painted."""
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    for k in regions:
        if k["grade"] == "reported" and k["polygon"]:
            d.polygon([tuple(p) for p in k["polygon"]], fill=int(255 * REPORTED_BLEND))
    for k in regions:
        if k["grade"] == "seen" and k["polygon"]:
            d.polygon([tuple(p) for p in k["polygon"]], fill=255)
    return m.filter(ImageFilter.GaussianBlur(FEATHER_PX))


def paint_ground(view, painting_im, clouds_im, mask):
    """The fogged painting, cropped to the view and scaled to its size."""
    box = (int(view.x0), int(view.y0), int(math.ceil(view.x1)), int(math.ceil(view.y1)))
    size = (view.iw, view.ih)
    p = painting_im.crop(box).resize(size, Image.LANCZOS)
    c = clouds_im.crop(box).resize(size, Image.LANCZOS)
    m = mask.crop(box).resize(size, Image.LANCZOS)
    return Image.composite(p, c, m).convert("RGBA")


# ---------------------------------------------------------------- drawing

def parchment_canvas(view):
    """A warm sheet, slightly darker toward the edges."""
    W, H = view.W, view.H
    base = Image.new("RGB", (W, H), PARCHMENT)
    edge = Image.new("RGB", (W, H), PARCHMENT_EDGE)
    grad = Image.radial_gradient("L").resize((W, H))
    grad = grad.point(lambda v: max(0, min(255, int((v - 140) * 2.2))))
    return Image.composite(edge, base, grad).convert("RGBA")


def draw_grid(canvas, view, painting):
    """Faint cell lines over the ground and the letters and numbers along all four edges.
    Letters and numbers name the full painting's cells, so a cropped sheet still reads against the whole."""
    over = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    lab = Labeler(canvas.size)
    cw, ch = painting.cw, painting.ch
    l, t, r, b = view.rect()
    c0, c1 = int(view.x0 // cw), min(painting.ncols, int(math.ceil(view.x1 / cw - 1e-9)))
    for c in range(c0, c1 + 1):
        x = c * cw
        if view.x0 < x < view.x1:
            vx = view.pt((x, 0))[0]
            d.line([(vx, t), (vx, b)], fill=INK + (46,), width=1)
        if c < c1:
            lo, hi = max(x, view.x0), min(x + cw, view.x1)
            if hi - lo > min(cw * 0.3, (view.x1 - view.x0) * 0.5):
                vx = view.pt(((lo + hi) / 2, 0))[0]
                for y in (t - 20, b + 20):
                    lab.text((vx, y), col_letters(c), size=15, style="bold", fill=INK, halo=False)
    r0, r1 = int(view.y0 // ch), min(painting.nrows, int(math.ceil(view.y1 / ch - 1e-9)))
    for rr in range(r0, r1 + 1):
        y = rr * ch
        if view.y0 < y < view.y1:
            vy = view.pt((0, y))[1]
            d.line([(l, vy), (r, vy)], fill=INK + (46,), width=1)
        if rr < r1:
            lo, hi = max(y, view.y0), min(y + ch, view.y1)
            if hi - lo > min(ch * 0.3, (view.y1 - view.y0) * 0.5):
                vy = view.pt((0, (lo + hi) / 2))[1]
                for x in (l - 22, r + 22):
                    lab.text((x, vy), str(rr + 1), size=15, style="bold", fill=INK, halo=False)
    canvas.alpha_composite(over)
    lab.flush(canvas)
    # the frame
    d = ImageDraw.Draw(canvas)
    d.rectangle([l - 1, t - 1, r, b], outline=INK + (255,), width=2)
    d.rectangle([l - 36, t - 36, r + 36, b + 36], outline=INK + (200,), width=2)
    d.rectangle([l - 32, t - 32, r + 32, b + 32], outline=INK_LIGHT + (160,), width=1)


def draw_settlement(canvas, xy, kind, alpha=255):
    d = ImageDraw.Draw(canvas)
    x, y = xy
    ink = INK + (alpha,)
    paper = PARCHMENT + (min(alpha, 230),)
    if kind == "city":
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=paper, outline=ink, width=2)
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=ink)
    elif kind == "village":
        d.ellipse([x - 3.5, y - 3.5, x + 3.5, y + 3.5], fill=paper, outline=ink, width=2)
    else:
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=paper, outline=ink, width=2)


def draw_region_labels(lab, view, regions, painting, dim=1.0):
    for k in regions:
        if k["grade"] == "rumored":
            p = k["near"]
            if view.inside(p):
                lab.add(view.pt(p), [(k["name"], 18, "italic", INK, int(150 * dim), 0)], priority=PRIORITY["rumored"])
            continue
        c = centroid(k["polygon"])
        if not view.inside(c):
            # the centroid of a region cut by the crop may fall outside; label the visible part instead
            vis = [p for p in k["polygon"] if view.inside(p)]
            if not vis:
                continue
            x0, y0, x1, y1 = bbox(vis)
            c = (max(view.x0, min(view.x1, (x0 + x1) / 2)), max(view.y0, min(view.y1, (y0 + y1) / 2)))
        reported = k["grade"] == "reported"
        # the label sits a little above the centroid, where features cluster, if that is still inside the region
        x0, y0, x1, y1 = bbox(k["polygon"])
        lifted = (c[0], c[1] - (c[1] - y0) * 0.3)
        if point_in_poly(lifted[0], lifted[1], k["polygon"]) and view.inside(lifted):
            c = lifted
        x, y = view.pt(c)
        fill = INK if not reported else INK_LIGHT
        a = int((255 if not reported else 225) * dim)
        lines = [(k["name"], 22, "regular", fill, a, -9),
                 (f"({painting.cell_of(centroid(k['polygon']))})", 13, "regular", fill, a, 11)]
        if reported:
            lines.append((f"reported: {k['source']}", 12, "italic", INK_LIGHT, int(210 * dim), 27))
        lab.add((x, y), lines, priority=PRIORITY["region-reported" if reported else "region"])


def draw_feature(canvas, lab, view, k, painting, region_names=(), dim=1.0):
    g = k["grade"]
    t = k["type"]
    coords = k["coords"]
    if t not in SETTLEMENT_TYPES and k["name"] in region_names:
        # a sea or wood that is also a region of the same name: the region label already names it
        return
    if g == "rumored":
        p = coords[0]
        if view.inside(p):
            lab.add(view.pt(p), [(k["name"], 13, "italic", INK, int(150 * dim), 0)], priority=PRIORITY["rumored"], leader=True)
        return
    reported = g == "reported"
    a = int((255 if not reported else 220) * dim)
    water = t in WATER_TYPES
    color = WATER_INK if water else (INK if not reported else INK_LIGHT)
    if t == "road":
        # the one feature drawn as a line: a thin ink trace, dashed when only reported
        if k["shape"] != "line" or len(coords) < 2:
            return
        pts = view.pts(coords)
        over = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(over)
        ink = ROAD_INK + (int(200 * dim) if not reported else int(150 * dim),)
        if reported:
            for i in range(len(pts) - 1):
                (x0, y0), (x1, y1) = pts[i], pts[i + 1]
                L = math.dist(pts[i], pts[i + 1])
                n = max(1, int(L // 6))
                for j in range(0, n, 2):
                    d.line([(x0 + (x1 - x0) * j / n, y0 + (y1 - y0) * j / n),
                            (x0 + (x1 - x0) * min(j + 1, n) / n, y0 + (y1 - y0) * min(j + 1, n) / n)], fill=ink, width=1)
        else:
            d.line(pts, fill=ink, width=2, joint="curve")
        canvas.alpha_composite(over)
        if k["name"]:
            mid = coords[len(coords) // 2]
            if view.inside(mid):
                lab.add(view.pt(mid), [(k["name"], 11, "italic", ROAD_INK, a, 0)],
                        priority=PRIORITY["road"] - (5 if reported else 0), leader=True)
        return
    if t in SETTLEMENT_TYPES:
        p = coords[0]
        if not view.inside(p):
            return
        x, y = view.pt(p)
        draw_settlement(canvas, (x, y), t, alpha=a)
        r = 8 if t == "city" else 6
        lab.obstacle((x - r, y - r, x + r, y + r))
        size = 17 if t == "city" else (15 if t == "town" else 13)
        lines = [(k["name"], size, "regular", color, a, 0)]
        if reported:
            lines.append((f"reported: {k['source']}", 10, "italic", INK_LIGHT, a, 14))
        lab.add((x, y), lines, priority=PRIORITY[t] - (10 if reported else 0), anchor="lm", leader=True)
        return
    # a named natural feature: label only
    if k["shape"] == "line" and len(coords) >= 2:
        # the label at the middle of the line, by length
        half = polyline_length(coords) / 2
        run = 0.0
        anchor = coords[len(coords) // 2]
        for i in range(len(coords) - 1):
            seg = math.dist(coords[i], coords[i + 1])
            if run + seg >= half and seg > 0:
                tt = (half - run) / seg
                anchor = (coords[i][0] + (coords[i + 1][0] - coords[i][0]) * tt, coords[i][1] + (coords[i + 1][1] - coords[i][1]) * tt)
                break
            run += seg
        p = anchor
    elif k["shape"] == "area" and len(coords) >= 3:
        p = centroid(coords)
    else:
        p = coords[0]
    if not view.inside(p):
        return
    x, y = view.pt(p)
    style = "italic" if water else "regular"
    size = 18 if t in ("sea", "mountain") else 14
    lines = [(k["name"], size, style, color, a, 0)]
    if reported:
        lines.append((f"reported: {k['source']}", 10, "italic", INK_LIGHT, a, 13))
    lab.add((x, y), lines, priority=PRIORITY.get(t, 50) - (10 if reported else 0), leader=True)


def scale_bar(view, painting):
    """(miles, length in sheet pixels) of the scale bar for this view: the first round figure
    at least 110 pixels long, so every zoom gets a bar at its own scale."""
    px_per_mile = view.scale / painting.mpp
    for mi in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500, 1000, 2000, 5000):
        if mi * px_per_mile >= 110:
            break
    return mi, mi * px_per_mile


def furniture_boxes(view, painting):
    """The scale bar's and the compass's boxes on the sheet, which no label may cover."""
    l, t, r, b = view.rect()
    _mi, L = scale_bar(view, painting)
    return [(l + 18 - 10, b - 22 - 26, l + 18 + L + 10, b - 22 + 12),
            (r - 42 - 32, t + 42 - 40, r - 42 + 32, t + 42 + 32)]


def draw_scale_bar(canvas, view, painting):
    mi, L = scale_bar(view, painting)
    l, t, r, b = view.rect()
    x0, y0 = l + 18, b - 22
    over = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    d.rounded_rectangle([x0 - 8, y0 - 24, x0 + L + 8, y0 + 10], radius=4, fill=PARCHMENT + (190,))
    canvas.alpha_composite(over)
    d = ImageDraw.Draw(canvas)
    d.line([(x0, y0), (x0 + L, y0)], fill=INK + (255,), width=2)
    for k in range(5):
        xx = x0 + L * k / 4
        d.line([(xx, y0 - 4), (xx, y0 + 4)], fill=INK + (255,), width=1)
    d.rectangle([x0, y0 - 3, x0 + L / 4, y0 + 3], fill=INK + (255,))
    d.rectangle([x0 + L / 2, y0 - 3, x0 + 3 * L / 4, y0 + 3], fill=INK + (255,))
    d.text((x0 + L / 2, y0 - 13), f"{mi} miles", font=font(11), fill=INK + (255,), anchor="mm")


def draw_compass(canvas, view):
    l, t, r, b = view.rect()
    cx, cy, rad = r - 42, t + 42, 22
    over = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    d.ellipse([cx - rad - 8, cy - rad - 8, cx + rad + 8, cy + rad + 8], fill=PARCHMENT + (190,))
    canvas.alpha_composite(over)
    d = ImageDraw.Draw(canvas)
    d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=INK + (255,), width=1)
    for i in range(8):
        ang = math.radians(i * 45)
        rr = rad if i % 2 == 0 else rad * 0.6
        tip = (cx + math.sin(ang) * rr, cy - math.cos(ang) * rr)
        bw = rad * 0.16
        bl = (cx + math.sin(ang - math.pi / 2) * bw, cy - math.cos(ang - math.pi / 2) * bw)
        br = (cx + math.sin(ang + math.pi / 2) * bw, cy - math.cos(ang + math.pi / 2) * bw)
        fill = INK + (255,) if i % 2 == 0 else PARCHMENT + (255,)
        d.polygon([tip, bl, (cx, cy), br], fill=fill, outline=INK + (255,))
    d.text((cx, cy - rad - 9), "N", font=font(13, "bold"), fill=INK + (255,), anchor="mm")


def wrap_lines(lines, width, size=11, style="italic"):
    """Word-wrap note lines to a pixel width."""
    f = font(size, style)
    out = []
    for line in lines:
        cur = ""
        for word in line.split():
            trial = (cur + " " + word).strip()
            if cur and f.getlength(trial) > width:
                out.append(cur)
                cur = word
            else:
                cur = trial
        if cur:
            out.append(cur)
    return out


def draw_notes(canvas, view, title, lines):
    d = ImageDraw.Draw(canvas)
    l, t, r, b = view.rect()
    y = b + 48
    d.text((l, y), title, font=font(15), fill=INK + (255,), anchor="lm")
    y += 18
    for line in lines:
        d.text((l, y), line, font=font(11, "italic"), fill=INK_LIGHT + (255,), anchor="lm")
        y += 14


def make_view(rect, notes):
    """A view whose bottom strip fits the wrapped notes."""
    probe = View(rect)
    wrapped = wrap_lines(notes, probe.W - probe.ml - 20)
    view = View(rect, margins=(56, 56, 56, 70 + 14 * len(wrapped)))
    return view, wrapped


def known_rect(regions_k, features_k, layer_id, painting):
    """The bounding box of seen and reported ground, with a margin of a fifth, clamped to the painting."""
    pts = []
    for k in regions_k.values():
        if k["polygon"]:
            pts.extend(k["polygon"])
    for k, lid in features_k.values():
        if lid == layer_id and k["grade"] != "rumored":
            pts.extend(k["coords"])
    if not pts:
        return (0, 0, painting.size[0], painting.size[1])
    x0, y0, x1, y1 = bbox(pts)
    mx, my = max((x1 - x0) / 5, 40), max((y1 - y0) / 5, 40)
    x0, y0 = max(0, x0 - mx), max(0, y0 - my)
    x1, y1 = min(painting.size[0], x1 + mx), min(painting.size[1], y1 + my)
    # keep the sheet from becoming a sliver
    if x1 - x0 < 200:
        c = (x0 + x1) / 2
        x0, x1 = max(0, c - 100), min(painting.size[0], c + 100)
    if y1 - y0 < 200:
        c = (y0 + y1) / 2
        y0, y1 = max(0, c - 100), min(painting.size[1], c + 100)
    return (x0, y0, x1, y1)


LANDING_MARGIN = 0.25     # of the seen box, on every side
LANDING_MIN_MARGIN = 6    # painting pixels
LANDING_MIN_SIZE = 32     # painting pixels across, at the least


def landing_rect(regions_k, features_k, painting):
    """The landing zoom: the bounding box of the seen regions, plus a margin of a quarter of the
    box (at least LANDING_MIN_MARGIN pixels) on every side, clamped to the painting. With no
    seen region it falls back to the known zoom."""
    pts = []
    for k in regions_k.values():
        if k["grade"] == "seen" and k["polygon"]:
            pts.extend(k["polygon"])
    if not pts:
        return known_rect(regions_k, features_k, None, painting)
    x0, y0, x1, y1 = bbox(pts)
    mx = max((x1 - x0) * LANDING_MARGIN, LANDING_MIN_MARGIN)
    my = max((y1 - y0) * LANDING_MARGIN, LANDING_MIN_MARGIN)
    x0, y0, x1, y1 = x0 - mx, y0 - my, x1 + mx, y1 + my
    for lo, hi, axis in ((x0, x1, 0), (y0, y1, 1)):
        if hi - lo < LANDING_MIN_SIZE:
            c = (lo + hi) / 2
            lo, hi = c - LANDING_MIN_SIZE / 2, c + LANDING_MIN_SIZE / 2
        if axis == 0:
            x0, x1 = lo, hi
        else:
            y0, y1 = lo, hi
    return (max(0, x0), max(0, y0), min(painting.size[0], x1), min(painting.size[1], y1))


def zoom_rect(zoom, regions_k, features_k, layer_id, painting):
    if zoom == "known":
        return known_rect(regions_k, features_k, layer_id, painting)
    if zoom == "landing":
        return landing_rect(regions_k, features_k, painting)
    return (0, 0, *painting.size)


def beyond_notes(view, regions_k, features_k, layer_id):
    cx, cy = (view.x0 + view.x1) / 2, (view.y0 + view.y1) / 2
    items = [(k["name"], k["near"]) for k in regions_k.values() if k["grade"] == "rumored"]
    items += [(k["name"], k["coords"][0]) for k, lid in features_k.values() if lid == layer_id and k["grade"] == "rumored"]
    notes = [f"{name}, {bearing_name(p[0] - cx, p[1] - cy)}" for name, p in items if not view.inside(p)]
    return ["rumored, beyond this sheet: " + "; ".join(notes)] if notes else []


LAST_LABELS = {"dropped": [], "moved": 0}


def draw_sheet(world, painting, paintings_dir, painting_file, regions, features, view, title, notes, layer_name=None):
    paint = load_painting(paintings_dir, painting_file, painting.size)
    clouds = load_painting(paintings_dir, "clouds.png", painting.size)
    mask = fog_mask(regions, painting.size)
    canvas = parchment_canvas(view)
    ground = paint_ground(view, paint, clouds, mask)
    canvas.alpha_composite(ground, (view.ml, view.mt))
    draw_grid(canvas, view, painting)
    lab = Labeler(canvas.size, bounds=view.rect())
    for box in furniture_boxes(view, painting):
        lab.obstacle(box)
    region_names = {k["name"] for k in regions if k["grade"] != "rumored"}
    # settlement marks first, so that every label (region names included) keeps off them
    for shape in ("area", "line", "point"):
        for k in features:
            if k["shape"] == shape:
                draw_feature(canvas, lab, view, k, painting, region_names)
    draw_region_labels(lab, view, regions, painting)
    lab.place()
    lab.flush(canvas)
    LAST_LABELS["dropped"] = list(lab.dropped)
    LAST_LABELS["moved"] = lab.moved
    draw_scale_bar(canvas, view, painting)
    draw_compass(canvas, view)
    if layer_name:
        d = ImageDraw.Draw(canvas)
        l, t, r, b = view.rect()
        d.text(((l + r) / 2, t - 46), layer_name, font=font(16, "bold"), fill=INK + (255,), anchor="mm")
    draw_notes(canvas, view, title, notes)
    return canvas.convert("RGB")


def draw_sheets(world, paintings_dir, knowledge, out_dir, zoom, which):
    painting = Painting(world)
    regions_k, features_k = gather(world, knowledge, painting)
    surface_regions = [k for rid, k in regions_k.items() if any(r["id"] == rid for r in world.get("regions", []))]
    name = world.get("campaign", "world")
    os.makedirs(out_dir, exist_ok=True)
    written = []
    legend = ["Seen ground shows the painting clear. Reported ground shows through cloud, as told, and may be wrong.",
              "Rumors are faint names. Cloud is ground the god does not know. Grid letters and numbers are for reference out of game."]

    frames = {}
    labels = {}
    if which in (None, "surface"):
        rect = zoom_rect(zoom, regions_k, features_k, None, painting)
        view = View(rect)
        feats = [k for k, lid in features_k.values() if lid is None]
        view, notes = make_view(rect, legend + beyond_notes(view, regions_k, features_k, None))
        im = draw_sheet(world, painting, paintings_dir, "surface.png", surface_regions, feats, view, f"{name}: the god's map", notes)
        path = os.path.join(out_dir, "map.png")
        im.save(path, optimize=True)
        written.append(path)
        frames["surface"] = rect
        labels["surface"] = dict(LAST_LABELS)

    for layer in world.get("layers", []):
        lid = layer["id"]
        depth = layer.get("depth", 1)
        if which not in (None, lid, f"under-{depth}"):
            continue
        under = [k for k, l in features_k.values() if l == lid]
        if not under and which is None:
            continue
        layer_regions = [regions_k[r["id"]] for r in layer.get("regions", []) if r["id"] in regions_k]
        regions = layer_regions if layer.get("regions") else surface_regions
        rect = zoom_rect(zoom, {k["id"]: k for k in regions}, features_k, lid, painting)
        view = View(rect)
        view, notes = make_view(rect, ["The ground below is fogged by what is known of the ground above it unless the layer has its own regions.",
                                       "Only known ground below is named."] + beyond_notes(view, {}, features_k, lid))
        im = draw_sheet(world, painting, paintings_dir, layer.get("painting", f"under-{depth}.png"), regions, under, view,
                        f"{name}: below, layer {depth}", notes, layer_name=f"Below, layer {depth}: {layer.get('name', '')}")
        path = os.path.join(out_dir, f"map-under-{depth}.png")
        im.save(path, optimize=True)
        written.append(path)
        frames[f"under-{depth}"] = rect
        labels[f"under-{depth}"] = dict(LAST_LABELS)

    def frame_cells(rect):
        return f"{painting.cell_of((rect[0], rect[1]))}:{painting.cell_of((rect[2] - 1, rect[3] - 1))}"

    meta = {"frames": {k: frame_cells(rect) for k, rect in frames.items()},
            "grid": [painting.ncols, painting.nrows], "sheet_miles": [round(painting.miles(v)) for v in painting.size],
            "zoom": zoom or "full",
            "frame_miles": {k: [round(painting.miles(r[2] - r[0])), round(painting.miles(r[3] - r[1]))] for k, r in frames.items()},
            "labels_dropped": {k: len(v["dropped"]) for k, v in labels.items()},
            "regions_drawn": {g: sum(1 for k in regions_k.values() if k["grade"] == g) for g in ("seen", "reported", "rumored")},
            "features_drawn": {g: sum(1 for k, _ in features_k.values() if k["grade"] == g) for g in ("seen", "reported", "rumored")},
            "drawn": pacific_today(), "files": [os.path.basename(w) for w in written]}
    save_json(os.path.join(out_dir, "map-meta.json"), meta)
    return written


# ---------------------------------------------------------------- gazetteer

def read_log(path):
    """map-log.md lines: - DATE | year N | kind id | old -> new | source"""
    hist = {}
    if not os.path.exists(path):
        return hist
    for line in open(path):
        line = line.strip()
        if not line.startswith("- "):
            continue
        parts = [p.strip() for p in line[2:].split("|")]
        if len(parts) < 5:
            continue
        kind_id = parts[2].split()
        if len(kind_id) == 2:
            hist.setdefault(kind_id[1], []).append(f"year {parts[1].replace('year ', '')}: {parts[3]} ({parts[4]})")
    return hist


def fmt_pt(p, painting):
    """A place as the public files give it: a grid cell, never a coordinate."""
    return painting.cell_of(p)


def believed_polygon(k, knowledge):
    """A known region's polygon as the god believes it: the truth if seen, told.polygon if reported
    with one, else None (a report that gave no shape carries no distance)."""
    if k["grade"] == "seen":
        return k["polygon"]
    told = (knowledge.get("regions", {}).get(k["id"], {}) or {}).get("told") or {}
    return told.get("polygon")


def told_span(a, b, knowledge, painting):
    """The distance between two known regions when one is only reported, from told data only:
    miles between the centers the god believes, no days. Never the sealed travel days."""
    pa, pb = believed_polygon(a, knowledge), believed_polygon(b, knowledge)
    if not pa or not pb:
        return "distance not told"
    return f"about {painting.miles(math.dist(centroid(pa), centroid(pb))):.0f} miles center to center as told, days not known"


def gazetteer(world, knowledge, out_dir, log_path):
    painting = Painting(world)
    hist = read_log(log_path)
    mi = painting.miles
    lines = [f"# Gazetteer: {world.get('campaign', 'the world')}", "",
             "Everything the god knows of the ground, exact where the map is pictorial. Regenerated from `player/map-knowledge.json` by `tools/map.py gazetteer`; never edited by hand. "
             f"Places are given by map grid cell ({painting.ncols} columns by {painting.nrows} rows); distances are in miles. "
             "Grades: seen (found so), reported (as told, may be wrong), rumored (a name and a rough place).", ""]
    regions_k, features_k = gather(world, knowledge, painting)
    regions = list(regions_k.values())
    region_truth = {r["id"]: r for r, _ in all_regions(world)}
    layer_by_id = {l["id"]: l for l in world.get("layers", [])}
    feats = [(k, layer_by_id.get(lid) if lid else None) for k, lid in features_k.values()]
    reg_name = {k["id"]: k["name"] for k in regions}

    def hist_line(i):
        return ("; history: " + "; ".join(hist[i])) if i in hist else ""

    lines.append("## Regions")
    lines.append("")
    for g in ("seen", "reported", "rumored"):
        for k in sorted((r for r in regions if r["grade"] == g), key=lambda r: r["name"]):
            if g == "rumored":
                lines.append(f"- **{k['name']}**, rumored, somewhere near {fmt_pt(k['near'], painting)} by the telling of {k['source']}, year {k['year']}{hist_line(k['id'])}.")
            else:
                c = centroid(k["polygon"])
                across = f", about {mi(extent_across(k['polygon'])):.0f} miles across" if g == "seen" else ""
                lines.append(f"- **{k['name']}** ({painting.cell_of(c)}), {k['terrain']}{across}, {g}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
    lines.append("")

    lines.append("## Travel between known regions")
    lines.append("")
    lines.append("Days on foot between neighboring regions the god has seen, at the pace table's rate. Where one of the two is only reported, "
                 "the figure is what was told: the miles between the two as the god believes them, and no days, since no one has walked it for the god.")
    lines.append("")
    pairs, done = [], set()
    for rid, k in regions_k.items():
        if k["grade"] == "rumored":
            continue
        for n in region_truth.get(rid, {}).get("neighbors", []):
            nid = n.get("id") if isinstance(n, dict) else n
            other = regions_k.get(nid)
            if not other or other["grade"] == "rumored" or frozenset((rid, nid)) in done:
                continue
            done.add(frozenset((rid, nid)))
            days = n.get("days") if isinstance(n, dict) else None
            grade = "seen" if k["grade"] == "seen" and other["grade"] == "seen" else "reported"
            pairs.append((rid, nid, days, grade))
    if not pairs:
        lines.append("No two known regions border each other.")
    for a, b, days, grade in sorted(pairs, key=lambda t: (regions_k[t[0]]["name"], regions_k[t[1]]["name"])):
        if grade == "seen":
            d = f"{days:g} days" if isinstance(days, (int, float)) else "days unknown"
        else:
            d = told_span(regions_k[a], regions_k[b], knowledge, painting)
        lines.append(f"- **{regions_k[a]['name']}** to **{regions_k[b]['name']}**: {d} ({grade}).")
    lines.append("")

    def place_block(title, items, kinds):
        lines.append(f"## {title}")
        lines.append("")
        sel = [k for k, layer in items if k["type"] in kinds and k["grade"] != "rumored"]
        if not sel:
            lines.append("Nothing known.")
        for k in sorted(sel, key=lambda k: (grade_rank(k["grade"]) * -1, k["name"])):
            regs = ", ".join(reg_name.get(r, "a region not yet known") for r in k["regions"] if regions_k.get(r, {}).get("grade") != "rumored") if k["grade"] == "seen" else ""
            if k["shape"] == "point":
                where = f"at {fmt_pt(k['coords'][0], painting)}"
            elif k["shape"] == "line":
                where = f"{mi(polyline_length(k['coords'])):.0f} miles long, from {fmt_pt(k['coords'][0], painting)} to {fmt_pt(k['coords'][-1], painting)}"
            else:
                x0, y0, x1, y1 = bbox(k["coords"])
                where = f"about {mi(x1 - x0):.0f} by {mi(y1 - y0):.0f} miles, centered {fmt_pt(centroid(k['coords']), painting)}"
            lines.append(f"- **{k['name']}** ({k['type']}), {where}{', in ' + regs if regs else ''}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
        lines.append("")

    surface = [(k, l) for k, l in feats if l is None]
    place_block("Places", surface, POINT_TYPES)
    place_block("Waters, woods and ranges", surface, {"river", "lake", "sea", "mountain", "marsh", "forest"})
    place_block("Roads", surface, {"road"})

    lines.append("## Rivers as routes")
    lines.append("")
    routes = [k for k, l in surface if k["type"] == "river" and k["grade"] != "rumored" and k["shape"] == "line"]
    points = [k for k, l in surface if k["shape"] == "point" and k["type"] in POINT_TYPES and k["grade"] != "rumored"]
    if not routes:
        lines.append("No river known.")
    for r in routes:
        along = []
        for p in points:
            d, t = dist_to_polyline(p["coords"][0], r["coords"])
            if mi(d) <= 3:
                along.append((t, p["name"]))
        along.sort()
        stops = ", ".join(n for _, n in along) if along else "no known place along it"
        lines.append(f"- **{r['name']}**, {mi(polyline_length(r['coords'])):.0f} miles, {r['grade']}: {stops}.")
    lines.append("")

    lines.append("## Distances")
    lines.append("")
    lines.append("As the crow flies, in miles, from the positions the god believes; a reported endpoint makes the distance reported. The pace table (`engine/rules/time-and-pace.md`) turns miles into days.")
    lines.append("")
    for p in sorted(points, key=lambda k: k["name"]):
        others = sorted(((math.dist(p["coords"][0], q["coords"][0]), q) for q in points if q is not p), key=lambda t: t[0])[:4]
        if not others:
            continue
        parts = [f"{q['name']} {mi(d):.0f} ({'seen' if p['grade'] == 'seen' and q['grade'] == 'seen' else 'reported'})" for d, q in others]
        lines.append(f"- **{p['name']}**: " + "; ".join(parts) + ".")
    lines.append("")

    lines.append("## Rumors")
    lines.append("")
    rum = [k for k, l in surface if k["grade"] == "rumored"]
    if not rum:
        lines.append("None.")
    for k in sorted(rum, key=lambda k: str(k["year"] or 0)):
        kind = f" ({k['type']})" if k["type"] else ""
        lines.append(f"- **{k['name']}**{kind}, somewhere near {fmt_pt(k['coords'][0], painting)}, by the telling of {k['source']}, year {k['year']}{hist_line(k['id'])}.")
    lines.append("")

    for layer in world.get("layers", []):
        under = [(k, l) for k, l in feats if l is layer]
        if not under:
            continue
        lines.append(f"## Below, layer {layer.get('depth', 1)}: {layer.get('name', '')}")
        lines.append("")
        for k, _ in sorted(under, key=lambda t: (grade_rank(t[0]["grade"]) * -1, t[0]["name"])):
            if k["grade"] == "rumored":
                lines.append(f"- **{k['name']}**, rumored, somewhere under {fmt_pt(k['coords'][0], painting)}, by the telling of {k['source']}, year {k['year']}.")
            elif k["shape"] == "line":
                lines.append(f"- **{k['name']}** ({k['type']}), {mi(polyline_length(k['coords'])):.0f} miles, from under {fmt_pt(k['coords'][0], painting)} to under {fmt_pt(k['coords'][-1], painting)}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
            else:
                lines.append(f"- **{k['name']}** ({k['type']}), under {fmt_pt(k['coords'][0], painting)}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
        lines.append("")

    path = os.path.join(out_dir, "gazetteer.md")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    return path


# ---------------------------------------------------------------- reveal

def reveal(world, knowledge, knowledge_path, log_path, args):
    painting = Painting(world)
    kind = "region" if args.region else "feature"
    ident = args.region or args.feature
    if args.grade not in GRADES or args.grade == "none":
        sys.exit("map.py: grade must be rumored, reported or seen")
    hit = index_world(world).get(ident)
    if hit is None or hit[0] != kind:
        sys.exit(f"map.py: no {kind} with id {ident!r} in the sealed map; a typo cannot create ground")
    truth = hit[1]
    if kind == "region" and args.grade == "rumored" and not RUMORED_REGIONS_ALLOWED:
        sys.exit("map.py: a region id enters the player's file only when seen or reported; attach the rumor to a feature, or keep it in the chronicle")
    if not OPAQUE_RE.match(ident):
        print(f"note: id {ident!r} is not opaque; new maps use ids like r01, f03, u01", file=sys.stderr)
    table = knowledge.setdefault(kind + "s", {})
    old = table.get(ident, {})
    old_grade = grade_of(old)
    if grade_rank(args.grade) < grade_rank(old_grade) and not args.force:
        sys.exit(f"map.py: {ident} is already {old_grade}; lowering needs --force \"reason\"")
    told = {}
    if args.told:
        try:
            told = json.loads(args.told)
        except json.JSONDecodeError as e:
            sys.exit(f"map.py: --told is not valid JSON: {e}")
        bad = set(told) - TOLD_KEYS
        if bad:
            sys.exit(f"map.py: --told takes only {', '.join(sorted(TOLD_KEYS))} ({', '.join(sorted(bad))} given)")
    if args.name:
        told["name"] = args.name
    if args.cell:
        told["cell"] = args.cell
    if "cell" in told:
        if painting.parse_cell(told["cell"]) is None:
            sys.exit(f"map.py: cell {told['cell']!r} is not on this {painting.ncols} by {painting.nrows} grid")
        told["cell"] = str(told["cell"]).upper()
    entry = {"grade": args.grade, "source": args.source, "year": args.year}
    correction = ""
    old_told = old.get("told", {}) or {}
    if args.grade == "seen":
        true_c = centroid(truth.get("polygon") or truth["coords"])
        shape = old_told.get("coords") or old_told.get("polygon")
        told_cell = painting.cell_of(centroid(shape)) if shape else old_told.get("cell")
        if old_grade in ("reported", "rumored") and (shape or told_cell):
            far = painting.miles(math.dist(centroid(shape), true_c)) > 1 if shape else told_cell != painting.cell_of(true_c)
            if far:
                correction = f"; told at {told_cell} by {old.get('source', '?')}, found at {painting.cell_of(true_c)}"
        if old_told.get("name") and old_told["name"] != truth["name"]:
            correction += f"; called {old_told['name']} by {old.get('source', '?')}, found to be {truth['name']}"
    elif args.grade == "reported":
        if PIXEL_KEYS & set(told) == {"near"}:
            sys.exit("map.py: `near` is not a reported shape; give coords, polygon or cell")
        if told:
            entry["told"] = told
        elif old_told and old_grade == "reported":
            entry["told"] = old_told  # keep what was told before if the new teller adds nothing
    else:  # rumored
        if PIXEL_KEYS & set(told):
            sys.exit("map.py: a rumor carries a name and a cell, never pixels")
        kept = {k: v for k, v in old_told.items() if k in ("name", "type")}
        shape = old_told.get("coords") or old_told.get("polygon")
        if shape and "cell" not in told:
            kept["cell"] = painting.cell_of(centroid(shape))  # lowered: the old telling as a rough place
        kept.update(told)
        if not kept.get("name"):
            sys.exit("map.py: a rumor needs a name (--name): the name as told, never the Keeper's")
        if "cell" not in kept:
            sys.exit("map.py: a rumor needs a cell (--cell C2): where the teller places it, as loosely as they did")
        entry["told"] = kept
    table[ident] = entry
    save_json(knowledge_path, knowledge)
    os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
    reason = f"; forced: {args.force}" if args.force else ""
    with open(log_path, "a") as f:
        f.write(f"- {pacific_today()} | year {args.year} | {kind} {ident} | {old_grade} -> {args.grade} | {args.source}{correction}{reason}\n")
    print(f"{kind} {ident}: {old_grade} -> {args.grade} ({args.source}, year {args.year}){correction}")


def migrate(world, knowledge, painting):
    """Bring an older knowledge file to the current rules: rumors get a cell instead of `near`,
    seen entries lose any told (and, if RUMORED_REGIONS_ALLOWED is False, rumored regions
    leave the file). Ids are not renamed (that is a
    sealed-map change). Returns notes on what changed."""
    notes = []
    for table, kind in (("regions", "region"), ("features", "feature")):
        for ident in list(knowledge.get(table, {})):
            e = knowledge[table][ident]
            g = grade_of(e)
            t = e.get("told") or {}
            if g == "seen" and "told" in e:
                del e["told"]
                notes.append(f"{kind} {ident}: dropped told from a seen entry")
            if g == "rumored":
                if kind == "region" and not RUMORED_REGIONS_ALLOWED:
                    del knowledge[table][ident]
                    notes.append(f"{kind} {ident}: rumored region removed (record the rumor in the chronicle or on a feature)")
                    continue
                if "near" in t:
                    t["cell"] = painting.cell_of(t.pop("near"))
                    notes.append(f"{kind} {ident}: near became cell {t['cell']}")
                if "cell" not in t:
                    el = index_world(world).get(ident, (None, None))[1]
                    if el:
                        t["cell"] = painting.cell_of(centroid(el.get("polygon") or el["coords"]))
                        notes.append(f"{kind} {ident}: rumor given cell {t['cell']}")
                e["told"] = t
    return notes


# ---------------------------------------------------------------- stamp

STAMP_SKIP = {"LOCKED.md"}


def stamp_names(world):
    """{name variant: sorted ids} for every map name (with and without a leading article), kept only
    when capitalized and four letters or more, the rule lockcheck --places warns by."""
    names = {}
    for el, _layer in list(all_regions(world)) + list(all_features(world)):
        nm = (el.get("name") or "").strip()
        variants = {nm}
        m = re.match(r"^(The|the|A|An)\s+(.+)$", nm)
        if m:
            variants.add(m.group(2))
        for v in variants:
            if len(v) >= 4 and v[0].isupper():
                names.setdefault(v, set()).add(el["id"])
    return {v: sorted(ids) for v, ids in names.items()}


def stamp_text(text, names):
    """Append [id] after every map name in text that does not already carry one of its ids.
    Longer names win where names overlap. Returns (new text, number stamped)."""
    if not names:
        return text, 0
    rx = re.compile(r"(?<![\w'\-\[])(" + "|".join(re.escape(v) for v in sorted(names, key=len, reverse=True)) + r")(?![\w\-])")
    out, last, n = [], 0, 0
    for m in rx.finditer(text):
        ids = names[m.group(1)]
        end = m.end()
        poss = re.match(r"'s\b", text[end:])
        if poss:
            end += poss.end()
        after = re.sub(r"^\s*(\([^)\n]*\)\s*)?", "", text[end:end + 80])
        bm = re.match(r"\[([a-z0-9, -]+)\]", after)
        if bm and set(re.split(r"\s*,\s*", bm.group(1))) & set(ids):
            continue
        out.append(text[last:end])
        out.append(f" [{', '.join(ids)}]")
        last = end
        n += 1
    out.append(text[last:])
    return "".join(out), n


def stamp(campaign, sealed_dir, world, dry_run=False):
    """Stamp every .md file in the sealed campaign folder. Never reads or writes the public folder.
    Skips the checker's flags files and LOCKED.md. Returns (files changed, names stamped, per-file counts)."""
    sealed_dir = os.path.abspath(sealed_dir)
    public = os.path.abspath(os.path.join(ROOT, "campaigns", campaign))
    names = stamp_names(world)
    changed, total, per = 0, 0, []
    for dirpath, dirs, files in os.walk(sealed_dir):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for fn in sorted(files):
            path = os.path.join(dirpath, fn)
            if not fn.endswith(".md") or fn in STAMP_SKIP or re.match(r"^lock-flags.*\.md$", fn):
                continue
            if os.path.commonpath([os.path.abspath(path), public]) == public:
                continue  # never the public folder
            with open(path, encoding="utf-8") as f:
                text = f.read()
            new, n = stamp_text(text, names)
            if n:
                per.append((os.path.relpath(path, sealed_dir), n))
                changed += 1
                total += n
                if not dry_run:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new)
    return changed, total, per


# ---------------------------------------------------------------- describe

EYE_FT = 6.0                # a tall mortal's eye above the ground
HORIZON_K = 1.22            # miles = 1.22 * sqrt(feet), the sight line over a curved earth with ordinary refraction
NEAR_MILES = {"open": 2.0, "closed": 0.5}   # ground-level things in view (map.md 1.4, 2.1): open ground, forest or hill
SKYLINE_MILES = 40.0        # the skyline from a hill, ridge or coast in clear air (map.md 1.4)
OPEN_TERRAIN = {"plain", "valley", "steppe", "coast", "desert", "tundra", "sea", "marsh", "island", "lake", "mountain"}
HEIGHT_TERRAIN = {"hill", "highland", "mountain"}
COAST_TERRAIN = {"coast", "island", "sea"}
VIEW_WORDS = {"floor": "from a valley floor or plain", "height": "from a hill, ridge or height", "coast": "from a coast"}
ELEVATION_WORDS = [          # (word, floor feet, top feet) when the elevation gives no figure, first match wins
    ("at the tide", 0, 10), ("sea level", 0, 50), ("sea", 0, 0), ("mountain", 4000, 10000),
    ("high", 2000, 6000), ("upland", 1000, 2500), ("low hill", 100, 800), ("hill", 300, 1500),
    ("pass", 500, 2000), ("low", 0, 500)]


def sight_miles(relief_ft, eye_ft=EYE_FT):
    """How far a tall mortal's eye sees ground that stands relief_ft above its own: the eye's horizon
    plus the target's. A target no higher than the eye shows only out to the eye's own horizon."""
    return HORIZON_K * (math.sqrt(max(eye_ft, 0)) + math.sqrt(max(relief_ft, 0)))


def parse_elevation(region):
    """(floor feet, top feet, from_figures) from a region's elevation text, terrain as a fallback."""
    text = str(region.get("elevation", ""))
    nums = [int(x.replace(",", "")) for x in re.findall(r"\d{1,3}(?:,\d{3})+|\d+", text)] if re.search(r"feet|ft\b|foot", text) else []
    low = text.lower()
    word = next(((f, t) for w, f, t in ELEVATION_WORDS if w in low), None)
    if word is None:
        terr = str(region.get("terrain", "")).lower()
        word = next(((f, t) for w, f, t in ELEVATION_WORDS if w in terr), (0, 500))
    if nums:
        if len(nums) >= 2:
            return min(nums), max(nums), True
        if re.search(r"(?<!\d)\bto\s+[\d,]+", text):
            return min(word[0], nums[0]), nums[0], True   # "to 4,000 feet": the floor from the word
        return nums[0], nums[0], True
    return word[0], word[1], False


def terrain_word(region):
    return (str(region.get("terrain", "")).split(",")[0].split() or ["land"])[0].lower()


def openness(region):
    return "open" if terrain_word(region) in OPEN_TERRAIN else "closed"


def dist_to_poly_edge(p, poly):
    """Miles-free distance (painting pixels) from p to a polygon: 0 inside, else to its nearest edge,
    and the nearest point."""
    if point_in_poly(p[0], p[1], poly):
        return 0.0, tuple(p)
    best, foot = float("inf"), None
    ring = list(poly) + [poly[0]]
    for i in range(len(ring) - 1):
        a, b = ring[i], ring[i + 1]
        ab = (b[0] - a[0], b[1] - a[1])
        L2 = ab[0] ** 2 + ab[1] ** 2
        t = 0 if L2 == 0 else max(0, min(1, ((p[0] - a[0]) * ab[0] + (p[1] - a[1]) * ab[1]) / L2))
        f = (a[0] + ab[0] * t, a[1] + ab[1] * t)
        d = math.dist(p, f)
        if d < best:
            best, foot = d, f
    return best, foot


def fmt_miles(mi):
    if mi < 0.2:
        return "a few hundred yards"
    if mi < 0.4:
        return "about a quarter mile"
    if mi < 0.75:
        return "about half a mile"
    if mi < 1.5:
        return "about a mile"
    return f"about {mi:.0f} miles"


class Namer:
    """Names as a god has learned them: from its knowledge file (seen: the name; told.name; a report
    with no told name: the name, as the teller was accurate), else a plain description. --names
    gives every true name."""

    def __init__(self, world, knowledge, all_names=False):
        self.world = world
        self.k = knowledge or {"regions": {}, "features": {}}
        self.all = all_names
        self.by_id = index_world(world)

    def learned(self, ident):
        kind = self.by_id.get(ident, (None,))[0]
        table = "regions" if kind == "region" else "features"
        e = self.k.get(table, {}).get(ident)
        g = grade_of(e)
        if g == "none":
            return None
        told = (e.get("told") or {}) if g != "seen" else {}
        if told.get("name"):
            return told["name"]
        if g in ("seen", "reported"):
            return self.by_id[ident][1].get("name")
        return None

    def generic(self, ident):
        kind, el, _ = self.by_id[ident]
        if kind == "region":
            w = terrain_word(el)
            return "the sea" if w == "sea" else f"{'an' if w[0] in 'aeiou' else 'a'} {w} country"
        t = el.get("type", "place")
        return f"{'an' if t[0] in 'aeiou' else 'a'} {t}"

    def name(self, ident):
        if self.all:
            return self.by_id[ident][1].get("name") or self.generic(ident)
        return self.learned(ident) or self.generic(ident)

    def scrub(self, text):
        """Free text from the sealed map with every name the god has not learned put plainly."""
        if self.all or not text:
            return text
        for ident, (kind, el, _l) in sorted(self.by_id.items(), key=lambda kv: -len(kv[1][1].get("name", ""))):
            nm = el.get("name", "")
            known = self.learned(ident)
            if not nm or known == nm:
                continue
            core = re.sub(r"^(The|the)\s+", "", nm)
            rx = re.compile(r"(?<![\w])(?:[Tt]he\s+)?" + re.escape(core) + r"(?![\w])")
            text = rx.sub(lambda m, k=known or self.generic(ident): k, text)
        return text

    def ids_or_text(self, v):
        if isinstance(v, list):
            return ", ".join(self.name(i) if i in self.by_id else str(i) for i in v) or "none named"
        return self.scrub(str(v))


def god_knowledge(campaign, god, sealed_dir):
    if god in (None, ""):
        return None
    if god == "player":
        p = os.path.join(ROOT, "campaigns", campaign, "player", "map-knowledge.json")
    else:
        p = os.path.join(sealed_dir, "gods", god, "map-knowledge.json")
    return load_json(p, default={"regions": {}, "features": {}})


def describe(world, region_id=None, at=None, knowledge=None, all_names=False, label=None):
    """A land description read off the map data: the region's terrain, elevation, water and climate;
    its neighbors with travel days and directions; what is in view from the point and the sight line.

    Sight at landing, engine/rules/map.md 1.4, read off the data the same way for every god:
    - The ground the god stands on decides the reading. From a valley floor or a plain (any ground but
      hill, highland, mountain, coast, island or sea) the eye is a tall mortal's, EYE_FT above the
      region's lowest figure; a region standing higher shows on the skyline out to sight_miles(relief),
      the eye's horizon plus the higher ground's own, unless ground between stands above the line from
      the eye to its top (blocker); level or lower ground shows only within the near distance.
      Worked: from a valley floor at 1,200 feet, ridges topping 3,000 feet (relief 1,800) show out to
      1.22 x (2.4 + 42.4), about 55 miles, and peaks of 13,000 feet out to about 136 miles if no ridge
      between stands above the line to them.
    - From a hill, highland or mountain the eye stands at the region's highest figure and sees out to
      a skyline of SKYLINE_MILES (forty) at most, whatever stands beyond; from a coast, island or sea, the
      sea and any shore within the same forty miles.
    - Point, line and area features (a town, a ruin, a cave mouth, a river's reach, a road, a lake) are
      in view within NEAR_MILES: two miles on open ground, half a mile in forest or hill (line of sight
      in mountains is read as the open-ground two miles). A settlement farther off is given as its
      smoke, walls or lights only: in the god's own region from a floor, within the forty-mile skyline
      from a height or a coast, and never past ground that stands above the line to it.
    - A mountain feature is read as the highest region it touches. Nothing underground is seen."""
    painting = Painting(world)
    mi = painting.miles
    by_id = index_world(world)
    names = Namer(world, knowledge, all_names)
    region = by_id[region_id][1]
    if at is None:
        at = centroid(region["polygon"])
        where = "from the middle of the region (no landing point is given)"
    else:
        where = "from the landing point"
    floor, top, figs = parse_elevation(region)
    out = []
    head = names.name(region_id)
    out.append(f"{label or 'Land description'}: {head}, {where}, in grid cell {painting.cell_of(at)}.")
    out.append("")
    terrain = names.scrub(region.get("terrain", ""))
    out.append(f"The ground is {terrain}. Elevation: {names.scrub(str(region.get('elevation', 'not given')))}"
               f"{'' if figs else ' (no figure given; read as ' + str(floor) + ' to ' + str(top) + ' feet)'}. "
               f"Water: {names.ids_or_text(region.get('water', 'none given'))}. Climate: {names.scrub(str(region.get('climate', 'not given')))}.")
    x0, y0, x1, y1 = bbox(region["polygon"])
    out.append(f"The region runs about {mi(x1 - x0):.0f} miles east to west and {mi(y1 - y0):.0f} miles north to south.")
    out.append("")

    # neighbors
    nb_lines = []
    for n in region.get("neighbors", []):
        nid = n.get("id") if isinstance(n, dict) else n
        if nid not in by_id:
            continue
        other = by_id[nid][1]
        d_edge, foot = dist_to_poly_edge(at, other["polygon"])
        c = centroid(other["polygon"])
        days = n.get("days") if isinstance(n, dict) else None
        by = n.get("by") if isinstance(n, dict) else None
        dtxt = f"{days:g} days on foot at the pace table's cross-country rate" if isinstance(days, (int, float)) else (f"by {by}" if by else "days not given")
        nb_lines.append(f"- {names.name(nid)} ({terrain_word(other)}), lying {bearing_name(c[0] - at[0], c[1] - at[1])}: "
                        f"{dtxt}; its nearest edge {fmt_miles(mi(d_edge))} {bearing_name(foot[0] - at[0], foot[1] - at[1])} of the point.")
    out.append("Neighbors:" if nb_lines else "Neighbors: none given.")
    out += nb_lines
    out.append("")

    # sight
    kind = viewpoint(region)
    near = NEAR_MILES[openness(region)]
    eye_ground = floor if kind == "floor" else top
    cap = None if kind == "floor" else SKYLINE_MILES
    out.append(f"Sight line ({VIEW_WORDS[kind]}): a tall mortal's eye, {EYE_FT:g} feet above ground at about {eye_ground:,} feet, "
               f"sees level ground out to {fmt_miles(sight_miles(0))}; things at ground level are in view within {fmt_miles(near)} "
               f"({'open' if near == NEAR_MILES['open'] else 'hill or forest'} ground)"
               + (f"; nothing past a skyline of {SKYLINE_MILES:g} miles." if cap else "; higher ground shows on the skyline as far as its height carries, unless ground between hides it."))
    in_view, hidden, smoke = [], [], []
    for r, _layer in all_regions(world):
        if r["id"] == region_id:
            continue
        d_px, foot = dist_to_poly_edge(at, r["polygon"])
        d = mi(d_px)
        rf, rt, _ = parse_elevation(r)
        relief = rt - eye_ground
        higher = relief > EYE_FT
        if kind == "floor":
            reach = sight_miles(relief) if higher else near
        elif kind == "coast":
            reach = cap
        else:
            reach = min(cap, sight_miles(relief)) if higher else cap
        if d > reach:
            continue
        block = blocker(world, at, foot, rt, eye_ground, region_id, r["id"], painting) if d > near else None
        dirn = bearing_name(foot[0] - at[0], foot[1] - at[1])
        if higher:
            what = f"on the skyline; its ground rises to about {rt:,} feet, {relief:,} above the eye's ground, seen to {fmt_miles(reach)}"
        else:
            what = f"its ground lies no higher than the eye's, seen to {fmt_miles(reach)}"
        if block:
            hidden.append(f"- {names.name(r['id'])}, {dirn}, {fmt_miles(d)} to its nearest edge: within reach ({what.replace('on the skyline; ', '')}) but hidden behind {names.name(block)}.")
        else:
            in_view.append((d, f"- {names.name(r['id'])} ({terrain_word(r)}), {dirn}, {fmt_miles(d)} to its nearest edge: {what}."))
    for f, layer in all_features(world):
        if layer is not None:
            continue
        coords = f.get("coords") or []
        if not coords:
            continue
        if f.get("type") == "mountain":
            rt = max([parse_elevation(by_id[r][1])[1] for r in f.get("regions", []) if r in by_id] or [eye_ground])
            reach = sight_miles(rt - eye_ground) if cap is None else min(cap, sight_miles(rt - eye_ground))
        else:
            reach = near
        if f.get("shape") == "line" and len(coords) >= 2:
            d_px, along = dist_to_polyline(at, coords)
            close = reach_in_view(at, coords, reach, painting)
            seg = ""
            if close:
                (a0, a1), length = close
                seg = (f", {fmt_miles(length)} of it in view, from the {bearing_name(a0[0] - at[0], a0[1] - at[1])} "
                       f"to the {bearing_name(a1[0] - at[0], a1[1] - at[1])}")
            nearest = point_along(coords, along)
            dirn = bearing_name(nearest[0] - at[0], nearest[1] - at[1])
        elif f.get("shape") == "area" and len(coords) >= 3:
            d_px, foot = dist_to_poly_edge(at, coords)
            dirn, seg = bearing_name(foot[0] - at[0], foot[1] - at[1]), ""
        else:
            d_px = math.dist(at, coords[0])
            dirn, seg = bearing_name(coords[0][0] - at[0], coords[0][1] - at[1]), ""
        d = mi(d_px)
        if d <= reach:
            in_view.append((d, f"- {names.name(f['id'])} ({f.get('type')}), {fmt_miles(d)} {dirn}{seg}."))
        elif f.get("type") in SETTLEMENT_TYPES and f.get("shape", "point") == "point":
            p = coords[0]
            if kind == "floor":
                ok = point_in_poly(p[0], p[1], region["polygon"])
            else:
                ok = d <= cap
            if ok:
                home = [r for r in f.get("regions", []) if r in by_id and by_id[r][0] == "region"]
                tgt = parse_elevation(by_id[home[0]][1])[0] if home else eye_ground
                if not blocker(world, at, p, tgt + 30, eye_ground, region_id, home[0] if home else None, painting):
                    smoke.append((d, f"- {names.generic(f['id'])}, {fmt_miles(d)} {dirn}: its smoke, walls or lights only, not the place itself."))
    out.append("")
    out.append("In view from the point:" if in_view else "In view from the point: nothing beyond the region's own ground.")
    out += [t for _d, t in sorted(in_view, key=lambda x: x[0])]
    if smoke:
        out.append("")
        out.append("Farther off, seen only as smoke, walls or lights:")
        out += [t for _d, t in sorted(smoke, key=lambda x: x[0])]
    if hidden:
        out.append("")
        out.append("Within reach of the eye but hidden by higher ground between:")
        out += hidden
    return "\n".join(out).rstrip() + "\n"


def viewpoint(region):
    """How the god's own ground reads (map.md 1.4): floor (valley, plain and the rest), height (hill,
    highland, mountain) or coast (coast, island, sea)."""
    w = terrain_word(region)
    if w in HEIGHT_TERRAIN:
        return "height"
    if w in COAST_TERRAIN:
        return "coast"
    return "floor"


def point_along(line, t):
    """The point at distance t (painting pixels) along a polyline."""
    run = 0.0
    for i in range(len(line) - 1):
        seg = math.dist(line[i], line[i + 1])
        if run + seg >= t and seg > 0:
            u = (t - run) / seg
            return (line[i][0] + (line[i + 1][0] - line[i][0]) * u, line[i][1] + (line[i + 1][1] - line[i][1]) * u)
        run += seg
    return tuple(line[-1])


def reach_in_view(at, line, reach_mi, painting, step_mi=0.05):
    """((first point, last point), miles) of the part of a line within reach_mi of the point, sampled
    every step_mi along it; None if no part is."""
    total = polyline_length(line)
    step = step_mi / painting.mpp
    pts, length, prev = [], 0.0, None
    t = 0.0
    while t <= total + 1e-9:
        p = point_along(line, t)
        if painting.miles(math.dist(at, p)) <= reach_mi:
            if prev is not None:
                length += painting.miles(math.dist(prev, p))
            pts.append(p)
            prev = p
        else:
            prev = None
        t += step
    if len(pts) < 2:
        return None
    return (pts[0], pts[-1]), length


def blocker(world, at, target, target_top, eye_ground, own_id, target_id, painting, steps=40):
    """The id of a region between the eye and the target that stands above the sight line, or None."""
    def curve(mi_):
        return (mi_ / HORIZON_K) ** 2
    D = painting.miles(math.dist(at, target))
    if D <= 0:
        return None
    eye = eye_ground + EYE_FT
    want = (target_top - eye - curve(D)) / D
    for i in range(1, steps):
        t = i / steps
        p = (at[0] + (target[0] - at[0]) * t, at[1] + (target[1] - at[1]) * t)
        for r, _layer in all_regions(world):
            if r["id"] in (own_id, target_id) or not point_in_poly(p[0], p[1], r["polygon"]):
                continue
            d = D * t
            if (parse_elevation(r)[1] - eye - curve(d)) / d > want:
                return r["id"]
    return None


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="StarFall map tool (painted maps)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("draw", "gazetteer", "reveal", "validate", "migrate", "stamp", "describe"):
        s = sub.add_parser(name)
        s.add_argument("campaign")
        s.add_argument("--world", help="path to the sealed map.json (default: the campaign's sealed folder)")
        s.add_argument("--knowledge", help="path to map-knowledge.json (default: campaigns/<name>/player/)")
        s.add_argument("--out", help="output folder (default: campaigns/<name>/player/)")
        if name == "draw":
            s.add_argument("--paintings", help="folder holding surface.png, under-N.png and clouds.png (default: map/ beside the sealed map.json)")
            s.add_argument("--zoom", choices=["known", "landing"],
                           help="known: crop to the seen and reported ground; landing: crop to the seen regions plus a margin, at its own scale")
            s.add_argument("--layer", help="draw one sheet only: surface, or under-N")
        if name == "stamp":
            s.add_argument("--sealed", help="sealed campaign folder to stamp (default: SPOILERS_do_not_open/campaigns/<name>/)")
            s.add_argument("--dry-run", action="store_true", help="count what would be stamped; change nothing")
        if name == "describe":
            g = s.add_mutually_exclusive_group(required=True)
            g.add_argument("--landing", help="a god's label (player, or an NPC god's folder label): its landing region and point")
            g.add_argument("--region", help="a region id: described from its middle")
            s.add_argument("--god", help="with --region: whose knowledge names places (player or a label); default none")
            s.add_argument("--names", action="store_true", help="give every true name, learned or not (the Keeper's own use)")
            s.add_argument("--sealed", help="sealed campaign folder (default: SPOILERS_do_not_open/campaigns/<name>/)")
        if name == "reveal":
            g = s.add_mutually_exclusive_group(required=True)
            g.add_argument("--region")
            g.add_argument("--feature")
            s.add_argument("--grade", required=True)
            s.add_argument("--source", required=True)
            s.add_argument("--year", required=True, type=int)
            s.add_argument("--told", help="JSON: what was told (name, type, terrain, cell; coords or polygon in painting pixels for a report)")
            s.add_argument("--name", help="told.name, the name as told")
            s.add_argument("--cell", help="told.cell, the grid cell as told, like C2 (rumors need one)")
            s.add_argument("--force", help="reason, to lower a grade")
    args = ap.parse_args(argv)
    world_path, paintings_dir, knowledge_path, out_dir = campaign_paths(args)
    world = load_json(world_path)
    painting = Painting(world)
    log_path = os.path.join(out_dir, "map-log.md")

    if args.cmd == "validate":
        probs = check_world(world)
        if os.path.exists(knowledge_path):
            probs += [f"knowledge: {p}" for p in knowledge_problems(world, load_json(knowledge_path))]
        for p in probs:
            print(p)
        print(f"{len(probs)} problem(s)")
        sys.exit(1 if probs else 0)

    if args.cmd == "stamp":
        sealed = args.sealed or os.path.dirname(os.path.abspath(world_path))
        changed, total, per = stamp(args.campaign, sealed, world, dry_run=args.dry_run)
        for rel, n in per:
            print(f"{rel}: {n}")
        verb = "would stamp" if args.dry_run else "stamped"
        print(f"{verb} {total} name(s) in {changed} file(s)")
        return

    if args.cmd == "describe":
        sealed = args.sealed or os.path.dirname(os.path.abspath(world_path))
        by_id = index_world(world)
        if args.landing:
            land = (world.get("landings") or {}).get(args.landing)
            if land is None:
                sys.exit(f"map.py: no landing for {args.landing!r} in the sealed map")
            rid = land.get("region") if isinstance(land, dict) else land
            at = landing_point(land)
            kn = load_json(args.knowledge, default={"regions": {}, "features": {}}) if args.knowledge \
                else god_knowledge(args.campaign, args.landing, sealed)
            label = f"Landing of {args.landing}"
        else:
            rid, at = args.region, None
            kn = load_json(args.knowledge, default={"regions": {}, "features": {}}) if args.knowledge \
                else god_knowledge(args.campaign, args.god, sealed)
            label = f"Region {rid}"
        if rid not in by_id or by_id[rid][0] != "region":
            sys.exit(f"map.py: no region with id {rid!r} in the sealed map")
        if at is not None and not is_point(at):
            sys.exit(f"map.py: the landing point {at!r} is not an [x, y] pair of numbers")
        sys.stdout.write(describe(world, rid, at, kn, args.names, label))
        return

    knowledge = load_json(knowledge_path, default={"campaign": world.get("campaign"), "regions": {}, "features": {}})
    knowledge.setdefault("regions", {})
    knowledge.setdefault("features", {})
    if args.cmd == "migrate":
        notes = migrate(world, knowledge, painting)
        for n in notes:
            print(n)
        save_json(knowledge_path, knowledge)
        print(f"{len(notes)} change(s) to {os.path.relpath(knowledge_path, ROOT)}")
    elif args.cmd == "reveal":
        reveal(world, knowledge, knowledge_path, log_path, args)
    elif args.cmd == "draw":
        which = args.layer
        if which and which != "surface" and not which.startswith("under-"):
            sys.exit("map.py: --layer must be surface or under-N")
        for p in draw_sheets(world, paintings_dir, knowledge, out_dir, args.zoom, which):
            print(f"wrote {os.path.relpath(p, ROOT)}")
        if LAST_LABELS["dropped"]:
            print(f"labels left off for want of room (the gazetteer still lists them): {', '.join(LAST_LABELS['dropped'])}")
    elif args.cmd == "gazetteer":
        print(f"wrote {os.path.relpath(gazetteer(world, knowledge, out_dir, log_path), ROOT)}")


if __name__ == "__main__":
    main()
