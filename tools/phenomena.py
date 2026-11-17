"""Count recurring phenomena from the record, so no agent estimates or varies them.

The event schedule (sealed) lists recurring phenomena with their true occurrences per year
in SPOILERS_do_not_open/campaigns/<name>/state/phenomena.json (sealed; the true counts are spoilers):
  {"sky-lights": {"rate": "fixed", "per_year": {"1": 4, "2": 5, ...}},
   "red-tide":   {"rate": "fixed", "per_year": {...}}}

Usage: python3 tools/phenomena.py SPOILERS_do_not_open/campaigns/<name> YEAR [name]
Prints the true count for the year. The Keeper includes it only when the god or its people
would notice; when included, this is the number, never a partial one.
"""
import json, sys

camp, year = sys.argv[1], sys.argv[2]
names = sys.argv[3:]
data = json.load(open(f"{camp}/state/phenomena.json"))
for name, ph in data.items():
    if names and name not in names:
        continue
    print(f"{name}: {ph['per_year'].get(str(year), 0)}")
