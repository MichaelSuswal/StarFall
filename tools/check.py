"""Mechanical continuity checks for a resolved year. The checker agent runs the judgment
checks; this script runs the ones a script can run.

Usage: python3 tools/check.py <campaign-name> <year> [--root DIR]
Exit code 1 if any check fails. Prints one line per finding.

The clock (campaigns/<name>/state/clock.md) carries campaign, year,
status: creation|open|closed, creation_night: 1|2|3 while in creation, and season_opens.
A year the world waited (no player post that day) has years/NNN/waited.md and no advance:
no sealed year.md, no morning story for the next year, and the clock still on that year.
Rolls are sealed: SPOILERS_do_not_open/campaigns/<name>/state/rolls.jsonl.
"""
import argparse, json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))


def read_clock(path):
    clock = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\s*([a-z_]+)\s*:\s*(.*?)\s*$", line)
        if m:
            clock[m.group(1)] = m.group(2)
    return clock


def clock_problems(clock):
    out = []
    status = clock.get("status", "").split()[0] if clock.get("status") else ""
    if status not in ("creation", "open", "closed"):
        out.append(f"clock: status is {clock.get('status')!r}, not creation, open or closed")
    if status == "creation":
        if clock.get("creation_night") not in ("1", "2", "3"):
            out.append(f"clock: status creation needs creation_night 1, 2 or 3 (has {clock.get('creation_night')!r})")
    elif "creation_night" in clock:
        out.append("clock: creation_night is set but status is not creation")
    for key in ("campaign", "year", "season_opens"):
        if key not in clock:
            out.append(f"clock: no {key}")
    return out


def waited_conflicts(base, sealed, clock_year=None):
    """Years with waited.md that also advanced."""
    out = []
    years = set()
    for root in (base, sealed):
        d = os.path.join(root, "years")
        if os.path.isdir(d):
            years |= {int(n) for n in os.listdir(d) if n.isdigit() and os.path.exists(os.path.join(d, n, "waited.md"))}
    for y in sorted(years):
        signs = []
        if os.path.exists(os.path.join(sealed, "years", f"{y:03d}", "year.md")):
            signs.append("a sealed year.md")
        if os.path.exists(os.path.join(base, "years", f"{y + 1:03d}", "morning-story.md")):
            signs.append(f"a morning story for year {y + 1}")
        if signs:
            out.append(f"year {y}: waited.md and a year advance both exist ({', '.join(signs)})")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("campaign")
    ap.add_argument("year", type=int)
    ap.add_argument("--root", default=os.path.dirname(TOOLS))
    a = ap.parse_args(argv)
    camp, year = a.campaign, a.year
    base = os.path.join(a.root, "campaigns", camp)
    sealed = os.path.join(a.root, "SPOILERS_do_not_open", "campaigns", camp)
    findings = []

    def rel(p):
        return os.path.relpath(p, a.root)

    def need(path, what):
        if not os.path.exists(path):
            findings.append(f"missing: {what} ({rel(path)})")
            return False
        return True

    waited = os.path.exists(os.path.join(base, "years", f"{year:03d}", "waited.md"))

    # 1. Clock
    clock_path = os.path.join(base, "state", "clock.md")
    clock = {}
    if need(clock_path, "the clock"):
        clock = read_clock(clock_path)
        findings += clock_problems(clock)
        status = (clock.get("status") or "").split()[0] if clock.get("status") else ""
        if status == "creation":
            findings.append(f"clock: campaign is in creation (night {clock.get('creation_night')}); there is no resolved year to check")
        elif waited:
            if clock.get("year") != str(year):
                findings.append(f"clock: the world waited in year {year}, so the clock stays on {year} (has {clock.get('year')})")
        elif clock.get("year") != str(year + 1):
            findings.append(f"clock not advanced to year {year + 1}")

    # 2. Waited years never also advance
    findings += waited_conflicts(base, sealed)

    # 3. Required outputs for the year (a waited year has none)
    if not waited:
        need(os.path.join(sealed, "years", f"{year:03d}", "year.md"), "the year's sealed record")
        need(os.path.join(base, "releases", f"{year:03d}", "dm.md"), "the DM release")
        need(os.path.join(base, "years", f"{year + 1:03d}", "morning-story.md"), "the morning story")
        req = os.path.join(a.root, "images", "requests", f"{camp}-{year + 1:03d}-morning.json")
        if not os.path.exists(req):
            findings.append("no painting request for the morning story")

    # 4. Rolls: sealed log readable, nothing rolled twice without a reroll reason, public log empty
    sys.path.insert(0, TOOLS)
    import roll as rollt
    rolls_path = os.path.join(sealed, "state", "rolls.jsonl")
    entries = rollt.read_log(rolls_path)
    firsts = {}
    for i, e in enumerate(entries, 1):
        if not e:
            findings.append(f"{rel(rolls_path)}:{i}: unreadable line")
            continue
        if e.get("replaces"):
            if not e.get("reason"):
                findings.append(f"{rel(rolls_path)}:{i}: reroll with no reason")
            continue
        firsts.setdefault(e.get("what", ""), []).append(rollt.entry_id(e, i))
    for w, ids in firsts.items():
        if len(ids) > 1:
            findings.append(f"rolled more than once: {w} ({', '.join(ids)})")
    pub = os.path.join(base, "state", "rolls.jsonl")
    if os.path.exists(pub) and any(l.strip() for l in open(pub)):
        findings.append(f"{rel(pub)}: rolls in the public log; rolls are sealed")

    # 5. Dashes in player-facing text
    for path in [os.path.join(base, "years", f"{year + 1:03d}", "morning-story.md"),
                 os.path.join(base, "releases", f"{year:03d}", "dm.md"),
                 os.path.join(base, "years", f"{year:03d}", "waited.md")]:
        if os.path.exists(path):
            text = open(path, encoding="utf-8").read()
            if "\u2014" in text or "\u2013" in text:
                findings.append(f"dash in player-facing text: {rel(path)}")

    for f in findings:
        print(f)
    print(f"{len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
