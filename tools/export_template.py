"""Copy the playable game from this workshop into a clone of the public template repo (StarFall 1.0).

Usage: python3 tools/export_template.py <target folder>

The target is a clone of github.com/MichaelSuswal/StarFall-Game. Everything in it except `.git/` is
replaced by the game as committed here (tracked files only), less the workshop: no campaigns, no
test runs, no paintings, no build-check notes. `template/README.md` becomes the template's README,
and `template/CLAUDE-preface.md` is put above this repo's CLAUDE.md. Review the result, then commit
and push it from the target.
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

INCLUDE = [
    ".github/workflows/",
    ".gitignore",
    "engine/",
    "tools/",
    "tests/tools/",
    "SPOILERS_do_not_open/README.md",
    "SPOILERS_do_not_open/keeper/",
    "starfall_v1_0.md",
]
EXCLUDE = [
    "tools/check-key.result",
    "tools/export_template.py",
    "SPOILERS_do_not_open/keeper/build7-check-sealed.md",
    "SPOILERS_do_not_open/keeper/build8-check-sealed.md",
    "tests/tools/lockcheck-sim-01.txt",
]
EMPTY_DIRS = [
    "campaigns",
    "images/requests", "images/held", "images/out",
    "SPOILERS_do_not_open/campaigns",
    "SPOILERS_do_not_open/images/requests", "SPOILERS_do_not_open/images/held",
    "SPOILERS_do_not_open/images/out",
]


def tracked(root=ROOT):
    out = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True, check=True).stdout
    return [p for p in out.splitlines() if p]


def selected(paths):
    keep = []
    for p in paths:
        if p in EXCLUDE or "__pycache__" in p:
            continue
        if any(p == inc or (inc.endswith("/") and p.startswith(inc)) for inc in INCLUDE):
            keep.append(p)
    return keep


def export(target, root=ROOT):
    if not os.path.isdir(os.path.join(target, ".git")):
        raise SystemExit(f"refused: {target} is not a git clone")
    for name in os.listdir(target):
        if name == ".git":
            continue
        path = os.path.join(target, name)
        shutil.rmtree(path) if os.path.isdir(path) and not os.path.islink(path) else os.remove(path)
    files = selected(tracked(root))
    for p in files:
        dst = os.path.join(target, p)
        os.makedirs(os.path.dirname(dst) or target, exist_ok=True)
        shutil.copy2(os.path.join(root, p), dst)
    for d in EMPTY_DIRS:
        os.makedirs(os.path.join(target, d), exist_ok=True)
        open(os.path.join(target, d, ".keep"), "w").close()
    shutil.copy2(os.path.join(root, "template", "README.md"), os.path.join(target, "README.md"))
    preface = open(os.path.join(root, "template", "CLAUDE-preface.md"), encoding="utf-8").read()
    claude = open(os.path.join(root, "CLAUDE.md"), encoding="utf-8").read()
    with open(os.path.join(target, "CLAUDE.md"), "w", encoding="utf-8") as f:
        f.write(preface.rstrip("\n") + "\n\n" + claude)
    return files


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    files = export(argv[0])
    print(f"exported {len(files)} files, the README, CLAUDE.md with its preface, and {len(EMPTY_DIRS)} empty folders")
    return 0


if __name__ == "__main__":
    sys.exit(main())
