"""Mechanical continuity checks for a resolved year. The checker agent runs the judgment
checks; this script runs the ones a script can run.

Usage: python3 tools/check.py <campaign-name> <year>
Exit code 1 if any check fails. Prints one line per finding.
"""
import json, os, re, sys

camp, year = sys.argv[1], int(sys.argv[2])
base = f"campaigns/{camp}"
sealed = f"SPOILERS_do_not_open/campaigns/{camp}"
findings = []

def need(path, what):
    if not os.path.exists(path):
        findings.append(f"missing: {what} ({path})")
        return False
    return True

# 1. Required outputs for the year
need(f"{base}/years/{year:03d}/year.md", "the year's sealed record")
need(f"{base}/releases/{year:03d}/dm.md", "the DM release")
need(f"{base}/years/{year+1:03d}/morning-story.md", "the morning story")

# 2. Rolls: every contest line in year.md that says "rolled" must match a logged roll this year
rolls_path = f"{base}/state/rolls.jsonl"
rolls = []
if os.path.exists(rolls_path):
    for line in open(rolls_path):
        try:
            rolls.append(json.loads(line))
        except json.JSONDecodeError:
            findings.append("rolls.jsonl: unreadable line")
whats = [r.get("what", "") for r in rolls]
dupes = {w for w in whats if whats.count(w) > 1}
for w in dupes:
    findings.append(f"rolled more than once: {w}")

# 3. Dashes in player-facing text
for path in [f"{base}/years/{year+1:03d}/morning-story.md", f"{base}/releases/{year:03d}/dm.md"]:
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
        if "—" in text or "–" in text:
            findings.append(f"dash in player-facing text: {path}")

# 4. Clock
clock = f"{base}/state/clock.md"
if need(clock, "the clock"):
    txt = open(clock).read()
    if f"year: {year+1}" not in txt:
        findings.append(f"clock not advanced to year {year+1}")

# 5. Painting request for the morning
req = f"images/requests/{camp}-{year+1:03d}-morning.json"
if not os.path.exists(req):
    findings.append("no painting request for the morning story")

for f in findings:
    print(f)
print(f"{len(findings)} finding(s)")
sys.exit(1 if findings else 0)
