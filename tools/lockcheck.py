"""Lock checks a script can run for a campaign. The continuity checker runs these before
writing LOCKED.md, and reads every public file itself as well.

Usage: python3 tools/lockcheck.py <campaign> [--places] [--leaks] [--mysteries] [--rolls] [--dashes] [--all]
                                             [--root DIR] [--counts-only]
With no check named, --all. Exit 1 on any failure. One line per finding, then one count
line per check. Warnings are printed but do not fail. --counts-only prints the count lines
alone (for records kept outside the spoiler folder). --root points at another repository
layout (tests use a fixture).

  --places     every bracketed id like [r12] or [f03] in a sealed file exists in map.json;
               the map's own ids, neighbors and landings resolve; warns on a capitalized
               map name written with no id after it.
  --leaks      builds the sealed term list (god names and folder labels, the count of gods,
               place names the player has not seen or been told, phenomena yearly counts,
               mystery and schedule titles, star values) and fails on any hit in
               campaigns/<name>/. Also fails a public map-knowledge file that breaks the
               map rules. S/leak-allow.txt (one term per line, # for comments) exempts terms.
  --mysteries  every mystery has Truth; Body; Cost if ignored; Clock or trigger; Clues;
               Branches; Never found, with a clue carrying readings and a branch saying
               what the world does.
  --rolls      every r-NNNN cited in a sealed file is in S/state/rolls.jsonl, nothing is
               rolled twice, every reroll has a reason; the public rolls log is empty.
  --dashes     no em or en dash in any campaign file, sealed or public.
"""
import argparse, json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import map as mapt  # noqa: E402

TEXT_EXT = {".md", ".txt", ".json", ".jsonl", ".py", ".yml", ".yaml", ".csv"}
REQUIRED = ["Truth", "Body", "Cost if ignored", "Clock or trigger", "Clues", "Branches", "Never found"]
NUM_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen", "twenty"]
BRACKET_RE = re.compile(r"(?<!\])\[([a-z0-9][a-z0-9-]*(?:\s*,\s*[a-z0-9][a-z0-9-]*)*)\](?![(\[])")
ROLL_RE = re.compile(r"\br-(\d{4,})\b")
BRACKET_SKIP = {"x", "sic", "tbd", "todo", "ok"}


class Report:
    def __init__(self, counts_only):
        self.counts_only = counts_only
        self.fails = {}
        self.warns = {}

    def fail(self, check, msg):
        self.fails[check] = self.fails.get(check, 0) + 1
        if not self.counts_only:
            print(f"FAIL {check}: {msg}")

    def warn(self, check, msg):
        self.warns[check] = self.warns.get(check, 0) + 1
        if not self.counts_only:
            print(f"WARN {check}: {msg}")

    def summary(self, checks):
        for c in checks:
            print(f"{c}: {self.fails.get(c, 0)} failure(s), {self.warns.get(c, 0)} warning(s)")
        return 1 if any(self.fails.values()) else 0


def text_files(folder):
    out = []
    for dirpath, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for fn in sorted(files):
            if os.path.splitext(fn)[1].lower() in TEXT_EXT:
                out.append(os.path.join(dirpath, fn))
    return out


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return ""


class Campaign:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.S = os.path.join(root, "SPOILERS_do_not_open", "campaigns", name)
        self.P = os.path.join(root, "campaigns", name)
        if not os.path.isdir(self.S):
            sys.exit(f"lockcheck: no sealed campaign at {self.S}")
        mp = os.path.join(self.S, "map.json")
        self.world = json.load(open(mp)) if os.path.exists(mp) else {}
        kp = os.path.join(self.P, "player", "map-knowledge.json")
        self.knowledge = json.load(open(kp)) if os.path.exists(kp) else {"regions": {}, "features": {}}
        self.knowledge.setdefault("regions", {})
        self.knowledge.setdefault("features", {})

    def rel(self, path):
        return os.path.relpath(path, self.root)

    def god_labels(self):
        labels = set()
        for sub in ("gods", "gods-sealed"):
            d = os.path.join(self.S, sub)
            if os.path.isdir(d):
                labels |= {x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))}
        return labels

    def npc_gods(self):
        d = os.path.join(self.S, "gods")
        return sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))) if os.path.isdir(d) else []

    def folder_names(self):
        names = set()
        for base in (self.S, self.P):
            d = os.path.join(base, "civs")
            if os.path.isdir(d):
                names |= {os.path.splitext(x)[0] for x in os.listdir(d)}
        return names

    def map_ids(self):
        ids = set()
        for el, _ in list(mapt.all_regions(self.world)) + list(mapt.all_features(self.world)):
            ids.add(el["id"])
        ids |= {layer["id"] for layer in self.world.get("layers", []) if "id" in layer}
        return ids

    def elements(self):
        for el, layer in mapt.all_regions(self.world):
            yield "region", el
        for el, layer in mapt.all_features(self.world):
            yield "feature", el

    def allow(self):
        p = os.path.join(self.S, "leak-allow.txt")
        if not os.path.exists(p):
            return set()
        return {l.strip().lower() for l in open(p) if l.strip() and not l.strip().startswith("#")}


def name_variants(name):
    """A map name and its form without a leading article, kept only if capitalized and 4+ letters."""
    out = {name}
    m = re.match(r"^(The|the|A|An)\s+(.+)$", name)
    if m:
        out.add(m.group(2))
    return {v for v in out if len(v) >= 4 and v[0].isupper()}


# ---------------------------------------------------------------- places

def check_places(c, rep):
    ids = c.map_ids()
    if not c.world:
        rep.fail("places", "no map.json in the sealed campaign")
        return
    for p in mapt.check_world(c.world):
        rep.fail("places", f"map.json: {p}")
    exempt = c.god_labels() | c.folder_names() | {"player"} | BRACKET_SKIP
    names = {}
    for kind, el in c.elements():
        for v in name_variants(el.get("name", "")):
            names.setdefault(v, set()).add(el["id"])
    name_res = {v: re.compile(r"(?<![\w'])" + re.escape(v) + r"(?![\w])") for v in names}
    for path in text_files(c.S):
        base = os.path.basename(path)
        if base in ("map.json", "rolls.jsonl", "phenomena.json") or path.endswith(".py"):
            continue
        text = read(path)
        for ln, line in enumerate(text.splitlines(), 1):
            for m in BRACKET_RE.finditer(line):
                for tok in re.split(r"\s*,\s*", m.group(1)):
                    if tok in ids or tok in exempt or re.fullmatch(r"r-\d+", tok) or len(tok) < 2:
                        continue
                    rep.fail("places", f"{c.rel(path)}:{ln}: [{tok}] is not in map.json")
        if not path.endswith(".md"):
            continue
        for v, rx in name_res.items():
            bare = 0
            for m in rx.finditer(text):
                after = text[m.end():m.end() + 60]
                after = re.sub(r"^('s)?\s*(\([^)\n]*\)\s*)?", "", after)
                bm = re.match(r"\[([a-z0-9, -]+)\]", after)
                if bm and set(re.split(r"\s*,\s*", bm.group(1))) & names[v]:
                    continue
                bare += 1
            if bare:
                rep.warn("places", f"{c.rel(path)}: map name \"{v}\" written {bare} time(s) with no id")


# ---------------------------------------------------------------- leaks

def word_num_re(n):
    alts = [str(n)]
    if 0 <= n < len(NUM_WORDS):
        alts.append(NUM_WORDS[n])
    return r"\b(?:" + "|".join(alts) + r")\b"


def leak_terms(c):
    """(kind, label, compiled regex) for every sealed term."""
    terms = []
    allow = c.allow()

    def add(kind, label, rx, flags=0):
        if label.lower() in allow:
            return
        terms.append((kind, label, re.compile(rx, flags)))

    def phrase(kind, s, case=False):
        s = s.strip()
        if len(s) < 3:
            return
        add(kind, s, r"(?<![\w])" + re.escape(s) + r"(?![\w])", 0 if case else re.I)

    for label in sorted(c.god_labels()):
        phrase("god label", label)
    gnames = set()
    for god in c.npc_gods():
        for path in text_files(os.path.join(c.S, "gods", god)) + text_files(os.path.join(c.S, "gods-sealed", god)):
            t = read(path)
            gnames |= set(re.findall(r"^#\s*Power card:\s*(.+?)\s*$", t, re.M))
            gnames |= set(re.findall(r"^\**Name\**:\**\s*([A-Z][\w' -]+?)\s*\.?\s*$", t, re.M))
            gnames |= set(re.findall(r"\bI name myself ([A-Z][\w'-]+)", t))
    for n in sorted(gnames):
        phrase("god name", n, case=True)
    n = len(c.npc_gods())
    if n:
        for k in sorted({n, n + 1}):
            add("god count", f"{k} gods", word_num_re(k) + r"\s+(?:other\s+|more\s+|npc\s+|rival\s+|living\s+)?(?:gods|deities)\b", re.I)

    # places the player has not seen or been told; names it was told are known to it
    known_ids, told_names = set(), set()
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            if e.get("grade") in ("seen", "reported"):
                known_ids.add(ident)
            t = e.get("told") or {}
            if t.get("name"):
                told_names.add(t["name"].lower())
    known_names = set()
    for kind, el in c.elements():
        if el["id"] in known_ids:
            known_names |= {v.lower() for v in name_variants(el.get("name", ""))}
    for kind, el in c.elements():
        if el["id"] in known_ids:
            continue
        for v in name_variants(el.get("name", "")):
            if v.lower() not in known_names and v.lower() not in told_names:
                phrase("unknown place", v, case=True)

    # phenomena: a phenomenon's words with one of its true counts on the same line
    pp = os.path.join(c.S, "state", "phenomena.json")
    if os.path.exists(pp):
        try:
            ph = json.load(open(pp))
        except json.JSONDecodeError:
            ph = {}
        for pname, d in ph.items():
            words = [w for w in re.split(r"[-_\s]+", d.get("name", pname)) if len(w) >= 3]
            counts = sorted({v for v in d.get("per_year", {}).values() if isinstance(v, int) and v >= 2})
            if not words or not counts:
                continue
            stems = [r"\b" + re.escape(w[:4].lower()) for w in words]
            need = min(2, len(stems))
            num_rx = r"\b(?:" + "|".join(sum(([str(k)] + ([NUM_WORDS[k]] if k < len(NUM_WORDS) else []) for k in counts), [])) + r")\b"
            # lookaheads: at least `need` of the words, and a count
            look = "".join(f"(?=.*{s})" for s in stems[:need]) if need == len(stems) else \
                "(?=" + "|".join(f".*{a}.*{b}|.*{b}.*{a}" for i, a in enumerate(stems) for b in stems[i + 1:]) + ")"
            add("phenomenon count", pname, r"^" + look + r".*" + num_rx, re.I)

    # mystery titles and schedule titles
    for path in mystery_files(c):
        for title, _body in mystery_units(read(path)):
            t = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip(" .*")
            phrase("mystery title", t)
    es = os.path.join(c.S, "event-schedule.md")
    if os.path.exists(es):
        for m in re.finditer(r"^#{3,6}\s+(.+?)\s*$", read(es), re.M):
            t = re.sub(r"\s*\([^)]*\)\s*$", "", m.group(1)).strip()
            phrase("schedule title", t)
        for m in re.finditer(r"^\s*[-*]?\s*\*\*([^*]+?)\.?\*\*", read(es), re.M):
            phrase("schedule title", m.group(1).strip())

    # star values: a numeric result beside its item's words, or a result phrase of 3+ words
    sp = os.path.join(c.S, "star.md")
    if os.path.exists(sp):
        for line in read(sp).splitlines():
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells) < 3 or set(cells[0]) <= set("-: ") or cells[0].lower() == "item":
                continue
            item = re.sub(r"\s*\([^)]*\)", "", cells[0]).strip().lower()
            result = cells[-1]
            if not item:
                continue
            num = re.match(r"^(\d+)\b", result)
            if num:
                add("star value", f"{item} {num.group(1)}", r"^(?=.*\b" + re.escape(item) + r")" + r".*" + word_num_re(int(num.group(1))), re.I)
            else:
                head = re.split(r"[.:;]", result)[0].strip()
                if len(head.split()) >= 3:
                    phrase("star value", head)
    return terms


def check_leaks(c, rep):
    terms = leak_terms(c)
    for p in mapt.knowledge_problems(c.world, c.knowledge) if c.world else []:
        rep.fail("leaks", f"{c.rel(os.path.join(c.P, 'player', 'map-knowledge.json'))}: {p}")
    if not os.path.isdir(c.P):
        rep.warn("leaks", f"no public folder {c.rel(c.P)}")
        return
    for path in text_files(c.P):
        for ln, line in enumerate(read(path).splitlines(), 1):
            for kind, label, rx in terms:
                if rx.search(line):
                    rep.fail("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\"")


# ---------------------------------------------------------------- mysteries

def mystery_files(c):
    out = []
    p = os.path.join(c.S, "mysteries.md")
    if os.path.exists(p):
        out.append(p)
    d = os.path.join(c.S, "mysteries")
    if os.path.isdir(d):
        out += [x for x in text_files(d) if x.endswith(".md")]
    return out


UNIT_RE = re.compile(r"^(?:(#{2,4})\s+(.+?)\s*|\*\*([A-Z]{0,2}\d+\.\s+[^*]+?)\*\*.*)$", re.M)


def label_re(label):
    return re.compile(r"(?:^|\n|\.\s+|\*\*)\s*(?:#{2,6}\s*)?(?:\*\*)?" + re.escape(label) + r"(?:\*\*)?\s*(?:[:.,]|\*\*|\n|$)")


LABEL_RES = {l: label_re(l) for l in REQUIRED}


def mystery_units(text):
    """(title, body) for each heading or numbered bold paragraph that holds any required label."""
    starts = [(m.start(), m.group(2) or m.group(3), len(m.group(1) or "##")) for m in UNIT_RE.finditer(text)]
    units = []
    for i, (pos, title, level) in enumerate(starts):
        end = len(text)
        for pos2, _t, level2 in starts[i + 1:]:
            if level2 <= level or (title and re.match(r"[A-Z]{0,2}\d+\.", title) and re.match(r"[A-Z]{0,2}\d+\.", _t or "")):
                end = pos2
                break
        body = text[pos:end]
        # a unit's own text, up to the first nested unit that is not one of its labels, must hold a label
        nxt = next((p2 for p2, t2, _l in starts[i + 1:] if (t2 or "").strip(" .*") not in REQUIRED), len(text))
        own = text[pos:min(end, nxt)]
        if title.strip(" .*") in REQUIRED or not any(r.search(own) for r in LABEL_RES.values()):
            continue
        t = re.sub(r"^(?:EPIC|LONG\s*\d*|SHORT\s*\d*|[A-Z]{0,2}\d+)[.:]\s*", "", title.strip())
        units.append((t, body))
    return units


def section(body, label):
    m = LABEL_RES[label].search(body)
    if not m:
        return None
    rest = body[m.end():]
    nxt = [r.search(rest) for l, r in LABEL_RES.items() if l != label]
    cut = min([x.start() for x in nxt if x] + [len(rest)])
    return rest[:cut]


def check_mysteries(c, rep):
    files = mystery_files(c)
    if not files:
        rep.fail("mysteries", "no mysteries file")
        return
    total = 0
    for path in files:
        for title, body in mystery_units(read(path)):
            total += 1
            missing = [l for l in REQUIRED if not LABEL_RES[l].search(body)]
            if missing:
                rep.fail("mysteries", f"{c.rel(path)}: \"{title}\" lacks {'; '.join(missing)}")
            clues = section(body, "Clues")
            if clues is not None and not re.search(r"\breadings?\b", clues, re.I):
                rep.fail("mysteries", f"{c.rel(path)}: \"{title}\": no clue carries readings")
            branches = section(body, "Branches")
            if branches is not None and not re.search(r"\bworld does\b", branches, re.I):
                rep.fail("mysteries", f"{c.rel(path)}: \"{title}\": no branch says what the world does")
    if total == 0:
        rep.fail("mysteries", "no mystery found")


# ---------------------------------------------------------------- rolls

def check_rolls(c, rep):
    sys.path.insert(0, TOOLS)
    import roll as rollt
    logp = os.path.join(c.S, "state", "rolls.jsonl")
    entries = rollt.read_log(logp)
    ids = {}
    for i, e in enumerate(entries, 1):
        if not e:
            rep.fail("rolls", f"{c.rel(logp)}:{i}: unreadable line")
            continue
        rid = rollt.entry_id(e, i)
        if rid in ids:
            rep.fail("rolls", f"{c.rel(logp)}:{i}: id {rid} used twice")
        ids[rid] = e
        if e.get("id") and e["id"] != f"r-{i:04d}":
            rep.warn("rolls", f"{c.rel(logp)}:{i}: id {e['id']} is not its line number")
        if e.get("replaces"):
            if not e.get("reason"):
                rep.fail("rolls", f"{c.rel(logp)}:{i}: reroll of {e['replaces']} has no reason")
            if e["replaces"] not in ids:
                rep.fail("rolls", f"{c.rel(logp)}:{i}: replaces {e['replaces']}, which is not an earlier roll")
        elif re.search(r"\bre-?roll", e.get("what", ""), re.I) and not e.get("reason") and not re.search(r"reroll(?:ed)?\b[^,;]*\b(because|for|as|:)", e.get("what", ""), re.I):
            rep.warn("rolls", f"{c.rel(logp)}:{i}: a reroll named in `what` with no reason or replaces field")
    firsts = {}
    for rid, e in ids.items():
        if e.get("replaces"):
            continue
        firsts.setdefault(e.get("what", ""), []).append(rid)
    for what, rids in firsts.items():
        if len(rids) > 1:
            rep.fail("rolls", f"rolled more than once without a reroll reason: {', '.join(rids)}")
    for path in text_files(c.S):
        if os.path.basename(path) == "rolls.jsonl":
            continue
        for ln, line in enumerate(read(path).splitlines(), 1):
            for m in ROLL_RE.finditer(line):
                rid = f"r-{m.group(1)}"
                if rid not in ids:
                    rep.fail("rolls", f"{c.rel(path)}:{ln}: cites {rid}, which is not in the rolls log")
    pub = os.path.join(c.P, "state", "rolls.jsonl")
    if os.path.exists(pub) and any(l.strip() for l in open(pub)):
        rep.fail("rolls", f"{c.rel(pub)}: the public rolls log is not empty; rolls are sealed")


# ---------------------------------------------------------------- dashes

def check_dashes(c, rep):
    for base in (c.S, c.P):
        if not os.path.isdir(base):
            continue
        for path in text_files(base):
            for ln, line in enumerate(read(path).splitlines(), 1):
                n = line.count("\u2014") + line.count("\u2013")
                if n:
                    rep.fail("dashes", f"{c.rel(path)}:{ln}: {n} em or en dash(es)")


CHECKS = [("places", check_places), ("leaks", check_leaks), ("mysteries", check_mysteries),
          ("rolls", check_rolls), ("dashes", check_dashes)]


def main(argv=None):
    ap = argparse.ArgumentParser(description="StarFall lock checks")
    ap.add_argument("campaign")
    for name, _ in CHECKS:
        ap.add_argument(f"--{name}", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--root", default=os.path.dirname(TOOLS), help="repository root (default: this repository)")
    ap.add_argument("--counts-only", action="store_true", help="print only the count line per check")
    a = ap.parse_args(argv)
    chosen = [n for n, _ in CHECKS if getattr(a, n)]
    if a.all or not chosen:
        chosen = [n for n, _ in CHECKS]
    c = Campaign(os.path.abspath(a.root), a.campaign)
    rep = Report(a.counts_only)
    for name, fn in CHECKS:
        if name in chosen:
            fn(c, rep)
    return rep.summary(chosen)


if __name__ == "__main__":
    sys.exit(main())
