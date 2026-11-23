"""Lock checks a script can run for a campaign. The continuity checker runs these before
writing LOCKED.md, and reads every public file itself as well.

Usage: python3 tools/lockcheck.py <campaign> [--places] [--leaks] [--mysteries] [--rolls] [--dashes] [--all]
                                             [--root DIR] [--counts-only]
With no check named, --all. Exit 1 on any failure. One line per finding, then one count
line per check. Warnings are printed but do not fail. --counts-only prints the count lines
alone (for records kept outside the spoiler folder). --root points at another repository
layout (tests use a fixture).

  --places     every bracketed id like [r12], [f03] or [p01] in a sealed file exists in map.json;
               the map's own ids, neighbors and landings resolve; the continent's size
               passes (map.py continent_problems: 600 miles at the narrowest, 800 to 1,200 on
               average); warns on a capitalized map name written with no id after it, and on
               one written in lower case (a name of two or more words, a placeholder label,
               or a one-word name that is not a common word). Headings and bold mystery
               titles are not counted, and a name inside a longer map name is the longer one's.
               Aliases are never stamped (change list 38), so a bare alias is not warned on.
  --leaks      reads the sealed term list S/sealed-terms.txt, which the Keeper writes (god
               names and bynames, hidden power names, names in the common secrets, places
               off the map; one term per line, # for comments, matched as written, case
               and all, with or without a leading "The"; a term that is a map name the
               player's god has seen or been told is passed over, so a term is never
               removed from the file), and adds the terms the data
               gives: god folder labels, the count of gods, map names the player has not
               seen or been told, phenomena yearly counts, mystery titles (matched case
               and all), schedule titles and star values. Fails on any hit in
               campaigns/<name>/ or in the campaign's public scene requests: every .json
               under images/requests/ or images/held/, at any depth, whose file name or id
               starts with "<name>-" or whose campaign field is the campaign (the sealed
               image folders are not scanned), and on a missing sealed-terms.txt. Also
               fails a number word or numeral (two to twelve, 2 to 12, "a dozen", "half a dozen", "twice")
               within six words of "god", "gods", "like me", "like us", "of us", "pulls",
               "came down" or "fell" in the same sentence, and a public map-knowledge file
               that breaks the map rules. A number word that counts units or things ("two
               days", "seven acres", "Two things") is a work rate or a count, not a hit.
               The older guesses from prose (power card titles, Name lines, hidden-power
               headings, capitals in the common secrets) are warnings only. A map name is
               known to the god only once heard (map.py heard_name, change list 39): marked
               named, reported with no other name told, a told name, or a name the player
               gave the place itself; a place seen with no name heard keeps its map name
               sealed. A people's knowledge file, campaigns/<name>/civs/<people>/knowledge.md,
               holds what the people know of the land by their own names: a map name or alias
               there is told to the people, not to the god, so it is allowed in that file
               and is no leak (change list 46); every other sealed term still fails there.
               A term written in sealed-terms.txt with a leading "!" (the sealed factors'
               names are written so) is kept sealed everywhere: it is never let through as
               a name the player said in the open table talk, a known map name, a name in a
               people's knowledge file or a phrase in leak-allow.txt. The creation
               transcripts, P/player/transcript-day*.md, are the player's own words kept
               verbatim, and are not scanned for a kept term (the player using an ordinary
               word reveals nothing); every other public file is, so no agent writes one.
               S/leak-allow.txt, as the checker writes it (one phrase per line, quoted or
               not, a # comment after it or on its own line), exempts terms; a number-word
               hit is exempted by its quoted phrase, or by a longer allowed phrase that holds
               it and stands in the line.
  --mysteries  every mystery follows runbook template 7.8: Truth; Body; Cost if ignored;
               Clock or trigger; Clues; Branches; Never found, a Kind: line, an
               "Answers questions: yes|no" line, each clue with Location: and Readings:,
               each branch with What the world does:, and a Limit: line in the Truth or
               Body of every mystery marked "Answers questions: yes", the same limit word
               for word in S/cast.md (emphasis, map ids and punctuation aside); one epic,
               two or more long, three or more short.
  --rolls      every r-NNNN cited in a sealed file is in S/state/rolls.jsonl, nothing is
               rolled twice, every reroll has a reason; the public rolls log is empty.
  --dashes     no em or en dash in any campaign file, sealed or public, or in the campaign's
               image requests, scene or map (a JSON escape counts). Run alone, it needs no
               sealed folder: before Night 1 it reads the public folder alone (change list 2).

Every mode skips the checker's own flags files (any lock-flags*.md, years/000/lock-flags.md
among them): they quote what they flag.
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
SEALED_TERMS = "sealed-terms.txt"
KEPT_KIND = "kept sealed term"   # a "!" line in sealed-terms.txt: never exempted (decision 8)
# Number words near god terms (change list 44): a count of gods written in words.
COUNT_WORDS = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "twice", "a dozen", "half a dozen"]
GOD_TRIGGERS = ["god", "gods", "like me", "like us", "of us", "pulls", "came down", "fell"]
COUNT_WINDOW = 6   # words between the number word and the trigger, at most ("within six words")


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


def is_flags_file(path):
    """The checker's own flags files, which every mode skips: lock-flags.md and lock-flags*.md."""
    return re.match(r"^lock-flags.*\.md$", os.path.basename(path)) is not None


def text_files(folder):
    out = []
    for dirpath, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for fn in sorted(files):
            if os.path.splitext(fn)[1].lower() in TEXT_EXT and not is_flags_file(fn):
                out.append(os.path.join(dirpath, fn))
    return out


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return ""


class Campaign:
    def __init__(self, root, name, sealed_optional=False):
        self.root = root
        self.name = name
        self.S = os.path.join(root, "SPOILERS_do_not_open", "campaigns", name)
        self.P = os.path.join(root, "campaigns", name)
        self.sealed_missing = not os.path.isdir(self.S)
        if self.sealed_missing and not sealed_optional:
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
        ids |= {i for i in mapt.plane_ids(self.world) if i}
        return ids

    def elements(self):
        for el, layer in mapt.all_regions(self.world):
            yield "region", el
        for el, layer in mapt.all_features(self.world):
            yield "feature", el

    def allow(self):
        """S/leak-allow.txt as the checker writes it (checker.md): one phrase per line, each with a #
        comment giving its reason and date, on the same line after the phrase or on a line of its own.
        A phrase may be quoted. Returns the phrases, lower case, spaces collapsed."""
        p = os.path.join(self.S, "leak-allow.txt")
        if not os.path.exists(p):
            return set()
        return {ph for ph in (allow_phrase(l) for l in read(p).splitlines()) if ph}

    def sealed_terms(self, kept=None):
        """The Keeper's sealed term list, S/sealed-terms.txt: one term per line, # for comments,
        or None when the file is missing. A leading "!" marks a kept term (never exempted, see
        --leaks); it is stripped here. kept=True returns only the kept terms, kept=False only the others."""
        p = os.path.join(self.S, SEALED_TERMS)
        if not os.path.exists(p):
            return None
        out = []
        for line in read(p).splitlines():
            t = line.strip()
            if not t or t.startswith("#"):
                continue
            is_kept = t.startswith("!")
            t = t.lstrip("!").strip()
            if t and t not in out and (kept is None or kept == is_kept):
                out.append(t)
        return out


QUOTES = "\"'“”‘’`"


def allow_phrase(line):
    """The phrase on one leak-allow.txt line, or None for a comment or blank line: the text before
    an inline # comment, with any quotes around it removed, lower case, spaces collapsed."""
    t = line.strip()
    if not t or t.startswith("#"):
        return None
    m = re.match(r"^([\"“'‘`])(.+?)([\"”'’`])(?:\s*#.*|\s*)$", t)
    if m:
        t = m.group(2)
    else:
        t = re.split(r"\s+#", t, maxsplit=1)[0]
    t = " ".join(t.strip().strip(QUOTES).split()).lower()
    return t or None


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
    probs, _line = mapt.continent_problems(c.world)
    for p in probs:
        rep.fail("places", f"map.json: {p}")
    exempt = c.god_labels() | c.folder_names() | {"player"} | BRACKET_SKIP
    names = {}
    for kind, el in c.elements():
        # the map name only: aliases are never stamped (change list 38), so a bare alias is not warned on
        for nm in ([] if mapt.is_placeholder(el.get("name", "")) else [el.get("name", "")]):
            for v in name_variants(nm):
                names.setdefault(v, set()).add(el["id"])
    name_res = {v: re.compile(r"(?<![\w'])" + re.escape(v) + r"(?![\w])") for v in names}
    # lower-case references (change list 74): a name of two or more words, a placeholder label, or a
    # one-word name that is not a common word, written in lower case
    lower = {}
    for kind, el in c.elements():
        nm = el.get("name", "")
        core = mapt.name_core(nm)
        if not core or (" " not in core and (len(core) < 4 or mapt.is_common_word(core))):
            continue
        lower.setdefault(core.lower(), set()).add(el["id"])
    lower_res = {v: re.compile(r"(?<![\w'])" + r"\s+".join(re.escape(w) for w in v.split()) + r"(?![\w])", re.I) for v in lower}
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
        spans = mapt.heading_spans(text)   # headings and bold mystery titles are never stamped
        claimed = []

        def has_id(m, own):
            after = text[m.end():m.end() + 60]
            after = re.sub(r"^('s)?\s*(\([^)\n]*\)\s*)?", "", after)
            bm = re.match(r"\[([a-z0-9, -]+)\]", after)
            return bool(bm and set(re.split(r"\s*,\s*", bm.group(1))) & own)

        hits = []
        for v, rx in name_res.items():
            hits += [(m, v, names[v], "cap") for m in rx.finditer(text)]
        for v, rx in lower_res.items():
            hits += [(m, v, lower[v], "low") for m in rx.finditer(text) if m.group(0)[0].islower()]
        bare, bare_low = {}, {}
        # a name inside a longer map name ("Mastwater" in "Mastwater Vale [r05]") is the longer name's
        for m, v, own, how in sorted(hits, key=lambda h: (-(h[0].end() - h[0].start()), h[0].start())):
            if mapt.in_spans(m.start(), spans) or any(a <= m.start() < b or a < m.end() <= b for a, b in claimed):
                continue
            claimed.append((m.start(), m.end()))
            if has_id(m, own):
                continue
            (bare if how == "cap" else bare_low)[v] = (bare if how == "cap" else bare_low).get(v, 0) + 1
        for v in sorted(bare):
            rep.warn("places", f"{c.rel(path)}: map name \"{v}\" written {bare[v]} time(s) with no id")
        for v in sorted(bare_low):
            rep.warn("places", f"{c.rel(path)}: map name \"{v}\" written in lower case {bare_low[v]} time(s) with no id")


# ---------------------------------------------------------------- leaks

def word_num_re(n):
    alts = [str(n)]
    if 0 <= n < len(NUM_WORDS):
        alts.append(NUM_WORDS[n])
    return r"\b(?:" + "|".join(alts) + r")\b"


def element_index(c):
    return {el["id"]: el for _kind, el in c.elements()}


def heard_ids(c):
    """Ids whose map name the player's god has heard (map.py heard_name, change list 39): marked
    `"named": true`, or reported with no other name told. A place seen with no name heard, or known
    only by a told name, keeps its map name sealed."""
    els = element_index(c)
    out = set()
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            el = els.get(ident)
            if el is not None and e.get("grade") in ("seen", "reported") and mapt.heard_name(el, e) == el.get("name"):
                out.add(ident)
    return out


def unnamed_seen_regions(c):
    """Ids of regions the player's god has seen without their name: graded seen, not marked
    `"named": true` and with no told name (map.md 1.2). Their true names are sealed terms."""
    els = element_index(c)
    return {ident for ident, e in c.knowledge.get("regions", {}).items()
            if e.get("grade") == "seen" and not mapt.region_name_known(e, els.get(ident))}


def unheard_places(c):
    """Ids of regions and features the god has seen or had reported without hearing their map name
    (change list 39): their map names are sealed terms, though the ground is known."""
    return {ident for table in ("regions", "features") for ident, e in c.knowledge.get(table, {}).items()
            if e.get("grade") in ("seen", "reported")} - heard_ids(c)


def known_map_names(c):
    """Lower-case names the player's god knows: the map names it has heard (heard_ids), with and
    without a leading article, every name it was told, and every name the player gave a place itself
    (an alias by "player", change list 39)."""
    known_ids, out = heard_ids(c), set()
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            t = e.get("told") or {}
            if t.get("name"):
                out |= {v.lower() for v in article_variants(t["name"])}
    for kind, el in c.elements():
        for a in mapt.player_aliases(el):
            out |= {v.lower() for v in article_variants(a)} | {v.lower() for v in name_variants(a)}
        if el["id"] in known_ids:
            nm = el.get("name", "")
            out |= {v.lower() for v in article_variants(nm)} | {v.lower() for v in name_variants(nm)}
    return out


def player_said_text(c):
    """Everything the player posted in the open creation table talk (the "## Player:" sections of
    P/player/transcript-day*.md). A term found there is the player's own word, never a sealed term."""
    out = []
    folder = os.path.join(c.P, "player")
    if not os.path.isdir(folder):
        return ""
    for name in sorted(os.listdir(folder)):
        if not re.match(r"transcript-day\d+\.md$", name):
            continue
        part = None
        for line in read(os.path.join(folder, name)).splitlines():
            if line.startswith("## "):
                part = line.strip().lower().startswith("## player")
                continue
            if part:
                out.append(line)
    return "\n".join(out)


def leak_terms(c):
    """(kind, label, compiled regex, severity) for every sealed term. Severity is "fail" for the
    Keeper's sealed-terms.txt and the terms the data gives, "warn" for the older guesses from prose."""
    terms = []
    allow = c.allow()
    severity = ["fail"]

    def add(kind, label, rx, flags=0):
        if label.lower() in allow:
            return
        terms.append((kind, label, re.compile(rx, flags), severity[0]))

    def phrase(kind, s, case=False):
        s = s.strip()
        if len(s) < 3:
            return
        add(kind, s, r"(?<![\w])" + re.escape(s) + r"(?![\w])", 0 if case else re.I)

    known_lower = known_map_names(c)
    said = player_said_text(c)
    # kept terms (a leading "!"): no exemption of any kind, the allow file included (decision 8)
    for t in c.sealed_terms(kept=True) or []:
        for v in sorted(article_variants(t)):
            if len(v.strip()) >= 3:
                terms.append((KEPT_KIND, v.strip(), re.compile(r"(?<![\w])" + re.escape(v.strip()) + r"(?![\w])"), "fail"))
    for t in c.sealed_terms(kept=False) or []:
        if {v.lower() for v in article_variants(t)} & known_lower:
            continue  # a map name the player's god has seen or been told may appear (runbook 7.12)
        if re.search(r"(?<![\w])" + re.escape(t) + r"(?![\w])", said):
            continue  # a name the player said in the open table talk is never sealed (Michael, 2026-11-22)
        for v in sorted(article_variants(t)):
            phrase("sealed term", v, case=True)
    for label in sorted(c.god_labels()):
        phrase("god label", label)
    # the older guesses from prose: warnings only (change list 30)
    severity[0] = "warn"
    gnames = set()
    for god in c.npc_gods():
        for path in text_files(os.path.join(c.S, "gods", god)) + text_files(os.path.join(c.S, "gods-sealed", god)):
            t = read(path)
            gnames |= set(re.findall(r"^#\s*Power card:\s*(.+?)\s*$", t, re.M))
            gnames |= set(re.findall(r"^\**Name\**:\**\s*([A-Z][\w' -]+?)\s*\.?\s*$", t, re.M))
            gnames |= set(re.findall(r"\bI name myself ([A-Z][\w'-]+)", t))
    for n in sorted(gnames):
        phrase("god name", n, case=True)
    # hidden power names, the player's and every NPC god's (their ### headings)
    hp_files = [os.path.join(c.S, "player", "hidden-powers.md")]
    hp_files += [os.path.join(c.S, "gods-sealed", g, "hidden-powers.md") for g in sorted(c.god_labels())]
    for path in hp_files:
        for m in re.finditer(r"^#{2,4}\s+(.+?)\s*$", read(path), re.M):
            t = m.group(1).strip()
            if t.lower() not in ("ceiling", "growth", "notes"):
                for v in name_variants(t) or {t}:
                    phrase("hidden power", v, case=True)
    # names in the common past (S/gods-sealed/common-past.md, or any file at the top of gods-sealed)
    gs = os.path.join(c.S, "gods-sealed")
    for path in sorted(os.path.join(gs, f) for f in (os.listdir(gs) if os.path.isdir(gs) else []) if f.endswith(".md")):
        for nm in common_names(read(path)):
            for v in name_variants(nm) or {nm}:
                phrase("common-past name", v, case=True)
    severity[0] = "fail"
    n = len(c.npc_gods())
    if n:
        for k in sorted({n, n + 1}):
            add("god count", f"{k} gods", word_num_re(k) + r"\s+(?:other\s+|more\s+|npc\s+|rival\s+|living\s+)?(?:gods|deities)\b", re.I)

    # places the player has not seen or been told; names it was told are known to it. A region seen
    # without its name keeps its true name sealed (map.md 1.2): its ground is known, its name is not.
    known_ids, told_names = heard_ids(c), set()
    unnamed = unnamed_seen_regions(c)
    unheard = unheard_places(c)
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            t = e.get("told") or {}
            if t.get("name"):
                told_names.add(t["name"].lower())
    for kind, el in c.elements():
        told_names |= {a.lower() for a in mapt.player_aliases(el)}
    known_names = set()
    for kind, el in c.elements():
        if el["id"] in known_ids:
            known_names |= {v.lower() for v in name_variants(el.get("name", ""))}
    for kind, el in c.elements():
        if el["id"] in known_ids:
            continue
        kind_ = ("unnamed seen region" if kind == "region" and el["id"] in unnamed else
                 "unheard map name" if el["id"] in unheard else "unknown place")
        for v in name_variants(el.get("name", "")):
            if v.lower() not in known_names and v.lower() not in told_names:
                phrase(kind_, v, case=True)

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
            phrase("mystery title", t, case=True)
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


STOP_CAPS = {"The", "This", "That", "These", "Those", "There", "Their", "They", "What", "When", "Where", "Which",
             "While", "With", "Without", "From", "Into", "Over", "Under", "After", "Before", "Year", "Years",
             "Night", "Day", "Days", "Keeper", "Truth", "Table", "God", "Gods", "None", "Each", "Every", "Some",
             "Most", "Many", "Only", "Both", "Also", "Then", "Here", "Even", "Never", "Always", "Pacific"}


def common_names(text):
    """Proper names in a common-past file: the name after a colon in its title, and capitalized
    words of four or more letters met mid-sentence that the file never writes in lower case."""
    names = set()
    m = re.search(r"^#\s+[^:\n]+:\s*(.+?)\s*$", text, re.M)
    if m:
        names.add(m.group(1).strip())
    lower = set(re.findall(r"\b[a-z][a-z'-]+\b", text))
    for m in re.finditer(r"(?<=[a-z,;] )([A-Z][a-z'-]{3,}(?: [A-Z][a-z'-]{3,})*)", text):
        nm = m.group(1)
        words = nm.split()
        if any(w in STOP_CAPS for w in words) or all(w.lower() in lower for w in words):
            continue
        names.add(nm)
    return names


def request_files(c, sealed=False):
    """The campaign's image request files (change list 83): every .json under images/requests/ and
    images/held/ (any depth, so an older images/requests/held/ too) whose file name or `id` starts with
    "<name>-" or whose `campaign` field is the campaign. With sealed=True, the same under
    SPOILERS_do_not_open/images/ (map requests), which the leak scan never reads."""
    base = os.path.join(c.root, "SPOILERS_do_not_open", "images") if sealed else os.path.join(c.root, "images")
    out = []
    for sub in ("requests", "held"):
        d = os.path.join(base, sub)
        if not os.path.isdir(d):
            continue
        for dirpath, dirs, files in os.walk(d):
            dirs[:] = sorted(x for x in dirs if not x.startswith("."))
            for f in sorted(files):
                if not f.endswith(".json"):
                    continue
                path = os.path.join(dirpath, f)
                mine = f.startswith(c.name + "-")
                if not mine:
                    try:
                        j = json.loads(read(path) or "{}")
                    except json.JSONDecodeError:
                        j = {}
                    if isinstance(j, dict):
                        mine = str(j.get("id", "")).startswith(c.name + "-") or j.get("campaign") == c.name
                if mine and path not in out:
                    out.append(path)
    return out


def public_files(c):
    """Every text file under campaigns/<name>/, plus the campaign's public scene requests, waiting or
    held (request_files). SPOILERS_do_not_open/images/ is sealed and not scanned for leaks."""
    out = text_files(c.P) if os.path.isdir(c.P) else []
    return out + request_files(c)


def article_variants(term):
    """A sealed term as written, and without a leading article if what is left is two or more
    words (a one-word remainder, "the Stray", is matched only with its article: alone it is
    an ordinary word at the head of a sentence)."""
    out = {term}
    m = re.match(r"^(The|the|A|An|an)\s+(.+)$", term)
    if m and len(m.group(2).split()) >= 2:
        out.add(m.group(2))
    return out


def _words_re(phrase):
    return r"\s+".join(re.escape(w) for w in phrase.split())


COUNT_RE = re.compile(r"(?<![\w-])(?:" + "|".join(_words_re(w) for w in sorted(COUNT_WORDS, key=len, reverse=True)) + r")(?![\w-])"
                      r"|(?<![\w.,-])(?:1[0-2]|[2-9])(?![\w-]|[.,]\d)", re.I)   # numerals 2 to 12 count alike
TRIGGER_RE = re.compile(r"(?<![\w])(?:" + "|".join(_words_re(w) for w in sorted(GOD_TRIGGERS, key=len, reverse=True)) + r")(?![\w])", re.I)
WORD_RE = re.compile(r"[A-Za-z0-9']+")
# a numeral that names a day, night, year, question or step is a label, not a count ("Day 3", "question 8")
LABEL_BEFORE_RE = re.compile(r"(?<![\w-])(?:day|days|night|nights|year|years|q|question|questions|item|items|step|steps|"
                             r"round|rounds|section|sections|rule|rules|line|lines|page|chapter|number|no|part|act|scene)\s*#?\s*$", re.I)
SENTENCE_RE = re.compile(r"(?:[^.!?;:]|(?<=\d)[.:](?=\d))+")   # "2.5" and "3:10" do not end a sentence
# A number word that counts units of time, distance, area or work, or things in a list, is a work rate
# or a count, not a count of gods (change list 30): "two days", "seven acres", "Two things about this god".
UNIT_NOUNS = ["days", "day", "nights", "night", "weeks", "week", "months", "month", "years", "year", "seasons", "season",
              "hours", "hour", "miles", "mile", "yards", "yard", "feet", "foot", "acres", "acre", "worker-days", "worker-day",
              "worker days", "tons", "ton", "pounds", "pound", "loads", "load", "furlongs", "leagues",
              "things", "thing", "matters", "questions", "points", "parts", "ways", "words", "steps", "times"]
UNIT_MODIFIERS = ["full", "whole", "more", "long", "short", "hard", "good", "working", "square", "cubic", "hundred", "thousand"]
UNIT_AFTER_RE = re.compile(r"^\s+(?:(?:" + "|".join(UNIT_MODIFIERS) + r")\s+)?(?:" +
                           "|".join(_words_re(w) for w in sorted(UNIT_NOUNS, key=len, reverse=True)) + r")(?![\w-])", re.I)


def is_unit_count(sent, m):
    """True when the number word at match m counts units or things: "two days", "five full acres"."""
    return m.group(0).lower() != "twice" and UNIT_AFTER_RE.match(sent[m.end():]) is not None


def count_hits(line):
    """Number words within COUNT_WINDOW words of a god term in the same sentence: (number word,
    trigger, the phrase between them inclusive) for each pair."""
    hits = []
    for sm in SENTENCE_RE.finditer(line):
        sent = sm.group(0)
        starts = [m.start() for m in WORD_RE.finditer(sent)]

        def word_index(pos):
            i = 0
            for k, s in enumerate(starts):
                if s <= pos:
                    i = k
            return i

        nums = [(m, word_index(m.start()), word_index(m.end() - 1)) for m in COUNT_RE.finditer(sent)
                if not (m.group(0).isdigit() and LABEL_BEFORE_RE.search(sent[:m.start()])) and not is_unit_count(sent, m)]
        trigs = [(m, word_index(m.start()), word_index(m.end() - 1)) for m in TRIGGER_RE.finditer(sent)]
        for n, n0, n1 in nums:
            for t, t0, t1 in trigs:
                if t0 <= n1 and n0 <= t1:
                    continue  # overlapping ("one" inside nothing, but be safe)
                gap = (t0 - n1 - 1) if t0 > n1 else (n0 - t1 - 1)
                if gap <= COUNT_WINDOW:
                    a, b = min(n.start(), t.start()), max(n.end(), t.end())
                    hits.append((n.group(0), t.group(0), " ".join(sent[a:b].split())))
    return hits


PEOPLE_KNOWLEDGE_RE = re.compile(r"^civs/[^/]+/knowledge\.md$")
TRANSCRIPT_RE = re.compile(r"^player/transcript-day\d+\.md$")
MAP_NAME_KINDS = {"unknown place", "unnamed seen region", "unheard map name"}


def is_people_knowledge(c, path):
    """True for a people's knowledge file, campaigns/<name>/civs/<people>/knowledge.md (change list 46)."""
    rel = os.path.relpath(path, c.P).replace(os.sep, "/")
    return not rel.startswith("..") and PEOPLE_KNOWLEDGE_RE.match(rel) is not None


def is_transcript(c, path):
    """True for a creation transcript, campaigns/<name>/player/transcript-dayN.md: the player's own
    words, kept verbatim, never scanned for a kept term."""
    rel = os.path.relpath(path, c.P).replace(os.sep, "/")
    return not rel.startswith("..") and TRANSCRIPT_RE.match(rel) is not None


def map_names_lower(c):
    """Every map name and alias in map.json, lower case, with and without a leading article."""
    out = set()
    for _kind, el in c.elements():
        for nm in [el.get("name", "")] + [a["name"] for a in el.get("aliases") or [] if isinstance(a, dict) and isinstance(a.get("name"), str)]:
            if nm:
                out |= {v.lower() for v in article_variants(nm.strip())} | {v.lower() for v in name_variants(nm.strip())}
    return out


def check_leaks(c, rep):
    terms = leak_terms(c)
    allow = c.allow()
    place_names = map_names_lower(c)

    def told_to_people(kind, label):
        """A map name (or alias) in a people's knowledge file is told to the people, not to the god:
        allowed there, and no leak (change list 46). Every other sealed term still fails there,
        and a kept term always does."""
        return kind != KEPT_KIND and (kind in MAP_NAME_KINDS or label.lower() in place_names)
    if c.sealed_terms() is None:
        rep.fail("leaks", f"{c.rel(os.path.join(c.S, SEALED_TERMS))} is missing; the Keeper writes it "
                          "(god names and bynames, hidden power names, common-secrets names, places off the map)")
    for p in mapt.knowledge_problems(c.world, c.knowledge) if c.world else []:
        rep.fail("leaks", f"{c.rel(os.path.join(c.P, 'player', 'map-knowledge.json'))}: {p}")
    if not os.path.isdir(c.P):
        rep.warn("leaks", f"no public folder {c.rel(c.P)}")
    for path in public_files(c):
        people = is_people_knowledge(c, path)
        transcript = is_transcript(c, path)
        for ln, line in enumerate(read(path).splitlines(), 1):
            failed_labels = set()
            for kind, label, rx, sev in terms:
                if people and told_to_people(kind, label):
                    continue
                if transcript and kind == KEPT_KIND:
                    continue  # the player's own words, kept verbatim (decision 8)
                if sev == "fail" and rx.search(line):
                    failed_labels.add(label.lower())
                    rep.fail("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\"")
            for kind, label, rx, sev in terms:
                if people and told_to_people(kind, label):
                    continue
                if sev == "warn" and label.lower() not in failed_labels and rx.search(line):
                    rep.warn("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\" (a guess from prose; "
                                      "add it to sealed-terms.txt if it is sealed)")
            low_line = " ".join(line.split()).lower()
            for num, trig, phrase_ in count_hits(line):
                ph = " ".join(phrase_.split()).lower()
                # exempt by its quoted phrase, or by a longer allowed phrase that holds it and stands in the line
                if ph in allow or any(ph in a and a in low_line for a in allow):
                    continue
                rep.fail("leaks", f"{c.rel(path)}:{ln}: number word \"{num}\" near \"{trig}\": \"{phrase_}\"")


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
        t = re.sub(r"^(?:EPIC|LONG\s*\d*|SHORT\s*\d*|[A-Z]{0,2}\d+)(?:[.:]\s*|\s+)", "", title.strip())
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


KIND_RE = re.compile(r"^\s*Kind:\s*(epic|long|short)\b", re.I | re.M)
ANSWERS_FIELD_RE = re.compile(r"(?:^|[.;]\s*|\*\*)\s*\**Answers questions\**:\**\s*([A-Za-z]*)", re.M)


LIMIT_LINE_RE = re.compile(r"^\s*(?:[-*]\s+)?\**Limit\**:\**\s*(\S.*?)\s*$", re.M)


def limit_words(text):
    """A Limit: line as its words, for a word-for-word comparison: markdown emphasis, bracketed map ids
    and punctuation are set aside, case is kept."""
    t = re.sub(r"\[[a-z0-9, -]+\]", " ", text.replace("*", "").replace("_", " "))
    return tuple(re.findall(r"[\w']+(?:-[\w']+)*", t))


def chunks(sec):
    """A section's #### sub-entries (clues or branches), or None when it has none."""
    parts = re.split(r"^####\s+.*$", sec, flags=re.M)
    heads = re.findall(r"^####\s+(.*)$", sec, flags=re.M)
    return list(zip(heads, parts[1:])) if heads else None


def check_mysteries(c, rep):
    """Template 7.8 of the creation runbook: headings in order, a Kind line, clues with
    Location and Readings, branches with What the world does, a Limit line for a being that
    answers questions; one epic, two or more long, three or more short."""
    files = mystery_files(c)
    if not files:
        rep.fail("mysteries", "no mysteries file")
        return
    total = 0
    kinds = {"epic": 0, "long": 0, "short": 0}
    cast_path = os.path.join(c.S, "cast.md")
    cast = {limit_words(m.group(1)) for m in LIMIT_LINE_RE.finditer(read(cast_path))} if os.path.exists(cast_path) else None
    for path in files:
        for title, body in mystery_units(read(path)):
            total += 1
            where = f"{c.rel(path)}: \"{title}\""
            missing = [l for l in REQUIRED if not LABEL_RES[l].search(body)]
            if missing:
                rep.fail("mysteries", f"{where} lacks {'; '.join(missing)}")
            k = KIND_RE.search(body)
            if k:
                kinds[k.group(1).lower()] += 1
            else:
                rep.fail("mysteries", f"{where}: no Kind: line (epic, long or short)")
            clues = section(body, "Clues")
            if clues is not None:
                items = chunks(clues)
                if items:
                    for name, text in items:
                        if not re.search(r"^\s*Location:\s*\S", text, re.M):
                            rep.fail("mysteries", f"{where}: clue \"{name.strip()}\" has no Location:")
                        if not re.search(r"^\s*Readings:\s*\S", text, re.M):
                            rep.fail("mysteries", f"{where}: clue \"{name.strip()}\" has no Readings:")
                else:
                    if not re.search(r"\breadings?\b", clues, re.I):
                        rep.fail("mysteries", f"{where}: no clue carries readings")
                    if not re.search(r"\bLocation:", clues):
                        rep.fail("mysteries", f"{where}: no clue carries a Location:")
            branches = section(body, "Branches")
            if branches is not None:
                items = chunks(branches)
                if items:
                    for name, text in items:
                        if not re.search(r"^\s*What the world does:\s*\S", text, re.M):
                            rep.fail("mysteries", f"{where}: branch \"{name.strip()}\" has no What the world does:")
                elif not re.search(r"\bworld does\b", branches, re.I):
                    rep.fail("mysteries", f"{where}: no branch says what the world does")
            answers = ANSWERS_FIELD_RE.findall(body)
            if not answers:
                rep.fail("mysteries", f"{where}: no Answers questions: line (yes or no)")
            elif len(answers) > 1:
                rep.fail("mysteries", f"{where}: more than one Answers questions: line")
            elif answers[0].lower() not in ("yes", "no"):
                rep.fail("mysteries", f"{where}: Answers questions: must be yes or no, not {answers[0]!r}")
            elif answers[0].lower() == "yes":
                being = (section(body, "Truth") or "") + "\n" + (section(body, "Body") or "")
                limits = [m.group(1) for m in LIMIT_LINE_RE.finditer(being)]
                if not limits:
                    rep.fail("mysteries", f"{where}: Answers questions: yes, but no Limit: line in its Truth or Body")
                for lim in limits:   # the same limit, word for word, in S/cast.md (change list 67)
                    if cast is None:
                        rep.fail("mysteries", f"{where}: its Limit: line has no copy, since {c.rel(cast_path)} is missing")
                    elif limit_words(lim) not in cast:
                        rep.fail("mysteries", f"{where}: its Limit: line is not in {c.rel(cast_path)} word for word: \"{lim.strip()}\"")
    if total == 0:
        rep.fail("mysteries", "no mystery found")
        return
    if kinds["epic"] != 1 or kinds["long"] < 2 or kinds["short"] < 3:
        rep.fail("mysteries", f"kinds: {kinds['epic']} epic, {kinds['long']} long, {kinds['short']} short; "
                              "the lock needs one epic, two or more long, three or more short")


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
    paths = []
    for base in (c.S, c.P):
        if os.path.isdir(base):
            paths += text_files(base)
    paths += request_files(c) + request_files(c, sealed=True)   # the campaign's image requests too (83)
    for path in paths:
        for ln, line in enumerate(read(path).splitlines(), 1):
            n = line.count("\u2014") + line.count("\u2013")
            if path.endswith((".json", ".jsonl")):   # a dash written as a JSON escape
                n += len(re.findall(r"\\u201[34]", line, re.I))
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
    # --dashes alone runs on the public folder when the sealed folder does not exist yet (Day 1, change list 2)
    c = Campaign(os.path.abspath(a.root), a.campaign, sealed_optional=chosen == ["dashes"])
    if c.sealed_missing:
        if not os.path.isdir(c.P):
            sys.exit(f"lockcheck: no campaign at {c.P} or {c.S}")
        print(f"note: no sealed campaign at {c.rel(c.S)} yet; --dashes reads the public folder alone")
    rep = Report(a.counts_only)
    for name, fn in CHECKS:
        if name in chosen:
            fn(c, rep)
    return rep.summary(chosen)


if __name__ == "__main__":
    sys.exit(main())
