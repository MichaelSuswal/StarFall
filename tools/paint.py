"""Turn image requests into paintings.

Two request folders, each with its own output folder:
  images/requests/*.json                        -> images/out/                        (scene paintings, public)
  SPOILERS_do_not_open/images/requests/*.json   -> SPOILERS_do_not_open/images/out/   (map paintings, sealed)
A map prompt describes the whole world's ground, so map requests go in the sealed folder.

A request file looks like:
{"id": "y001-morning", "prompt": "...", "shape": "square" | "wide" | "tall"}
Requests that already have an output are skipped. Paths are resolved from the repository root.

Held requests are never painted. A request written before its image is approved waits in
images/held/ (outside both request folders and outside the workflow's trigger paths, so
writing one starts no job); it is moved into a request folder only with Michael's go. The
scan reads only the top level of each request folder, and any path with a `held` folder in
it is skipped as well, so an older images/requests/held/ is never painted either.
"""
import base64, glob, json, os, re, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDERS = [("images/requests", "images/out"),
           ("SPOILERS_do_not_open/images/requests", "SPOILERS_do_not_open/images/out")]
HELD = "held"   # images/held/: requests that wait for Michael's go; never painted
MODEL = os.environ.get("OPENAI_IMAGE_MODEL") or "chatgpt-image-latest"
SIZES = {"square": "1024x1024", "wide": "1536x1024", "tall": "1024x1536"}


def is_held(path, root=ROOT):
    """True for a request under a `held` folder (images/held/, or an older images/requests/held/)."""
    parts = os.path.relpath(os.path.abspath(path), os.path.abspath(root)).split(os.sep)
    return HELD in parts[:-1]


def campaign_of(req, root=ROOT):
    """The request's campaign: its `campaign` field, else the longest campaign folder name its id starts with."""
    if req.get("campaign"):
        return req["campaign"]
    d = os.path.join(root, "campaigns")
    names = sorted((n for n in (os.listdir(d) if os.path.isdir(d) else []) if os.path.isdir(os.path.join(d, n))),
                   key=len, reverse=True)
    rid = str(req.get("id", ""))
    return next((n for n in names if rid.startswith(n + "-")), None)


def kind_words(rest):
    """(words the label must hold, words it must not) for a request id less its campaign prefix."""
    if rest == "map-surface":
        return ["surface"], []
    if rest == "map-clouds":
        return ["cloud"], []
    m = re.fullmatch(r"map-under-(\d+)", rest)
    if m:
        return ["underground", f"under-{m.group(1)}"], []
    m = re.fullmatch(r"(\d{3})-morning", rest)
    if m:
        return (["first morning"], []) if int(m.group(1)) == 1 else (["morning"], ["first"])
    if re.fullmatch(r"\d{3}-request-\d+", rest):   # a painting the player asked for (house-style.md)
        return ["player-asked", "on request", "requested"], []
    return [], []


NUM_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
COUNT_RE = re.compile(r"\b(?:up to |at most )?(\d+|one|two|three|four|five|six) (?:a|per|each) (?:played )?(day|year)\b")
GROUP_RE = re.compile(r"(\d{3})-(morning|request-\d+)")


def line_limit(value):
    """The count an approval line sets ("one per played year", "up to two a day"), or None for none.
    A played year is one day of play (DESIGN 14.7), so both count by the request id's NNN."""
    m = COUNT_RE.search(value)
    if not m:
        return None
    n = m.group(1)
    return int(n) if n.isdigit() else NUM_WORDS[n]


def group_of(rest):
    """(NNN, kind) for a play request id less its campaign prefix: kind "morning" or "request"."""
    m = GROUP_RE.fullmatch(rest)
    if not m:
        return None
    return m.group(1), "morning" if m.group(2) == "morning" else "request"


def known_ids(name, root=ROOT):
    """Every image id for the campaign, from requests (held ones included, since a held request
    still counts toward the day once it is moved in) and from paintings already made."""
    ids = set()
    for req_dir, out_dir in FOLDERS:
        for path in glob.glob(os.path.join(root, req_dir, "*.json")):
            if is_held(path, root):
                continue
            try:
                ids.add(str(json.load(open(path)).get("id", "")))
            except (json.JSONDecodeError, OSError):
                continue
        ids |= {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(root, out_dir, "*.png"))}
    return {i for i in ids if i.startswith(name + "-")}


def within_count(name, rid, limit, root=ROOT):
    """True when rid is among the first `limit` play requests of its kind for its year (by id order)."""
    g = group_of(rid[len(name) + 1:])
    if g is None or limit is None:
        return True
    same = sorted(i for i in known_ids(name, root) | {rid} if group_of(i[len(name) + 1:]) == g)
    return same.index(rid) < limit


def approval_lines(text):
    """(label, value) for every "label: value" line of images.md, list markers and bold set aside."""
    out = []
    for line in text.splitlines():
        t = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", line).replace("**", "").strip()
        if ":" not in t or t.startswith("#"):
            continue
        label, value = t.split(":", 1)
        out.append((label.strip().lower(), value.strip().lower()))
    return out


def covered(req, root=ROOT):
    """(True, line) when the campaign's state/images.md approves the request, else (False, reason)."""
    name = campaign_of(req, root)
    rid = str(req.get("id", ""))
    if not name:
        return False, "no campaign folder matches its id, so no images.md covers it"
    path = os.path.join(root, "campaigns", name, "state", "images.md")
    if not os.path.exists(path):
        return False, f"campaigns/{name}/state/images.md is missing"
    want, avoid = kind_words(rid[len(name) + 1:] if rid.startswith(name + "-") else rid)
    over = None
    for label, value in approval_lines(open(path, encoding="utf-8").read()):
        if not re.match(r"approved\b", value):
            continue
        if rid.lower() in label:
            return True, f"{label}: {value}"
        if "repaint" in label or not want:
            continue
        if any(w in label for w in want) and not any(w in label for w in avoid):
            limit = line_limit(value)
            if not within_count(name, rid, limit, root):
                over = f"campaigns/{name}/state/images.md approves {limit} for that year ({label}: {value}); this one is over the count"
                continue
            return True, f"{label}: {value}"
    if over:
        return False, over
    return False, f"campaigns/{name}/state/images.md does not approve it"


def pending(root=ROOT, skipped=None):
    """(request path, request, output path) for every request without an output that the campaign's
    images.md covers. Requests it does not cover are left out, and appended to `skipped` as
    (request path, reason) when a list is given."""
    out = []
    for req_dir, out_dir in FOLDERS:
        for path in sorted(glob.glob(os.path.join(root, req_dir, "*.json"))):
            if is_held(path, root):
                continue
            req = json.load(open(path))
            target = os.path.join(root, out_dir, f"{req['id']}.png")
            if os.path.exists(target):
                continue
            ok, why = covered(req, root)
            if not ok:
                if skipped is not None:
                    skipped.append((path, why))
                continue
            out.append((path, req, target))
    return out


def report_skipped(skipped, root=ROOT):
    lines = [f"skipped {os.path.relpath(p, root)}: {why}; not painted (it waits for images.md, or belongs in a held folder)"
             for p, why in skipped]
    for l in lines:
        print(l)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary and lines:
        with open(summary, "a") as f:
            f.write("### Requests not painted\n\n" + "\n".join("- " + l for l in lines) + "\n")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    skipped = []
    todo = pending(skipped=skipped)
    report_skipped(skipped)
    if "--check" in argv:
        for path, req, target in todo:
            print(f"would paint {os.path.relpath(path, ROOT)} -> {os.path.relpath(target, ROOT)}")
        print(f"{len(todo)} to paint, {len(skipped)} skipped")
        return
    if not todo:
        print("0 new painting(s)")
        return
    key = os.environ["OPENAI_API_KEY"]
    made = 0
    for path, req, target in todo:
        body = json.dumps({
            "model": MODEL,
            "prompt": req["prompt"],
            "size": SIZES.get(req.get("shape", "square"), "1024x1024"),
            "n": 1,
        }).encode()
        r = urllib.request.Request(
            "https://api.openai.com/v1/images/generations", data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            resp = json.load(urllib.request.urlopen(r, timeout=300))
        except urllib.error.HTTPError as e:
            print(f"{req['id']}: HTTP {e.code} {e.read().decode()[:500]}", file=sys.stderr)
            sys.exit(1)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, "wb").write(base64.b64decode(resp["data"][0]["b64_json"]))
        print(f"painted {os.path.relpath(target, ROOT)}")
        made += 1
    print(f"{made} new painting(s)")


if __name__ == "__main__":
    main()
