"""Mechanical continuity checks for a resolved year. The checker agent runs the judgment
checks; this script runs the ones a script can run.

Usage: python3 tools/check.py <campaign-name> <year> [--step 4|7] [--root DIR]
Exit code 1 if any check fails. Prints one line per finding, then any notes (which do not count).

--step (build 7, run 06 change list 73): the night turn runs the check at step 7, one round over
everything, with a quick script check at the end of step 4. `--step 4` checks what step 4 has made: the clock
still on year NNN, the timing file, the engage rule, the sealed year record and the rolls; the releases,
the morning story and its painting request are later steps and are not looked for. `--step 7` checks
everything the night has made by its step 7 check, the clock still on year NNN (step 8 advances it). With no
--step, the full check after step 8: the clock advanced to NNN+1.
The morning painting request (build check B7): images/requests/<name>-NNN+1-morning.json, or, when the
campaign's state/images.md does not approve it, the same file held in images/held/, which is a note, not a
finding. A held request images.md does approve is a finding (it belongs in images/requests/), and a morning with neither is a finding.

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
Painting approval (build 8, run 07 change list 14): a play-year morning is approved only by the images.md line
that names its own year ("Year 2 morning painting: approved" approves the Year 2 morning and no other), or
by the standing line that names every played year ("year morning painting: approved, one per played year").
The held-request check reads approval through tools/paint.py covered(), so both tools read it the same way.
The clock waits (build 8, Michael 2026-11-27; engine/night/night-turn.md step 0): the clock may carry
`play_day: K` (2 or more) while a year stays open at a held moment. The check reads the night's play day K
from --play-day, else from the clock (at steps 4 and 7 its play_day, or 1; after step 8 a clock that waited
reads K+1). Play day K's files carry its number: player/decisions-NNN-K.md, releases/NNN/dm-K.md,
S/releases/NNN/dm-sealed-K.md, years/NNN/closing-K.md. The night's morning is years/NNN+1/morning-story.md
when the clock advances (no play_day line after it) or years/NNN/morning-story-<K+1>.md when it waits (the
clock left on NNN with play_day: K+1), with its painting request <name>-NNN-morning-<K+1>.json, approved only
by an images.md line naming that year and that play day. The timing line "clock waited: year NNN open, play
day K+1" is the night's own and is not a waited day; no date may hold two of a waited day, a clock advance
and a clock that waited. A morning request in images/requests/ that images.md does not approve is a finding.
The transcript (build 8, run 07 change list 24): player/transcript-year-NNN.md is append-only. The check
reads its committed versions (git log) and fails it when its `## ` section count falls between two commits,
or when the working file is shorter than its last committed version. A fall that a later commit restored
(every section any committed version held stands in the file now, verbatim) is a note, not a finding.
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
    if "play_day" in clock:   # build 8, the clock waits: 2 or more, only while a year stays open
        pd = clock["play_day"]
        if not (pd.isdigit() and int(pd) >= 2):
            out.append(f"clock: play_day is {pd!r}; it is 2 or more, set only when the clock waited (a clock without it is play day 1)")
        if status != "open":
            out.append("clock: play_day is set but status is not open")
    return out


DATE_RE = re.compile(r"^\s*(?:[-*]\s+)?(\d{4}-\d{2}-\d{2})\b")
ADVANCE_RE = re.compile(r"clock advanced", re.I)
CLOCK_WAITED_RE = re.compile(r"clock waited\b", re.I)


def timing_conflicts(timing_path):
    """Pacific dates in timing.md with both a waited line and an advance line."""
    if not os.path.exists(timing_path):
        return []
    waited, advanced, clock_waited = set(), set(), set()
    for line in open(timing_path, encoding="utf-8"):
        m = DATE_RE.match(line)
        if not m:
            continue
        if CLOCK_WAITED_RE.search(line):   # "clock waited: year NNN open, play day K+1" (build 8): the night ran
            clock_waited.add(m.group(1))
        elif re.search(r"\bwaited\b", line, re.I):
            waited.add(m.group(1))
        if ADVANCE_RE.search(line):
            advanced.add(m.group(1))
    return ([f"timing: {d} has both a waited line and a clock advance" for d in sorted(waited & advanced)] +
            [f"timing: {d} has both a waited line and a clock-waited line" for d in sorted(waited & clock_waited)] +
            [f"timing: {d} has both a clock-waited line and a clock advance" for d in sorted(clock_waited & advanced)])


def timing_path(base, sealed):
    """The campaign's timing file: the sealed S/state/timing.md (change list 74), else, for an older
    campaign, the public P/state/timing.md."""
    s = os.path.join(sealed, "state", "timing.md")
    return s if os.path.exists(s) else os.path.join(base, "state", "timing.md")


def held_request_approved(root, path):
    """(approved, reason) for a held request, by its campaign's state/images.md, as tools/paint.py reads it."""
    sys.path.insert(0, TOOLS)
    import paint
    try:
        req = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, "the held request is not readable JSON"
    return paint.covered(req, root)


SECTION_RE = re.compile(r"(?m)^(?=## )")


def sections(text):
    """The `## ` sections of a transcript, each from its heading to the next, trailing space set aside."""
    return [p.rstrip() for p in SECTION_RE.split(text) if p.startswith("## ")]


def committed_versions(root, rel_path):
    """[(short commit, text)] for every commit that touched rel_path, oldest first; [] outside a git repository."""
    import subprocess
    try:
        r = subprocess.run(["git", "-C", root, "log", "--reverse", "--format=%h", "--", rel_path],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return []
    if r.returncode != 0:
        return []
    out = []
    for c in r.stdout.split():
        shown = subprocess.run(["git", "-C", root, "show", f"{c}:{rel_path}"], capture_output=True, text=True, timeout=60)
        if shown.returncode == 0:   # a commit that deleted the file shows nothing
            out.append((c, shown.stdout))
    return out


def transcript_problems(root, path):
    """(findings, notes) for an append-only transcript (change list 24): its `## ` count may never fall
    between commits, and the working file may never be shorter than its last committed version. A fall a
    later commit restored, with every committed section standing in the file now, is a note."""
    rel_path = os.path.relpath(path, root)
    if not os.path.exists(path):
        return [], []
    current = open(path, encoding="utf-8").read()
    now = set(sections(current))
    versions = committed_versions(root, rel_path)
    findings, notes = [], []
    lost = [x for _c, t in versions for x in sections(t) if x not in now]
    for (c0, t0), (c1, t1) in zip(versions, versions[1:]):
        n0, n1 = len(sections(t0)), len(sections(t1))
        if n1 < n0:
            line = f"transcript: {rel_path} fell from {n0} to {n1} `## ` sections between commits {c0} and {c1}"
            if lost:
                findings.append(line + "; it is append-only")
            else:
                notes.append(line + "; every committed section stands in the file now, so it was restored")
    if versions:
        c, last = versions[-1]
        if len(current) < len(last):
            findings.append(f"transcript: {rel_path} is shorter than its last committed version ({c}: "
                            f"{len(last)} characters, now {len(current)}); it is append-only")
    if lost and not any(f.startswith(f"transcript: {rel_path} fell") for f in findings):
        findings.append(f"transcript: {rel_path} has lost {len(lost)} committed section(s); it is append-only")
    return findings, notes


def waited_notes(base, year):
    d = os.path.join(base, "years", f"{year:03d}")
    return sorted(f for f in os.listdir(d) if re.fullmatch(r"waited-\d{4}-\d{2}-\d{2}\.md", f)) if os.path.isdir(d) else []


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("campaign")
    ap.add_argument("year", type=int)
    ap.add_argument("--root", default=os.path.dirname(TOOLS))
    ap.add_argument("--play-day", dest="play_day", type=int, default=None,
                    help="the play day K the night resolved (default: from the clock's play_day line, or 1)")
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

    # The play day (build 8, the clock waits; engine/night/night-turn.md step 0): K, from --play-day, else from the
    # clock (its play_day line, or 1); after step 8 a clock that waited reads K+1, one that advanced reads none.
    nnn = f"{year:03d}"
    clock_path = os.path.join(base, "state", "clock.md")
    clock = read_clock(clock_path) if os.path.exists(clock_path) else {}
    clock_day = int(clock["play_day"]) if str(clock.get("play_day", "")).isdigit() else None
    if a.play_day:
        K = a.play_day
    elif step < 8:
        K = clock_day or 1
    elif clock.get("year") == str(year) and clock_day:
        K = clock_day - 1
    else:   # advanced: the highest play day the year has a decisions file for
        days = [int(m.group(1)) for f in (os.listdir(os.path.join(base, "player")) if os.path.isdir(os.path.join(base, "player")) else [])
                for m in [re.fullmatch(rf"decisions-{nnn}-(\d+)\.md", f)] if m]
        K = max(days) if days else 1
    sfx = "" if K == 1 else f"-{K}"
    decisions = os.path.join(base, "player", f"decisions-{nnn}{sfx}.md")
    release = os.path.join(base, "releases", nnn, f"dm{sfx}.md")

    # a day counts as waited when it has waited notes and nothing resolved for it yet: on play day 1 no sealed
    # record, on a later play day no decisions file and no release for that day
    notes = waited_notes(base, year)
    if K == 1:
        waited = bool(notes) and not os.path.exists(os.path.join(sealed, "years", nnn, "year.md"))
    else:
        waited = bool(notes) and not os.path.exists(decisions) and not os.path.exists(release)
    # which morning the night wrote: the next year's (the clock will advance) or this year's next play day (it waits)
    advance_morning = os.path.join(base, "years", f"{year + 1:03d}", "morning-story.md")
    wait_morning = os.path.join(base, "years", nnn, f"morning-story-{K + 1}.md")
    waits = os.path.exists(wait_morning) and not os.path.exists(advance_morning)

    # 1. Clock
    if need(clock_path, "the clock"):
        findings += clock_problems(clock)
        status = (clock.get("status") or "").split()[0] if clock.get("status") else ""
        if status == "creation":
            print(f"check.py does not apply during creation (night {clock.get('creation_night')}); "
                  "run tools/lockcheck.py for the lock")
            return 0
        day_txt = f", play day {clock_day}" if clock_day else ""
        if waited:
            if clock.get("year") != str(year) or (clock_day or 1) != K:
                findings.append(f"clock: the world waited in year {year}, play day {K}, so the clock stays there "
                                f"(has year {clock.get('year')}{day_txt})")
        elif step < 8:
            if clock.get("year") != str(year) or (clock_day or 1) != K:
                findings.append(f"clock: at step {step} the clock is still on year {year}, play day {K}; step 8 moves it "
                                f"(has year {clock.get('year')}{day_txt})")
        elif waits:
            if clock.get("year") != str(year) or clock_day != K + 1:
                findings.append(f"clock: the night stopped at a held moment (years/{nnn}/morning-story-{K + 1}.md), so the clock "
                                f"waits on year {year} with play_day: {K + 1} (has year {clock.get('year')}{day_txt})")
        elif clock.get("year") != str(year + 1):
            findings.append(f"clock not advanced to year {year + 1}")
        elif clock_day:
            findings.append(f"clock: advanced to year {year + 1}, so it carries no play_day line (has {clock_day})")

    # 2. A day the world waited never also moves the clock
    findings += timing_conflicts(timing_path(base, sealed))

    # 3. Required outputs for the play day (a waited day has none)
    if not notes and not os.path.exists(decisions):
        findings.append(f"engage: year {year} turned with no player/{os.path.basename(decisions)} and no waited note"
                        + (f" (play day {K})" if K > 1 else ""))
    elif not waited and not os.path.exists(decisions):
        findings.append(f"engage: year {year} play day {K} has a waited note and a release, but no {rel(decisions)}")
    if not waited:
        need(os.path.join(sealed, "years", nnn, "year.md"), "the year's sealed record")
        if step >= 7:   # the releases are step 5, the morning story and its painting request step 6, the check step 7 (change list 73)
            need(release, "the DM release")
            if waits:
                rid = f"{camp}-{nnn}-morning-{K + 1}"
            else:
                need(advance_morning, f"the morning story (or years/{nnn}/morning-story-{K + 1}.md on a waiting night)")
                rid = f"{camp}-{year + 1:03d}-morning"
            req = os.path.join(a.root, "images", "requests", f"{rid}.json")
            held = os.path.join(a.root, "images", "held", f"{rid}.json")
            if not os.path.exists(req):
                # a morning whose painting images.md does not approve waits in images/held/ (build check B7)
                if os.path.exists(held):
                    ok, why = held_request_approved(a.root, held)
                    if ok:
                        findings.append(f"the morning painting request is held in {rel(held)}, but "
                                        f"campaigns/{camp}/state/images.md approves it ({why}); it belongs in images/requests/")
                    else:
                        notes_out.append(f"the morning painting request waits in {rel(held)}: {why}")
                else:
                    findings.append(f"no painting request for the morning story (none in images/requests/ or images/held/) for {rid}")
            else:
                ok, why = held_request_approved(a.root, req)
                if not ok:
                    findings.append(f"the morning painting request {rel(req)} is in images/requests/, but "
                                    f"campaigns/{camp}/state/images.md does not approve it ({why}); it belongs in images/held/")

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

    # 5. The year's transcript is append-only (change list 24)
    tf, tn = transcript_problems(a.root, os.path.join(base, "player", f"transcript-year-{year:03d}.md"))
    findings += tf
    notes_out += tn

    # 6. Dashes in player-facing text
    for path in [advance_morning, wait_morning, release, os.path.join(base, "years", nnn, f"closing{sfx}.md"),
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
