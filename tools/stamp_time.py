"""Print the Pacific clock time in the timing log's format (run 04 change list 10).

Usage: python3 tools/stamp_time.py [--time | --date]
  (no option)   2026-11-22 21:39    the date and time, as a timing table's Began and Closed cells
  --time        21:39               the time alone, as a stage line's times ("releases written 23:13")
  --date        2026-11-22          the Pacific date alone, as a line that starts with its date

The time is read from the system clock at the moment of the call, in America/Los_Angeles, never
from memory, so a logged time is never a minute ahead. Take the stamp when the step is done, and
write what it prints.
"""
import datetime
import os
import subprocess
import sys

ZONE = "America/Los_Angeles"


def pacific_now(now=None):
    """The current time (or `now`, an aware datetime) in America/Los_Angeles."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    try:
        from zoneinfo import ZoneInfo
        return now.astimezone(ZoneInfo(ZONE))
    except Exception:
        out = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S%z"], env={**os.environ, "TZ": ZONE},
                             capture_output=True, text=True).stdout.strip()
        return datetime.datetime.strptime(out, "%Y-%m-%dT%H:%M:%S%z")


def stamp(kind="both", now=None):
    t = pacific_now(now)
    if kind == "time":
        return t.strftime("%H:%M")
    if kind == "date":
        return t.strftime("%Y-%m-%d")
    return t.strftime("%Y-%m-%d %H:%M")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if any(a in ("-h", "--help") for a in argv) or len(argv) > 1 or any(a not in ("--time", "--date") for a in argv):
        sys.stdout.write(__doc__.lstrip())
        return 0 if all(a in ("-h", "--help") for a in argv) else 2
    print(stamp("time" if "--time" in argv else "date" if "--date" in argv else "both"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
