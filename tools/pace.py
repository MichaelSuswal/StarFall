"""StarFall pace tool. Turns the public pace table into days.

The numbers below are the same as engine/rules/time-and-pace.md and must stay
in step with it. Change one, change the other, and log it in the Change List.

Usage:
  python3 tools/pace.py travel --mode walk --terrain mountain --miles 120 \
      [--laden] [--group] [--season winter] [--weather rain] [--god]
  python3 tools/pace.py work --task palisade --length 400 --workers 40 \
      [--season winter] [--god]

  python3 tools/pace.py travel --mode walk --terrain road --miles 40 --climb 3000

Travel modes: walk, ride, oxcart, river_down, river_up, sail, swim.
Climbing (build 8, run 07 change list 25): --climb FEET is the height gained on the way, in the direction
travelled. By Naismith's rule (W. W. Naismith, 1892), one hour is added for every 2,000 feet climbed;
a descent adds nothing. A travel day is ten hours of movement (time-and-pace.md), so each 2,000 feet
climbed adds a tenth of a day, on foot, on horse or with a cart alike, and before the god's endurance,
laden, group, season and weather, which bend only the miles a day. The same road taken uphill takes
longer than downhill by exactly that. tools/map.py travel applies it where a line carries `heights_ft`.
Terrain (walk, ride, oxcart only): road, rough, forest, mountain, marsh, snow.
Work tasks: see WORK below. --length is the number of units for the task
(yards of wall, feet of well, acres, cubic yards, or 1 for a single item).
--god counts the god as one tireless worker added to --workers.
"""
import argparse
import math
import sys

# Miles per day, one healthy adult, fair day in summer.
TRAVEL = {
    "walk":   {"road": 20, "rough": 14, "forest": 10, "mountain": 8, "marsh": 6, "snow": 6},
    "ride":   {"road": 30, "rough": 20, "forest": 10, "mountain": 10, "marsh": 4, "snow": 8},
    "oxcart": {"road": 10, "rough": 6, "snow": 3},
    "river_down": 30,
    "river_up": 12,
    "sail": 50,
    "swim": 2,
}

# Multipliers on travel.
LADEN = {"walk": 0.75, "ride": 0.8, "oxcart": 1.0, "river_down": 1.0, "river_up": 1.0,
         "sail": 1.0, "swim": 1.0}
GROUP = 0.8

# Naismith's rule: hours added per foot climbed, in the direction travelled; a descent adds nothing.
CLIMB_FEET_PER_HOUR = 2000
DAY_HOURS = 10          # hours of movement in a travel day
CLIMB_MODES = {"walk", "ride", "oxcart"}


def climb_days(feet, mode="walk"):
    """Days added for `feet` climbed (Naismith: an hour per 2,000 feet; ten hours a travel day); 0 for a descent
    or a mode on water."""
    if mode not in CLIMB_MODES or not feet or feet <= 0:
        return 0.0
    return feet / CLIMB_FEET_PER_HOUR / DAY_HOURS

SEASON_TRAVEL = {"spring": 0.9, "summer": 1.0, "autumn": 0.95, "winter": 0.7}
SEASON_WORK = {"spring": 0.9, "summer": 1.0, "autumn": 0.9, "winter": 0.6}
WEATHER_TRAVEL = {"fair": 1.0, "rain": 0.8, "storm": 0.5}
WEATHER_WORK = {"fair": 1.0, "rain": 0.7, "storm": 0.0}

# How a god moves: a multiplier on the mortal rate, or a flat miles per day.
# Riding, carts and crewed boats move at the animal's or the crew's pace.
GOD_TRAVEL = {
    "walk": ("mult", 1.6),
    "ride": ("mult", 1.0),
    "oxcart": ("mult", 1.0),
    "river_down": ("mult", 1.6),   # a god rowing alone; a crewed boat is 1.0
    "river_up": ("mult", 1.6),     # same
    "sail": ("mult", 1.5),         # a god sailing alone through the night on a known coast
    "swim": ("flat", 20),
}
GOD_WORKER = 1.6  # a god working alone counts as this many workers

# Worker-days per unit.
WORK = {
    "palisade":      {"rate": 2,   "unit": "yard of wall"},
    "hall":          {"rate": 300, "unit": "hall"},
    "stone_wall":    {"rate": 6,   "unit": "yard of wall"},
    "weir":          {"rate": 6,   "unit": "yard of river width"},
    "well_soil":     {"rate": 1.5, "unit": "foot of depth"},
    "well_rock":     {"rate": 5,   "unit": "foot of depth"},
    "digging":       {"rate": 0.7, "unit": "cubic yard"},
    "clear_forest":  {"rate": 20,  "unit": "acre"},
    "planting":      {"rate": 1,   "unit": "acre"},
    "harvest":       {"rate": 3,   "unit": "acre"},
    "dugout":        {"rate": 30,  "unit": "boat"},
    "planked_boat":  {"rate": 120, "unit": "boat"},
    "bow":           {"rate": 3,   "unit": "bow"},
    "charcoal":      {"rate": 30,  "unit": "clamp"},
    "copper_smelt":  {"rate": 20,  "unit": "smelt of ten pounds of copper"},
    "bronze_cast":   {"rate": 5,   "unit": "tool or weapon"},
}


def fail(msg):
    print("pace: " + msg, file=sys.stderr)
    sys.exit(2)


def travel(a):
    base = TRAVEL.get(a.mode)
    if base is None:
        fail("unknown mode " + a.mode)
    if isinstance(base, dict):
        if a.terrain is None:
            fail("--terrain is required for " + a.mode)
        if a.terrain not in TRAVEL["walk"]:
            fail("unknown terrain " + a.terrain)
        if a.terrain not in base:
            print("No passage: an ox-cart cannot cross %s without a road. If a road has been cut, use --terrain road." % a.terrain)
            return
        rate = base[a.terrain]
    else:
        rate = base
    notes = []
    god_kind, god_val = GOD_TRAVEL[a.mode]
    if a.god and god_kind == "flat":
        rate = god_val
        notes.append("god swimming, flat %d miles a day" % god_val)
    else:
        if a.god and god_val != 1.0:
            rate *= god_val
            notes.append("god endurance x%.1f" % god_val)
        if a.laden and LADEN[a.mode] != 1.0:
            rate *= LADEN[a.mode]
            notes.append("laden x%.2f" % LADEN[a.mode])
        if a.group:
            rate *= GROUP
            notes.append("group x%.1f" % GROUP)
    rate *= SEASON_TRAVEL[a.season]
    rate *= WEATHER_TRAVEL[a.weather]
    if a.season != "summer":
        notes.append("%s x%.2f" % (a.season, SEASON_TRAVEL[a.season]))
    if a.weather != "fair":
        notes.append("%s x%.1f" % (a.weather, WEATHER_TRAVEL[a.weather]))
    days = a.miles / rate
    if a.climb:
        extra = climb_days(a.climb, a.mode)
        days += extra
        if extra:
            notes.append("climb of %g feet, %s days by Naismith's rule (an hour per 2,000 feet)" % (a.climb, fmt2(extra)))
        else:
            notes.append("no time added for the climb (a descent, or on water)")
    where = (a.mode + " on " + a.terrain) if a.terrain and isinstance(base, dict) else a.mode
    print("%s, %g miles: %.1f miles a day, %s days (%d full days)." % (
        where, a.miles, rate, fmt(days), math.ceil(days)))
    if notes:
        print("Applied: " + ", ".join(notes) + ".")


def work(a):
    task = WORK.get(a.task)
    if task is None:
        fail("unknown task " + a.task + ". Tasks: " + ", ".join(sorted(WORK)))
    workers = a.workers + (GOD_WORKER if a.god else 0)
    if workers <= 0:
        fail("need at least one worker")
    season = SEASON_WORK[a.season]
    weather = WEATHER_WORK[a.weather]
    if weather == 0:
        print("No work in a storm.")
        return
    worker_days = task["rate"] * a.length
    days = worker_days / (workers * season * weather)
    unit = task["unit"]
    if a.length != 1:
        head, sep, tail = unit.partition(" ")
        head = "feet" if head == "foot" else head + "s"
        unit = head + sep + tail
    print("%s, %g %s: %g worker-days, %s workers, %s days (%d full days)." % (
        a.task, a.length, unit, worker_days, fmt(workers), fmt(days), math.ceil(days)))
    notes = []
    if a.god:
        notes.append("god counts as %.1f workers" % GOD_WORKER)
    if a.season != "summer":
        notes.append("%s x%.1f" % (a.season, season))
    if a.weather != "fair":
        notes.append("%s x%.1f" % (a.weather, weather))
    if notes:
        print("Applied: " + ", ".join(notes) + ".")


def fmt(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


def fmt2(x):
    return ("%.2f" % x).rstrip("0").rstrip(".")


def main(argv=None):
    p = argparse.ArgumentParser(description="StarFall pace tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("travel")
    t.add_argument("--mode", required=True, choices=sorted(TRAVEL))
    t.add_argument("--terrain", choices=sorted(TRAVEL["walk"]))
    t.add_argument("--miles", type=float, required=True)
    t.add_argument("--laden", action="store_true")
    t.add_argument("--group", action="store_true")
    t.add_argument("--season", default="summer", choices=sorted(SEASON_TRAVEL))
    t.add_argument("--weather", default="fair", choices=sorted(WEATHER_TRAVEL))
    t.add_argument("--god", action="store_true")
    t.add_argument("--climb", type=float, default=0,
                   help="feet climbed on the way, in the direction travelled: an hour per 2,000 feet (Naismith's rule); "
                        "a descent (0 or less) adds nothing")

    w = sub.add_parser("work")
    w.add_argument("--task", required=True, choices=sorted(WORK))
    w.add_argument("--length", type=float, default=1, help="units of the task (default 1)")
    w.add_argument("--workers", type=float, default=0)
    w.add_argument("--season", default="summer", choices=sorted(SEASON_WORK))
    w.add_argument("--weather", default="fair", choices=sorted(WEATHER_WORK))
    w.add_argument("--god", action="store_true")

    a = p.parse_args(argv)
    if a.cmd == "travel":
        travel(a)
    else:
        work(a)


if __name__ == "__main__":
    main()
