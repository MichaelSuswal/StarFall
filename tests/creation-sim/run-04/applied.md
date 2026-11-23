# Applied changes, build 5

Each line names the run 04 change list items it applies (and run 03 item 94, mirror mode).

## Engine side

- `CLAUDE.md`: 25 (pull with --rebase --autostash), 58 (the player starts a campaign; the exception covers the whole run; no step waits on Michael; spending beyond images.md still needs him; test-run exception).
- `engine/design/DESIGN.md`: 1.1 and 3.4c and 3.9 mirror mode (run 03 item 94), 2.7a 58, 3.11 29, 3.13 16, 10.7 13, 30, 32, 11.1 and 11.2 68, 11.4 46, 12.6 66, 15.2 and 15.5 58.
- `engine/design/CHANGELIST.md`: build 5 section, reversed decisions for mirror mode, 58, 66, 13, 46, 68, 29.
- `engine/creation/day1-world-survey.md`: 3 (one place for a closing question, remarks before the numbers, premise line format, ISO date, option plus extra), mirror mode (the mode question, mode line, mirror.md, the mirror survey as a SEALED reply, test person file).
- `engine/creation/day2-the-god.md`: 13, 30 (unsaid asked last, SEALED reply, transcript line), 18 (read the hidden-powers line, a declined trade stays closed until play, sealed path written directly), 19 (every world-rules item stated before the close), 24 (unsaid.md header), 32 (check-with-the-player mark), mirror mode (abilities still chosen, knacks unmentioned).
- `engine/creation/day3-the-people.md`: 26 and 47 as they touch the DM (what counts as land; the brief names only what the draft fixes, corrections at the pre-landing block), 29 and 34 (refusal priced plainly, asked or not; edge named, one weakness per step), 30, 32 (sealed answers section), 43 as it touches the Day 3 guide (every table pricing marked Ledger: pending).
- `engine/roles/dm.md`: 4 (failures checklist on the creation list), 18 (sealed paths written directly), 30, 32, 34, 46 (knowledge.md, names in mortals' mouths), 58, 66 (open rolls, Keeper may overrule), mirror mode (mirror.md exception, Day 1 reads).
- `engine/roles/keeper.md`: 6 (no number word beside god), 32, 46 (writes and updates knowledge.md), 56 (landing releases on 3b), 58 (Rulings for review), 66, mirror mode (reads mirror.md on Night 2).
- `engine/roles/checker.md`: 32, 46 (knowledge.md names), 58 (the lock never pauses), mirror mode (reads mirror.md).
- `engine/roles/civ.md`: 32, 46.
- `engine/roles/npc-god.md`: 25, 56.
- `engine/night/creation-nights.md`: 9 and 68 (Night 1 underground decision; 3a writes the layer before painting, data rules below), 25, 46, 56, 58 (player's go, no waiting, lock never pauses, the ruling-wait notice removed), 63, mirror mode (Night 2 reads and knacks).
- `engine/night/night-turn.md`: 25, 46, 56 (Year 1 setup), 58, 66.
- `engine/night/scheduled-prompt.md`: 58 (automatic approval note).
- `engine/rules/powers.md`: 16 (part loss and the stacking rule), 17 (return ground set at the table if no advantage), 20 (the faster return costs more), 21 (ground gone, nearest ground; rung fixed at creation).
- `engine/rules/time-and-pace.md`: 16 (flight rates, section 7).
- `engine/rules/map.md`: 39 and 59 (a creation name counts as heard; a seen feature shows its told name or none), 46, 68.
- `engine/rules/morning-story.md`: 59, 63, 64 (the "(oog) Before you land" block).
- `engine/style/house-style.md`: 61 (no-face line for bodies that are not figures), 67 (a mostly solid layer asked as solid rock, checked against the data).
- `tests/creation-sim/README.md`: 1 and 37 (setting up the next run), 58 (test runs never pause, except a ruling Michael asks to make), mirror mode (person.md).
- `README.md`: 58 (automatic approval note for whoever enables the task), mirror mode (the Day 1 question).

## Tools

Agent T, 2026-11-22. Files: `tools/lockcheck.py`, `tools/map.py`, `tools/paint.py`, new `tools/stamp_time.py`, `tests/tools/test_tools.py`, `tests/tools/README.md`, the fixture's `campaigns/fx/player/map-knowledge.json`.

- 2 (`lockcheck.py`): `--dashes` run alone reads the public folder when no sealed folder exists yet, with a note; every other check still needs the sealed folder.
- 10 (`tools/stamp_time.py`): prints the Pacific clock time from the system clock in the timing log's format (`2026-11-22 21:39`; `--time` for `21:39`, `--date` for the date). It prints; the writer copies it into the log.
- 38 (`map.py` stamp; `lockcheck.py --places`): aliases are never stamped; `--places` no longer warns on a bare alias, since stamp will not give it an id. The gazetteer still prints the god's aliases.
- 39 and 59 (`map.py`; `lockcheck.py` to match): a place shows the name the god has heard (`heard_name`): the Keeper's name once marked `"named": true`, a name the player gave it at creation (an alias `by` "player"), a told name, or for a report with no other name the Keeper's name ("told, reported", map.md 4.2). A seen place with no name heard shows none: a settlement's mark alone, no label; the gazetteer gives its id and type. Seeing a told place keeps the told name (`told.name` is now allowed on a seen entry) and no longer turns it into the Keeper's name; the map log prints a "found to be" name only once it is heard. The leak scan follows the same rule, so a Keeper's name the god has not heard (a seen place unnamed, or a place known only by a told name) is a sealed term in public files. The fixture's seen features f01 to f03 are marked named, since its public notes use their names.
- 40 (`map.py` describe): a settlement within two miles is never missed (in view, or as its smoke, walls or lights past the near distance of hill or forest ground, with no blocker test); a settlement of any shape is read at its nearest point; no region a border settlement stands in hides it. On sim-04's present landings no settlement within 45 miles was missed before or after; the change guards the case.
- 41 (`map.py` travel): a boat trip may start with a walk to the water and end with a walk from it, each up to 10 miles (`BOAT_WALK_MILES`, under a day on any ground), priced on foot; land between two waters is still no passage by boat. A walk, ride or wagon trip whose straight line crosses a sea or lake goes around it over land by the shortest way the map gives, said in the output. The 10-mile figure is mine; the item named no figure.
- 42 (`map.py` draw): the landing frame is widened about its middle (shifted to stay on the painting) so the sheet never blows the painting up more than three times; a rumor beyond the sheet carries one direction, its told name's when it gives one.
- 44 (`map.py`): `regions-from-paint` cuts region polygons from a flat-colored label painting so that neighbors share each border point for point (no gaps, no overlaps; a lake inside a region cut out by a zero-width slit; stray parts and unclaimed pixels given to neighbors), checks them, and saves or applies them; `tiles` checks that the regions tile the painting; a sea or lake region's name is kept on its water where it fits.
- 50 (`map.py` travel): a trip's end may be `rNN:edge` (the nearest point of a region's or an area feature's edge, toward the other end) or a line's `fNN:start` (source) or `fNN:end` (mouth).
- 53 (`map.py` validate): overlapping regions fail, with their area, cells and thickness, and so does a landing point inside two regions; gaps are a warning in validate and a failure in `tiles`.
- 60 (`map.py` draw): with `--zoom landing` the god's mark is drawn at its landing point, and a far sighting (a rumor with `told.bearing`, or a told name like "smoke to the north-west" from the god's own sight) is a bearing tick from it, named once in the footer and never listed as a rumor beyond the sheet; a region cut by the crop is labeled on its visible part with that part's cell. `told.bearing` is a new allowed key on a rumored entry.
- 62 (`paint.py`): `--help` prints the usage; with no arguments it reports as `--check` does and paints nothing; `--paint` paints. Inside the paint workflow (`GITHUB_ACTIONS` true) no arguments still paints, so the workflow keeps working until `.github/workflows/paint.yml` is changed to call `--paint`, which is outside agent T's files.
- 68 (`map.py`): validate fails a world whose placement plan, histories or world draft give an underground (an `Underground:` or "The underground:" line, a ticked box, "has an underground", or a heading of its own, not a line that says there is none) while `map.json` has no layer; layers are checked for their form (id `under-N`, a whole-number depth no other layer has, features `uNN`, optional regions, painting a file name or left out); a `uNN` id on the surface fails; a layer with no painting yet is not drawn and the draw says so.
- Tests: 14 new (59 in all, all passing under `python3 tests/tools/run.py` and pytest); two older tests updated for 38 and 39.
- Run on sim-04 (its data unchanged): `lockcheck.py sim-04 --all` is unchanged, 0 failures in every check, 16 places warnings. `map.py validate sim-04` now fails with 86 problems where it passed with 0: 85 pairs of overlapping regions, nearly all about a mile (one pixel) thick along shared borders, the borders item 44 found cut overlapping; and the underground the world draft and placement plan give with no layer in `map.json` (item 68's finding). It also warns of about 2,270 square miles in no region. `regions-from-paint` on a raster of sim-04's own regions gives 34 polygons that tile the sheet.

## Sealed side

Agent K, 2026-11-22. Files: `SPOILERS_do_not_open/keeper/creation-runbook.md`, `npc-god-rubric.md`, `survey-keeper-notes.md`, `sealed-factors.md`.

- 7, 27, 51 (runbook): one close order for every night (timing, clock, commit, pull with rebase and autostash, push); one list of commit forms, each starting "Creation night N:", with forms for a stage, the hand-off's logged commit id and a round of lock fixes; timing stages named by what was written; one ledger entry per matter; months in the schedule counted from each country's waking season; a 3b hand-off check before the hand-off commit.
- 8 (runbook 1.4 and template 7.4; survey notes rule 6): a marker counts only at the start of an answer; an "or something else" answer is never bent.
- 9 (survey notes; runbook 1.5): an untilted "some of each" placed at the midpoint; even odds succeed on 51 to 100, a half-median success rounds up, a tied vote's success goes to the side the question names first; a quarter median rounds to the nearer whole; a Night 1 box deciding the underground.
- 11 (runbook): the template is the model, never a prior run's files.
- 13, 24, 32 (runbook, unsaid standing rule): the sealed file is written from the player's `SEALED:` replies by the orchestrator or the DM, never from the transcript; its header says written by the DM, read by the DM, the Keeper and the checker; an open conduct line marked "check with the player before acting" is read with its sealed answer.
- 20 (rubric section 1; runbook templates 7.1, 7.5 and 2.1): each lean printed with a plain sentence from a table; the release says plainly that the faster return costs more.
- 22 (runbook 2.3): a clarification is wording if it changes no number, reach or cost.
- 23, 43, 52, 66 (sealed factors file; runbook standing rules, 1.1, 7.12): a shrunk power, a choice between equal prices, and "taking none" defined; the factor's name on every campaign's sealed term list from Night 1, never removed; the weighting method written as a general rule; a fixed-target harm with a rolled year takes no factor on its year; the Keeper may overrule a DM roll's outcome when resolving the year (which rolls, what it changes, at most once per god per year, sealed log only), with a checker line for it.
- 25 (runbook standing rules and section 7): the pull is `git pull --rebase --autostash origin main`; every release ends with that line.
- 26, 47 (runbook 2.8): what counts as land for the Day 3 brief, with both kinds of case left out; the brief names only what the placement draft fixes, and a view the trace does not hold is corrected through `corrections.md`.
- 33 (runbook 3a.2): a designed mortal's unplaced noticed thing is replaced through `corrections.md`.
- 36 (runbook 3a.1, template 7.7; rubric section 12): the Night 3 release carries the size lean beside the rule and worship leans, with the usual number as the middle, not the expectation.
- 37 (rubric section 13): a test override may force one NPC god to a lean that invites refusal, named as the first god rolled.
- 46 (runbook standing rules, 3a Writes, 3a.7, 3b.8, lock checklist): the player's people's public knowledge file written on Night 3a by the Keeper, updated each year in pass two; the first release points the DM to it.
- 48 (runbook 3a.5, 3b.5): a wonders line for every region; each read on 3b against the mysteries.
- 49 (runbook 2.5, 3b Writes): the Night 2 history checked against section 8; 3b may correct a Night 2 sealed file that contradicts the plane, logged.
- 53 (runbook section 4): after any region-shape fix, every record line placing a fixed point is reread and measured again.
- 54 (runbook standing rules and 7.12): the removal sentence matches the ruling.
- 56 (runbook 3b Writes, 3b.8, lock checklist): each NPC god's landing release written on 3b and handed over at Year 1 setup.
- 58 (runbook standing rules, log format, 3a.4, 4, 4.1, 6): no step waits on the owner; rulings applied and listed under "Rulings for review"; the lock never pauses for a ruling, the checker rules it and the lock goes on; the test-run exception for a ruling Michael asks to make himself; image approvals from `images.md` only.
- 68 (runbook standing rules, 1.5, 1.7, 3a Writes, 3a.3, 3a.4, 3a.5, lock checklist; survey notes Q12): the underground decided on Night 1, written into `map.json` as a layer before any painting, asked for as it is in the data, the painting checked against the data with the data ruling, and no sheet when there is none.
- Run 03 item 94 (runbook Night 2 Reads, 2.6, 2.7, 7.13): mirror mode on Night 2, the hidden powers and two or three knacks for the player's god drawn from the sealed mirror file by the mode recorded on Day 1, nothing sensitive drawn; knacks in the sealed hidden-powers file and counted in balance.
- Also applied in the runbook, as consequences of items assigned to other agents: 38 (aliases are never stamped, said in 3a.5) and 40's runbook half (seat distances and landing views measured again after a landing move).
- Not applied: the logged rulings with no assigned item (the return-scale clauses in the Night 2 release, word-bound drawbacks, ledger ids on a DM-owned people record, the Hierarchy hint's refusal words, which peoples count among the godless), left for Michael. Item 37's watch note for the next run's setup belongs to the stand-in brief, not these files.

## Orchestrator

- .github/workflows/paint.yml: the paint step calls `tools/paint.py --paint`, since a bare call now only reports (62).

## Fixes from the build check

Applied 2026-11-22 against `build-check.md`, under `build-plan.md` (decisions 7 to 9). Every must-fix and should-fix item is applied.

### Must-fix

1. `tests/tools/test_tools.py`: `test_paint_needs_images_md` reads `- run: python3 tools/paint.py --paint`. Suite 61 passed, 0 failed.
2. `engine/design/DESIGN.md` 3.3 and 3.9: every god, player and NPC, gets two or three small innate knacks, sealed, found only in play, counted toward balance, named in no public file; an NPC god's from its own sealed backstory; knacks listed among what the sealed folder holds.
3. `engine/design/CHANGELIST.md` build 5: three reversed-decision lines for decisions 7, 8 and 9.
4. `engine/night/creation-nights.md` Night 2 Does: hidden powers and knacks for all eight gods, each NPC god's knacks from its own sealed backstory in `S/gods-sealed/<god>/`, the player's in `S/player/`.
5. `creation-runbook.md` 2.6 and 2.7: balance counts every god's knacks; 2.7 is "Hidden powers and knacks, all eight", with a new step drawing two or three knacks per NPC god from `backstory-secret.md`, written in `S/gods-sealed/<god>/hidden-powers.md` with Status `knack (undiscovered)`; 2.10's term check names knack names.
6. `creation-runbook.md` section 4, NPC god line: two hidden powers and two or three knacks from the backstory, each with limit and surfacing moment, counted in `balance.md`, named nowhere public, on the sealed terms list. The sealed terms lock line names knack names.
7. `engine/roles/npc-god.md` (never receives its knacks; found only in play), `checker.md` check 4 (no NPC folder holds knacks; no public file names one), `keeper.md` creation list (knacks in `S/gods-sealed/<god>/`; knack names on the sealed list).
8. `tools/lockcheck.py`: a `sealed-terms.txt` line starting `!` is a kept term (the docstring says only that the sealed factors' names are written so): never let through as the player's open word, a known map name, a people's knowledge name or a `leak-allow.txt` phrase. Test `test_lockcheck_kept_term_never_exempted`.
9. `engine/roles/checker.md` leak paragraph: the exception for the sealed factors' names (`!` lines), worded without naming one; the transcripts are not scanned for them, every other public file is, and a hit is fixed by rewording, never by an allow line.
10. The rule: the creation transcripts are the player's own words kept verbatim, not scanned for the sealed factor's name; every other public file is. Written in `creation-runbook.md` section 4 (new paragraph "The sealed factor's name in the player's words"), the sealed terms standing rule, template 7.12 and 1.1 (`!` lines), the DM-owned files rule (a third mechanical exception: the Keeper itself replaces the name in a DM-owned non-transcript file with a plain word of the same sense, logged sealed only, no correction written), the close-of-night rule and the fixing-flags rule; `sealed-factors.md` (secrecy paragraph and check 4); `checker.md` leak paragraph; and in `tools/lockcheck.py` (transcripts skipped for `!` terms only) with test `test_lockcheck_kept_term_not_scanned_in_transcripts`. The DM side, without naming anything: `day1-world-survey.md`, `day2-the-god.md` and `day3-the-people.md` close lists, and DESIGN 3.4b, say the transcript is the verbatim record and never changed, and a copy keeps any word the Keeper replaced with a plain word of the same sense.
11. `survey-keeper-notes.md` rule 4 is now "Ties are the Keeper's": a half or quarter median, an even vote and any even-odds tie are decided by the Keeper by what makes the more interesting game, reason logged, no die; the Even odds line and the quarter rounding are removed. Overview line 13 matches.
12. `survey-keeper-notes.md` Counting rule votes 1 and 3: ties decided by the Keeper as rule 4, no die.
13. `creation-runbook.md` standing rules: Blends and votes, Table rolls (the half-median roll removed from the d100 list) and Rounding (the survey blend is not rounded; a blend between two whole steps is a tie for the Keeper). DESIGN 3.19 says ties in the blend are the Keeper's, no die.

### Should-fix

1. `checker.md` lock paragraph: `Rulings for review`.
2. `creation-runbook.md` unsaid rule quotes "Written by the DM. Read by the DM, the Keeper and the checker." and says the header stands as written when the orchestrator writes the file in a test run (it names the role, not the hand).
3. `day1-world-survey.md`: a layout for `mirror.md` (heading, the same header line, mode and date, `## Found` with `Source:` per line, `## Mirror survey` or `Not asked.`; no file in standard mode).
4. Order named, scan not extended: `dm.md` and `checker.md` check 4 say a told name is recorded in `player/map-knowledge.json` (`tools/map.py reveal`, `told.name`) before, or in the same commit as, the first scene, rolling save or morning story outside `knowledge.md` that uses it.
5. `npc-god.md` names `SPOILERS_do_not_open/campaigns/<name>/releases/000/<you>-landing.md`, read at Year 1 in place of last year's release; `night-turn.md` step 1 says the same.
6. `sealed-factors.md` Record: the overrule is logged in the keeper log only; nothing is added to either roll log, since `tools/roll.py` has no note option and is the only writer. Check 5 says keeper log.
7. DESIGN 12.6 and `dm.md`: "in the open" means the odds are stated to the player before the roll and `tools/roll.py` logs it with factors and odds in the campaign's public roll log `state/rolls.jsonl`; the die stays hidden and the player hears the outcome. (Worded to match `roll.py` and DESIGN 12.6 rather than "the public roll log with stated odds" alone.)
8. `creation-runbook.md` 1.5 and 1.7: the world draft's decision line is `Underground: yes, <what it is>` or `Underground: none`. `tools/map.py validate` now also fails the converse, a layer in `map.json` when the world draft's line reads `Underground: none`; test added to `test_validate_underground_and_layers`.
9. `tools/paint.py`: no arguments only reports, inside `GITHUB_ACTIONS` too; the stale fallback and docstring removed; `test_paint_help_and_no_arguments` updated.
10. `tools/stamp_time.py` named in the runbook Time rule and 4.1, `creation-nights.md` and `night-turn.md`, in place of `TZ=America/Los_Angeles date`.
11. `creation-runbook.md` 4.1: log that Night 3 closed first, then the close order (timing, commit `Creation night 3b: <name> closed`, pull with rebase and autostash, push); nothing after the push.
12. `creation-runbook.md` Commit forms: forms for the 3a.4 blocked night, the Year 1 clock (Night 3b's close), the checker's `lock.md` states and `LOCKED.md`; 3a.4 uses its form; `checker.md` names its forms.
13. `engine/rules/powers.md` Hidden powers rules: a knack bullet (every god has two or three, kept in the same sealed file, named on no card before it surfaces; how it surfaces and is added to the card under the hidden powers heading marked "knack"); the sealed-folder line names knacks.
14. `engine/style/house-style.md` (and runbook 3a.4): answered. A layer that is one small gallery, or a few hollows with no regions of its own, is not painted; it stays as data with no `painting`, `draw` draws no sheet, and its hollows are told in words.

### Also

- `tests/tools/README.md`: the fixes' tests noted.
- Notes 1 to 13 needed no change. `npc-god-rubric.md` section 12's variety-table tie roll is left as is (note 13; decision 9 covers the survey blend only).
- Results: `python3 tests/tools/run.py` 61 passed, 0 failed (pytest the same); `python3 tools/lockcheck.py sim-04 --all` 0 failures in every check, 16 places warnings, unchanged. sim-04's own `sealed-terms.txt` was not changed.
