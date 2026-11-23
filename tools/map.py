#!/usr/bin/env python3
"""StarFall map tool, painted-map edition. Needs Pillow. Rules: engine/rules/map.md.

  python3 tools/map.py draw <campaign> [--zoom known|landing] [--layer surface|under-N] [--if-changed]
  python3 tools/map.py gazetteer <campaign>
  python3 tools/map.py stamp <campaign> [--dry-run]    append [id] after every map name in the sealed .md files
  python3 tools/map.py describe <campaign> (--landing <god> [--reference] | --region <id> [--god <god>]) [--names] [--json]
  python3 tools/map.py travel <campaign> <from> <to> --by foot|horse|wagon|boat [--via <id>,<id>] [--god G] [--names] [--json]
  python3 tools/map.py reveal <campaign> (--region R | --feature F) --grade G --source "..." --year N
                                        [--told '<json>'] [--name N] [--cell C3] [--named] [--force "reason"]
  python3 tools/map.py validate <campaign>     check the sealed map's ids, neighbors, landings and types, and the
                                               continent's size; warn on common-word names
  python3 tools/map.py migrate <campaign>      rewrite an older knowledge file to the current rules
  python3 tools/map.py tiles <campaign>        check that the regions tile the painting: no gaps, no overlaps
  python3 tools/map.py regions-from-paint <campaign> --labels L.png --key key.json [--tolerance 1] [--layer under-N]
                                        [--save out.json] [--apply]    cut region polygons that tile the sheet

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
four letters or more; never an alias, change list 38) in every .md file of the sealed campaign folder, the rule lockcheck --places
warns by, and after every placeholder label ("unnamed town", matched in any case) that only one place
carries. A name already followed by one of its ids (after any 's or a parenthesis) is left alone, so
running it twice changes nothing. Headings and bold mystery titles are never stamped. It skips
LOCKED.md and the checker's lock-flags*.md, never touches the public folder, and prints the count per
file, then any placeholder shared by several places (left unstamped) and any common-word name.

Feature types include `site` (a marked place smaller than a hill: a shrine, a stone, a burial ground,
a ford; a point or an area, drawn as a label) and `path` (a beaten track, a line drawn like a road).
A map name that is one common word ("The Hollow", "Folds") cannot be told from prose; validate and
stamp warn on it.

The sheet labels a region only once the god has its name (change list 81): a told name, a report, or
`"named": true` on the entry, set by `reveal --named` when the name is heard or seen with the ground,
and kept when a told name's region is later seen. A region seen at landing with no name heard is
drawn unlabeled.

`draw` writes a hash of everything it reads into map-meta.json (`input_hash`); `--if-changed` keeps the
existing sheets when the hash is the same and the sheets are there (change list 86).

`validate` measures the continent from the traced land (change list 87): the largest body of land
regions that touch, its width between parallel lines taken every degree; it fails a continent whose
narrowest width is under 600 miles or whose average width lies outside 800 to 1,200 miles, and
lockcheck --places fails the lock on the same.

`travel` prices a trip (change list 93, map.md 5.1) along the route chosen with --via (roads, paths,
rivers or places, in order), segment by segment: open ground split by the regions it crosses at each
region's ground, a road at the road row, a path at the rough row, a river by boat downstream or
upstream (its coords run from source to mouth) or walked along its bank by the ground, open water by
boat at coastal sailing. A place within half a mile of a route is on it. Rates come from the quick
reference of engine/rules/time-and-pace.md (tools/pace.py for anything it lacks). Names are as the
god knows them (--god, default the player); --names gives true names and ids. The gazetteer's "Travel
by route" section and describe's neighbors use the same pricing.

`describe` writes a land description from the sealed data, for the Keeper's use: the region's terrain,
elevation, water, climate and extent, and what is in view from the landing point (or the region's
middle) by the sight rule in describe()'s docstring. With --landing the output is the seen view alone;
--reference adds every neighbor with true travel days and directions, seen or not, for the Keeper's
reference only, never for a release. With --region the neighbors are always given. Names
come from the god's knowledge file (the player's public file, or S/gods/<god>/map-knowledge.json);
anything the god has not learned is put plainly ("a river", "a hill country"), free text included.
--names gives every true name. --json gives the same reading as data. Sight crosses region borders the
same as inside a region; distances under 0.2 miles are in yards; a thing at the point has no bearing.

Coordinates may be whole pixels or tenths (one decimal) or finer; validate fails any that is not a
pair of numbers or lies off the painting.

Build 5 (run 04 change list):
- Names (39): a place shows the name the god has heard (heard_name): the Keeper's name once marked
  `"named": true`, a name the player gave it at creation (an alias by "player"), a told name (kept as
  told.name when the place is later seen), or, for a report with no other name, the Keeper's name; a
  seen place with no name heard shows none (a settlement's mark alone, no label). stamp never stamps
  aliases (38).
- describe (40): a settlement within two miles (PLAIN_VIEW_MILES) is never missed, and no region a
  settlement stands in hides it.
- travel (41, 50): a boat trip may start or end with a walk of up to BOAT_WALK_MILES to or from the
  water, priced on foot; a walk, ride or wagon trip whose straight line crosses a sea or lake goes around
  it over land (land_route); an end may be `rNN:edge` (the nearest point of a region's or an area's edge)
  or a line's `fNN:start` (source) or `fNN:end` (mouth).
- draw (42, 44, 60): the landing frame is widened so the painting is never blown up more than
  LANDING_MAX_UPSCALE times; a rumor beyond the sheet carries one direction (its told name's, if it gives
  one); with --zoom landing the god's mark is drawn at its landing point and a far sighting (a rumor with
  told.bearing, or "smoke to the north-west" from the god's own sight) is a bearing tick from it, named
  once in the footer; a region cut by the crop is labeled on its visible part, with that part's cell; a
  sea or lake region's name is kept on its water where it fits; a layer with no painting yet is not drawn.
- validate (53, 68): overlapping regions fail (and a landing point inside two regions), gaps warn; a
  world whose placement plan or history gives an underground that map.json has no layer for fails;
  layers are checked for their form (id under-N, depth, features uNN). `tiles` fails on gaps too.
  `regions-from-paint` cuts region polygons that tile the sheet from a flat-colored label painting (44).

The sealed map's regions carry elevation, water, climate and neighbors ({id, days});
the sheet carries landings (god label to region id), roads and paths (feature types, drawn
as thin lines) and a plane section, which the drawer ignores.
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
POINT_TYPES = SETTLEMENT_TYPES | {"ruin", "cave", "pass", "site"}
NATURAL_TYPES = {"river", "lake", "sea", "mountain", "pass", "forest", "marsh", "ruin", "cave"}
# A `site` is a marked place smaller than a hill that is none of the other kinds (a shrine, a standing
# stone, a burial ground, a ford, a landing place): a point, or an area, drawn as a label only.
FEATURE_TYPES = SETTLEMENT_TYPES | NATURAL_TYPES | {"road", "path", "site"}
LINE_ROUTE_TYPES = {"road", "path"}   # ground drawn as a thin line, and priced along (map.md 1.2, 5.1)
WATER_TYPES = {"river", "lake", "sea"}
DEFAULT_GRID = (5, 4)   # columns, rows
CELL_RE = re.compile(r"^([A-Z]+)([0-9]+)$")
OPAQUE_RE = re.compile(r"^[a-z][0-9]{2,4}$")
TOLD_KEYS = {"name", "terrain", "type", "cell", "coords", "polygon", "bearing"}
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
            "ruin": 52, "cave": 52, "site": 50, "road": 46, "path": 44, "rumored": 30}

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


COMPASS16 = ["north", "north-north-east", "north-east", "east-north-east", "east", "east-south-east", "south-east",
             "south-south-east", "south", "south-south-west", "south-west", "west-south-west", "west", "west-north-west",
             "north-west", "north-north-west"]
COMPASS_RE = re.compile(r"\b(" + "|".join(sorted((re.escape(c) for c in COMPASS16), key=len, reverse=True)) + r")\b", re.I)


def bearing_degrees(word):
    """Degrees clockwise from north for a compass word ("north-west", "east-north-east"), or None."""
    w = re.sub(r"\s+", "-", str(word or "").strip().lower())
    return COMPASS16.index(w) * 22.5 if w in COMPASS16 else None


def compass_in(text):
    """The compass word a told name gives ("smoke to the north-west" gives north-west), or None."""
    m = COMPASS_RE.search(str(text or ""))
    return m.group(1).lower() if m else None


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


def player_aliases(el):
    """The names the player gave a place itself (aliases `by` "player"), which count as heard (39)."""
    return [a["name"] for a in el.get("aliases") or [] if isinstance(a, dict) and a.get("by") == "player"
            and isinstance(a.get("name"), str) and a["name"].strip()]


def heard_name(el, entry):
    """The name the god has for a place (change list 39), or None when it has heard none.

    In order: the Keeper's name when the god has heard it (`"named": true`, set by `reveal --named`); a
    name the player gave the place itself at creation (an alias `by` "player"), which counts as heard;
    the name it was told (`told.name`, kept when the place is later seen); for a report that gave no
    other name, the Keeper's name (the teller named it accurately, map.md 4.2: "told, reported"); else
    none. Seeing a place gives its ground, never its name, so a seen place with no name heard has none,
    and the sheet labels it with nothing."""
    g = grade_of(entry)
    if g == "none":
        return None
    if entry.get("named"):
        return el.get("name")
    own = player_aliases(el)
    if own:
        return own[0]
    told = entry.get("told") or {}
    if told.get("name"):
        return told["name"]
    return el.get("name") if g == "reported" else None


def unnamed_feature_label(f):
    """How a seen or reported feature with no name heard is shown in the gazetteer: its id and type."""
    t = f.get("type") or "place"
    return f"{f['id']}, {'an' if t[0] in 'aeiou' else 'a'} {t}"


def known_feature(f, entry, painting=None):
    """The feature as the god knows it: told values override truth below seen; its name only as heard (39)."""
    g = grade_of(entry)
    k = {"id": f["id"], "type": f["type"], "shape": f.get("shape", "point"), "grade": g,
         "source": entry.get("source", ""), "year": entry.get("year", ""), "regions": f.get("regions", [])}
    told = entry.get("told", {}) if g != "seen" else {}
    heard = heard_name(f, entry)
    k["named"] = heard is not None
    k["name"] = heard if heard is not None else unnamed_feature_label(f)
    k["bearing"] = told.get("bearing")
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
    heard = heard_name(r, entry)
    k = {"id": r["id"], "grade": g, "source": entry.get("source", ""), "year": entry.get("year", ""),
         "name": heard if heard is not None else r["name"], "terrain": told.get("terrain", r.get("terrain", "")),
         "named": heard is not None}
    if not k["named"] and g != "none":
        k["name"] = unnamed_region_label(r)   # seen, no name heard: its id and terrain (map.md 1.2, 4.2)
    if g == "rumored":
        k["polygon"] = None
        k["near"] = rumor_near(told, r, painting)
    else:
        k["polygon"] = told.get("polygon", r["polygon"])
    return k


def unnamed_region_label(r):
    """How a region the god has seen but whose name it never heard is shown in the gazetteer, describe
    and travel: its opaque id and its terrain word ("r05, a hill country"), never its name."""
    w = terrain_word(r)
    return f"{r['id']}, the sea" if w == "sea" else f"{r['id']}, {'an' if w[0] in 'aeiou' else 'a'} {w} country"


def alias_problems(el):
    """Problems in an element's `aliases` (map.md 1.2): a list of entries, each with a non-empty `name`,
    `by` (who uses it: "player", a god's folder label, a people) and `since` (a year or a date), and
    optionally `known` (true when the player's god has heard it)."""
    if "aliases" not in el:
        return []
    al, i, probs = el["aliases"], el.get("id", "?"), []
    if not isinstance(al, list):
        return [f"{i}: aliases must be a list"]
    for n, a in enumerate(al, 1):
        if not isinstance(a, dict):
            probs.append(f"{i}: alias {n} is not an entry with name, by and since")
            continue
        if not isinstance(a.get("name"), str) or not a["name"].strip():
            probs.append(f"{i}: alias {n} has no name")
        elif a["name"].strip() == (el.get("name") or "").strip():
            probs.append(f"{i}: alias {n} is the map name itself")
        if not isinstance(a.get("by"), str) or not a["by"].strip():
            probs.append(f"{i}: alias {n} has no by (who uses it)")
        if not isinstance(a.get("since"), (str, int)) or isinstance(a.get("since"), bool) or a.get("since") == "":
            probs.append(f"{i}: alias {n} has no since (a year or a date)")
        if "known" in a and not isinstance(a["known"], bool):
            probs.append(f"{i}: alias {n}: known must be true or false")
        extra = set(a) - {"name", "by", "since", "known", "notes"}
        if extra:
            probs.append(f"{i}: alias {n} has unknown fields {', '.join(sorted(extra))}")
    return probs


def known_aliases(el):
    """The aliases the player's god has: its own (`by` "player") and any marked `"known": true`."""
    return [a["name"] for a in el.get("aliases") or [] if isinstance(a, dict) and isinstance(a.get("name"), str)
            and (a.get("by") == "player" or a.get("known") is True)]


def region_name_known(entry, el=None):
    """Whether the god has a name for the region (change lists 81 and 39): a name was told (told.name),
    the region is reported (a telling carries its name), the entry is marked `"named": true` (the
    Keeper's name heard, set by `reveal --named`), or, given the region itself, the player named it at
    creation (an alias by "player"). Ground merely seen, with no name heard, is not named, and the
    player's sheet draws no label for it."""
    if grade_of(entry) == "none":
        return False
    return heard_name(el or {}, entry) is not None


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
            if g == "seen" and set(t) - {"name"}:
                probs.append(f"{kind} {ident}: seen entries carry no told but a name heard (told.name)")
            if t.get("bearing") is not None and (g != "rumored" or bearing_degrees(t["bearing"]) is None):
                probs.append(f"{kind} {ident}: told.bearing is a compass word on a rumored sighting")
            if g == "rumored":
                if PIXEL_KEYS & set(t):
                    probs.append(f"{kind} {ident}: a rumor carries a cell, never pixels")
                if not t.get("cell") or not t.get("name"):
                    probs.append(f"{kind} {ident}: a rumor needs told.name and told.cell")
                elif Painting(world).parse_cell(t["cell"]) is None:
                    probs.append(f"{kind} {ident}: rumor cell {t['cell']!r} is not on the grid")
            if g == "reported" and "near" in t:
                probs.append(f"{kind} {ident}: `near` is not a reported shape")
            if "named" in e and not isinstance(e["named"], bool):
                probs.append(f"{kind} {ident}: named must be true or false")
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
        probs += alias_problems(el)
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
        if f.get("type") in LINE_ROUTE_TYPES and (f.get("shape") != "line" or len(f.get("coords", [])) < 2):
            probs.append(f"feature {f['id']}: a {f['type']} is a line of two or more points")
        if f.get("type") == "site" and f.get("shape", "point") not in ("point", "area"):
            probs.append(f"feature {f['id']}: a site is a point or an area")
        for rid in f.get("regions", []):
            if rid not in region_ids and rid not in seen_ids:
                probs.append(f"feature {f['id']}: region {rid} is not in the map")
    probs += layer_problems(world)
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


LAYER_ID_RE = re.compile(r"^under-[1-9][0-9]*$")
UNDER_ID_RE = re.compile(r"^u[0-9]{2,4}$")


def layer_problems(world):
    """The underground layers' form (change list 68, map.md 1.2): `layers` is a list; each layer has an
    id `under-N`, a whole-number `depth` of 1 or more that no other layer has, a `features` list whose
    ids are `uNN`, optional `regions`, and an optional `painting` file name (a layer is written before
    it is painted, and painted only if it exists). A `uNN` id on the surface is a problem too."""
    probs = []
    layers = world.get("layers", [])
    if not isinstance(layers, list):
        return ["layers: must be a list of layers"]
    depths = {}
    for n, layer in enumerate(layers, 1):
        if not isinstance(layer, dict):
            probs.append(f"layer {n}: not a layer entry")
            continue
        lid = layer.get("id")
        if not isinstance(lid, str) or not LAYER_ID_RE.match(lid):
            probs.append(f"layer {lid or n}: id must be under-N (under-1 just below the surface)")
        d = layer.get("depth")
        if not isinstance(d, int) or isinstance(d, bool) or d < 1:
            probs.append(f"layer {lid or n}: depth must be a whole number of 1 or more")
        elif d in depths:
            probs.append(f"layer {lid or n}: depth {d} is also {depths[d]}'s")
        else:
            depths[d] = lid
        if not isinstance(layer.get("features", []), list):
            probs.append(f"layer {lid or n}: features must be a list")
            continue
        if "regions" in layer and not isinstance(layer["regions"], list):
            probs.append(f"layer {lid or n}: regions must be a list")
        if "painting" in layer and not (isinstance(layer["painting"], str) and layer["painting"].strip()):
            probs.append(f"layer {lid or n}: painting must be a file name (or left out until it is painted)")
        for f in layer.get("features", []):
            fid = f.get("id") if isinstance(f, dict) else None
            if fid and not UNDER_ID_RE.match(fid):
                probs.append(f"layer {lid or n}: feature {fid} is underground, so its id is uNN (u01)")
    for f in world.get("features", []):
        if isinstance(f, dict) and UNDER_ID_RE.match(str(f.get("id", ""))):
            probs.append(f"feature {f['id']}: uNN ids are for underground features; a surface feature is fNN")
    return probs


# The files that say whether the world has an underground (change list 68): the placement plan and
# draft, the histories, and Night 1's world draft (where the 1.5 underground box is kept).
UNDERGROUND_FILES_RE = re.compile(r"^(?:placement-(?:plan|draft)|deep-history|history[\w-]*|world-draft)\.md$")
UNDER_NEG_RE = re.compile(r"\b(?:no|without|not|never|nor)\s+(?:an?\s+|any\s+)?underground\b|\bunderground\s*:\s*\**\s*(?:none|no)\b|"
                          r"\bhas none\b|\bthere is none\b", re.I)
UNDER_POS_RES = [
    re.compile(r"^\s*(?:[-*]\s+)?\**(?:the\s+)?underground\**\s*:\**\s*\S", re.I),       # "Underground: yes, ...", "The underground: ..."
    re.compile(r"^\s*[-*]\s+\[[xX]\][^\n]*\bunderground\b", re.I),                      # a ticked 1.5 box
    re.compile(r"\b(?:has|have|had|holds?|keeps?|with)\s+an?\s+(?:[\w-]+\s+){0,3}underground\b", re.I),
    re.compile(r"^\s*#{1,6}\s[^\n]*\bunderground\b", re.I),                             # a heading of its own
]


def underground_claims(sealed_dir):
    """(file, line number, line) for every line in the placement plan or a history (UNDERGROUND_FILES_RE,
    anywhere in the sealed campaign folder) that gives the world an underground. A line that says it
    has none ("no underground", "Underground: none") and an unticked box are not claims; a heading is a
    claim unless the first line under it says there is none."""
    out = []
    if not sealed_dir or not os.path.isdir(sealed_dir):
        return out
    for dirpath, dirs, files in os.walk(sealed_dir):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for fn in sorted(files):
            if not UNDERGROUND_FILES_RE.match(fn):
                continue
            path = os.path.join(dirpath, fn)
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except (OSError, UnicodeDecodeError):
                continue
            for i, line in enumerate(lines):
                if "underground" not in line.lower() or UNDER_NEG_RE.search(line):
                    continue
                if not any(rx.search(line) for rx in UNDER_POS_RES):
                    continue
                if line.lstrip().startswith("#"):
                    nxt = next((l for l in lines[i + 1:] if l.strip()), "")
                    if UNDER_NEG_RE.search(nxt):
                        continue
                out.append((os.path.relpath(path, sealed_dir), i + 1, line.strip()))
    return out


def underground_problems(world, sealed_dir):
    """validate's underground check (change list 68): a world whose placement plan or history gives an
    underground must carry it in map.json as a layer; one problem naming the files that give it."""
    if world.get("layers"):
        return []
    claims = underground_claims(sealed_dir)
    if not claims:
        return []
    where = {}
    for rel, ln, _line in claims:
        where.setdefault(rel, ln)
    return ["underground: " + ", ".join(f"{rel}:{ln}" for rel, ln in where.items()) +
            " give the world an underground, but map.json has no layer; write it as a layer (id under-N, a depth, "
            "every hollow a uNN feature) before any painting (map.md 1.2)"]


def is_point(p):
    """An [x, y] pair of finite numbers; whole pixels or tenths (one decimal) alike, any precision accepted."""
    return (isinstance(p, (list, tuple)) and len(p) == 2
            and all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in p))


def landing_point(land):
    """The landing's point in painting pixels (`at`, or `point` in older files), or None."""
    if isinstance(land, dict):
        return land.get("at", land.get("point"))
    return None


# ---------------------------------------------------------------- names: placeholders and common words

# A placeholder label stands for a place with no name yet ("unnamed town", "the nameless ford").
PLACEHOLDER_RE = re.compile(r"^(?:(?:the|an?)\s+)?(?:unnamed|nameless|un-named|no-name)\b", re.I)
# Single words too ordinary to be told apart from prose (change list 60): a map name that is one of
# these, with or without "The", cannot be stamped or scanned reliably. validate and stamp warn on it.
COMMON_WORDS = set("""
bank barrow bay beacon bend bluff bottom bridge brook burn cairn camp castle causeway cave chapel
cliff coast common corner court cove crag crest cross crossing dale dam deep dell den ditch dock down
downs drift dyke edge end fall falls farm fell fen field fields fold ford forest fork fort fountain
gap garden gate glade glen ground grove gully hall harbor harbour haven head heath height heights
hill hold hole hollow home hook hythe island isle keep knoll lake landing lea ledge lodge low marsh
mead meadow mere mill moor moss mound mount mouth narrows neck nest notch orchard pass path peak pen
pike pit place plain point pond pool port quarry quay rest ridge ring rise river road rock run scar
shelf shore shrine side slope sound spring springs spur stair stairs stand stead steps stone stones
strand stray stream street sward tarn terrace thorn tor tower town track vale valley village wall
walls ward warren wash water waters way weir well wells wharf wick wild wilds wood woods yard
north south east west middle upper lower old new far near high deep long broad
anvil ash cradle crown door eye fire hand hearth heart horn key kettle king lamp maiden mother father
mouth needle queen root seat shield sleeper spine stair tooth teeth throne tree watcher warden wheel
""".split())


def is_common_word(word):
    """A common word, or the plural of one ("Folds", "Stairs")."""
    w = word.lower()
    return w in COMMON_WORDS or (w.endswith("es") and w[:-2] in COMMON_WORDS) or (w.endswith("s") and w[:-1] in COMMON_WORDS)


def is_placeholder(name):
    """True for a placeholder label like "unnamed town" (a place the Keeper has not named)."""
    return bool(PLACEHOLDER_RE.match((name or "").strip()))


def name_core(name):
    """A name without a leading article."""
    return re.sub(r"^(?:The|the|A|An|an)\s+", "", (name or "").strip())


def is_common_word_name(name):
    """True when a map name (less any leading article) is a single common word ("The Hollow", "Ford")."""
    core = name_core(name)
    return bool(core) and " " not in core and is_common_word(core) and not is_placeholder(name)


def common_word_warnings(world):
    out = []
    for el, _layer in list(all_regions(world)) + list(all_features(world)):
        if is_common_word_name(el.get("name", "")):
            out.append(f"warning: {el.get('id', '?')} is named {el['name']!r}, a common word; stamp and lockcheck "
                       "cannot tell it from prose, so give it a proper name")
    return out


def edge_land_warnings(world):
    """Traced land that runs off the sheet: a surface land region (terrain not sea, lake or ocean)
    with a polygon point on or past the painting's border. One warning naming the edges it touches
    and, for each edge, the regions that touch it; none when all land lies inside the sheet."""
    W, H = Painting(world).size
    hits = {}
    for r in world.get("regions", []):
        if terrain_word(r) in WATER_TERRAIN or len(r.get("polygon", [])) < 3:
            continue
        xs, ys = [p[0] for p in r["polygon"]], [p[1] for p in r["polygon"]]
        for edge, hit in (("north", min(ys) <= 0.5), ("south", max(ys) >= H - 0.5),
                          ("west", min(xs) <= 0.5), ("east", max(xs) >= W - 0.5)):
            if hit:
                hits.setdefault(edge, []).append(r.get("id", "?"))
    if not hits:
        return []
    edges = [e for e in ("north", "south", "west", "east") if e in hits]
    detail = "; ".join(f"{e}: {', '.join(hits[e])}" for e in edges)
    return [f"warning: traced land runs off the sheet's {', '.join(edges)} edge(s) ({detail}); "
            "the land touches the painting border, so the sheet does not show where it ends"]


# ---------------------------------------------------------------- the continent's size (change list 87)

CONTINENT_NARROWEST_MIN = 600          # miles across at the narrowest, at least
CONTINENT_AVERAGE_RANGE = (800, 1200)  # miles across on average (about 1,000)
WATER_TERRAIN = {"sea", "lake", "ocean"}
CONTINENT_RASTER = 256                 # cells on the long side when finding which land touches which


def convex_hull(points):
    pts = sorted(set((float(p[0]), float(p[1])) for p in points))
    if len(pts) <= 2:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def continent_measure(world):
    """The continent's width from the traced land. The land is every surface region whose terrain is
    not sea or lake; the continent is the largest body of land regions that touch one another (islands
    apart from it are left out). Its width in a direction is the distance between two parallel lines
    that just hold it (a caliper laid across the whole land), taken every degree: `narrowest` is the
    least of these, `average` their mean. This is the reading Michael gave on 2026-11-21: narrowest means
    the overall shape, so a thin neck of land or a deep bay does not lower it and does not fail the
    600-mile rule. Returns a dict, or None when there is no land."""
    painting = Painting(world)
    land = [r for r in world.get("regions", []) if terrain_word(r) not in WATER_TERRAIN and len(r.get("polygon", [])) >= 3]
    if not land:
        return None
    W, H = painting.size
    k = CONTINENT_RASTER / max(W, H)
    rw, rh = max(1, round(W * k)), max(1, round(H * k))
    im = Image.new("I", (rw, rh), 0)
    d = ImageDraw.Draw(im)
    for i, r in enumerate(land, 1):
        d.polygon([(p[0] * k, p[1] * k) for p in r["polygon"]], fill=i, outline=i)
    px = im.load()
    parent = list(range(len(land) + 1))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    area = [0] * (len(land) + 1)
    for y in range(rh):
        for x in range(rw):
            v = px[x, y]
            if not v:
                continue
            area[v] += 1
            for nx, ny in ((x + 1, y), (x, y + 1)):
                if nx < rw and ny < rh:
                    u = px[nx, ny]
                    if u and u != v:
                        parent[find(u)] = find(v)
    groups = {}
    for i in range(1, len(land) + 1):
        groups.setdefault(find(i), []).append(i)
    best = max(groups.values(), key=lambda g: (sum(area[i] for i in g), len(g)))
    body = [land[i - 1] for i in best]
    pts = [(min(max(p[0], 0), W), min(max(p[1], 0), H)) for r in body for p in r["polygon"]]
    hull = convex_hull(pts)
    widths = []
    for deg in range(180):
        a = math.radians(deg)
        c, s = math.cos(a), math.sin(a)
        proj = [p[0] * c + p[1] * s for p in hull]
        widths.append((painting.miles(max(proj) - min(proj)), deg))
    narrow, ndeg = min(widths)
    x0, y0, x1, y1 = bbox(pts)
    edges = [n for n, hit in (("north", y0 <= 0.5), ("south", y1 >= H - 0.5), ("west", x0 <= 0.5), ("east", x1 >= W - 0.5)) if hit]
    return {"regions": [r["id"] for r in body], "narrowest": narrow, "narrowest_across": bearing_axis(ndeg),
            "average": sum(w for w, _ in widths) / len(widths), "widest": max(widths)[0],
            "east_west": painting.miles(x1 - x0), "north_south": painting.miles(y1 - y0),
            "land_left_out": [r["id"] for r in land if r not in body], "touches_edge": edges}


def bearing_axis(deg):
    """The line a caliper width at `deg` (0 = along x, east to west) is measured along, in words."""
    names = ["east to west", "south-east to north-west", "north to south", "south-west to north-east"]
    return names[int(((deg % 180) + 22.5) // 45) % 4]


def continent_problems(world):
    """The lock's continent check (change list 87): at least 600 miles across at the narrowest and
    800 to 1,200 miles across on average. Returns (problems, a line describing the measure)."""
    m = continent_measure(world)
    if m is None:
        return ["continent: no land regions to measure"], "continent: no land"
    lo, hi = CONTINENT_AVERAGE_RANGE
    line = (f"continent: {len(m['regions'])} land region(s), narrowest about {m['narrowest']:,.0f} miles across "
            f"({m['narrowest_across']}), average about {m['average']:,.0f} miles, widest about {m['widest']:,.0f}; "
            f"east to west {m['east_west']:,.0f}, north to south {m['north_south']:,.0f} miles")
    if m["touches_edge"]:
        line += f"; the land runs to the sheet's {', '.join(m['touches_edge'])} edge(s), measured as traced"
    if m["land_left_out"]:
        line += f"; left out as apart from it: {', '.join(m['land_left_out'])}"
    probs = []
    if m["narrowest"] < CONTINENT_NARROWEST_MIN:
        probs.append(f"continent: narrowest about {m['narrowest']:,.0f} miles across, under {CONTINENT_NARROWEST_MIN:,}")
    if not lo <= m["average"] <= hi:
        probs.append(f"continent: average about {m['average']:,.0f} miles across, outside {lo:,} to {hi:,}")
    return probs, line


# ---------------------------------------------------------------- tiling (change lists 44 and 53)

TILE_STEP = 1.0          # painting pixels between scan rows
TILE_MIN_PX2 = 0.05      # an overlap or gap smaller than this (in square pixels) is rounding, not ground


def row_intervals(poly, y):
    """The x-intervals of a polygon on the line at height y, by the even-odd rule point_in_poly uses."""
    xs = []
    n = len(poly)
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % n]
        if (y0 > y) != (y1 > y):
            xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
    xs.sort()
    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1, 2)]


def tiling_report(regions, size, painting=None, step=TILE_STEP):
    """How a set of region polygons tiles the painting, read along scan rows every `step` pixels:
    {"overlaps": {(id, id): (square pixels, cells, about how thick in pixels)}, "gaps": (square pixels, cells)}.
    Shared borders drawn on the same points overlap by nothing; a border traced twice a pixel apart is
    an overlap or a gap along its length."""
    W, H = size
    painting = painting or Painting({"painting": {"size": list(size)}})
    polys = [(r["id"], r["polygon"], bbox(r["polygon"])) for r in regions if len(r.get("polygon") or []) >= 3]
    overlaps, gap_area, gap_cells = {}, 0.0, set()
    y = step / 2 + 1e-4
    while y < H:
        ivs = []
        for rid, poly, (bx0, by0, bx1, by1) in polys:
            if by0 <= y <= by1:
                for a, b in row_intervals(poly, y):
                    a, b = max(a, 0.0), min(b, float(W))
                    if b > a:
                        ivs.append((a, b, rid))
        ivs.sort()
        for i in range(len(ivs)):
            a0, b0, r0 = ivs[i]
            for j in range(i + 1, len(ivs)):
                a1, b1, r1 = ivs[j]
                if a1 >= b0:
                    break
                if r1 == r0:
                    continue
                ov = min(b0, b1) - a1
                if ov > 1e-9:
                    key = tuple(sorted((r0, r1)))
                    area, cells, rows, xs = overlaps.get(key, (0.0, set(), set(), [float("inf"), float("-inf")]))
                    cells.add(painting.cell_of(((a1 + min(b0, b1)) / 2, y)))
                    rows.add(y)
                    xs[0], xs[1] = min(xs[0], a1), max(xs[1], min(b0, b1))
                    overlaps[key] = (area + ov * step, cells, rows, xs)
        cur = 0.0
        for a, b, _r in ivs:
            if a > cur + 1e-9:
                gap_area += (a - cur) * step
                gap_cells.add(painting.cell_of(((a + cur) / 2, y)))
            cur = max(cur, b)
        if cur < W - 1e-9:
            gap_area += (W - cur) * step
            gap_cells.add(painting.cell_of(((W + cur) / 2, y)))
        y += step
    # (square pixels, cells, about how thick in pixels: the area over the length of the box it spans)
    overlaps = {k: (v[0], v[1], v[0] / max(math.hypot(len(v[2]) * step, v[3][1] - v[3][0]), 1e-9))
                for k, v in overlaps.items() if v[0] > TILE_MIN_PX2}
    return {"overlaps": overlaps, "gaps": (gap_area, gap_cells) if gap_area > TILE_MIN_PX2 else (0.0, set())}


def tiling_lines(world, gaps_fail=False):
    """(problems, warnings) from the tiling of the surface regions and of each layer's own regions:
    overlapping regions are a problem (change list 53), and a landing point inside two regions; gaps
    in the surface are a warning from validate and a problem from the tiling check (`tiles`)."""
    painting = Painting(world)
    mpp2 = painting.mpp ** 2
    probs, warns = [], []
    sets = [("", world.get("regions", []), True)] + [(f"layer {l.get('id', '?')}: ", l.get("regions") or [], False)
                                                    for l in world.get("layers", []) if isinstance(l, dict)]
    for label, regions, full in sets:
        if not regions:
            continue
        rep = tiling_report(regions, painting.size, painting)
        for (a, b), (area, cells, width) in sorted(rep["overlaps"].items()):
            probs.append(f"{label}regions {a} and {b} overlap, about {area * mpp2:,.1f} square miles in {', '.join(sorted(cells))} "
                         f"(about {painting.miles(width):,.1f} miles thick); regions tile the painting without overlaps (map.md 1.2)")
        area, cells = rep["gaps"]
        if full and area:
            line = (f"{label}the regions leave about {area * mpp2:,.1f} square miles of the painting in no region, in "
                    f"{', '.join(sorted(cells))}; regions tile the painting without gaps, water included (map.md 1.2)")
            (probs if gaps_fail else warns).append(line if gaps_fail else "warning: " + line)
    for god, land in (world.get("landings") or {}).items():
        at = landing_point(land)
        if at is None or not is_point(at):
            continue
        inside = [r["id"] for r in world.get("regions", []) if len(r.get("polygon") or []) >= 3
                  and point_in_poly(at[0], at[1], r["polygon"])]
        if len(inside) > 1:
            probs.append(f"landing {god}: its point lies inside {len(inside)} regions ({', '.join(inside)})")
    return probs, warns


# ---------------------------------------------------------------- regions from a label painting (change list 44)

def _dp(points, tol):
    """Douglas-Peucker on an open polyline, iteratively; the ends are kept."""
    if len(points) < 3:
        return list(points)
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        i, j = stack.pop()
        a, b = points[i], points[j]
        best, idx = -1.0, None
        for k in range(i + 1, j):
            d = dist_to_polyline(points[k], [a, b])[0]
            if d > best:
                best, idx = d, k
        if idx is not None and best > tol:
            keep[idx] = True
            stack += [(i, idx), (idx, j)]
    return [p for p, k in zip(points, keep) if k]


def _drop_collinear(seq):
    out = [seq[0]]
    for i in range(1, len(seq) - 1):
        a, b, c = out[-1], seq[i], seq[i + 1]
        if (b[0] - a[0]) * (c[1] - b[1]) != (b[1] - a[1]) * (c[0] - b[0]):
            out.append(b)
    out.append(seq[-1])
    return out


def regions_from_labels(labels, tol=1.0):
    """Region polygons that tile the sheet exactly, cut from a label grid (change list 44).

    `labels` is a list of rows, each a list of region ids (or None for a pixel no region claims). Every
    unclaimed pixel goes to the region nearest it; every region is kept to its largest 4-connected part
    (smaller parts go to the region around them). Each border between two regions is traced once along
    the pixel edges and simplified once (Douglas-Peucker, `tol` pixels), and both regions take that same
    line, so neighbors share their border point for point: no gaps, no overlaps. A region with a hole
    (a lake inside a plain) is cut to the hole by a zero-width slit, so its polygon is one ring.
    Returns ({id: polygon}, notes)."""
    from collections import deque
    H = len(labels)
    W = len(labels[0]) if H else 0
    ids = sorted({v for row in labels for v in row if v is not None})
    idx = {v: i for i, v in enumerate(ids)}
    L = [[idx[v] if v is not None else -1 for v in row] for row in labels]
    notes = []
    # unclaimed pixels go to the nearest claimed one (breadth first, so ties go by scan order)
    q = deque((x, y) for y in range(H) for x in range(W) if L[y][x] >= 0)
    filled = 0
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < W and 0 <= ny < H and L[ny][nx] < 0:
                L[ny][nx] = L[y][x]
                filled += 1
                q.append((nx, ny))
    if filled:
        notes.append(f"{filled} pixel(s) no region claimed were given to the nearest region")
    # each region to its largest part; the rest to the region around it
    for _round in range(3):
        seen = [[False] * W for _ in range(H)]
        parts = {}
        for y in range(H):
            for x in range(W):
                if seen[y][x]:
                    continue
                lab, comp, dq = L[y][x], [], deque([(x, y)])
                seen[y][x] = True
                while dq:
                    cx, cy = dq.popleft()
                    comp.append((cx, cy))
                    for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                        if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx] and L[ny][nx] == lab:
                            seen[ny][nx] = True
                            dq.append((nx, ny))
                parts.setdefault(lab, []).append(comp)
        moved = 0
        for lab, comps in parts.items():
            comps.sort(key=len, reverse=True)
            for comp in comps[1:]:
                around = {}
                cs = set(comp)
                for cx, cy in comp:
                    for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                        if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in cs:
                            around[L[ny][nx]] = around.get(L[ny][nx], 0) + 1
                to = max(around, key=around.get) if around else lab
                for cx, cy in comp:
                    L[cy][cx] = to
                moved += 1
                notes.append(f"{ids[lab]}: a part of {len(comp)} pixel(s) apart from the rest was given to {ids[to]}")
        if not moved:
            break

    def lab(x, y):
        return L[y][x] if 0 <= x < W and 0 <= y < H else -1
    # directed pixel-edge borders, each region on the left of its own edges
    out_edges = {}
    for y in range(H):
        for x in range(W):
            v = L[y][x]
            for (nx, ny), (a, b) in (((x, y - 1), ((x + 1, y), (x, y))), ((x, y + 1), ((x, y + 1), (x + 1, y + 1))),
                                     ((x - 1, y), ((x, y), (x, y + 1))), ((x + 1, y), ((x + 1, y + 1), (x + 1, y)))):
                if lab(nx, ny) != v:
                    out_edges.setdefault((v, a), []).append(b)

    def corner_labels(p):
        x, y = p
        return (lab(x - 1, y - 1), lab(x, y - 1), lab(x - 1, y), lab(x, y))
    junction = {}

    def is_junction(p):
        if p not in junction:
            tl, tr, bl, br = corner_labels(p)
            junction[p] = len({tl, tr, bl, br}) >= 3 or (tl == br and tr == bl and tl != tr)
        return junction[p]
    rings = {}
    for (v, start), outs in list(out_edges.items()):
        while out_edges.get((v, start)):
            ring = [start]
            prev_dir, cur = None, start
            while True:
                choices = out_edges.get((v, cur)) or []
                if not choices:
                    break
                if prev_dir is None or len(choices) == 1:
                    nxt = choices[0]
                else:   # turn left first, so that a region touching itself at a corner keeps two rings
                    left = (prev_dir[1], -prev_dir[0])
                    pref = [left, prev_dir, (-left[0], -left[1])]
                    nxt = min(choices, key=lambda c: pref.index((c[0] - cur[0], c[1] - cur[1]))
                              if (c[0] - cur[0], c[1] - cur[1]) in pref else 9)
                choices.remove(nxt)
                prev_dir = (nxt[0] - cur[0], nxt[1] - cur[1])
                cur = nxt
                if cur == start:
                    break
                ring.append(cur)
            rings.setdefault(v, []).append(ring)
    # split rings at junctions into chains, simplify each border once, reassemble
    cache = {}

    def simplified(chain, closed=False):
        key = min(tuple(chain), tuple(reversed(chain)))
        if key not in cache:
            seq = list(key)
            if closed:
                far = max(range(len(seq)), key=lambda i: math.dist(seq[0], seq[i]))
                cache[key] = _dp(_drop_collinear(seq[:far + 1]), tol)[:-1] + _dp(_drop_collinear(seq[far:] + [seq[0]]), tol)[:-1]
            else:
                cache[key] = _dp(_drop_collinear(seq), tol)
        s = cache[key]
        return list(s) if key == tuple(chain) else list(reversed(s)) if not closed else list(s)

    polys = {}
    for v, rs in rings.items():
        done = []
        for ring in rs:
            js = [i for i, p in enumerate(ring) if is_junction(p)]
            if not js:
                # a ring with no junction (an island in one region, or a region alone): canonical start
                k = min(range(len(ring)), key=lambda i: ring[i])
                seq = ring[k:] + ring[:k]
                fwd = tuple(seq + [seq[0]])
                rev = tuple(reversed(fwd))
                canon = min(fwd, rev)
                s = simplified(list(canon[:-1]), closed=True)
                if canon != fwd:
                    s = [s[0]] + list(reversed(s[1:]))
                done.append(s)
                continue
            k = js[0]
            seq = ring[k:] + ring[:k] + [ring[k]]
            cut = [i for i, p in enumerate(seq) if is_junction(p)]
            pts = []
            for a, b in zip(cut, cut[1:]):
                part = simplified(seq[a:b + 1])
                pts += part[:-1]
            done.append(pts)
        done = [r for r in done if len(r) >= 3]
        if not done:
            continue
        done.sort(key=lambda r: abs(poly_area(r)), reverse=True)
        outer, holes = done[0], done[1:]
        for hole in holes:   # a zero-width slit from the outer ring to each hole
            bi, bj = min(((i, j) for i in range(len(outer)) for j in range(len(hole))),
                         key=lambda t: math.dist(outer[t[0]], hole[t[1]]))
            outer = outer[:bi + 1] + hole[bj:] + hole[:bj + 1] + outer[bi:]
        polys[ids[v]] = [[float(p[0]), float(p[1])] for p in outer]
    return polys, notes


def poly_area(poly):
    a = 0.0
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        a += x0 * y1 - x1 * y0
    return a / 2


def labels_from_image(path, key, size=None):
    """A label grid from a flat-colored painting of the regions: `key` maps a region id to its color
    ("#rrggbb"), or a color to an id. Pixels of any other color are left unclaimed (None)."""
    im = Image.open(path).convert("RGB")
    if size and im.size != tuple(size):
        im = im.resize(tuple(size), Image.NEAREST)
    colors = {}
    for a, b in key.items():
        rid, col = (b, a) if str(a).startswith("#") else (a, b)
        c = str(col).lstrip("#")
        colors[(int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))] = rid
    W, H = im.size
    px = im.load()
    return [[colors.get(px[x, y]) for x in range(W)] for y in range(H)]


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

    def add(self, xy, lines, priority=50, anchor="mm", marker=None, leader=False, within=None):
        """Queue a label group. lines: [(text, size, style, fill, alpha, dy)], the first the name.
        anchor "mm" centers the group on xy; "lm" sets it to the right of a marker at xy (and may
        move it to the left, above or below the marker). `within` (sheet points of a polygon) keeps
        the group inside that shape when any place inside it fits, shrinking it if need be (a narrow
        sea's name on its water, never over the coast, change list 44); if none fits it is laid
        down as any other label."""
        lines = [l for l in lines if l[0]]
        if lines:
            self.queue.append({"xy": xy, "lines": lines, "priority": priority, "anchor": anchor,
                               "order": len(self.queue), "marker": marker, "leader": leader, "within": within})

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

    @staticmethod
    def _inside(boxes, poly):
        """Every corner and edge middle of every box lies inside the polygon."""
        for b in boxes:
            for x, y in ((b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3]),
                         ((b[0] + b[2]) / 2, b[1]), ((b[0] + b[2]) / 2, b[3]), (b[0], (b[1] + b[3]) / 2), (b[2], (b[1] + b[3]) / 2)):
                if not point_in_poly(x, y, poly):
                    return False
        return True

    def _try(self, g, lines, scale, within=None):
        """Lay the group down at the first free candidate place (inside `within` when given); True if laid."""
        for i, (xy, anchor) in enumerate(self._candidates(g, lines, scale)):
            boxes, ops = self._layout(g, xy, anchor, lines, scale)
            if within and not self._inside(boxes, within):
                continue
            if self._free(boxes) and (not (g["leader"] and i) or self._leader_free(g, boxes)):
                if g["leader"] and i:
                    self._leader(g["xy"], boxes, lines[0][3])
                for p, s_, sz, style, fill, alpha, anc in ops:
                    self.text(p, s_, size=sz, style=style, fill=fill, alpha=alpha, anchor=anc)
                self.placed += boxes
                self.groups.append(boxes)
                if i or scale != 1.0 or len(lines) < len(g["lines"]):
                    self.moved += 1
                return True
        return False

    def place(self):
        """Lay down every queued group, highest priority first; returns the names dropped."""
        for g in sorted(self.queue, key=lambda g: (-g["priority"], g["order"])):
            tries = [(g["lines"], 1.0)]
            if len(g["lines"]) > 2:
                tries.append((g["lines"][:2], 1.0))
            if len(g["lines"]) > 1:
                tries.append((g["lines"][:1], 1.0))
            tries.append((g["lines"][:1], 0.8))
            # a group kept within a shape tries inside it first, smaller too, then anywhere as before
            passes = ([(g["within"], tries + [(g["lines"][:1], 0.65)])] if g.get("within") else []) + [(None, tries)]
            if not any(self._try(g, lines, scale, within) for within, ts in passes for lines, scale in ts):
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


def clip_poly_rect(poly, rect):
    """The part of a polygon inside a rectangle (x0, y0, x1, y1), by Sutherland-Hodgman."""
    x0, y0, x1, y1 = rect
    out = [tuple(p) for p in poly]
    for inside, cut in ((lambda p: p[0] >= x0, lambda a, b: (x0, a[1] + (b[1] - a[1]) * (x0 - a[0]) / (b[0] - a[0]))),
                        (lambda p: p[0] <= x1, lambda a, b: (x1, a[1] + (b[1] - a[1]) * (x1 - a[0]) / (b[0] - a[0]))),
                        (lambda p: p[1] >= y0, lambda a, b: (a[0] + (b[0] - a[0]) * (y0 - a[1]) / (b[1] - a[1]), y0)),
                        (lambda p: p[1] <= y1, lambda a, b: (a[0] + (b[0] - a[0]) * (y1 - a[1]) / (b[1] - a[1]), y1))):
        src, out = out, []
        for i in range(len(src)):
            cur, prev = src[i], src[i - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(cut(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(cut(prev, cur))
        if not out:
            return []
    return out


def pole_point(poly, n=24, rounds=3):
    """A point well inside a polygon, as far from its edges as a grid search finds (the pole of
    inaccessibility): where a label best sits in a narrow or bent shape. Falls back to the centroid."""
    x0, y0, x1, y1 = bbox(poly)
    best, bd = None, -1.0
    cx, cy, w, h = (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0
    for _ in range(rounds):
        for i in range(n + 1):
            for j in range(n + 1):
                p = (cx - w / 2 + w * i / n, cy - h / 2 + h * j / n)
                if not point_in_poly(p[0], p[1], poly):
                    continue
                d = edge_distance(p, poly)
                if d > bd:
                    best, bd = p, d
        if best is None:
            return tuple(centroid(poly))
        cx, cy, w, h = best[0], best[1], w * 2.5 / n, h * 2.5 / n
    return best


def edge_distance(p, poly):
    """The distance from p to the nearest edge of a polygon."""
    return dist_to_polyline(p, list(poly) + [poly[0]])[0]


def draw_region_labels(lab, view, regions, painting, dim=1.0):
    for k in regions:
        if k["grade"] == "rumored":
            p = k["near"]
            if view.inside(p):
                lab.add(view.pt(p), [(k["name"], 18, "italic", INK, int(150 * dim), 0)], priority=PRIORITY["rumored"])
            continue
        if not k.get("named", True):
            continue  # ground seen with no name heard: no label until the name is told or seen (81)
        poly = k["polygon"]
        water = terrain_word({"terrain": k.get("terrain", "")}) in WATER_TERRAIN
        cell_at = centroid(poly)
        shape = poly
        if not all(view.inside(p) for p in poly):
            # cut by the crop (change list 60): the label goes on the part in view, and its cell is that part's
            shape = clip_poly_rect(poly, (view.x0, view.y0, view.x1, view.y1))
            if len(shape) < 3 or abs(poly_area(shape)) < 1e-6:
                continue
            c = pole_point(shape)
            cell_at = c
        elif water:
            c = pole_point(poly)   # a narrow sea or a bent lake: on the water, never over the coast (44)
        else:
            c = centroid(poly)
            # the label sits a little above the centroid, where features cluster, if that is still inside the region
            x0, y0, x1, y1 = bbox(poly)
            lifted = (c[0], c[1] - (c[1] - y0) * 0.3)
            if point_in_poly(lifted[0], lifted[1], poly) and view.inside(lifted):
                c = lifted
        reported = k["grade"] == "reported"
        x, y = view.pt(c)
        fill = INK if not reported else INK_LIGHT
        a = int((255 if not reported else 225) * dim)
        lines = [(k["name"], 22, "regular", fill, a, -9),
                 (f"({painting.cell_of(cell_at)})", 13, "regular", fill, a, 11)]
        if reported:
            lines.append((f"reported: {k['source']}", 12, "italic", INK_LIGHT, int(210 * dim), 27))
        lab.add((x, y), lines, priority=PRIORITY["region-reported" if reported else "region"],
                within=view.pts(shape) if water else None)


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
    if t in LINE_ROUTE_TYPES:
        # the features drawn as a line (a road, a path): a thin ink trace, dashed when only reported
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
        if k["name"] and k.get("named", True):
            mid = coords[len(coords) // 2]
            if view.inside(mid):
                lab.add(view.pt(mid), [(k["name"], 11, "italic", ROAD_INK, a, 0)],
                        priority=PRIORITY[t] - (5 if reported else 0), leader=True)
        return
    if t in SETTLEMENT_TYPES:
        p = coords[0]
        if not view.inside(p):
            return
        x, y = view.pt(p)
        draw_settlement(canvas, (x, y), t, alpha=a)
        r = 8 if t == "city" else 6
        lab.obstacle((x - r, y - r, x + r, y + r))
        if not k.get("named", True):
            return   # seen with no name heard: the mark alone (39)
        size = 17 if t == "city" else (15 if t == "town" else 13)
        lines = [(k["name"], size, "regular", color, a, 0)]
        if reported:
            lines.append((f"reported: {k['source']}", 10, "italic", INK_LIGHT, a, 14))
        lab.add((x, y), lines, priority=PRIORITY[t] - (10 if reported else 0), anchor="lm", leader=True)
        return
    # a named natural feature: label only, and only once its name is heard (39)
    if not k.get("named", True):
        return
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


LANDING_MAX_UPSCALE = 3.0   # the landing frame is never blown up more than this from the painting (42)


def landing_rect(regions_k, features_k, painting, size_px=1024):
    """The landing zoom: the bounding box of the seen regions, plus a margin of a quarter of the
    box (at least LANDING_MIN_MARGIN pixels) on every side, clamped to the painting. With no
    seen region it falls back to the known zoom. A frame so small that the sheet would blow the
    painting up more than LANDING_MAX_UPSCALE times is widened about its middle (shifted to stay on
    the painting) until it is not, so the first morning's sheet stays sharp (change list 42)."""
    r = _landing_rect(regions_k, features_k, painting)
    need = min(size_px / LANDING_MAX_UPSCALE, painting.size[0], painting.size[1])
    x0, y0, x1, y1 = r
    out = []
    for lo, hi, full in ((x0, x1, painting.size[0]), (y0, y1, painting.size[1])):
        if hi - lo < need:
            c = (lo + hi) / 2
            lo, hi = c - need / 2, c + need / 2
            if lo < 0:
                lo, hi = 0, need
            if hi > full:
                lo, hi = full - need, full
        out.append((lo, hi))
    return (out[0][0], out[1][0], out[0][1], out[1][1])


def _landing_rect(regions_k, features_k, painting):
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


def beyond_notes(view, regions_k, features_k, layer_id, skip=()):
    """The footer line for rumors whose cell lies off the sheet, each with one direction (change list
    42): the direction its told name gives ("smoke to the north-west"), else the bearing from the
    sheet's middle to its cell. Rumors in `skip` (sightings drawn as ticks) are left out."""
    cx, cy = (view.x0 + view.x1) / 2, (view.y0 + view.y1) / 2
    items = [(k["name"], k["near"]) for k in regions_k.values() if k["grade"] == "rumored"]
    items += [(k["name"], k["coords"][0]) for k, lid in features_k.values()
              if lid == layer_id and k["grade"] == "rumored" and k["id"] not in skip]
    notes = [name if compass_in(name) else f"{name}, {bearing_name(p[0] - cx, p[1] - cy)}"
             for name, p in items if not view.inside(p)]
    return ["rumored, beyond this sheet: " + "; ".join(notes)] if notes else []


def sighting_bearing(k):
    """The compass bearing of a rumored feature that is a far sighting (smoke seen from where the god
    stands, change list 60): told.bearing, or the direction a told name gives when the source is the
    god's own sight ("smoke to the north-west", "own sight at the landing"). None for any other rumor."""
    if k["grade"] != "rumored":
        return None
    if bearing_degrees(k.get("bearing")) is not None:
        return str(k["bearing"]).strip().lower().replace(" ", "-")
    if "sight" in str(k.get("source", "")).lower():
        return compass_in(k["name"])
    return None


GOD_MARK_R = 7          # sheet pixels: the god's mark at the landing
TICK_FROM, TICK_TO = 11, 40   # sheet pixels from the mark: where a sighting's bearing tick starts and ends


def draw_god_mark(canvas, lab, xy, ticks):
    """The god's mark at the landing (a small four-pointed star in a ring) and, for each bearing in
    `ticks`, a short ink tick pointing from it toward what the god saw far off (change list 60)."""
    over = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    x, y = xy
    for b in sorted(set(ticks), key=bearing_degrees):
        a = math.radians(bearing_degrees(b))
        p0 = (x + math.sin(a) * TICK_FROM, y - math.cos(a) * TICK_FROM)
        p1 = (x + math.sin(a) * TICK_TO, y - math.cos(a) * TICK_TO)
        d.line([p0, p1], fill=INK + (220,), width=2)
        lab.obstacle((min(p0[0], p1[0]) - 2, min(p0[1], p1[1]) - 2, max(p0[0], p1[0]) + 2, max(p0[1], p1[1]) + 2))
    r = GOD_MARK_R
    d.ellipse([x - r - 2, y - r - 2, x + r + 2, y + r + 2], fill=PARCHMENT + (210,), outline=INK + (255,), width=1)
    star = []
    for i in range(8):
        ang = math.radians(i * 45)
        rr = r if i % 2 == 0 else r * 0.35
        star.append((x + math.sin(ang) * rr, y - math.cos(ang) * rr))
    d.polygon(star, fill=INK + (255,))
    canvas.alpha_composite(over)
    lab.obstacle((x - r - 3, y - r - 3, x + r + 3, y + r + 3))


def sighting_note(sights):
    """The footer line naming the ticks: each told name once, with how many there are."""
    counts = {}
    for k in sights:
        counts[k["name"]] = counts.get(k["name"], 0) + 1
    parts = [f"{n} ({c})" if c > 1 else n for n, c in sorted(counts.items(), key=lambda t: bearing_degrees(compass_in(t[0]) or "north") or 0)]
    return ["The star is the god where it landed; each tick points to what it saw far off: " + "; ".join(parts) + "."]


LAST_LABELS = {"dropped": [], "moved": 0}
LAST_NOTES = []   # notes from the last draw (a layer with no painting yet)


def draw_sheet(world, painting, paintings_dir, painting_file, regions, features, view, title, notes, layer_name=None,
               mark=None, ticks=()):
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
    region_names = {k["name"] for k in regions if k["grade"] != "rumored" and k.get("named", True)}
    if mark is not None and view.inside(mark):
        draw_god_mark(canvas, lab, view.pt(mark), ticks)
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


def inputs_hash(world, paintings_dir, knowledge, zoom, which):
    """A hash of everything a draw reads (change list 86): the sealed map, the knowledge file, the
    paintings, the zoom and layer asked for, and this tool's own code. map-meta.json keeps it, and
    `draw --if-changed` keeps the drawn sheets when it has not changed."""
    import hashlib
    h = hashlib.sha256()
    h.update(json.dumps(world, sort_keys=True).encode())
    h.update(json.dumps(knowledge, sort_keys=True).encode())
    h.update(f"zoom={zoom or 'full'};layer={which or 'all'}".encode())
    if os.path.isdir(paintings_dir):
        for fn in sorted(os.listdir(paintings_dir)):
            if fn.endswith(".png"):
                h.update(fn.encode())
                with open(os.path.join(paintings_dir, fn), "rb") as f:
                    h.update(hashlib.sha256(f.read()).digest())
    with open(os.path.abspath(__file__), "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def unchanged_since_last_draw(world, paintings_dir, knowledge, out_dir, zoom, which):
    """The last draw's map-meta.json when its input hash matches this draw's and its sheets are all
    still there; else None."""
    mp = os.path.join(out_dir, "map-meta.json")
    if not os.path.exists(mp):
        return None
    try:
        meta = json.load(open(mp))
    except (OSError, json.JSONDecodeError):
        return None
    if meta.get("input_hash") != inputs_hash(world, paintings_dir, knowledge, zoom, which):
        return None
    if not meta.get("files") or not all(os.path.exists(os.path.join(out_dir, f)) for f in meta["files"]):
        return None
    return meta


def draw_sheets(world, paintings_dir, knowledge, out_dir, zoom, which):
    LAST_NOTES[:] = []
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
        mark, sights = None, []
        if zoom == "landing":   # the god's mark, and far sightings as ticks from it (change list 60)
            mark = landing_point((world.get("landings") or {}).get("player"))
            if mark is not None and is_point(mark) and View(rect).inside(mark):
                sights = [k for k in feats if sighting_bearing(k)]
            else:
                mark = None
        feats = [k for k in feats if k not in sights]
        extra = sighting_note(sights) if sights else []
        view, notes = make_view(rect, legend + extra + beyond_notes(view, regions_k, features_k, None, skip={k["id"] for k in sights}))
        im = draw_sheet(world, painting, paintings_dir, "surface.png", surface_regions, feats, view, f"{name}: the god's map", notes,
                        mark=mark, ticks=[sighting_bearing(k) for k in sights])
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
        pfile = layer.get("painting", f"under-{depth}.png")
        if not os.path.exists(os.path.join(paintings_dir, pfile)):
            # a layer is written before it is painted, and painted only if it exists (change list 68)
            LAST_NOTES.append(f"layer {lid} has no painting yet ({pfile}); its sheet is not drawn, and the gazetteer lists what is known below")
            continue
        layer_regions = [regions_k[r["id"]] for r in layer.get("regions", []) if r["id"] in regions_k]
        regions = layer_regions if layer.get("regions") else surface_regions
        rect = zoom_rect(zoom, {k["id"]: k for k in regions}, features_k, lid, painting)
        view = View(rect)
        view, notes = make_view(rect, ["The ground below is fogged by what is known of the ground above it unless the layer has its own regions.",
                                       "Only known ground below is named."] + beyond_notes(view, {}, features_k, lid))
        im = draw_sheet(world, painting, paintings_dir, pfile, regions, under, view,
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
            "drawn": pacific_today(), "files": [os.path.basename(w) for w in written],
            "input_hash": inputs_hash(world, paintings_dir, knowledge, zoom, which)}
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
    truth_by_id = index_world(world)

    def hist_line(i):
        return ("; history: " + "; ".join(hist[i])) if i in hist else ""

    def alias_line(i):
        """The other names the god has for a place (92): its own, and any it has heard."""
        el = truth_by_id.get(i, (None, {}, None))[1]
        names = known_aliases(el)
        return (", also called " + ", ".join(names)) if names else ""

    lines.append("## Regions")
    lines.append("")
    for g in ("seen", "reported", "rumored"):
        for k in sorted((r for r in regions if r["grade"] == g), key=lambda r: r["name"]):
            if g == "rumored":
                lines.append(f"- **{k['name']}**{alias_line(k['id'])}, rumored, somewhere near {fmt_pt(k['near'], painting)} by the telling of {k['source']}, year {k['year']}{hist_line(k['id'])}.")
            else:
                c = centroid(k["polygon"])
                across = f", about {mi(extent_across(k['polygon'])):.0f} miles across" if g == "seen" else ""
                lines.append(f"- **{k['name']}** ({painting.cell_of(c)}){alias_line(k['id'])}, {k['terrain']}{across}, {g}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
    lines.append("")

    lines.append("## Travel between known regions")
    lines.append("")
    lines.append("Days on foot between neighboring regions the god has seen, middle to middle over open ground, priced by `tools/map.py travel` "
                 "at the pace table's rates by the ground crossed (map.md 5.1); a road or river may be quicker. Where one of the two is only reported, "
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
            grade = "seen" if k["grade"] == "seen" and other["grade"] == "seen" else "reported"
            days = None
            if grade == "seen":   # priced over open ground, never the hand-set neighbor days (93)
                a_pt = tuple(centroid(region_truth[rid]["polygon"]))
                b_pt = tuple(centroid(region_truth[nid]["polygon"]))
                days = price_trip(world, plan_trip(world, a_pt, b_pt, [], painting), "foot", pace_rates())["days"]
            pairs.append((rid, nid, days, grade))
    if not pairs:
        lines.append("No two known regions border each other.")
    for a, b, days, grade in sorted(pairs, key=lambda t: (regions_k[t[0]]["name"], regions_k[t[1]]["name"])):
        if grade == "seen":
            d = f"{fmt_days(days)} on foot over open ground" if isinstance(days, (int, float)) else "no passage on foot"
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
            lines.append(f"- **{k['name']}** ({k['type']}){alias_line(k['id'])}, {where}{', in ' + regs if regs else ''}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
        lines.append("")

    surface = [(k, l) for k, l in feats if l is None]
    place_block("Places", surface, POINT_TYPES)
    place_block("Waters, woods and ranges", surface, {"river", "lake", "sea", "mountain", "marsh", "forest"})
    place_block("Roads", surface, LINE_ROUTE_TYPES)

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

    # travel by route (change list 93): between known places on a known road or river, along it
    lines.append("## Travel by route")
    lines.append("")
    lines.append("Between known places that lie on a known road or river (within half a mile of it), measured along it as the god knows it, "
                 "at the pace table's rates for a fair summer day (`engine/rules/time-and-pace.md`); `tools/map.py travel` prices any other trip, "
                 "segment by segment, by the route chosen and the ground. A reported route may be wrong.")
    lines.append("")
    rates = pace_rates()
    trav = [k for k, l in surface if k["type"] in ROUTE_TYPES and k["grade"] != "rumored" and k["shape"] == "line" and len(k["coords"]) >= 2]
    any_route = False
    for r in sorted(trav, key=lambda k: k["name"]):
        on = []
        for p in points:
            d, t = dist_to_polyline(p["coords"][0], r["coords"])
            if mi(d) <= ON_ROUTE_MILES:
                on.append((t, p))
        on.sort(key=lambda x: x[0])
        for (t0, p), (t1, q) in zip(on, on[1:]):
            m = mi(t1 - t0)
            if m <= 0:
                continue
            grade = "seen" if r["grade"] == p["grade"] == q["grade"] == "seen" else "reported"
            if r["type"] in LINE_ROUTE_TYPES:
                row = rates["route"].get(r["type"], ROUTE_GROUND[r["type"]])
                parts = [f"{m / rates[MEANS[w]][row]:.1f} days {MEANS_WORDS[w]}" for w in ("foot", "horse", "wagon")
                         if rates[MEANS[w]].get(row)]
            else:
                parts = [f"{m / rates['boat'][g]:.1f} days by boat {word}" for g, word in (("river_down", "downstream"), ("river_up", "upstream"))
                         if rates["boat"].get(g)]
            lines.append(f"- **{p['name']}** to **{q['name']}** along **{r['name']}** ({r['type']}): {m:.0f} miles; " + ", ".join(parts) + f" ({grade}).")
            any_route = True
    if not any_route:
        lines.append("No two known places on one known road or river.")
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
    # a name once heard stays heard (change lists 81 and 39): the Keeper's name kept from the old entry or
    # set now; seeing a place never gives its name, so a told name is kept as told.name when it is seen
    if getattr(args, "named", False) or old.get("named"):
        entry["named"] = True
    if args.grade == "seen" and not entry.get("named"):
        heard = told.get("name") or old_told.get("name")
        if heard and heard == truth.get("name"):
            entry["named"] = True
        elif heard:
            entry["told"] = {"name": heard}
        elif old_grade == "reported":
            entry["named"] = True   # the report gave the Keeper's name (heard_name), and seeing keeps it
    if args.grade == "seen":
        true_c = centroid(truth.get("polygon") or truth["coords"])
        shape = old_told.get("coords") or old_told.get("polygon")
        told_cell = painting.cell_of(centroid(shape)) if shape else old_told.get("cell")
        if old_grade in ("reported", "rumored") and (shape or told_cell):
            far = painting.miles(math.dist(centroid(shape), true_c)) > 1 if shape else told_cell != painting.cell_of(true_c)
            if far:
                correction = f"; told at {told_cell} by {old.get('source', '?')}, found at {painting.cell_of(true_c)}"
        if old_told.get("name") and old_told["name"] != truth["name"] and entry.get("named"):
            # only once the Keeper's name is heard; the public log never prints a name the god lacks (39)
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
            if g == "seen" and "told" in e and set(t) - {"name"}:
                if t.get("name"):
                    e["told"] = {"name": t["name"]}   # the name heard is kept (39)
                    notes.append(f"{kind} {ident}: kept only the told name of a seen entry")
                else:
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


STAMP_NOTES = []   # notes from the last stamp (placeholder labels shared by several places, left unstamped)


def stamp_names(world):
    """{name variant: sorted ids} for every map name (with and without a leading article), kept only
    when capitalized and four letters or more, the rule lockcheck --places warns by. Aliases are never
    stamped (change list 38): an alias is often a common word that means something else in prose. A placeholder label
    ("unnamed town") is kept too, lower case and all, under the key "~" + its lower-case form, and is
    matched without regard to case; one shared by several places is left out (it cannot say which)."""
    names, holders = {}, {}
    for el, _layer in list(all_regions(world)) + list(all_features(world)):
        nm = (el.get("name") or "").strip()
        if is_placeholder(nm):
            holders.setdefault(name_core(nm).lower(), set()).add(el["id"])
            continue
        variants = {nm}   # the map name only: aliases are never stamped, and print in the gazetteer only (38)
        m = re.match(r"^(The|the|A|An)\s+(.+)$", nm)
        if m:
            variants.add(m.group(2))
        for v in variants:
            if len(v) >= 4 and v[0].isupper():
                names.setdefault(v, set()).add(el["id"])
    out = {v: sorted(ids) for v, ids in names.items()}
    for v, ids in holders.items():
        if len(ids) == 1:
            out["~" + v] = sorted(ids)
    return out


def ambiguous_placeholders(world):
    holders = {}
    for el, _layer in list(all_regions(world)) + list(all_features(world)):
        if is_placeholder(el.get("name", "")):
            holders.setdefault(name_core(el["name"]).lower(), []).append(el["id"])
    return {v: ids for v, ids in holders.items() if len(ids) > 1}


# headings and bold mystery titles are never stamped (change list 67): a title holds a name as a title
HEADING_SPAN_RE = re.compile(r"^[ \t]*#{1,6}[ \t][^\n]*|^[ \t]*\*\*[A-Z]{0,2}\d+\.\s+[^*\n]+\*\*", re.M)


def heading_spans(text):
    return [(m.start(), m.end()) for m in HEADING_SPAN_RE.finditer(text)]


def in_spans(pos, spans):
    return any(a <= pos < b for a, b in spans)


def stamp_text(text, names):
    """Append [id] after every map name in text that does not already carry one of its ids.
    Longer names win where names overlap. Headings and bold mystery titles are left alone.
    Returns (new text, number stamped)."""
    if not names:
        return text, 0
    plain = sorted((v for v in names if not v.startswith("~")), key=len, reverse=True)
    holders = sorted((v[1:] for v in names if v.startswith("~")), key=len, reverse=True)
    alts = [re.escape(v) for v in plain] + [r"(?i:" + r"\s+".join(re.escape(w) for w in v.split()) + r")" for v in holders]
    alts.sort(key=len, reverse=True)
    rx = re.compile(r"(?<![\w'\-\[])(" + "|".join(alts) + r")(?![\w\-])")
    spans = heading_spans(text)
    out, last, n = [], 0, 0
    for m in rx.finditer(text):
        if in_spans(m.start(), spans):
            continue
        key = m.group(1)
        ids = names.get(key) or names.get("~" + " ".join(key.lower().split()))
        if not ids:
            continue
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
    STAMP_NOTES[:] = [f"placeholder {v!r} names {', '.join(ids)}; not stamped, since it cannot say which"
                      for v, ids in sorted(ambiguous_placeholders(world).items())] + common_word_warnings(world)
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


# ---------------------------------------------------------------- travel (change list 93)

PACE_MD = os.path.join(ROOT, "engine", "rules", "time-and-pace.md")
MEANS = {"foot": "walk", "horse": "ride", "wagon": "oxcart", "boat": "boat"}
MEANS_WORDS = {"foot": "on foot", "horse": "on horse", "wagon": "by wagon", "boat": "by boat"}
ROUTE_TYPES = {"road", "path", "river"}
ROUTE_GROUND = {"road": "road", "path": "rough"}   # the pace row a road or path takes; the Route: line may say otherwise
ON_ROUTE_MILES = 0.5     # a place within half a mile of a route counts as on it
GROUND_WORDS = {"road": "road", "rough": "rough ground", "forest": "forest", "mountain": "mountain",
                "marsh": "marsh", "snow": "snow", "sea": "open water along a coast",
                "river_down": "river, downstream", "river_up": "river, upstream"}
PACE_LABELS = {"walk": "walk", "foot": "walk", "on foot": "walk", "ride": "ride", "riding": "ride", "horse": "ride",
               "on horse": "ride", "oxcart": "oxcart", "ox-cart": "oxcart", "ox cart": "oxcart", "wagon": "oxcart",
               "cart": "oxcart", "boat": "boat", "water": "boat", "on water": "boat"}
PACE_KEYS = {"good road": "road", "rough ground": "rough", "open ground": "rough", "coastal sail": "sea",
             "coastal sailing": "sea", "sail": "sea", "sea": "sea", "downstream": "river_down", "upstream": "river_up",
             "river downstream": "river_down", "river upstream": "river_up", "river boat downstream": "river_down",
             "river boat upstream": "river_up"}


def pace_rates(path=None):
    """Miles a day by means and ground, read from the quick reference of engine/rules/time-and-pace.md,
    the public pace table: its lines "Walk: road 20, rough 14, ...", "Ride: ...", "Oxcart: ..." (or
    "Wagon:") and "Boat: downstream 30, upstream 12, coastal sail 50, ...". Any rate the file does not
    give comes from tools/pace.py, which must match it. Its "Route:" line says which row a road or a path takes (a path
    takes the rough-ground row), kept under rates["route"]. Returns {means: {ground: miles a day},
    "route": {route type: ground}}."""
    rates = {"walk": {}, "ride": {}, "oxcart": {}, "boat": {}}
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import pace as _pace
        for m in ("walk", "ride", "oxcart"):
            rates[m].update(_pace.TRAVEL[m])
        rates["boat"].update({"river_down": _pace.TRAVEL["river_down"], "river_up": _pace.TRAVEL["river_up"],
                              "sea": _pace.TRAVEL["sail"]})
    except Exception:
        pass
    p = path or PACE_MD
    text = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    rates["route"] = dict(ROUTE_GROUND)
    for line in text.splitlines():
        rm = re.match(r"^\s*Route\s*:\s*(.+)$", line)
        if rm:   # "Route: road = road row; path = rough row; ..."
            for part in re.split(r"[;,]", rm.group(1)):
                pm = re.match(r"^\s*(road|path)\s*=\s*([a-z ]+?)\s+row\s*$", part.strip().lower())
                if pm:
                    rates["route"][pm.group(1)] = PACE_KEYS.get(pm.group(2).strip(), pm.group(2).strip())
            continue
        m = re.match(r"^\s*([A-Za-z][A-Za-z -]*?)\s*:\s*(.+)$", line)
        if not m or m.group(1).strip().lower() not in PACE_LABELS:
            continue
        means = PACE_LABELS[m.group(1).strip().lower()]
        for part in re.split(r"[,;]", m.group(2)):
            pm = re.match(r"^\s*([a-z][a-z -]*?)\s+(\d+(?:\.\d+)?)\s*$", part.strip().lower())
            if not pm:
                continue
            key = PACE_KEYS.get(pm.group(1).strip(), pm.group(1).strip().replace(" ", "_"))
            if means == "boat" and key == "swim":
                continue
            rates[means][key] = float(pm.group(2))
    return rates


def ground_of(region):
    """The pace table's ground for a region, from the first word of its terrain."""
    w = terrain_word(region) if region else "plain"
    if w in WATER_TERRAIN:
        return "sea"
    return {"forest": "forest", "mountain": "mountain", "marsh": "marsh", "snow": "snow"}.get(w, "rough")


def region_at(world, p):
    for r in world.get("regions", []):
        if point_in_poly(p[0], p[1], r["polygon"]):
            return r
    best = min(world.get("regions", []), key=lambda r: dist_to_poly_edge(p, r["polygon"])[0], default=None)
    return best


def split_by_region(world, pts, painting, step_mi=0.25):
    """[(region, miles)] along a polyline, in order, from samples every step_mi."""
    runs = []
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        L = math.dist(a, b)
        n = max(1, int(math.ceil(painting.miles(L) / step_mi)))
        for k in range(n):
            t = (k + 0.5) / n
            r = region_at(world, (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
            seg = painting.miles(L) / n
            if runs and runs[-1][0] is r:
                runs[-1][1] += seg
            else:
                runs.append([r, seg])
    return [(r, m) for r, m in runs]


def open_leg(world, a, b, painting=None):
    return {"kind": "open", "pts": [tuple(a), tuple(b)]}


def sub_line(line, t0, t1):
    """The part of a polyline between along-distances t0 and t1, in the order travelled."""
    lo, hi = min(t0, t1), max(t0, t1)
    pts = [point_along(line, lo)]
    run = 0.0
    for i in range(len(line) - 1):
        run += math.dist(line[i], line[i + 1])
        if lo < run < hi:
            pts.append(tuple(line[i + 1]))
    pts.append(point_along(line, hi))
    return pts if t1 >= t0 else list(reversed(pts))


def route_leg(feature, t0, t1, coords=None):
    return {"kind": "route", "feature": feature, "t0": t0, "t1": t1,
            "pts": sub_line(coords or feature["coords"], t0, t1)}


def closest_along(line, other):
    """The along-distance on `line` of its point nearest the polyline `other`."""
    total = polyline_length(line)
    best = (float("inf"), 0.0)
    n = max(2, int(total / 0.5))
    for i in range(n + 1):
        t = total * i / n
        d = dist_to_polyline(point_along(line, t), other)[0]
        if d < best[0]:
            best = (d, t)
    return best[1]


def plan_trip(world, a, b, vias, painting):
    """Legs from a to b through vias (route features or points), in order. Joining a route from a
    place more than half a mile off it is an open-ground leg to its nearest point; leaving it is the
    same at the far end. A trip with no route is one open-ground leg."""
    legs, cur = [], tuple(a)
    stops = list(vias) + [("point", tuple(b))]
    for i, (kind, v) in enumerate(stops[:-1]):
        if kind == "point":
            legs.append(open_leg(world, cur, v))
            cur = v
            continue
        line = v["coords"]
        nkind, nv = stops[i + 1]
        d_in, t_in = dist_to_polyline(cur, line)
        t_out = dist_to_polyline(nv, line)[1] if nkind == "point" else closest_along(line, nv["coords"])
        entry = point_along(line, t_in)
        if painting.miles(d_in) > ON_ROUTE_MILES:
            legs.append(open_leg(world, cur, entry))
        if abs(t_out - t_in) > 1e-9:
            legs.append(route_leg(v, t_in, t_out))
        cur = point_along(line, t_out)
    if not vias or painting.miles(math.dist(cur, b)) > ON_ROUTE_MILES:
        if math.dist(cur, b) > 0:
            legs.append(open_leg(world, cur, b))
    return legs


BOAT_WALK_MILES = 10.0   # a boat trip may start or end with a walk this long to or from the water, under a day (41)


def price_trip(world, legs, means, rates=None):
    """Segments with miles, ground, rate and days for the means (foot, horse, wagon, boat), each
    open-ground leg split by the regions it crosses and priced by their ground, each route leg at the
    route's rate (a road at the road rate whatever it crosses; a river by boat downstream or upstream,
    or walked along its bank by the ground). days is None when any segment has no passage.

    Change list 41: a boat trip may start with a walk to the water and end with a walk from it, each
    of up to BOAT_WALK_MILES over land, priced on foot by the ground (land between two waters is still
    no passage by boat); and an open-ground leg on land that a straight line would take across water (a
    lake, a sea) goes around it instead, by the shortest way over land the map gives (land_route)."""
    painting = Painting(world)
    rates = rates or pace_rates()
    table = rates[MEANS[means]]
    segs = []
    for li, leg in enumerate(legs):
        if leg["kind"] == "route":
            f = leg["feature"]
            t = f.get("type")
            miles = painting.miles(polyline_length(leg["pts"]))
            if t in LINE_ROUTE_TYPES and means != "boat":
                segs.append({"how": "route", "feature": f["id"], "type": t, "region": None,
                             "ground": rates.get("route", {}).get(t, ROUTE_GROUND[t]), "miles": miles})
                continue
            if t == "river" and means == "boat":
                segs.append({"how": "route", "feature": f["id"], "type": t, "region": None,
                             "ground": "river_down" if leg["t1"] >= leg["t0"] else "river_up", "miles": miles})
                continue
            if t in LINE_ROUTE_TYPES and means == "boat":
                segs.append({"how": "route", "feature": f["id"], "type": t, "region": None, "ground": "land", "miles": miles})
                continue
            for r, m in split_by_region(world, leg["pts"], painting):   # along a river's bank, by the ground
                segs.append({"how": "bank", "feature": f["id"], "type": t, "region": r["id"] if r else None,
                             "ground": ground_of(r), "miles": m})
            continue
        pts, around = leg["pts"], False
        if means != "boat":
            runs = split_by_region(world, pts, painting)
            if any(ground_of(r) == "sea" for r, _m in runs) and all(ground_of(region_at(world, q)) != "sea" for q in (pts[0], pts[-1])):
                path = land_route(world, pts[0], pts[-1], painting)
                if path:
                    pts, around = path, True
        runs = split_by_region(world, pts, painting)
        if around:
            runs = shore_runs(runs, painting)
        leg_segs = []
        for r, m in runs:
            g = ground_of(r)
            if means == "boat" and g != "sea":
                g = "land"
            leg_segs.append({"how": "open", "feature": None, "type": None, "region": r["id"] if r else None, "ground": g,
                             "miles": m, "around": around, "walk_ground": ground_of(r)})
        if means == "boat":
            walk_ends(leg_segs, first=li == 0, last=li == len(legs) - 1, has_water=any(l["kind"] == "route" for l in legs))
        segs += leg_segs
    total_days, blocked = 0.0, None
    for s in segs:
        rate = (rates["walk"] if s.get("on_foot") else table).get(s["ground"])
        s["rate"] = rate
        s["days"] = s["miles"] / rate if rate else None
        if rate is None and blocked is None:
            blocked = s
        elif rate:
            total_days += s["days"]
    return {"segments": segs, "miles": sum(s["miles"] for s in segs), "days": None if blocked else total_days,
            "blocked": blocked, "means": means}


def walk_ends(segs, first, last, has_water):
    """For a boat trip: the land at the start of the first leg and at the end of the last, up to
    BOAT_WALK_MILES each, is walked (change list 41). A leg wholly on land is walked only when the trip
    also goes by water (a route leg) and the leg is a short walk to or from it."""
    def land_run(order):
        run = []
        for i in order:
            if segs[i]["ground"] != "land":
                break
            run.append(i)
        return run
    any_water = has_water or any(s["ground"] == "sea" for s in segs)
    if not any_water:
        return
    picks = []
    if first:
        picks.append((land_run(range(len(segs))), True))
    if last:
        picks.append((land_run(range(len(segs) - 1, -1, -1)), False))
    for run, to_water in picks:
        if run and len(run) == len(segs) and not has_water:
            continue   # all land and no water on the trip: no boat trip at all
        if run and sum(segs[i]["miles"] for i in run) <= BOAT_WALK_MILES + 1e-9:
            for i in run:
                if segs[i].get("on_foot"):
                    continue
                segs[i].update({"how": "walk", "on_foot": True, "to_water": to_water, "ground": segs[i]["walk_ground"]})


def shore_runs(runs, painting):
    """A detour hugs the shore, so a sliver of water a few pixels long at a turn is the shore itself:
    it takes the ground of the land run before it (or after it)."""
    out = [[r, m] for r, m in runs]
    tiny = painting.miles(3 * land_cell(painting))
    for i, (r, m) in enumerate(out):
        if ground_of(r) == "sea" and m <= tiny:
            j = i - 1 if i > 0 else i + 1
            if 0 <= j < len(out) and ground_of(out[j][0]) != "sea":
                out[i][0] = out[j][0]
    merged = []
    for r, m in out:
        if merged and merged[-1][0] is r:
            merged[-1][1] += m
        else:
            merged.append([r, m])
    return [(r, m) for r, m in merged]


def land_cell(painting):
    """Pixels per cell of the grid land_route searches on (about 512 cells on the long side)."""
    return max(1.0, max(painting.size) / 512.0)


_LAND_GRID = {}


def water_grid(world, painting):
    """(cells, columns, rows, cell size) of the painting with every water region (sea, lake) and every
    lake or sea area feature on the surface marked as water, for land_route."""
    c = land_cell(painting)
    polys = [r["polygon"] for r in world.get("regions", []) if ground_of(r) == "sea" and len(r.get("polygon") or []) >= 3]
    polys += [f["coords"] for f in world.get("features", []) if f.get("type") in ("lake", "sea") and f.get("shape") == "area"
              and len(f.get("coords") or []) >= 3]
    key = (json.dumps(polys), painting.size, c)
    if key in _LAND_GRID:
        return _LAND_GRID[key]
    cols, rows = int(math.ceil(painting.size[0] / c)), int(math.ceil(painting.size[1] / c))
    im = Image.new("L", (cols, rows), 0)
    d = ImageDraw.Draw(im)
    for poly in polys:
        d.polygon([(p[0] / c - 0.5, p[1] / c - 0.5) for p in poly], fill=255)
    px = im.load()
    grid = [[px[x, y] > 0 for x in range(cols)] for y in range(rows)]
    _LAND_GRID.clear()
    _LAND_GRID[key] = (grid, cols, rows, c)
    return _LAND_GRID[key]


def land_route(world, a, b, painting=None):
    """The shortest way over land from a to b around water (change list 41), as points in painting
    pixels: an eight-way search on a grid of about 512 cells a side, pulled straight wherever the line
    between two of its points stays on land. None when no way over land joins them."""
    import heapq
    painting = painting or Painting(world)
    grid, cols, rows, c = water_grid(world, painting)

    def cell(p):
        return (min(cols - 1, max(0, int(p[0] / c))), min(rows - 1, max(0, int(p[1] / c))))
    s, g = cell(a), cell(b)

    def free(x, y):
        return 0 <= x < cols and 0 <= y < rows and (not grid[y][x] or (x, y) in (s, g))
    if s == g:
        return [tuple(a), tuple(b)]
    openq = [(math.dist(s, g), 0.0, s)]
    came, cost = {s: None}, {s: 0.0}
    steps = [(1, 0, 1.0), (-1, 0, 1.0), (0, 1, 1.0), (0, -1, 1.0),
             (1, 1, math.sqrt(2)), (1, -1, math.sqrt(2)), (-1, 1, math.sqrt(2)), (-1, -1, math.sqrt(2))]
    while openq:
        _f, gc, cur = heapq.heappop(openq)
        if cur == g:
            break
        if gc > cost.get(cur, float("inf")) + 1e-12:
            continue
        for dx, dy, w in steps:
            nx, ny = cur[0] + dx, cur[1] + dy
            if not free(nx, ny) or (dx and dy and not (free(cur[0] + dx, cur[1]) and free(cur[0], cur[1] + dy))):
                continue
            nc = gc + w
            if nc < cost.get((nx, ny), float("inf")):
                cost[(nx, ny)] = nc
                came[(nx, ny)] = cur
                heapq.heappush(openq, (nc + math.dist((nx, ny), g), nc, (nx, ny)))
    if g not in came:
        return None
    path = []
    cur = g
    while cur is not None:
        path.append(cur)
        cur = came[cur]
    path.reverse()
    pts = [tuple(a)] + [((x + 0.5) * c, (y + 0.5) * c) for x, y in path[1:-1]] + [tuple(b)]

    def clear(p, q):
        n = max(2, int(math.dist(p, q) / (c * 0.4)))
        for i in range(1, n):
            x = p[0] + (q[0] - p[0]) * i / n
            y = p[1] + (q[1] - p[1]) * i / n
            cx, cy = cell((x, y))
            if grid[cy][cx] and (cx, cy) not in (s, g):
                return False
        return True
    out, i = [pts[0]], 0
    while i < len(pts) - 1:
        j = i + 1
        while j + 1 < len(pts) and clear(pts[i], pts[j + 1]):
            j += 1
        out.append(pts[j])
        i = j
    return out


def fmt_days(d):
    if d is None:
        return "no passage"
    if d < 0.1:
        return f"{d:.2f} days"
    return f"{d:.1f} days"


END_FORMS = {"edge": "edge", "start": "start", "source": "start", "end": "end", "mouth": "end"}


def split_end(ident):
    """(id, form) for a trip's end written `id:edge`, `id:start` (or `:source`), `id:end` (or
    `:mouth`); (id, None) for a bare id."""
    if ":" in str(ident):
        i, form = str(ident).split(":", 1)
        f = END_FORMS.get(form.strip().lower())
        if f is None:
            sys.exit(f"map.py: {ident!r}: an end is an id, or id:edge, id:start (source) or id:end (mouth)")
        return i.strip(), f
    return ident, None


def resolve_place(world, ident, toward=None):
    """(point, how it is read) for a trip's end (change list 50): a point feature, an area feature's
    middle, a region's middle, or a god's landing point; `rNN:edge` (or an area feature's) is the point
    of its edge nearest `toward` (the trip's other end), and a line's `:start` (source) or `:end`
    (mouth) is its first or last point. A bare line is a route, not a place."""
    by_id = index_world(world)
    ident, form = split_end(ident)
    if ident in by_id:
        kind, el, layer = by_id[ident]
        if layer is not None:
            sys.exit(f"map.py: {ident} is underground; travel prices the surface")
        if form == "edge":
            ring = el.get("polygon") if kind == "region" else (el.get("coords") if el.get("shape") == "area" else None)
            if not ring or len(ring) < 3:
                sys.exit(f"map.py: {ident}:edge needs a region or an area feature")
            ref = toward if toward is not None else centroid(ring)
            foot = dist_to_polyline(ref, list(ring) + [ring[0]])
            return tuple(point_along(list(ring) + [ring[0]], foot[1])), "its nearest edge"
        if form in ("start", "end"):
            if el.get("shape") != "line" or len(el.get("coords", [])) < 2:
                sys.exit(f"map.py: {ident}:{form} needs a line (a river, a road or a path)")
            word = {"start": "source" if el.get("type") == "river" else "first point",
                    "end": "mouth" if el.get("type") == "river" else "last point"}[form]
            return tuple(el["coords"][0 if form == "start" else -1]), f"its {word}"
        if kind == "region":
            return tuple(centroid(el["polygon"])), "the middle of the region"
        if el.get("shape") == "area" and len(el.get("coords", [])) >= 3:
            return tuple(centroid(el["coords"])), "its middle"
        if el.get("shape") == "line":
            sys.exit(f"map.py: {ident} is a line ({el.get('type')}); go by it with --via, from a place, "
                     f"or name one of its ends ({ident}:start, {ident}:end)")
        return tuple(el["coords"][0]), None
    if form is None:
        land = (world.get("landings") or {}).get(ident)
        if land is not None and landing_point(land) is not None:
            return tuple(landing_point(land)), "the landing point"
    sys.exit(f"map.py: no place {ident!r} in the sealed map (a feature id, a region id or a god's landing)")


def resolve_ends(world, start, end):
    """Both ends of a trip; an edge end is read toward the other end (the other end first)."""
    if split_end(start)[1] == "edge" and split_end(end)[1] != "edge":
        b = resolve_place(world, end)
        return resolve_place(world, start, b[0]), b
    a = resolve_place(world, start)
    return a, resolve_place(world, end, a[0])


def routes_near_both(world, a, b, painting):
    out = []
    for f in world.get("features", []):
        if f.get("type") in ROUTE_TYPES and f.get("shape") == "line" and len(f.get("coords", [])) >= 2:
            if all(painting.miles(dist_to_polyline(p, f["coords"])[0]) <= ON_ROUTE_MILES for p in (a, b)):
                out.append(f)
    return out


def travel(world, start, end, means, vias=(), namer=None, show_ids=False):
    """The trip priced segment by segment (time-and-pace.md, map.md): (text, data)."""
    painting = Painting(world)
    by_id = index_world(world)
    namer = namer or Namer(world, None, True)
    if means not in MEANS:
        sys.exit(f"map.py: --by must be one of {', '.join(MEANS)}")
    (a, a_how), (b, b_how) = resolve_ends(world, start, end)
    via_items = []
    for v in vias:
        if v not in by_id:
            sys.exit(f"map.py: no feature {v!r} in the sealed map for --via")
        kind, el, _l = by_id[v]
        if kind == "feature" and el.get("shape") == "line" and len(el.get("coords", [])) >= 2:
            via_items.append(("line", el))
        else:
            via_items.append(("point", resolve_place(world, v)[0]))
    rates = pace_rates()
    trip = price_trip(world, plan_trip(world, a, b, via_items, painting), means, rates)

    def nm(i):
        return f"{namer.name(i)}{f' [{i}]' if show_ids else ''}"

    def end_nm(e):
        i = split_end(e)[0]
        return nm(i) if i in by_id else e
    head = f"Travel from {end_nm(start)}{' (' + a_how + ')' if a_how else ''} to " \
           f"{end_nm(end)}{' (' + b_how + ')' if b_how else ''}, {MEANS_WORDS[means]}"
    head += (", by " + ", then ".join(nm(v) for v in vias)) if vias else ", over open ground (no route chosen)"
    lines = [head + ":"]
    for i, s in enumerate(trip["segments"], 1):
        if s["how"] == "route":
            where = f"along {nm(s['feature'])} ({s['type']})"
        elif s["how"] == "bank":
            where = f"along the bank of {nm(s['feature'])}, through {nm(s['region'])}" if s["region"] else f"along {nm(s['feature'])}"
        elif s["how"] == "walk":
            where = f"on foot {'to' if s.get('to_water') else 'from'} the water, through {nm(s['region'])}" if s["region"] \
                else f"on foot {'to' if s.get('to_water') else 'from'} the water"
        else:
            where = f"open ground through {nm(s['region'])}" if s["region"] else "open ground"
            if s.get("around"):
                where += " (around the water)"
        ground = GROUND_WORDS.get(s["ground"], s["ground"].replace("_", " ")) if s["ground"] != "land" else "land, which a boat cannot cross"
        if s["rate"]:
            rate_words = f"{s['rate']:g} miles a day{' on foot' if s['how'] == 'walk' else ''}"
            lines.append(f"{i}. {where}, {ground}: {s['miles']:.1f} miles at {rate_words}, {fmt_days(s['days'])}.")
        else:
            lines.append(f"{i}. {where}, {ground}: {s['miles']:.1f} miles, no passage {MEANS_WORDS[means]}.")
    if trip["days"] is None:
        lines.append(f"Total: {trip['miles']:.1f} miles; no passage {MEANS_WORDS[means]} (segment {trip['segments'].index(trip['blocked']) + 1}).")
    else:
        lines.append(f"Total: {trip['miles']:.1f} miles, {fmt_days(trip['days'])} ({math.ceil(trip['days'] - 1e-9)} full days), "
                     "at the pace table's rates for a fair summer day; season, weather, load, a group and a god's endurance "
                     "adjust it (time-and-pace.md, tools/pace.py).")
    if not vias:
        near = [f for f in routes_near_both(world, a, b, painting)
                if namer.all or grade_of(namer.k.get("features", {}).get(f["id"])) in ("seen", "reported")]
        if near:
            lines.append("Routes that pass within half a mile of both ends: " + "; ".join(
                f"{nm(f['id'])} (--via {f['id']})" for f in near) + ".")
    if any(s.get("around") for s in trip["segments"]):
        lines.append("The open ground goes around water a walker cannot cross, by the shortest way the map gives "
                     "(change list 41); a ferry or a boat may be quicker.")
    data = {"from": start, "to": end, "by": means, "via": list(vias), "miles": round(trip["miles"], 2),
            "days": round(trip["days"], 3) if trip["days"] is not None else None,
            "segments": [{"how": s["how"], "route": s["feature"], "region": s["region"], "ground": s["ground"],
                          "miles": round(s["miles"], 2), "rate": s["rate"],
                          "days": round(s["days"], 3) if s["days"] is not None else None} for s in trip["segments"]]}
    if not show_ids:
        for s in data["segments"]:
            s["route"] = namer.name(s["route"]) if s["route"] else None
            s["region"] = namer.name(s["region"]) if s["region"] else None
    return "\n".join(lines) + "\n", data


# ---------------------------------------------------------------- describe

EYE_FT = 6.0               # a tall mortal's eye above the ground
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


ZERO_MILES = 0.005   # nearer than this (about nine yards) a thing is at the point itself, with no bearing (74)


def yards(mi):
    """Yards to the nearest ten, at least ten."""
    return max(10, int(round(mi * 1760 / 10.0)) * 10)


def fmt_miles(mi):
    if mi < 0.2:
        return f"{yards(mi):,} yards"   # exact yards under 0.2 miles (change list 74)
    if mi < 0.4:
        return "about a quarter mile"
    if mi < 0.75:
        return "about half a mile"
    if mi < 1.5:
        return "about a mile"
    return f"about {mi:.0f} miles"


def dist_dir(mi, dx, dy):
    """"about 2 miles north", "150 yards east", or "at the point itself" with no bearing at zero distance."""
    if mi < ZERO_MILES:
        return "at the point itself"
    return f"{fmt_miles(mi)} {bearing_name(dx, dy)}"


def bearing_or_none(mi, dx, dy):
    return None if mi < ZERO_MILES else bearing_name(dx, dy)


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
        if grade_of(e) == "none":
            return None
        # the name as heard (change list 39): seen with no name heard is shown plainly (map.md 1.2, 4.2)
        return heard_name(self.by_id[ident][1], e)

    def graded(self, ident):
        kind = self.by_id.get(ident, (None,))[0]
        table = "regions" if kind == "region" else "features"
        return grade_of(self.k.get(table, {}).get(ident)) != "none"

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
        known = self.learned(ident)
        if known:
            return known
        kind, el, _l = self.by_id[ident]
        if kind == "region" and self.graded(ident):
            return unnamed_region_label(el)
        return self.generic(ident)

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


SMOKE_MILES = SKYLINE_MILES   # a settlement's smoke, walls or lights show out to the forty-mile skyline
PLAIN_VIEW_MILES = NEAR_MILES["open"]   # within this a settlement is never missed (change list 40)


def describe(world, region_id=None, at=None, knowledge=None, all_names=False, label=None, reference=True, data=None):
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
      smoke, walls or lights only, within SMOKE_MILES (the forty-mile skyline) from any ground, and
      never past ground that stands above the line to it. A settlement in plain view, within
      PLAIN_VIEW_MILES (two miles), is never missed (change list 40): it is in view, or past the near
      distance of hill or forest ground it is given as its smoke, walls or lights with no ground
      between taken to hide it; a settlement of any shape is read at its nearest point, and no region
      it stands in hides it. Sight crosses region borders the same as it
      runs inside a region (change list 58): which region a thing stands in never hides it.
    - A mountain feature is read as the highest region it touches. Nothing underground is seen.
    - Distances under 0.2 miles are given in yards; a thing at the point itself has no bearing (74).

    With `data` (a dict), the same reading is filled in as data for `describe --json`: miles, bearings,
    grid cells and ids, with names as the god has learned them; never a pixel."""
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
    D = data if data is not None else {}
    out = []
    head = names.name(region_id)
    D.update({"label": label or "Land description", "region": {"id": region_id, "name": head, "terrain": terrain_word(region)},
              "from": "landing point" if where == "from the landing point" else "middle of the region",
              "cell": painting.cell_of(at), "neighbors": [], "in_view": [], "smoke": [], "hidden": []})
    out.append(f"{label or 'Land description'}: {head}, {where}, in grid cell {painting.cell_of(at)}.")
    out.append("")
    terrain = names.scrub(region.get("terrain", ""))
    out.append(f"The ground is {terrain}. Elevation: {names.scrub(str(region.get('elevation', 'not given')))}"
               f"{'' if figs else ' (no figure given; read as ' + str(floor) + ' to ' + str(top) + ' feet)'}. "
               f"Water: {names.ids_or_text(region.get('water', 'none given'))}. Climate: {names.scrub(str(region.get('climate', 'not given')))}.")
    x0, y0, x1, y1 = bbox(region["polygon"])
    out.append(f"The region runs about {mi(x1 - x0):.0f} miles east to west and {mi(y1 - y0):.0f} miles north to south.")
    out.append("")
    D["region"].update({"elevation_ft": [floor, top], "east_west_miles": round(mi(x1 - x0), 2), "north_south_miles": round(mi(y1 - y0), 2)})

    # neighbors
    nb_lines = []
    rates = pace_rates()
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
        edge_mi = mi(d_edge)
        walk = price_trip(world, [open_leg(world, at, foot, painting)], "foot", rates) if edge_mi >= ZERO_MILES else None
        wtxt = ""
        if walk and walk["days"] is not None:
            wtxt = f", {fmt_days(walk['days'])} on foot over open ground by the ground crossed"
        nb_lines.append(f"- {names.name(nid)} ({terrain_word(other)}), lying {bearing_name(c[0] - at[0], c[1] - at[1])}: "
                        f"{dtxt}; its nearest edge {dist_dir(edge_mi, foot[0] - at[0], foot[1] - at[1])} of the point{wtxt}."
                        .replace("its nearest edge at the point itself of the point", "its nearest edge at the point itself"))
        D["neighbors"].append({"id": nid, "name": names.name(nid), "terrain": terrain_word(other),
                               "lying": bearing_name(c[0] - at[0], c[1] - at[1]), "days": days,
                               "edge_miles": round(edge_mi, 2), "edge_bearing": bearing_or_none(edge_mi, foot[0] - at[0], foot[1] - at[1]),
                               "edge_days_on_foot": round(walk["days"], 2) if walk and walk["days"] is not None else None})
    if reference:
        out.append("Neighbors (reference for the Keeper, not the seen view):" if nb_lines else "Neighbors: none given.")
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
        dirn = bearing_or_none(d, foot[0] - at[0], foot[1] - at[1])
        loc = f"{dirn}, {fmt_miles(d)} to its nearest edge" if dirn else "its edge at the point itself"
        if higher:
            what = f"on the skyline; its ground rises to about {rt:,} feet, {relief:,} above the eye's ground, seen to {fmt_miles(reach)}"
        else:
            what = f"its ground lies no higher than the eye's, seen to {fmt_miles(reach)}"
        rec = {"id": r["id"], "name": names.name(r["id"]), "kind": "region", "terrain": terrain_word(r),
               "miles": round(d, 2), "bearing": dirn, "top_ft": rt, "reach_miles": round(reach, 2)}
        if block:
            hidden.append(f"- {names.name(r['id'])}, {loc}: within reach ({what.replace('on the skyline; ', '')}) but hidden behind {names.name(block)}.")
            D["hidden"].append({**rec, "behind": block})
        else:
            in_view.append((d, f"- {names.name(r['id'])} ({terrain_word(r)}), {loc}: {what}."))
            D["in_view"].append(rec)
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
            dxy = (nearest[0] - at[0], nearest[1] - at[1])
        elif f.get("shape") == "area" and len(coords) >= 3:
            d_px, foot = dist_to_poly_edge(at, coords)
            dxy, seg = (foot[0] - at[0], foot[1] - at[1]), ""
        else:
            d_px = math.dist(at, coords[0])
            dxy, seg = (coords[0][0] - at[0], coords[0][1] - at[1]), ""
        d = mi(d_px)
        dirn = bearing_or_none(d, *dxy)
        if d <= reach:
            on = ""
            if f.get("type") in ROUTE_TYPES and f.get("shape") == "line" and d <= ON_ROUTE_MILES:
                on = "; the point is on it"
            in_view.append((d, f"- {names.name(f['id'])} ({f.get('type')}), {dist_dir(d, *dxy)}{seg}{on}."))
            D["in_view"].append({"id": f["id"], "name": names.name(f["id"]), "kind": "feature", "type": f.get("type"),
                                 "miles": round(d, 2), "bearing": dirn, "on_it": bool(on)})
        elif f.get("type") in SETTLEMENT_TYPES:
            # a settlement of any shape, read at its nearest point (change list 40)
            p = (at[0] + dxy[0], at[1] + dxy[1])
            if d <= SMOKE_MILES:   # the same rule across a region border as inside one (change list 58)
                home = [r for r in f.get("regions", []) if r in by_id and by_id[r][0] == "region"]
                tgt = parse_elevation(by_id[home[0]][1])[0] if home else eye_ground
                # in plain view (within PLAIN_VIEW_MILES) a settlement is never missed: a region's highest
                # figure cannot stand for the ground a mile or two off; farther, no region it stands in hides it
                if d <= PLAIN_VIEW_MILES or not blocker(world, at, p, tgt + 30, eye_ground, region_id, home, painting):
                    smoke.append((d, f"- {names.generic(f['id'])}, {dist_dir(d, *dxy)}: its smoke, walls or lights only, not the place itself."))
                    D["smoke"].append({"id": f["id"], "name": names.generic(f["id"]), "miles": round(d, 2), "bearing": dirn})
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
    """The id of a region between the eye and the target that stands above the sight line, or None.
    target_id may be one region id or a list of them (a settlement on a border stands in each)."""
    skip = {own_id} | (set(target_id) if isinstance(target_id, (list, tuple, set)) else {target_id})
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
            if r["id"] in skip or not point_in_poly(p[0], p[1], r["polygon"]):
                continue
            d = D * t
            if (parse_elevation(r)[1] - eye - curve(d)) / d > want:
                return r["id"]
    return None


def regions_from_paint_cmd(world, world_path, painting, args):
    """`regions-from-paint`: region polygons cut from a flat-colored label painting so that they tile
    the sheet (change list 44), checked with the tiling check, then saved or written into the map."""
    key = load_json(args.key)
    if not isinstance(key, dict) or not key:
        sys.exit("map.py: --key must be a JSON object of region ids and colors")
    labels = labels_from_image(args.labels, key, painting.size)
    polys, notes = regions_from_labels(labels, args.tolerance)
    for n in notes:
        print(n)
    target = world.get("regions", [])
    if args.layer:
        layer = next((l for l in world.get("layers", []) if l.get("id") == args.layer), None)
        if layer is None:
            sys.exit(f"map.py: no layer {args.layer!r} in the map")
        target = layer.setdefault("regions", [])
    have = {r["id"] for r in target}
    missing = sorted(set(polys) - have)
    keyed = {(b if str(a).startswith("#") else a) for a, b in key.items()}
    for rid in sorted(keyed - set(polys)):
        print(f"{rid}: no pixel of its color in the label painting")
    probs = tiling_lines({"painting": world.get("painting", {}), "regions": [{"id": i, "polygon": p} for i, p in polys.items()]},
                         gaps_fail=True)[0]
    for p in probs:
        print(p)
    print(f"{len(polys)} region polygon(s), {sum(len(p) for p in polys.values())} points; "
          + ("they tile the painting" if not probs else f"{len(probs)} tiling problem(s)"))
    if args.save:
        save_json(args.save, polys)
        print(f"wrote {args.save}")
    if args.apply:
        if missing:
            sys.exit(f"map.py: not applied: {', '.join(missing)} not among the {'layer' if args.layer else 'surface'} regions of the map")
        for r in target:
            if r["id"] in polys:
                r["polygon"] = polys[r["id"]]
        save_json(world_path, world)
        print(f"applied to {len(polys)} region(s) in {world_path}")


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="StarFall map tool (painted maps)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("draw", "gazetteer", "reveal", "validate", "migrate", "stamp", "describe", "travel", "tiles",
                 "regions-from-paint"):
        s = sub.add_parser(name)
        s.add_argument("campaign")
        if name == "regions-from-paint":
            s.add_argument("--labels", required=True, help="a PNG of the painting's size with each region painted one flat color")
            s.add_argument("--key", required=True, help="JSON mapping each region id to its color (\"#rrggbb\"), or each color to an id")
            s.add_argument("--tolerance", type=float, default=1.0, help="how far, in pixels, a simplified border may stray (default 1)")
            s.add_argument("--layer", help="cut a layer's own regions (under-N) instead of the surface's")
            s.add_argument("--save", help="write the polygons as JSON ({id: polygon}) to this path")
            s.add_argument("--apply", action="store_true", help="write the polygons into the map file's regions of the same ids")
        if name == "travel":
            s.add_argument("start", metavar="from", help="a place: a feature id, a region id or a god's landing label; "
                                                          "or rNN:edge, a line's fNN:start (source) or fNN:end (mouth)")
            s.add_argument("end", metavar="to", help="a place, as for from")
            s.add_argument("--by", required=True, choices=sorted(MEANS), help="the means: foot, horse, wagon or boat")
            s.add_argument("--via", default="", help="the route chosen, as ids in order: roads, rivers or places (f26,f01)")
            s.add_argument("--god", default="player", help="whose knowledge names places (player or an NPC label; default player)")
            s.add_argument("--names", action="store_true", help="every true name, with ids (the Keeper's own use)")
            s.add_argument("--json", action="store_true", help="the segments as JSON")
            s.add_argument("--sealed", help="sealed campaign folder (default: SPOILERS_do_not_open/campaigns/<name>/)")
        s.add_argument("--world", help="path to the sealed map.json (default: the campaign's sealed folder)")
        s.add_argument("--knowledge", help="path to map-knowledge.json (default: campaigns/<name>/player/)")
        s.add_argument("--out", help="output folder (default: campaigns/<name>/player/)")
        if name == "draw":
            s.add_argument("--paintings", help="folder holding surface.png, under-N.png and clouds.png (default: map/ beside the sealed map.json)")
            s.add_argument("--zoom", choices=["known", "landing"],
                           help="known: crop to the seen and reported ground; landing: crop to the seen regions plus a margin, at its own scale")
            s.add_argument("--layer", help="draw one sheet only: surface, or under-N")
            s.add_argument("--if-changed", action="store_true",
                           help="keep the existing sheets when nothing the draw reads has changed since the last draw (map-meta.json's input_hash)")
        if name == "stamp":
            s.add_argument("--sealed", help="sealed campaign folder to stamp (default: SPOILERS_do_not_open/campaigns/<name>/)")
            s.add_argument("--dry-run", action="store_true", help="count what would be stamped; change nothing")
        if name == "describe":
            g = s.add_mutually_exclusive_group(required=True)
            g.add_argument("--landing", help="a god's label (player, or an NPC god's folder label): its landing region and point")
            g.add_argument("--region", help="a region id: described from its middle")
            s.add_argument("--god", help="with --region: whose knowledge names places (player or a label); default none")
            s.add_argument("--names", action="store_true", help="give every true name, learned or not (the Keeper's own use)")
            s.add_argument("--reference", action="store_true",
                           help="with --landing: also print every neighbor with true travel days and directions, seen or not (the Keeper's reference; never for a release)")
            s.add_argument("--sealed", help="sealed campaign folder (default: SPOILERS_do_not_open/campaigns/<name>/)")
            s.add_argument("--json", action="store_true", help="the same reading as JSON: miles, bearings, cells and ids, never a pixel")
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
            s.add_argument("--named", action="store_true",
                           help="the god has heard or seen the place's name with it; a seen region is labeled on the sheet only then")
    args = ap.parse_args(argv)
    world_path, paintings_dir, knowledge_path, out_dir = campaign_paths(args)
    world = load_json(world_path)
    painting = Painting(world)
    log_path = os.path.join(out_dir, "map-log.md")

    if args.cmd == "validate":
        probs = check_world(world)
        cont, cont_line = continent_problems(world)
        probs += cont
        tprobs, twarns = tiling_lines(world)   # overlapping regions fail (change list 53); gaps warn
        probs += tprobs
        probs += underground_problems(world, os.path.dirname(os.path.abspath(world_path)))   # change list 68
        if os.path.exists(knowledge_path):
            probs += [f"knowledge: {p}" for p in knowledge_problems(world, load_json(knowledge_path))]
        warns = common_word_warnings(world) + edge_land_warnings(world) + twarns
        for p in probs:
            print(p)
        for w in warns:
            print(w)
        print(cont_line)
        print(f"{len(probs)} problem(s), {len(warns)} warning(s)")
        sys.exit(1 if probs else 0)

    if args.cmd == "tiles":
        probs, _w = tiling_lines(world, gaps_fail=True)
        for p in probs:
            print(p)
        n = len(world.get("regions", []))
        print(f"{n} surface region(s): {'they tile the painting' if not probs else str(len(probs)) + ' problem(s)'}")
        sys.exit(1 if probs else 0)

    if args.cmd == "regions-from-paint":
        regions_from_paint_cmd(world, world_path, painting, args)
        return

    if args.cmd == "stamp":
        sealed = args.sealed or os.path.dirname(os.path.abspath(world_path))
        changed, total, per = stamp(args.campaign, sealed, world, dry_run=args.dry_run)
        for rel, n in per:
            print(f"{rel}: {n}")
        for note in STAMP_NOTES:
            print(note)
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
        data = {}
        text = describe(world, rid, at, kn, args.names, label, reference=bool(args.reference or not args.landing), data=data)
        if args.json:
            if not (args.reference or not args.landing):
                data.pop("neighbors", None)
            print(json.dumps(data, indent=2))
        else:
            sys.stdout.write(text)
        return

    if args.cmd == "travel":
        sealed = args.sealed or os.path.dirname(os.path.abspath(world_path))
        if args.names:
            kn = None
        elif args.knowledge:
            kn = load_json(args.knowledge, default={"regions": {}, "features": {}})
        else:
            kn = god_knowledge(args.campaign, args.god, sealed)
        vias = [v.strip() for v in args.via.split(",") if v.strip()]
        text, data = travel(world, args.start, args.end, args.by, vias, Namer(world, kn, args.names), show_ids=args.names)
        print(json.dumps(data, indent=2)) if args.json else sys.stdout.write(text)
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
        if args.if_changed:
            meta = unchanged_since_last_draw(world, paintings_dir, knowledge, out_dir, args.zoom, which)
            if meta:
                print(f"unchanged since the draw of {meta.get('drawn', '?')}; kept {', '.join(meta['files'])}")
                return
        for p in draw_sheets(world, paintings_dir, knowledge, out_dir, args.zoom, which):
            print(f"wrote {os.path.relpath(p, ROOT)}")
        if LAST_LABELS["dropped"]:
            print(f"labels left off for want of room (the gazetteer still lists them): {', '.join(LAST_LABELS['dropped'])}")
        for note in LAST_NOTES:
            print(note)
    elif args.cmd == "gazetteer":
        print(f"wrote {os.path.relpath(gazetteer(world, knowledge, out_dir, log_path), ROOT)}")


if __name__ == "__main__":
    main()
