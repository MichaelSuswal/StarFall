#!/usr/bin/env python3
"""StarFall map tool. Standard library only. Rules: engine/rules/map.md.

  python3 tools/map.py draw <campaign> [--zoom known]
  python3 tools/map.py gazetteer <campaign>
  python3 tools/map.py reveal <campaign> (--region R | --feature F) --grade G --source "..." --year N
                                        [--told '<json>'] [--force "reason"]

<campaign> is a campaign name under campaigns/. The sealed world is read from
SPOILERS_do_not_open/campaigns/<name>/map.json; the player's knowledge from
campaigns/<name>/player/map-knowledge.json. For tests and examples the three
paths can be given directly with --world, --knowledge and --out.

The tool prints nothing from the sealed file that the knowledge file does not
allow. Unknown ground is not drawn, named or hinted at.
"""
import argparse
import datetime
import json
import math
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GRADES = ["none", "rumored", "reported", "seen"]
POINT_TYPES = {"town", "ruin", "cave", "pass"}
LINE_TYPES = {"river", "road"}
AREA_TYPES = {"lake", "sea", "forest", "marsh"}

# Ink and wash.
PARCHMENT = "#efe3c4"
PARCHMENT_EDGE = "#d9c396"
INK = "#5a3a1c"
INK_LIGHT = "#8a6842"
INK_FAINT = "#a8906a"
WATER_INK = "#5a6a7a"
WATER_WASH = "#c9d3d2"
TERRAIN_WASH = {
    "plain": "#dfe2bb", "valley": "#dbe3b6", "hill": "#e3d5a8", "steppe": "#e6d9a4",
    "mountain": "#d4c7ad", "forest": "#c9cfa4", "marsh": "#cfd6c6", "desert": "#eadcae",
    "tundra": "#e4e1d0", "coast": "#dfdfc0", "highland": "#ddcfa8", "island": "#dfe2bb",
    "river": "#dbe3b6",
}


# ---------------------------------------------------------------- paths

def campaign_paths(args):
    """Resolve the world, knowledge, log and output paths."""
    name = args.campaign
    world = args.world or os.path.join(ROOT, "SPOILERS_do_not_open", "campaigns", name, "map.json")
    player = os.path.join(ROOT, "campaigns", name, "player")
    knowledge = args.knowledge or os.path.join(player, "map-knowledge.json")
    out = args.out or player
    return world, knowledge, out


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


def polygon_area(poly):
    a = 0.0
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        a += x0 * y1 - x1 * y0
    return abs(a) / 2


def extent_across(poly):
    x0, y0, x1, y1 = bbox(poly)
    return max(x1 - x0, y1 - y0)


def bearing_name(dx, dy):
    ang = math.degrees(math.atan2(dx, dy)) % 360
    names = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]
    return names[int((ang + 22.5) // 45) % 8]


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


def known_feature(f, entry):
    """The feature as the god knows it: told values override truth below seen."""
    g = grade_of(entry)
    k = {"id": f["id"], "type": f["type"], "shape": f.get("shape", "point"), "grade": g,
         "source": entry.get("source", ""), "year": entry.get("year", ""), "regions": f.get("regions", [])}
    told = entry.get("told", {}) if g != "seen" else {}
    k["name"] = told.get("name", f["name"]) if g == "reported" else (told.get("name", f["name"]) if g == "rumored" else f["name"])
    k["type"] = told.get("type", f["type"])
    if g == "seen":
        k["coords"] = f["coords"]
    elif g == "reported":
        k["coords"] = told.get("coords", f["coords"])
    else:
        k["coords"] = [told["near"]] if "near" in told else [list(centroid(f["coords"]))]
    k["shape"] = f.get("shape", "point") if g != "rumored" else "point"
    if k["shape"] == "line" and len(k["coords"]) < 2:
        k["shape"] = "point"
    return k


def known_region(r, entry):
    g = grade_of(entry)
    told = entry.get("told", {}) if g != "seen" else {}
    k = {"id": r["id"], "grade": g, "source": entry.get("source", ""), "year": entry.get("year", ""),
         "name": told.get("name", r["name"]), "terrain": told.get("terrain", r["terrain"])}
    if g == "rumored":
        k["polygon"] = None
        k["near"] = told.get("near", list(centroid(r["polygon"])))
    else:
        k["polygon"] = told.get("polygon", r["polygon"])
    return k


# ---------------------------------------------------------------- svg helpers

def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


class Sheet:
    """Builds one SVG. Converts miles to pixels, y up in miles, y down on the page."""

    def __init__(self, frame, width_px=1400, pad=60):
        self.fx0, self.fy0, self.fx1, self.fy1 = frame
        fw = max(self.fx1 - self.fx0, 1e-6)
        fh = max(self.fy1 - self.fy0, 1e-6)
        self.pad = pad
        self.scale = (width_px - 2 * pad) / fw
        self.w = width_px
        self.h = int(fh * self.scale + 2 * pad)
        self.parts = []
        self.defs = []
        self.nclip = 0

    def px(self, p):
        return (self.pad + (p[0] - self.fx0) * self.scale, self.pad + (self.fy1 - p[1]) * self.scale)

    def pts(self, coords):
        return " ".join(f"{x:.1f},{y:.1f}" for x, y in (self.px(c) for c in coords))

    def add(self, s):
        self.parts.append(s)

    def clip(self, coords):
        self.nclip += 1
        cid = f"clip{self.nclip}"
        self.defs.append(f'<clipPath id="{cid}"><polygon points="{self.pts(coords)}"/></clipPath>')
        return cid

    def text(self, p, s, size=12, italic=False, color=INK, anchor="middle", opacity=1.0, caps=False, dy=0, dx=0, weight="normal"):
        x, y = self.px(p)
        x += dx
        style = f"font-family:Georgia,'Times New Roman',serif;font-size:{size}px;"
        if italic:
            style += "font-style:italic;"
        if caps:
            style += "font-variant:small-caps;letter-spacing:1px;"
        if weight != "normal":
            style += f"font-weight:{weight};"
        self.add(f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" fill="{color}" opacity="{opacity}" style="{style}">{esc(s)}</text>')

    def wavy_path(self, coords, rng, amp=1.6, seg=14.0, close=False):
        """A path through pixel points with a gentle hand-drawn waver."""
        pp = [self.px(c) for c in coords]
        if close:
            pp.append(pp[0])
        out = []
        for i in range(len(pp) - 1):
            (x0, y0), (x1, y1) = pp[i], pp[i + 1]
            d = math.hypot(x1 - x0, y1 - y0)
            n = max(1, int(d / seg))
            nx, ny = (-(y1 - y0) / d, (x1 - x0) / d) if d else (0, 0)
            for k in range(n):
                t0, t1 = k / n, (k + 1) / n
                mx = x0 + (x1 - x0) * (t0 + t1) / 2
                my = y0 + (y1 - y0) * (t0 + t1) / 2
                off = rng.uniform(-amp, amp)
                ex, ey = x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1
                if i == 0 and k == 0:
                    out.append(f"M{x0:.1f},{y0:.1f}")
                out.append(f"Q{mx + nx * off:.1f},{my + ny * off:.1f} {ex:.1f},{ey:.1f}")
        return " ".join(out)

    def render(self, title, note_lines):
        g = ('<radialGradient id="parch" cx="50%" cy="50%" r="75%">'
             f'<stop offset="0" stop-color="{PARCHMENT}"/><stop offset="0.8" stop-color="{PARCHMENT}"/>'
             f'<stop offset="1" stop-color="{PARCHMENT_EDGE}"/></radialGradient>')
        inner_x, inner_y = self.pad - 8, self.pad - 8
        inner_w, inner_h = self.w - 2 * self.pad + 16, self.h - 2 * self.pad + 16
        frame_clip = f'<clipPath id="frame"><rect x="{inner_x}" y="{inner_y}" width="{inner_w}" height="{inner_h}"/></clipPath>'
        head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">',
                f"<title>{esc(title)}</title>", "<defs>", g, frame_clip, *self.defs, "</defs>",
                f'<rect width="{self.w}" height="{self.h}" fill="url(#parch)"/>',
                f'<rect x="{self.pad - 12}" y="{self.pad - 12}" width="{self.w - 2 * self.pad + 24}" height="{self.h - 2 * self.pad + 24}" '
                f'fill="none" stroke="{INK}" stroke-width="1.6"/>',
                f'<rect x="{inner_x}" y="{inner_y}" width="{inner_w}" height="{inner_h}" fill="none" stroke="{INK_LIGHT}" stroke-width="0.6"/>']
        body = ['<g clip-path="url(#frame)">', *self.parts, "</g>"]
        tail = []
        y = self.h - self.pad + 28
        for line in note_lines:
            tail.append(f'<text x="{self.pad}" y="{y}" fill="{INK_LIGHT}" style="font-family:Georgia,serif;font-size:11px;font-style:italic">{esc(line)}</text>')
            y += 14
        tail.append("</svg>")
        return "\n".join(head + body + tail)


# ---------------------------------------------------------------- drawing

def terrain_kind(terrain):
    """The first word of the terrain, letters only: 'hill, sheep country' gives 'hill'."""
    word = (terrain or "").strip().split()[0].lower() if (terrain or "").strip() else ""
    return "".join(ch for ch in word if ch.isalpha())


def terrain_wash(terrain):
    return TERRAIN_WASH.get(terrain_kind(terrain), "#e3dcbb")


def grid_points(poly, step, rng, jitter=0.35):
    x0, y0, x1, y1 = bbox(poly)
    pts = []
    row = 0
    y = y0 + step / 2
    while y < y1:
        x = x0 + step / 2 + (step / 2 if row % 2 else 0)
        while x < x1:
            jx, jy = x + rng.uniform(-jitter, jitter) * step, y + rng.uniform(-jitter, jitter) * step
            if point_in_poly(jx, jy, poly):
                pts.append((jx, jy))
            x += step
        y += step
        row += 1
    return pts


def draw_mountain_mark(sh, p, size_px, rng, color=INK, opacity=1.0):
    x, y = sh.px(p)
    w = size_px * rng.uniform(0.8, 1.2)
    h = size_px * rng.uniform(0.9, 1.4)
    apex = (x + rng.uniform(-0.15, 0.15) * w, y - h)
    sh.add(f'<path d="M{x - w / 2:.1f},{y:.1f} L{apex[0]:.1f},{apex[1]:.1f} L{x + w / 2:.1f},{y:.1f}" fill="none" '
           f'stroke="{color}" stroke-width="0.9" stroke-linejoin="round" opacity="{opacity}"/>')
    # shade the south-east face
    sh.add(f'<path d="M{apex[0]:.1f},{apex[1]:.1f} L{x + w / 2:.1f},{y:.1f} L{apex[0] + w * 0.18:.1f},{y:.1f} Z" '
           f'fill="{color}" opacity="{0.35 * opacity:.2f}"/>')


def draw_tree_mark(sh, p, size_px, rng, color=INK, opacity=0.9):
    x, y = sh.px(p)
    r = size_px * rng.uniform(0.7, 1.1)
    sh.add(f'<circle cx="{x:.1f}" cy="{y - r:.1f}" r="{r:.1f}" fill="none" stroke="{color}" stroke-width="0.8" opacity="{opacity}"/>')
    sh.add(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y + r * 0.9:.1f}" stroke="{color}" stroke-width="0.8" opacity="{opacity}"/>')


def draw_marsh_mark(sh, p, size_px, color=INK_LIGHT, opacity=0.9):
    x, y = sh.px(p)
    s = size_px
    sh.add(f'<path d="M{x - s:.1f},{y:.1f} h{2 * s:.1f} M{x - s * 0.6:.1f},{y + 3:.1f} h{1.2 * s:.1f} M{x - s * 0.3:.1f},{y - 3:.1f} h{0.6 * s:.1f}" '
           f'stroke="{color}" stroke-width="0.8" opacity="{opacity}"/>')


def draw_waves(sh, poly, rng, color=WATER_INK, spacing_mi=None):
    cid = sh.clip(poly)
    x0, y0, x1, y1 = bbox(poly)
    span = max(x1 - x0, y1 - y0)
    spacing = spacing_mi or max(span / 9, 2.5)
    y = y0 + spacing / 2
    while y < y1:
        pts = []
        x = x0
        phase = rng.uniform(0, math.pi * 2)
        while x <= x1 + spacing:
            pts.append((x, y + math.sin(x / (spacing * 0.9) + phase) * spacing * 0.12))
            x += spacing / 3
        d = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in (sh.px(p) for p in pts))
        sh.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="0.7" opacity="0.7" clip-path="url(#{cid})"/>')
        y += spacing


def draw_region(sh, k, rng):
    """A seen or reported region: wash, outline, terrain texture, label."""
    poly = k["polygon"]
    reported = k["grade"] == "reported"
    wash = terrain_wash(k["terrain"])
    op = 0.55 if reported else 0.85
    sh.add(f'<polygon points="{sh.pts(poly)}" fill="{wash}" opacity="{op}"/>')
    sh.add(f'<path d="{sh.wavy_path(poly, rng, amp=1.0, close=True)}" fill="none" stroke="{INK}" '
           f'stroke-width="{0.8 if reported else 1.2}" stroke-dasharray="{"4 3" if reported else "none"}" stroke-linejoin="round"/>')
    first = terrain_kind(k["terrain"])
    tex_op = 0.5 if reported else 0.9
    if first in ("mountain", "highland"):
        for p in grid_points(poly, extent_across(poly) / 7, rng):
            draw_mountain_mark(sh, p, 9 if first == "mountain" else 6, rng, opacity=tex_op)
    elif first == "hill":
        for p in grid_points(poly, extent_across(poly) / 6, rng):
            x, y = sh.px(p)
            w = 9 * rng.uniform(0.8, 1.2)
            sh.add(f'<path d="M{x - w:.1f},{y:.1f} Q{x:.1f},{y - w * 0.8:.1f} {x + w:.1f},{y:.1f}" fill="none" stroke="{INK}" stroke-width="0.9" opacity="{tex_op}"/>')
            sh.add(f'<path d="M{x - w * 0.3:.1f},{y:.1f} Q{x + w * 0.3:.1f},{y - w * 0.5:.1f} {x + w:.1f},{y:.1f}" fill="none" stroke="{INK}" stroke-width="0.6" opacity="{tex_op * 0.7:.2f}"/>')
    elif first == "forest":
        for p in grid_points(poly, extent_across(poly) / 9, rng):
            draw_tree_mark(sh, p, 3.5, rng, opacity=tex_op)
    elif first == "marsh":
        for p in grid_points(poly, extent_across(poly) / 8, rng):
            draw_marsh_mark(sh, p, 5, opacity=tex_op)
    elif first in ("plain", "steppe", "valley"):
        for p in grid_points(poly, extent_across(poly) / 5, rng, jitter=0.45):
            x, y = sh.px(p)
            sh.add(f'<path d="M{x - 3:.1f},{y:.1f} h6" stroke="{INK_FAINT}" stroke-width="0.6" opacity="{tex_op * 0.6:.2f}"/>')
    elif first == "desert":
        for p in grid_points(poly, extent_across(poly) / 8, rng, jitter=0.45):
            x, y = sh.px(p)
            sh.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="0.7" fill="{INK_FAINT}" opacity="{tex_op}"/>')
    # the region's name runs along the top of its ground, leaving the middle for features
    c = centroid(poly)
    x0, y0, x1, y1 = bbox(poly)
    lab = (c[0], y1 - (y1 - y0) * 0.12)
    size = 15 if not reported else 13
    sh.text(lab, k["name"], size=size, caps=True, color=INK if not reported else INK_LIGHT, dy=-2)
    sh.text(lab, k["terrain"], size=9, italic=True, color=INK_LIGHT, dy=11)
    if reported:
        sh.text(lab, f"reported: {k['source']}", size=8.5, italic=True, color=INK_FAINT, dy=22)


def draw_rumored_region(sh, k):
    sh.text(k["near"], k["name"], size=12, italic=True, color=INK, opacity=0.4, dy=0)
    sh.text(k["near"], f"rumor, {k['source']}", size=8, italic=True, color=INK, opacity=0.4, dy=11)


def draw_feature(sh, k, rng, dim=1.0):
    """A known feature by its grade. dim < 1 draws it faintly (surface under an underground sheet)."""
    g = k["grade"]
    t = k["type"]
    coords = k["coords"]
    if g == "rumored":
        sh.text(coords[0], k["name"], size=10.5, italic=True, color=INK, opacity=0.4 * dim)
        sh.text(coords[0], f"rumor, {k['source']}", size=7.5, italic=True, color=INK, opacity=0.4 * dim, dy=10)
        return
    reported = g == "reported"
    op = (0.7 if reported else 1.0) * dim
    label_color = INK_LIGHT if reported else INK
    if k["shape"] == "line" and len(coords) >= 2:
        if t == "river":
            # widen toward the mouth (the last point)
            n = len(coords)
            for i in range(n - 1):
                w = 1.0 + 2.2 * (i + 1) / n
                d = sh.wavy_path(coords[i:i + 2], rng, amp=1.3, seg=12)
                sh.add(f'<path d="{d}" fill="none" stroke="{WATER_INK}" stroke-width="{w:.1f}" opacity="{op}" stroke-linecap="round"/>')
            mid = coords[len(coords) // 2]
            sh.text(mid, k["name"], size=10.5, italic=True, color=WATER_INK, opacity=op, dy=-6)
        elif t == "road":
            d = sh.wavy_path(coords, rng, amp=0.8)
            sh.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.1" stroke-dasharray="5 3" opacity="{op}"/>')
            mid = coords[len(coords) // 2]
            sh.text(mid, k["name"], size=9.5, italic=True, color=label_color, opacity=op, dy=-5)
        elif t == "mountain":
            # a range: chevrons along the line, two rows
            total = polyline_length(coords)
            step = max(total / 14, 2.0)
            d = 0.0
            marks = []
            for i in range(len(coords) - 1):
                (x0, y0), (x1, y1) = coords[i], coords[i + 1]
                seg = math.dist(coords[i], coords[i + 1])
                nx, ny = (-(y1 - y0) / seg, (x1 - x0) / seg) if seg else (0, 0)
                while d <= seg:
                    tt = d / seg if seg else 0
                    bx, by = x0 + (x1 - x0) * tt, y0 + (y1 - y0) * tt
                    marks.append((bx, by))
                    marks.append((bx + nx * step * 0.8, by + ny * step * 0.8))
                    marks.append((bx - nx * step * 0.6, by - ny * step * 0.6))
                    d += step
                d -= seg
            for p in marks:
                draw_mountain_mark(sh, p, 10, rng, opacity=op)
            mid = coords[len(coords) // 2]
            sh.text(mid, k["name"], size=11, caps=True, color=label_color, opacity=op, dy=-16)
        else:
            # a cave gallery or any other line: a double hairline, as passages are drawn on mine charts
            d = sh.wavy_path(coords, rng, amp=1.0)
            sh.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.6" opacity="{op}"/>')
            sh.add(f'<path d="{d}" fill="none" stroke="{PARCHMENT}" stroke-width="1.2" opacity="{op}"/>')
            sh.text(coords[len(coords) // 2], k["name"], size=10, color=label_color, opacity=op, dy=-6)
    elif k["shape"] == "area" and len(coords) >= 3:
        c = centroid(coords)
        if t in ("lake", "sea"):
            sh.add(f'<polygon points="{sh.pts(coords)}" fill="{WATER_WASH}" opacity="{0.9 * op:.2f}"/>')
            draw_waves(sh, coords, rng)
            sh.add(f'<path d="{sh.wavy_path(coords, rng, amp=1.2, close=True)}" fill="none" stroke="{WATER_INK}" stroke-width="1.1" opacity="{op}"/>')
            sh.text(c, k["name"], size=12 if t == "sea" else 10.5, italic=t == "lake", caps=t == "sea", color=WATER_INK, opacity=op)
        elif t == "forest":
            cid = sh.clip(coords)
            sh.add(f'<polygon points="{sh.pts(coords)}" fill="{TERRAIN_WASH["forest"]}" opacity="{0.6 * op:.2f}"/>')
            for p in grid_points(coords, max(extent_across(coords) / 9, 1.5), rng):
                draw_tree_mark(sh, p, 3.2, rng, opacity=op)
            sh.add(f'<path d="{sh.wavy_path(coords, rng, amp=1.5, close=True)}" fill="none" stroke="{INK_LIGHT}" stroke-width="0.7" opacity="{op}"/>')
            sh.text(c, k["name"], size=10, italic=True, color=label_color, opacity=op)
        elif t == "marsh":
            sh.add(f'<polygon points="{sh.pts(coords)}" fill="{TERRAIN_WASH["marsh"]}" opacity="{0.6 * op:.2f}"/>')
            for p in grid_points(coords, max(extent_across(coords) / 7, 1.5), rng):
                draw_marsh_mark(sh, p, 4.5, opacity=op)
            sh.text(c, k["name"], size=10, italic=True, color=label_color, opacity=op)
        elif t == "mountain":
            for p in grid_points(coords, max(extent_across(coords) / 6, 1.5), rng):
                draw_mountain_mark(sh, p, 10, rng, opacity=op)
            sh.text(c, k["name"], size=11, caps=True, color=label_color, opacity=op, dy=-14)
        else:
            sh.add(f'<polygon points="{sh.pts(coords)}" fill="none" stroke="{INK}" stroke-width="0.9" opacity="{op}"/>')
            sh.text(c, k["name"], size=10, color=label_color, opacity=op)
    else:
        p = coords[0]
        x, y = sh.px(p)
        if t == "town":
            sh.add(f'<rect x="{x - 4.5:.1f}" y="{y - 4.5:.1f}" width="9" height="9" fill="{INK}" opacity="{op}"/>')
            sh.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{PARCHMENT}" opacity="{op}"/>')
        elif t == "ruin":
            sh.add(f'<path d="M{x - 4.5:.1f},{y + 4.5:.1f} v-9 h4 M{x + 4.5:.1f},{y - 4.5:.1f} v9 h-4 M{x - 2:.1f},{y + 1:.1f} l4,-2" '
                   f'fill="none" stroke="{INK}" stroke-width="1.2" opacity="{op}"/>')
        elif t == "cave":
            sh.add(f'<path d="M{x - 5:.1f},{y + 2:.1f} A5,5 0 0 1 {x + 5:.1f},{y + 2:.1f}" fill="none" stroke="{INK}" stroke-width="1.3" opacity="{op}"/>')
            sh.add(f'<line x1="{x - 5:.1f}" y1="{y + 2:.1f}" x2="{x + 5:.1f}" y2="{y + 2:.1f}" stroke="{INK}" stroke-width="0.8" opacity="{op}"/>')
        elif t == "pass":
            sh.add(f'<path d="M{x - 7:.1f},{y - 4:.1f} l5,6 M{x + 7:.1f},{y - 4:.1f} l-5,6" fill="none" stroke="{INK}" stroke-width="1.3" opacity="{op}"/>')
        else:
            sh.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="none" stroke="{INK}" stroke-width="1" opacity="{op}"/>')
        sh.text(p, k["name"], size=11, color=label_color, opacity=op, anchor="start", dx=8, dy=4)
        if reported:
            sh.text(p, f"reported, {k['source']}", size=7.5, italic=True, color=INK_FAINT, opacity=op, anchor="start", dx=8, dy=14)


def draw_scale_bar(sh, frame):
    fw = frame[2] - frame[0]
    for mi in (5, 10, 20, 25, 50, 100, 200, 500):
        if mi * sh.scale >= 120 or mi >= fw / 3:
            break
    x0 = sh.pad + 10
    y0 = sh.h - sh.pad - 16
    L = mi * sh.scale
    sh.add(f'<rect x="{x0 - 6}" y="{y0 - 20}" width="{L + 12:.1f}" height="34" fill="{PARCHMENT}" opacity="0.8"/>')
    sh.add(f'<line x1="{x0}" y1="{y0}" x2="{x0 + L:.1f}" y2="{y0}" stroke="{INK}" stroke-width="1.4"/>')
    for k in range(5):
        xx = x0 + L * k / 4
        sh.add(f'<line x1="{xx:.1f}" y1="{y0 - 4}" x2="{xx:.1f}" y2="{y0 + 4}" stroke="{INK}" stroke-width="1"/>')
    sh.add(f'<rect x="{x0}" y="{y0 - 3}" width="{L / 4:.1f}" height="6" fill="{INK}"/>')
    sh.add(f'<rect x="{x0 + L / 2:.1f}" y="{y0 - 3}" width="{L / 4:.1f}" height="6" fill="{INK}"/>')
    sh.add(f'<text x="{x0 + L / 2:.1f}" y="{y0 - 8}" text-anchor="middle" fill="{INK}" style="font-family:Georgia,serif;font-size:10px">{mi} miles</text>')


def draw_compass(sh):
    cx, cy, r = sh.w - sh.pad - 48, sh.pad + 52, 30
    sh.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 8}" fill="{PARCHMENT}" opacity="0.85"/>')
    sh.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="0.8"/>')
    sh.add(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.55:.1f}" fill="none" stroke="{INK_LIGHT}" stroke-width="0.5"/>')
    for i in range(8):
        a = math.radians(i * 45)
        rr = r if i % 2 == 0 else r * 0.6
        tip = (cx + math.sin(a) * rr, cy - math.cos(a) * rr)
        base_w = r * 0.14
        bl = (cx + math.sin(a - math.pi / 2) * base_w, cy - math.cos(a - math.pi / 2) * base_w)
        br = (cx + math.sin(a + math.pi / 2) * base_w, cy - math.cos(a + math.pi / 2) * base_w)
        fill = INK if i % 2 == 0 else "none"
        sh.add(f'<path d="M{tip[0]:.1f},{tip[1]:.1f} L{bl[0]:.1f},{bl[1]:.1f} L{cx},{cy} L{br[0]:.1f},{br[1]:.1f} Z" fill="{fill}" stroke="{INK}" stroke-width="0.7"/>')
    sh.add(f'<text x="{cx}" y="{cy - r - 10}" text-anchor="middle" fill="{INK}" style="font-family:Georgia,serif;font-size:13px;font-weight:bold">N</text>')


def draw_sheets(world, knowledge, out_dir, zoom):
    regions_k = {r["id"]: known_region(r, knowledge["regions"][r["id"]]) for r in world["regions"] if grade_of(knowledge["regions"].get(r["id"])) != "none"}
    features_k = {}
    for f, layer in all_features(world):
        e = knowledge["features"].get(f["id"])
        if grade_of(e) != "none":
            features_k[f["id"]] = (known_feature(f, e), layer["id"] if layer else None)

    # The frame.
    ext = world.get("extent", {})
    full = (ext.get("x", [0, 100])[0], ext.get("y", [0, 100])[0], ext.get("x", [0, 100])[1], ext.get("y", [0, 100])[1])
    frame = full
    if zoom == "known":
        pts = []
        for k in regions_k.values():
            if k["polygon"]:
                pts.extend(k["polygon"])
        for k, _ in features_k.values():
            if k["grade"] != "rumored":
                pts.extend(k["coords"])
        if pts:
            x0, y0, x1, y1 = bbox(pts)
            mx, my = max((x1 - x0) / 5, 5), max((y1 - y0) / 5, 5)
            frame = (x0 - mx, y0 - my, x1 + mx, y1 + my)

    def seed(s):
        return random.Random(hash_str(s))

    def surface(sh, dim=1.0):
        order = [k for k in regions_k.values() if k["grade"] == "seen"] + [k for k in regions_k.values() if k["grade"] == "reported"]
        for k in order:
            if dim < 1:
                sh.add(f'<g opacity="{dim}">')
            draw_region(sh, k, seed(k["id"]))
            if dim < 1:
                sh.add("</g>")
        for k in regions_k.values():
            if k["grade"] == "rumored":
                if dim < 1:
                    sh.add(f'<g opacity="{dim}">')
                draw_rumored_region(sh, k)
                if dim < 1:
                    sh.add("</g>")
        # areas, then lines, then points, so symbols sit on top
        surf = [k for k, lid in features_k.values() if lid is None]
        for shape in ("area", "line", "point"):
            for k in surf:
                if k["shape"] == shape:
                    draw_feature(sh, k, seed(k["id"]), dim=dim)

    def beyond_notes(sh):
        notes = []
        fx0, fy0, fx1, fy1 = frame
        cx, cy = (fx0 + fx1) / 2, (fy0 + fy1) / 2
        items = [(k["name"], k["near"]) for k in regions_k.values() if k["grade"] == "rumored"]
        items += [(k["name"], k["coords"][0]) for k, lid in features_k.values() if lid is None and k["grade"] == "rumored"]
        for name, p in items:
            if not (fx0 <= p[0] <= fx1 and fy0 <= p[1] <= fy1):
                notes.append(f"{name}, {bearing_name(p[0] - cx, p[1] - cy)}")
        return ["rumored, beyond this sheet: " + "; ".join(notes)] if notes else []

    written = []
    title = f"{world.get('campaign', 'world')}: the god's chart"
    sh = Sheet(frame)
    surface(sh)
    draw_scale_bar(sh, frame)
    draw_compass(sh)
    notes = ["Seen ground is drawn as found. Reported ground is drawn as told and may be wrong. Rumors are faint names."] + beyond_notes(sh)
    path = os.path.join(out_dir, "map.svg")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w") as f:
        f.write(sh.render(title, notes))
    written.append(path)

    for layer in world.get("layers", []):
        under = [k for k, lid in features_k.values() if lid == layer["id"]]
        if not under:
            continue
        sh = Sheet(frame)
        surface(sh, dim=0.28)
        for shape in ("area", "line", "point"):
            for k in under:
                if k["shape"] == shape:
                    draw_feature(sh, k, seed(k["id"]))
        draw_scale_bar(sh, frame)
        draw_compass(sh)
        depth = layer.get("depth", 1)
        sh.text(((frame[0] + frame[2]) / 2, frame[3]), f"Below, layer {depth}: {layer.get('name', '')}", size=14, caps=True, dy=22)
        p = os.path.join(out_dir, f"map-under-{depth}.svg")
        with open(p, "w") as f:
            f.write(sh.render(f"{title}, below layer {depth}", ["The surface is drawn faintly for bearings. Only known ground below is drawn."]))
        written.append(p)

    meta = {"frame_miles": {"x": [frame[0], frame[2]], "y": [frame[1], frame[3]]}, "zoom": zoom or "full",
            "regions_drawn": {g: sum(1 for k in regions_k.values() if k["grade"] == g) for g in ("seen", "reported", "rumored")},
            "features_drawn": {g: sum(1 for k, _ in features_k.values() if k["grade"] == g) for g in ("seen", "reported", "rumored")},
            "drawn": datetime.date.today().isoformat(), "files": [os.path.basename(w) for w in written]}
    save_json(os.path.join(out_dir, "map-meta.json"), meta)
    return written


def hash_str(s):
    h = 1469598103934665603
    for ch in s:
        h = ((h ^ ord(ch)) * 1099511628211) & 0xFFFFFFFFFFFFFFFF
    return h


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


def fmt_pt(p):
    return f"{p[0]:.0f},{p[1]:.0f}"


def gazetteer(world, knowledge, out_dir, log_path):
    hist = read_log(log_path)
    lines = [f"# Gazetteer: {world.get('campaign', 'the world')}", "",
             "Everything the god knows of the ground, exact where the chart is pictorial. Regenerated from `player/map-knowledge.json` by `tools/map.py gazetteer`; never edited by hand. "
             "Positions are miles east and north of the chart's origin. Grades: seen (found so), reported (as told, may be wrong), rumored (a name and a rough place).", ""]
    regions = [known_region(r, knowledge["regions"][r["id"]]) for r in world["regions"] if grade_of(knowledge["regions"].get(r["id"])) != "none"]
    feats = []
    for f, layer in all_features(world):
        e = knowledge["features"].get(f["id"])
        if grade_of(e) != "none":
            feats.append((known_feature(f, e), layer))
    reg_name = {k["id"]: k["name"] for k in regions}

    def hist_line(i):
        return ("; history: " + "; ".join(hist[i])) if i in hist else ""

    lines.append("## Regions")
    lines.append("")
    for g in ("seen", "reported", "rumored"):
        for k in sorted((r for r in regions if r["grade"] == g), key=lambda r: r["name"]):
            if g == "rumored":
                lines.append(f"- **{k['name']}**, rumored, somewhere near {fmt_pt(k['near'])} by the telling of {k['source']}, year {k['year']}{hist_line(k['id'])}.")
            else:
                across = f", about {extent_across(k['polygon']):.0f} miles across" if g == "seen" else ""
                lines.append(f"- **{k['name']}**, {k['terrain']}{across}, {g}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
    lines.append("")

    def place_block(title, items, kinds):
        lines.append(f"## {title}")
        lines.append("")
        sel = [k for k, layer in items if k["type"] in kinds and k["grade"] != "rumored"]
        if not sel:
            lines.append("Nothing known.")
        for k in sorted(sel, key=lambda k: (grade_rank(k["grade"]) * -1, k["name"])):
            regs = ", ".join(reg_name.get(r, "a region not yet known") for r in k["regions"]) if k["grade"] == "seen" else ""
            where = ""
            if k["shape"] == "point":
                where = f"at {fmt_pt(k['coords'][0])}"
            elif k["shape"] == "line":
                where = f"{polyline_length(k['coords']):.0f} miles long, from {fmt_pt(k['coords'][0])} to {fmt_pt(k['coords'][-1])}"
            else:
                x0, y0, x1, y1 = bbox(k["coords"])
                where = f"about {x1 - x0:.0f} by {y1 - y0:.0f} miles, centered {fmt_pt(centroid(k['coords']))}"
            lines.append(f"- **{k['name']}** ({k['type']}), {where}{', in ' + regs if regs else ''}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
        lines.append("")

    surface = [(k, l) for k, l in feats if l is None]
    place_block("Places", surface, POINT_TYPES)
    place_block("Waters and ranges", surface, {"river", "lake", "sea", "mountain", "marsh", "forest"})

    lines.append("## Routes")
    lines.append("")
    routes = [k for k, l in surface if k["type"] in ("road", "river") and k["grade"] != "rumored" and k["shape"] == "line"]
    points = [k for k, l in surface if k["shape"] == "point" and k["type"] in POINT_TYPES and k["grade"] != "rumored"]
    if not routes:
        lines.append("No route known.")
    for r in routes:
        along = []
        for p in points:
            d, t = dist_to_polyline(p["coords"][0], r["coords"])
            if d <= 3:
                along.append((t, p["name"]))
        along.sort()
        stops = ", ".join(n for _, n in along) if along else "no known place along it"
        lines.append(f"- **{r['name']}** ({r['type']}), {polyline_length(r['coords']):.0f} miles, {r['grade']}: {stops}.")
    lines.append("")

    lines.append("## Distances")
    lines.append("")
    lines.append("As the crow flies, in miles, from the positions the god believes; a reported endpoint makes the distance reported. The pace table (`engine/rules/time-and-pace.md`) turns miles into days.")
    lines.append("")
    for p in sorted(points, key=lambda k: k["name"]):
        others = sorted(((math.dist(p["coords"][0], q["coords"][0]), q) for q in points if q is not p), key=lambda t: t[0])[:4]
        if not others:
            continue
        parts = [f"{q['name']} {d:.0f} ({'seen' if p['grade'] == 'seen' and q['grade'] == 'seen' else 'reported'})" for d, q in others]
        lines.append(f"- **{p['name']}**: " + "; ".join(parts) + ".")
    lines.append("")

    lines.append("## Rumors")
    lines.append("")
    rum = [k for k, l in surface if k["grade"] == "rumored"]
    if not rum:
        lines.append("None.")
    for k in sorted(rum, key=lambda k: k["year"] or 0):
        lines.append(f"- **{k['name']}** ({k['type']}), somewhere near {fmt_pt(k['coords'][0])}, by the telling of {k['source']}, year {k['year']}{hist_line(k['id'])}.")
    lines.append("")

    for layer in world.get("layers", []):
        under = [(k, l) for k, l in feats if l is layer]
        if not under:
            continue
        lines.append(f"## Below, layer {layer.get('depth', 1)}: {layer.get('name', '')}")
        lines.append("")
        for k, _ in sorted(under, key=lambda t: (grade_rank(t[0]["grade"]) * -1, t[0]["name"])):
            if k["grade"] == "rumored":
                lines.append(f"- **{k['name']}**, rumored, somewhere under {fmt_pt(k['coords'][0])}, by the telling of {k['source']}, year {k['year']}.")
            elif k["shape"] == "line":
                lines.append(f"- **{k['name']}** ({k['type']}), {polyline_length(k['coords']):.0f} miles, from under {fmt_pt(k['coords'][0])} to under {fmt_pt(k['coords'][-1])}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
            else:
                lines.append(f"- **{k['name']}** ({k['type']}), under {fmt_pt(k['coords'][0])}, {k['grade']}, source: {k['source']}, year {k['year']}{hist_line(k['id'])}.")
        lines.append("")

    path = os.path.join(out_dir, "gazetteer.md")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    return path


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


# ---------------------------------------------------------------- reveal

def reveal(world, knowledge, knowledge_path, log_path, args):
    kind = "region" if args.region else "feature"
    ident = args.region or args.feature
    if args.grade not in GRADES or args.grade == "none":
        sys.exit("map.py: grade must be rumored, reported or seen")
    truth = None
    if kind == "region":
        truth = next((r for r in world["regions"] if r["id"] == ident), None)
    else:
        truth = next((f for f, _ in all_features(world) if f["id"] == ident), None)
    if truth is None:
        sys.exit(f"map.py: no {kind} with id {ident!r} in the sealed map; a typo cannot create ground")
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
    entry = {"grade": args.grade, "source": args.source, "year": args.year}
    correction = ""
    if args.grade == "seen":
        if old_grade == "reported" and "coords" in old.get("told", {}) and kind == "feature":
            told_c = centroid(old["told"]["coords"])
            true_c = centroid(truth["coords"])
            if math.dist(told_c, true_c) > 1:
                correction = f"; told at {fmt_pt(told_c)} by {old.get('source', '?')}, found at {fmt_pt(true_c)}"
        if old.get("told", {}).get("name") and old["told"]["name"] != truth["name"]:
            correction += f"; called {old['told']['name']} by {old.get('source', '?')}, found to be {truth['name']}"
    else:
        if told:
            entry["told"] = told
        elif "told" in old and grade_rank(args.grade) >= grade_rank(old_grade):
            # keep what was told before if the new teller adds nothing
            entry["told"] = old["told"]
        elif "told" in old:
            # lowered to rumored: keep the old telling as a rough place, never the truth
            kept = {k: v for k, v in old["told"].items() if k in ("name", "type", "terrain")}
            shape_key = "coords" if "coords" in old["told"] else ("polygon" if "polygon" in old["told"] else None)
            if shape_key:
                kept["near"] = [round(v, 1) for v in centroid(old["told"][shape_key])]
            elif "near" in old["told"]:
                kept["near"] = old["told"]["near"]
            if kept:
                entry["told"] = kept
        if args.grade == "rumored" and "near" not in entry.get("told", {}):
            print("note: no near given; the faint label will sit at the true centroid. Give --told '{\"near\": [x, y]}' when the rumor is vague.", file=sys.stderr)
    table[ident] = entry
    save_json(knowledge_path, knowledge)
    os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
    reason = f"; forced: {args.force}" if args.force else ""
    with open(log_path, "a") as f:
        f.write(f"- {datetime.date.today().isoformat()} | year {args.year} | {kind} {ident} | {old_grade} -> {args.grade} | {args.source}{correction}{reason}\n")
    print(f"{kind} {ident}: {old_grade} -> {args.grade} ({args.source}, year {args.year}){correction}")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="StarFall map tool")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("draw", "gazetteer", "reveal"):
        s = sub.add_parser(name)
        s.add_argument("campaign")
        s.add_argument("--world", help="path to the sealed map.json (default: the campaign's sealed folder)")
        s.add_argument("--knowledge", help="path to map-knowledge.json (default: campaigns/<name>/player/)")
        s.add_argument("--out", help="output folder (default: campaigns/<name>/player/)")
        if name == "draw":
            s.add_argument("--zoom", choices=["known"], help="crop to the known regions")
        if name == "reveal":
            g = s.add_mutually_exclusive_group(required=True)
            g.add_argument("--region")
            g.add_argument("--feature")
            s.add_argument("--grade", required=True)
            s.add_argument("--source", required=True)
            s.add_argument("--year", required=True, type=int)
            s.add_argument("--told", help="JSON: what was told (name, type, coords, polygon, terrain, near)")
            s.add_argument("--force", help="reason, to lower a grade")
    args = ap.parse_args()
    world_path, knowledge_path, out_dir = campaign_paths(args)
    world = load_json(world_path)
    knowledge = load_json(knowledge_path, default={"campaign": world.get("campaign"), "regions": {}, "features": {}})
    knowledge.setdefault("regions", {})
    knowledge.setdefault("features", {})
    log_path = os.path.join(out_dir, "map-log.md")

    if args.cmd == "draw":
        for p in draw_sheets(world, knowledge, out_dir, args.zoom):
            print(f"wrote {os.path.relpath(p, ROOT)}")
    elif args.cmd == "gazetteer":
        print(f"wrote {os.path.relpath(gazetteer(world, knowledge, out_dir, log_path), ROOT)}")
    elif args.cmd == "reveal":
        reveal(world, knowledge, knowledge_path, log_path, args)


if __name__ == "__main__":
    main()
