# Build 4 check

Independent check of build 4 (commits db93099, f7dbc2f, f65cab9, 7e37dfb against 3391fb5), by an agent that did none of the work. Read: CLAUDE.md, build-plan.md, changes.md, applied.md, and every changed file's diff, sealed side included. Checked 2026-11-21.

## Runs

- Test suite: 38 passed, 0 failed (`python3 -m pytest tests/tools` and `python3 tests/tools/run.py`).
- `python3 tools/lockcheck.py sim-03 --all`: exit 1. places 1 failure (continent average about 1,845 miles, outside 800 to 1,200) and 13 warnings (map names written in lower case with no id); leaks, mysteries, rolls, dashes 0. The failure is the new continent rule (item 87), as expected; sim-03 is locked and was not changed.
- `python3 tools/map.py validate sim-03`: 1 problem (the same continent average), 2 warnings (region and feature names that are common words). Narrowest about 1,440 miles passes; the traced land runs to three sheet edges.

## Must-fix

1. `engine/rules/map.md` 1.2 and `tools/map.py` (item 81): 1.2 still says the knowledge file "learns names only through `told` and through seeing", against 4.2's new rule that seen ground with no heard name is unlabeled; and the gazetteer (`gazetteer()`) and `Namer` (describe, travel) still print a seen region's true name without `named`, so the name the sheet hides reaches the player another way.
2. `tools/paint.py` `covered()` (item 83, images.md play lines): player-asked request ids (`<campaign>-NNN-request-1`, house-style.md) get no kind words, so the line `player-asked painting: approved, up to two a day` that creation-nights.md prescribes never covers them; every player-asked painting would be skipped (tested on a scratch copy).
3. `SPOILERS_do_not_open/keeper/creation-runbook.md` template 7.8 (item 74): the mystery template field cross-checking each cost against the agreed weaknesses and ledger rulings is not applied anywhere (no agent was assigned it).
4. `engine/design/DESIGN.md` 12.6a against 10.5 and 12.6 (item 90): odds are stated to the player before commitment and argued with the DM, but luck shifts the odds out of sight of both; no line says the stated odds exclude luck or how the logged odds and the stated odds differ.

## Should-fix

1. `creation-runbook.md` section 4 (item 65): says the leak allow file "is in the checker's Writes for the lock", but section 4 has no Writes line; add one naming `S/leak-allow.txt` and the lock files.
2. `creation-runbook.md` section 4 (items 65, 78): the checker runs `lockcheck.py` with `--places --mysteries --leaks`; checker.md and creation-nights.md say `--all` (which adds rolls and dashes).
3. `engine/roles/keeper.md` (item 12): "one form, `Creation night N: <stage>`"; the runbook gives two forms, `Creation night N: <name> closed` and `Creation night 3b: <name> ready for lock`.
4. `creation-runbook.md` template 7.7 (item 59): the scale line the 3a.1 checkbox requires is not in the template text.
5. `creation-runbook.md` 3b.8 `P/world/world.md` checkbox (item 81): the landing given by grid cell only, never a region centroid cell, is in morning-story.md but not in the Keeper's step that writes the file.
6. `creation-runbook.md` 2.1 (items 31, 91): still lists technology among the facts "the DM states to the player on Day 2", but no Day 2 guide line or world-rules template 7.9 gives the DM the line; the Keeper's own statement now settles it, so the 2.1 wording should say so.
7. `DESIGN.md` 12.6a, `keeper.md`, runbook standing rules (item 90): how a luck shift meets the 5 to 95 clamp of 12.6 ("never past certain" is not the clamp), and what happens in a contest between two gods with luck, are unstated.
8. `dm.md` and `DESIGN.md` 10.7 against `keeper.md`, runbook and `checker.md` 5 (item 26): the DM confirms "before acting" (read as every time), while the Keeper and checker accept any confirmation within three played years; say which.
9. `tools/map.py`, `tools/lockcheck.py` (item 92): `aliases` has no schema check in validate (any shape passes), the player gazetteer prints no aliases though map.md 1.2 says it records them, and stamp and `--places` do not know alias names.
10. `tools/paint.py` (item 83): the counts in the play lines ("one per played year", "up to two a day") are not enforced; any number of matching requests is covered.
11. `tools/map.py` `continent_measure` (item 87): widths are caliper widths of the convex hull, so a narrow neck or deep bay never lowers "narrowest"; land running off the sheet edge is only noted, not warned, though DESIGN 11.1a puts the continent on one sheet. Confirm this reading with Michael.
12. `creation-runbook.md` lock checklist "Gods spaced evenly" (item 62): does not carry the range checker.md 9 now gives.
13. `engine/rules/map.md` 1.2 and DESIGN 11.1d (item 93): region `neighbors` still carry travel days "at the cross-country rate", set by hand, against 5.1's "no agent prices a trip by the straight line or by eye"; say they come from `map.py travel` over open ground or are a rough guide only.
14. `engine/roles/checker.md` 9 (item 93): does not name the travel-time check against `map.py travel` that the runbook's lock line requires.
15. `engine/creation/day2-the-god.md` (item 22): the provisional-pricing paragraph sits unindented between checklist items 7 and 8, breaking the numbered list.
16. `tests/tools/README.md` (build 4 tools items): no notes for travel, continent, `--if-changed`, `--named`, paint coverage or the new lockcheck checks.

## Notes

1. `engine/style/house-style.md` line 55 (item 26): "The DM cannot read that folder" has no mention of the `unsaid.md` exception; harmless in context.
2. `engine/rules/time-and-pace.md` (item 93): wagon uses the ox-cart table as the spec says; hill, highland, plain, desert and tundra price as rough ground; the snow row is never reached by any terrain word.
3. `tools/map.py` `inputs_hash` (item 86): hashes the whole sealed map and the tool's code, so a Keeper edit to map.json or a tool update forces a redraw with no change to the player's knowledge; safe, wider than the rule.
4. `tools/lockcheck.py` `UNIT_NOUNS` (item 30): general nouns (things, ways, times, questions, points) exempt a number word before them; a count phrase built on them passes silently.
5. Rulings route (item 76): named consistently in CLAUDE.md, DESIGN 2.7a, creation-nights.md, the runbook, all five role files and the test README; path and "only the orchestrator writes it" agree.
6. Luck (item 90): 0 to +5, two per refused power, one per extra priced step, 5 points a step on d100, one step toward 0 per tier, never for craft or technology; agrees across DESIGN 12.6a, keeper.md, night-turn.md, powers.md, checker.md, runbook and rubric 14, and template 7.14 exists.
7. Travel (item 93): the `travel` CLI, its `--by` choices, `--via` and the half-mile rule agree across map.md 5.1, time-and-pace.md, the runbook and map.py; rates read from the quick reference match `tools/pace.py`.
8. Continent (item 87): 600 narrowest and 800 to 1,200 average agree in DESIGN 11.1a, map.md, the runbook (draft, plan, tracing, lock) and map.py; lockcheck `--places` fails on it.
9. Technology (item 91) and names (item 92): engine text, roles, runbook naming rule and template 7.5 agree; the runbook keeps "a name a god gives its own people or home, as a wish, is a name given", which fits ruling 92.
10. Unsaid want (item 26): sealed path, DM exception, readers (Keeper, checker; no NPC god or civ agent) agree in DESIGN 10.7, dm.md, keeper.md, checker.md, day2 guide and runbook.
11. Redraw (item 86) and landing scale line (item 80): `--if-changed`, `input_hash` and `frame_miles` in map-meta.json match map.md 4.1, 4.6, morning-story.md and DESIGN 11.6.
12. Item 57: "allow marked sites smaller than a hill" was resolved as data only, not painted (map.md 1.2); not the wording of the item, but consistent.
13. Item 32: the second return rung is marked under review in powers.md, not repriced.
14. Placement plan "many weeks' walk" between eight seats may not hold on a continent about 1,000 miles across; worth watching in run 04.
15. No em or en dash in any changed file.

Counts: 4 must-fix, 16 should-fix, 15 notes.
