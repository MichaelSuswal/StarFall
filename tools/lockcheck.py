"""Lock checks a script can run for a campaign. The continuity checker runs these before
writing LOCKED.md, and reads every public file itself as well.

Usage: python3 tools/lockcheck.py <campaign> [--places] [--leaks] [--releases] [--mysteries] [--rolls] [--dashes] [--all]
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
               The files map.py stamp skips (the keeper log, LOCKED.md and the files a god's agent
               writes in S/gods/<god>/, change list 56) are not warned on for a bare name; their
               bracketed ids are still checked.
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
               Build 6: a number word before a fraction word ("three quarters", "two thirds") or a
               numeral fraction (3/4) is no count (change list 23). In a people's knowledge file another
               people's name (a sealed term whose form without "the" is a people's folder label) passes
               only when told to them in their record: S/civs/<people>/record.md or P/civs/<people>/record.md
               (change list 55). S/civs/<people>-sealed.md is the world's side, told to no one, and never
               counts as told (build 6 check, must-fix 3). The campaign's timing file is sealed,
               S/state/timing.md (change list 74): a public P/state/timing.md is warned on, to be moved,
               and is not scanned for ordinals.
               Build 7 (run 06 change list): on Day 1, before Night 1 has written S/sealed-terms.txt (the
               clock at creation night 1 and no Night 1 work in the sealed folder: no world-draft.md,
               star.md, map.json or gods/), a missing file is "no sealed terms yet", a pass, and --leaks
               runs with no sealed folder at all (1). The creation transcripts are not scanned for number
               words either, the DM's own posts in them included (12). In P/player/power-card.md the frozen
               terms (Description: and Drawback: lines, and the list under "Limits settled at creation:")
               are not scanned for number words; every other line of the card is (13). The play
               transcripts, P/player/transcript-year-NNN.md, are verbatim records as the creation
               transcripts are (96): in their "## Player:" and "## DM:" sections no kept term and no number
               word is scanned (an ordinary sealed term still is, as in the creation transcripts' DM posts);
               any other line of them is scanned in full. A line-level allow (71):
               a leak-allow.txt line `in <file>: "<phrase>"` exempts that phrase only on a line of that file
               holding it (the file as campaigns/<name>/..., P/... or a path inside the public folder), so
               a count once seen is allowed where it stands and nowhere else. A phenomenon's label in
               leak-allow.txt still exempts its counts, as before, and is warned on every run, since it
               lets every count through, a year to come's included. The sealed civ files (78): every text
               file of S/civs/<people>/ for each people a civ agent plays (not S/civs/godless/ or the Keeper's
               S/civs/<people>-sealed.md) fails on a kept sealed term, since a civ agent cannot be told to avoid
               the word; so night-turn step 4's --leaks covers them.
  --releases   the Keeper's releases (every .md under S/releases/) and the Day 3 brief,
               P/player/day3-brief.md, against the world draft (change list 37): a sentence naming one
               of the world's scarce things (the items of a "Scarcities:", "World scarcities:" or "Local
               shortages:" line of S/world-draft.md) beside a word of scarcity ("scarce", "rare", "dear",
               "came short") is warned on, for the Keeper to reword or keep by reading; a kept sealed term
               fails in any of them.
  --mysteries  every mystery follows runbook template 7.8: Truth; Body; Cost if ignored;
               Clock or trigger; Clues; Branches; Never found, a Kind: line, an
               "Answers questions: yes|no" line, each clue with Location: and Readings:,
               each branch with What the world does:, and a Limit: line in the Truth or
               Body of every mystery marked "Answers questions: yes", the same limit word
               for word in S/cast.md (emphasis, map ids and punctuation aside); one epic,
               two or more long, three or more short. Each cast being's "Mysteries:" pointers name
               mysteries that exist, and a being with a Limit: line (it answers questions) is in no
               mystery marked "Answers questions: no" (change list 71).
  --rolls      every r-NNNN cited in a sealed file is in S/state/rolls.jsonl, nothing is
               rolled twice, every reroll has a reason. The DM's open rolls stay in the public log,
               P/state/rolls.jsonl, with ids dm-NNNN (Michael, 2026-11-24 22:06; run 06 change list 70):
               every line there is the DM's, its rerolls have a reason, nothing is rolled twice
               (tools/roll.py public_log_problems), and every dm-NNNN cited in any campaign file is in it.
               An older public line with an r-NNNN id (before build 7) is warned on, never failed.
  --dashes     no em or en dash in any campaign file, sealed or public, or in the campaign's
               image requests, scene or map (a JSON escape counts). Run alone, it needs no
               sealed folder: before Night 1 it reads the public folder alone (change list 2).

Every mode skips the checker's own flags files (any lock-flags*.md, years/000/lock-flags.md
among them, and every year's years/NNN/flags.md and flags-K.md, build 8, run 07 change list 26): they quote what they flag.
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
DM_ROLL_RE = re.compile(r"(?<![\w-])dm-(\d{4,})\b")   # the DM's open rolls, in the public log (change list 70)
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
    """The checker's own flags files, which every mode skips: lock-flags.md and lock-flags*.md, and a
    year's years/NNN/flags.md (change list 26) or flags-K.md (a night after the clock waited), the night checker's
    file, which quotes what it flags."""
    if re.match(r"^lock-flags.*\.md$", os.path.basename(path)):
        return True
    parts = os.path.normpath(path).split(os.sep)
    # flags.md, and flags-K.md on a night after the clock waited (engine/night/night-turn.md; build check finding 2)
    return (len(parts) >= 3 and re.fullmatch(r"flags(?:-\d+)?\.md", parts[-1]) is not None and parts[-3] == "years"
            and re.fullmatch(r"\d{3}", parts[-2]) is not None)


def text_files(folder):
    out = []
    for dirpath, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for fn in sorted(files):
            if os.path.splitext(fn)[1].lower() in TEXT_EXT and not is_flags_file(os.path.join(dirpath, fn)):
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
        return {ph for ph in (allow_phrase(l) for l in read(p).splitlines() if not LINE_ALLOW_RE.match(l.strip())) if ph}

    def allow_lines(self):
        """The line-level allows of S/leak-allow.txt (change list 71): (file, phrase) for each line
        `in <file>: "<phrase>"`, the file normalized to its path inside the public folder, the phrase
        lower case with spaces collapsed."""
        p = os.path.join(self.S, "leak-allow.txt")
        out = []
        for l in (read(p).splitlines() if os.path.exists(p) else []):
            m = LINE_ALLOW_RE.match(l.strip())
            if m:
                ph = allow_phrase(m.group(2))
                if ph:
                    out.append((self.public_rel(m.group(1)), ph))
        return out

    def public_rel(self, given):
        """A file named in leak-allow.txt as its path inside the public folder: campaigns/<name>/x, P/x
        and x all give x."""
        g = given.strip().strip(QUOTES).replace(os.sep, "/").lstrip("./")
        for pre in (f"campaigns/{self.name}/", "P/"):
            if g.startswith(pre):
                return g[len(pre):]
        return g

    def clock(self):
        """The public clock, P/state/clock.md, as key: value pairs."""
        p = os.path.join(self.P, "state", "clock.md")
        out = {}
        for line in (read(p).splitlines() if os.path.exists(p) else []):
            m = re.match(r"^\s*([a-z_]+)\s*:\s*(.*?)\s*$", line)
            if m:
                out[m.group(1)] = m.group(2)
        return out

    def before_night1(self):
        """True on Day 1 (change list 1): the clock at creation night 1, and no Night 1 work in the sealed
        folder yet (no world-draft.md, star.md, map.json or gods/), so S/sealed-terms.txt cannot exist yet."""
        ck = self.clock()
        if (ck.get("status") or "").split()[:1] != ["creation"] or ck.get("creation_night") != "1":
            return False
        return not any(os.path.exists(os.path.join(self.S, x)) for x in ("world-draft.md", "star.md", "map.json", "gods"))

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
LINE_ALLOW_RE = re.compile(r"^in\s+(\S+?):\s+(\S.*)$")   # a line-level allow (change list 71)


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
        if mapt.stamp_skipped(os.path.relpath(path, c.S)):
            continue   # what stamp skips carries no ids, so no bare name is warned on there (build 6 check, should-fix 7)
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
    (an alias by "player", change list 39, or its map name with "named_by": "player", change list 52)."""
    known_ids, out = heard_ids(c), set()
    for table in ("regions", "features"):
        for ident, e in c.knowledge.get(table, {}).items():
            t = e.get("told") or {}
            if t.get("name"):
                out |= {v.lower() for v in article_variants(t["name"])}
    for kind, el in c.elements():
        for a in mapt.player_names(el):
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
        told_names |= {a.lower() for a in mapt.player_names(el)}
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
                      r"|(?<![\w.,/-])(?:1[0-2]|[2-9])(?![\w-]|[.,]\d|/\d)", re.I)   # numerals 2 to 12 count alike; 3/4 is a fraction
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


# A number word before a fraction word is a fraction, not a count (build 6, change list 23): card text in the
# third person ("the god's reach falls to three quarters"), "two thirds", "four fifths".
FRACTION_WORDS = ["half", "halves", "third", "thirds", "quarter", "quarters", "fourth", "fourths", "fifth", "fifths",
                  "sixth", "sixths", "seventh", "sevenths", "eighth", "eighths", "ninth", "ninths", "tenth", "tenths",
                  "twelfth", "twelfths"]
FRACTION_AFTER_RE = re.compile(r"^\s+(?:" + "|".join(FRACTION_WORDS) + r")(?![\w-])", re.I)


def is_unit_count(sent, m):
    """True when the number word at match m counts units or things ("two days", "five full acres"), or is
    the top of a fraction ("three quarters", "two thirds", change list 23)."""
    if m.group(0).lower() == "twice":
        return False
    rest = sent[m.end():]
    return UNIT_AFTER_RE.match(rest) is not None or FRACTION_AFTER_RE.match(rest) is not None


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
PLAY_TRANSCRIPT_RE = re.compile(r"^player/transcript-year-\d+\.md$")   # a play day's verbatim record (96)
POWER_CARD_REL = "player/power-card.md"
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


def public_rel_of(c, path):
    return os.path.relpath(path, c.P).replace(os.sep, "/")


def verbatim_lines(c, path, text):
    """Line numbers of a public file that are a verbatim record of the table: every line of a creation
    transcript, and the "## Player:" and "## DM:" sections of a play transcript (change list 96)."""
    rel = public_rel_of(c, path)
    lines = text.splitlines()
    if TRANSCRIPT_RE.match(rel):
        return set(range(1, len(lines) + 1))
    if not PLAY_TRANSCRIPT_RE.match(rel):
        return set()
    out, part = set(), False
    for ln, line in enumerate(lines, 1):
        if line.startswith("## "):
            h = line.strip().lower()
            part = h.startswith("## player") or h.startswith("## dm")
            continue
        if part:
            out.add(ln)
    return out


FROZEN_LABEL_RE = re.compile(r"^\s*\**(?:Description|Drawback)\**\s*:")
LIMITS_LABEL_RE = re.compile(r"^\s*\**Limits settled at creation\**\s*:")
CARD_LABEL_RE = re.compile(r"^\s*\**[A-Z][\w ,'()-]*\**\s*:")


def frozen_card_lines(c, path, text):
    """Line numbers of the player's power card that hold its frozen terms (change list 13): the
    Description: and Drawback: lines, and the list under "Limits settled at creation:" up to the next
    label, heading or blank line. Empty for any other file."""
    if public_rel_of(c, path) != POWER_CARD_REL:
        return set()
    out, in_limits = set(), False
    for ln, line in enumerate(text.splitlines(), 1):
        if FROZEN_LABEL_RE.match(line):
            out.add(ln)
            in_limits = False
        elif LIMITS_LABEL_RE.match(line):
            in_limits = True
        elif in_limits and re.match(r"^\s*[-*]\s+", line):
            out.add(ln)
        elif not line.strip() or line.startswith("#") or CARD_LABEL_RE.match(line):
            in_limits = False
    return out


def people_folder(c, path):
    """The people's folder label of a knowledge file, campaigns/<name>/civs/<people>/knowledge.md."""
    return os.path.relpath(path, c.P).replace(os.sep, "/").split("/")[1]


def people_labels(c):
    """Every people's folder label, lower case: S/civs/<people>/, S/civs/godless/<people>/ and P/civs/<people>/."""
    out = set()
    for d in (os.path.join(c.S, "civs"), os.path.join(c.S, "civs", "godless"), os.path.join(c.P, "civs")):
        if os.path.isdir(d):
            out |= {x.lower() for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)) and x != "godless"}
    return out


def is_people_name(label, labels):
    """True when a sealed term is a people's name: its form without a leading article is a people's folder label."""
    return mapt.name_core(label).lower().replace(" ", "-") in labels


def record_text(c, people):
    """What a people's own record tells them (change list 55): S/civs/<people>/record.md (or the godless
    one) and the public P/civs/<people>/record.md. S/civs/<people>-sealed.md is the world's side of the
    record, told to no one, so a name found only there is not told (build 6 check, must-fix 3)."""
    paths = [os.path.join(c.S, "civs", people, "record.md"),
             os.path.join(c.S, "civs", "godless", people, "record.md"), os.path.join(c.P, "civs", people, "record.md")]
    return "\n".join(read(p) for p in paths if os.path.exists(p))


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
        if c.before_night1():
            if not rep.counts_only:   # Day 1: Night 1 writes the file (change list 1)
                print(f"note leaks: no sealed terms yet ({c.rel(os.path.join(c.S, SEALED_TERMS))} is written on Night 1); a pass on Day 1")
        else:
            rep.fail("leaks", f"{c.rel(os.path.join(c.S, SEALED_TERMS))} is missing; the Keeper writes it "
                              "(god names and bynames, hidden power names, common-secrets names, places off the map)")
    for p in mapt.knowledge_problems(c.world, c.knowledge) if c.world else []:
        rep.fail("leaks", f"{c.rel(os.path.join(c.P, 'player', 'map-knowledge.json'))}: {p}")
    if not os.path.isdir(c.P):
        rep.warn("leaks", f"no public folder {c.rel(c.P)}")
    # the campaign's timing file is sealed, S/state/timing.md (change list 74): nothing public carries night
    # or stage times, so a public one is named to be moved; the ordinal rule is no longer scanned in public
    pub_timing = os.path.join(c.P, "state", "timing.md")
    if os.path.exists(pub_timing):
        rep.warn("leaks", f"{c.rel(pub_timing)} is public; the campaign's timing file is "
                          f"{c.rel(os.path.join(c.S, 'state', 'timing.md'))}, sealed (change list 74)")
    labels = people_labels(c)
    records = {}
    line_allows = c.allow_lines()
    pp = os.path.join(c.S, "state", "phenomena.json")
    try:
        phen = json.load(open(pp)) if os.path.exists(pp) else {}
    except json.JSONDecodeError:
        phen = {}
    for label in sorted(x for x in phen if x.lower() in allow):
        rep.warn("leaks", f"{c.rel(os.path.join(c.S, 'leak-allow.txt'))}: the phenomenon \"{label}\" is allowed by its label, "
                          "which lets every count of it through, a year to come's included; a line allow, "
                          "in <file>: \"<phrase>\", passes one count on one line (change list 71)")
    for path in public_files(c):
        people = is_people_knowledge(c, path)
        text = read(path)
        verbatim = verbatim_lines(c, path, text)
        frozen = frozen_card_lines(c, path, text)
        prel = public_rel_of(c, path)
        mine = [ph for f, ph in line_allows if f == prel]
        if people:
            folk = people_folder(c, path)
            if folk not in records:
                records[folk] = record_text(c, folk)
        for ln, line in enumerate(text.splitlines(), 1):
            failed_labels = set()
            low = " ".join(line.split()).lower()
            line_ok = any(ph in low for ph in mine)   # a line-level allow (change list 71)
            for kind, label, rx, sev in terms:
                if people and told_to_people(kind, label):
                    continue
                if ln in verbatim and kind == KEPT_KIND:
                    continue  # a verbatim record of the table (decision 8; play transcripts, change list 96)
                if kind != KEPT_KIND and line_ok:
                    continue  # allowed on this line (change list 71)
                if sev == "fail" and rx.search(line):
                    if people and kind == "sealed term" and is_people_name(label, labels):
                        # another people's name, in a people's knowledge file, only if told to them in
                        # their record (change list 55)
                        if rx.search(records[folk]):
                            failed_labels.add(label.lower())   # settled here: no guess from prose either
                            continue
                        failed_labels.add(label.lower())
                        rep.fail("leaks", f"{c.rel(path)}:{ln}: people's name \"{label}\", not told to the {folk} in their record")
                        continue
                    failed_labels.add(label.lower())
                    rep.fail("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\"")
            for kind, label, rx, sev in terms:
                if people and told_to_people(kind, label):
                    continue
                if line_ok:
                    continue
                if sev == "warn" and label.lower() not in failed_labels and rx.search(line):
                    rep.warn("leaks", f"{c.rel(path)}:{ln}: {kind} \"{label}\" (a guess from prose; "
                                      "add it to sealed-terms.txt if it is sealed)")
            low_line = low
            if ln in verbatim or ln in frozen or line_ok:
                continue  # transcripts kept verbatim (12, 96), frozen card terms (13), a line-level allow (71)
            for num, trig, phrase_ in count_hits(line):
                ph = " ".join(phrase_.split()).lower()
                # exempt by its quoted phrase, or by a longer allowed phrase that holds it and stands in the line
                if ph in allow or any(ph in a and a in low_line for a in allow):
                    continue
                rep.fail("leaks", f"{c.rel(path)}:{ln}: number word \"{num}\" near \"{trig}\": \"{phrase_}\"")
    check_civs(c, rep)   # the sealed civ files, for a kept term (change list 78)


# ---------------------------------------------------------------- releases (change list 37)

SCARCITY_LINE_RE = re.compile(r"^\s*(?:[-*]\s+)?\**(?:world\s+scarcit(?:y|ies)|scarcit(?:y|ies)|local\s+shortages?)\**\s*:\**\s*(.+)$",
                              re.I | re.M)
SCARCITY_WORD_RE = re.compile(r"(?<![\w-])(?:scarce|scarcer|scarcest|scarcity|scarcities|rare|rarer|rarest|dear|dearer|"
                              r"dearest|shortage|shortages|short\s+of|in\s+short\s+supply|came\s+short|runs?\s+short|"
                              r"lack|lacks|lacking|wanting|precious|hard\s+to\s+come\s+by|hard\s+to\s+find|prized)(?![\w-])", re.I)
ORDER_WORDS = {"first", "second", "third", "chiefly", "above all", "most", "least"}


def world_scarcities(c):
    """The world draft's scarce things (S/world-draft.md): each item of a "Scarcities:", "World
    scarcities:" or "Local shortages:" line, by its last word ("salt", "good iron" gives "iron"), up to
    the line's first full stop, with "(unplaced)" and order words ("first", "second") set aside."""
    p = os.path.join(c.S, "world-draft.md")
    out = []
    for m in SCARCITY_LINE_RE.finditer(read(p) if os.path.exists(p) else ""):
        body = re.split(r"\.(?:\s|$)", m.group(1), maxsplit=1)[0]
        body = re.sub(r"\([^)]*\)", "", body)
        for item in re.split(r"\s*;\s*", body):
            head = re.split(r"\s*[,:]\s*", item.strip())[0]
            head = re.sub(r"^and\s+", "", head, flags=re.I)
            head = re.split(r"\s+(?:that|which|who|where|in|of|for|as|at|on|from|to|by|with)\s+", head, maxsplit=1)[0]
            for part in re.split(r"\s+(?:and|or)\s+", head):
                words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]*", part) if w.lower() not in ORDER_WORDS]
                if words and len(words[-1]) >= 3 and words[-1].lower() not in out:
                    out.append(words[-1].lower())
    return out


def release_files(c):
    """The Keeper-written releases (every .md under S/releases/, the god releases and landing releases
    among them) and the Day 3 brief, P/player/day3-brief.md."""
    out = text_files(os.path.join(c.S, "releases")) if os.path.isdir(os.path.join(c.S, "releases")) else []
    out = [p for p in out if p.endswith(".md")]
    brief = os.path.join(c.P, "player", "day3-brief.md")
    if os.path.exists(brief):
        out.append(brief)
    return out


def check_releases(c, rep):
    """The Keeper's releases and the Day 3 brief against the world draft (change list 37): a sentence that
    names one of the world's scarce things beside a word of scarcity states a world fact the reader may not
    have, and is warned on for the Keeper to reword or keep, by reading; a kept sealed term (a "!" line in
    sealed-terms.txt) fails in any of them."""
    goods = world_scarcities(c)
    good_res = [(g, re.compile(r"(?<![\w-])" + re.escape(g) + r"(?:s|es)?(?![\w-])", re.I)) for g in goods]
    kept = []
    for t in c.sealed_terms(kept=True) or []:
        for v in sorted(article_variants(t)):
            if len(v.strip()) >= 3:
                kept.append((v.strip(), re.compile(r"(?<![\w])" + re.escape(v.strip()) + r"(?![\w])")))
    for path in release_files(c):
        for ln, line in enumerate(read(path).splitlines(), 1):
            for label, rx in kept:
                if rx.search(line):
                    rep.fail("releases", f"{c.rel(path)}:{ln}: {KEPT_KIND} \"{label}\"")
            for sm in SENTENCE_RE.finditer(line):
                sent = sm.group(0)
                if not SCARCITY_WORD_RE.search(sent):
                    continue
                for g, rx in good_res:
                    if rx.search(sent):
                        rep.warn("releases", f"{c.rel(path)}:{ln}: names the world scarcity \"{g}\" beside a word of scarcity: "
                                             f"\"{' '.join(sent.split())[:160]}\"; a release states no world fact its reader lacks")


# ---------------------------------------------------------------- civs (change list 78)

def civ_files(c):
    """Every text file in the sealed folder of a people a civ agent plays, S/civs/<people>/ (the godless
    peoples, S/civs/godless/, and the Keeper's S/civs/<people>-sealed.md are not a civ agent's)."""
    d = os.path.join(c.S, "civs")
    out = []
    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if name == "godless" or not os.path.isdir(os.path.join(d, name)):
            continue
        out += text_files(os.path.join(d, name))
    return out


def check_civs(c, rep):
    """A kept sealed term (a "!" line of sealed-terms.txt, the sealed factors' names) in a civ agent's sealed
    files fails (change list 78): the agent cannot be told to avoid the word, so the scan finds it, at
    night-turn step 4 and at the lock. Part of --leaks, reported under leaks."""
    kept = []
    for t in c.sealed_terms(kept=True) or []:
        for v in sorted(article_variants(t)):
            if len(v.strip()) >= 3:
                kept.append((v.strip(), re.compile(r"(?<![\w])" + re.escape(v.strip()) + r"(?![\w])")))
    for path in civ_files(c):
        for ln, line in enumerate(read(path).splitlines(), 1):
            for label, rx in kept:
                if rx.search(line):
                    rep.fail("leaks", f"{c.rel(path)}:{ln}: {KEPT_KIND} \"{label}\" in a civ agent's sealed file")


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


MYSTERY_ID_RE = re.compile(r"^[ \t]*(?:#{2,4}[ \t]+|\*\*)(?:(?:EPIC|LONG|SHORT)[ \t:.]+)?([A-Z]{1,2}\d+)\b")
CAST_HEAD_RE = re.compile(r"^#{2,4}\s+(.+?)\s*$", re.M)
CAST_POINTERS_RE = re.compile(r"\bMysteries\**:\**\s*((?:[A-Z]{1,2}\d+\b[\s,;]*(?:and\s+)?)+)")


def mystery_id(body):
    """A mystery unit's id from its heading line ("## E01 The Widening Quiet", "**S06. ...**"), or None."""
    m = MYSTERY_ID_RE.match(body.split("\n", 1)[0])
    return m.group(1) if m else None


def cast_entries(text):
    """(heading, own text) for each heading in S/cast.md, up to the next heading of any level."""
    heads = list(CAST_HEAD_RE.finditer(text))
    return [(m.group(1).strip(), text[m.end():heads[i + 1].start() if i + 1 < len(heads) else len(text)])
            for i, m in enumerate(heads)]


def check_cast_pointers(c, rep, cast_path, answers_by_id):
    """Each cast being's "Mysteries:" pointers against the mysteries' Answers questions line (change
    list 71): a being with a Limit: line answers questions, so every mystery it is in is marked yes; and
    every pointer names a mystery that exists."""
    for head, own in cast_entries(read(cast_path)):
        ids = []
        for m in CAST_POINTERS_RE.finditer(own):
            ids += re.findall(r"[A-Z]{1,2}\d+", m.group(1))
        if not ids:
            continue
        limited = LIMIT_LINE_RE.search(own) is not None
        where = f"{c.rel(cast_path)}: \"{head}\""
        for mid in ids:
            if mid not in answers_by_id:
                rep.fail("mysteries", f"{where}: Mysteries: names {mid}, which is not a mystery")
            elif limited and answers_by_id[mid] != "yes":
                rep.fail("mysteries", f"{where} has a Limit: line (it answers questions) and is in {mid}, "
                                      "which is marked Answers questions: no")


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
    answers_by_id = {}   # mystery id (E01, L02, S06) -> "yes" or "no", for the cast pointers (change list 71)
    for path in files:
        for title, body in mystery_units(read(path)):
            total += 1
            where = f"{c.rel(path)}: \"{title}\""
            mid = mystery_id(body)
            ans = ANSWERS_FIELD_RE.findall(body)
            if mid and len(ans) == 1:
                answers_by_id[mid] = ans[0].lower()
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
    if cast is not None:
        check_cast_pointers(c, rep, cast_path, answers_by_id)
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
    # the DM's open rolls stay in the public log, ids dm-NNNN (change list 70)
    pub = os.path.join(c.P, "state", "rolls.jsonl")
    pub_entries = rollt.read_log(pub)
    fails, warns = rollt.public_log_problems(pub_entries, c.rel(pub))
    for f in fails:
        rep.fail("rolls", f)
    for w in warns:
        rep.warn("rolls", w)
    dm_ids = {rollt.entry_id(e, i, rollt.DM_PREFIX) for i, e in enumerate(pub_entries, 1) if e}
    for base in (c.S, c.P):
        for path in (text_files(base) if os.path.isdir(base) else []):
            if os.path.basename(path) == "rolls.jsonl":
                continue
            for ln, line in enumerate(read(path).splitlines(), 1):
                for m in DM_ROLL_RE.finditer(line):
                    rid = f"{rollt.DM_PREFIX}-{m.group(1)}"
                    if rid not in dm_ids:
                        rep.fail("rolls", f"{c.rel(path)}:{ln}: cites {rid}, which is not in the public log of the DM's rolls")


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


CHECKS = [("places", check_places), ("leaks", check_leaks), ("releases", check_releases), ("mysteries", check_mysteries),
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
    # --dashes alone runs on the public folder when the sealed folder does not exist yet (Day 1, change list 2);
    # so does --leaks on Day 1, before Night 1 (build 7, change list 1)
    c = Campaign(os.path.abspath(a.root), a.campaign, sealed_optional=set(chosen) <= {"dashes", "leaks"})
    if c.sealed_missing:
        if not os.path.isdir(c.P):
            sys.exit(f"lockcheck: no campaign at {c.P} or {c.S}")
        if "leaks" in chosen and not c.before_night1():
            sys.exit(f"lockcheck: no sealed campaign at {c.S}")
        print(f"note: no sealed campaign at {c.rel(c.S)} yet; {' and '.join('--' + n for n in chosen)} {'reads' if len(chosen) == 1 else 'read'} the public folder alone")
    rep = Report(a.counts_only)
    for name, fn in CHECKS:
        if name in chosen:
            fn(c, rep)
    return rep.summary(chosen)


if __name__ == "__main__":
    sys.exit(main())
