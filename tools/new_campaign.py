"""Start a new campaign: the files a campaign needs before the DM posts Day 1 (StarFall 1.0).

Usage: python3 tools/new_campaign.py <name> [--paintings full|maps] [--date YYYY-MM-DD]

  <name>          lowercase letters, digits and hyphens, starting with a letter ("ashfall", "seah-1")
  --paintings     full (default): the two map sheets, the underground sheet if the world has one,
                  the first morning, one morning painting per played year and up to two paintings
                  the player asks for a day.
                  maps: the map sheets only, which creation cannot run without. Nothing else is painted.
                  Either way, a further morning while the clock waits is not approved (held).
  --date          the Pacific date written into images.md (default: today, from stamp_time.py)

It writes, and refuses to overwrite:
  campaigns/<name>/state/clock.md    status: creation, creation_night: 1 (engine/night/creation-nights.md)
  campaigns/<name>/state/models.md   the model for each role
  campaigns/<name>/state/images.md   the paintings the player approved at setup

The sealed folder is created by the Keeper on Night 1, and every other file by the day or night that
owns it. The script writes no game content and makes no image request.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

NAME_RE = re.compile(r"[a-z][a-z0-9-]{0,39}")

MODELS = """# Models ({name})

The model for each role in the night turn and the live day. The owner of this copy may change them.

keeper: fable
npc-god: sonnet
civ: sonnet
checker: opus
dm: fable
"""

IMAGES_HEAD = """# Images approved ({name})

Set at setup on {date} by the player, the owner of this copy. Every painting is made on the OpenAI key
saved as this repository's `OPENAI_API_KEY` secret, and each one costs money on that account.
A request this file does not approve is held in `images/held/` and never painted.

Creation:
- surface sheet: approved
- cloud sheet: approved
"""

CREATION_FULL = """- underground sheet: approved, if the world has an underground with regions of its own
- first morning painting: approved
"""

CREATION_MAPS = """- underground sheet: not approved; the underground stays as data in the map
- first morning painting: not approved
"""

PLAY_FULL = """
Play:
- year morning painting: approved, one per played year
- player-asked painting: approved, up to two a day
- further morning while the clock waits: not approved; hold
- any repaint: not approved; hold
"""

PLAY_MAPS = """
Play:
- year morning painting: not approved
- player-asked painting: not approved
- further morning while the clock waits: not approved; hold
- any repaint: not approved; hold
"""


def files_for(name, paintings, date):
    images = IMAGES_HEAD.format(name=name, date=date)
    images += CREATION_FULL if paintings == "full" else CREATION_MAPS
    images += PLAY_FULL if paintings == "full" else PLAY_MAPS
    return {
        "clock.md": f"campaign: {name}\nstatus: creation\ncreation_night: 1\n",
        "models.md": MODELS.format(name=name),
        "images.md": images,
    }


def main(argv=None, root=ROOT):
    ap = argparse.ArgumentParser(description="Start a new StarFall campaign.")
    ap.add_argument("name")
    ap.add_argument("--paintings", choices=["full", "maps"], default="full")
    ap.add_argument("--date")
    a = ap.parse_args(argv)
    if not NAME_RE.fullmatch(a.name):
        print(f"refused: '{a.name}' is not a campaign name (lowercase letters, digits and hyphens, "
              "starting with a letter, at most 40)", file=sys.stderr)
        return 2
    camp = os.path.join(root, "campaigns", a.name)
    if os.path.exists(camp) or os.path.exists(os.path.join(root, "SPOILERS_do_not_open", "campaigns", a.name)):
        print(f"refused: campaign '{a.name}' already exists", file=sys.stderr)
        return 2
    if a.date:
        date = a.date
    else:
        import stamp_time
        date = stamp_time.stamp("date")
    state = os.path.join(camp, "state")
    os.makedirs(state)
    for fname, text in files_for(a.name, a.paintings, date).items():
        with open(os.path.join(state, fname), "w", encoding="utf-8") as f:
            f.write(text)
    print(f"campaign {a.name} created: campaigns/{a.name}/state/clock.md, models.md, images.md "
          f"(paintings: {a.paintings})")
    print("next: the DM posts Day 1 (engine/creation/day1-world-survey.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
