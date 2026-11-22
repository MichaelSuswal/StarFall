# Applied changes, build 4

Each line names the run 03 change list items it applies.

## Engine side

- `CLAUDE.md`: 55 (a pull is always allowed in a run), 76 (the sealed `rulings.md` route).
- `engine/design/DESIGN.md`: 76 (2.7a), 45 and 54 with ruling 18's sibling on refused defaults (3.11 measure), 92 (3.11a names), 91 (4.7 technology), 90 (12.6a luck), 93 (10.1, 11.1d routes), 26 (10.7 unsaid wants), 87 (11.1a continent size), 80 and 86 (11.6), 29 (open list item marked done).
- `engine/design/CHANGELIST.md`: build 4 section, decisions 26, 45, 55, 76, 87, 86, 90, 91, 92, 93.
- `engine/creation/day1-world-survey.md`: 2, 3, 4, 5 (file layouts).
- `engine/creation/day2-the-god.md`: 18, 19, 20, 21, 22, 24, 25, 26, 27, 47.
- `engine/creation/day3-the-people.md`: 43, 44, 45, 46, 47, 48.
- `engine/roles/dm.md`: 5 (creation reading list once), 26, 76, 91, 92.
- `engine/roles/keeper.md`: 12 (creation reads, one commit form), 26, 76, 84, 90, 91, 92.
- `engine/roles/checker.md`: 26, 62 (spacing range), 76, 78 (three states, Michael-only flag pauses), 90 (neutrality check names luck).
- `engine/roles/npc-god.md`: 55, 76, 91, 92.
- `engine/roles/civ.md`: 76, 91.
- `engine/night/creation-nights.md`: 76, 78 (Michael-only flag at the deadline), 84, 90.
- `engine/night/night-turn.md`: 90, ruling 34 (sealed standing measure updated in pass two).
- `engine/rules/powers.md`: 23, 24, 25, 32, 33, 34, 39, 44, 54 as ruling 18, 66, 90; rulings 10 (as 90), the memory-loss enactment and the return scale (Night 2), the copied by-shape ask (Night 3a).
- `engine/rules/map.md`: 59, 74 as 93, 80, 81, 86, 87, 92, 93; ruling on `plane.count_roll`.
- `engine/rules/time-and-pace.md`: 93.
- `engine/rules/morning-story.md`: 80, 81.
- `engine/style/appearance-card.md`, `engine/style/house-style.md`: 82.
- `tests/creation-sim/README.md`: 76, build 4 note.

## Tools

- `tools/lockcheck.py`: 30 (number words before a unit or count noun pass; leak-allow.txt read as the checker writes it, quoted or not, with # comments inline or on their own line, and a longer allowed phrase that holds a hit exempts it), 60 (a name inside a longer map name is not warned on), 67 (each mystery Limit compared word for word with S/cast.md; headings and bold titles skipped by --places, as stamp skips them), 74 (lower-case map names and placeholder labels with no id warn), 83 (every request for the campaign, by file name, id or campaign field, in any request or held folder, scanned for leaks; scene and map requests checked for dashes), 87 (--places fails a continent outside the size rule).
- `tools/map.py`: 58 (smoke out to forty miles across region borders the same as inside; `describe --json`), 60 (`site` type; stamp handles placeholder labels and warns on a shared one; common-word name warnings in validate and stamp), 67 (stamp skips headings and bold mystery titles), 74 (no bearing at zero distance; yards under 0.2 miles; "the point is on it" for a road or river within half a mile), 81 (no region label until named: a told name, a report, or `"named": true` from `reveal --named`), 86 (`input_hash` in map-meta.json; `draw --if-changed`), 87 (validate measures the continent's narrowest and average width from the traced land and fails outside 600 and 800 to 1,200), 93 (`travel` by route and means, segment by segment, rates read from time-and-pace.md's quick reference and its Route line; `path` type; describe's neighbors and the gazetteer's "Travel by route" use it).
- `tools/paint.py`: 83 (a request is painted only when its campaign's state/images.md covers it; others are skipped and reported; `--check` lists both).
- `.github/workflows/paint.yml`: 83 (a check step runs `paint.py --check` before painting).
- `tests/tools/test_tools.py` and the `fx` fixture: tests for every item above; the fixture gets `cast.md` and 1 mile a pixel so the clean fixture passes the new checks.

## Sealed side

- `SPOILERS_do_not_open/keeper/creation-runbook.md`: 7, 8, 9, 10, 11, 12, 13 (pointer), 14, 16, 31, 35, 36, 37, 38, 39, 52, 53, 54 (one id per pending mark, wished names), 55, 56, 57 (count table, second placement roll), 58 (landing spots set before the brief), 61, 65, 68, 69, 70, 71, 75, 76, 78, 84, 87 (size at placement, plan and tracing; lock line), 90 (standing rule, set at 2.4 and 3a.1, used before rolls and in schedule weighting, template 7.14, lock line, neutrality), 91, 92, 93 (standing rule, tracing, records, lock line), 26 (sealed unsaid want read, applied only after a dated confirmation); rulings 1 to 8, 10, 11, 13 to 17, 20 to 25, 27, 30, 32, 35 to 41.
- `SPOILERS_do_not_open/keeper/npc-god-rubric.md`: 7 (what counts as a match), 8, 9, 10, 61, 90 (section 14); rulings 1 to 4, 26.
- `SPOILERS_do_not_open/keeper/survey-keeper-notes.md`: 13, 14.
- `SPOILERS_do_not_open/keeper/mystery-standard.md`: 67 (what answering means; cast limits word for word).
- `SPOILERS_do_not_open/keeper/deep-lore.md`: 68, 70; rulings 28, 29, 31, 34 (new section on setting a star's numbers).
- `SPOILERS_do_not_open/keeper/clue-design.md`: 70; ruling 33 (random table base and step).
- Not applied here: the self.md template half of 32 and the runbook half of 33 (items not assigned to agent K); the style block half of 57 and the template 7.7 scale line of 59 (assigned to agent E). Rulings 9, 12, 18 and 19 have engine homes (powers.md, DESIGN 3.11); the runbook only points to them.
