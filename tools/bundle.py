"""Bundle a campaign for carrying into a new chat.

Usage: python3 tools/bundle.py <campaign-name> [--with-spoilers]
Writes bundles/<campaign>-<date>.zip containing CLAUDE.md, README.md, engine/, tools/,
campaigns/<name>/ and images/out for that campaign. Spoilers are left out unless asked,
since the bundle is for the player's chat.
"""
import os, sys, zipfile, datetime

name = sys.argv[1]
spoilers = "--with-spoilers" in sys.argv
stamp = datetime.date.today().isoformat()
os.makedirs("bundles", exist_ok=True)
out = f"bundles/{name}-{stamp}.zip"
roots = ["CLAUDE.md", "README.md", "engine", "tools", f"campaigns/{name}"]
if spoilers:
    roots += ["SPOILERS_do_not_open/keeper", f"SPOILERS_do_not_open/campaigns/{name}"]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root in roots:
        if os.path.isfile(root):
            z.write(root); continue
        for d, _, files in os.walk(root):
            for f in files:
                z.write(os.path.join(d, f))
    for d, _, files in os.walk("images/out"):
        for f in files:
            if f.startswith(name):
                z.write(os.path.join(d, f))
print(out)
