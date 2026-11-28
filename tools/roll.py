"""StarFall roll tool. The only way any agent may decide a random outcome.

Contest mode (odds and success):
  python3 tools/roll.py --campaign NAME --who keeper --what "raid on the ford" \
      --factor numbers=+10 --factor ground=-10 --factor surprise=+20

Die mode (a face, no odds and no success):
  python3 tools/roll.py --campaign NAME --who keeper --what "god 3, form" --die d12

Weighted draw (one of several outcomes, each with a whole-number weight; build 6, change list 63):
  python3 tools/roll.py --campaign NAME --who keeper --what "Year 3 storm, which people" \
      --weight carrow=10 --weight orvanni=12 --weight ferrow=12

Manual reroll (any mode):
  python3 tools/roll.py --campaign NAME --who keeper --what "god 3, archetype seed" --die d30 \
      --reason "same seed as god 1" --replaces r-0012

Contest odds start at 50 (even), move by each factor's step, and are clamped to 5..95.
Steps: small 5, moderate 10, large 20 (other values allowed when a ruling says so).
Factors are open-ended: any named circumstance may be added or negated.

Every roll draws 1..100. A die maps that draw to a face:
  d20: ((roll - 1) mod 20) + 1             d10: ((roll - 1) mod 10) + 1
  d12: reroll above 96, else ((roll - 1) mod 12) + 1
  d30: reroll above 90, else ((roll - 1) mod 30) + 1
  d6:  reroll above 96, else ((roll - 1) mod 6) + 1
  d8:  reroll above 96, else ((roll - 1) mod 8) + 1
  d100: the draw itself (a plain roll: leans, the star's phase, d100 tables)
A weighted draw draws 1..T, where T is the sum of the weights (1..100 when they sum to 100). Each
outcome holds a band of T in the order given (carrow 1-10, orvanni 11-22, ferrow 23-34), written in the
logged line with the draw and the outcome chosen, so the bands are on record with the cast. A weight is a
whole number, 0 or more (0 holds no band), at least one above 0; each outcome is named once.
An automatic reroll is its own logged line: the out-of-range draw is logged with no face,
and the next draw is logged with reason "die reroll" and replaces the one before it.

A roll needs --campaign NAME or --log PATH; the tool refuses to guess a log.
Every line gets a roll id, r-NNNN, numbered per log file (existing lines plus one), and is
appended to the log BEFORE the result is shown. With --campaign NAME the log is
SPOILERS_do_not_open/campaigns/NAME/state/rolls.jsonl (sealed); otherwise state/rolls.jsonl
at the repo root. Paths are resolved from the repository root, whatever the working directory.
`time` is UTC ISO; `pacific` is the same moment in America/Los_Angeles.
Dice are hidden from the player; the DM reports only outcomes.

The DM's open rolls (build 7, run 06 change list 62 and 70): the DM rolls in play with
  python3 tools/roll.py --campaign NAME --public --who "<party>, rolled by the dm" --what "..." --factor ...
(the party is whose attempt it is: the god, a mortal by name or office, or the world for a world fact;
plain "dm" is also accepted, and --public refuses any other form; engine/roles/dm.md, build 8, run 07 change list 23
and the build check's finding 16), which writes the campaign's public log, campaigns/NAME/state/rolls.jsonl, never the sealed one. The
DM's open rolls stay in that public log (Michael, 2026-11-24 22:06), and their ids carry the DM's own
prefix, dm-NNNN, numbered per log file as r-NNNN is, so the two logs never share an id. --public
needs --campaign and a --who that names the DM ("<party>, rolled by the dm", or plain "dm"), and
takes no --log. The Keeper's rolls stay sealed, r-NNNN. public_log_problems() is the check that
tools/check.py and tools/lockcheck.py --rolls run on the public log.
"""
import argparse, datetime, json, os, re, secrets, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# die: (reroll when the draw is above this, or None; number of faces)
DICE = {"d6": (96, 6), "d8": (96, 8), "d10": (None, 10), "d12": (96, 12), "d20": (None, 20), "d30": (90, 30),
        "d100": (None, 100)}
ID_RE = re.compile(r"^(?:r|dm)-\d{4,}$")
DM_PREFIX = "dm"   # the DM's open rolls in the public log (change list 70)


def face_of(die, roll):
    """The face for a 1..100 draw, or None when the draw must be rerolled."""
    limit, faces = DICE[die]
    if limit is not None and roll > limit:
        return None
    return ((roll - 1) % faces) + 1


def pacific_now(now_utc):
    try:
        from zoneinfo import ZoneInfo
        return now_utc.astimezone(ZoneInfo("America/Los_Angeles")).isoformat(timespec="seconds")
    except Exception:
        out = subprocess.run(["date", "-d", now_utc.isoformat(), "+%Y-%m-%dT%H:%M:%S%:z"],
                             env={**os.environ, "TZ": "America/Los_Angeles"},
                             capture_output=True, text=True)
        return out.stdout.strip() or None


def log_path(args):
    if args.log:
        return args.log
    if getattr(args, "public", False) and args.campaign:
        return public_log_path(args.campaign)
    if args.campaign:
        return os.path.join(ROOT, "SPOILERS_do_not_open", "campaigns", args.campaign, "state", "rolls.jsonl")
    return os.path.join(ROOT, "state", "rolls.jsonl")


def public_log_path(campaign, root=None):
    """The campaign's public log of the DM's open rolls, campaigns/<name>/state/rolls.jsonl (change list 62)."""
    return os.path.join(root or ROOT, "campaigns", campaign, "state", "rolls.jsonl")


def read_log(path):
    """Lines of the log, each as a dict (unreadable lines as {})."""
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                out.append({})
    return out


def entry_id(entry, lineno, prefix="r"):
    """A logged line's id; lines written before ids existed take their line number (with the log's prefix)."""
    return entry.get("id") or f"{prefix}-{lineno:04d}"


DM_WHO_RE = re.compile(r"\bdm\b", re.I)


PUBLIC_WHO_RE = re.compile(r"^\s*(?:dm|[^,]*\S[^,]*,\s*rolled by the dm)\s*$", re.I)


def public_who_ok(who):
    """True for a --who that --public takes (engine/roles/dm.md; build 8 check, finding 16 and R6): plain "dm", or
    "<party>, rolled by the dm" with a party before the comma, case aside. is_dm() stays for reading older lines."""
    return bool(PUBLIC_WHO_RE.match(str(who or "")))


def is_dm(who):
    """True when a roll's `who` names the DM ("dm", "the Weigher (player), rolled by the dm")."""
    return bool(DM_WHO_RE.search(str(who or "")))


def public_log_problems(entries, where):
    """(failures, warnings) for the public log of the DM's open rolls (change list 70): every line readable
    and the DM's; a reroll has a reason and replaces an earlier line of this log; nothing rolled twice
    without one. A line with no id, or an older r-NNNN id from before the dm- prefix (build 7), is warned
    on, not failed: it was written before the prefix and is never edited."""
    fails, warns, ids, firsts, legacy = [], [], {}, {}, []
    for i, e in enumerate(entries, 1):
        if not e:
            fails.append(f"{where}:{i}: unreadable line")
            continue
        rid = entry_id(e, i, DM_PREFIX)
        if not is_dm(e.get("who")):
            fails.append(f"{where}:{i}: {rid} is not the DM's (who: {e.get('who')!r}); only the DM's open rolls are public, every other roll is sealed")
        if not e.get("id"):
            warns.append(f"{where}:{i}: no id (an older line; read as {rid})")
        elif not e["id"].startswith(DM_PREFIX + "-"):
            legacy.append(e["id"])
        elif e["id"] != f"{DM_PREFIX}-{i:04d}":
            warns.append(f"{where}:{i}: id {e['id']} is not its line number")
        if rid in ids:
            fails.append(f"{where}:{i}: id {rid} used twice")
        if e.get("replaces"):
            if not e.get("reason"):
                fails.append(f"{where}:{i}: reroll of {e['replaces']} has no reason")
            if e["replaces"] not in ids:
                fails.append(f"{where}:{i}: replaces {e['replaces']}, which is not an earlier roll of this log")
        else:
            firsts.setdefault(e.get("what", ""), []).append(rid)
        ids[rid] = e
    for what, rids in firsts.items():
        if len(rids) > 1:
            fails.append(f"{where}: rolled more than once without a reroll reason: {', '.join(rids)}")
    if legacy:
        span = legacy[0] if len(legacy) == 1 else f"{legacy[0]} to {legacy[-1]}"
        warns.append(f"{where}: {len(legacy)} line(s) with an older id and no dm- prefix ({span}), written before build 7; "
                     "they may repeat ids of the sealed log, so cite them as \"DM r-NNNN\"")
    return fails, warns


class Log:
    def __init__(self, path, prefix="r"):
        self.path = path
        self.prefix = prefix
        self.count = len(read_log(path))

    def next_id(self):
        return f"{self.prefix}-{self.count + 1:04d}"

    def write(self, entry):
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        with open(self.path, "a") as fh:
            fh.write(json.dumps(entry) + "\n")
        self.count += 1
        print(json.dumps(entry))
        return entry


def stamp():
    now = datetime.datetime.now(datetime.timezone.utc)
    return {"time": now.isoformat(timespec="seconds").replace("+00:00", "Z"), "pacific": pacific_now(now)}


def draw(n=100):
    return secrets.randbelow(n) + 1


def parse_weights(items):
    """[(outcome, weight)] from name=N items, in the order given; raises ValueError on a bad item."""
    out, seen = [], set()
    for it in items:
        if "=" not in it:
            raise ValueError(f"--weight {it!r}: use name=10")
        name, w = (x.strip() for x in it.split("=", 1))
        if not name:
            raise ValueError(f"--weight {it!r}: no outcome name")
        if name in seen:
            raise ValueError(f"--weight {name}: named twice")
        if not re.fullmatch(r"\d+", w):
            raise ValueError(f"--weight {it!r}: a weight is a whole number, 0 or more")
        seen.add(name)
        out.append((name, int(w)))
    if not any(w > 0 for _n, w in out):
        raise ValueError("--weight: at least one weight above 0")
    return out


def bands(weights):
    """[{outcome, weight, band: [lo, hi] or None}] over 1..T in the order given, and T."""
    out, lo = [], 1
    for name, w in weights:
        out.append({"outcome": name, "weight": w, "band": [lo, lo + w - 1] if w > 0 else None})
        lo += w
    return out, lo - 1


def chosen(band_list, roll):
    return next(b["outcome"] for b in band_list if b["band"] and b["band"][0] <= roll <= b["band"][1])


def main(argv=None):
    p = argparse.ArgumentParser(description="StarFall roll tool")
    p.add_argument("--who", required=True,
                   help="whose roll it is: keeper, a god, or for the DM's open roll \"<party>, rolled by the dm\" "
                        "(the god, a mortal by name or office, or the world), or plain dm")
    p.add_argument("--what", required=True)
    p.add_argument("--factor", action="append", default=[], help="name=+10 (contest mode)")
    p.add_argument("--base", type=int, default=None, help="contest base odds, default 50")
    p.add_argument("--die", choices=sorted(DICE, key=lambda d: int(d[1:])), help="die mode: d6, d8, d10, d12, d20, d30, or d100 for a plain roll")
    p.add_argument("--weight", action="append", default=[], help="name=10 (weighted draw: one outcome of several, by weight)")
    p.add_argument("--reason", help="why this is a reroll (needs --replaces)")
    p.add_argument("--replaces", help="the roll id this reroll replaces, r-NNNN")
    p.add_argument("--log", default=None, help="log file; default state/rolls.jsonl at the repo root, or the campaign's sealed state when --campaign is given")
    p.add_argument("--campaign", default=None)
    p.add_argument("--public", action="store_true",
                   help="the DM's open roll: the campaign's public log campaigns/NAME/state/rolls.jsonl, ids dm-NNNN (needs --campaign and --who \"<party>, rolled by the dm\", or plain dm)")
    a = p.parse_args(argv)

    if not a.campaign and not a.log:
        p.error("give --campaign NAME (the campaign's sealed log) or --log PATH; a roll never lands in an unchecked log")
    if a.public:
        if a.log or not a.campaign:
            p.error("--public needs --campaign NAME and takes no --log: it writes the campaign's public log")
        if not public_who_ok(a.who):
            p.error("--public is the DM's open roll: --who names the DM (\"<party>, rolled by the dm\", the party whose attempt it is, or plain \"dm\"); every other roll is sealed")
    if a.die and (a.factor or a.base is not None):
        p.error("--die takes no --factor or --base; a die returns a face, not a success")
    if a.weight and (a.die or a.factor or a.base is not None):
        p.error("--weight takes no --die, --factor or --base; a weighted draw returns an outcome, not a face or a success")
    weights = None
    if a.weight:
        try:
            weights = parse_weights(a.weight)
        except ValueError as e:
            p.error(str(e))
    if bool(a.reason) != bool(a.replaces):
        p.error("a manual reroll needs both --reason and --replaces")
    path = log_path(a)
    prefix = DM_PREFIX if a.public else "r"
    log = Log(path, prefix)
    if a.replaces:
        if not ID_RE.match(a.replaces):
            p.error("--replaces takes a roll id like r-0012 (or dm-0012 in the public log)")
        known = {entry_id(e, i + 1, prefix) for i, e in enumerate(read_log(path))}
        if a.replaces not in known:
            p.error(f"--replaces {a.replaces}: no such roll in {os.path.relpath(path, ROOT)}")

    head = {"who": a.who, "what": a.what}
    tail = {}
    if a.reason:
        tail = {"reason": a.reason, "replaces": a.replaces}

    if weights is not None:
        band_list, total = bands(weights)
        roll = draw(total)
        entry = {"id": log.next_id(), **stamp(), **head, "mode": "weighted", "weights": band_list, "of": total,
                 "roll": roll, "outcome": chosen(band_list, roll), **tail}
        return log.write(entry)

    if a.die:
        replaces = tail
        while True:
            roll = draw()
            face = face_of(a.die, roll)
            entry = {"id": log.next_id(), **stamp(), **head, "die": a.die, "roll": roll, "face": face, **replaces}
            if face is None:
                entry["void"] = f"draw above {DICE[a.die][0]}, rerolled"
            log.write(entry)
            if face is not None:
                return entry
            replaces = {"reason": "die reroll", "replaces": entry["id"]}

    base = 50 if a.base is None else a.base
    factors = []
    odds = base
    for f in a.factor:
        if "=" not in f:
            p.error(f"--factor {f!r}: use name=+10")
        name, step = f.split("=", 1)
        step = int(step)
        factors.append({"factor": name.strip(), "step": step})
        odds += step
    odds = max(5, min(95, odds))
    roll = draw()
    entry = {"id": log.next_id(), **stamp(), **head, "base": base, "factors": factors,
             "odds": odds, "roll": roll, "success": roll <= odds, **tail}
    return log.write(entry)


if __name__ == "__main__":
    main()
