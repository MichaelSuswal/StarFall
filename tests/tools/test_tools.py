"""Self-tests for the build 2 and build 3 tools: roll ids and die mappings, the map tool's knowledge
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
             ("There is one like me in the hills.", "number word")]
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
        append(repo, "campaigns/fx/state/rolls.jsonl", '{"what": "public"}\n')
        assert "public rolls log is not empty" in lock(repo, "--rolls")[1]


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
    assert not hits("No one came down the track.") and not hits("They help one another, as gods do.")
    assert not hits("Seven sheep. The god sleeps.")  # another sentence
    assert not hits("seven fields of barley and rye and oats and wheat lay by the god")  # more than six words apart
    assert hits("seven fields of barley and rye, the god")  # six words between
    assert not hits("seven fields of barley and rye by the god")  # seven words between
    assert not hits("thirteen gods")  # one to twelve only; the count of gods itself is its own check
    with tmpcopy() as repo:  # a number-word hit is exempted by its quoted phrase
        append(repo, "campaigns/fx/player/notes.md", "Snow fell two days running.\n")
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
        append(repo, "SPOILERS_do_not_open/campaigns/fx/years/000/flags.md", "[r77]\n")
        assert lock(repo, "--places")[0] == 1


# ---------------------------------------------------------------- build 3: paint

def test_paint_skips_held():
    import paint
    d = tempfile.mkdtemp()
    try:
        for rel in ("images/requests/a.json", "images/requests/held/b.json", "images/held/c.json",
                    "SPOILERS_do_not_open/images/requests/held/d.json"):
            path = os.path.join(d, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            json.dump({"id": os.path.splitext(os.path.basename(rel))[0], "prompt": "x"}, open(path, "w"))
        assert [r["id"] for _p, r, _t in paint.pending(d)] == ["a"]
        assert paint.is_held(os.path.join(d, "images/held/c.json"), d)
        assert not paint.is_held(os.path.join(d, "images/requests/a.json"), d)
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
    k = {"regions": {"r01": {"grade": "seen", "source": "landing", "year": 1}},
         "features": {"f02": {"grade": "reported", "source": "own sight", "year": 1, "told": {"name": "the quick water"}}}}
    t = mapt.describe(w, "r01", mapt.landing_point(land), k)
    # names: seen and told names only; every other name put plainly, in free text too
    assert "Vale of Osk" in t and "the quick water, quick" in t and "the quick water (river)" in t
    for sealed in ("Osk Water", "Oskby", "Shoulders", "White Teeth", "Hob Hole", "Farstead"):
        assert sealed not in t, sealed
    assert "a town (town), about half a mile south-east" in t and "a hill country (hill), lying east: 3 days on foot" in t
    assert "the quick water (river), about a mile east, about 4 miles of it in view, from the north-east to the south-east" in t
    # sight (map.md 1.4): the town, river and cave mouth within two miles of a valley floor; the village
    # 20 miles off in the same valley shows only as its smoke, walls or lights
    assert "from a valley floor or plain" in t and "a cave (cave), about half a mile south" in t
    assert "Farther off, seen only as smoke, walls or lights:\n- a village, about 20 miles east" in t
    # the ridges (top 2,800 over the 1,000-foot floor) are on the skyline 40 miles east
    assert "a hill country (hill), east, about 40 miles to its nearest edge: on the skyline" in t
    # the peaks (relief 10,000, reach about 125 miles) stand 80 miles off, behind the ridges or over them by the line
    assert "a mountain country" in t
    tn = mapt.describe(w, "r01", mapt.landing_point(land), k, all_names=True)
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
        assert meta["zoom"] == "landing" and meta["frames"]["surface"] == "A1:C3" and meta["frame_miles"]["surface"] == [1000, 1000]
        assert meta["labels_dropped"]["surface"] == 0
        # a tiny seen region still gets a sheet of at least LANDING_MIN_SIZE pixels, at its own scale bar
        tiny = {"r01": {"id": "r01", "grade": "seen", "polygon": [[500, 500], [504, 500], [504, 503]], "name": "x"}}
        r = mapt.landing_rect(tiny, {}, painting)
        assert r[2] - r[0] >= mapt.LANDING_MIN_SIZE and r[3] - r[1] >= mapt.LANDING_MIN_SIZE
        v = mapt.View(r)
        assert mapt.scale_bar(v, painting)[0] < mapt.scale_bar(mapt.View((0, 0, 1000, 800)), painting)[0]
