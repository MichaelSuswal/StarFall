"""Turn image requests in images/requests/*.json into paintings in images/out/.

A request file looks like:
{"id": "y001-morning", "prompt": "...", "shape": "square" | "wide" | "tall"}
Requests that already have an output are skipped.
"""
import base64, glob, json, os, sys, urllib.request

MODEL = os.environ.get("OPENAI_IMAGE_MODEL") or "chatgpt-image-latest"
SIZES = {"square": "1024x1024", "wide": "1536x1024", "tall": "1024x1536"}
KEY = os.environ["OPENAI_API_KEY"]

made = 0
for path in sorted(glob.glob("images/requests/*.json")):
    req = json.load(open(path))
    out = f"images/out/{req['id']}.png"
    if os.path.exists(out):
        continue
    body = json.dumps({
        "model": MODEL,
        "prompt": req["prompt"],
        "size": SIZES.get(req.get("shape", "square"), "1024x1024"),
        "n": 1,
    }).encode()
    r = urllib.request.Request(
        "https://api.openai.com/v1/images/generations", data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        resp = json.load(urllib.request.urlopen(r, timeout=300))
    except urllib.error.HTTPError as e:
        print(f"{req['id']}: HTTP {e.code} {e.read().decode()[:500]}", file=sys.stderr)
        sys.exit(1)
    open(out, "wb").write(base64.b64decode(resp["data"][0]["b64_json"]))
    print(f"painted {out}")
    made += 1
print(f"{made} new painting(s)")
