# Tools self-tests

Run either way (Pillow and the standard library only):

```
python3 -m pytest tests/tools
python3 tests/tools/run.py
```

`test_tools.py` covers roll ids and every die mapping (`tools/roll.py`), the map tool's
grid, validation, reveal rules, migration, drawing and gazetteer (`tools/map.py`),
every lockcheck mode (`tools/lockcheck.py`), and the clock and waited rules in
`tools/check.py`. The fixture campaign `fx` lives in `fixtures/repo/`, laid out like the
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
   pixels into `told.cell`, drops `told` from seen entries, and removes rumored regions (a
   region id appears only when seen or reported). Reported `told` shapes in pixels stay.
3. `python3 tools/map.py validate <campaign>` then reports 0 problems.

The tool and its rules are in the docstrings of `tools/map.py` and `tools/lockcheck.py`.
