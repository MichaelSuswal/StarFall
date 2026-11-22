# Tools self-tests

Run either way (Pillow and the standard library only):

```
python3 -m pytest tests/tools
python3 tests/tools/run.py
```

`test_tools.py` covers roll ids, every die mapping including the plain `d100`, and the
refusal to roll without `--campaign` or `--log` (`tools/roll.py`), the map tool's
grid, validation, reveal rules, migration, drawing and gazetteer (`tools/map.py`),
every lockcheck mode (`tools/lockcheck.py`), and in `tools/check.py` the clock rules
(`creation_night` 1, 2, 3a or 3b; a quiet exit 0 during creation), the engage rule
(a year that turned needs `player/decisions-NNN.md` or a waited note), and the timing rule
(only lines that start with a Pacific date count; only "clock advanced" is an advance).

The map tool's `validate` fails a map with no `miles_per_pixel` (the default is 2.5, a
continent), a region missing `elevation`, `water`, `climate` or `neighbors`, and plane ids
that are not unique `pNN`. `reveal` refuses a rumor with no told name or no cell. The map
log and `map-meta.json` are dated in Pacific. The fixture's mysteries follow runbook
template 7.8: one epic, two long, three short, one of them a being with a `Limit:` line. The fixture campaign `fx` lives in `fixtures/repo/`, laid out like the
repository (`SPOILERS_do_not_open/campaigns/fx/` and `campaigns/fx/`). Its names are
invented for the tests. The clean fixture passes every lockcheck; each test copies it to a
temporary folder and breaks one thing. Paintings are made at test time.

Build 3 adds: `map.py stamp` (idempotent, counts, skips the flags file, never the public
folder), `map.py describe` (names only as learned, free text scrubbed, the sight rule's worked
figures, the skyline and higher ground between, caves found only by looking, the command line),
one-decimal coordinates, the `--zoom landing` frame and its scale bar, label placement (no two
label groups overlap, none covers a mark or leaves the frame, the highest priority keeps its
place), and the gazetteer's told distances for reported regions; in lockcheck the sealed-terms
file as the primary list (case and all, the article rule, a missing file fails, prose guesses
warn), number words near god terms (the six-word window, sentences, "one" never counted, the phrase
exemption), case-sensitive mystery titles, the `Answers questions: yes|no` field, and the
skipping of `lock-flags*.md` in every mode; and in paint.py that held requests are never painted.
The fixture carries `S/sealed-terms.txt` and an `Answers questions:` line on every mystery.

Build 4 adds: `map.py travel` (a trip priced segment by segment by route and means, `--by
foot|horse|wagon|boat`, `--via` routes, the half-mile rule, a line refused as a place, the `path`
type at the rough-ground row, rates read from `engine/rules/time-and-pace.md`); the continent
measure in `validate` (narrowest and average caliper widths of the traced land, failing outside
600 and 800 to 1,200; a thin neck does not lower narrowest, the overall shape being the reading);
`draw --if-changed` (the inputs hash in `map-meta.json`; an unchanged map is kept); `reveal
--named` and region labels (a seen region is labeled, and named in the gazetteer, describe and
travel, only with `"named": true` or a told name; otherwise it is shown by its id and terrain);
the gazetteer's travel between seen regions priced by open-ground travel, never the hand-set
neighbor days, and its travel by route; `aliases` (the schema in `validate`, the god's own and
known aliases in the gazetteer, alias names stamped and known to `--places`); the `site` type,
placeholder labels and common-word warnings; and in paint.py that a request is painted only when
its campaign's `state/images.md` covers it, the play lines (`year morning painting: approved, one
per played year`, `player-asked painting: approved, up to two a day`) covering the real
`<campaign>-NNN-morning` and `<campaign>-NNN-request-K` ids, with the count per year enforced (a
painting already made counts). In lockcheck: number words before a unit or count noun pass,
`leak-allow.txt` read as the checker writes it, a name inside a longer map name not warned on,
mystery Limits compared word for word with `S/cast.md`, lower-case map names and placeholder
labels with no id warned, every image request for the campaign scanned for leaks and dashes, and
`--places` failing a continent outside the size rule. The fixture has `cast.md` and 1 mile a
pixel so the clean fixture passes the new checks.

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

Before the continuity checker writes `LOCKED.md`, run `python3 tools/lockcheck.py <campaign> --all` from the repository root (or `--places`, `--leaks`, `--mysteries`, `--rolls`, `--dashes` one at a time while fixing). It reads `SPOILERS_do_not_open/campaigns/<campaign>/` and `campaigns/<campaign>/`, prints one line per finding and a count line per check, and exits 1 on any failure; warnings (names written without an id, old reroll lines) do not fail but should be read. Findings name sealed terms, so the full output stays in the sealed session or the keeper log, never in a public file; for a record outside the spoiler folder use `--counts-only`. A leak hit that is an ordinary word gets a line in `SPOILERS_do_not_open/campaigns/<campaign>/leak-allow.txt` only after the checker has read the public line and agreed it reveals nothing. `--leaks` reads `S/sealed-terms.txt` (the Keeper's list) as its primary sealed list and fails a campaign without one; the older guesses from prose only warn, and a warning names a term to add to the file if it is sealed. A number-word hit near a god term that the checker has read and agreed reveals nothing is exempted by its quoted phrase in `leak-allow.txt`. `--mysteries` reads each mystery's `Answers questions: yes|no` line and requires a `Limit:` line on yes; the checker still reads every Truth and Body for a being marked no that does answer. Every mode skips the checker's own `lock-flags*.md`. Lock only when every check shows 0 failures.
