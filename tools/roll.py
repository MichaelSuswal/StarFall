"""StarFall roll tool. The only way any agent may decide a random outcome.

Usage:
  python3 tools/roll.py --who keeper --what "raid on the ford" \
      --factor numbers=+10 --factor ground=-10 --factor surprise=+20

Odds start at 50 (even), move by each factor's step, and are clamped to 5..95.
Steps: small 5, moderate 10, large 20 (other values allowed when a ruling says so).
Factors are open-ended: any named circumstance may be added or negated.
Every call is appended to state/rolls.jsonl BEFORE the result is shown.
Dice are hidden from the player; the DM reports only outcomes.
"""
import argparse, json, secrets, datetime, os

p = argparse.ArgumentParser()
p.add_argument("--who", required=True)
p.add_argument("--what", required=True)
p.add_argument("--factor", action="append", default=[], help="name=+10")
p.add_argument("--base", type=int, default=50)
a = p.parse_args()

factors = []
odds = a.base
for f in a.factor:
    name, step = f.split("=", 1)
    step = int(step)
    factors.append({"factor": name.strip(), "step": step})
    odds += step
odds = max(5, min(95, odds))
roll = secrets.randbelow(100) + 1
success = roll <= odds
entry = {"time": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
         "who": a.who, "what": a.what, "base": a.base, "factors": factors,
         "odds": odds, "roll": roll, "success": success}
os.makedirs("state", exist_ok=True)
with open("state/rolls.jsonl", "a") as fh:
    fh.write(json.dumps(entry) + "\n")
print(json.dumps(entry))
