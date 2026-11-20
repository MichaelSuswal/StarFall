"""Self-tests for the build 2 tools: roll ids and die mappings, the map tool's knowledge
rules and drawing, lockcheck on the fixture campaign, and check.py's waited rule.

Run with `python3 -m pytest tests/tools` or `python3 tests/tools/run.py`.
Only the standard library and Pillow are needed.
"""
import contextlib
import io
import json
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
                              "--cell", "B2", "--force", "chart proved false")
        assert code == 0
        log = open(os.path.join(os.path.dirname(know_p), "map-log.md")).read()
        assert "feature f05 | none -> rumored" in log and "forced: chart proved false" in log
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
        assert "6 days" in g and "The Chalk Way" in g


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


def test_lockcheck_leaks():
    pub = "campaigns/fx/player/notes.md"
    cases = [("Vessaline walks the shore.", "god name"),
             ("They speak of god-tide.", "god label"),
             ("There are two other gods.", "god count"),
             ("Beyond lies Hollow Moor.", "unknown place"),
             ("The bell hum came on 5 nights.", "phenomenon count"),
             ("The ceiling here is 73.", "star value"),
             ("A drowned crystal orchard, they say.", "star value"),
             ("They whisper of the silent bell.", "mystery title"),
             ("Remember the Founders' Quarrel.", "schedule title")]
    for text, kind in cases:
        with tmpcopy() as repo:
            append(repo, pub, text + "\n")
            code, out, _ = lock(repo, "--leaks")
            assert code == 1 and kind in out, (text, out)
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
               "\n## SHORT 1. The Lost Ewe\n\n**Truth.** A fox.\n\n**Body.** The fold.\n\n**Clues.** Tufts of wool.\n\n**Branches.** Hunt it.\n")
        code, out, _ = lock(repo, "--mysteries")
        assert code == 1 and "The Lost Ewe" in out
        assert "Cost if ignored" in out and "Never found" in out and "readings" in out and "world does" in out
        assert "The Silent Bell" not in out


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
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"what": "public"}\n')
        assert "public rolls log is not empty" in lock(repo, "--rolls")[1]


# ---------------------------------------------------------------- check.py

def test_check_waited_and_clock():
    with tmpcopy() as repo:
        base = os.path.join(repo, "campaigns", "fx")
        append(repo, "campaigns/fx/years/001/waited-2026-11-20.md", "The world waited.\n")
        append(repo, "campaigns/fx/state/timing.md",
               "## Year 1, 2026-11-20 (Pacific)\n- 01:45 no decisions file; the world waited.\n"
               "## Year 1, 2026-11-21 (Pacific)\n- 01:45 decisions found.\n- 03:10 clock advanced, year 2 open.\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 0, out  # waited: clock stays on year 1, no outputs expected, dates differ
        append(repo, "campaigns/fx/state/timing.md", "## 2026-11-22\n- 01:45 the world waited.\n- 03:00 year 2 open\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert code == 1 and "timing: 2026-11-22 has both a waited line and a clock advance" in out
        assert "2026-11-20" not in out and "2026-11-21" not in out
        with open(os.path.join(base, "state", "clock.md"), "w") as f:
            f.write("campaign: fx\nyear: 0\nstatus: creation\nseason_opens: spring\n")
        code, out, _ = run_quiet(check.main, ["fx", "1", "--root", repo])
        assert "creation needs creation_night" in out
    assert check.clock_problems({"campaign": "x", "year": "0", "status": "creation", "creation_night": "2", "season_opens": "s"}) == []
    assert check.clock_problems({"campaign": "x", "year": "1", "status": "open", "creation_night": "2", "season_opens": "s"})
