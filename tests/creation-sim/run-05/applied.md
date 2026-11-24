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

## Fixes from the check

2026-11-24. One line per line of `build-check.md`.

### Must-fix

1. `engine/rules/powers.md` (return paragraph), DESIGN 6.11 and CHANGELIST (item 20) now give only the option and who prices it. The older line of the same wording in `powers.md` (pricing list) and its CHANGELIST entry now read "A heavier price a god asks for ... is written as asked."
2. Runbook 3a.5: the player's people's home takes the player's Day 3 name as its map name, a common word or not, with `"named_by": "player"`, never in `aliases`, and stamp marks of a common word read and reworded where used in the ordinary sense; standing rules (Naming) say the same; `engine/rules/map.md` 1.2 names the `"named_by": "player"` mark.
3. `tools/lockcheck.py` `record_text` no longer reads `S/civs/<people>-sealed.md`; docstrings updated; the item 55 test now fails a name found only there and passes it from the sealed record.
4. The channel, written the same way in DESIGN 10.7, CHANGELIST, `dm.md`, `keeper.md`, `checker.md`, the Day 1, 2 and 3 guides and the runbook (standing rules, Sealed requests): the Keeper's reason as an indented line under the request's entry in `S/player/requests-answered.md`; the DM's dated agreement in `S/player/unsaid.md` beneath the request; the further line only after it. The DM still never writes `requests-answered.md`; the checker checks the order.

### Should-fix

1. Runbook section 4: `--releases` in the `--all` list, in the scripts paragraph and as a lock checklist line; 2.10, 3a.8 and 3b.9 run it; `checker.md` names it among the scripts.
2. `tests/tools/README.md`: build 6 notes and the build 6 fixes; `--releases` in the mode list.
3. `sealed-factors.md` (Weighting) and runbook 3b.6 name `tools/roll.py --weight <label>=<share>` as one weighted draw; the "on a `--die d100`" wording is gone.
4. Runbook 3a.5 sets `ground_ft` on each landing; 3b.8 checks describe's `Standing ground:` line for every landing release and the DM release; `map.md` 1.2 `landings` line names `at` and `ground_ft`.
5. `map.md` 1.4 now says the view is read from the region's kind (height, coast, floor), that `ground_ft` sets the eye's height and never the kind, and that a landing on other ground is traced as a region of its own. The tool is unchanged.
6. Runbook 4.1: the checker's read comes before the final leak scan, which runs after every fix the read asked for, as in the engine files.
7. `tools/lockcheck.py --places` warns on no bare map name in the files stamp skips (bracketed ids still checked), with a test; runbook standing rules (Places) and the lock line say so.
8. Day 2 guide: "What the DM has from Night 1" lists `requests-answered.md`; the Opening reads it and tells the player of each Day 1 sealed request; `dm.md`'s creation reading list adds it from Day 2.
9. Day 3 sealed requests reach the player in the first morning's closing (oog) block: Day 3 guide, `morning-story.md`, `creation-nights.md` Night 3a, runbook standing rules and 3b.8.
10. Runbook 1.8: a checkbox to answer Day 1 sealed requests.
11. Runbook 3a.1 luck line cites `sealed-factors.md` (What counts) as 2.4 does, with the priced bend counted there; `sealed-factors.md` cites both the Night 2 round (2.3) and 3a.1.
12. Runbook 3a.1 and the Day 3 guide: "designed, not yet serving" is a bend and gets the round so its cost is stated; it is never priced and buys nothing; `sealed-factors.md` says it counts nothing.
13. `checker.md`, runbook section 4 and `creation-nights.md`: the public `lock.md` carries no time; the time of each state goes in the sealed lock flags.
14. `morning-story.md` and runbook 4.1 point to `map-meta.json` `creation_names` and the draw command's note.
15. `morning-story.md` takes "Settled for you" from the `## Settled for you` section of `releases/000/dm.md`; runbook 3b.8 tells the Keeper to write it.
16. `dm.md` and the Day 2 guide give pace sections 1 to 5 and 7.
17. `engine/roles/npc-god.md`: the night session commits, or the orchestrator in a test run.

### Notes

1 to 9. Information only; no change.
10. Knacks (68): left as K wrote it, for Michael.
11. `map.md` 4.2 now says smoke shows only its told words, never a creation name; the `heard_name` and `player_aliases` docstrings in `tools/map.py` say a creation name is shown and noted, not heard.
12. `checker.md`: the first morning read is outside the lock and adds nothing to the locked world.
13. Left for Michael: whether the player's priced bend on Day 3 counts in the sealed factors is a decision.
14. `map.md`: the second 1.4 is now 1.5 (every reference to 1.4 meant the sight rule). No dashes added.

Runs: the suite, 72 passed. `lockcheck.py sim-05 --all`: 0 failures in every check; places 7 warnings (12 before; the files stamp skips are no longer warned on), leaks 1 (the public timing file, as before), releases 0 and 0. `map.py validate sim-05`: 0 problems, 0 warnings. sim-05 unchanged.
