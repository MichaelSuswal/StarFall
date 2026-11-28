# Build 8 (1.0): the build check

The independent check of build 8, the commits after 95f2b5f (8394fda, 238c90b, 3b9e672, 38e0f70, 212ab64, 551990b), against `build-plan.md`, `changes.md` (items 1 to 30 and Michael's decisions of 2026-11-27), `rulings-to-rules.md` (lines 1 to 87) and `applied.md`. Checked 2026-11-27 by a checker that did not build it, under Michael's go of 19:37 Pacific for this file and its sealed companion only. Procedure only: sealed detail is in `SPOILERS_do_not_open/keeper/build8-check-sealed.md`.

## Counts

0 major, 5 moderate, 12 minor.

## Script runs

- `python3 -m pytest tests/tools -q`: 96 passed.
- `python3 tools/lockcheck.py sim-06 --all`: 0 failures (places 98 warnings, leaks 1, releases 8, rolls 1). Matches Agent T's run.
- `python3 tools/check.py sim-06 5`: 0 findings, 4 notes (the held Year 6 morning request; the older public roll ids; the Year 5 transcript's two falls, each restored).
- `python3 tools/lockcheck.py sim-07 --all`: 2 failures, places (no `map.json`) and mysteries (no mysteries file). Expected: sim-07 was closed after Night 1, before Night 3a writes either. Leaks, releases, rolls and dashes 0. Not a build fault; Agent T ran only `--leaks --dashes` on it.

## Coverage

- Items 1 to 30: each is applied where it belongs, or recorded as needing nothing (9, 10, 16, 19) or as watch (12), for reasons that hold. Item 23's open point is ruled below (R6).
- `rulings-to-rules.md`: its 87 lines cover every "Rulings for review" entry in the sections the build plan names, one for one (counts in the sealed companion). Each line that becomes a rule is in the file it names, in the form ruled; the superseded lines (2, 30, 32, 49, 60, 74, 76, and parts of 25, 57, 62, 85) are superseded by the decision they cite.
- Decision 1 (the clock waits; a minor held moment; a play day at most one year): stated in `night-turn.md` step 0, with DESIGN 1.12 and 10.5a, `encounters.md` 6, `morning-story.md`, `keeper.md`, `checker.md`, `time-and-pace.md` 8, `README.md` and the sealed `year-turn.md` 1 agreeing with it. The build 7 lag rule and L-0056 are gone from every engine, tool and sealed file; CHANGELIST keeps them struck through, as it should. One build 7 phrase is left in a sealed file (finding 15).
- Decision 2 (paintings): `paint.py` and `check.py` read approval the same way, through `paint.covered()`; a line for another year never approves; the standing line covers a year's first morning only; a further morning while the clock waits needs a line naming its year and its play day. Engine (`morning-story.md` 2, `night-turn.md` 6) and sealed runbook agree. No `images.md` line yet approves a further morning, so each is held: approving one is spending, for Michael.
- Decision 3 (travel by direction, with the climb rule): `map.py travel` prices each way, names every line end by place, and reads `heights_ft` and per-direction `pace`, field names and form as `map.md` 5.1 gives them; the gazetteer gives each way its figure. One engine sentence misstates when the climb applies (finding 3).
- The version: `CHANGELIST.md` has "Build 8: 1.0, after the short check run 07"; `README.md` opens "Version 1.0 (build 8, 2026-11-27)"; DESIGN names 1.0 in its opening paragraph and 1.13. Its title still reads "(pre-build)" (finding 13).

## The clock waiting: the mechanics judged

- The `play_day` line: sound. Absent means play day 1; 2 or more only while a year stays open; removed when the clock advances. `check.py` `clock_problems()` enforces all three, and step 8 of `night-turn.md` sets it as `check.py` reads it.
- `decisions-NNN-K.md` and the K-suffixed files: one rule, applied the same in `night-turn.md`, `year-turn.md` 1 and 2 and `check.py`: every file the night of play day K writes carries K (`dm-K.md`, `dm-sealed-K.md`, `closing-K.md`, `flags-K.md`), and the morning it writes is the next play day's, `morning-story-<K+1>.md`, with request `<campaign>-NNN-morning-<K+1>.json`. The scheme is consistent but leaves the reader to work out that play day K reads the release of night K-1; the DM's and the Keeper's role files name only the play day 1 files (finding 4). `lockcheck.py` does not yet skip `flags-K.md` (finding 2).
- "A night after the clock waited": sound. NPC gods do not decide again, the world's year stands as resolved on its first night, the player's people's agent works only the stretch, and anyone the stretch reaches gets a short pass or the Keeper's logged step. It does not say what the night does when the player posted but did not play the held moment (finding 6, ruled R8).
- Engine, `check.py` and `year-turn.md` agree on the clock line, the file names, the morning paths, the request names and the timing line "clock waited: year NNN open, play day K+1". A test run of `check.py` on a mid-year day the world waited (play day 3, no post) gave no false finding with the default flags, and flagged a clock that raised `play_day` on that day.

## Findings

1. **Moderate, E.** `tests/creation-sim/run-07/applied.md`, after line 76. Commit 551990b removed Agent K's whole section ("## Sealed side (Agent K)", 43 lines, present at 212ab64) while rewriting the climb gap line. Fix: restore that section verbatim from 212ab64, between Agent E's "Gaps for the build check" and "## Tools (Agent T)", and keep Agent E's revised climb line.
2. **Moderate, T.** `tools/lockcheck.py` line 161, `is_flags_file()`. It skips `years/NNN/flags.md` but not `years/NNN/flags-K.md`, the checker's file on a night after the clock waited (`night-turn.md`), so item 26's place-scan failure returns on the first waiting night. Fix: match `flags.md` and `flags-<digits>.md` under `years/NNN/`; a test.
3. **Moderate, E.** `engine/rules/time-and-pace.md` line 11 and `engine/design/DESIGN.md` line 175 (10.1). Both say the climb applies where a line carries `heights_ft` "or a per-direction `pace`". `map.py` adds a climb only from `heights_ft` (`climb_feet()`); a `pace` stretch only picks each way's row. Fix: "The climb applies where a line carries `heights_ft`; a `pace` stretch sets the pace table row for each direction." `map.md` 5.1 already reads so.
4. **Moderate, E.** `engine/roles/dm.md` lines 5, 13 and 53; `engine/roles/keeper.md` lines 36 and 65; `engine/night/scheduled-prompt.md` line 21; `engine/rules/morning-story.md` line 3. Each names only `releases/NNN/dm.md` or `dm-sealed.md`. Under `night-turn.md` the night of play day K writes `dm-K.md`, so play day K reads the release of night K-1 (`dm.md` on play day 2, `dm-<K-1>.md` after). Fix: one sentence in `dm.md`'s read list and its sealed-companion paragraph saying which pair play day K reads, and "(or its play day's numbered file, `night-turn.md`)" in the others.
5. **Minor, E.** `engine/roles/civ.md` line 5 and `engine/rules/morning-story.md` line 131 name only `decisions-NNN.md`. Fix: add "(`decisions-NNN-K.md` on play day K)".
6. **Moderate, E.** `engine/night/night-turn.md`, "A night after the clock waited", its step 0 line. Nothing says what the night does when the play day's decisions file has no `## Played at a held moment` section (the player posted, but not in the scene). Fix: add the rule of R8.
7. **Minor, K.** `SPOILERS_do_not_open/keeper/year-turn.md` section 1, "The clock waits". The same gap. Fix: the same rule, R8, in a sentence.
8. **Minor, E.** `engine/night/night-turn.md` line 95. The marker "says only that a line was set aside and where it is kept"; `year-turn.md` 1 says "kept where it stands". Fix: "and that it is kept where it stands" (R5).
9. **Minor, E.** `engine/roles/checker.md` line 18 (item 6). It checks only that no passed moment was a prepared scene. Fix: "and none was a moment `year-turn.md` section 1 calls never minor".
10. **Minor, E.** `engine/roles/dm.md` line 31. It says `check.py` fails any transcript whose section count falls between commits; the tool makes a fall that a later commit restored a note (R7). Fix: add "unless a later commit restored every section, which is a note".
11. **Minor, E.** `engine/rules/time-and-pace.md` line 11. A process note stands in a rule file: "which is Agent T's reading in build 8, for the build check". Fix: "(build 8 check, R4)".
12. **Minor, E.** `engine/design/CHANGELIST.md` line 129. The decision 3 line does not name the climb rule. Fix: add "and a climb adds an hour per 2,000 feet climbed in the direction travelled (Naismith), a descent nothing".
13. **Minor, E.** `engine/design/DESIGN.md` line 1. The title reads "Design Record (pre-build)" at 1.0. Fix: "StarFall: Design Record (1.0)".
14. **Minor, E.** `engine/roles/checker.md` line 35. It names only `years/NNN/flags.md`. Fix: add "(`flags-K.md` on play day K, `night-turn.md`)".
15. **Minor, K.** `SPOILERS_do_not_open/keeper/year-turn.md` line 21. "At most one untold stretch of the player's thread is open at a time" is the build 7 lag rule's frame. Under the clock waiting it says nothing. Fix: drop the sentence.
16. **Minor, T.** `tools/roll.py` line 120 (`DM_WHO_RE`) and line 250. `--public` accepts any `who` with the word "dm" in it ("keeper for the dm", "dm keeper"); `dm.md` line 67 says the tool refuses any form but two. Fix, by R6: for `--public`, accept only `dm` or `<party>, rolled by the dm` with a party before the comma, case aside; keep `is_dm()` for reading older public log lines; a test.
17. **Minor, E.** `engine/style/house-style.md` line 69. The request names give no form for a further morning. Fix: add "(`<campaign>-NNN-morning-K.json` for a further morning while the clock waits)".

## Rulings for review

Ruled by the judgment order in `engine/roles/keeper.md`: fairness, above all to the player's original intent; then fit with the rule as Michael gave it; then balance.

- **R1. Agent K's cases of "never minor".** Upheld, each of them. A moment the player said it means to play is a prepared scene in all but name (fairness to the player's intent). A moment a morning has already told the player its story stands at cannot be passed without taking back a board the player was shown (a told line is never taken back). "In doubt, held" is `encounters.md` 6's rule for an unsure agent. K's test for minor (standing conduct and words already answer all the moment asks, and nothing turns on a choice the player has not made) is a fair reading of Michael's word "minor". None of these narrows his rule beyond what his words carry. Michael's own words name only "minor"; the build plan's line naming a prepared scene stands with them.
- **R2. A play day never reaches past the clock's year.** Upheld. It follows from "the clock waits until the story catches up": no part of the world past the clock's year is resolved, so a day that ran past it would tell an unresolved world. It is within "a play day should not be more than one year". `dm.md` line 33 agrees.
- **R3. The climb rule.** Michael's words name no figure. The rule came by the coordinator's instruction after 38e0f70. Upheld, as the real-world rate DESIGN 10.1 calls for, and the only way "uphill against downhill" in his decision changes a road's time. Logged as a figure he did not name.
- **R4. The same climb hour on horse and with a cart.** Upheld, as the floor: Naismith wrote it for walkers, and a beast or a cart is no faster up a slope. Logged for review; a steeper figure for a cart would be Michael's.
- **R5. The set-aside marker.** One wording: "kept where it stands", since marking is in place and nothing moves (decision on item 7; rule 37).
- **R6. `roll.py --public` and `--who`.** The tool is brought to `dm.md`'s text (finding 16), not the text to the tool. The public log is what the player sees of open rolls, and the narrow form names whose attempt it is (DESIGN 12.6). `dm.md` and build check C5 already give that text.
- **R7. Agent T's ruling on a restored transcript.** Upheld. A fall that a later commit restored, with every committed section standing now, is a note. Item 24 guards against losing table talk. A restored fall loses none, and a permanent finding would fail every later check of the sim-06 Year 5 transcript.
- **R8. A play day with a post but the held moment unplayed.** The moment stays held and nothing past it is resolved. The clock waits again, with `play_day` raised, and the next morning opens on the same board. The DM never acts for the player, and the player chooses when to play. A scene the player walked away from in play is played: its outcome is what the god did.

## Open for Michael (not findings)

- No `images.md` line approves a further morning while the clock waits, so each is held. Approving them is spending.
- The installed scheduled task's own prompt was not changed for item 17 (`applied.md`, Agent E); updating it needs his go.

## Can 1.0 ship

Yes, once the findings are fixed. Findings 1 to 4 and 6 must be fixed first. Each bites only from a campaign's second play day in a year, or in the build record, and none touches play day 1. The minor findings go with them in the same fix pass.

## Recheck

2026-11-27, against 84ee295, 1023be2 and 4cc9d49, at the text and tools as they now stand. All 17 findings are fixed.

- Finding 1: Agent K's section in `applied.md` matches 212ab64 lines 78 to 120 line for line (checked by diff). The only addition is K's own "Fixes after the build check" subsection after it.
- Finding 2: `lockcheck.py` `is_flags_file()` skips `years/NNN/flags.md` and `flags-K.md` and still scans `closing-2.md`; a test covers it.
- Finding 3: `time-and-pace.md` line 11 and the quick reference, and DESIGN 10.1, now say the climb applies where a line carries `heights_ft` and a `pace` stretch sets each direction's row, as `map.py` does.
- Finding 4: `dm.md` line 5 names the pair play day K reads (`dm.md`/`dm-sealed.md` on play day 2, `dm-<K-1>.md`/`dm-sealed-<K-1>.md` after), and lines 13 and 53 point to it; `keeper.md` 36 and 65, `scheduled-prompt.md` 21 and `morning-story.md` 3 add the numbered file.
- Finding 5: `civ.md` 5 and `morning-story.md` 131 name `decisions-NNN-K.md`.
- Finding 6: `night-turn.md` line 86 carries R8.
- Finding 7: `year-turn.md` section 1, "The clock waits", carries R8 in one sentence, agreeing with `night-turn.md`.
- Finding 8: `night-turn.md` line 95 reads "kept where it stands" (R5), as `year-turn.md` does.
- Finding 9: `checker.md` item 6 checks every never-minor case `year-turn.md` section 1 names.
- Finding 10: `dm.md` item 4 says a fall a later commit restored is a note (R7), as `check.py` does.
- Finding 11: the process note is gone; `time-and-pace.md` cites R4.
- Finding 12: the CHANGELIST decision 3 line names the climb rule.
- Finding 13: the DESIGN title reads "(1.0)".
- Finding 14: `checker.md` 35 names `flags-K.md`.
- Finding 15: the build 7 sentence is gone from `year-turn.md` line 21; no engine, tool or sealed file carries the old lag rule.
- Finding 16: `roll.py --public` takes only `dm` or `<party>, rolled by the dm` (`public_who_ok()`), refusing "keeper for the dm", "dm keeper" and a bare ", rolled by the dm"; `is_dm()` stays for older log lines; a test covers it.
- Finding 17: `house-style.md` 69 names `<campaign>-NNN-morning-K.json`.

Each agent logs its fixes in `applied.md` under its own heading: Agent E (findings 1, 3 to 6, 8 to 14, 17), Agent K (7, 15, with R1 and R2 standing), Agent T (2, 16, with R7 standing). T's fixes were committed inside E's commit 1023be2, as T's log says. No em or en dash in the changed files.

Script runs: `python3 -m pytest tests/tools -q` 97 passed; `lockcheck.py sim-06 --all` 0 failures (places 98 warnings, leaks 1, releases 8, rolls 1, unchanged); `check.py sim-06 5` 0 findings, 4 notes, unchanged.

One observation, not a finding: `public_who_ok()` refuses a party that itself holds a comma ("Ada, the smith, rolled by the dm"). The refusal is loud and the DM can write the party without one, so nothing is lost.

Still open, for Michael only: approving paintings for a further morning while the clock waits (spending), and updating the installed scheduled task's prompt for item 17.

1.0 can ship.
