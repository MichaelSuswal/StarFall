"""Self-tests for the build 2 and build 3 tools: roll ids and die mappings, the map tool's knowledge
rules and drawing, lockcheck on the fixture campaign, and check.py's waited rule.

Run with `python3 -m pytest tests/tools` or `python3 tests/tools/run.py`.
Only the standard library and Pillow are needed.
"""
import contextlib
import io
import json
import math
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import roll  # noqa: E402
import map as mapt  # noqa: E402
import lockcheck  # noqa: E402
import check  # noqa: E402

FIXTURE = os.path.join(HERE, "fixtures", "repo")


def run_quiet(fn, *a, **k):
    out, err = io.StringIO(), io.StringIO()
    code = 0
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            r = fn(*a, **k)
            code = r if isinstance(r, int) else 0
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
    return code, out.getvalue(), err.getvalue()


@contextlib.contextmanager
def tmpcopy():
    d = tempfile.mkdtemp()
    try:
        dst = os.path.join(d, "repo")
        shutil.copytree(FIXTURE, dst)
        yield dst
    finally:
        shutil.rmtree(d)


def read_lines(path):
    return [json.loads(l) for l in open(path) if l.strip()]


# ---------------------------------------------------------------- roll.py

def test_die_mappings():
    for roll_v in range(1, 101):
        assert roll.face_of("d20", roll_v) == ((roll_v - 1) % 20) + 1
        assert roll.face_of("d10", roll_v) == ((roll_v - 1) % 10) + 1
        assert roll.face_of("d12", roll_v) == (None if roll_v > 96 else ((roll_v - 1) % 12) + 1)
        assert roll.face_of("d30", roll_v) == (None if roll_v > 90 else ((roll_v - 1) % 30) + 1)
        assert roll.face_of("d6", roll_v) == (None if roll_v > 96 else ((roll_v - 1) % 6) + 1)
        assert roll.face_of("d8", roll_v) == (None if roll_v > 96 else ((roll_v - 1) % 8) + 1)
    # every face is equally likely over the draws that are kept
    for die, (limit, faces) in roll.DICE.items():
        counts = {}
        for roll_v in range(1, 101):
            f = roll.face_of(die, roll_v)
            if f is not None:
                counts[f] = counts.get(f, 0) + 1
        assert sorted(counts) == list(range(1, faces + 1)), die
        assert len(set(counts.values())) == 1, die


def test_roll_ids_and_auto_reroll():
    d = tempfile.mkdtemp()
    try:
        log = os.path.join(d, "rolls.jsonl")
        with open(log, "w") as f:  # two lines written before ids existed
            f.write('{"who": "k", "what": "old 1", "roll": 3}\n{"who": "k", "what": "old 2", "roll": 4}\n')
        seq = iter([99, 97, 40])  # d12: two draws above 96, then 40
        real = roll.draw
        roll.draw = lambda: next(seq)
        try:
            run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "form", "--die", "d12"])
        finally:
            roll.draw = real
        lines = read_lines(log)
        assert [l.get("id") for l in lines[2:]] == ["r-0003", "r-0004", "r-0005"]
        assert lines[2]["face"] is None and "reason" not in lines[2]
        assert lines[3]["reason"] == "die reroll" and lines[3]["replaces"] == "r-0003" and lines[3]["face"] is None
        assert lines[4]["reason"] == "die reroll" and lines[4]["replaces"] == "r-0004" and lines[4]["face"] == 4
        for l in lines[2:]:
            assert "success" not in l and "odds" not in l
            assert l["time"].endswith("Z") and l["pacific"][-6:] in ("-08:00", "-07:00")
        # contest mode keeps odds and success
        code, out, _ = run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "raid", "--factor", "numbers=+10"])
        e = read_lines(log)[-1]
        assert e["id"] == "r-0006" and e["odds"] == 60 and "success" in e and json.loads(out)["id"] == "r-0006"
        # manual reroll: needs both fields and a real id
        assert run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "raid", "--reason", "x"])[0] != 0
        assert run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "raid", "--reason", "x", "--replaces", "r-0099"])[0] != 0
        assert run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "form", "--die", "d12", "--factor", "a=+5"])[0] != 0
        run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "raid", "--die", "d20", "--reason", "same as god 1", "--replaces", "r-0006"])
        e = read_lines(log)[-1]
        assert e["id"] == "r-0007" and e["replaces"] == "r-0006" and e["reason"] == "same as god 1" and 1 <= e["face"] <= 20
    finally:
        shutil.rmtree(d)


def test_d100_and_log_required():
    d = tempfile.mkdtemp()
    try:
        log = os.path.join(d, "rolls.jsonl")
        for _ in range(5):
            run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "lean", "--die", "d100"])
        for e in read_lines(log):
            assert e["die"] == "d100" and e["face"] == e["roll"] and 1 <= e["face"] <= 100
            assert "odds" not in e and "success" not in e and "reason" not in e
        code, _, err = run_quiet(roll.main, ["--who", "k", "--what", "x", "--die", "d6"])
        assert code != 0 and "--campaign" in err
    finally:
        shutil.rmtree(d)


def test_campaign_log_path():
    class A:
        log = None
        campaign = "zz"
    assert roll.log_path(A()).endswith(os.path.join("SPOILERS_do_not_open", "campaigns", "zz", "state", "rolls.jsonl"))


# ---------------------------------------------------------------- map.py

def fx_paths(repo):
    return (os.path.join(repo, "SPOILERS_do_not_open", "campaigns", "fx", "map.json"),
            os.path.join(repo, "campaigns", "fx", "player", "map-knowledge.json"))


def test_grid_and_validate():
    world_p, know_p = fx_paths(FIXTURE)
    world = json.load(open(world_p))
    p = mapt.Painting(world)
    assert (p.ncols, p.nrows) == (5, 4) and len(p.cells()) == 20
    assert p.cell_of((0, 0)) == "A1" and p.cell_of((999, 799)) == "E4" and p.cell_of((450, 410)) == "C3"
    assert p.parse_cell("F1") is None and p.parse_cell("A5") is None and p.cell_center("b2") == (300.0, 300.0)
    assert mapt.check_world(world) == []
    assert mapt.knowledge_problems(world, json.load(open(know_p))) == []
    legacy = mapt.Painting({"painting": {"size": [1024, 1024], "grid_cell_px": 128}})
    assert (legacy.ncols, legacy.nrows) == (8, 8)
    assert (mapt.Painting({}).ncols, mapt.Painting({}).nrows) == (5, 4)
    bad = json.loads(json.dumps(world))
    bad["regions"][0]["neighbors"].append({"id": "r99", "days": 3})
    bad["landings"]["god-x"] = "r98"
    bad["features"].append({"id": "kings-fort", "name": "Fort", "type": "road", "shape": "point", "coords": [[1, 1]]})
    probs = mapt.check_world(bad)
    assert any("neighbor r99" in x for x in probs) and any("landing god-x" in x for x in probs)
    assert any("not opaque" in x for x in probs) and any("a road is a line" in x for x in probs)
    bad = json.loads(json.dumps(world))
    del bad["painting"]["miles_per_pixel"]
    del bad["regions"][1]["climate"]
    bad["plane"]["starfalls"].append({"id": "p01"})
    bad["plane"]["to_fall"].append({"id": "star-x"})
    probs = mapt.check_world(bad)
    assert "painting: no miles_per_pixel" in probs and "region r02: no climate" in probs
    assert "duplicate id p01 (plane)" in probs and any("plane id star-x" in x for x in probs)
    assert mapt.DEFAULT_MPP == 2.5


def reveal(repo, *args):
    world_p, know_p = fx_paths(repo)
    return run_quiet(mapt.main, ["reveal", "fx", "--world", world_p, "--knowledge", know_p,
                                 "--out", os.path.dirname(know_p), *args])


def test_reveal_rules():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        # a rumor gets a name and a cell, never a pixel
        code, out, err = reveal(repo, "--feature", "f05", "--grade", "rumored", "--source", "a tinker", "--year", "2",
                                "--name", "a drowned hold", "--cell", "b4")
        assert code == 0, err
        k = json.load(open(know_p))
        assert k["features"]["f05"]["told"] == {"name": "a drowned hold", "cell": "B4"}
        assert reveal(repo, "--feature", "f05", "--grade", "rumored", "--source", "x", "--year", "2",
                      "--told", '{"name": "n", "near": [1, 2]}')[0] != 0
        assert reveal(repo, "--feature", "f05", "--grade", "rumored", "--source", "x", "--year", "2", "--cell", "Z9")[0] != 0
        # a rumored region carries a name and a cell only
        code, out, err = reveal(repo, "--region", "r03", "--grade", "rumored", "--source", "a shepherd", "--year", "2",
                                "--name", "the high moor", "--cell", "a4")
        assert code == 0, err
        assert json.load(open(know_p))["regions"]["r03"]["told"] == {"name": "the high moor", "cell": "A4"}
        assert reveal(repo, "--region", "r03", "--grade", "rumored", "--source", "x", "--year", "2",
                      "--told", '{"name": "m", "polygon": [[0, 0], [1, 0], [1, 1]]}')[0] != 0
        assert reveal(repo, "--region", "nowhere", "--grade", "seen", "--source", "x", "--year", "2")[0] != 0
        # seen corrects a report, drops told and logs the correction
        code, out, _ = reveal(repo, "--feature", "f04", "--grade", "seen", "--source", "walked", "--year", "2")
        assert code == 0 and "told at" in out
        k = json.load(open(know_p))
        assert "told" not in k["features"]["f04"] and k["features"]["f04"]["grade"] == "seen"
        # lowering needs --force
        assert reveal(repo, "--feature", "f04", "--grade", "reported", "--source", "x", "--year", "2")[0] != 0
        code, out, _ = reveal(repo, "--feature", "f01", "--grade", "rumored", "--source", "x", "--year", "2",
                              "--cell", "B2", "--name", "a market town", "--force", "chart proved false")
        assert code == 0
        log = open(os.path.join(os.path.dirname(know_p), "map-log.md")).read()
        assert "feature f05 | none -> rumored" in log and "forced: chart proved false" in log
        assert log.splitlines()[-1].startswith(f"- {mapt.pacific_today()} |")
        # a rumor needs the name as told; the Keeper's name is never filled in
        assert reveal(repo, "--feature", "u01", "--grade", "rumored", "--source", "x", "--year", "2", "--cell", "B2")[0] != 0
        world = json.load(open(world_p))
        assert mapt.knowledge_problems(world, json.load(open(know_p))) == []


def test_migrate_older_file():
    world_p, _ = fx_paths(FIXTURE)
    world = json.load(open(world_p))
    old = {"regions": {"r03": {"grade": "rumored", "source": "s", "year": 1, "told": {"name": "moor", "near": [100, 500]}},
                       "r01": {"grade": "seen", "source": "s", "year": 1, "told": {"name": "x"}}},
           "features": {"f05": {"grade": "rumored", "source": "s", "year": 1, "told": {"name": "hold", "near": [260, 620]}}}}
    assert mapt.knowledge_problems(world, old)
    notes = mapt.migrate(world, old, mapt.Painting(world))
    assert notes and old["regions"]["r03"]["told"] == {"name": "moor", "cell": "A3"}
    assert old["features"]["f05"]["told"] == {"name": "hold", "cell": "B4"}
    assert mapt.knowledge_problems(world, old) == []


def make_paintings(folder, size=(1000, 800)):
    from PIL import Image, ImageDraw
    os.makedirs(folder, exist_ok=True)
    im = Image.new("RGB", size, (120, 150, 90))
    ImageDraw.Draw(im).rectangle([500, 400, size[0], size[1]], fill=(60, 90, 130))
    im.save(os.path.join(folder, "surface.png"))
    Image.new("RGB", size, (70, 60, 50)).save(os.path.join(folder, "under-1.png"))
    Image.new("RGB", size, (200, 200, 205)).save(os.path.join(folder, "clouds.png"))


def test_draw_and_gazetteer():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        paint = os.path.join(repo, "paint")
        out = os.path.join(repo, "out")
        make_paintings(paint)
        k = json.load(open(know_p))
        k["features"]["u01"] = {"grade": "seen", "source": "walked", "year": 1}
        k["regions"]["r01"]["named"] = True
        json.dump(k, open(know_p, "w"))
        code, o, err = run_quiet(mapt.main, ["draw", "fx", "--world", world_p, "--knowledge", know_p, "--paintings", paint,
                                             "--out", out, "--zoom", "known"])
        assert code == 0, err
        assert os.path.exists(os.path.join(out, "map.png")) and os.path.exists(os.path.join(out, "map-under-1.png"))
        meta = json.load(open(os.path.join(out, "map-meta.json")))
        assert meta["grid"] == [5, 4] and "frames_px" not in meta
        code, o, err = run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        assert "px" not in g and "Hollow Moor" not in g and "Brackwater" not in g and "Cinder Gap" not in g
        assert "the cinder road" in g and "somewhere near A3" in g and "(pass)" not in g
        assert "The Chalk Way" in g
        # a reported region (no told shape) gets no sealed travel days, only what was told
        assert "6 days" not in g and "**The Wend Downs** to **the Reach**: distance not told (reported)." in g


# ---------------------------------------------------------------- lockcheck.py

def lock(repo, *flags):
    return run_quiet(lockcheck.main, ["fx", "--root", repo, *flags])


def append(repo, rel, text):
    path = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(text)


def test_lockcheck_clean_fixture():
    code, out, err = lock(FIXTURE)
    assert code == 0, out + err
    for c in ("places", "leaks", "mysteries", "rolls", "dashes"):
        assert f"{c}: 0 failure(s)" in out


def test_lockcheck_places():
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/notes.md", "The road to [r77] and [f01, f99]. Hollow Moor is cold.\n")
        code, out, _ = lock(repo, "--places")
        assert code == 1 and "[r77]" in out and "[f99]" in out and "[f01]" not in out
        assert 'WARN places' in out and '"Hollow Moor"' in out
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/deep-history.md", "The first fall [p01]; a second [p02].\n")
        code, out, _ = lock(repo, "--places")
        assert code == 1 and "[p02]" in out and "[p01]" not in out


def test_lockcheck_leaks():
    pub = "campaigns/fx/player/notes.md"
    cases = [("Vessaline walks the shore.", "sealed term"),
             ("They hail the Tide-Mother.", "sealed term"),
             ("They speak of god-tide.", "god label"),
             ("There are two other gods.", "god count"),
             ("Beyond lies Hollow Moor.", "unknown place"),
             ("The bell hum came on 5 nights.", "phenomenon count"),
             ("The ceiling here is 73.", "star value"),
             ("A drowned crystal orchard, they say.", "star value"),
             ("They whisper of The Silent Bell.", "mystery title"),
             ("Remember the Founders' Quarrel.", "schedule title"),
             ("A lantern of brine? No, the Lantern of Brine.", "sealed term"),
             ("They fear the Undertow Oath.", "sealed term"),
             ("They fear Undertow Oath.", "sealed term"),
             ("An old song about Saltreach.", "sealed term"),
             ("The last of Orvanne.", "sealed term"),
             ("We were seven when we came down.", "number word"),
             ("Seven of us, they say.", "number word"),
             ("Half a dozen gods walk here.", "number word"),
             ("The star pulls twice a year.", "number word"),
             ("There are two like me in the hills.", "number word")]
    for text, kind in cases:
        with tmpcopy() as repo:
            append(repo, pub, text + "\n")
            code, out, _ = lock(repo, "--leaks")
            assert code == 1 and kind in out, (text, out)
    with tmpcopy() as repo:  # the campaign's public scene requests are scanned too
        append(repo, "images/requests/fx-002-morning.json", '{"id": "fx-002-morning", "prompt": "dawn over Hollow Moor"}\n')
        append(repo, "images/requests/other-002-morning.json", '{"id": "other", "prompt": "Hollow Moor"}\n')
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "fx-002-morning.json" in out and "other-002" not in out
    with tmpcopy() as repo:  # held scene requests are scanned too; the sealed held folder is not
        append(repo, "images/held/fx-001-morning.json", '{"id": "fx-001-morning", "prompt": "dawn over Hollow Moor"}\n')
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "images/held/fx-001-morning.json" in out
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/images/held/fx-map-surface.json", '{"id": "x", "prompt": "Hollow Moor"}\n')
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # the allowlist exempts a term
        append(repo, pub, "Beyond lies Hollow Moor.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/leak-allow.txt", "Hollow Moor\n")
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # a rumored region with a cell is fine; a rumor with a pixel fails
        _, know_p = fx_paths(repo)
        k = json.load(open(know_p))
        k["regions"]["r03"] = {"grade": "rumored", "source": "s", "year": 1, "told": {"name": "moor", "cell": "A3"}}
        json.dump(k, open(know_p, "w"))
        assert lock(repo, "--leaks")[0] == 0
        k["regions"]["r03"]["told"]["near"] = [100, 500]
        k["features"]["f06"]["told"] = {"name": "the cinder road", "near": [100, 500]}
        json.dump(k, open(know_p, "w"))
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "region r03: a rumor carries a cell, never pixels" in out and "feature f06" in out


def test_lockcheck_mysteries():
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/mysteries.md",
               "\n## SHORT 1. The Lost Ram\n\n**Truth.** A fox.\n\n**Body.** The fold.\n\n**Clues.** Tufts of wool.\n\n**Branches.** Hunt it.\n")
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and "The Lost Ram" in out
        assert "Cost if ignored" in out and "Never found" in out and "readings" in out and "world does" in out
        assert "The Silent Bell" not in out and "no Kind: line" in out
    with tmpcopy() as repo:
        mp = os.path.join(repo, "SPOILERS_do_not_open/campaigns/fx/mysteries.md")
        t = open(mp).read()
        t = t.replace("Location: [f01]\n", "", 1)
        t = t.replace("Limit: it knows only", "It knows only")
        t = t.replace("Kind: short.", "Kind: long.", 1)
        t = t.replace("What the world does: every dog", "Every dog", 1)
        open(mp, "w").write(t)
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1
        assert 'clue "Founders refuse moor tin" has no Location:' in out
        assert "Answers questions: yes, but no Limit: line in its Truth or Body" in out
        assert "has no What the world does:" in out
        assert "kinds: 1 epic, 3 long, 2 short" in out


def test_lockcheck_rolls_and_dashes():
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/notes.md", "Set by r-0042.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/state/rolls.jsonl",
               '{"id": "r-0006", "who": "k", "what": "fx bell age", "die": "d20", "roll": 3, "face": 3}\n'
               '{"id": "r-0007", "who": "k", "what": "fx ceiling", "die": "d10", "roll": 5, "face": 5, "replaces": "r-0002"}\n')
        append(repo, "campaigns/fx/player/notes.md", "A long pause \u2014 then rain.\n")
        code, out, _ = lock(repo, "--rolls", "--dashes")
        assert code == 1
        assert "cites r-0042" in out and "rolled more than once" in out and "has no reason" in out
        assert "dashes: 1 failure(s)" in out
        # build 7 (change list 70): the public log holds the DM's open rolls; a line that is not the DM's fails
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"what": "public"}\n')
        assert "is not the DM's" in lock(repo, "--rolls")[1]


# ---------------------------------------------------------------- check.py

def test_check_waited_and_clock():
    with tmpcopy() as repo:
        base = os.path.join(repo, "campaigns", "fx")
        append(repo, "campaigns/fx/years/001/waited-2026-11-20.md", "The world waited.\n")
        append(repo, "campaigns/fx/state/timing.md",
               "## Year 1 (Pacific)\n- 2026-11-20 01:45 no decisions file; the world waited.\n"
               "- 2026-11-21 01:45 decisions found; turn started, year 1 open.\n"
               "- 2026-11-21 03:10 clock advanced to year 2.\n"
               "Notes for 2026-11-21: the world waited for nothing; clock advanced, as the heading says.\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 0, out  # waited: clock stays on year 1; undated lines and "year 1 open" do not count
        append(repo, "campaigns/fx/state/timing.md", "- 2026-11-22 01:45 the world waited.\n2026-11-22 03:00 clock advanced\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 1 and "timing: 2026-11-22 has both a waited line and a clock advance" in out
        assert "2026-11-20" not in out and "2026-11-21" not in out
        with open(os.path.join(base, "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 0\nstatus: creation\ncreation_night: 3b\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 0 and out.strip().count("\n") == 0 and "does not apply during creation" in out
    with tmpcopy() as repo:  # a year that turned needs the decisions file or a waited note
        with open(os.path.join(repo, "campaigns", "fx", "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 2\nstatus: open\nseason_opens: spring\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 1 and "engage: year 1 turned with no player/decisions-001.md and no waited note" in out
        append(repo, "campaigns/fx/player/decisions-001.md", "Go north.\n")
        assert "engage:" not in run_quiet(check.main, ["fx", "1", "--root", repo])[1]
    for night in ("1", "2", "3a", "3b"):
        assert check.clock_problems({"campaign": "x", "year": "0", "status": "creation", "creation_night": night, "season_opens": "s"}) == []
    assert check.clock_problems({"campaign": "x", "year": "0", "status": "creation", "creation_night": "3", "season_opens": "s"})
    assert check.clock_problems({"campaign": "x", "year": "1", "status": "open", "creation_night": "2", "season_opens": "s"})


# ---------------------------------------------------------------- build 3: lockcheck

def test_lockcheck_sealed_terms_primary():
    pub = "campaigns/fx/player/notes.md"
    sealed = "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt"
    with tmpcopy() as repo:  # the file is read as written, case and all; comments are skipped
        append(repo, sealed, "# Hidden Name in a comment\nGrey Warden\n")
        append(repo, pub, "A grey warden passed. Hidden Name is not a term.\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, pub, "The Grey Warden passed.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'sealed term "Grey Warden"' in out
    with tmpcopy() as repo:  # a map name the god has seen or been told stays on the list and may appear
        _, know_p = fx_paths(repo)
        k = json.load(open(know_p))
        k["regions"]["r01"]["named"] = True
        json.dump(k, open(know_p, "w"))
        append(repo, sealed, "The Wend Downs\nthe cinder road\nHollow Moor\n")
        append(repo, pub, "The Wend Downs and the cinder road.\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, pub, "Hollow Moor.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'sealed term "Hollow Moor"' in out
    with tmpcopy() as repo:  # a one-word remainder is matched only with its article
        append(repo, sealed, "the Stray\n")
        append(repo, pub, "Stray dogs came.\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, pub, "They saw the Stray.\n")
        assert lock(repo, "--leaks")[0] == 1
    with tmpcopy() as repo:  # the old guesses from prose only warn
        os.remove(os.path.join(repo, sealed))
        append(repo, sealed, "# nothing sealed\n")
        append(repo, pub, "Vessaline walks the shore.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0 and 'WARN leaks' in out and 'god name "Vessaline"' in out and "sealed-terms.txt" in out
    with tmpcopy() as repo:  # a missing sealed-terms.txt fails
        os.remove(os.path.join(repo, sealed))
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "sealed-terms.txt is missing" in out
    with tmpcopy() as repo:  # mystery titles are matched case and all
        append(repo, pub, "the silent bell rang at dusk.\n")
        assert lock(repo, "--leaks")[0] == 0


def test_lockcheck_number_words():
    hits = lockcheck.count_hits
    assert hits("We were seven when we came down.")
    assert hits("the seven of us") and hits("A dozen gods") and hits("half a dozen like us walk")
    assert [h[0] for h in hits("It fell twice that winter.")] == ["twice"]
    assert not hits("No one came down the track.") and not hits("A god here has one body.")  # "one" is never a count
    assert not hits("Seven sheep. The god sleeps.")  # another sentence
    assert not hits("seven fields of barley and rye and oats and wheat lay by the god")  # more than six words apart
    assert hits("seven fields of barley and rye, the god")  # six words between
    assert not hits("seven fields of barley and rye by the god")  # seven words between
    assert [h[0] for h in hits("We were 7 when we came down.")] == ["7"] and hits("12 of us")
    assert not hits("On Day 3 the god named them.") and not hits("Question 8, how much a god sees.")
    assert not hits("1 god") and not hits("13 gods came down") and not hits("2.5 miles from the god") and not hits("1,200 feet below the god")
    assert not hits("thirteen gods")  # two to twelve only; the count of gods itself is its own check
    with tmpcopy() as repo:  # a number-word hit is exempted by its quoted phrase
        append(repo, "campaigns/fx/player/notes.md", "Snow fell two winters running.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'number word "two" near "fell": "fell two"' in out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/leak-allow.txt", "fell two\n")
        assert lock(repo, "--leaks")[0] == 0


def test_lockcheck_answers_field():
    mp = "SPOILERS_do_not_open/campaigns/fx/mysteries.md"
    with tmpcopy() as repo:  # wording no longer decides: "no" with oracle words passes
        path = os.path.join(repo, mp)
        t = open(path).read().replace("The answer to the lost ewe is plain", "An oracle answers questions; the answer is plain", 1)
        open(path, "w").write(t)
        assert lock(repo, "--mysteries")[0] == 0
    with tmpcopy() as repo:
        path = os.path.join(repo, mp)
        t = open(path).read()
        t = t.replace("Related to: none. Answers questions: no.", "Related to: none.", 1)
        t = t.replace("Related to: none. Answers questions: no.", "Related to: none. Answers questions: maybe.", 1)
        t = t.replace("Related to: none. Answers questions: no.", "Related to: none. Answers questions: yes.", 1)
        open(path, "w").write(t)
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1
        assert '"The Silent Bell": no Answers questions: line' in out
        assert '"The Grey Tithe": Answers questions: must be yes or no' in out
        assert '"The Salt Debt": Answers questions: yes, but no Limit: line' in out
        assert "The Drowned Choir" not in out


def test_lockcheck_skips_flags_files():
    with tmpcopy() as repo:
        for rel in ("SPOILERS_do_not_open/campaigns/fx/years/000/lock-flags.md",
                    "SPOILERS_do_not_open/campaigns/fx/years/000/lock-flags-round2.md",
                    "campaigns/fx/years/000/lock-flags.md"):
            append(repo, rel, "Flag: Hollow Moor [r77] cited r-0099, Vessaline \u2014 seven gods came down.\n")
        code, out, _ = lock(repo, "--all")
        assert code == 0, out
        # a year's flags.md is the checker's file too, skipped from build 8 on (run 07 change list 26)
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/000/flags.md", "[r77]\n")
        assert lock(repo, "--places")[0] == 0
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/000/notes.md", "[r77]\n")
        assert lock(repo, "--places")[0] == 1


# ---------------------------------------------------------------- build 3: paint

def test_paint_skips_held():
    import paint
    d = tempfile.mkdtemp()
    try:
        for rel in ("images/requests/zz-a.json", "images/requests/held/zz-b.json", "images/held/zz-c.json",
                    "SPOILERS_do_not_open/images/requests/held/zz-d.json"):
            path = os.path.join(d, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            json.dump({"id": os.path.splitext(os.path.basename(rel))[0], "prompt": "x"}, open(path, "w"))
        os.makedirs(os.path.join(d, "campaigns", "zz", "state"))
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("- zz-a: approved\n- zz-b: approved\n- zz-c: approved\n- zz-d: approved\n")
        assert [r["id"] for _p, r, _t in paint.pending(d)] == ["zz-a"]
        assert paint.is_held(os.path.join(d, "images/held/zz-c.json"), d)
        assert not paint.is_held(os.path.join(d, "images/requests/zz-a.json"), d)
    finally:
        shutil.rmtree(d)
    wf = open(os.path.join(ROOT, ".github", "workflows", "paint.yml")).read()
    assert 'paths: ["images/requests/**", "SPOILERS_do_not_open/images/requests/**"]' in wf and "images/held" not in wf.split("paths:")[1].split("\n")[0]


# ---------------------------------------------------------------- build 3: map.py

def test_stamp():
    with tmpcopy() as repo:
        world_p, _ = fx_paths(repo)
        S = os.path.dirname(world_p)
        append(repo, "SPOILERS_do_not_open/campaigns/fx/notes.md",
               "Tallowford and Tallowford's market [f01]. The Wend Downs, Wend Downs again. "
               "Mewsby (the village) [f04]. River Wend runs. Not Tallowfordish. [Tallowford]\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/000/lock-flags.md", "Tallowford\n")
        append(repo, "campaigns/fx/player/notes2.md", "Tallowford\n")
        before_pub = open(os.path.join(repo, "campaigns/fx/player/notes2.md")).read()
        world = json.load(open(world_p))
        changed, total, per = mapt.stamp("fx", S, world, dry_run=True)
        assert open(os.path.join(S, "notes.md")).read().startswith("Tallowford and")  # dry run changes nothing
        changed, total, per = mapt.stamp("fx", S, world)
        t = open(os.path.join(S, "notes.md")).read()
        assert t.startswith("Tallowford [f01] and Tallowford's [f01] market [f01]. The Wend Downs [r01], Wend Downs [r01] again. "
                            "Mewsby (the village) [f04]. River Wend [f02] runs. Not Tallowfordish. [Tallowford]"), t
        assert dict(per)["notes.md"] == 5
        assert open(os.path.join(S, "years/000/lock-flags.md")).read() == "Tallowford\n"
        assert open(os.path.join(repo, "campaigns/fx/player/notes2.md")).read() == before_pub
        # idempotent; and the stamped files pass lockcheck --places with no bare-name warning for them
        assert mapt.stamp("fx", S, world)[1] == 0
        code, out, _ = lock(repo, "--places")
        # only the bracketed "[Tallowford]" (link text, never stamped) is left bare
        assert 'notes.md: map name "Tallowford" written 1 time(s)' in out and '"Wend Downs"' not in out
        # the command line reports counts
        code, out, _ = run_quiet(mapt.main, ["stamp", "fx", "--world", world_p, "--sealed", S, "--dry-run"])
        assert code == 0 and "would stamp 0 name(s) in 0 file(s)" in out


def small_world():
    """Three regions on a 100 by 100 painting at 2 miles a pixel: a valley floor at 1,000 feet with a
    town and a river by the landing, ridges to 2,800 feet to the east, and peaks to 11,000 feet beyond."""
    return {"campaign": "t", "painting": {"size": [100, 100], "miles_per_pixel": 2.0, "grid": {"cols": 5, "rows": 4}},
            "regions": [
                {"id": "r01", "name": "Vale of Osk", "terrain": "valley, a long vale", "elevation": "upland, 1,000 to 1,400 feet",
                 "water": "the Osk Water, quick", "climate": "cool", "neighbors": [{"id": "r02", "days": 3}],
                 "polygon": [[0, 0], [40, 0], [40, 100], [0, 100]]},
                {"id": "r02", "name": "The Shoulders", "terrain": "hill", "elevation": "hill, to 2,800 feet", "water": "springs",
                 "climate": "cool", "neighbors": [{"id": "r01", "days": 3}, {"id": "r03", "days": 9}],
                 "polygon": [[40, 0], [60, 0], [60, 100], [40, 100]]},
                {"id": "r03", "name": "The White Teeth", "terrain": "mountain", "elevation": "high, to 11,000 feet", "water": "snow",
                 "climate": "cold", "neighbors": [{"id": "r02", "days": 9}],
                 "polygon": [[60, 0], [100, 0], [100, 100], [60, 100]]}],
            "features": [
                {"id": "f01", "name": "Oskby", "type": "town", "shape": "point", "coords": [[20.4, 50.3]], "regions": ["r01"]},
                {"id": "f02", "name": "Osk Water", "type": "river", "shape": "line", "coords": [[20.6, 0], [20.6, 49.5], [20.6, 100]], "regions": ["r01"]},
                {"id": "f03", "name": "Hob Hole", "type": "cave", "shape": "point", "coords": [[20.2, 50.4]], "regions": ["r01"]},
                {"id": "f04", "name": "Farstead", "type": "village", "shape": "point", "coords": [[30, 50]], "regions": ["r01"]}],
            "landings": {"player": {"region": "r01", "at": [20.2, 50.1]}}}


def test_describe_and_sight():
    w = small_world()
    assert mapt.check_world(w) == []
    # the sight rule's worked figures
    assert round(mapt.sight_miles(0), 1) == 3.0
    assert round(mapt.sight_miles(1800)) == 55 and round(mapt.sight_miles(11800)) == 136
    assert mapt.parse_elevation({"elevation": "upland, 1,200 to 2,500 feet"}) == (1200, 2500, True)
    assert mapt.parse_elevation({"elevation": "hill, to 4,000 feet"})[1] == 4000
    assert mapt.parse_elevation({"elevation": "low"})[2] is False
    land = w["landings"]["player"]
    k = {"regions": {"r01": {"grade": "seen", "source": "landing", "year": 1, "named": True}},
         "features": {"f02": {"grade": "reported", "source": "own sight", "year": 1, "told": {"name": "the quick water"}}}}
    t = mapt.describe(w, "r01", mapt.landing_point(land), k, reference=False)
    # names: seen and told names only; every other name put plainly, in free text too
    assert "Vale of Osk" in t and "the quick water, quick" in t and "the quick water (river)" in t
    for sealed in ("Osk Water", "Oskby", "Shoulders", "White Teeth", "Hob Hole", "Farstead"):
        assert sealed not in t, sealed
    assert "a town (town), about half a mile south-east" in t and "lying east: 3 days on foot" not in t and "Neighbors" not in t
    tr = mapt.describe(w, "r01", mapt.landing_point(land), k, reference=True)
    assert "Neighbors (reference for the Keeper, not the seen view):" in tr and "a hill country (hill), lying east: 3 days on foot" in tr
    assert "the quick water (river), about a mile east, about 4 miles of it in view, from the north-east to the south-east" in t
    # sight (map.md 1.4): the town, river and cave mouth within two miles of a valley floor; the village
    # 20 miles off in the same valley shows only as its smoke, walls or lights
    assert "from a valley floor or plain" in t and "a cave (cave), about half a mile south" in t
    assert "Farther off, seen only as smoke, walls or lights:\n- a village, about 20 miles east" in t
    # the ridges (top 2,800 over the 1,000-foot floor) are on the skyline 40 miles east
    assert "a hill country (hill), east, about 40 miles to its nearest edge: on the skyline" in t
    # the peaks (relief 10,000, reach about 125 miles) stand 80 miles off, behind the ridges or over them by the line
    assert "a mountain country" in t
    tn = mapt.describe(w, "r01", mapt.landing_point(land), k, all_names=True, reference=True)
    assert "Oskby (town)" in tn and "The Shoulders" in tn and "Osk Water" in tn
    # a region described from its middle when no point is given; from a hill the skyline stops at forty miles
    th = mapt.describe(w, "r02", None, None)
    assert "from the middle of the region" in th and "from a hill, ridge or height" in th
    assert "a mountain country (mountain), east, about 20 miles" in th and "a valley country (valley), west" in th
    w3 = json.loads(json.dumps(w))
    for poly_r in w3["regions"]:
        poly_r["polygon"] = [[x * 3 if x > 40 else x, y] for x, y in poly_r["polygon"]]
    w3["painting"]["size"] = [300, 100]
    th3 = mapt.describe(w3, "r02", [100, 50], None)
    assert "a mountain country" not in th3.split("In view")[1]  # 80 miles off: past the forty-mile skyline
    # hidden: raise the ridges so that they stand above the line to the peaks
    w2 = json.loads(json.dumps(w))
    w2["regions"][1]["elevation"] = "hill, to 9,000 feet"
    t2 = mapt.describe(w2, "r01", mapt.landing_point(land), k)
    assert "hidden behind a hill country" in t2
    # the command line: by landing, from the god's knowledge file
    d = tempfile.mkdtemp()
    try:
        wp, kp = os.path.join(d, "map.json"), os.path.join(d, "k.json")
        json.dump(w, open(wp, "w"))
        json.dump(k, open(kp, "w"))
        code, out, err = run_quiet(mapt.main, ["describe", "t", "--world", wp, "--knowledge", kp, "--landing", "player"])
        assert code == 0 and out.startswith("Landing of player: Vale of Osk") and out.split("\n", 1)[1] == t.split("\n", 1)[1], err
        code, out2, _ = run_quiet(mapt.main, ["describe", "t", "--world", wp, "--knowledge", kp, "--landing", "player", "--reference"])
        assert "Neighbors (reference" in out2 and "lying east: 3 days" in out2
        assert run_quiet(mapt.main, ["describe", "t", "--world", wp, "--landing", "god-x"])[0] != 0
        assert run_quiet(mapt.main, ["describe", "t", "--world", wp, "--region", "r09"])[0] != 0
    finally:
        shutil.rmtree(d)


def test_one_decimal_coordinates():
    w = small_world()
    assert mapt.check_world(w) == []
    bad = json.loads(json.dumps(w))
    bad["features"][0]["coords"] = [["20.4", 50.3]]
    bad["landings"]["player"]["at"] = [20.2]
    probs = mapt.check_world(bad)
    assert any("f01: coordinate" in p for p in probs) and any("landing player: point" in p for p in probs)
    p = mapt.Painting(w)
    assert p.cell_of((20.2, 50.1)) == "B3"


def test_labels_never_overprint():
    from PIL import Image
    lab = mapt.Labeler((400, 300), bounds=(0, 0, 400, 300))
    lab.obstacle((190, 140, 210, 160))
    for i in range(12):
        lab.add((200, 150), [(f"A long place name {i}", 16, "regular", mapt.INK, 255, 0),
                             ("reported: a drover", 10, "italic", mapt.INK_LIGHT, 255, 14)],
                priority=50 + i, anchor="lm" if i % 2 else "mm", leader=True)
    dropped = lab.place()
    groups = lab.groups
    boxes = [mapt.bbox([(b[0], b[1]) for b in g] + [(b[2], b[3]) for b in g]) for g in groups]
    for i in range(len(boxes)):
        assert not Labeler_hit(boxes[i], (190, 140, 210, 160))
        for j in range(i + 1, len(boxes)):
            assert not Labeler_hit(boxes[i], boxes[j]), (boxes[i], boxes[j])
        assert 0 <= boxes[i][0] and boxes[i][2] <= 400 and 0 <= boxes[i][1] and boxes[i][3] <= 300
    assert len(groups) + len(dropped) == 12 and len(groups) >= 6 and lab.moved >= len(groups) - 1
    # the highest priority keeps its place
    assert "A long place name 11" not in dropped
    lab.flush(Image.new("RGBA", (400, 300)))


def Labeler_hit(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def test_landing_zoom():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        paint = os.path.join(repo, "paint")
        out = os.path.join(repo, "out")
        make_paintings(paint)
        world = json.load(open(world_p))
        painting = mapt.Painting(world)
        regions_k, features_k = mapt.gather(world, json.load(open(know_p)), painting)
        rect = mapt.landing_rect(regions_k, features_k, painting)
        # the seen region r01 is 0..400 by 0..400: a quarter margin, clamped to the painting
        assert rect == (0, 0, 500, 500)
        code, o, err = run_quiet(mapt.main, ["draw", "fx", "--world", world_p, "--knowledge", know_p, "--paintings", paint,
                                             "--out", out, "--zoom", "landing", "--layer", "surface"])
        assert code == 0, err
        meta = json.load(open(os.path.join(out, "map-meta.json")))
        assert meta["zoom"] == "landing" and meta["frames"]["surface"] == "A1:C3" and meta["frame_miles"]["surface"] == [500, 500]
        assert meta["labels_dropped"]["surface"] == 0
        # a tiny seen region still gets a sheet of at least LANDING_MIN_SIZE pixels, at its own scale bar
        tiny = {"r01": {"id": "r01", "grade": "seen", "polygon": [[500, 500], [504, 500], [504, 503]], "name": "x"}}
        r = mapt.landing_rect(tiny, {}, painting)
        assert r[2] - r[0] >= mapt.LANDING_MIN_SIZE and r[3] - r[1] >= mapt.LANDING_MIN_SIZE
        v = mapt.View(r)
        assert mapt.scale_bar(v, painting)[0] < mapt.scale_bar(mapt.View((0, 0, 1000, 800)), painting)[0]


# ---------------------------------------------------------------- build 4: lockcheck (run 03 items 30, 67, 74, 83)

def test_lockcheck_work_rate_and_count_phrases():
    hits = lockcheck.count_hits
    # work rates and counts of things are not counts of gods (item 30)
    for text in ("Two things about this god.", "The god cleared seven acres.", "It took the god two days.",
                 "five full days of walking for the god", "Three worker-days, the god said.", "a god's work: 3 days",
                 "twelve miles from the god", "The god asked two questions."):
        assert not hits(text), text
    # counts of gods still hit
    for text in ("We were seven when we came down.", "There are two gods here.", "seven of us",
                 "The star pulls twice a year.", "Two more gods", "two like me"):
        assert hits(text), text


def test_lockcheck_leak_allow_as_the_checker_writes_it():
    pub = "campaigns/fx/player/notes.md"
    allow = "SPOILERS_do_not_open/campaigns/fx/leak-allow.txt"
    assert lockcheck.allow_phrase('"fell two"  # frozen card text, ruled not a leak, 2026-11-21') == "fell two"
    assert lockcheck.allow_phrase("Hollow  Moor # a reason") == "hollow moor"
    assert lockcheck.allow_phrase("# a comment line") is None and lockcheck.allow_phrase("   ") is None
    with tmpcopy() as repo:
        append(repo, pub, "Snow fell two winters running.\n")
        assert lock(repo, "--leaks")[0] == 1
        append(repo, allow, "# checker, 2026-11-21: the snow, not a count of gods\n\"fell two\"  # frozen text, 2026-11-21\n")
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # a longer allowed phrase that holds the hit and stands in the line exempts it
        append(repo, pub, "Snow fell two winters running.\n")
        append(repo, allow, "snow fell two winters  # 2026-11-21\n")
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # a sealed term with an inline comment is exempted as before
        append(repo, pub, "Beyond lies Hollow Moor.\n")
        append(repo, allow, "Hollow Moor   # seen from the downs, ruled 2026-11-21\n")
        assert lock(repo, "--leaks")[0] == 0


def test_lockcheck_limit_matches_cast():
    cast = "SPOILERS_do_not_open/campaigns/fx/cast.md"
    with tmpcopy() as repo:  # the fixture's limit is in the cast word for word; emphasis and ids aside
        p = os.path.join(repo, cast)
        t = open(p).read().replace("Limit: it knows", "**Limit:** it [f02] knows")
        open(p, "w").write(t)
        assert lock(repo, "--mysteries")[0] == 0
    with tmpcopy() as repo:  # one word changed
        p = os.path.join(repo, cast)
        open(p, "w").write(open(p).read().replace("one question a year", "two questions a year"))
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and '"The Drowned Choir": its Limit: line is not in' in out and "word for word" in out
    with tmpcopy() as repo:  # no cast file
        os.remove(os.path.join(repo, cast))
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and "cast.md is missing" in out


def test_lockcheck_lower_case_places_and_headings():
    notes = "SPOILERS_do_not_open/campaigns/fx/notes.md"
    with tmpcopy() as repo:
        append(repo, notes, "We met at tallowford, then took the chalk way east. A hollow moor, the wend downs.\n")
        code, out, _ = lock(repo, "--places")
        assert code == 0  # a warning, as for a capitalized bare name
        assert 'map name "tallowford" written in lower case 1 time(s)' in out
        assert 'map name "chalk way" written in lower case 1 time(s)' in out
        assert 'map name "hollow moor" written in lower case' in out and 'map name "wend downs" written in lower case' in out
    with tmpcopy() as repo:  # with ids, no warning; a heading is never counted
        append(repo, notes, "## Tallowford and the Chalk Way\n\nWe met at tallowford [f01] and took the chalk way [f03].\n")
        out = lock(repo, "--places")[1]
        assert "Tallowford" not in out and "chalk way" not in out
    with tmpcopy() as repo:  # a name inside a longer map name belongs to the longer name (item 60)
        world_p, _ = fx_paths(repo)
        w = json.load(open(world_p))
        w["features"].append({"id": "f07", "name": "Tallowford Bridge", "type": "site", "shape": "point",
                              "coords": [[224, 262]], "regions": ["r01"]})
        json.dump(w, open(world_p, "w"))
        append(repo, notes, "At Tallowford Bridge [f07] we waited.\n")
        out = lock(repo, "--places")[1]
        assert '"Tallowford"' not in out and "places: 0 failure(s)" in out


def test_lockcheck_scans_request_files():
    with tmpcopy() as repo:  # by id or campaign field, whatever the file is called, at any depth
        append(repo, "images/requests/dawn.json", '{"id": "fx-003-morning", "prompt": "dawn over Hollow Moor"}\n')
        append(repo, "images/held/old/scene.json", '{"id": "x", "campaign": "fx", "prompt": "Hollow Moor at dusk"}\n')
        append(repo, "images/requests/other.json", '{"id": "zz-003-morning", "prompt": "Hollow Moor"}\n')
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "images/requests/dawn.json" in out and "images/held/old/scene.json" in out and "other.json" not in out
    with tmpcopy() as repo:  # dashes in any of the campaign's requests, sealed map requests too, escapes and all
        append(repo, "SPOILERS_do_not_open/images/requests/fx-map-surface.json", '{"id": "fx-map-surface", "prompt": "hills \\u2014 sea"}\n')
        append(repo, "images/requests/fx-004-morning.json", '{"id": "fx-004-morning", "prompt": "rain \u2013 wind"}\n')
        code, out, _ = lock(repo, "--dashes")
        assert code == 1 and "fx-map-surface.json" in out and "fx-004-morning.json" in out and "dashes: 2 failure(s)" in out


# ---------------------------------------------------------------- build 4: paint (item 83)

def test_paint_needs_images_md():
    import paint
    d = tempfile.mkdtemp()
    try:
        reqs = {"images/requests/zz-001-morning.json": "zz-001-morning", "images/requests/zz-002-morning.json": "zz-002-morning",
                "SPOILERS_do_not_open/images/requests/zz-map-surface.json": "zz-map-surface",
                "SPOILERS_do_not_open/images/requests/zz-map-surface-2.json": "zz-map-surface-2",
                "SPOILERS_do_not_open/images/requests/zz-map-under-1.json": "zz-map-under-1",
                "SPOILERS_do_not_open/images/requests/zz-map-clouds.json": "zz-map-clouds",
                "images/requests/yy-001-morning.json": "yy-001-morning"}
        for rel, rid in reqs.items():
            path = os.path.join(d, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            json.dump({"id": rid, "prompt": "x"}, open(path, "w"))
        os.makedirs(os.path.join(d, "campaigns", "zz", "state"))
        os.makedirs(os.path.join(d, "campaigns", "yy", "state"))
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("# Images approved for creation (zz)\n\n- surface sheet: approved\n- cloud sheet: approved\n"
                    "- first morning painting: approved\n- underground sheet: not approved; hold and ask Michael\n"
                    "- any repaint: not approved; hold and ask Michael\n")
        skipped = []
        todo = sorted(r["id"] for _p, r, _t in paint.pending(d, skipped))
        assert todo == ["zz-001-morning", "zz-map-clouds", "zz-map-surface"]
        why = {os.path.basename(p): w for p, w in skipped}
        assert set(why) == {"zz-002-morning.json", "zz-map-surface-2.json", "zz-map-under-1.json", "yy-001-morning.json"}
        assert "yy/state/images.md is missing" in why["yy-001-morning.json"] and "does not approve it" in why["zz-map-under-1.json"]
        # a line that names the request's id covers it; a morning line that names no year covers no play-year
        # morning (build 8, run 07 change list 14), and the line naming Year 2 covers the Year 2 morning
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "a") as f:
            f.write("- zz-map-surface-2: approved by Michael, one repaint\n- morning paintings in play: approved\n")
        assert sorted(r["id"] for _p, r, _t in paint.pending(d)) == ["zz-001-morning", "zz-map-clouds",
                                                                     "zz-map-surface", "zz-map-surface-2"]
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "a") as f:
            f.write("- Year 2 morning painting: approved\n")
        assert sorted(r["id"] for _p, r, _t in paint.pending(d)) == ["zz-001-morning", "zz-002-morning", "zz-map-clouds",
                                                                     "zz-map-surface", "zz-map-surface-2"]
        assert paint.campaign_of({"id": "x", "campaign": "zz"}, d) == "zz"
    finally:
        shutil.rmtree(d)
    wf = open(os.path.join(ROOT, ".github", "workflows", "paint.yml")).read()
    assert "python3 tools/paint.py --check" in wf and wf.index("--check") < wf.index("- run: python3 tools/paint.py --paint\n")


# ---------------------------------------------------------------- build 4: map.py (items 58, 60, 67, 74, 81, 86, 87, 93)

def test_site_type_placeholders_and_common_words():
    w = small_world()
    w["features"].append({"id": "f05", "name": "unnamed town", "type": "town", "shape": "point", "coords": [[25, 60]], "regions": ["r01"]})
    w["features"].append({"id": "f06", "name": "The Old Stone", "type": "site", "shape": "point", "coords": [[26, 61]], "regions": ["r01"]})
    w["features"].append({"id": "f07", "name": "The Hollow", "type": "site", "shape": "area",
                          "coords": [[10, 10], [12, 10], [12, 12]], "regions": ["r01"]})
    assert mapt.check_world(w) == []
    bad = json.loads(json.dumps(w))
    bad["features"][-1]["shape"] = "line"
    assert any("a site is a point or an area" in p for p in mapt.check_world(bad))
    warns = mapt.common_word_warnings(w)
    assert len(warns) == 1 and "f07" in warns[0] and "common word" in warns[0]
    assert mapt.is_placeholder("unnamed town") and mapt.is_placeholder("the Nameless ford") and not mapt.is_placeholder("Oskby")
    d = tempfile.mkdtemp()
    try:
        S = os.path.join(d, "S")
        os.makedirs(S)
        with open(os.path.join(S, "notes.md"), "w") as f:
            f.write("## Oskby and the Osk Water\n\n**S1. The Oskby Bell**\n\nThe unnamed town lies by Oskby. The Old Stone stands.\n")
        changed, total, per = mapt.stamp("t", S, w)
        t = open(os.path.join(S, "notes.md")).read()
        assert t.startswith("## Oskby and the Osk Water\n\n**S1. The Oskby Bell**\n\n"), t  # headings and titles untouched
        assert "The unnamed town [f05] lies by Oskby [f01]. The Old Stone [f06] stands." in t
        assert mapt.stamp("t", S, w)[1] == 0
        # a placeholder two places share is not stamped, and the tool says so
        w2 = json.loads(json.dumps(w))
        w2["features"].append({"id": "f08", "name": "unnamed town", "type": "town", "shape": "point", "coords": [[70, 70]], "regions": ["r03"]})
        with open(os.path.join(S, "more.md"), "w") as f:
            f.write("Another unnamed town.\n")
        mapt.stamp("t", S, w2)
        assert open(os.path.join(S, "more.md")).read() == "Another unnamed town.\n"
        assert any("placeholder 'unnamed town' names f05, f08" in n for n in mapt.STAMP_NOTES)
        wp = os.path.join(d, "map.json")
        json.dump(w, open(wp, "w"))
        code, out, _ = run_quiet(mapt.main, ["validate", "t", "--world", wp, "--knowledge", os.path.join(d, "none.json")])
        assert "f07 is named 'The Hollow', a common word" in out and "2 warning(s)" in out
        assert "traced land runs off the sheet's north, south, west, east edge(s)" in out
    finally:
        shutil.rmtree(d)


def test_describe_across_borders_yards_and_json():
    w = small_world()
    w["features"].append({"id": "f05", "name": "Shoulderby", "type": "town", "shape": "point", "coords": [[45, 50]], "regions": ["r02"]})
    w["features"].append({"id": "f06", "name": "Old Cairn", "type": "ruin", "shape": "point", "coords": [[30, 50.05]], "regions": ["r01"]})
    at = (30, 50)   # on Farstead (f04)
    t = mapt.describe(w, "r01", at, None, reference=False)
    # a town 30 miles off across the border shows as smoke, the same as one inside the region (item 58)
    assert "- a town, about 30 miles east: its smoke, walls or lights only" in t
    # no bearing at zero distance; yards under 0.2 miles (item 74)
    assert "- a village (village), at the point itself." in t
    assert "- a ruin (ruin), 180 yards south." in t
    assert mapt.fmt_miles(0.19) == "330 yards" and mapt.fmt_miles(0.2) == "about a quarter mile"
    # past the forty-mile skyline no smoke shows, inside the region or out
    w["features"][-2]["coords"] = [[55, 50]]
    assert "a town, about 50 miles" not in mapt.describe(w, "r01", at, None, reference=False)
    data = {}
    mapt.describe(w, "r01", at, None, reference=True, data=data)
    assert data["cell"] == "B3" and data["region"]["id"] == "r01"
    v = {e["id"]: e for e in data["in_view"]}
    assert v["f04"]["miles"] == 0 and v["f04"]["bearing"] is None and v["f06"]["bearing"] == "south"
    assert data["neighbors"][0]["id"] == "r02" and data["neighbors"][0]["edge_days_on_foot"] > 0
    d = tempfile.mkdtemp()
    try:
        wp = os.path.join(d, "map.json")
        json.dump(w, open(wp, "w"))
        code, out, err = run_quiet(mapt.main, ["describe", "t", "--world", wp, "--landing", "player", "--json"])
        j = json.loads(out)
        assert code == 0 and j["label"] == "Landing of player" and "neighbors" not in j and "coords" not in out
        code, out, _ = run_quiet(mapt.main, ["describe", "t", "--world", wp, "--region", "r02", "--json"])
        assert json.loads(out)["neighbors"]
    finally:
        shutil.rmtree(d)


def test_region_label_only_when_named():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        world = json.load(open(world_p))
        painting = mapt.Painting(world)

        def labels():
            regions_k, _f = mapt.gather(world, json.load(open(know_p)), painting)
            lab = mapt.Labeler((1200, 1000))
            mapt.draw_region_labels(lab, mapt.View((0, 0, 1000, 800)), list(regions_k.values()), painting)
            return [g["lines"][0][0] for g in lab.queue]
        # r01 seen at the landing with no name heard: no label; r02 reported with a told name: labeled
        assert labels() == ["the Reach"]
        assert reveal(repo, "--region", "r01", "--grade", "seen", "--source", "a shepherd named it", "--year", "1", "--named")[0] == 0
        assert json.load(open(know_p))["regions"]["r01"]["named"] is True
        assert labels() == ["The Wend Downs", "the Reach"]
        # a told name stays heard when the ground is seen, as the told name: seeing never gives the
        # Keeper's name (build 5, run 04 item 39)
        assert reveal(repo, "--region", "r02", "--grade", "seen", "--source", "walked", "--year", "2")[0] == 0
        e = json.load(open(know_p))["regions"]["r02"]
        assert "named" not in e and e["told"] == {"name": "the Reach"}
        assert labels() == ["The Wend Downs", "the Reach"]
        assert mapt.knowledge_problems(world, json.load(open(know_p))) == []


def test_draw_if_changed():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        paint = os.path.join(repo, "paint")
        out = os.path.join(repo, "out")
        make_paintings(paint)
        args = ["draw", "fx", "--world", world_p, "--knowledge", know_p, "--paintings", paint, "--out", out, "--layer", "surface"]
        assert run_quiet(mapt.main, args)[0] == 0
        meta = json.load(open(os.path.join(out, "map-meta.json")))
        assert len(meta["input_hash"]) == 64
        png = os.path.join(out, "map.png")
        os.utime(png, (1, 1))
        code, o, _ = run_quiet(mapt.main, args + ["--if-changed"])
        assert code == 0 and "unchanged since the draw of" in o and os.path.getmtime(png) == 1
        # a change to the player's map knowledge redraws
        reveal(repo, "--region", "r01", "--grade", "seen", "--source", "x", "--year", "1", "--named")
        code, o, _ = run_quiet(mapt.main, args + ["--if-changed"])
        assert "wrote" in o and os.path.getmtime(png) != 1
        assert json.load(open(os.path.join(out, "map-meta.json")))["input_hash"] != meta["input_hash"]
        # a different zoom is a different draw
        os.utime(png, (1, 1))
        run_quiet(mapt.main, args + ["--if-changed", "--zoom", "landing"])
        assert os.path.getmtime(png) != 1


def test_continent_size():
    world_p, _ = fx_paths(FIXTURE)
    world = json.load(open(world_p))
    probs, line = mapt.continent_problems(world)
    assert probs == [] and "narrowest about 800 miles" in line and "average about 1,063 miles" in line
    big = json.loads(json.dumps(world))
    big["painting"]["miles_per_pixel"] = 2.0
    probs, _ = mapt.continent_problems(big)
    assert probs == ["continent: average about 2,126 miles across, outside 800 to 1,200"]
    # a long thin land fails at the narrowest; an island apart from the continent is left out
    strip = {"painting": {"size": [1000, 1000], "miles_per_pixel": 1.0},
             "regions": [{"id": "r01", "terrain": "plain", "polygon": [[0, 0], [1000, 0], [1000, 400], [0, 400]]},
                         {"id": "r02", "terrain": "sea", "polygon": [[0, 400], [1000, 400], [1000, 1000], [0, 1000]]},
                         {"id": "r03", "terrain": "island", "polygon": [[450, 800], [500, 800], [500, 850]]}]}
    m = mapt.continent_measure(strip)
    assert m["regions"] == ["r01"] and m["land_left_out"] == ["r03"] and round(m["narrowest"]) == 400
    probs, _ = mapt.continent_problems(strip)
    assert any("narrowest about 400 miles across, under 600" in p for p in probs)
    with tmpcopy() as repo:  # the lock fails on it
        wp, _ = fx_paths(repo)
        json.dump(big, open(wp, "w"))
        code, out, _ = lock(repo, "--places")
        assert code == 1 and "map.json: continent: average about 2,126 miles" in out
        code, out, _ = run_quiet(mapt.main, ["validate", "fx", "--world", wp, "--knowledge", os.path.join(repo, "none.json")])
        assert code == 1 and "continent: 3 land region(s)" in out


def travel_world():
    """A 200 by 100 sheet at 1 mile a pixel: plain to the west (x < 100), forest to the east, with a
    road that bends north through both and a river running east from source to mouth."""
    return {"campaign": "t", "painting": {"size": [200, 100], "miles_per_pixel": 1.0, "grid": {"cols": 5, "rows": 4}},
            "regions": [{"id": "r01", "name": "West Plain", "terrain": "plain", "elevation": "low", "water": "x", "climate": "x",
                         "neighbors": [], "polygon": [[0, 0], [100, 0], [100, 100], [0, 100]]},
                        {"id": "r02", "name": "East Wood", "terrain": "forest", "elevation": "low", "water": "x", "climate": "x",
                         "neighbors": [], "polygon": [[100, 0], [200, 0], [200, 100], [100, 100]]}],
            "features": [{"id": "f01", "name": "Westby", "type": "town", "shape": "point", "coords": [[20, 50]], "regions": ["r01"]},
                         {"id": "f02", "name": "Eastby", "type": "town", "shape": "point", "coords": [[180, 50]], "regions": ["r02"]},
                         {"id": "f03", "name": "The Bent Road", "type": "road", "shape": "line",
                          "coords": [[20, 50.2], [100, 10], [180, 50]], "regions": ["r01", "r02"]},
                         {"id": "f04", "name": "The Long Water", "type": "river", "shape": "line",
                          "coords": [[20, 70], [180, 70]], "regions": ["r01", "r02"]}],
            "landings": {"player": {"region": "r01", "at": [20, 50]}}}


def test_travel_by_route_and_means():
    w = travel_world()
    namer = mapt.Namer(w, None, True)
    # open ground: 80 miles of plain at the rough rate, 80 of forest at the forest rate
    text, data = mapt.travel(w, "f01", "f02", "foot", (), namer, show_ids=True)
    segs = data["segments"]
    assert [(s["region"], s["ground"], round(s["miles"])) for s in segs] == [("r01", "rough", 80), ("r02", "forest", 80)]
    assert abs(data["days"] - (80 / 14 + 80 / 10)) < 0.01 and "over open ground (no route chosen)" in text
    assert "The Bent Road [f03] (--via f03)" in text   # both ends lie on it
    # by the road: longer, but at the road rate the whole way
    text, data = mapt.travel(w, "f01", "f02", "foot", ("f03",), namer, show_ids=True)
    assert [s["how"] for s in data["segments"]] == ["route"] and data["segments"][0]["ground"] == "road"
    assert abs(data["miles"] - 2 * math.dist((20, 50.2), (100, 10))) < 0.6 and abs(data["days"] - data["miles"] / 20) < 0.01
    assert "1. along The Bent Road [f03] (road), toward its last point (:end), at Eastby [f02], in East Wood [r02] (E3), road:" in text
    # a wagon has no passage through the wood off the road, and goes by the road
    assert mapt.travel(w, "f01", "f02", "wagon", (), namer)[1]["days"] is None
    assert mapt.travel(w, "f01", "f02", "wagon", ("f03",), namer)[1]["days"] > 0
    # by boat: downstream east, upstream west; joining the river from a town is no passage by boat
    _, down = mapt.travel(w, "f01", "f02", "boat", ("f04",), namer)
    assert down["days"] is None and [s["how"] for s in down["segments"]] == ["open", "route", "open"]
    assert down["segments"][1]["ground"] == "river_down" and down["segments"][1]["miles"] == 160
    w["features"][0]["coords"] = [[20, 70.3]]   # Westby on the bank, within half a mile
    w["features"][1]["coords"] = [[180, 69.8]]
    _, down = mapt.travel(w, "f01", "f02", "boat", ("f04",), namer)
    _, up = mapt.travel(w, "f02", "f01", "boat", ("f04",), namer)
    assert [s["ground"] for s in down["segments"]] == ["river_down"] and [s["ground"] for s in up["segments"]] == ["river_up"]
    assert abs(down["days"] - 160 / 30) < 0.01 and abs(up["days"] - 160 / 12) < 0.01
    # walking the bank is priced by the ground
    _, bank = mapt.travel(w, "f01", "f02", "foot", ("f04",), namer)
    assert [s["ground"] for s in bank["segments"]] == ["rough", "forest"]
    # names as the god knows them: unknown ground is put plainly
    text, _ = mapt.travel(w, "player", "f02", "foot", (), mapt.Namer(w, {"regions": {}, "features": {}}))
    assert "West Plain" not in text and "a plain country" in text and "[r01]" not in text
    # the rates come from time-and-pace.md, with tools/pace.py for any rate it does not give
    d = tempfile.mkdtemp()
    try:
        md = os.path.join(d, "pace.md")
        with open(md, "w") as f:
            f.write("```\nWalk:   road 22, rough 14, path 16, forest 10\nWagon:  road 11, rough 6; no passage elsewhere\n"
                    "Boat:   downstream 31, upstream 12, coastal sail 50, swim 2\n```\n")
        r = mapt.pace_rates(md)
        assert r["walk"]["road"] == 22 and r["walk"]["path"] == 16 and r["walk"]["mountain"] == 8
        assert r["oxcart"]["road"] == 11 and "forest" not in r["oxcart"] and r["boat"] == {"river_down": 31, "river_up": 12, "sea": 50}
    finally:
        shutil.rmtree(d)
    live = mapt.pace_rates()
    assert live["walk"]["road"] == 20 and live["ride"]["rough"] == 20 and live["boat"]["sea"] == 50
    # the command line
    d = tempfile.mkdtemp()
    try:
        wp = os.path.join(d, "map.json")
        json.dump(travel_world(), open(wp, "w"))
        code, out, err = run_quiet(mapt.main, ["travel", "t", "f01", "f02", "--by", "horse", "--via", "f03", "--world", wp,
                                               "--names", "--json"])
        j = json.loads(out)
        assert code == 0 and j["by"] == "horse" and j["segments"][0]["rate"] == 30, err
        assert run_quiet(mapt.main, ["travel", "t", "f01", "f03", "--by", "foot", "--world", wp])[0] != 0  # a line is a route, not a place
    finally:
        shutil.rmtree(d)


def test_gazetteer_travel_by_route():
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        out = os.path.join(repo, "out")
        reveal(repo, "--feature", "f04", "--grade", "seen", "--source", "walked", "--year", "2")
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        assert "## Travel by route" in g
        assert ("- **Tallowford** to **Mewsby** along **The Chalk Way** (road): 425 miles; either way, 21.2 days on foot, "
                "14.2 days on horse, 42.5 days by wagon (seen).") in g
        # each line's ends are named by their places (build 8, run 07 change list 25)
        assert "from its first point, at Tallowford (B2), to its last point, at Mewsby (D2)" in g


def test_path_type():
    w = travel_world()
    w["features"].append({"id": "f05", "name": "The Deer Path", "type": "path", "shape": "line",
                          "coords": [[20, 50], [180, 50]], "regions": ["r01", "r02"]})
    assert mapt.check_world(w) == []
    bad = json.loads(json.dumps(w))
    bad["features"][-1]["shape"] = "point"
    assert any("a path is a line of two or more points" in p for p in mapt.check_world(bad))
    # a path takes the rough-ground row (time-and-pace.md's Route: line), whatever it crosses
    _, data = mapt.travel(w, "f01", "f02", "foot", ("f05",), mapt.Namer(w, None, True))
    assert [s["ground"] for s in data["segments"]] == ["rough"] and abs(data["days"] - 160 / 14) < 0.01
    assert mapt.pace_rates()["route"] == {"road": "road", "path": "rough"}


# ---------------------------------------------------------------- build 4 fixes (build-check.md)

def test_seen_region_unnamed_shows_id_and_terrain():
    """Must-fix 1: a seen region's name is printed only with "named": true; otherwise its id and terrain."""
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        world = json.load(open(world_p))
        out = os.path.join(repo, "out")
        k = json.load(open(know_p))
        assert "named" not in k["regions"]["r01"]
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        assert "Wend Downs" not in g and "**r01, a hill country** (" in g and ", in r01, a hill country," in g
        t = mapt.describe(world, "r01", mapt.landing_point(world["landings"]["player"]), k, reference=False)
        assert "Wend Downs" not in t and "r01, a hill country" in t
        text, data = mapt.travel(world, "f01", "f04", "foot", ("f03",), mapt.Namer(world, k))
        assert "Wend Downs" not in text and "Saltmarsh" not in text
        # a told name is the god's (r02 reported as the Reach); a region never graded stays plain, with no id
        nm = mapt.Namer(world, k)
        assert nm.name("r02") == "the Reach" and nm.name("r03") == "a highland country"
        # once the name is heard, it is printed
        assert reveal(repo, "--region", "r01", "--grade", "seen", "--source", "a shepherd", "--year", "1", "--named")[0] == 0
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        assert "**The Wend Downs** (" in g and "r01, a hill country" not in g
        assert mapt.Namer(world, json.load(open(know_p))).name("r01") == "The Wend Downs"


def test_gazetteer_region_travel_priced_not_hand_days():
    """Should-fix 13: days between seen neighbors come from travel over open ground, not the hand-set days."""
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        world = json.load(open(world_p))
        k = json.load(open(know_p))
        k["regions"]["r03"] = {"grade": "seen", "source": "walked", "year": 2}
        json.dump(k, open(know_p, "w"))
        out = os.path.join(repo, "out")
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        a = tuple(mapt.centroid(world["regions"][0]["polygon"]))
        b = tuple(mapt.centroid(world["regions"][2]["polygon"]))
        days = mapt.price_trip(world, mapt.plan_trip(world, a, b, [], mapt.Painting(world)), "foot")["days"]
        assert f"{mapt.fmt_days(days)} on foot over open ground (seen)" in g and ": 8 days" not in g


def test_aliases_schema_stamp_gazetteer_places():
    """Should-fix 9: aliases are checked by validate, printed by the gazetteer when the god has them,
    stamped with the place's id, and known to lockcheck --places."""
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        world = json.load(open(world_p))
        assert mapt.check_world(world) == []
        bad = json.loads(json.dumps(world))
        bad["features"][0]["aliases"] = "Tallowmouth"
        assert "f01: aliases must be a list" in mapt.check_world(bad)
        bad["features"][0]["aliases"] = [{"name": "Tallowmouth"}, "x", {"name": "Tallowford", "by": "player", "since": 2}]
        probs = mapt.check_world(bad)
        assert "f01: alias 1 has no by (who uses it)" in probs and "f01: alias 1 has no since (a year or a date)" in probs
        assert "f01: alias 2 is not an entry with name, by and since" in probs and "f01: alias 3 is the map name itself" in probs
        world["features"][0]["aliases"] = [{"name": "Tallowmouth", "by": "player", "since": 2},
                                           {"name": "Greyford", "by": "god-tide", "since": 1}]
        assert mapt.check_world(world) == []
        json.dump(world, open(world_p, "w"))
        out = os.path.join(repo, "out")
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out])
        g = open(os.path.join(out, "gazetteer.md")).read()
        assert "**Tallowford** (town), also called Tallowmouth," in g and "Greyford" not in g
        # build 5, run 04 item 38: aliases are never stamped, and lockcheck --places does not ask for their ids
        names = mapt.stamp_names(world)
        assert "Tallowmouth" not in names and "Greyford" not in names and names["Tallowford"] == ["f01"]
        S = os.path.dirname(world_p)
        append(repo, "SPOILERS_do_not_open/campaigns/fx/alias-notes.md", "They call it Tallowmouth now.\n")
        code, o, err = lock(repo, "--places")
        assert "Tallowmouth" not in o + err
        mapt.stamp("fx", S, world)
        assert open(os.path.join(S, "alias-notes.md")).read() == "They call it Tallowmouth now.\n"


def test_paint_player_asked_and_counts():
    """Must-fix 2 and should-fix 10: the play lines creation-nights.md prescribes cover the real ids,
    one year morning per played year and up to two player-asked paintings a day."""
    import paint
    d = tempfile.mkdtemp()
    try:
        ids = ["zz-001-morning", "zz-002-morning", "zz-002-request-1", "zz-002-request-2", "zz-002-request-3",
               "zz-003-request-1"]
        for rid in ids:
            path = os.path.join(d, "images", "requests", rid + ".json")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            json.dump({"id": rid, "prompt": "x"}, open(path, "w"))
        os.makedirs(os.path.join(d, "campaigns", "zz", "state"))
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("# Images approved (zz)\n\n- first morning painting: approved\n"
                    "- year morning painting: approved, one per played year\n"
                    "- player-asked painting: approved, up to two a day\n")
        skipped = []
        todo = sorted(r["id"] for _p, r, _t in paint.pending(d, skipped))
        assert todo == ["zz-001-morning", "zz-002-morning", "zz-002-request-1", "zz-002-request-2", "zz-003-request-1"]
        why = {os.path.basename(p): w for p, w in skipped}
        assert list(why) == ["zz-002-request-3.json"] and "over the count" in why["zz-002-request-3.json"]
        # a painting already made counts toward its day
        os.makedirs(os.path.join(d, "images", "out"))
        open(os.path.join(d, "images", "out", "zz-003-request-0.png"), "wb").close()
        open(os.path.join(d, "images", "out", "zz-003-request-00.png"), "wb").close()
        assert not paint.covered({"id": "zz-003-request-1"}, d)[0]
        # without the play lines, a player-asked painting is not covered
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("- first morning painting: approved\n")
        assert not paint.covered({"id": "zz-002-request-1"}, d)[0] and not paint.covered({"id": "zz-002-morning"}, d)[0]
        assert paint.line_limit("approved, one per played year") == 1 and paint.line_limit("approved, up to two a day") == 2
        assert paint.line_limit("approved") is None
    finally:
        shutil.rmtree(d)


def test_lockcheck_unnamed_seen_region_is_sealed():
    """A seen region with no `"named": true` and no told name keeps its true name sealed in public files."""
    pub = "campaigns/fx/player/notes.md"
    with tmpcopy() as repo:  # r01 is seen at the landing, its name never heard
        append(repo, pub, "The god rested on the Wend Downs.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'unnamed seen region "Wend Downs"' in out, out
    with tmpcopy() as repo:  # on the Keeper's sealed term list too, it is no longer let through as known
        append(repo, "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt", "The Wend Downs\n")
        append(repo, pub, "The Wend Downs.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'sealed term "The Wend Downs"' in out, out
    with tmpcopy() as repo:  # once named, the name may appear
        _, know_p = fx_paths(repo)
        k = json.load(open(know_p))
        k["regions"]["r01"]["named"] = True
        json.dump(k, open(know_p, "w"))
        append(repo, pub, "The god rested on the Wend Downs.\n")
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # the reported region with a told name (r02) is unchanged
        append(repo, pub, "The Reach lies east.\n")
        assert lock(repo, "--leaks")[0] == 0


def test_lockcheck_name_said_openly_by_player_is_not_sealed():
    """A sealed term the player said in the open table talk (a "## Player:" section of a transcript)
    is the player's own word, and its public use is no leak (Michael, 2026-11-22)."""
    pub = "campaigns/fx/player/notes.md"
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt", "Hollin Marsh\n")
        append(repo, pub, "Hollin Marsh keeps nine skeps.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'sealed term "Hollin Marsh"' in out, out
        append(repo, "campaigns/fx/player/transcript-day3.md",
               "## DM:\n\nWho is he?\n\n## Player:\n\nHollin Marsh, about sixty.\n")
        assert lock(repo, "--leaks")[0] == 0
    with tmpcopy() as repo:  # said only by the DM, it stays sealed
        append(repo, "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt", "Hollin Marsh\n")
        append(repo, pub, "Hollin Marsh keeps nine skeps.\n")
        append(repo, "campaigns/fx/player/transcript-day3.md", "## DM:\n\nHollin Marsh waits.\n")
        assert lock(repo, "--leaks")[0] == 1


def test_lockcheck_kept_term_never_exempted():
    """Decision 8: a "!" term (the sealed factors' names) is never let through as the player's open
    word, a known map name, a people's knowledge name or an allowed phrase."""
    sealed = "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt"
    pub = "campaigns/fx/player/notes.md"
    with tmpcopy() as repo:
        append(repo, sealed, "!kettle\n!Kettle\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, pub, "A kettle sang.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'kept sealed term "kettle"' in out, out
        # said by the player in the open table talk: still sealed outside the transcript
        append(repo, "campaigns/fx/player/transcript-day2.md", "## Player:\n\nMy kettle, I think.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "notes.md" in out and "transcript-day2.md" not in out, out
        # an allowed phrase does not exempt it
        append(repo, "SPOILERS_do_not_open/campaigns/fx/leak-allow.txt", "kettle  # test, 2026-11-22\n")
        assert lock(repo, "--leaks")[0] == 1
    with tmpcopy() as repo:  # a people's knowledge file is no exemption either
        append(repo, sealed, "!Kettle\n")
        append(repo, "campaigns/fx/civs/fxpeople/knowledge.md", "The Kettle is a hill to the east.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'kept sealed term "Kettle"' in out, out
    with tmpcopy() as repo:  # an ordinary "!" term line is a term; the "!" is no part of it
        append(repo, sealed, "!Hollin Marsh\n")
        append(repo, pub, "Hollin Marsh keeps nine skeps.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'kept sealed term "Hollin Marsh"' in out and '"!Hollin' not in out, out


def test_lockcheck_kept_term_not_scanned_in_transcripts():
    """Must-fix 10: the creation transcripts are the player's own words kept verbatim, and are not
    scanned for a kept term; every other public file is, the DM's copies of the player included."""
    sealed = "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt"
    with tmpcopy() as repo:
        append(repo, sealed, "!kettle\n")
        append(repo, "campaigns/fx/player/transcript-day1.md", "## Player:\n\nA kettle, and the kettle again.\n"
                                                              "## DM:\n\nNoted.\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, "campaigns/fx/player/survey-day1.md", "Remark: a kettle.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "survey-day1.md" in out and "transcript-day1.md" not in out, out
    with tmpcopy() as repo:  # an ordinary sealed term is still scanned in the transcripts
        append(repo, sealed, "Hollin Marsh\n")
        append(repo, "campaigns/fx/player/transcript-day1.md", "## DM:\n\nHollin Marsh waits.\n")
        assert lock(repo, "--leaks")[0] == 1


def test_validate_warns_land_off_the_sheet():
    """map.py validate warns when traced land touches the painting border, naming the edges."""
    inside = {"painting": {"size": [1000, 1000], "miles_per_pixel": 1.0},
              "regions": [{"id": "r01", "terrain": "sea", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
                          {"id": "r02", "terrain": "plain", "polygon": [[100, 100], [900, 100], [900, 900], [100, 900]]}]}
    assert mapt.edge_land_warnings(inside) == []
    off = json.loads(json.dumps(inside))
    off["regions"].append({"id": "r03", "terrain": "forest", "polygon": [[900, 0], [1000, 0], [1000, 300], [900, 300]]})
    off["regions"].append({"id": "r04", "terrain": "hill", "polygon": [[300, 900], [500, 900], [400, 1000]]})
    w = mapt.edge_land_warnings(off)
    assert len(w) == 1 and "north, south, east edge(s)" in w[0] and "west" not in w[0]
    assert "north: r03" in w[0] and "south: r04" in w[0] and "east: r03" in w[0] and "r01" not in w[0]
    with tmpcopy() as repo:
        wp, _ = fx_paths(repo)
        code, out, _ = run_quiet(mapt.main, ["validate", "fx", "--world", wp, "--knowledge", os.path.join(repo, "none.json")])
        assert code == 0 and "traced land runs off the sheet's north, south, west, east edge(s)" in out
        assert "north: r01, r02" in out and "1 warning(s)" in out


# ---------------------------------------------------------------- build 5 (run 04 change list)

def test_lockcheck_dashes_without_sealed_folder():
    """Item 2: --dashes alone runs on the public folder when no sealed folder exists yet (Day 1)."""
    with tmpcopy() as repo:
        shutil.rmtree(os.path.join(repo, "SPOILERS_do_not_open", "campaigns", "fx"))
        code, out, _ = lock(repo, "--dashes")
        assert code == 0 and "reads the public folder alone" in out and "dashes: 0 failure(s)" in out
        append(repo, "campaigns/fx/player/transcript-day1.md", "A pause \u2014 then rain.\n")
        code, out, _ = lock(repo, "--dashes")
        assert code == 1 and "transcript-day1.md:1: 1 em or en dash(es)" in out
        # every other check still needs the sealed folder
        assert lock(repo, "--leaks")[0] != 0 and lock(repo)[0] != 0


def test_lockcheck_people_knowledge_names():
    """Item 46: a map name in campaigns/<name>/civs/<people>/knowledge.md is told to the people: allowed
    there, and no leak; anywhere else it still fails, and a sealed term that is no map name fails there too."""
    know = "campaigns/fx/civs/tallowfolk/knowledge.md"
    with tmpcopy() as repo:
        append(repo, know, "# What the Tallowfolk know\n\nBeyond the downs lies Hollow Moor (A3), and the ruin of Brackwater Hold (B4).\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0, out
        append(repo, "campaigns/fx/player/notes.md", "Hollow Moor lies south.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "notes.md" in out and "knowledge.md" not in out
    with tmpcopy() as repo:   # a god's name is no map name: it fails in the people's file as anywhere
        append(repo, know, "They fear Vessaline.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'knowledge.md:1: sealed term "Vessaline"' in out
    with tmpcopy() as repo:   # only that file: another file in the people's folder is scanned as before
        append(repo, "campaigns/fx/civs/tallowfolk/notes.md", "Hollow Moor.\n")
        assert lock(repo, "--leaks")[0] == 1


def test_stamp_never_stamps_aliases():
    """Item 38: stamp never stamps an alias (often a common word); the gazetteer still prints it."""
    w = small_world()
    w["features"][0]["aliases"] = [{"name": "Ford", "by": "god-x", "since": 1}, {"name": "Oskmouth", "by": "player", "since": 1}]
    assert mapt.check_world(w) == []
    assert set(mapt.stamp_names(w)) == {"Vale of Osk", "The Shoulders", "Shoulders", "The White Teeth", "White Teeth",
                                        "Oskby", "Osk Water", "Hob Hole", "Farstead"}
    d = tempfile.mkdtemp()
    try:
        with open(os.path.join(d, "notes.md"), "w") as f:
            f.write("At the Ford we met. Oskmouth, they call it. Oskby is near.\n")
        mapt.stamp("t", d, w)
        assert open(os.path.join(d, "notes.md")).read() == "At the Ford we met. Oskmouth, they call it. Oskby [f01] is near.\n"
    finally:
        shutil.rmtree(d)


def test_seen_feature_name_told_or_none():
    """Item 39: a seen feature shows its told name or none; a name the player gave at creation counts as
    heard; seeing a told place keeps the told name; lockcheck keeps an unheard map name sealed."""
    w = small_world()
    k = {"regions": {"r01": {"grade": "seen", "source": "the landing", "year": 1}},
         "features": {"f01": {"grade": "seen", "source": "the landing", "year": 1},
                      "f02": {"grade": "seen", "source": "the landing", "year": 1, "told": {"name": "the quick water"}},
                      "f04": {"grade": "reported", "source": "a drover", "year": 1}}}
    assert mapt.knowledge_problems(w, k) == []
    nm = mapt.Namer(w, k)
    assert nm.name("f01") == "a town" and nm.name("f02") == "the quick water" and nm.name("f04") == "Farstead"
    regions_k, features_k = mapt.gather(w, k, mapt.Painting(w))
    assert features_k["f01"][0]["named"] is False and features_k["f01"][0]["name"] == "f01, a town"
    assert regions_k["r01"]["named"] is False
    # a name the player gave at creation is heard: the label stays
    w["regions"][0]["aliases"] = [{"name": "Hearthvale", "by": "player", "since": "creation"}]
    assert mapt.Namer(w, k).name("r01") == "Hearthvale" and mapt.region_name_known(k["regions"]["r01"], w["regions"][0])
    # a seen settlement with no name heard: its mark, no label
    lab = mapt.Labeler((1200, 1000))
    canvas = mapt.Image.new("RGBA", (1200, 1000))
    mapt.draw_feature(canvas, lab, mapt.View((0, 0, 100, 100)), features_k["f01"][0], mapt.Painting(w))
    assert lab.queue == [] and len(lab.obstacles) == 1
    bad = {"regions": {}, "features": {"f01": {"grade": "seen", "source": "x", "year": 1, "told": {"name": "n", "coords": [[1, 1]]}}}}
    assert any("seen entries carry no told but a name heard" in p for p in mapt.knowledge_problems(w, bad))
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        # the ruin (f05) rumored by a name, then seen: the told name is kept, the Keeper's is not given
        assert reveal(repo, "--feature", "f05", "--grade", "rumored", "--source", "a tinker", "--year", "1",
                      "--name", "the drowned hold", "--cell", "B4")[0] == 0
        code, out, _ = reveal(repo, "--feature", "f05", "--grade", "seen", "--source", "walked", "--year", "2")
        e = json.load(open(know_p))["features"]["f05"]
        assert code == 0 and e["told"] == {"name": "the drowned hold"} and "named" not in e
        assert "Brackwater" not in out and "Brackwater" not in open(os.path.join(os.path.dirname(know_p), "map-log.md")).read()
        out_dir = os.path.join(repo, "out")
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out_dir])
        g = open(os.path.join(out_dir, "gazetteer.md")).read()
        assert "**the drowned hold** (ruin)" in g and "Brackwater" not in g
        # the Keeper's name in a public file is a leak until it is heard
        append(repo, "campaigns/fx/player/notes.md", "Brackwater Hold stands empty.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'unheard map name "Brackwater Hold"' in out, out
        assert reveal(repo, "--feature", "f05", "--grade", "seen", "--source", "a fisher named it", "--year", "2", "--named")[0] == 0
        assert lock(repo, "--leaks")[0] == 0


def test_describe_settlement_in_plain_view():
    """Item 40: a settlement in plain view (within two miles) is never missed, even from hill ground with
    a high region between, and no region a border settlement stands in hides it."""
    w = {"campaign": "t", "painting": {"size": [100, 100], "miles_per_pixel": 0.1, "grid": {"cols": 5, "rows": 4}},
         "regions": [
             {"id": "r01", "name": "Lowfold", "terrain": "hill, wooded folds", "elevation": "hill, 500 to 900 feet",
              "water": "x", "climate": "x", "neighbors": [], "polygon": [[0, 0], [40, 0], [40, 100], [0, 100]]},
             {"id": "r02", "name": "The Spur", "terrain": "mountain", "elevation": "high, to 9,000 feet",
              "water": "x", "climate": "x", "neighbors": [], "polygon": [[40, 0], [45, 0], [45, 100], [40, 100]]},
             {"id": "r03", "name": "Farvale", "terrain": "valley", "elevation": "low, 300 to 400 feet",
              "water": "x", "climate": "x", "neighbors": [], "polygon": [[45, 0], [100, 0], [100, 100], [45, 100]]}],
         "features": [
             {"id": "f01", "name": "Nearby", "type": "town", "shape": "point", "coords": [[50, 50]], "regions": ["r03"]},
             {"id": "f02", "name": "Farby", "type": "village", "shape": "point", "coords": [[90, 50]], "regions": ["r03"]},
             {"id": "f03", "name": "Spurfoot", "type": "town", "shape": "area", "coords": [[44, 60], [52, 60], [52, 66], [44, 66]],
              "regions": ["r02", "r03"]}],
         "landings": {"player": {"region": "r01", "at": [35, 50]}}}
    d = {}
    t = mapt.describe(w, "r01", (35, 50), None, reference=False, data=d)
    smoke = {e["id"]: e for e in d["smoke"]}
    assert "f01" in smoke and round(smoke["f01"]["miles"], 1) == 1.5, t   # 1.5 miles, behind the spur: never missed
    assert "f03" in smoke   # an area settlement, on the border with the spur, read at its nearest point
    assert "f02" not in smoke and "f02" not in {e["id"] for e in d["in_view"]}   # 5.5 miles behind the spur: hidden
    assert mapt.PLAIN_VIEW_MILES == 2.0


def lake_world():
    """A 200 by 100 sheet at 1 mile a pixel: plain all round a lake region in the middle (x 60 to 140,
    y 20 to 80), a town each side of it on the shore, and a river from the west shore to the sheet's edge."""
    plain = [[0, 0], [200, 0], [200, 100], [0, 100], [0, 0], [60, 20], [60, 80], [140, 80], [140, 20], [60, 20]]
    return {"campaign": "t", "painting": {"size": [200, 100], "miles_per_pixel": 1.0, "grid": {"cols": 5, "rows": 4}},
            "regions": [{"id": "r01", "name": "Shorefields", "terrain": "plain", "elevation": "low", "water": "x", "climate": "x",
                         "neighbors": [], "polygon": plain},
                        {"id": "r02", "name": "Mere Long", "terrain": "lake, still", "elevation": "low", "water": "x", "climate": "x",
                         "neighbors": [], "polygon": [[60, 20], [140, 20], [140, 80], [60, 80]]}],
            "features": [{"id": "f01", "name": "Westmere", "type": "town", "shape": "point", "coords": [[55, 50]], "regions": ["r01"]},
                         {"id": "f02", "name": "Eastmere", "type": "town", "shape": "point", "coords": [[145, 50]], "regions": ["r01"]},
                         {"id": "f03", "name": "Inland", "type": "village", "shape": "point", "coords": [[30, 50]], "regions": ["r01"]},
                         {"id": "f04", "name": "Mere Run", "type": "river", "shape": "line", "coords": [[60, 30], [0, 30]], "regions": ["r01"]}],
            "landings": {"player": {"region": "r01", "at": [55, 50]}}}


def test_travel_boat_walk_and_around_water():
    """Item 41: a walk routes around water; a boat trip may start or end with a short walk."""
    w = lake_world()
    assert mapt.check_world(w) == [] and mapt.tiling_lines(w)[0] == []
    namer = mapt.Namer(w, None, True)
    text, data = mapt.travel(w, "f01", "f02", "foot", (), namer, show_ids=True)
    assert data["days"] is not None and all(s["ground"] == "rough" for s in data["segments"])
    assert 140 < data["miles"] < 150 and "(around the water)" in text and "around water a walker cannot cross" in text
    # by boat straight over the lake: five miles of shore walk each end, priced on foot
    text, data = mapt.travel(w, "f01", "f02", "boat", (), namer, show_ids=True)
    assert [s["how"] for s in data["segments"]] == ["walk", "open", "walk"] and data["days"] is not None
    assert [s["ground"] for s in data["segments"]] == ["rough", "sea", "rough"]
    assert abs(data["days"] - (5 / 14 + 80 / 50 + 5 / 14)) < 0.01 and "on foot to the water" in text and "14 miles a day on foot" in text
    # down the river from a village 25 miles off it: the walk is too long, so no passage by boat
    assert mapt.travel(w, "f03", "f04:end", "boat", ("f04",), namer)[1]["days"] is None
    w["features"][2]["coords"] = [[30, 36]]   # six miles from the river: walked to it
    _, data = mapt.travel(w, "f03", "f04:end", "boat", ("f04",), namer)
    assert [s["how"] for s in data["segments"]] == ["walk", "route"] and data["segments"][1]["ground"] == "river_down"
    # a boat trip all on land is still no passage
    assert mapt.travel(w, "f03", "f01", "boat", (), namer)[1]["days"] is None
    # a walk that crosses no water is priced straight, as before
    _, straight = mapt.travel(w, "f03", "f01", "foot", (), namer)
    assert not any(s.get("around") for s in mapt.price_trip(w, mapt.plan_trip(w, (30, 36), (55, 50), [], mapt.Painting(w)), "foot")["segments"])
    assert mapt.BOAT_WALK_MILES == 10.0


def test_travel_edges_and_line_ends():
    """Item 50: travel takes a region's edge and a line's ends as endpoints."""
    w = lake_world()
    namer = mapt.Namer(w, None, True)
    text, data = mapt.travel(w, "f03", "r02:edge", "foot", (), namer, show_ids=True)
    assert abs(data["miles"] - 30) < 0.6 and "(its nearest edge)" in text
    text, data = mapt.travel(w, "f04:start", "f04:end", "boat", ("f04",), namer, show_ids=True)
    assert [s["ground"] for s in data["segments"]] == ["river_down"] and abs(data["miles"] - 60) < 0.01
    assert "'s source (:start)" in text and "'s mouth (:end)" in text
    _, up = mapt.travel(w, "f04:mouth", "f04:source", "boat", ("f04",), namer)
    assert [s["ground"] for s in up["segments"]] == ["river_up"]
    # the edge read toward the other end, whichever end it is
    _, back = mapt.travel(w, "r02:edge", "f03", "foot", (), namer)
    assert abs(back["miles"] - 30) < 0.6
    d = tempfile.mkdtemp()
    try:
        wp = os.path.join(d, "map.json")
        json.dump(w, open(wp, "w"))
        assert run_quiet(mapt.main, ["travel", "t", "f03", "r02:edge", "--by", "foot", "--world", wp, "--names"])[0] == 0
        assert run_quiet(mapt.main, ["travel", "t", "f03", "f04", "--by", "foot", "--world", wp])[0] != 0
        try:
            mapt.resolve_place(w, "f04")
            assert False
        except SystemExit as e:
            assert "f04:start" in str(e.code)
        assert run_quiet(mapt.main, ["travel", "t", "f03", "f01:edge", "--by", "foot", "--world", wp])[0] != 0
        assert run_quiet(mapt.main, ["travel", "t", "f03", "r02:middle", "--by", "foot", "--world", wp])[0] != 0
    finally:
        shutil.rmtree(d)


def test_landing_zoom_resolution_and_one_direction():
    """Item 42: the landing frame is never blown up more than LANDING_MAX_UPSCALE times; a rumor beyond
    the sheet carries one direction."""
    w = json.load(open(fx_paths(FIXTURE)[0]))
    painting = mapt.Painting(w)
    tiny = {"r01": {"id": "r01", "grade": "seen", "polygon": [[500, 500], [504, 500], [504, 503]], "name": "x"}}
    r = mapt.landing_rect(tiny, {}, painting)
    need = 1024 / mapt.LANDING_MAX_UPSCALE
    assert abs((r[2] - r[0]) - need) < 1e-6 and abs((r[3] - r[1]) - need) < 1e-6 and r[0] <= 500 and r[2] >= 504
    assert mapt.View(r).scale <= mapt.LANDING_MAX_UPSCALE + 1e-9
    edge = {"r01": {"id": "r01", "grade": "seen", "polygon": [[990, 790], [999, 790], [999, 799]], "name": "x"}}
    r = mapt.landing_rect(edge, {}, painting)
    assert r[2] == 1000 and r[3] == 800 and abs(r[2] - r[0] - need) < 1e-6   # shifted, not cut, at the sheet's edge
    view = mapt.View((0, 0, 200, 200))
    feats = {"f09": ({"id": "f09", "name": "smoke to the north-east", "grade": "rumored", "coords": [[900, 700]]}, None),
             "f08": ({"id": "f08", "name": "a tall tower", "grade": "rumored", "coords": [[900, 100]]}, None)}
    notes = mapt.beyond_notes(view, {}, feats, None)
    assert notes == ["rumored, beyond this sheet: smoke to the north-east; a tall tower, east"]


def test_tiles_and_regions_from_paint():
    """Item 44: a region-from-paint helper whose polygons tile the sheet, and the tiling check; a narrow
    sea's name kept on its water."""
    W, H = 60, 40
    labels = [["r01" if x < 30 else "r02" for x in range(W)] for y in range(H)]
    for y in range(10, 20):
        for x in range(8, 20):
            labels[y][x] = "r03"   # a lake inside r01
    for y in range(30, 40):
        for x in range(25, 45):
            labels[y][x] = None    # unclaimed: given to the nearest region
    labels[0][59] = "r01"          # a stray pixel of r01 inside r02: given to r02
    polys, notes = mapt.regions_from_labels(labels, tol=1.0)
    assert set(polys) == {"r01", "r02", "r03"}
    assert any("unclaimed" in n or "no region claimed" in n for n in notes) and any("r01: a part of 1 pixel" in n for n in notes)
    world = {"painting": {"size": [W, H], "miles_per_pixel": 1.0}, "regions": [{"id": i, "polygon": p} for i, p in polys.items()]}
    rep = mapt.tiling_report(world["regions"], (W, H))
    assert rep["overlaps"] == {} and rep["gaps"][0] == 0.0
    assert mapt.point_in_poly(12, 15, polys["r03"]) and not mapt.point_in_poly(12, 15, polys["r01"]) and mapt.point_in_poly(4, 4, polys["r01"])
    # hand polygons a pixel apart: an overlap and a gap, both found
    hand = [{"id": "r01", "polygon": [[0, 0], [31, 0], [31, 40], [0, 40]]}, {"id": "r02", "polygon": [[30, 0], [60, 0], [60, 40], [30, 40]]},
            {"id": "r03", "polygon": [[0, 40], [60, 40], [60, 39.5]]}]
    rep = mapt.tiling_report(hand[:2], (W, H))
    assert set(rep["overlaps"]) == {("r01", "r02")} and abs(rep["overlaps"][("r01", "r02")][0] - 40) < 0.5
    assert abs(rep["overlaps"][("r01", "r02")][2] - 1) < 0.05
    gap = mapt.tiling_report([{"id": "r01", "polygon": [[0, 0], [29, 0], [29, 40], [0, 40]]}, hand[1]], (W, H))
    assert abs(gap["gaps"][0] - 40) < 0.5
    # the command: tiles fails on a gap; regions-from-paint writes polygons that pass it
    d = tempfile.mkdtemp()
    try:
        from PIL import Image
        im = Image.new("RGB", (W, H), (0, 0, 0))
        px = im.load()
        cols = {"r01": (200, 10, 10), "r02": (10, 200, 10), "r03": (10, 10, 200)}
        for y in range(H):
            for x in range(W):
                if labels[y][x]:
                    px[x, y] = cols[labels[y][x]]
        im.save(os.path.join(d, "labels.png"))
        json.dump({k: "#%02x%02x%02x" % v for k, v in cols.items()}, open(os.path.join(d, "key.json"), "w"))
        wp = os.path.join(d, "map.json")
        base = {"campaign": "t", "painting": {"size": [W, H], "miles_per_pixel": 1.0},
                "regions": [{"id": "r01", "name": "A", "terrain": "plain", "elevation": "low", "water": "x", "climate": "x",
                             "neighbors": [], "polygon": hand[0]["polygon"]},
                            {"id": "r02", "name": "B", "terrain": "plain", "elevation": "low", "water": "x", "climate": "x",
                             "neighbors": [], "polygon": [[32, 0], [60, 0], [60, 40], [32, 40]]},
                            {"id": "r03", "name": "C", "terrain": "lake", "elevation": "low", "water": "x", "climate": "x",
                             "neighbors": [], "polygon": [[8, 10], [20, 10], [20, 20], [8, 20]]}], "features": []}
        json.dump(base, open(wp, "w"))
        code, out, _ = run_quiet(mapt.main, ["tiles", "t", "--world", wp])
        assert code == 1 and "regions r01 and r03 overlap" in out and "in no region" in out
        code, out, _ = run_quiet(mapt.main, ["regions-from-paint", "t", "--world", wp, "--labels", os.path.join(d, "labels.png"),
                                             "--key", os.path.join(d, "key.json"), "--apply"])
        assert code == 0 and "they tile the painting" in out and "applied to 3 region(s)" in out, out
        code, out, _ = run_quiet(mapt.main, ["tiles", "t", "--world", wp])
        assert code == 0 and "they tile the painting" in out
    finally:
        shutil.rmtree(d)
    # a narrow sea: its name sits on its water, not over the coast
    sea = [[100, 100], [700, 100], [700, 140], [100, 140]]
    lab = mapt.Labeler((800, 300), bounds=(0, 0, 800, 300))
    k = {"id": "r09", "grade": "seen", "named": True, "name": "The Narrow Sea", "terrain": "sea", "polygon": sea, "source": "x"}
    mapt.draw_region_labels(lab, mapt.View((0, 0, 800, 240), size_px=800, margins=(0, 0, 0, 0)), [k], mapt.Painting({"painting": {"size": [800, 240]}}))
    assert lab.queue[0]["within"] is not None
    lab.place()
    box = mapt.bbox([(b[0], b[1]) for b in lab.groups[0]] + [(b[2], b[3]) for b in lab.groups[0]])
    assert 100 <= box[0] and box[2] <= 700 and 100 <= box[1] and box[3] <= 140, box


def test_validate_fails_overlapping_regions():
    """Item 53: validate fails on overlapping regions and on a landing point inside two regions."""
    w = small_world()
    assert mapt.tiling_lines(w) == ([], [])
    w["regions"][1]["polygon"] = [[39, 0], [60, 0], [60, 100], [39, 100]]   # a pixel over the valley
    w["landings"]["player"]["at"] = [39.5, 50]
    probs, _ = mapt.tiling_lines(w)
    assert any(p.startswith("regions r01 and r02 overlap, about 400.0 square miles") and "about 2.0 miles thick" in p for p in probs), probs
    assert any("landing player: its point lies inside 2 regions (r01, r02)" in p for p in probs)
    d = tempfile.mkdtemp()
    try:
        wp = os.path.join(d, "map.json")
        json.dump(w, open(wp, "w"))
        code, out, _ = run_quiet(mapt.main, ["validate", "t", "--world", wp, "--knowledge", os.path.join(d, "none.json")])
        assert code == 1 and "overlap" in out
        w["regions"][1]["polygon"] = [[41, 0], [60, 0], [60, 100], [41, 100]]   # a gap warns in validate, fails in tiles
        w["landings"]["player"]["at"] = [20.2, 50.1]
        json.dump(w, open(wp, "w"))
        code, out, _ = run_quiet(mapt.main, ["validate", "t", "--world", wp, "--knowledge", os.path.join(d, "none.json")])
        assert "warning: the regions leave about 400.0 square miles" in out and "overlap" not in out
        assert run_quiet(mapt.main, ["tiles", "t", "--world", wp])[0] == 1
    finally:
        shutil.rmtree(d)
    # the fixture tiles
    assert mapt.tiling_lines(json.load(open(fx_paths(FIXTURE)[0]))) == ([], [])


def test_draw_god_mark_ticks_and_cropped_labels():
    """Item 60: on the landing sheet the god's mark is drawn, far sightings are ticks from it (named once
    in the footer, never as rumors beyond the sheet), and a cropped region is labeled on its visible part."""
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        paint = os.path.join(repo, "paint")
        out = os.path.join(repo, "out")
        make_paintings(paint)
        w = json.load(open(world_p))
        w["landings"]["player"] = {"region": "r01", "at": [200, 200]}
        json.dump(w, open(world_p, "w"))
        k = json.load(open(know_p))
        k["features"]["f05"] = {"grade": "rumored", "source": "own sight at the landing", "year": 1,
                                "told": {"name": "smoke to the south", "cell": "B4"}}
        k["features"]["f04"] = {"grade": "rumored", "source": "a carter", "year": 1,
                                "told": {"name": "a smoke far east", "cell": "E1", "bearing": "east"}}
        json.dump(k, open(know_p, "w"))
        assert mapt.knowledge_problems(w, k) == []
        painting = mapt.Painting(w)
        regions_k, features_k = mapt.gather(w, k, painting)
        assert mapt.sighting_bearing(features_k["f05"][0]) == "south" and mapt.sighting_bearing(features_k["f04"][0]) == "east"
        assert mapt.sighting_bearing(features_k["f06"][0]) is None   # a drover's rumor is no sighting
        code, o, err = run_quiet(mapt.main, ["draw", "fx", "--world", world_p, "--knowledge", know_p, "--paintings", paint,
                                             "--out", out, "--zoom", "landing", "--layer", "surface"])
        assert code == 0, err
        rect = mapt.landing_rect(regions_k, features_k, painting)
        view, notes = mapt.make_view(rect, ["x"] + mapt.sighting_note([features_k["f05"][0], features_k["f04"][0]]))
        assert "each tick points to what it saw far off: a smoke far east; smoke to the south." in " ".join(notes)
        # the full sheet has no mark, and the sightings are rumors as before
        lab = mapt.Labeler((1200, 1000))
        canvas = mapt.Image.new("RGBA", (1200, 1000))
        mapt.draw_god_mark(canvas, lab, (100, 100), ["south", "east", "east"])
        assert len(lab.obstacles) == 3   # two ticks and the mark
        # a bad bearing is a knowledge problem
        k["features"]["f04"]["told"]["bearing"] = "upward"
        assert any("told.bearing" in p for p in mapt.knowledge_problems(w, k))
    # a region cut by the crop: its label on the part in view, with that part's cell
    w = json.load(open(fx_paths(FIXTURE)[0]))
    painting = mapt.Painting(w)
    k = {"regions": {"r02": {"grade": "seen", "source": "x", "year": 1, "named": True}}, "features": {}}
    regions_k, _f = mapt.gather(w, k, painting)
    view = mapt.View((0, 0, 500, 500))
    lab = mapt.Labeler((1200, 1000))
    mapt.draw_region_labels(lab, view, list(regions_k.values()), painting)
    g = lab.queue[0]
    x = (g["xy"][0] - view.ml) / view.scale
    assert 400 < x < 500 and g["lines"][1][0] == "(C1)"   # r02 runs 400 to 1000; only 400 to 500 is in view


def test_validate_underground_and_layers():
    """Item 68: validate fails a world whose placement plan or history gives an underground that map.json
    lacks; layers carry id under-N, a depth and uNN features; a layer with no painting yet is not drawn."""
    d = tempfile.mkdtemp()
    try:
        S = os.path.join(d, "S")
        os.makedirs(os.path.join(S, "world"))
        w = small_world()
        wp = os.path.join(S, "map.json")
        json.dump(w, open(wp, "w"))

        def validate():
            return run_quiet(mapt.main, ["validate", "t", "--world", wp, "--knowledge", os.path.join(d, "none.json")])
        with open(os.path.join(S, "world-draft.md"), "w") as f:
            f.write("# World draft\n\nUnderground: none; the world has no underground.\n")
        with open(os.path.join(S, "deep-history.md"), "w") as f:
            f.write("The old ones dug nothing. There is no underground.\n")
        assert "underground" not in validate()[1]
        with open(os.path.join(S, "world", "placement-plan.md"), "w") as f:
            f.write("# Placement plan\n\n## The underground\n\nOne cut gallery under the range.\n")
        code, out, _ = validate()
        assert code == 1 and "underground: world/placement-plan.md:3 give the world an underground, but map.json has no layer" in out
        assert mapt.underground_claims(S) == [("world/placement-plan.md", 3, "## The underground")]
        with open(os.path.join(S, "deep-history.md"), "a") as f:
            f.write("- [x] The world has an underground (1.5)\n")
        assert [c[0] for c in mapt.underground_claims(S)] == ["deep-history.md", "world/placement-plan.md"]
        for line, n in (("The underground: none; the world has no layer.", 0), ("- **Underground:** no", 0),
                        ("The underground: a layer at depth 1, mostly solid rock with one gallery.", 1),
                        ("Underground: yes, one gallery.", 1), ("Nothing lies below.", 0)):
            with open(os.path.join(S, "world-draft.md"), "w") as f:
                f.write(line + "\n")
            assert sum(c[0] == "world-draft.md" for c in mapt.underground_claims(S)) == n, line
        # written into the data as a layer, it passes
        w["layers"] = [{"id": "under-1", "name": "The Cut", "depth": 1,
                        "features": [{"id": "u01", "name": "The Gallery", "type": "cave", "shape": "line",
                                      "coords": [[60, 50], [90, 50]], "regions": ["r03"]}]}]
        json.dump(w, open(wp, "w"))
        code, out, _ = validate()
        assert "underground" not in out and "layer" not in out   # (the small world fails only the continent rule)
        # the converse: a layer when the Night 1 decision line reads none (should-fix 8)
        with open(os.path.join(S, "world-draft.md"), "w") as f:
            f.write("# World draft\n\nUnderground: none\n")
        code, out, _ = validate()
        assert code == 1 and "world-draft.md:3 decide the world has no underground, but map.json has a layer (under-1)" in out, out
        with open(os.path.join(S, "world-draft.md"), "w") as f:
            f.write("# World draft\n\nUnderground: yes, one cut gallery.\n")
        assert "underground" not in validate()[1]
        # the layer's form
        bad = json.loads(json.dumps(w))
        bad["layers"][0]["id"] = "deep"
        bad["layers"][0]["depth"] = 0
        bad["layers"][0]["features"][0]["id"] = "f09"
        bad["layers"].append({"id": "under-2", "depth": 2, "features": [], "painting": ""})
        bad["features"].append({"id": "u05", "name": "Hole", "type": "cave", "shape": "point", "coords": [[5, 5]], "regions": ["r01"]})
        probs = mapt.check_world(bad)
        for want in ("layer deep: id must be under-N", "layer deep: depth must be a whole number", "feature f09 is underground, so its id is uNN",
                     "layer under-2: painting must be a file name", "feature u05: uNN ids are for underground features"):
            assert any(want in p for p in probs), (want, probs)
        # a layer with no painting yet: the surface is drawn, the layer sheet is not
        paint = os.path.join(d, "paint")
        make_paintings(paint, size=(1000, 1000))   # resized to the 100-pixel sheet when drawn
        os.remove(os.path.join(paint, "under-1.png"))
        k = {"regions": {"r01": {"grade": "seen", "source": "x", "year": 1}},
             "features": {"u01": {"grade": "seen", "source": "walked", "year": 1}}}
        kp = os.path.join(d, "k.json")
        json.dump(k, open(kp, "w"))
        code, out, err = run_quiet(mapt.main, ["draw", "t", "--world", wp, "--knowledge", kp, "--paintings", paint, "--out", os.path.join(d, "out")])
        assert code == 0 and "layer under-1 has no painting yet" in out and not os.path.exists(os.path.join(d, "out", "map-under-1.png")), err
        assert os.path.exists(os.path.join(d, "out", "map.png"))
    finally:
        shutil.rmtree(d)


def test_paint_help_and_no_arguments():
    """Item 62: --help prints the usage; with no arguments paint.py only reports, in the workflow too."""
    import paint
    code, out, _ = run_quiet(paint.main, ["--help"])
    assert code == 0 and "--paint" in out and "--check" in out and "painted" not in out.split("Usage")[0]
    real_pending = paint.pending
    paint.pending = lambda skipped=None: [("r.json", {"id": "zz-001-morning", "prompt": "x"}, "out.png")]
    old = os.environ.pop("GITHUB_ACTIONS", None)
    try:
        code, out, _ = run_quiet(paint.main, [])
        assert code == 0 and "would paint r.json" in out and "nothing painted" in out
        assert run_quiet(paint.main, ["--bogus"])[0] == 2
        assert paint.wants_paint(["--paint"], {}) and not paint.wants_paint([], {})
        assert not paint.wants_paint([], {"GITHUB_ACTIONS": "true"}) and not paint.wants_paint(["--check"], {"GITHUB_ACTIONS": "true"})
        os.environ["GITHUB_ACTIONS"] = "true"
        code, out, _ = run_quiet(paint.main, [])
        assert code == 0 and "nothing painted" in out
        del os.environ["GITHUB_ACTIONS"]
    finally:
        paint.pending = real_pending
        if old is not None:
            os.environ["GITHUB_ACTIONS"] = old


def test_stamp_time():
    """Item 10: the stamp helper prints the Pacific clock time in the timing log's format."""
    import datetime
    import stamp_time
    t = datetime.datetime(2026, 11, 23, 5, 39, 30, tzinfo=datetime.timezone.utc)   # 21:39 the day before, Pacific
    assert stamp_time.stamp(now=t) == "2026-11-22 21:39" and stamp_time.stamp("time", t) == "21:39"
    assert stamp_time.stamp("date", t) == "2026-11-22"
    summer = datetime.datetime(2026, 7, 1, 19, 5, tzinfo=datetime.timezone.utc)
    assert stamp_time.stamp(now=summer) == "2026-07-01 12:05"
    code, out, _ = run_quiet(stamp_time.main, [])
    assert code == 0 and len(out.strip()) == 16 and out.strip()[:10] == mapt.pacific_today()
    assert run_quiet(stamp_time.main, ["--soon"])[0] == 2


# ---------------------------------------------------------------- build 6 (run 05 change list)

def test_build6_lockcheck_fractions_are_not_counts():
    """Item 23: a number word before a fraction word, or a numeral fraction, is no count of gods."""
    assert lockcheck.count_hits("The god's reach falls to three quarters of a day's walk.") == []
    assert lockcheck.count_hits("Two thirds of what the god holds.") == []
    assert lockcheck.count_hits("The god keeps 3/4 of the toll.") == []
    assert lockcheck.count_hits("Four fifths of the measure, says the god.") == []
    assert lockcheck.count_hits("Three gods came down.")   # a count still hits
    assert lockcheck.count_hits("Three of us fell, and a quarter of the sky with us.")


def test_build6_lockcheck_releases():
    """Item 37: the Keeper's releases and the Day 3 brief against the world draft's scarcities (warned,
    by sentence, beside a word of scarcity) and the kept sealed terms (failed)."""
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/world-draft.md",
               "# World draft\n- Scarcities: salt, first; good iron, second. Trust is dear.\n"
               "- Local shortages: clean water (unplaced); seed that breeds true (unplaced).\n")
        c = lockcheck.Campaign(repo, "fx")
        assert lockcheck.world_scarcities(c) == ["salt", "iron", "water", "seed"]
        code, out, _ = lock(repo, "--releases")
        assert code == 0 and "releases: 0 failure(s), 0 warning(s)" in out
        rel = "SPOILERS_do_not_open/campaigns/fx/releases/creation/god-tide-night2.md"
        append(repo, rel, "Salt is scarce in this land. You taste salt on your lips.\n")
        append(repo, "campaigns/fx/player/day3-brief.md", "The road is old. Iron came short last year.\n")
        code, out, _ = lock(repo, "--releases")
        assert code == 0 and 'god-tide-night2.md:1: names the world scarcity "salt"' in out
        assert 'day3-brief.md:1: names the world scarcity "iron"' in out and "releases: 0 failure(s), 2 warning(s)" in out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt", "!Weight of Debt\n")
        append(repo, rel, "Your Weight of Debt grows.\n")
        code, out, _ = lock(repo, "--releases")
        assert code == 1 and 'god-tide-night2.md:2: kept sealed term "Weight of Debt"' in out


def test_build6_lockcheck_people_names_in_knowledge():
    """Item 55: another people's name in a people's knowledge file passes only if told to them in their record."""
    know = "campaigns/fx/civs/tallowfolk/knowledge.md"
    with tmpcopy() as repo:
        os.makedirs(os.path.join(repo, "SPOILERS_do_not_open/campaigns/fx/civs/orvanne"))
        append(repo, know, "Traders from the Orvanne come at midsummer.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'knowledge.md:1: people\'s name "Orvanne", not told to the tallowfolk in their record' in out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/tallowfolk-sealed.md", "They trade with the Orvanne.\n")
        code, out, _ = lock(repo, "--leaks")   # the world's side is told to no one (build 6 check, must-fix 3)
        assert code == 1 and 'people\'s name "Orvanne", not told to the tallowfolk' in out, out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/tallowfolk/record.md", "They trade with the Orvanne.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0, out
        append(repo, "campaigns/fx/player/notes.md", "The Orvanne.\n")   # elsewhere it still fails
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "notes.md" in out and "knowledge.md" not in out, out
    with tmpcopy() as repo:   # a sealed term that is no people's name fails there as before
        append(repo, know, "They fear Vessaline.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/tallowfolk/record.md", "Vessaline.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'knowledge.md:1: sealed term "Vessaline"' in out


def test_build6_lockcheck_cast_pointers():
    """Item 71: a cast being with a Limit: line is in no mystery marked Answers questions: no; every pointer resolves."""
    cast = "SPOILERS_do_not_open/campaigns/fx/cast.md"
    with tmpcopy() as repo:
        append(repo, cast, "Mysteries: S03.\n")
        assert lock(repo, "--mysteries")[0] == 0
        append(repo, cast, "\n## The bell-ringer\nA mortal. Mysteries: E01, L01.\n")
        assert lock(repo, "--mysteries")[0] == 0   # no limit: it answers nothing, and may be in a "no" mystery
    with tmpcopy() as repo:
        append(repo, cast, "Mysteries: S03, E01.\n")
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and '"The Drowned Choir [f02]" has a Limit: line (it answers questions) and is in E01' in out
        assert "is in S03" not in out
    with tmpcopy() as repo:
        append(repo, cast, "Mysteries: X09.\n")
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and "Mysteries: names X09, which is not a mystery" in out


def test_build6_timing_file_is_sealed():
    """Item 74: lockcheck warns on a public timing file and scans it for nothing else; check.py reads the
    sealed timing file, and an older campaign's public one when there is no sealed one."""
    with tmpcopy() as repo:
        assert "is public" not in lock(repo, "--leaks")[1]
        append(repo, "campaigns/fx/state/timing.md", "- 2026-11-20 first clock reading, round 2 of the lock.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0 and "WARN leaks: campaigns/fx/state/timing.md is public" in out
    conflict = "- 2026-11-22 01:45 the world waited.\n- 2026-11-22 03:00 clock advanced\n"
    for where in ("SPOILERS_do_not_open/campaigns/fx/state/timing.md", "campaigns/fx/state/timing.md"):
        with tmpcopy() as repo:
            append(repo, where, conflict)
            code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
            assert "timing: 2026-11-22 has both a waited line and a clock advance" in out, (where, out)
    with tmpcopy() as repo:   # the sealed file wins over an older public one
        append(repo, "campaigns/fx/state/timing.md", conflict)
        append(repo, "SPOILERS_do_not_open/campaigns/fx/state/timing.md", "- 2026-11-22 01:45 the world waited.\n")
        assert "timing:" not in run_quiet(check.main, ["fx", "1", "--root", repo])[1]


def test_build6_roll_weighted_draw():
    """Item 63: a weighted draw over 1..T, bands in the order given, logged with the outcome."""
    b, total = roll.bands([("a", 10), ("b", 0), ("c", 5)])
    assert total == 15 and [x["band"] for x in b] == [[1, 10], None, [11, 15]]
    assert [roll.chosen(b, r) for r in (1, 10, 11, 15)] == ["a", "a", "c", "c"]
    for bad in (["a"], ["a=x"], ["a=1", "a=2"], ["a=0"], ["=3"], ["a=-1"]):
        try:
            roll.parse_weights(bad)
            assert False, bad
        except ValueError:
            pass
    d = tempfile.mkdtemp()
    try:
        log = os.path.join(d, "rolls.jsonl")
        seen = set()
        for _ in range(60):
            code, out, _ = run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "storm", "--weight", "a=3", "--weight", "b=0", "--weight", "c=1"])
            e = read_lines(log)[-1]
            assert e["mode"] == "weighted" and e["of"] == 4 and 1 <= e["roll"] <= 4
            assert e["outcome"] == ("a" if e["roll"] <= 3 else "c")
            seen.add(e["outcome"])
        assert "b" not in seen
        e = read_lines(log)[0]
        run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "storm", "--weight", "a=1", "--weight", "c=1",
                              "--reason", "a people already struck", "--replaces", e["id"]])
        last = read_lines(log)[-1]
        assert last["replaces"] == e["id"] and last["reason"] == "a people already struck"
        for bad in (["--die", "d6"], ["--factor", "x=+10"]):
            assert run_quiet(roll.main, ["--log", log, "--who", "k", "--what", "x", "--weight", "a=1", *bad])[0] != 0
    finally:
        shutil.rmtree(d)


def test_build6_player_given_map_name():
    """Item 52: the player's people's home carries the player's name as its map name ("named_by": "player"),
    which counts as the player's own: heard, and never a leak."""
    w = small_world()
    w["features"][0]["named_by"] = "player"
    assert mapt.check_world(w) == []
    seen = {"grade": "seen", "source": "landing", "year": 1}
    assert mapt.heard_name(w["features"][0], seen) == "Oskby"
    assert mapt.heard_name(w["features"][3], seen) is None
    w["features"][3]["named_by"] = "the Keeper"
    assert any("named_by must be" in p for p in mapt.check_world(w))
    with tmpcopy() as repo:
        wp = os.path.join(repo, "SPOILERS_do_not_open/campaigns/fx/map.json")
        append(repo, "campaigns/fx/player/notes.md", "Brackwater Hold stands empty.\n")
        assert lock(repo, "--leaks")[0] == 1   # a place it never heard of
        world = json.load(open(wp))
        next(f for f in world["features"] if f["id"] == "f05")["named_by"] = "player"
        json.dump(world, open(wp, "w"))
        code, out, _ = lock(repo, "--leaks")
        assert code == 0, out


def test_build6_stamp_skips_god_written_files_and_the_log():
    """Item 56: stamp never touches a god's own files in S/gods/<god>/ or the keeper log."""
    with tmpcopy() as repo:
        world_p, _ = fx_paths(repo)
        S = os.path.dirname(world_p)
        skipped = ["gods/god-tide/people-hoped.md", "gods/god-tide/self.md", "gods/god-tide/survey-day1.md",
                   "gods/god-tide/negotiation-night3.md", "gods/god-tide/decisions-002.md", "keeper-log.md"]
        for rel in skipped + ["gods/god-tide/sheet.md", "notes.md"]:
            append(repo, f"SPOILERS_do_not_open/campaigns/fx/{rel}", "Tallowford is near.\n")
        _changed, _total, per = mapt.stamp("fx", S, json.load(open(world_p)))
        done = {r for r, _n in per}
        assert done == {"gods/god-tide/sheet.md", "notes.md"}, done
        for rel in skipped:
            assert open(os.path.join(S, rel)).read() == "Tallowford is near.\n"
    assert mapt.is_god_written("gods/god-x/goals.md") and not mapt.is_god_written("gods/god-x/power-card.md")
    assert not mapt.is_god_written("gods-sealed/god-x/self.md")


def test_build6_places_skips_what_stamp_skips():
    """Build 6 check, should-fix 7: --places warns on no bare map name in a file stamp skips (the keeper log,
    a god's own files), and still fails a bracketed id the map lacks there."""
    with tmpcopy() as repo:
        for rel in ("gods/god-tide/people-hoped.md", "keeper-log.md"):
            append(repo, f"SPOILERS_do_not_open/campaigns/fx/{rel}", "Tallowford is near.\n")
        code, out, _ = lock(repo, "--places")
        assert code == 0 and "people-hoped.md" not in out and "keeper-log.md" not in out, out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/notes.md", "Tallowford is near.\n")
        code, out, _ = lock(repo, "--places")
        assert "notes.md" in out, out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/keeper-log.md", "The ford [f99].\n")
        code, out, _ = lock(repo, "--places")
        assert code == 1 and "keeper-log.md:2: [f99] is not in map.json" in out, out


def test_build6_describe_standing_height_wood_edges_and_knowledge():
    """Item 61: the standing height (ground_ft), wood edges as a tree line, and the god's own knowledge file by label."""
    w = small_world()
    land = w["landings"]["player"]
    t = mapt.describe(w, "r01", mapt.landing_point(land), None, reference=False)
    assert "Standing ground: the point's own height is not given; the region runs 1,000 to 1,400 feet" in t
    t2 = mapt.describe(w, "r01", mapt.landing_point(land), None, reference=False, ground_ft=1180)
    assert "Standing ground: about 1,180 feet at the point" in t2 and "at about 1,180 feet, sees" in t2
    # a wood 8 miles west, on ground as low as the eye's: its tree line shows (sight_miles(60 - 0) is about 12.4)
    w["features"].append({"id": "f09", "name": "Ash Holt", "type": "forest", "shape": "area",
                          "coords": [[2, 40], [16, 40], [16, 60], [2, 60]], "regions": ["r01"]})
    data = {}
    t3 = mapt.describe(w, "r01", mapt.landing_point(land), None, reference=False, data=data)
    assert "a forest (forest), its wood edge about 8 miles west: a tree line, trees about 60 feet tall" in t3, t3
    assert data["wood_edges"][0]["id"] == "f09"
    w["features"][-1]["coords"] = [[2, 40], [5, 40], [5, 60], [2, 60]]   # 30 miles off: past the tree line's reach
    assert "wood edge" not in mapt.describe(w, "r01", mapt.landing_point(land), None, reference=False)
    land["ground_ft"] = "high"
    assert any("ground_ft" in p for p in mapt.check_world(w))
    # the command line finds a god's own knowledge file by its label and says which
    with tmpcopy() as repo:
        world_p, _ = fx_paths(repo)
        kdir = os.path.join(os.path.dirname(world_p), "gods", "god-tide")
        os.makedirs(kdir, exist_ok=True)
        json.dump({"regions": {"r02": {"grade": "seen", "source": "landing", "year": 1, "named": True}}, "features": {}},
                  open(os.path.join(kdir, "map-knowledge.json"), "w"))
        code, out, err = run_quiet(mapt.main, ["describe", "fx", "--world", world_p, "--landing", "god-tide"])
        assert code == 0 and out.startswith("Landing of god-tide: Saltmarsh Reach"), out + err
        assert "names as god-tide knows them, from" in err and "gods/god-tide/map-knowledge.json" in err


def test_build6_landing_lines_and_creation_names():
    """Item 76: on the landing sheet a line the god knows from its landing is drawn only as far as seen;
    smoke keeps its told words over the player's name; a creation name shown is named for the (oog) line."""
    w = small_world()
    painting = mapt.Painting(w)
    at = mapt.landing_point(w["landings"]["player"])
    part = mapt.seen_part(w["features"][1]["coords"], at, 2.0, painting)
    assert part and all(painting.miles(math.dist(at, p)) <= 2.0 + 1e-6 for p in part)
    assert painting.miles(mapt.polyline_length(part)) < 4.1
    k = {"regions": {"r01": {"grade": "seen", "source": "landing", "year": 1, "named": True}},
         "features": {"f02": {"grade": "reported", "source": "own sight at landing", "year": 1, "told": {"name": "a quick river"}}}}
    _r, feats = mapt.gather(w, k, painting)
    clipped, cut = mapt.landing_lines(w, [kv[0] for kv in feats.values()], at, painting)
    assert cut == ["f02"] and len(clipped[0]["coords"]) < 100 and clipped[0]["coords"] != w["features"][1]["coords"]
    # smoke seen from afar: its told words, not the name the player gave the place
    w["features"][0]["aliases"] = [{"name": "Homefire", "by": "player", "since": "creation Day 3"}]
    smoke = {"grade": "rumored", "source": "own sight at landing", "year": 1, "told": {"name": "smoke to the north", "cell": "B2", "bearing": "north"}}
    assert mapt.heard_name(w["features"][0], smoke) == "smoke to the north"
    seen = {"grade": "seen", "source": "landing", "year": 1}
    assert mapt.heard_name(w["features"][0], seen) == "Homefire" and mapt.creation_name(w["features"][0], seen) == "Homefire"
    assert mapt.creation_name(w["features"][0], dict(seen, named=True)) is None
    k["features"]["f01"] = seen
    rk, fk = mapt.gather(w, k, painting)
    assert mapt.creation_names_shown(w, k, fk, rk) == [("f01", "Homefire")]
    d = tempfile.mkdtemp()
    try:
        make_paintings(d)
        wp, kp, out = os.path.join(d, "map.json"), os.path.join(d, "k.json"), os.path.join(d, "out")
        json.dump(w, open(wp, "w"))
        json.dump(k, open(kp, "w"))
        code, o, e = run_quiet(mapt.main, ["draw", "t", "--world", wp, "--knowledge", kp, "--out", out, "--paintings", d, "--zoom", "landing"])
        assert code == 0, o + e
        meta = json.load(open(os.path.join(out, "map-meta.json")))
        assert meta["creation_names"] == [{"id": "f01", "name": "Homefire"}]
        assert "names the player gave at creation" in o and "Homefire (f01)" in o
    finally:
        shutil.rmtree(d)


# ---------------------------------------------------------------- build 7 (run 06 change list)

def test_build7_roll_public_dm_prefix():
    """Items 62 and 70: roll.py --public writes the DM's open roll to the campaign's public log, with its own
    id prefix dm-NNNN; it needs --campaign and a DM --who, and takes no --log. The sealed log is untouched."""
    d = tempfile.mkdtemp()
    real = roll.ROOT
    roll.ROOT = d
    try:
        code, out, err = run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "dm", "--what", "is it market day",
                                               "--factor", "market every few days=-20"])
        assert code == 0, err
        pub = os.path.join(d, "campaigns", "zz", "state", "rolls.jsonl")
        e = read_lines(pub)[0]
        assert e["id"] == "dm-0001" and e["odds"] == 30 and json.loads(out)["id"] == "dm-0001"
        assert not os.path.exists(os.path.join(d, "SPOILERS_do_not_open", "campaigns", "zz", "state", "rolls.jsonl"))
        run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "the Weigher (player), rolled by the dm", "--what", "the scale"])
        run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "dm", "--what", "the scale, again",
                              "--reason", "the player argued a factor", "--replaces", "dm-0002"])
        lines = read_lines(pub)
        assert [l["id"] for l in lines] == ["dm-0001", "dm-0002", "dm-0003"] and lines[2]["replaces"] == "dm-0002"
        assert run_quiet(roll.main, ["--public", "--who", "dm", "--what", "x", "--log", pub])[0] != 0
        assert run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "keeper", "--what", "x"])[0] != 0
        assert run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "dm", "--what", "x", "--log", pub])[0] != 0
        # the Keeper's rolls stay sealed, r-NNNN
        run_quiet(roll.main, ["--campaign", "zz", "--who", "keeper", "--what", "storm"])
        assert read_lines(os.path.join(d, "SPOILERS_do_not_open", "campaigns", "zz", "state", "rolls.jsonl"))[0]["id"] == "r-0001"
        fails, warns = roll.public_log_problems(lines, "pub")
        assert fails == [] and warns == []
        fails, warns = roll.public_log_problems(lines + [{"id": "dm-0004", "who": "keeper", "what": "y"},
                                                        {"id": "dm-0005", "who": "dm", "what": "is it market day"}], "pub")
        assert any("is not the DM's" in f for f in fails) and any("rolled more than once" in f for f in fails)
        _f, warns = roll.public_log_problems([{"id": "r-0001", "who": "dm", "what": "a"}, {"id": "r-0002", "who": "dm", "what": "b"}], "pub")
        assert len(warns) == 1 and "2 line(s) with an older id" in warns[0] and "r-0001 to r-0002" in warns[0]
    finally:
        roll.ROOT = real
        shutil.rmtree(d)


def test_build7_check_public_rolls_and_steps():
    """Items 70 and 73: check.py takes the DM's open rolls in the public log (an older r- id is a note), and
    --step 4 and --step 7 look only for what those steps have made, the clock still on the year."""
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/player/decisions-001.md", "Go north.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/001/year.md", "The year.\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "4"])
        assert code == 0, out
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "7"])
        assert code == 1 and "the DM release" in out and "the morning story" in out and "clock" not in out
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 1 and "clock not advanced to year 2" in out
        append(repo, "campaigns/fx/state/rolls.jsonl",
               '{"id": "dm-0001", "who": "dm", "what": "market day", "odds": 30, "roll": 7, "success": true}\n'
               '{"id": "r-0002", "who": "dm", "what": "the scale", "odds": 50, "roll": 19, "success": true}\n')
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "4"])
        assert code == 0 and "note:" in out and "older id" in out and "rolls are sealed" not in out, out
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"id": "dm-0003", "who": "keeper", "what": "storm", "roll": 4}\n')
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "4"])
        assert code == 1 and "is not the DM's" in out
        with open(os.path.join(repo, "campaigns", "fx", "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 2\nstatus: open\nseason_opens: spring\n")
        assert "at step 4 the clock is still on year 1" in run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "4"])[1]


def test_build7_lockcheck_public_rolls():
    """Item 70: lockcheck --rolls passes the DM's open rolls in the public log, fails a line that is not the
    DM's, fails a dm-NNNN cited anywhere that the public log lacks, and warns on older r- ids there."""
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"id": "dm-0001", "who": "dm", "what": "market day", "roll": 7}\n')
        append(repo, "SPOILERS_do_not_open/campaigns/fx/notes.md", "Overruled DM roll dm-0001 by the factors.\n")
        code, out, _ = lock(repo, "--rolls")
        assert code == 0 and "rolls: 0 failure(s), 0 warning(s)" in out, out
        append(repo, "campaigns/fx/player/rolling-save.md", "The scale read off (dm-0002).\n")
        code, out, _ = lock(repo, "--rolls")
        assert code == 1 and "cites dm-0002, which is not in the public log" in out
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"id": "r-0001", "who": "dm", "what": "market day", "roll": 7}\n')
        code, out, _ = lock(repo, "--rolls")
        assert code == 0 and "1 line(s) with an older id" in out and "rolls: 0 failure(s), 1 warning(s)" in out


def test_build7_lockcheck_day1_no_sealed_terms():
    """Item 1: on Day 1, before Night 1 writes S/sealed-terms.txt, --leaks passes with "no sealed terms yet",
    with or without a sealed folder; once Night 1's work is there a missing file fails as before."""
    with tmpcopy() as repo:
        shutil.rmtree(os.path.join(repo, "SPOILERS_do_not_open", "campaigns", "fx"))
        with open(os.path.join(repo, "campaigns", "fx", "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 0\nstatus: creation\ncreation_night: 1\nseason_opens: not yet set\n")
        os.remove(os.path.join(repo, "campaigns", "fx", "player", "map-knowledge.json"))
        code, out, _ = lock(repo, "--leaks", "--dashes")
        assert code == 0 and "no sealed terms yet" in out and "leaks: 0 failure(s)" in out, out
        append(repo, "SPOILERS_do_not_open/campaigns/fx/player/unsaid.md", "No sealed answers on Day 1.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0 and "no sealed terms yet" in out, out
        append(repo, "campaigns/fx/player/survey-day1.md", "We were seven when we came down.\n")
        assert lock(repo, "--leaks")[0] == 1   # the other leak rules still run on Day 1
    with tmpcopy() as repo:   # Night 1 has written its world draft: the file is due
        os.remove(os.path.join(repo, "SPOILERS_do_not_open", "campaigns", "fx", "sealed-terms.txt"))
        with open(os.path.join(repo, "campaigns", "fx", "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 0\nstatus: creation\ncreation_night: 1\nseason_opens: not yet set\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "sealed-terms.txt is missing" in out


def test_build7_lockcheck_transcripts_and_card_number_words():
    """Items 12, 13 and 96: number words are not scanned in the creation transcripts (the DM's posts too), in
    the play transcripts' "## Player:" and "## DM:" sections, or in the card's frozen terms; a kept term is not
    scanned in a play transcript's sections; the player's own words there pass; everything else is scanned."""
    sealed = "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt"
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/player/transcript-day2.md", "## DM:\n\nThose three are given, the same for every god.\n"
                                                              "## Player:\n\nI am the god of the moment two people agree.\n")
        append(repo, "campaigns/fx/player/transcript-year-001.md",
               "# Transcript: Year 1\n\n## DM:\n\n(oog) Odds 60, plus 10 because he came down to you himself.\n\n"
               "## Player:\n\nTwo of us came down to the landing. I ask after the kettle.\n")
        append(repo, "campaigns/fx/player/power-card.md",
               "# Power card\n\n### The Seal\nDescription: Up to two seals a season may the god set.\n"
               "Limits settled at creation:\n- Two at most, the god says.\n- Not applicable: water.\n"
               "Rulings:\n- Year 2. The god may set two.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "power-card.md:9" in out, out   # the Rulings line is not frozen text
        assert "transcript-day2" not in out and "transcript-year-001" not in out and "power-card.md:4" not in out
        assert "power-card.md:6" not in out and out.count("FAIL") == 1
    with tmpcopy() as repo:   # outside the sections of a play transcript the scan runs; a kept term is skipped inside
        append(repo, sealed, "!kettle\n")
        append(repo, "campaigns/fx/player/transcript-year-002.md",
               "# Transcript: Year 2\nThree gods came down, the header says.\n\n## DM:\n\nThe kettle sings.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "transcript-year-002.md:2" in out and "transcript-year-002.md:6" not in out, out
        append(repo, "campaigns/fx/player/rolling-save.md", "The kettle sings.\n")
        assert "rolling-save.md:1" in lock(repo, "--leaks")[1]
    with tmpcopy() as repo:   # the DM's words in a play transcript are still scanned for an ordinary sealed term
        append(repo, "campaigns/fx/player/transcript-year-001.md", "## DM:\n\nThe Undertow Oath waits.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and "Undertow Oath" in out


def test_build7_lockcheck_line_allow():
    """Item 71: a line allow, `in <file>: "<phrase>"`, exempts the phrase on a line of that file only; a
    phenomenon allowed by its label is warned on, since it lets every count through."""
    allowf = "SPOILERS_do_not_open/campaigns/fx/leak-allow.txt"
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/releases/001/dm.md", "The bell hum came on 3 nights this year.\n")
        append(repo, "campaigns/fx/player/notes.md", "The bell hum came on 3 nights this year.\n")
        assert lock(repo, "--leaks")[1].count("phenomenon count") == 2
        append(repo, allowf, 'in campaigns/fx/releases/001/dm.md: "bell hum came on 3 nights"  # seen, 2026-11-25\n')
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and out.count("phenomenon count") == 1 and "player/notes.md" in out and "releases/001" not in out, out
        append(repo, allowf, 'in P/player/notes.md: "came on 3 nights"\n')
        assert lock(repo, "--leaks")[0] == 0
        c = lockcheck.Campaign(repo, "fx")
        assert ("releases/001/dm.md", "bell hum came on 3 nights") in c.allow_lines()
        assert not any(p.startswith("in ") for p in c.allow())
    with tmpcopy() as repo:
        append(repo, allowf, "bell-hum-nights\n")
        append(repo, "campaigns/fx/player/notes.md", "The bell hum came on 5 nights.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 0 and 'the phenomenon "bell-hum-nights" is allowed by its label' in out


def test_build7_lockcheck_civs():
    """Item 78: --leaks fails a kept sealed term in a civ agent's sealed files (S/civs/<people>/); the godless
    peoples and the Keeper's <people>-sealed.md are not a civ agent's files."""
    sealed = "SPOILERS_do_not_open/campaigns/fx/sealed-terms.txt"
    with tmpcopy() as repo:
        append(repo, sealed, "!luck\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/godless/hill-folk/record.md", "By luck the ford held.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/marsh-folk-sealed.md", "Sealed factor: luck.\n")
        assert lock(repo, "--leaks")[0] == 0
        append(repo, "SPOILERS_do_not_open/campaigns/fx/civs/marsh-folk/years/001.md", "By luck the nets came home full.\n")
        code, out, _ = lock(repo, "--leaks")
        assert code == 1 and 'civs/marsh-folk/years/001.md:1: kept sealed term "luck"' in out
        assert "leaks: 1 failure(s)" in lock(repo)[1]   # in --all too


def test_build7_stamp_skips_flags_logs_and_rulings():
    """Item 78: stamp skips the checker's flags files (years/NNN/flags.md too), rulings.md and other agents'
    logs (a god's map-log.md); lockcheck --places warns on no bare name in them."""
    with tmpcopy() as repo:
        S = os.path.join(repo, "SPOILERS_do_not_open", "campaigns", "fx")
        for rel in ("years/001/flags.md", "rulings.md", "gods/god-tide/map-log.md", "years/001/year.md"):
            append(repo, os.path.join("SPOILERS_do_not_open/campaigns/fx", rel), "They met at Tallowford.\n")
        world = json.load(open(os.path.join(S, "map.json")))
        changed, total, per = mapt.stamp("fx", S, world)
        assert [r for r, _n in per] == ["years/001/year.md"], per
        for rel in ("years/001/flags.md", "rulings.md", "gods/god-tide/map-log.md"):
            assert "[f01]" not in open(os.path.join(S, rel)).read()
            assert mapt.stamp_skipped(rel)
        assert not mapt.stamp_skipped("years/001/year.md") and mapt.stamp_skipped("years/000/lock-flags.md")
        code, out, _ = lock(repo, "--places")
        assert "flags.md" not in out and "rulings.md" not in out and "map-log.md" not in out


def test_build7_validate_sea_all_round():
    """Item 43: land traced at a sheet edge fails validate when the plan asks for sea on every side (the
    placement plan, the world draft, map.json, or the surface map request); otherwise it warns as before."""
    w = {"campaign": "t", "painting": {"size": [1000, 1000], "miles_per_pixel": 1.0},
         "regions": [{"id": "r01", "terrain": "sea", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
                     {"id": "r02", "terrain": "plain", "polygon": [[0, 100], [900, 100], [900, 900], [0, 900]]}]}
    d = tempfile.mkdtemp()
    try:
        S = os.path.join(d, "SPOILERS_do_not_open", "campaigns", "t")
        os.makedirs(os.path.join(S, "world"))
        assert mapt.edge_land_problems(w, S)[0] == [] and len(mapt.edge_land_problems(w, S)[1]) == 1
        with open(os.path.join(S, "world", "placement-plan.md"), "w") as f:
            f.write("# Plan\nOne continent with sea on every side.\n")
        probs, warns = mapt.edge_land_problems(w, S)
        assert len(probs) == 1 and warns == [] and "west edge(s)" in probs[0] and "world/placement-plan.md:2" in probs[0]
        os.remove(os.path.join(S, "world", "placement-plan.md"))
        req = os.path.join(d, "SPOILERS_do_not_open", "images", "requests")
        os.makedirs(req)
        json.dump({"id": "t-map-surface", "prompt": "A continent, with a margin of sea on every side so that no coast is cut off."},
                  open(os.path.join(req, "t-map-surface.json"), "w"))
        assert "surface map request" in mapt.edge_land_problems(w, S)[0][0]
        wp = os.path.join(S, "map.json")
        json.dump(w, open(wp, "w"))
        code, out, _ = run_quiet(mapt.main, ["validate", "t", "--world", wp, "--knowledge", os.path.join(d, "none.json")])
        assert code == 1 and "asks for sea on every side" in out
        assert mapt.edge_land_problems(dict(w, painting=dict(w["painting"], sea_all_round=True)), None)[0]
    finally:
        shutil.rmtree(d)


def coast_world():
    """A sea with a headland of land between two coves: a straight boat line from one cove to the other crosses it."""
    return {"campaign": "t", "painting": {"size": [400, 400], "miles_per_pixel": 0.5, "grid": {"cols": 4, "rows": 4}},
            "regions": [{"id": "r01", "name": "Grey Sea", "terrain": "sea",
                         "polygon": [[0, 0], [150, 0], [150, 250], [250, 250], [250, 0], [400, 0], [400, 400], [0, 400]],
                         "elevation": "sea", "water": "the sea", "climate": "cold", "neighbors": []},
                        {"id": "r02", "name": "Ness", "terrain": "coast", "polygon": [[150, 0], [250, 0], [250, 250], [150, 250]],
                         "elevation": "0 to 300 feet", "water": "springs", "climate": "cold", "neighbors": []}],
            "features": [{"id": "f01", "name": "West Cove", "type": "village", "shape": "point", "coords": [[100, 100]], "regions": ["r01"]},
                         {"id": "f02", "name": "East Cove", "type": "village", "shape": "point", "coords": [[300, 100]], "regions": ["r01"]}],
            "landings": {}}


def test_build7_travel_boat_coasting():
    """Item 44: a boat trip whose straight line crosses a headland goes round it by water, coasting, and is
    priced; a walk still goes over the land."""
    w = coast_world()
    namer = mapt.Namer(w, None, True)
    text, data = mapt.travel(w, "f01", "f02", "boat", (), namer, show_ids=True)
    assert data["days"] is not None and "coasting, around the land" in text and "coasting by the shortest way" in text, text
    assert all(s["ground"] == "sea" for s in data["segments"]) and data["miles"] > 100 * 0.5, data
    path = mapt.coasting_route(w, (100, 100), (300, 100), mapt.Painting(w))
    assert path and all(not (150 < p[0] < 250 and p[1] < 250) for p in path)
    assert mapt.coasting_route(w, (100, 300), (300, 300), mapt.Painting(w)) is None   # open water all the way
    _t, walk = mapt.travel(w, "f01", "f02", "foot", (), namer)
    assert walk["days"] is None or all(s["ground"] != "land" for s in walk["segments"])


def test_build7_describe_lists_region_areas():
    """Item 44: a marsh area of the landing's own region past the near distance is listed in its own section
    (and JSON in_region), never as in view."""
    w = {"campaign": "t", "painting": {"size": [400, 400], "miles_per_pixel": 0.1, "grid": {"cols": 4, "rows": 4}},
         "regions": [{"id": "r01", "name": "Reedmouths", "terrain": "marsh, a wide delta", "polygon": [[0, 0], [400, 0], [400, 400], [0, 400]],
                      "elevation": "0 to 20 feet", "water": "channels", "climate": "mild", "neighbors": []}],
         "features": [{"id": "f01", "name": "Maun Flats", "type": "marsh", "shape": "area",
                       "coords": [[200, 230], [260, 230], [260, 280], [200, 280]], "regions": ["r01"]},
                      {"id": "f02", "name": "Near Pond", "type": "lake", "shape": "area",
                       "coords": [[200, 205], [210, 205], [210, 210], [200, 210]], "regions": ["r01"]}],
         "landings": {"player": {"region": "r01", "at": [200, 200], "ground_ft": 12}}}
    data = {}
    text = mapt.describe(w, "r01", (200, 200), {"regions": {}, "features": {}}, False, "Landing", reference=False, data=data, ground_ft=12)
    assert "In this region, past the near distance and not in view" in text and "a marsh (marsh), about 3 miles south" in text, text
    assert [x["id"] for x in data["in_region"]] == ["f01"] and "f01" not in [x["id"] for x in data["in_view"]]
    assert "f02" in [x["id"] for x in data["in_view"]]


def test_build7_reveal_line_stretch_and_gazetteer():
    """Item 61: a line revealed as seen needs a stretch (or --whole); the knowledge file keeps the stretch's
    ends; the gazetteer gives only what was seen, never the whole length or the far end; the sheet draws it."""
    with tmpcopy() as repo:
        world_p, know_p = fx_paths(repo)
        k = json.load(open(know_p))
        del k["features"]["f03"]
        json.dump(k, open(know_p, "w"))
        code, out, err = reveal(repo, "--feature", "f03", "--grade", "seen", "--source", "walked", "--year", "1")
        assert code != 0 and "f03" not in json.load(open(know_p))["features"]
        code, out, err = reveal(repo, "--feature", "f03", "--grade", "seen", "--source", "walked a mile of it", "--year", "1",
                                "--seen-from", "f01", "--reach", "1", "--named")
        assert code == 0, err
        e = json.load(open(know_p))["features"]["f03"]
        assert len(e["stretches"]) == 1 and e["stretches"][0][0] == [220.0, 260.0]
        world = json.load(open(world_p))
        assert mapt.knowledge_problems(world, json.load(open(know_p))) == []
        log = open(os.path.join(os.path.dirname(know_p), "map-log.md")).read()
        assert "stretch seen from B2 to B2, about 1.0 miles" in log
        out_d = os.path.join(repo, "out")
        run_quiet(mapt.main, ["gazetteer", "fx", "--world", world_p, "--knowledge", know_p, "--out", out_d])
        g = open(os.path.join(out_d, "gazetteer.md")).read()
        line = next(l for l in g.splitlines() if "The Chalk Way" in l and "(road)" in l)
        assert "seen in part" in line and "about 1.0 miles of it seen" in line and "D2" not in line and "miles long" not in line, line
        paint = os.path.join(repo, "paint")
        make_paintings(paint)
        code, o, err = run_quiet(mapt.main, ["draw", "fx", "--world", world_p, "--knowledge", know_p, "--paintings", paint,
                                             "--out", out_d, "--zoom", "known"])
        assert code == 0, err
        # a second stretch farther on is added beside the first; --whole makes the line whole
        assert reveal(repo, "--feature", "f03", "--grade", "seen", "--source", "x", "--year", "2", "--stretch", "600,207.3 640,200")[0] == 0
        assert len(json.load(open(know_p))["features"]["f03"]["stretches"]) == 2
        assert reveal(repo, "--feature", "f03", "--grade", "seen", "--source", "x", "--year", "2", "--whole", "walked it all")[0] == 0
        assert "stretches" not in json.load(open(know_p))["features"]["f03"]
        # a seen line already whole stays whole without a stretch; a stretch is only for a line
        assert reveal(repo, "--feature", "f02", "--grade", "seen", "--source", "x", "--year", "2")[0] == 0
        assert reveal(repo, "--feature", "f01", "--grade", "seen", "--source", "x", "--year", "2", "--whole", "x")[0] != 0
        bad = json.load(open(know_p))
        bad["features"]["f02"]["stretches"] = [[[900, 900], [950, 950]]]
        assert any("does not lie on the line" in p for p in mapt.knowledge_problems(world, bad))


def test_build7_docs_phenomena_name_and_paint_edit():
    """Items 53 and 58: phenomena.py documents the name field; paint.py's docs say an edited request with a
    painting paints nothing."""
    import paint
    import subprocess
    assert '"name"' in open(os.path.join(ROOT, "tools", "phenomena.py")).read().split('"""')[1]
    assert "edited after its painting has come back" in paint.__doc__
    d = tempfile.mkdtemp()
    try:   # the optional months are printed after the count, and must number as many as it
        os.makedirs(os.path.join(d, "state"))
        json.dump({"dim-nights": {"name": "dim nights", "rate": "fixed", "per_year": {"1": 3, "2": 2},
                                  "months": {"1": [8, 7, 5], "2": [4]}}}, open(os.path.join(d, "state", "phenomena.json"), "w"))
        run = lambda y: subprocess.run([sys.executable, os.path.join(ROOT, "tools", "phenomena.py"), d, y], capture_output=True, text=True)
        r = run("1")
        assert r.returncode == 0 and r.stdout.strip() == "dim-nights: 3 (months 5, 7, 8)"
        assert run("2").returncode == 1 and run("3").stdout.strip() == "dim-nights: 0"
    finally:
        shutil.rmtree(d)


def test_build7_check_held_morning_request():
    """Build check B7: a morning painting request held in images/held/ is a note when the campaign's
    images.md does not approve it, a finding when it does; with neither a request nor a held one, a finding."""
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/player/decisions-001.md", "Go north.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/001/year.md", "The year.\n")
        append(repo, "campaigns/fx/releases/001/dm.md", "Release.\n")
        append(repo, "campaigns/fx/years/002/morning-story.md", "Morning.\n")
        run = lambda: run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "7"])
        code, out, _ = run()
        assert code == 1 and "no painting request for the morning story (none in images/requests/ or images/held/)" in out
        append(repo, "images/held/fx-002-morning.json", '{"id": "fx-002-morning", "campaign": "fx", "prompt": "dawn"}\n')
        code, out, _ = run()
        assert code == 0 and "note: the morning painting request waits in images/held/fx-002-morning.json" in out, out
        append(repo, "campaigns/fx/state/images.md", "- year morning painting: approved, one per played year\n")
        code, out, _ = run()
        assert code == 1 and "it belongs in images/requests/" in out, out
        os.remove(os.path.join(repo, "images", "held", "fx-002-morning.json"))
        append(repo, "images/requests/fx-002-morning.json", '{"id": "fx-002-morning", "campaign": "fx", "prompt": "dawn"}\n')
        assert run()[0] == 0


# ---------------------------------------------------------------- build 8 (1.0): run 07 change list


def test_build8_paint_morning_named_by_its_own_year():
    """Item 14 (Michael, 2026-11-27 19:32, "fix it"): a play-year morning is approved only by the images.md line
    that names its own year, in paint.py and in check.py, which reads approval through paint.covered()."""
    import paint
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "campaigns", "zz", "state"))
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("- first morning painting: approved\n- Year 2 morning painting: approved\n"
                    "- Year 3 morning painting: approved\n- **Year 4 morning painting**: approved\n"
                    "- any other painting or repaint: not approved; hold and ask Michael\n")
        cov = lambda n: paint.covered({"id": f"zz-{n:03d}-morning"}, d)
        assert all(cov(n)[0] for n in (1, 2, 3, 4)), [cov(n) for n in (1, 2, 3, 4)]
        assert cov(2)[1] == "year 2 morning painting: approved" and cov(4)[1] == "year 4 morning painting: approved"
        assert not cov(5)[0] and not cov(6)[0] and "does not approve it" in cov(5)[1]
        # a Year 5 morning is not approved by the Year 2 line alone
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("- Year 2 morning painting: approved\n")
        assert not cov(5)[0] and cov(2)[0] and not cov(3)[0]
        # the line may name its year in words or in its value, or name the request by id
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "a") as f:
            f.write("- year five morning painting: approved\n- morning painting: approved for year 7\n- zz-008-morning: approved\n")
        assert cov(5)[0] and cov(7)[0] and cov(8)[0] and not cov(6)[0]
        # the standing play line creation-nights.md writes names every played year, within its count
        with open(os.path.join(d, "campaigns", "zz", "state", "images.md"), "w") as f:
            f.write("- year morning painting: approved, one per played year\n")
        assert cov(5)[0] and cov(12)[0]
        assert paint.year_ok(5, "year 2 morning painting", "approved") is False
        assert paint.year_ok(None, "first morning painting", "approved") is True
    finally:
        shutil.rmtree(d)
    # the sim-06 held requests for Years 5 and 6 are not approved; the Year 2 to 4 mornings still are
    for n in (5, 6):
        req = json.load(open(os.path.join(ROOT, "images", "held", f"sim-06-{n:03d}-morning.json")))
        ok, why = paint.covered(req, ROOT)
        assert not ok, why
        assert check.held_request_approved(ROOT, os.path.join(ROOT, "images", "held", f"sim-06-{n:03d}-morning.json")) == (ok, why)
    for n in (2, 3, 4):
        ok, why = paint.covered({"id": f"sim-06-{n:03d}-morning"}, ROOT)
        assert ok and why == f"year {n} morning painting: approved", why


def test_build8_check_held_morning_of_another_year():
    """Item 14 in check.py: a held Year 5 morning is a note, not a finding, under a Year 2 line."""
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/player/decisions-004.md", "Go north.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/004/year.md", "The year.\n")
        append(repo, "campaigns/fx/releases/004/dm.md", "Release.\n")
        append(repo, "campaigns/fx/years/005/morning-story.md", "Morning.\n")
        append(repo, "campaigns/fx/state/images.md", "- Year 2 morning painting: approved\n")
        append(repo, "images/held/fx-005-morning.json", '{"id": "fx-005-morning", "campaign": "fx", "prompt": "dawn"}\n')
        with open(os.path.join(repo, "campaigns", "fx", "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 4\nstatus: open\nseason_opens: 3\n")
        code, out, _ = run_quiet(check.main, ["fx", "4", "--root", repo, "--step", "7"])
        assert code == 0 and "note: the morning painting request waits in images/held/fx-005-morning.json" in out, out
        append(repo, "campaigns/fx/state/images.md", "- Year 5 morning painting: approved\n")
        code, out, _ = run_quiet(check.main, ["fx", "4", "--root", repo, "--step", "7"])
        assert code == 1 and "it belongs in images/requests/" in out and "(year 5 morning painting: approved)" in out, out


def test_build8_check_transcript_append_only():
    """Item 24: check.py fails a transcript whose `## ` count falls between commits, or that is shorter than its
    last committed version; a fall a later commit restored is a note."""
    import subprocess
    with tmpcopy() as repo:
        append(repo, "campaigns/fx/player/decisions-001.md", "Go north.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/001/year.md", "The year.\n")
        git = lambda *a: subprocess.run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@example.com", *a],
                                        capture_output=True, text=True, check=True)
        git("init", "-q")
        tp = os.path.join(repo, "campaigns", "fx", "player", "transcript-year-001.md")
        posts = ["## DM:\n\nThe ford.\n", "## Player:\n\nI cross.\n", "## DM:\n\nThe water is cold.\n"]

        def commit(text, msg):
            open(tp, "w").write(text)
            git("add", "-A")
            git("commit", "-q", "-m", msg)
        run = lambda: run_quiet(check.main, ["fx", "1", "--root", repo, "--step", "4"])
        commit(posts[0], "one")
        commit(posts[0] + "\n" + posts[1], "two")
        assert "transcript" not in run()[1]
        # overwritten at the third post: the count falls from 2 to 1
        commit(posts[2], "three")
        code, out, _ = run()
        assert code == 1 and "fell from 2 to 1 `## ` sections between commits" in out and "append-only" in out, out
        # restored from the commits, every section in order: a note, not a finding
        commit(posts[0] + "\n" + posts[1] + "\n" + posts[2], "restored")
        code, out, _ = run()
        assert code == 0 and "note: transcript:" in out and "so it was restored" in out, out
        # the working file shorter than its last committed version
        open(tp, "w").write(posts[0])
        code, out, _ = run()
        assert code == 1 and "is shorter than its last committed version" in out, out
        # outside a git repository there is nothing to compare
        f, n = check.transcript_problems(tempfile.gettempdir(), os.path.join(tempfile.gettempdir(), "no-such-transcript.md"))
        assert f == [] and n == []
    assert check.sections("## DM:\n\na\n## Player:\n\nb\n") == ["## DM:\n\na", "## Player:\n\nb"]


def test_build8_lockcheck_skips_every_year_flags_file():
    """Item 26: every years/NNN/flags.md is the checker's file, skipped by the place scan (and every mode)."""
    assert lockcheck.is_flags_file(os.path.join("S", "years", "004", "flags.md"))
    assert lockcheck.is_flags_file("lock-flags-round2.md")
    assert not lockcheck.is_flags_file(os.path.join("S", "years", "004", "year.md"))
    assert not lockcheck.is_flags_file("flags.md") and not lockcheck.is_flags_file(os.path.join("S", "notes", "flags.md"))
    with tmpcopy() as repo:
        for y in ("001", "004"):
            append(repo, f"SPOILERS_do_not_open/campaigns/fx/years/{y}/flags.md", "Flag: [painting] is quoted from a release.\n")
        code, out, _ = lock(repo, "--places")
        assert code == 0, out


def test_build8_roll_help_names_the_dm_form():
    """Item 23: roll.py --help gives --who as engine/roles/dm.md does, "<party>, rolled by the dm"."""
    code, out, _ = run_quiet(roll.main, ["--help"])
    assert code == 0 and "<party>, rolled by the dm" in out, out
    assert '--who "<party>, rolled by the dm"' in roll.__doc__
    assert '--who "<party>, rolled by the dm"' in open(os.path.join(ROOT, "engine", "roles", "dm.md")).read()


def test_build8_travel_by_direction_and_named_ends():
    """Item 25 (Michael, 2026-11-27 19:32, "the direction of travel matters"): a line is priced segment by segment
    in the direction travelled, from the line's own pace data, and travel names each line's ends by their places."""
    w = travel_world()
    # the road climbs from Westby to the ridge at its bend, and runs level from the ridge to Eastby
    w["features"][2]["pace"] = [{"from": 0, "to": 1, "forward": "mountain", "back": "rough"}]
    assert mapt.check_world(w) == []
    namer = mapt.Namer(w, None, True)
    leg = math.dist((20, 50.2), (100, 10))
    _, east = mapt.travel(w, "f01", "f02", "foot", ("f03",), namer, show_ids=True)
    text, west = mapt.travel(w, "f02", "f01", "foot", ("f03",), namer, show_ids=True)
    assert [(s["ground"], s["toward"]) for s in east["segments"]] == [("mountain", "end"), ("road", "end")]
    assert [(s["ground"], s["toward"]) for s in west["segments"]] == [("road", "start"), ("rough", "start")]
    assert abs(east["days"] - (leg / 8 + leg / 20)) < 0.02 and abs(west["days"] - (leg / 20 + leg / 14)) < 0.02
    assert abs(east["miles"] - west["miles"]) < 0.01 and east["days"] > west["days"]
    assert "toward its first point (:start), at Westby [f01], in West Plain [r01] (A3)" in text
    assert "by the line's own data for this direction" in text
    assert ("Ends: The Bent Road [f03] runs from its first point (:start), at Westby [f01], in West Plain [r01] (A3), "
            "to its last point (:end), at Eastby [f02], in East Wood [r02] (E3).") in text
    assert west["ends"]["f03"]["start"].startswith("at Westby")
    # a horse on the same stretch takes the rows of its own table
    _, ride = mapt.travel(w, "f01", "f02", "horse", ("f03",), namer)
    assert [s["rate"] for s in ride["segments"]] == [10, 30]
    # a river by boat: downstream toward its mouth, upstream toward its source, and its own data where it has it
    w["features"][0]["coords"] = [[20, 70.3]]
    w["features"][1]["coords"] = [[180, 69.8]]
    _, down = mapt.travel(w, "f01", "f02", "boat", ("f04",), namer)
    _, up = mapt.travel(w, "f02", "f01", "boat", ("f04",), namer)
    assert [s["ground"] for s in down["segments"]] == ["river_down"] and [s["ground"] for s in up["segments"]] == ["river_up"]
    # a walk along the bank: the river's land rows by direction, else the ground
    w["features"][3]["pace"] = [{"from": 0, "to": 1, "back": "marsh"}]
    _, bank_e = mapt.travel(w, "f01", "f02", "foot", ("f04",), namer)
    _, bank_w = mapt.travel(w, "f02", "f01", "foot", ("f04",), namer)
    assert [s["ground"] for s in bank_e["segments"]] == ["rough", "forest"] and [s["ground"] for s in bank_w["segments"]] == ["marsh", "marsh"]
    assert [s["ground"] for s in mapt.travel(w, "f02", "f01", "boat", ("f04",), namer)[1]["segments"]] == ["river_up"]
    # an end named as a line's :start or :end says where on the ground it lies
    text, _ = mapt.travel(w, "f03:end", "f03:start", "foot", ("f03",), namer, show_ids=True)
    # (the towns now stand on the river, twenty miles south of the road's ends: the nearest known place, with its bearing)
    assert text.startswith("Travel from The Bent Road [f03]'s last point (:end), about 20 miles north of Eastby [f02], in East Wood "
                           "[r02] (E3), to The Bent Road [f03]'s first point (:start), about 20 miles north of Westby [f01], in West "
                           "Plain [r01] (A3), on foot"), text
    # names as the god knows them: an unknown place is never named at a line's end
    text, _ = mapt.travel(w, "f01", "f02", "foot", ("f03",), mapt.Namer(w, {"regions": {}, "features": {}}))
    assert "Westby" not in text and "West Plain" not in text and "runs from its first point (:start), in a plain country (A3)" in text
    # validate checks the form of pace
    bad = json.loads(json.dumps(w))
    bad["features"][2]["pace"] = [{"from": 1, "to": 0, "forward": "road"}, {"from": 0, "to": 2, "forward": "uphill"}]
    probs = mapt.check_world(bad)
    assert any("from and to are point indexes" in p for p in probs) and any("'uphill' is not a pace table row" in p for p in probs)
    assert mapt.directional_pieces({"coords": [[0, 0], [10, 0]]}, 0, 10) == [(0, 10, None)]


def test_build8_gazetteer_prices_each_way():
    """Item 25 in the gazetteer: Travel by route gives each direction its own figure when they differ, and the
    river's way down and up are named by the places."""
    w = travel_world()
    w["features"][2]["pace"] = [{"from": 0, "to": 1, "forward": "mountain", "back": "rough"}]
    w["features"][0]["coords"] = [[20, 50.2]]
    w["features"].append({"id": "f05", "name": "Riverby", "type": "town", "shape": "point", "coords": [[20, 70]], "regions": ["r01"]})
    w["features"].append({"id": "f06", "name": "Mouthby", "type": "town", "shape": "point", "coords": [[180, 70]], "regions": ["r02"]})
    seen = {"grade": "seen", "source": "walked", "year": 1, "named": True}
    kn = {"regions": {"r01": dict(seen), "r02": dict(seen)},
          "features": {i: dict(seen) for i in ("f01", "f02", "f03", "f05", "f06")}}
    kn["features"]["f04"] = dict(seen)
    d = tempfile.mkdtemp()
    try:
        g = open(mapt.gazetteer(w, kn, d, os.path.join(d, "map-log.md"))).read()
        leg = math.dist((20, 50.2), (100, 10))
        east = f"{leg / 8 + leg / 20:.1f}"
        west = f"{leg / 20 + leg / 14:.1f}"
        assert f"along **The Bent Road** (road): 179 miles; from Westby to Eastby {east} days on foot" in g, g
        assert f"; from Eastby to Westby {west} days on foot" in g
        assert ("along **The Long Water** (river): 160 miles; from Riverby to Mouthby 5.3 days by boat downstream; "
                "from Mouthby to Riverby 13.3 days by boat upstream (seen).") in g, g
        assert "from its source, at Riverby (A3), to its mouth, at Mouthby (E3)" in g
    finally:
        shutil.rmtree(d)


def test_build8_paint_waiting_morning_needs_year_and_play_day():
    """Agent E's note on decision 2: a further morning while the clock waits (<name>-NNN-morning-K) is approved only
    by a line naming its year and its play day, never by the year's own line or the standing line; an id is
    matched whole, so a line for zz-005-morning-2 does not approve zz-005-morning."""
    import paint
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "campaigns", "zz", "state"))
        md = os.path.join(d, "campaigns", "zz", "state", "images.md")
        with open(md, "w") as f:
            f.write("- year morning painting: approved, one per played year\n- Year 5 morning painting: approved\n")
        cov = lambda rid: paint.covered({"id": rid}, d)[0]
        assert cov("zz-005-morning") and cov("zz-006-morning")
        assert not cov("zz-005-morning-2") and not cov("zz-006-morning-2")
        with open(md, "a") as f:
            f.write("- Year 5 morning painting, play day 2: approved\n")
        assert cov("zz-005-morning-2") and not cov("zz-005-morning-3") and not cov("zz-006-morning-2")
        with open(md, "w") as f:
            f.write("- zz-005-morning-2: approved\n")
        assert cov("zz-005-morning-2") and not cov("zz-005-morning")
        assert paint.play_day_of("005-morning-2") == 2 and paint.play_day_of("005-morning") is None
    finally:
        shutil.rmtree(d)


def test_build8_check_play_days_and_the_waiting_clock():
    """Agent E's note on decision 1: check.py reads the clock's play_day, the K-suffixed files of a later play day,
    the waiting morning and its request, and the timing line "clock waited"."""
    with tmpcopy() as repo:
        clock = os.path.join(repo, "campaigns", "fx", "state", "clock.md")
        setclock = lambda extra="": open(clock, "w").write(f"campaign: fx\nyear: 3\nstatus: open\nseason_opens: 3\n{extra}")
        append(repo, "campaigns/fx/player/decisions-003.md", "Go north.\n")
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/003/year.md", "The year.\n")
        append(repo, "campaigns/fx/releases/003/dm.md", "Release.\n")
        # play day 1 stops at a held moment: the morning is years/003/morning-story-2.md and the clock waits
        append(repo, "campaigns/fx/years/003/morning-story-2.md", "Morning.\n")
        append(repo, "images/held/fx-003-morning-2.json", '{"id": "fx-003-morning-2", "campaign": "fx", "prompt": "dawn"}\n')
        setclock()
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo, "--step", "7"])
        assert code == 0 and "fx-003-morning-2.json" in out, out
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo])
        assert code == 1 and "waits on year 3 with play_day: 2" in out, out
        setclock("play_day: 2\n")
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo])
        assert code == 0, out
        # play day 2: its own decisions file and release, numbered
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo, "--step", "4"])
        assert code == 1 and "no player/decisions-003-2.md" in out, out
        append(repo, "campaigns/fx/player/decisions-003-2.md", "I answer.\n")
        assert run_quiet(check.main, ["fx", "3", "--root", repo, "--step", "4"])[0] == 0
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo, "--step", "7"])
        assert code == 1 and "releases/003/dm-2.md" in out, out
        append(repo, "campaigns/fx/releases/003/dm-2.md", "Release two.\n")
        append(repo, "campaigns/fx/years/004/morning-story.md", "Morning of year 4.\n")
        append(repo, "images/requests/fx-004-morning.json", '{"id": "fx-004-morning", "campaign": "fx", "prompt": "dawn"}\n')
        append(repo, "campaigns/fx/state/images.md", "- year morning painting: approved, one per played year\n")
        assert run_quiet(check.main, ["fx", "3", "--root", repo, "--step", "7"])[0] == 0
        # the thread reached the year's end: the clock advances, with no play_day line
        open(clock, "w").write("campaign: fx\nyear: 4\nstatus: open\nseason_opens: 3\nplay_day: 2\n")
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo])
        assert code == 1 and "carries no play_day line" in out, out
        open(clock, "w").write("campaign: fx\nyear: 4\nstatus: open\nseason_opens: 3\n")
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo])
        assert code == 0, out
        assert check.clock_problems({"campaign": "fx", "year": "3", "status": "open", "season_opens": "3", "play_day": "1"})
        # a request in images/requests/ that images.md does not approve is a finding
        append(repo, "images/requests/fx-003-morning-2.json", '{"id": "fx-003-morning-2", "campaign": "fx", "prompt": "dawn"}\n')
        os.remove(os.path.join(repo, "images", "held", "fx-003-morning-2.json"))
        setclock("play_day: 2\n")
        os.remove(os.path.join(repo, "campaigns", "fx", "years", "004", "morning-story.md"))
        code, out, _ = run_quiet(check.main, ["fx", "3", "--root", repo, "--play-day", "1"])
        assert code == 1 and "does not approve it" in out and "it belongs in images/held/" in out, out
    d = tempfile.mkdtemp()
    try:
        t = os.path.join(d, "timing.md")
        open(t, "w").write("- 2026-12-01 01:40 clock waited: year 3 open, play day 2\n2026-12-02 waited\n")
        assert check.timing_conflicts(t) == []
        open(t, "a").write("2026-12-01 clock advanced: year 4 open\n")
        assert check.timing_conflicts(t) == ["timing: 2026-12-01 has both a clock-waited line and a clock advance"]
    finally:
        shutil.rmtree(d)


def test_build8_climb_by_naismith_both_ways():
    """Agent E's note on decision 3: a line that carries heights_ft prices its climb by Naismith's rule (an hour per
    2,000 feet climbed, a tenth of a ten-hour travel day; a descent adds nothing), stated in tools/pace.py, so a
    route takes longer uphill than down; no line without heights changes."""
    import pace
    assert pace.climb_days(2000) == 0.1 and pace.climb_days(-500) == 0 and pace.climb_days(2000, "river_up") == 0
    assert "Naismith" in pace.__doc__ and "2,000 feet" in pace.__doc__
    code, out, _ = run_quiet(pace.main, ["travel", "--mode", "walk", "--terrain", "road", "--miles", "40", "--climb", "4000"])
    assert "2.2 days" in out and "Naismith" in out, out
    w = travel_world()
    namer = mapt.Namer(w, None, True)
    _, flat = mapt.travel(w, "f03:start", "f03:end", "foot", ("f03",), namer)
    w["features"][2]["heights_ft"] = [500, 4500, 1500]   # up 4,000 feet from the west end to the ridge, down 3,000 to the east end
    assert mapt.check_world(w) == []
    text, east = mapt.travel(w, "f03:start", "f03:end", "foot", ("f03",), namer, show_ids=True)
    _, west = mapt.travel(w, "f03:end", "f03:start", "foot", ("f03",), namer)
    assert abs(east["days"] - (flat["days"] + 0.2)) < 0.01 and abs(west["days"] - (flat["days"] + 0.15)) < 0.01
    assert abs(east["miles"] - west["miles"]) < 0.01 and "4,000 feet climbed (0.20 days by Naismith's rule)" in text, text
    assert [s["climb_ft"] for s in east["segments"]] == [4000.0] and [s["climb_ft"] for s in west["segments"]] == [3000.0]
    # by boat no climb is added; a bank walk shares it by the miles
    assert all(s["climb_ft"] == 0 for s in mapt.travel(w, "f03:start", "f03:end", "boat", ("f03",), namer)[1]["segments"])
    bad = json.loads(json.dumps(w))
    bad["features"][2]["heights_ft"] = [500, 4500]
    assert any("heights_ft is a list of 3 heights" in p for p in mapt.check_world(bad))
    assert mapt.climb_feet({"coords": [[0, 0], [10, 0]], "heights_ft": [0, 100]}, 10, 0) == 0
    assert abs(mapt.climb_feet({"coords": [[0, 0], [10, 0]], "heights_ft": [0, 100]}, 2, 7) - 50) < 1e-9


def test_build8_check_fixes_flags_k_and_public_who():
    """Build 8 check findings 2 and 16: lockcheck skips a waiting night's years/NNN/flags-K.md as well as flags.md;
    roll.py --public takes only "dm" or "<party>, rolled by the dm" (R6), while is_dm() still reads older lines."""
    assert lockcheck.is_flags_file(os.path.join("S", "years", "005", "flags-2.md"))
    assert lockcheck.is_flags_file(os.path.join("P", "years", "005", "flags-12.md"))
    assert not lockcheck.is_flags_file(os.path.join("S", "years", "005", "flags-two.md"))
    assert not lockcheck.is_flags_file(os.path.join("S", "years", "005", "closing-2.md"))
    with tmpcopy() as repo:
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/001/flags-2.md", "Flag: [painting] is quoted from a release.\n")
        code, out, _ = lock(repo, "--places")
        assert code == 0, out
    for who in ("dm", "DM", "the god, rolled by the dm", "Kessan the reeve, rolled by the DM", "the world, rolled by the dm"):
        assert roll.public_who_ok(who), who
    for who in ("keeper for the dm", "dm keeper", ", rolled by the dm", "rolled by the dm", "the god rolled by the dm", "keeper"):
        assert not roll.public_who_ok(who), who
    assert roll.is_dm("dm keeper")   # older public lines are still read as the DM's
    d = tempfile.mkdtemp()
    real = roll.ROOT
    try:
        roll.ROOT = d
        code, _out, err = run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "keeper for the dm", "--what", "x"])
        assert code == 2 and "--public is the DM's open roll" in err, err
        code, _out, err = run_quiet(roll.main, ["--campaign", "zz", "--public", "--who", "the god, rolled by the dm",
                                                "--what", "the leap", "--factor", "strength=+10"])
        assert code == 0, err
        assert read_lines(os.path.join(d, "campaigns", "zz", "state", "rolls.jsonl"))[0]["id"] == "dm-0001"
    finally:
        roll.ROOT = real
        shutil.rmtree(d)
