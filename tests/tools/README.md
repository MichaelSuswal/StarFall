# Tools self-tests

Run either way (Pillow and the standard library only):

```
python3 -m pytest tests/tools
python3 tests/tools/run.py
```

`test_tools.py` covers roll ids and every die mapping (`tools/roll.py`), the map tool's
grid, validation, reveal rules, migration, drawing and gazetteer (`tools/map.py`),
every lockcheck mode (`tools/lockcheck.py`), and the clock rules and the timing.md
waited rule in `tools/check.py`. The fixture campaign `fx` lives in `fixtures/repo/`, laid out like the
repository (`SPOILERS_do_not_open/campaigns/fx/` and `campaigns/fx/`). Its names are
invented for the tests. The clean fixture passes every lockcheck; each test copies it to a
temporary folder and breaks one thing. Paintings are made at test time.

`lockcheck-sim-01.txt` records what lockcheck found on sim-01, as counts only.

## Migration from the sim-01 and dryrun formats

What still works without change:

- `roll.py`: old log lines have no `id`; lockcheck and check.py read the line number as the id
  (`r-0012` is line 12), which is what the sim-01 Keeper cited. New lines continue the count.
- `map.py draw` and `gazetteer` still read a `painting.grid_cell_px` grid (sim-01 and dryrun
  draw on their old 8 by 8 grid) and still draw an older rumor's `told.near`.
- Name-slug ids still draw and reveal; `reveal` prints a note, and `validate` and
  `lockcheck --places` fail them as not opaque.

What a campaign needs to reach the build 2 rules:

1. `map.json`: set `painting.grid` to `{"cols": 5, "rows": 4}` (or the sheet's grid) and drop
   `grid_cell_px`; give regions, features and underground features opaque ids (`r01`, `f03`,
   `u01`) and rename them everywhere they are cited in sealed files and in the player's
   knowledge file. The tool does not rename ids; that is a Keeper change to sealed files.
2. `player/map-knowledge.json`: `python3 tools/map.py migrate <campaign>` turns rumor `near`
   pixels into `told.cell` (regions and features alike) and drops `told` from seen entries.
   Reported `told` shapes in pixels stay.
3. `python3 tools/map.py validate <campaign>` then reports 0 problems.

The tool and its rules are in the docstrings of `tools/map.py` and `tools/lockcheck.py`.

## Running the lockcheck before a lock

Before the continuity checker writes `LOCKED.md`, run `python3 tools/lockcheck.py <campaign> --all` from the repository root (or `--places`, `--leaks`, `--mysteries`, `--rolls`, `--dashes` one at a time while fixing). It reads `SPOILERS_do_not_open/campaigns/<campaign>/` and `campaigns/<campaign>/`, prints one line per finding and a count line per check, and exits 1 on any failure; warnings (names written without an id, old reroll lines) do not fail but should be read. Findings name sealed terms, so the full output stays in the sealed session or the keeper log, never in a public file; for a record outside the spoiler folder use `--counts-only`. A leak hit that is an ordinary word gets a line in `SPOILERS_do_not_open/campaigns/<campaign>/leak-allow.txt` only after the checker has read the public line and agreed it reveals nothing. Lock only when every check shows 0 failures.
