"""Count recurring phenomena from the record, so no agent estimates or varies them.

The event schedule (sealed) lists recurring phenomena with their true occurrences per year
in SPOILERS_do_not_open/campaigns/<name>/state/phenomena.json (sealed; the true counts are spoilers):
  {"sky-lights": {"name": "sky lights", "rate": "fixed", "per_year": {"1": 4, "2": 5, ...}},
   "red-tide":   {"name": "red tide", "rate": "fixed", "per_year": {...}}}
Each key is the phenomenon's label (lower case, hyphens). `name` (build 7, run 06 change list 53) is the
phenomenon's words as prose writes them: tools/lockcheck.py --leaks reads it to find a true count written
beside those words in a public file (without it, the label's words are used). `rate` is "fixed" (the
counts are rolled at creation and never change); `per_year` maps each year, as a string, to its count.
An optional `months` maps a year to the month of each occurrence ({"1": [8, 7, 5]}, months counted from the
waking month); when the year has them they are printed after the count, for the pass-one release (run 06
change list 98), and they must number as many as the count.

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
    n = ph['per_year'].get(str(year), 0)
    months = (ph.get("months") or {}).get(str(year))
    print(f"{name}: {n}" + (f" (months {', '.join(str(m) for m in sorted(months))})" if months else ""))
    if months and len(months) != n:
        print(f"{name}: year {year} has {len(months)} month(s) for a count of {n}", file=sys.stderr)
        sys.exit(1)
