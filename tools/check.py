"""Mechanical continuity checks for a resolved year. The checker agent runs the judgment
checks; this script runs the ones a script can run.

Usage: python3 tools/check.py <campaign-name> <year> [--step 4|7] [--root DIR]
Exit code 1 if any check fails. Prints one line per finding, then any notes (which do not count).

--step (build 7, run 06 change list 73): the night turn runs the check after step 7, one round over
everything, with a quick script check after step 4. `--step 4` checks what step 4 has made: the clock
still on year NNN, the timing file, the engage rule, the sealed year record and the rolls; the releases,
the morning story and its painting request are later steps and are not looked for. `--step 7` checks
everything step 7 has made, the clock still on year NNN (step 8 advances it). With no --step, the full
check after step 8: the clock advanced to NNN+1.

The clock (campaigns/<name>/state/clock.md) carries campaign, year,
status: creation|open|closed, creation_night: 1|2|3a|3b while in creation, and season_opens.
During creation there is no resolved year: the script says so and exits 0.
A year turns only on a day the player posted: a resolved year needs player/decisions-NNN.md
or a waited note. A day the world waited leaves years/NNN/waited-YYYY-MM-DD.md (Pacific date)
and no advance. The timing file is sealed, SPOILERS_do_not_open/campaigns/<name>/state/timing.md (build 6,
change list 74); an older campaign's public campaigns/<name>/state/timing.md is read when the sealed one
does not exist. In the timing file only lines that start with a Pacific date count (a list
marker before the date is allowed); no date may have both a line containing "waited" and a
line containing "clock advanced".
Rolls: the Keeper's are sealed, SPOILERS_do_not_open/campaigns/<name>/state/rolls.jsonl, ids r-NNNN. The
DM's open rolls stay in the public log, campaigns/<name>/state/rolls.jsonl, ids dm-NNNN (Michael,
2026-11-24 22:06; run 06 change list 70): each line the DM's, rerolls with a reason, nothing rolled twice
(tools/roll.py public_log_problems). An older public line with an r-NNNN id is a note, not a finding.
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
        if clock.get("creation_night") not in ("1", "2", "3a", "3b"):
            out.append(f"clock: status creation needs creation_night 1, 2, 3a or 3b (has {clock.get('creation_night')!r})")
    elif "creation_night" in clock:
        out.append("clock: creation_night is set but status is not creation")
    for key in ("campaign", "year", "season_opens"):
        if key not in clock:
            out.append(f"clock: no {key}")
    return out


DATE_RE = re.compile(r"^\s*(?:[-*]\s+)?(\d{4}-\d{2}-\d{2})\b")
ADVANCE_RE = re.compile(r"clock advanced", re.I)


def timing_conflicts(timing_path):
    """Pacific dates in timing.md with both a waited line and an advance line."""
    if not os.path.exists(timing_path):
        return []
    waited, advanced = set(), set()
    for line in open(timing_path, encoding="utf-8"):
        m = DATE_RE.match(line)
        if not m:
            continue
        if re.search(r"\bwaited\b", line, re.I):
            waited.add(m.group(1))
        if ADVANCE_RE.search(line):
            advanced.add(m.group(1))
    return [f"timing: {d} has both a waited line and a clock advance" for d in sorted(waited & advanced)]


def timing_path(base, sealed):
    """The campaign's timing file: the sealed S/state/timing.md (change list 74), else, for an older
    campaign, the public P/state/timing.md."""
    s = os.path.join(sealed, "state", "timing.md")
    return s if os.path.exists(s) else os.path.join(base, "state", "timing.md")


def waited_notes(base, year):
    d = os.path.join(base, "years", f"{year:03d}")
    return sorted(f for f in os.listdir(d) if re.fullmatch(r"waited-\d{4}-\d{2}-\d{2}\.md", f)) if os.path.isdir(d) else []


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("campaign")
    ap.add_argument("year", type=int)
    ap.add_argument("--root", default=os.path.dirname(TOOLS))
    ap.add_argument("--step", type=int, choices=(4, 7), default=None,
                    help="the quick check after step 4, or the check after step 7 (before the clock advances); default: after step 8")
    a = ap.parse_args(argv)
    camp, year = a.campaign, a.year
    step = a.step or 8
    notes_out = []
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

    # a year counts as waited when it has waited notes and no sealed record yet
    notes = waited_notes(base, year)
    waited = bool(notes) and not os.path.exists(os.path.join(sealed, "years", f"{year:03d}", "year.md"))

    # 1. Clock
    clock_path = os.path.join(base, "state", "clock.md")
    clock = {}
    if need(clock_path, "the clock"):
        clock = read_clock(clock_path)
        findings += clock_problems(clock)
        status = (clock.get("status") or "").split()[0] if clock.get("status") else ""
        if status == "creation":
            print(f"check.py does not apply during creation (night {clock.get('creation_night')}); "
                  "run tools/lockcheck.py for the lock")
            return 0
        if waited:
            if clock.get("year") != str(year):
                findings.append(f"clock: the world waited in year {year}, so the clock stays on {year} (has {clock.get('year')})")
        elif step < 8:
            if clock.get("year") != str(year):
                findings.append(f"clock: at step {step} the clock is still on year {year}; step 8 advances it (has {clock.get('year')})")
        elif clock.get("year") != str(year + 1):
            findings.append(f"clock not advanced to year {year + 1}")

    # 2. A day the world waited never also advances the clock
    findings += timing_conflicts(timing_path(base, sealed))

    # 3. Required outputs for the year (a waited year has none)
    if not notes and not os.path.exists(os.path.join(base, "player", f"decisions-{year:03d}.md")):
        findings.append(f"engage: year {year} turned with no player/decisions-{year:03d}.md and no waited note")
    if not waited:
        need(os.path.join(sealed, "years", f"{year:03d}", "year.md"), "the year's sealed record")
        if step >= 7:   # the releases are step 6, the morning story and its painting request step 7 (change list 73)
            need(os.path.join(base, "releases", f"{year:03d}", "dm.md"), "the DM release")
            need(os.path.join(base, "years", f"{year + 1:03d}", "morning-story.md"), "the morning story")
            req = os.path.join(a.root, "images", "requests", f"{camp}-{year + 1:03d}-morning.json")
            if not os.path.exists(req):
                findings.append("no painting request for the morning story")

    # 4. Rolls: sealed log readable, nothing rolled twice without a reroll reason; the public log holds the
    # DM's open rolls only (change list 70)
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
    pub_fails, pub_warns = rollt.public_log_problems(rollt.read_log(pub), rel(pub))
    findings += pub_fails
    notes_out += pub_warns

    # 5. Dashes in player-facing text
    for path in [os.path.join(base, "years", f"{year + 1:03d}", "morning-story.md"),
                 os.path.join(base, "releases", f"{year:03d}", "dm.md"),
                 *[os.path.join(base, "years", f"{year:03d}", n) for n in notes]]:
        if os.path.exists(path):
            text = open(path, encoding="utf-8").read()
            if "\u2014" in text or "\u2013" in text:
                findings.append(f"dash in player-facing text: {rel(path)}")

    for f in findings:
        print(f)
    for n in notes_out:
        print(f"note: {n}")
    print(f"{len(findings)} finding(s)" + (f", {len(notes_out)} note(s)" if notes_out else ""))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
