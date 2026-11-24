# Build 6: what was applied

## Sealed side

- `SPOILERS_do_not_open/keeper/creation-runbook.md`: items 6, 8, 10, 11, 21, 27, 28, 29, 31, 32, 34, 35, 36, 48, 50, 51, 54, 57, 60, 63, 65, 66, 67, 72, 73, 74, 80, 81; templates 7.6 (35), 7.10 (68), 7.13 (30), new 7.15 (60); every `P/state/timing.md` changed to `S/state/timing.md` (74).
- `SPOILERS_do_not_open/keeper/npc-god-rubric.md`: items 7, 9, 30, 51.
- `SPOILERS_do_not_open/keeper/survey-keeper-notes.md`: item 6.
- `SPOILERS_do_not_open/keeper/sealed-factors.md`: items 20, 31, 58, 63.

## Engine side

Agent E, 2026-11-24.

- `engine/design/DESIGN.md`: 3.3 78; 3.8 7; 3.8a 51; 4.10 67 (far travelers); 6.11 20, 16, 22; 8.1 67 (season); 10.7 14, 32; 11.4 55; 12.2a 74; 12.6 62.
- `engine/design/CHANGELIST.md`: build 6 section: 7, 20, 32, 51, 67, 74, 78, and 14 with 43 and 64, 76, 22.
- `engine/creation/day1-world-survey.md`: 2, 3 (with 45), 4, 14, 15.
- `engine/creation/day2-the-god.md`: 14, 15, 17, 24, 32, 43, 64 (new Sealed answers section).
- `engine/creation/day3-the-people.md`: 3 and 45, 21, 32, 33, 40, 41, 42, 43, 44, 46 (close file templates), 47, 53, 14 and 64 (Sealed answers).
- `engine/roles/dm.md`: 14, 17, 32.
- `engine/roles/keeper.md`: 32, 55, 62, 66, 74 (owns the sealed timing file), 80, 81.
- `engine/roles/checker.md`: 32, 38 (checker note), 55, 81.
- `engine/roles/civ.md`: 55, 66.
- `engine/roles/npc-god.md`: 36 (retry a failed pull once; the god does not commit).
- `engine/night/creation-nights.md`: 74, and to match 32, 78, 80, 81.
- `engine/night/night-turn.md`: 74, 62.
- `engine/night/scheduled-prompt.md`: 74, 75.
- `engine/rules/powers.md`: 16, 18, 19 (claimed ground: nearest standing boundary mark of anyone's setting, the run 05 ruling), 20, 22, 24 (Bynames line).
- `engine/rules/map.md`: 52, 76.
- `engine/rules/morning-story.md`: 76 (to match), 77, 78, 80, 81.
- `engine/style/house-style.md`: 79.
- `tests/creation-sim/README.md`: 26, 36, 74.
- `CLAUDE.md`: no change needed.

## Tools

Agent T, 2026-11-24.

- `tools/lockcheck.py`: 23 (fractions are no count), 37 (new `--releases` check: releases and the Day 3 brief against the world draft's scarcities, warned; kept sealed terms, failed), 55 (another people's name in a knowledge file only if told in their record), 71 (cast `Mysteries:` pointers against each mystery's yes or no), 74 (a public `P/state/timing.md` is warned on; no ordinal scan in public), and 52 (a map name with `named_by: player` is the player's own).
- `tools/map.py`: 52 (`"named_by": "player"` on the home's element; validate checks it), 56 (stamp skips god-written files and the keeper log), 61 (describe finds the god's knowledge file by label, reports the standing height from an optional landing `ground_ft`, lists wood edges), 76 (landing sheet draws a line only as far as seen from the landing; told words over a creation name for a rumor or report; creation names shown are noted for the (oog) line).
- `tools/roll.py`: 63 (weighted draw, `--weight name=N`, bands logged).
- `tools/check.py`: 74 (reads the sealed `S/state/timing.md`, falling back to the public one for older campaigns), at the coordinator's word.
- `tests/tools/test_tools.py`: one test per item above (10 new; 71 in all, all passing).
- Runs: `lockcheck.py sim-05 --all` passes as before, with one new warning (its public timing file, item 74) and the new `releases` line at 0 and 0; `map.py validate sim-05` unchanged (0 problems, 0 warnings).
