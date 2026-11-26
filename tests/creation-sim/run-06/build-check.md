# Build 7 check

The independent check of build 7, commits af79446 to 5f29100, against `build-plan.md`, `changes.md` (every row and the closing decisions) and `applied.md` (Agents E, T and K, both passes). Written 2026-11-25 under Michael's go of 21:16 Pacific ("ok.... go build and run .7"), which covers this file and the sealed companion `SPOILERS_do_not_open/keeper/build7-check-sealed.md` only. Procedure only: nothing sealed is written here. Where a finding needs sealed detail, it says so and the detail is in the companion.

Counts: 2 major, 8 moderate, 13 minor. No fix has been made; each waits for Michael's go.

## Scripts

- `python3 -m pytest tests/tools -q`: 85 passed (Agent T's figure confirmed).
- `python3 tools/lockcheck.py sim-06 --all`: exit 0. places 0 failures, 34 warnings (place names with no id in sealed civ files, as before); leaks 0 failures, 1 warning (the phenomenon allowed by its label, item 71); releases 0; mysteries 0; rolls 0 failures, 1 warning (15 older public lines with `r-` ids); dashes 0. Matches `applied.md`.
- `python3 tools/check.py sim-06 3`: 0 findings, 1 note (the same older ids). With `--step 7`: 1 finding, the clock on Year 4, as expected for a closed year.

## 1. Items and decisions applied

Every row of `changes.md` from 1 to 101 is cited in an engine, tool or sealed file, or recorded in `applied.md` as needing no change, except the no-change rows, which need none. Items 4 and 22, which carry no item number in the files, are applied (`engine/creation/day1-world-survey.md` line 36 and 58; `engine/roles/dm.md` lines 7 to 13, a numbered list of three). Items 3, 33, 81, 82, 90, 94, 99 and 101 are applied as their status lines read. Every "no change" reason in `applied.md` holds. The findings below are where an item or decision is applied but left a conflict.

## 2. Decisions 1 to 9, and the old rules

- Each country's own season and L-0043: gone from the engine and tools. The sealed files keep them only in lines that say they are replaced. Holds.
- Sealed parts never acted on: gone. DESIGN 10.7, the runbook standing rules, `year-turn.md` section 5 agree: an act is done, a habit is conduct, wants and fears wait on confirmation. Holds.
- The DM pricing a mortal's knack: gone. `day3-the-people.md` items 5 and 6, `dm.md` line 53, `powers.md` line 91, DESIGN 3.16a, runbook 3a.2 agree. Holds.
- A prepared event resolved in the night, L-0038, L-0046: gone for new campaigns. They still bind sim-06 (major finding A1).
- Prompting gods to grow: gone. `npc-god.md` step 6 removed; the decide release template prompts nothing. Holds.
- Any felt hint before year 70: stated plainly in DESIGN 6.8, `powers.md` sections 4 and 5, `keeper.md`, `dm.md`, the runbook and the rubric. Two rules in `powers.md` section 4 still tell the player of growth before year 70 (moderate finding B3).
- Decision 3 is stated two ways (moderate finding B4).

## 3. Names and paths

Agree across engine, tools and sealed files: `year-turn.md` (named in `night-turn.md` line 5); `dm-sealed.md` (`night-turn.md` line 61, `dm.md` line 13, `checker.md` line 5, `year-turn.md` section 2, runbook 3b.8); `card-summary.md` (`keeper.md`, `npc-god.md`, runbook 2.4); the decide release `S/releases/NNN/<label>-decide.md` (`night-turn.md` lines 18 and 25, `npc-god.md` line 5, `year-turn.md` 3.2, and sim-06's own Year 3 files); the side release `S/releases/NNN/civ-<people>-sealed.md` (`night-turn.md` line 34, `civ.md` line 5, `year-turn.md` 3.3); `check.py --step 4|7` (`night-turn.md` lines 56, 72, 79, and the tool); `roll.py --public` with `dm-NNNN` ids (DESIGN 12.6, `dm.md`, `encounters.md`, the tool, `check.py`, `lockcheck.py`); the leak allow line form `in <file>: "<phrase>"` (`checker.md` line 31 and `lockcheck.py`); the phenomena `months` field (`phenomena.py`, runbook 3b.6, `year-turn.md` 3.1).

T's `S/civs/<people>-sealed.md` is not the side release under another name. It is the Keeper's world side of the player's people, written on Night 3a (runbook 3a Writes and 3a.2) and told to no one. The player's people have three distinct sealed things: that file, their agent's sealed folder `S/civs/<people>/` (decision 7), and the yearly side release. They agree in use; no file says they are three (minor finding C8).

## 4. Findings

### A. Major

A1. `tests/creation-sim/run-07/plan.md` lines 13 to 20 (owner: the run 07 plan, the orchestrator). Part B reopens sim-06, but sim-06's ruling ledger still binds L-0038, L-0043 and L-0046, and build 7 replaces them only for new campaigns (`SPOILERS_do_not_open/keeper/year-turn.md` line 20; `survey-keeper-notes.md` line 133). The Keeper checks the ledger before any ruling (`night-turn.md` line 47), so the reopened years would run under the rules decision 1 replaced, and the test would not test build 7. Fix: the `rulings.md` entry that reopens sim-06 says, in Michael's words, that build 7's decisions 1 and 3 to 8 apply from Year 4, that L-0038 and L-0046 are set aside from then, and whether L-0043 (each country's own season) stays for sim-06, which was made under it.

A2. `tests/creation-sim/run-07/plan.md` lines 15 and 16 (owner: the run 07 plan; the board itself is the Keeper's). The Year 4 morning's held moment was written under build 6: `campaigns/sim-06/releases/003/dm.md` has no day sheet and no board with parameters and reasons, and the Year 4 morning tells the year past the held moment ("the rest of the year went on around it"). `dm.md` line 37 plays a held moment only from the Keeper's parameters, so the Year 4 play day cannot be played under build 7 as the plan reads. Fix: add a setup step under the same `rulings.md` entry: the Keeper writes the board (facts, parameters, reasons) and a day sheet for that moment before the Year 4 play day, in the template of `year-turn.md` section 2; and the plan says how the Year 4 night treats Year 3's stretch already told past the moment (the "held year's tail" of `night-turn.md` line 16): stands as told, or is worked again.

### B. Moderate

B1. `engine/night/night-turn.md` line 61, `engine/rules/encounters.md` line 95, DESIGN 10.5 and 10.5a, `SPOILERS_do_not_open/keeper/year-turn.md` lines 24 and 30 (owners: E, K). The day sheet and the board's reasons, both "for the DM only" by decision 1 and item 60, are written into the public `campaigns/<name>/releases/NNN/dm.md`, which DESIGN 12.2 treats as the player's folder. The true figures (a weight's true value) and the reasons would sit where the player can read them. Fix: write the day sheet and the reasons in `S/releases/NNN/dm-sealed.md` (the DM already reads it), leaving a pointer in the public release; or Michael confirms the public release is the DM's and may carry them.

B2. `engine/night/night-turn.md` line 16, `engine/rules/morning-story.md` line 63, `year-turn.md` line 18 (owners: E, K). The clock turns one year every night, but nothing says what happens when a held year's tail meets a second held moment: year NNN's player thread cannot start, the clock still advances, and the told time falls further behind with no bound. Fix: say in `night-turn.md` step 0 and `morning-story.md` that a tail stopped again leaves year NNN's player thread unresolved, that the decisions file may then carry more than one earlier year, and how far the clock may run ahead before the world waits.

B3. `engine/rules/powers.md` lines 171 and 172 (owner: E). Need 4 (a new power's drawback negotiated with the player in (oog) before the final attempt) and need 5 (the DM tells the player the attempt is beyond what the world allows) both tell the player of a change in powers, and decision 2 allows no hint of any kind before year 70. Fix: before year 70 the Keeper sets the new drawback sealed and it is found with the power in use, and a ceiling held is met as a failed attempt in the world; or Michael rules that a player's own stated attempt may hear these.

B4. `engine/rules/encounters.md` line 9 (owner: E). It says a thing the Keeper placed "is there, and only the search for it is rolled". `mystery-standard.md` rule 17, `year-turn.md` section 7 and `sealed-factors.md` say a search that reaches the place finds it and is not rolled (Agent K's reading of decision 3, logged). Fix: one reading in both; `encounters.md` and DESIGN 8.7 to match rule 17, or rule 17 to match `encounters.md`, by Michael's choice.

B5. `SPOILERS_do_not_open/keeper/year-turn.md` line 197 (owner: K). The sealed procedure adds a rule that is not in decision 5 and not in any engine file: an ask the god promised to answer later becomes a held moment. Under decision 1 the first held moment stops the player's whole year, so this would stop many years. Fix: take it out, or put it to Michael and, if he agrees, add it to `encounters.md` section 6 where the held list is.

B6. `engine/roles/npc-god.md` line 11 (owner: E). Every NPC god reads on its creation nights that "every power carries a drawback you would notice losing". Item 24 (Michael, 22:10 and 22:11) says nothing about a price is said to an NPC god, so that prices are found in negotiation. Agent E kept the line as a rule, not a price, and logged it for this check. Fix: remove the line from the role file, or Michael confirms it stays.

B7. `tools/check.py` line 150, `engine/night/night-turn.md` line 67, `engine/rules/morning-story.md` line 38 (owners: T, E). The night always writes the morning painting request to `images/requests/`, and `check.py --step 7` and the full check fail when it is not there. A morning whose painting `state/images.md` does not approve (every morning of run 07) belongs in `images/held/`, so the check fails every night of Part B. `paint.py` already skips an unapproved request, so no money is spent. Fix: `check.py` accepts `images/held/<campaign>-NNN+1-morning.json` as a note; `night-turn.md` and `morning-story.md` say an unapproved morning request is written to `images/held/`.

B8. `tests/creation-sim/run-07/plan.md` lines 7 to 11 (owner: the run 07 plan). Part A stops after Night 1 with no step for the clock. Left at `status: creation`, `creation_night: 2`, sim-07 would be run by the scheduled task once enabled (`engine/night/scheduled-prompt.md`), and `creation-nights.md` line 21 never leaves a test campaign open. Fix: the plan says the orchestrator sets sim-07's clock to `status: closed` after Night 1, under its `rulings.md` entry.

### C. Minor

C1. `engine/roles/checker.md` line 31 (owner: E). The paragraph allows a line allow for a phenomenon's count once seen and for frozen card text, then ends "A hit in any other public file is a flag and is fixed by rewording the file, never by an allow line". Fix: end it "A hit in any other public file is fixed by rewording, except a seen count or frozen card text, which take a line allow."

C2. `SPOILERS_do_not_open/keeper/creation-runbook.md` line 491 (owner: K). The leak allow file is described as "one phrase per line", without the line form `in <file>: "<phrase>"` that `checker.md` and `lockcheck.py` now use. Fix: name the line form there.

C3. `engine/roles/checker.md` line 9 (owner: E). In a night turn the checker runs `tools/check.py <campaign> <year>` with no step flag at step 7, which reports the clock not advanced. Fix: "`--step 7` in a night turn's step 7".

C4. `tools/check.py` line 147 (owner: T). The comment numbers the releases step 6 and the morning story step 7; `night-turn.md` numbers them 5 and 6. Fix the comment.

C5. `engine/roles/dm.md` line 63 (owner: E). It does not give the `--who` form `roll.py --public` requires (`dm`, or "<party>, rolled by the dm"); the tool refuses any other. Fix: give the form, with whose attempt it is.

C6. `engine/rules/map.md` lines 176 to 181 (owner: E). The reveal examples show no line feature raised to seen, which now needs `--seen-from`, `--stretch` or `--whole`. Fix: add one example.

C7. `engine/night/night-turn.md` lines 13 and 19 (owner: E). Step 0 pulls twice. Fix: keep the one at line 19, before spawning.

C8. `SPOILERS_do_not_open/keeper/year-turn.md` section 3.3 and `engine/night/night-turn.md` line 34 (owners: K, E). The three sealed things of the player's people (section 3 above) are not named as three anywhere, and 3.3 does not say whether the side release is drawn from the Keeper's world-side file. Fix: one line in each.

C9. DESIGN 6.8 (line 136), `engine/roles/keeper.md` line 57, `year-turn.md` line 233 (owners: E, K). A tier or knack step earned before year 70 is "found in use" and gets its card entry when it shows. That is a reading of decision 2 ("no hint of any kind"), not its words. Fix: record it as a reading for Michael, or hold the showing to year 70.

C10. `tests/tools/README.md` (owner: T). Not updated for build 7 (Agent T noted it as outside its files). Fix: add the build 7 tests, if Michael counts it among the tools' tests.

C11. `tests/creation-sim/run-07/plan.md` line 16 (owner: the run 07 plan). The Year 4 decide releases copy "What the people tell their god" from each civ's Year 3 report; sim-06's Year 3 reports were written before that section existed. Fix: the plan says the Keeper writes Year 4's from the reports as they stand, logged.

C12. `tests/creation-sim/run-07/plan.md` line 10 (owner: the run 07 plan). "every god, player and NPC, votes its top two waking months on Day 1": the NPC gods answer the survey on Night 1. Fix: "in the Day 1 survey (the NPC gods on Night 1)".

C13. `tests/creation-sim/run-07/plan.md` line 20 (owner: the run 07 plan). It checks decisions 3, 4, 5 and 8, which need a search, an absence with an ask, and an act in a sealed note, but names no stand-in brief and nothing that brings them about. Fix: a short run 07 stand-in brief, or the plan says they are checked only if play brings them.

## 5. Awaiting Michael (noted, not ruled)

- The overrule of DM rolls by the sealed factors against decision 1's "a played scene holds". Agents E and K applied it narrowly: the overrule stays for ordinary DM rolls, and no roll made in a played held moment or prepared scene is overruled; the factors enter such a scene through the board's ranges instead. Applied consistently in DESIGN 12.6, `dm.md`, `keeper.md`, `night-turn.md` line 44 and the sealed files. If Michael meant every played scene, those files change together.
- The knack growth figures. `powers.md` section 4 leaves them to the Keeper's sealed files; Agent K set them in `year-turn.md` section 8 and marked them for Michael's ruling. They are in the sealed companion.

## 6. Run 07

Not as written. Part A can run once B8 is fixed (the clock after Night 1). Part B cannot run under build 7 until A1 and A2 are settled: a `rulings.md` entry that sets sim-06's superseded rulings aside and says which season rule holds, and a setup step that gives the carried held moment a build 7 board and day sheet and says how the Year 3 stretch already told past it is treated. B7 makes every Part B night fail `check.py` while the painting requests are held; fix the tool or have the checker rule it each night. C11 to C13 are small changes to the plan.
