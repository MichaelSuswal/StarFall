# Build 6: independent check

Checker: an agent that did none of the build. Checked against `build-plan.md` (decisions 1 to 7 and the shared specifications), `changes.md`, `applied.md`, and the diff from e5f83df to 9739ec0. Procedure only; no lore, and the hidden mechanic is named only as "the sealed factors".

Counts: 4 must-fix, 17 should-fix, 14 notes.

## Must-fix

1. `engine/rules/powers.md` (return paragraph), `engine/design/DESIGN.md` 6.11, `engine/design/CHANGELIST.md` (item 20): the public wording for the slower return borrows the counting language of the sealed factors file ("a heavier price taken willingly", "buys nothing on the card"), which `sealed-factors.md` (Secrecy) bars from any engine file. The public text should give only the option and who prices it.
2. `SPOILERS_do_not_open/keeper/creation-runbook.md` 3a.5 (the "one map name" line) and standing rules (Naming), `engine/rules/map.md` 1.2 (item 52): no Keeper text says to set `"named_by": "player"` on the home's element, and 3a.5 still sends a home named by a common word to `aliases`. That is the run 05 case, so the tool's change cannot take effect.
3. `tools/lockcheck.py` `record_text` (item 55): it counts `S/civs/<people>-sealed.md` as told to the people, but that file is the world's side and its own header says it is told to no one. A people's name found only there would pass into the public `knowledge.md`.
4. `engine/roles/dm.md`, `engine/roles/keeper.md`, `engine/creation/day2-the-god.md`, runbook standing rules (Sealed requests) (item 32, decision 3): no file says where the Keeper puts its reason to the DM or where the DM writes its agreement. dm.md says the DM never writes `requests-answered.md`, and the keeper log, where both must be logged, is closed to the DM. Michael's exception cannot run as written.

## Should-fix

1. `creation-runbook.md` section 4 (item 37): the `--all` list, the "scripts check only what they check" paragraph and the lock checklist all omit `--releases`, and no night's checklist runs it.
2. `tests/tools/README.md` (items 37, 52, 61, 63, 74): there are no build 6 notes, and the mode list omits `--releases`.
3. `SPOILERS_do_not_open/keeper/sealed-factors.md` (Weighting) and `creation-runbook.md` 3b.6 (item 63): neither names `tools/roll.py --weight name=N`, and the method still reads "on a `--die d100`".
4. `creation-runbook.md` 3a (landings) and 3b.8, `engine/rules/map.md` 1.2 `landings` line (item 61): nothing tells the Keeper to set `ground_ft` on a landing. Without it, describe reports the height as not given. The line belongs where 3a writes each landing point into `map.json`, and the 3b.8 describe step should check it.
5. `engine/rules/map.md` 1.4 against `tools/map.py` describe (item 61): 1.4 chooses the view by the ground the god stands on (floor or height). The tool chooses it by the region's kind, which sets the skyline cap, and applies `ground_ft` to eye height only, so a `ground_ft` that disagrees with the region's kind gives a view 1.4 would not. 1.4 also does not mention `ground_ft`.
6. `creation-runbook.md` 4.1 against `engine/night/creation-nights.md` and `engine/roles/keeper.md` (items 80, 81): the runbook runs the final leak scan before the checker's read of the first morning. The engine files run the read first. In the runbook order, a fix made after the read is never rescanned.
7. `tools/map.py` stamp against `tools/lockcheck.py --places` and the runbook lock line "no warning stands for a capitalized map name without its id" (item 56): stamp now skips god-written files and the keeper log, but `--places` still warns on them. The skip lists, or the lock line, should agree.
8. `engine/creation/day2-the-god.md` Opening and "What the DM has from Night 1" (items 14, 32): neither has the DM read `requests-answered.md` for a Day 1 sealed request, and the Opening still says the DM sees nothing else of the night.
9. `engine/night/creation-nights.md` Night 3a and `engine/rules/morning-story.md` (item 32): Day 3 sealed requests are answered on Night 3a, but no file says when the player hears they were received and ruled, since no creation day follows.
10. `creation-runbook.md` Night 1 (1.8 or 1.9) (item 32): there is no checkbox to answer Day 1 sealed requests. Night 2 (2.3) and Night 3a (3a.2) have one.
11. `creation-runbook.md` 3a.1 counting line and `sealed-factors.md` What counts (items 51, 58): the 3a.1 count line does not cite What counts as 2.4 does, so a priced bend has no count step. Also, sealed-factors cites only 3a.1 and not the Night 2 bend round in 2.3.
12. `creation-runbook.md` 3a.1, `engine/creation/day3-the-people.md` (hierarchy template heading "bent, and empty at landing") (item 51): designed-not-yet-serving is headed as a bend, while 3a.1 gives a bend a round and in the same place says designed-not-yet-serving buys nothing. The files should say whether it gets the round.
13. `engine/roles/checker.md` and `creation-runbook.md` section 4 (item 74, decision 6): the public `P/years/000/lock.md` still carries a Pacific time, which is a stage time in a public file.
14. `engine/rules/morning-story.md` and runbook 4.1 (item 76): the (oog) map line for creation names has no pointer to `map-meta.json` `creation_names` or the draw command's note.
15. `engine/rules/morning-story.md` and runbook 3b.8 (item 77): the "Settled for you" block names no source file for the Keeper's answers, and the DM release step does not tell the Keeper to supply them.
16. `engine/creation/day2-the-god.md` and `engine/roles/dm.md` (item 17): the reading list gives pace sections 1 to 4 and 7, but the provisional case the guide names is a work rate, which is section 5.
17. `engine/roles/npc-god.md` (item 36): it names only the orchestrator as the committer. The runbook (standing rules) names the night session, or the orchestrator in a test run.

## Notes

1. Test suite: 71 passed (61 at e5f83df).
2. `python3 tools/lockcheck.py sim-05 --all`: 0 failures in every check. Places has 12 warnings, the same as at e5f83df. Leaks has 1 new warning, the public timing file (item 74), which is expected on the closed run 05 record. Releases shows 0 and 0. Nothing was changed.
3. `python3 tools/map.py validate sim-05`: 0 problems, 0 warnings, unchanged.
4. Timing (74): the engine, runbook, night turn, scheduled prompt, creation-nights and the tests README now name only the sealed `S/state/timing.md`. The public path appears only in lockcheck's warning and in check.py's fallback for older campaigns. The closed records (dryrun, sim-02 to sim-05) keep their public files, as expected.
5. `tools/check.py` (74): the change is covered by decision 6 in substance, because the file moves everywhere and check.py would otherwise read a file no longer written. The plan's assignment does not name check.py; `applied.md` records it as done at the coordinator's word.
6. Sealed answers (14, 43, 64): the kinds and headings (want, fear, request not to be told, request to the Keeper, other), the two-kind split and the open-line wording agree across the Day 1 to 3 guides, dm.md, keeper.md, checker.md, DESIGN 10.7 and the runbook. The file header and the paths of `requests-answered.md` agree.
7. Return (16, 19, 20, 22): `powers.md` and `sealed-factors.md` agree in substance. The return never takes a possession, the slower return counts in the sealed factors, and the fallback for a god with no ground matches the run 05 ledger ruling.
8. First morning (78, 80, 81): the closing line in test runs, the close waiting on the painting, and the checker's read before the clock is set are present in DESIGN 3.3, CHANGELIST, creation-nights, keeper.md, checker.md, morning-story.md and runbook 4.1. The only difference is the order in should-fix 6.
9. Item 36: the README, npc-god.md and the runbook's release lines agree on substance (retry a failed pull once; the god does not commit; the session that spawned it commits). The only gap is the wording in should-fix 17.
10. Knacks (68): K's template 7.10 reads that knacks never grow. This is a decision for Michael, not a fix.
11. `engine/rules/map.md` 4.2 says smoke seen from afar is drawn unnamed, while the tool keeps a rumor's told words. Separately, `tools/map.py` `heard_name` still says a creation name "counts as heard". Behaviour matches 4.2 through its (oog) clause.
12. The checker's read of the first morning writes to the lock flags after `LOCKED.md` says "Nothing is added after this lock" (`checker.md`). Worth a line saying the read is outside the lock.
13. `sealed-factors.md` counts a priced bend only through a negotiation round. Whether the player's priced bend on Day 3 counts is unsaid.
14. No em or en dash was added. `map.md` carries two sections numbered 1.4, which predates this build.
