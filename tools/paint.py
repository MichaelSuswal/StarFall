"""Turn image requests into paintings.

Two request folders, each with its own output folder:
  images/requests/*.json                        -> images/out/                        (scene paintings, public)
  SPOILERS_do_not_open/images/requests/*.json   -> SPOILERS_do_not_open/images/out/   (map paintings, sealed)
A map prompt describes the whole world's ground, so map requests go in the sealed folder.

A request file looks like:
{"id": "y001-morning", "prompt": "...", "shape": "square" | "wide" | "tall"}
Requests that already have an output are skipped. Paths are resolved from the repository root.
"""
import base64, glob, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDERS = [("images/requests", "images/out"),
           ("SPOILERS_do_not_open/images/requests", "SPOILERS_do_not_open/images/out")]
MODEL = os.environ.get("OPENAI_IMAGE_MODEL") or "chatgpt-image-latest"
SIZES = {"square": "1024x1024", "wide": "1536x1024", "tall": "1024x1536"}


def pending(root=ROOT):
    """(request path, request, output path) for every request without an output."""
    out = []
    for req_dir, out_dir in FOLDERS:
        for path in sorted(glob.glob(os.path.join(root, req_dir, "*.json"))):
            req = json.load(open(path))
            target = os.path.join(root, out_dir, f"{req['id']}.png")
            if not os.path.exists(target):
                out.append((path, req, target))
    return out


def main():
    todo = pending()
    if not todo:
        print("0 new painting(s)")
        return
    key = os.environ["OPENAI_API_KEY"]
    made = 0
    for path, req, target in todo:
        body = json.dumps({
            "model": MODEL,
            "prompt": req["prompt"],
            "size": SIZES.get(req.get("shape", "square"), "1024x1024"),
            "n": 1,
        }).encode()
        r = urllib.request.Request(
            "https://api.openai.com/v1/images/generations", data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            resp = json.load(urllib.request.urlopen(r, timeout=300))
        except urllib.error.HTTPError as e:
            print(f"{req['id']}: HTTP {e.code} {e.read().decode()[:500]}", file=sys.stderr)
            sys.exit(1)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, "wb").write(base64.b64decode(resp["data"][0]["b64_json"]))
        print(f"painted {os.path.relpath(target, ROOT)}")
        made += 1
    print(f"{made} new painting(s)")


if __name__ == "__main__":
    main()
