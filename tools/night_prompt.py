"""Print the overnight scheduled task's prompt for a player's own copy of the game (StarFall 1.0).

Usage: python3 tools/night_prompt.py <owner> <repo>

The prompt is the one in engine/night/scheduled-prompt.md (everything below its `---` line), with the
repository it pulls and the folder it clones into set to the player's copy. The setup in the drop-in
file (starfall_v1_0.md) passes the printed text, unchanged, as the scheduled task's prompt.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SOURCE = os.path.join(ROOT, "engine", "night", "scheduled-prompt.md")
PART_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}")


def prompt_for(owner, repo, source=SOURCE):
    text = open(source, encoding="utf-8").read()
    body = text.split("\n---\n", 1)[1].strip() + "\n"
    folder = "/home/claude/" + repo.lower()
    body = body.replace("MichaelSuswal/StarFall", f"{owner}/{repo}")
    body = body.replace("owner MichaelSuswal repo StarFall", f"owner {owner} repo {repo}")
    body = body.replace("/home/claude/starfall", folder)
    return body


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2 or not all(PART_RE.fullmatch(p) for p in argv):
        print("usage: python3 tools/night_prompt.py <owner> <repo>", file=sys.stderr)
        return 2
    sys.stdout.write(prompt_for(*argv))
    return 0


if __name__ == "__main__":
    sys.exit(main())
