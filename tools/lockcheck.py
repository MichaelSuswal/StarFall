"""Lock checks a script can run for a campaign. The continuity checker runs these before
writing LOCKED.md, and reads every public file itself as well.

Usage: python3 tools/lockcheck.py <campaign> [--places] [--leaks] [--mysteries] [--rolls] [--dashes] [--all]
                                             [--root DIR] [--counts-only]
With no check named, --all. Exit 1 on any failure. One line per finding, then one count
line per check. Warnings are printed but do not fail. --counts-only prints the count lines
alone (for records kept outside the spoiler folder). --root points at another repository
layout (tests use a fixture).

  --places     every bracketed id like [r12], [f03] or [p01] in a sealed file exists in map.json;
               the map's own ids, neighbors and landings resolve; warns on a capitalized
               map name written with no id after it.
  --leaks      reads the sealed term list S/sealed-terms.txt, which the Keeper writes (god
               names and bynames, hidden power names, names in the common secrets, places
               off the map; one term per line, # for comments, matched as written, case
               and all, with or without a leading "The"; a term that is a map name the
               player's god has seen or been told is passed over, so a term is never
               removed from the file), and adds the terms the data
               gives: god folder labels, the count of gods, map names the player has not
               seen or been told, phenomena yearly counts, mystery titles (matched case
               and all), schedule titles and star values. Fails on any hit in
               campaigns/<name>/ or in the campaign's public scene requests,
               images/requests/<name>-*.json and images/held/<name>-*.json (the sealed
               held folder is not scanned), and on a missing sealed-terms.txt. Also
               fails a number word or numeral (two to twelve, 2 to 12, "a dozen", "half a dozen", "twice")
               within six words of "god", "gods", "like me", "like us", "of us", "pulls",
               "came down" or "fell" in the same sentence, and a public map-knowledge file
               that breaks the map rules. The older guesses from prose (power card
               titles, Name lines, hidden-power headings, capitals in the common secrets)
               are warnings only. S/leak-allow.txt (one term per line, # for comments)
               exempts terms; a number-word hit is exempted by its quoted phrase.
  --mysteries  every mystery follows runbook template 7.8: Truth; Body; Cost if ignored;
               Clock or trigger; Clues; Branches; Never found, a Kind: line, an
               "Answers questions: yes|no" line, each clue with Location: and Readings:,
               each branch with What the world does:, and a Limit: line in the Truth or
               Body of every mystery marked "Answers questions: yes"; one epic, two or
               more long, three or more short.
  --rolls      every r-NNNN cited in a sealed file is in S/state/rolls.jsonl, nothing is
               rolled twice, every reroll has a reason; the public rolls log is empty.
  --dashes     no em or en dash in any campaign file, sealed or public.

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
        ids |= {i for i in mapt.plane_ids(self.world) if i}
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

    def sealed_terms(self):
        """The Keeper's sealed term list, S/sealed-terms.txt: one term per line, # for comments,
        or None when the file is missing."""
        p = os.path.join(self.S, SEALED_TERMS)
        if not os.path.exists(p):
            return None
        out = []
        for line in read(p).splitlines():
            t = line.strip()
            if t and not t.startswith("#") and t not in out:
                out.append(t)
        return out


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


def known_map_names(c):
    """Lower-case names the player's god knows: the map names of what it has seen or had reported,
    with and without a leading article, and every name it was told."""
    known_ids, out = set(), set()
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            if e.get("grade") in ("seen", "reported"):
                known_ids.add(ident)
            t = e.get("told") or {}
            if t.get("name"):
                out |= {v.lower() for v in article_variants(t["name"])}
    for kind, el in c.elements():
        if el["id"] in known_ids:
            nm = el.get("name", "")
            out |= {v.lower() for v in article_variants(nm)} | {v.lower() for v in name_variants(nm)}
    return out


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
    for t in c.sealed_terms() or []:
        if {v.lower() for v in article_variants(t)} & known_lower:
            continue  # a map name the player's god has seen or been told may appear (runbook 7.12)
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


def public_files(c):
    """Every text file under campaigns/<name>/, plus the campaign's public scene requests, waiting or
    held: images/requests/<name>-*.json and images/held/<name>-*.json (and an older
    images/requests/held/). SPOILERS_do_not_open/images/held/ is sealed and not scanned."""
    out = text_files(c.P) if os.path.isdir(c.P) else []
    for req in (os.path.join(c.root, "images", "requests"), os.path.join(c.root, "images", "held"),
                os.path.join(c.root, "images", "requests", "held")):
        if os.path.isdir(req):
            out += sorted(os.path.join(req, f) for f in os.listdir(req)
                          if f.startswith(c.name + "-") and f.endswith(".json"))
    return out


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
                if not (m.group(0).isdigit() and LABEL_BEFORE_RE.search(sent[:m.start()]))]
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


def check_leaks(c, rep):
    terms = leak_terms(c)
    allow = c.allow()
    if c.sealed_terms() is None:
        rep.fail("leaks", f"{c.rel(os.path.join(c.S, SEALED_TERMS))} is missing; the Keeper writes it "
                          "(god names and bynames, hidden power names, common-secrets names, places off the map)")
    for p in mapt.knowledge_problems(c.world, c.knowledge) if c.world else []:
        rep.fail("leaks", f"{c.rel(os.path.join(c.P, 'player', 'map-knowledge.json'))}: {p}")
    if not os.path.isdir(c.P):
        rep.warn("leaks", f"no public folder {c.rel(c.P)}")
    for path in public_files(c):
        for ln, line in enumerate(read(path).splitlines(), 1):
            failed_labels = set()
            for kind, label, rx, sev in terms:
                if sev == "fail" and rx.search(line):
                    failed_labels.add(label.lower())
                    rep.fail("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\"")
            for kind, label, rx, sev in terms:
                if sev == "warn" and label.lower() not in failed_labels and rx.search(line):
                    rep.warn("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\" (a guess from prose; "
                                      "add it to sealed-terms.txt if it is sealed)")
            for num, trig, phrase_ in count_hits(line):
                if phrase_.lower() in allow:
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
                being = (section(body, "Truth") or "") + (section(body, "Body") or "")
                if not re.search(r"^\s*\**Limit\**:\**\s*\S", being, re.M):
                    rep.fail("mysteries", f"{where}: Answers questions: yes, but no Limit: line in its Truth or Body")
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
