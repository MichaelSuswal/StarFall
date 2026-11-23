# Build 5 check

Independent check of build 5 (commits 28029a0 to 41c5f7d, diffed from 64fe2e9), against `build-plan.md` (decisions 1 to 9 and the specs), `changes.md`, run 03 item 94 and `applied.md`. Procedure only; no lore. Checked 2026-11-22.

Counts: 13 must-fix, 14 should-fix, 13 notes.

## Must-fix

1. `tests/tools/test_tools.py` (62): `test_paint_needs_images_md` fails; it still looks for the bare `- run: python3 tools/paint.py` line that the orchestrator's `paint.yml` change replaced with `--paint`. The suite is 58 passed, 1 failed, not 59 as `applied.md` says.
2. `engine/design/DESIGN.md` 3.3 and 3.9 (decision 7): knacks are given to the player's god only; every NPC god needs two or three small innate knacks from its own sealed backstory, sealed, found only in play, counted toward balance.
3. `engine/design/CHANGELIST.md` (decisions 7, 8, 9): the build 5 section records none of the three late decisions.
4. `engine/night/creation-nights.md` Night 2 Does (decision 7): knacks named for the player's god only.
5. `SPOILERS_do_not_open/keeper/creation-runbook.md` 2.6 and 2.7 (decision 7): balance counts the player's knacks only, and 2.7 draws knacks for the player only; NPC knacks from `backstory-secret.md`, written in `S/gods-sealed/<god>/hidden-powers.md`, are missing.
6. `SPOILERS_do_not_open/keeper/creation-runbook.md` section 4, NPC god line (decision 7): the lock checks two hidden powers per NPC god, not its knacks.
7. `engine/roles/npc-god.md`, `engine/roles/checker.md` check 4, `engine/roles/keeper.md` creation list (decision 7): each lists what an NPC god never receives, or what goes in `S/gods-sealed/<god>/`, as hidden powers, secret past, ceiling and growth, with no knacks.
8. `tools/lockcheck.py` `leak_terms` (decision 8): the open-talk exemption drops any sealed term found in a `## Player:` section, the sealed factor's name included; that one name must never be exempted, with a test.
9. `engine/roles/checker.md` leak paragraph (decision 8): "never a sealed term, wherever else it is written" needs the exception for the sealed factor's name, worded without naming it.
10. `SPOILERS_do_not_open/keeper/creation-runbook.md` section 4, with `engine/creation/day2-the-god.md` and `day3-the-people.md` (decision 8): no procedure for a hit on the sealed factor's name in the player's own open words (verbatim transcript, DM files that copy the player); `leak-allow.txt` may not hold a sealed term and the transcript cannot be reworded, so such a lock cannot pass. Write how "that conversation should stay sealed" is done.
11. `SPOILERS_do_not_open/keeper/survey-keeper-notes.md` rule 4 and its Even odds line (decision 9): a half median and a tied vote are still settled by a d100, and a quarter median rounds to the nearer whole; each must be decided by the Keeper by what makes the more interesting game, reason logged, no die.
12. `SPOILERS_do_not_open/keeper/survey-keeper-notes.md` Counting rule votes 1 and 3 (decision 9): a tie still "goes to a roll at even odds" and "a tie by even roll".
13. `SPOILERS_do_not_open/keeper/creation-runbook.md` standing rules Blends and votes, Table rolls, Rounding (decision 9): still "a half settled by an even-odds roll", "the survey blend's halves ... (an even-odds roll)", and the half-median roll among the d100 rolls.

## Should-fix

1. `engine/roles/checker.md` lock paragraph (58): the lock flags heading is "For review"; the runbook section 4 and log format call it `Rulings for review`.
2. `SPOILERS_do_not_open/keeper/creation-runbook.md` unsaid standing rule (24): it paraphrases the header; quote "Written by the DM. Read by the DM, the Keeper and the checker." as `day2-the-god.md` does, and say whether the header stands when the orchestrator writes the file in a test run.
3. `engine/creation/day1-world-survey.md` (run 03 item 94): `mirror.md` has no header or layout, where `unsaid.md` has both.
4. `tools/lockcheck.py` with `engine/roles/dm.md` and `checker.md` check 4 (46): names from `knowledge.md` pass only in that file; a mortal saying one in the morning story fails the scan unless the told name is recorded in map knowledge first. Name that order or extend the scan.
5. `engine/roles/npc-god.md` and `engine/night/night-turn.md` step 1 (56): "your first, at Year 1, carries your landing release" reads as `releases/001/`; name `S/releases/000/<label>-landing.md` in npc-god.md, and say step 1 reads it in place of last year's release.
6. `SPOILERS_do_not_open/keeper/sealed-factors.md` DM rolls, Record (66): the overrule is to be noted "in the sealed roll log", but `tools/roll.py` has no note option and only it writes that log; say how, or keep the note to the keeper log.
7. `engine/design/DESIGN.md` 12.6 and `engine/roles/dm.md` (66): "the DM rolls in the open" sits beside "dice are hidden from the player"; say it means the public roll log with stated odds.
8. `SPOILERS_do_not_open/keeper/creation-runbook.md` 1.5 and 1.7 (68, 9): the world draft's underground line has no set form; name `Underground: <yes, what>` and `Underground: none`, which `tools/map.py validate` reads. Validate also does not fail the converse, a layer in `map.json` when the decision is none.
9. `tools/paint.py` (62): the no-argument painting fallback under `GITHUB_ACTIONS` and its docstring ("until it is changed to call --paint") are stale now `paint.yml` calls `--paint`; with no arguments it should only report, as the item says.
10. `SPOILERS_do_not_open/keeper/creation-runbook.md` Time rule, `engine/night/creation-nights.md`, `engine/night/night-turn.md` (10): `tools/stamp_time.py` is named in no file an agent reads; all still say `TZ=America/Los_Angeles date`.
11. `SPOILERS_do_not_open/keeper/creation-runbook.md` 4.1 (7): "Commit, pull with rebase, push, and log that Night 3 closed" writes the log line after the push, against the one close order.
12. `SPOILERS_do_not_open/keeper/creation-runbook.md` Commit forms (7, 51): "the only forms" has none for the `night-blocked.md` commit (3a.4), the Year 1 clock commit (4.1), or the checker's `lock.md` and `LOCKED.md` commits (`checker.md`).
13. `engine/rules/powers.md` Hidden powers (decision 7, item 94): no line on how a knack surfaces and reaches the card; the section speaks of hidden powers only.
14. `engine/style/house-style.md` (67): "consider not painting a layer that is one small gallery" is not answered either way.

## Notes

1. `CLAUDE.md`, `npc-god.md` (25): `git pull --rebase --autostash` without `origin main`, where the runbook and the release line carry it; same effect, different text.
2. 58 (decision 1): CLAUDE.md, DESIGN 2.7a, 15.2 and 15.5, creation-nights, keeper, checker, dm, night-turn, scheduled-prompt, README and runbook standing rules, 4 and 6 agree; the paused-lock wake notice is gone; the only owner waits left are the repaint and held image requests, which are spending, as the spec allows.
3. 66 (decision 2): DESIGN 12.6, dm.md, keeper.md, night-turn pass two, the runbook standing rule and `sealed-factors.md` agree; checker line 5 added.
4. 13, 30, 32 (decision 3): the `SEALED:` reply and the transcript line "(One more answer was given privately, for the sealed record.)" read the same in DESIGN 10.7, dm.md, day2, day3 and the runbook; the "check with the player before acting" mark is in dm, keeper, civ, checker and the runbook.
5. 46: the path `civs/<people>/knowledge.md` is the same in DESIGN 11.4, map.md, dm, keeper, civ, checker, night-turn, creation-nights 3a, runbook 3a.7, 3b.8 and the lock line, and `lockcheck.py` matches it.
6. 56: creation-nights 3b, keeper.md, runbook 3b Writes, 3b.8, 3b.9 and the lock line, and night-turn setup agree on `S/releases/000/<label>-landing.md`.
7. 68: DESIGN 11.1 and 11.2, map.md 1.1, 1.2, 1.3 and 4.2, creation-nights 1 and 3a, house-style, survey notes Q12, runbook 1.5, 3a.3 to 3a.5 and the lock line, and validate agree on `under-N`, `depth`, `uNN` and the data ruling below ground.
8. Run 03 item 94 (decision 6): the Day 1 question is word for word in DESIGN 3.4c and day1; the `Mode:` line is in the survey layout and the Night 2 Reads; history reading is the DM's alone, on Day 1; the mirror survey is a `SEALED:` reply; Night 2 draws by mode; `person.md` is in the tests README, day1 and dm.md.
9. Public engine files (decision 2): engine, README, CLAUDE.md and tools name only "the sealed factors"; no description of the mechanic. No em or en dash in any changed file.
10. `python3 tests/tools/run.py`: 58 passed, 1 failed (must-fix 1).
11. `python3 tools/lockcheck.py sim-04 --all`: 0 failures in every check, 16 places warnings, unchanged from before the build.
12. `python3 tools/map.py validate sim-04`: 86 problems (85 region overlaps under item 53, one underground with no layer under item 68) and one gap warning. These are new failures on the locked run 04 record, expected from items 53 and 68; nothing was changed. Run 04's own public files would also hit the sealed factor's name if its list were updated, which shows must-fix 10 is a likely case.
13. Every run 04 item the plan puts in is applied; 37 went in both as a rubric rule and as a setup note; agent K's list of unassigned rulings left for Michael stands. `npc-god-rubric.md` section 12's variety-table tie is still settled by a roll; decision 9 covers the survey blend only, so it is left as is.
