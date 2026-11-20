# Build 2 check: continuity checker

Checked 2026-11-19 against build 2 at commit c578820 (main). Engine audit, not a campaign. This file holds procedure and sealed references by file and line; it is written check by check.

Sealed files read: everything in `SPOILERS_do_not_open/keeper/` except `deep-lore.md` (existence confirmed only). No campaign sealed folder was opened.

## Check 1. Coverage

Scope: 92 items (100 less the five marked no change, 43, 64, 72, 90, 99, and the three that only ask Michael to read rulings, 28, 48, 58), plus the plan's sixteen decisions. Each item was traced to the file and line that carries it.

Result: 83 items applied as the plan says. 9 items applied only in part or against the plan (6, 14, 30, 31, 79, 86, 91, 94, and decision 15 with its clock value). One decision cannot be verified within this check's limits (decision 11, the deep-lore comparison). Two housekeeping notes.

### Applied in part, or against the plan

1.1 **Item 6 (god-sense per campaign) not carried into `engine/rules/messages.md:9`.** It still says god-sense "tells a god that others exist and roughly where", a fixed content. DESIGN 1.5 (`DESIGN.md:15`) and 7.2 (`DESIGN.md:136`) now say god-sense is set per campaign by the vote and nothing else. Fix: "God-sense (7.2), as set for the campaign, carries no words."

1.2 **Items 30 and 31, decision 5 (what `player/world-rules.md` holds): four files, three versions.**
- `DESIGN.md:49` (4a): god-sense, bodies, and the god's own power limits.
- `engine/creation/day2-the-god.md:14`, `engine/night/creation-nights.md:37`, `engine/creation/day3-the-people.md:28`: god-sense, bodies, and the pricing terms for mortal magic (simple, costs the worker).
- `SPOILERS_do_not_open/keeper/creation-runbook.md:130` and template 7.9 (`:619` to `:634`, "Nothing else goes in this file"): god-sense and bodies only. `survey-keeper-notes.md:37` agrees with the runbook and puts the magic pricing terms in the Day 3 brief instead (runbook `:214`).
- `survey-keeper-notes.md:29` lists the god's own power limits as given before Day 2, but no template carries them to the player before Day 2; the runbook gives them to NPC gods in the Night 2 release (`:148`) and the DM states them on Day 2.
`applied.md:46` says the engine side was reconciled to "world-rules carries magic's pricing terms only"; the runbook template and the Keeper notes were not. A Keeper following the runbook writes a file the Day 2 guide says is incomplete. Fix: pick one list and put it in all six places. Also note the tension that Q7 (what magic costs) is on the discovered side of the table (`survey-keeper-notes.md:31`) while "it costs the worker" is given.

1.3 **Item 14 (no meaningless odds and success on table rolls) applied for dice only.** `tools/roll.py` has no plain 1 to 100 mode. The runbook routes leans, the star's phase ("a d100 table ... a plain roll"), the scale variation roll and the plane's phase rolls through plain rolls (`creation-runbook.md:19`, `:63`, `:74`, `:675`), which in the tool are contest mode (`roll.py:161` to `:175`) and log `base: 50`, `odds: 50` and `success`. That is the exact shape item 14 asked to remove. Fix: a `--d100` (or `--die d100`) mode that logs the roll and no success.

1.4 **Item 79 and decision 2 (continent scale): an old small-sheet default remains.** `tools/map.py:86` sets `DEFAULT_MPP = 0.25` miles per pixel (a sheet about 256 miles across), while `engine/rules/map.md:66` sets a continent at 2 to 4 miles per pixel. `validate` (`map.py:399` to `:437`) does not require `miles_per_pixel`, so a map that omits it draws a scale bar and gazetteer distances about ten times too short. Fix: default in the continent range, or have `validate` fail a missing scale.

1.5 **Item 86 and the plan's map spec ("public map-knowledge files carry opaque ids and grid cells only, never coordinates", `build-plan.md:30`): applied for rumors only.** `engine/rules/map.md:101`, `:109`, `:122` and `:123`, and `tools/map.py:33` to `:34` and `:1245`, allow a reported entry in the public `player/map-knowledge.json` to carry `told.coords` or `told.polygon` in painting pixels. `DESIGN.md:184` (11.4) says the file holds "opaque ids and grid cells only, never coordinates". `creation-runbook.md:282` narrows the rule to "never coordinates for rumors", siding with the tool. An accurate report written with coordinates is a true sealed coordinate in a public file. `tests/tools/README.md:39` records this as intended ("Reported told shapes in pixels stay"). Michael's call: either DESIGN 11.4 and the plan are amended to "no coordinate for a rumor", or reported shapes move to cells.

1.6 **Item 91 (the checker locks): the runbook's lock section disagrees with the engine on the flags file.** `creation-runbook.md:357` says the checker's lock flags file "sits in the public folder and the leak scan reads it", with detail to `S/lock-flags.md`. `engine/roles/checker.md:25` and `engine/night/creation-nights.md:54` put lock flags in `S/years/000/lock-flags.md` (sealed) and a one-line public `P/years/000/lock.md`. Two paths and two visibility rules for one file. `applied.md:46` lists the reconciliation for creation-nights, day2, day3 and checker.md, not the runbook. Also `DESIGN.md:103` (5.7) still says the checker "writes nothing", against `DESIGN.md:227` (15.2) and `checker.md:3`, `:25`.

1.7 **Item 94 with decision 11 (place ids for the plane): the lock script fails a correctly written plane id.** `tools/lockcheck.py:120` to `:125` (`map_ids`) collects region, feature and layer ids but not `plane.starfalls` ids. The runbook requires plane entries to be named by id (`creation-runbook.md:311`, `:687`) and every place to carry a bracketed id, and its lock line `:368` says every plane entry referred to must exist in `map.json`. A bracketed `[p01]` in the deep history fails `--places`. Reproduced on a scratch copy of the fixture (1 failure). `map.py` `check_world` also does not validate plane ids. Fix: add plane ids to `map_ids` and to `check_world`.

1.8 **Decision 15 (clock): the night value `3b` is outside the spec.** `build-plan.md:33` and `tools/check.py:8`, `:35` to `:36` allow `creation_night: 1|2|3`. `engine/night/creation-nights.md:49` and `creation-runbook.md:289` set `creation_night: 3b`. `check.py` reports a clock fault on every 3b clock (reproduced). Either the spec admits `3a|3b` or the night stays `3` across both sittings. See also 6.4.

1.9 **Item 8 (failures checks during creation): two lists.** `engine/roles/dm.md:16` names inventing, acting for the player, lists of loose threads, flattery, pointing at signs and dashes. `engine/rules/failures-checklist.md:7` adds 13, invented drama. Small; make them one list.

### Not verifiable here

1.10 **Decision 11, the deep-lore comparison** (the lore must differ from the 2012 story and the original Telegram game). `applied.md:44` records only the god-sense change to `deep-lore.md`; no file records the comparison's outcome. This check does not open `deep-lore.md`, so it cannot say whether the comparison was done. `DESIGN.md:76` carries the rule. Ask the sealed-side agent for a one-line record of the result.

1.11 **Items 6 and 18 in `deep-lore.md`** (god-sense no longer fixed by the lore): logged at `applied.md:44`, not opened here. `survey-keeper-notes.md:5` and `clue-design.md:13` agree with it.

### Housekeeping

1.12 `tests/creation-sim/run-01/changes.md:7` to `:105`: the Status column still reads `proposed` for items 1 to 99, while `tests/creation-sim/README.md:26` and the plan say all 100 are applied. Michael approved them (`build-plan.md:3`); the column should read applied.

1.13 Items whose application was confirmed, by file: 1 to 5 (`day1-world-survey.md:27` to `:43`, `DESIGN.md:48` to `:50`); 7 (`DESIGN.md:67`); 9 and 22 (`CLAUDE.md:11`); 10 (`creation-nights.md:7` to `:20`, `night-turn.md:7`, `scheduled-prompt.md`); 11 (`tests/creation-sim/README.md:18`); 12 (`roll.py:91` to `:105`); 13 (`creation-runbook.md:18`); 15 (`npc-god-rubric.md:80` to `:83`); 16 (`creation-runbook.md:85` to `:87`, `:483` to `:502`); 17 (`day1-world-survey.md:20`, `creation-runbook.md:113`); 19 (`creation-runbook.md:50`); 20 (`npc-god.md:7`, `keeper.md:7`); 21 and 59 (`creation-runbook.md:21`, `roll.py:108`); 23 (`creation-runbook.md:91`, `:420`); 24 to 27 (`survey-keeper-notes.md:39` to `:70`); 29 and 75 (`creation-runbook.md:59` to `:68`); 32 to 36 (`creation-runbook.md:28` to `:46`, `:89` to `:97`, `:131`); 37, 41, 56 (`powers.md:11` to `:70`); 38 (`creation-runbook.md:169`); 39, 40, 42, 50, 51 (`day2-the-god.md:24` to `:31`, `:43`); 44 to 47, 49, 53 to 55 (`creation-runbook.md:144` to `:183`, `:504` to `:553`); 52 (`night-turn.md:41`, `npc-god.md:28`, `powers.md:184`); 57 (`creation-runbook.md:13`, `powers.md:185`); 60 (`DESIGN.md:198`, `keeper.md:30`); 61 (`dm.md:5`); 62 and 98 (`creation-runbook.md:187` to `:212`); 63 (`creation-runbook.md:202`, `:213`); 65 to 71 (`day3-the-people.md`, `creation-runbook.md:239` to `:246`); 73, 84 (`DESIGN.md:177` to `:178`, `map.md:11`); 74 (`tools/paint.py:15` to `:16`, `paint.yml:4`, `house-style.md:27`); 76 (`survey-keeper-notes.md:72` to `:101`, `roll.py:39`); 77, 81 (`creation-runbook.md:234` to `:236`); 78 (`creation-runbook.md:230`, `:261`); 80 (`DESIGN.md:193`); 82 (`creation-runbook.md:13`, `:185`); 83, 93 (`DESIGN.md:177`, `creation-runbook.md:264`, `:273`, `checker.md:21`); 85 (`map.md:30` to `:46`, `map.py:399` to `:437`); 87 (`npc-god-rubric.md:108` to `:131`); 88 (`creation-runbook.md:357` to `:359`, `:653` to `:664`); 89 (`house-style.md:15` to `:27`); 92 (`lockcheck.py:199` to `:316`); 95 (`creation-runbook.md:583` to `:617`, `lockcheck.py:373` to `:392`); 96 (`mystery-standard.md:22`); 97 (`creation-runbook.md:378`); 100 and decision 14 (`DESIGN.md:129`, `powers.md:150` to `:176`, `creation-runbook.md:636` to `:651`); decision 7 oaths (`DESIGN.md:141`, `day1-world-survey.md:32`, `survey-keeper-notes.md:141`, `npc-god.md:16`); decision 12 engage (`night-turn.md:12`, `dm.md:24`, `check.py:93` to `:113`); decision 16 labels (`creation-runbook.md:11`).

## Check 2. Contradictions between files

Result: 14 findings (4 that would change what a run produces, 10 smaller). The hand-offs between days and nights match: Night 1 reads exactly what the Day 1 close writes; Night 2 reads exactly the Day 2 close list; Day 2 reads what Night 1 leaves; Day 3 reads what Night 2 leaves; Night 3a reads the Day 3 close list; 3b reads what 3a writes. The grep for "oath", "sworn", "god-sense", "senses that others", "question 16" and "15 rules" over every file read found the oath cut and the bodies question carried everywhere, no "15 rules" and no "senses that others"; the one stale god-sense line is 1.1.

### Paths and formats

2.1 **Lock flags path and visibility.** See 1.6: `creation-runbook.md:357` (public flags file, detail in `S/lock-flags.md`) against `checker.md:25` and `creation-nights.md:54` (`S/years/000/lock-flags.md`, sealed, plus public `P/years/000/lock.md`).

2.2 **`world-rules.md` content.** See 1.2: three versions across `DESIGN.md:49`, `day2-the-god.md:14`, `creation-nights.md:37`, `day3-the-people.md:28`, `creation-runbook.md:130` and `:619` to `:634`, `survey-keeper-notes.md:29` and `:37`.

2.3 **Clock `creation_night` value.** See 1.8: `creation-nights.md:49`, `creation-runbook.md:289` (`3b`) against `build-plan.md:33`, `check.py:8`, `:35`. Also the starting clock in `creation-nights.md:11` to `:16` has no `season_opens`, which `check.py:39` to `:41` requires; the runbook sets it only in 3b.8 (`creation-runbook.md:346`).

2.4 **Waited note name.** The plan says `years/NNN/waited.md` (`build-plan.md:34`); the engine and tools use `years/NNN/waited-YYYY-MM-DD.md` (`night-turn.md:12`, `dm.md:20`, `morning-story.md:77`, `check.py:68` to `:70`). Consistent across every file that uses it, and recorded as a deliberate follow-up at `applied.md:45`. No action, noted only because it departs from the written spec.

2.5 **The knowledge file's coordinates.** See 1.5: `DESIGN.md:184` against `map.md:122` to `:123`, `map.py:33` to `:34`, `creation-runbook.md:282`.

2.6 **`map-meta.json`.** `map.md:201` says the tool writes "the frame used in painting pixels". `map.py:937` to `:946` writes frames as grid cells (`frame_cells`), and `applied.md` says map-meta gives cells, never pixels. The rule file is stale; the tool is right.

2.7 **A rumor with no cell.** `map.md:122` says a rumored entry with no `cell` is drawn at the true centroid's cell. `map.py:390` to `:391` (`knowledge_problems`) fails it, and `reveal` refuses it (`map.py:1180` to `:1181`). Make `map.md` say a cell is required.

2.8 **Message files and the message log are public.** `engine/rules/messages.md:17` stores every message at `campaigns/<name>/messages/<id>.md` and `:44` the log at `campaigns/<name>/state/messages.jsonl`, both under the public folder, for messages between any parties. `night-turn.md:71` lists "the message log" as sealed. Pre-dates build 2, but it is a direct path contradiction and see 4.3.

2.9 **Where NPC civ pass-one releases live.** `night-turn.md:28` writes `releases/NNN/civ-<x>-pass1.md` with no sealed prefix; `night-turn.md:71` lists every NPC god's release as sealed but does not name NPC civ releases. Read literally they land in the public `campaigns/<name>/releases/`. See 4.3.

### Who writes what

2.10 **The checker writes.** `DESIGN.md:103` (5.7) says the checker writes nothing; `DESIGN.md:227`, `checker.md:3`, `:25`, `:29` give it the lock files, `LOCKED.md` and the yearly flags. DESIGN 5.7 needs the build 2 wording.

2.11 **Which commit `LOCKED.md` names.** `checker.md:25` says "the commit id of the lock commit"; `DESIGN.md:227` says "the lock's commit id"; `creation-runbook.md:357` and `:659` say the commit the checker checked, with `LOCKED.md` committed alone after it. Only the runbook is unambiguous (a commit cannot carry its own id). Align the other two to "the checked commit".

2.12 **NPC god instruction files during negotiation.** `engine/roles/npc-god.md:9` says the god's release on the creation nights is `releases/creation/<you>-night1.md`, `-night2.md` or `-night3.md` and "it is your whole instruction". The negotiation rounds come in a different file, `S/releases/creation/<god>-night2-negotiation.md` and `-night3-negotiation.md` (`creation-runbook.md:170`, `:236`), which the role file never names. See 6.3 for the permission effect.

2.13 **Release templates that do not name the file to write.** Template 7.4 (`creation-runbook.md:483` to `:500`) never names `S/gods/<god>/survey-day1.md`; the answer format is given below the template block (`:502`), outside what the god receives. Template 7.6 (`:529` to `:551`) never names `negotiation-night2.md` or `negotiation-night3.md`; that line is outside the block too (`:553`). Templates 7.5 (`:521`) and 7.7 (`:576`) do name their files. Under `CLAUDE.md:11` the release is the god's go "for exactly the files that release ... names". See 6.3.

### Given and discovered

2.14 **The DM's first release and god-sense.** `creation-runbook.md:348` puts "god-sense as set" in `P/releases/000/dm.md`. If the campaign's god-sense gives a felt pull per god at a distance, the release states how many pulls, which is the count of gods that `DESIGN.md:14` and `:192` say the player never learns. No file says how god-sense is reported without giving a number. `clue-design.md:142` shows the test world doing exactly this ("three pulls felt"). See 4.1.

Also checked and consistent: the roll id format (`r-NNNN`, `roll.py:40`, `lockcheck.py:38`, `creation-runbook.md:18`); the power card format (`powers.md:11` to `:66` against `day2-the-god.md:57` to `:66` and `creation-runbook.md:183`); the growth file (`creation-runbook.md:636` to `:651` against `powers.md:150` to `:166` and `build-plan.md:36`); the mystery template (`creation-runbook.md:583` to `:617` against `mystery-standard.md:26` and `lockcheck.py:33`); `map.json` fields (`map.md:27` to `:61` against `map.py` and `creation-runbook.md:261`); the sealed folders (`creation-runbook.md:13`, `keeper.md:14`, `npc-god.md:3`, `powers.md:185`); the negotiation files (`build-plan.md:27`, `creation-runbook.md:170` to `:176`).

## Check 3. Tools against rules

Run: `python3 tests/tools/run.py` passes 13 of 13. `python3 tools/lockcheck.py --help` prints the five checks, `--all`, `--root` and `--counts-only`. Two behaviors below were reproduced on a scratch copy of the test fixture outside the repository, then deleted.

Result: 15 findings (3 that would fail or mislead a real lock, 12 smaller).

### `tools/map.py` against `engine/rules/map.md`

Agrees: opaque ids (`map.py:68`, `map.md:68`); grid 5 by 4 by default, lettered on four edges, the same cells on a cropped sheet (`map.py:66`, `:591` to `:630`; `map.md:66`, `:210`); rumors carry `told.name` and `told.cell` and never a pixel (`map.py:387` to `:393`, `:1172` to `:1181`); roads as a line feature drawn thin, dashed when reported (`map.py:692` to `:715`); landings validated against regions (`map.py:433` to `:436`); plane ignored by the drawer; gazetteer gives cells and miles and travel days between known neighbors (`map.py:975` to `:1027`); underground sheets on the same grid and fog (`map.py:916` to `:935`).

3.1 **A rumor revealed without `--name` takes the Keeper's true name.** `map.py:1179` (`kept.setdefault("name", truth["name"])`). `map.md:68` says the god "learns names only through `told` and through seeing", and a rumor is the name as told. Reproduced: the public file then holds the sealed name. The leak scan cannot see it, because every `told.name` is counted as known (`lockcheck.py:237` to `:239`). Fix: `reveal` refuses a rumor with no `--name`, as it refuses one with no cell.

3.2 **Plane ids are not map ids to the lock script.** See 1.7 (`lockcheck.py:120` to `:125`); `check_world` (`map.py:399` to `:437`) also checks no plane id.

3.3 **Scale default.** See 1.4 (`map.py:86`).

3.4 **`validate` checks less than the rules require.** `check_world` (`map.py:399` to `:437`) does not check that every region has `elevation`, `water` and `climate` (`map.md:67`, `creation-runbook.md:261`), that regions tile without gaps or overlaps (`map.md:67`), or that `miles_per_pixel` is set. A traced map missing these passes `validate` and `--places`.

3.5 **Reported coordinates in the public file.** See 1.5. The tool and `map.md` agree with each other and not with `DESIGN.md:184`.

3.6 **Dates in UTC.** The map log line (`map.py:1188`, `datetime.date.today()`) and `map-meta.json`'s `drawn` (`map.py:945`) use the machine's date, which is UTC on the overnight machine and a day ahead of Pacific late at night (run 01 item 21). The plan says every logged real time is Pacific (`build-plan.md:35`).

3.7 **`map-meta.json` doc.** See 2.6 (`map.md:201`).

### `tools/roll.py` against the runbook's standing rules and `keeper.md`

Agrees: `--campaign` writes the sealed log (`roll.py:62` to `:67`; `creation-runbook.md:18`; `keeper.md:34`); ids `r-NNNN` per log, printed and logged before the result is shown (`roll.py:91` to `:105`); `--die d6|d8|d10|d12|d20|d30` with automatic rerolls logged as their own lines with reason and `replaces` (`roll.py:148` to `:159`); `--reason` and `--replaces` required together and checked against the log (`roll.py:132` to `:141`); `pacific` beside UTC `time` (`roll.py:108` to `:110`).

3.8 **No plain roll.** See 1.3. Leans, the phase, the variation and the half-median rolls log `odds` and `success` they do not have.

3.9 **A roll without `--campaign` lands where no check looks.** The default log is `state/rolls.jsonl` at the repository root (`roll.py:67`). `check.py:142` to `:144` and `lockcheck.py:436` to `:438` check the public campaign log `campaigns/<name>/state/rolls.jsonl` instead. A Keeper that forgets `--campaign` writes a public, unchecked roll, which is the failure item 13 was about. Fix: refuse to roll without `--campaign` (or `--log`), or have both checks look at the root log too.

3.10 **Two dice for one result share a name.** `check.py:129` to `:141` and `lockcheck.py:420` to `:427` treat two first rolls with the same `--what` as "rolled more than once". The ceiling shading rolls two d10 and keeps one (`survey-keeper-notes.md:95` to `:99`). The runbook's "name every roll plainly" (`creation-runbook.md:18`) covers it only if the Keeper names the two dice differently; say so at 1.6.

### `tools/lockcheck.py` against the lock checklist and the mystery template

Agrees: the seven required headings, in the template's words (`lockcheck.py:33`; `creation-runbook.md:591` to `:614`); `--places` on bracketed ids and bare map names (`lockcheck.py:151` to `:187`); `--leaks` builds the term list the plan names (god names and labels, the count of gods, unknown places, phenomena counts, mystery and schedule titles, star values; `lockcheck.py:199` to `:302`) and runs the knowledge-file rules; `--rolls` and `--dashes`.

3.11 **`--mysteries` checks less than the lock line it is cited for.** `creation-runbook.md:372` says `--mysteries` passing means "one epic, several long, many short", every clue placed with its readings, every branch with the world's answer. The script checks that the headings exist, that the Clues section holds the word "reading" once and that the Branches section holds "world does" once (`lockcheck.py:373` to `:392`). It does not read the `Kind:` line, count kinds, check each clue's `Location:`, check every branch, or check the rule 16 `Limit:` line (`creation-runbook.md:617`). The checker's reading covers these, but the runbook should not credit the script with them.

3.12 **`--leaks` limits.** The term list does not include the player's or any NPC's hidden power names, the sealed common-past names (`creation-runbook.md:194`), or the count of gods written other than as "N gods" (for example "seven pulls", "the seven of us"). It scans only `campaigns/<name>/`, so the public scene requests in `images/requests/<campaign>-*.json` are never scanned. The checker's line-by-line read (`creation-runbook.md:377`) is the only guard for these.

### `tools/check.py` against `night-turn.md`

Agrees: dated waited notes (`check.py:68` to `:70`, `night-turn.md:12`); a waited year leaves the clock where it was (`check.py:106` to `:108`); the timing rule (`check.py:49` to `:65`) reads the lines `night-turn.md:12` and `:66` say to write; clock fields `campaign`, `year`, `status`, `creation_night`, `season_opens`; the morning painting request path (`check.py:120`, `night-turn.md:61`); the public rolls log empty.

3.13 **The engage rule is not checked.** `checker.md:18` says the year turned only if a decisions file existed. `check.py` never looks for `player/decisions-NNN.md`; a year that turned with no decisions file and no waited note passes.

3.14 **The timing rule can misfire.** `night-turn.md:12` asks for "a line containing 'waited'" with no Pacific date on it; `check.py:55` to `:60` files an undated line under the last date above it, which may be a day that did advance. And `ADVANCE_RE` (`check.py:46`) also matches any line like "turn started, year 3 open", which step 0 (`night-turn.md:11`) invites. Say in `night-turn.md` that each timing line starts with its Pacific date, and match only "clock advanced".

3.15 **`check.py` cannot pass during creation.** It always reports "campaign is in creation ... no resolved year to check" (`check.py:104` to `:105`), plus the `3b` clock fault and missing year outputs when run at the lock (reproduced: 6 findings on a clean fixture with a 3b clock). `checker.md:9` tells the checker to run it before the lock. See 6.5.

## Check 4. Leaks by design

Each player-facing file the engine says to write was read against DESIGN 12.2 (`DESIGN.md:192`: no vote, pool, other god, count of gods, deep history, star, mystery, schedule, hidden power, or a phenomenon's count before seen).

Clean by their own rules: `world-rules.md` (template `creation-runbook.md:619` to `:634`, facts of being a god, never as a vote); `day3-brief.md` (`creation-runbook.md:213` to `:215`: no names, no history, no other gods, no distance); the follow-ups (`creation-runbook.md:131`, "no question may reveal a vote, a pool, another god or anything from `S/`"); `world.md` (`creation-runbook.md:344`); `lock.md` (one line, `checker.md:25`); waited notes (one line, `night-turn.md:12`); the gazetteer (cells and miles only, `map.py:970` to `:972`).

Result: 6 findings, 3 of them real routes for sealed content into the public folder.

4.1 **God-sense in `P/releases/000/dm.md` can state the count of gods.** See 2.14 (`creation-runbook.md:348`, `clue-design.md:142`). If the vote gives a pull per god at a distance, the first release and the first morning story report one pull per god. Nothing in the engine says how to give god-sense without a number, and the leak scan's count pattern (`lockcheck.py:226` to `:229`) matches only "N gods". This needs a design rule (for example, a pull is felt as direction and weight, never as a tally), in DESIGN 7.2 and the runbook.

4.2 **Yearly flags are public and are written after the leak scan.** `checker.md:29` writes flags to `campaigns/<name>/years/NNN/flags.md`, each with "what the record says instead", and `night-turn.md:71` lists flags as public. `checker.md:25` itself says lock flags must be sealed "since flags name sealed things"; the same is true of yearly flags. The leak scan runs in step 5 (`night-turn.md:48`) before the checker writes them (`night-turn.md:49`). Fix: yearly flags to `S/years/NNN/flags.md`, with a public one-line note if needed.

4.3 **Messages, the message log and NPC civ releases in the public folder.** See 2.8 and 2.9 (`messages.md:17`, `:44`; `night-turn.md:28`). A message between two NPC gods, or an NPC people's pass-one release, written where the rule file says, names another god and its people in `campaigns/<name>/`. The leak scan would fail it every night by god name, so in practice it would block rather than leak; still, the rule files send it there. Also `night-turn.md:42` updates `state/` with "population, stores, messages, map knowledge per god", with no sealed prefix for the NPC peoples' numbers.

4.4 **The leak scan runs before the files it should guard are written.** DESIGN 12.2 (`DESIGN.md:192`) says the script runs "before every lock and every morning", and `keeper.md:46` says before pushing. In the night turn it runs in step 5 (`night-turn.md:48`), before the releases (step 6), the morning story, the closing and the chronicle (step 7), and the close (step 8) has no second scan. In creation, the first morning story is written after the lock (`creation-nights.md:55`, `creation-runbook.md:348`) and is never scanned. Fix: run `--leaks --dashes` again as the first line of step 8 and after the first morning story.

4.5 **Reported coordinates and the default rumor name in `map-knowledge.json`.** See 1.5 and 3.1. An accurate report given with `told.coords` puts a true sealed coordinate in the public file (`map.md:122` to `:123`); a rumor written without `--name` puts the Keeper's sealed name there (`map.py:1179`), and the scan treats it as known.

4.6 **The full lockcheck output.** `tests/tools/README.md:46` says findings name sealed terms and stay sealed, with `--counts-only` for public records. Nothing in `checker.md` or the runbook says where the checker keeps the full output at the lock; the runbook's current lock section (`creation-runbook.md:357`) puts the flags file in the public folder. Settled once 1.6 is fixed.

Not leaks: `P/state/models.md` and `P/state/timing.md` carry no sealed term by their rules, and the scan covers them. The DM's release carries the god's senses by design (`keeper.md:26`).

## Check 5. Dashes

Every file read for this check was scanned for U+2014 (em dash) and U+2013 (en dash): `CLAUDE.md`, all of `engine/`, `tools/*.py`, `.github/workflows/*.yml`, `tests/tools/` (README, tests, fixtures), `tests/creation-sim/README.md`, everything in `tests/creation-sim/run-01/`, and the five sealed Keeper files read (`creation-runbook.md`, `survey-keeper-notes.md`, `npc-god-rubric.md`, `mystery-standard.md`, `clue-design.md`). 63 files.

Result: 0 dashes. `deep-lore.md` was not scanned, since it was not opened.

## Check 6. Unattended runs

Question: could a fresh overnight session run `engine/night/creation-nights.md` and the runbook end to end, with no human present, under `CLAUDE.md` as written?

Result: no. 5 steps would stall or loop, 2 depend on a go that cannot arrive overnight, and 3 carry risk.

### Would stall

6.1 **Nothing starts the session.** `engine/night/scheduled-prompt.md:3`: the scheduled task holds the older prompt and is paused; installing the new one needs Michael's go (also `DESIGN.md:240`). By design, but until then no creation night runs.

6.2 **God agents have no named file to write on Night 1 and in every negotiation round.** `CLAUDE.md:11` gives an agent its go "for exactly the files that release or role file names". The Night 1 release template does not name `survey-day1.md` (`creation-runbook.md:483` to `:500`); the negotiation template does not name the reply file (`:529` to `:551`); and `npc-god.md:9` calls the night release the god's "whole instruction", which leaves out the negotiation release. A god agent that reads `CLAUDE.md` strictly has no go to write its answers (run 01 item 22 saw agents deliberate over exactly this). Fix: each template names its output path inside the block, and `npc-god.md:9` names the negotiation release and the `day3-questions` follow-up as instruction files.

6.3 **The lock cannot pass.** `checker.md:9` tells the checker to run `tools/check.py <campaign> <year>` first and carry every finding into the flags; `creation-runbook.md:361` requires every line yes. During creation `check.py` always reports findings (3.15), so a literal checker never writes `LOCKED.md`. Fix: `checker.md` says `check.py` is for resolved years and is not run at the lock, or `check.py` gains a creation mode.

6.4 **The paintings have no wait and no failure path.** 3a.4 commits the requests to `SPOILERS_do_not_open/images/requests/` (`creation-runbook.md:257`); the GitHub job paints and pushes (`paint.yml:1` to `:23`); 3a.5 begins "when the sheets return" (`creation-runbook.md:261`). No file says how the session waits, for how long, or what to do if the job fails (`paint.py:52` to `:54` exits on any HTTP error, for example billing). A failed job leaves 3a waiting until 6:30, with no night-blocked note and Day 4 unready. Also the job's own push lands on main while the session holds local commits, so the session's next push is rejected until it pulls; no step says to pull and rebase.

6.5 **No deadline or fallback for an unlocked world.** The night turn stops its check loop at 6:00 and posts a notice (`night-turn.md:50`); the creation lock has no time limit and no rule for 6:30 if flags remain (`creation-nights.md:54` to `:55`, `creation-runbook.md:357` to `:361`). The clock stays `status: creation`, the next overnight session reruns "the night the clock names" (3b), and nothing tells the 6:30 wake or the DM what Day 4 is.

### Need a go that cannot arrive overnight

6.6 **The repaint.** `creation-runbook.md:264` holds the request in `requests/held/` until Michael's go "before 3b ends". Correctly safe (`paint.py:25` reads only the top folder, so a held file is never painted), and the fallback (trace the sheet in hand) runs on. But with no human present the go never comes, so the repaint path is dead in an unattended night. If it is ever used, the repaint needs a new request id: `paint.py:27` to `:29` skips a request whose output already exists.

6.7 **Decisions marked for Michael.** `creation-runbook.md:384` to `:386`: the Keeper decides, logs and goes on. Not a stall. Noted because it means an unattended run will carry Keeper rulings Michael has not seen into the lock.

### Risks

6.8 **`sim-01` would be picked up every night.** `campaigns/sim-01/state/clock.md` says `status: open`, year 1. The new prompt runs every campaign whose clock says open or creation (`scheduled-prompt.md:13`), so each night it would run the night turn on sim-01, find no decisions file, and write a waited note and timing line into a campaign the test README calls the locked record of run 01 (`tests/creation-sim/README.md:26`). Set sim-01's clock to `status: closed` (with Michael's go) before the prompt is installed.

6.9 **Spawning.** The night session must spawn seven god agents, then the checker and the DM (`creation-nights.md:26`, `creation-runbook.md:23`). The prompt says "where the Agent tool allows" (`scheduled-prompt.md:17`); if the scheduled session cannot spawn, there is no fallback.

6.10 **Commits and pushes.** `CLAUDE.md:7` lists commits and pushes among what needs Michael's go; the run exception in `CLAUDE.md:11` speaks of files. `creation-nights.md:27`, the runbook's close checks and the prompt all require pushing. One sentence in `CLAUDE.md` ("including the commits and pushes the design assigns") closes the gap.

Not a stall: models (`creation-runbook.md:347`; `campaigns/sim-01/state/models.md` exists to copy from); the night-blocked path (`creation-nights.md:25`, `scheduled-prompt.md:21`); the Pacific clock (`creation-nights.md:31`).

## Verdict

Not ready for creation simulation run 02 as an unattended overnight run. Ready for a run 02 driven by the orchestrator, as run 01 was, once the must-fix items below are made, because the orchestrator stands in for the missing waits and spawns.

Must fix before run 02:
1. One list for `world-rules.md` in all six files (1.2).
2. One lock flags path and visibility, runbook matching `checker.md` (1.6, 2.1), and DESIGN 5.7 updated (2.10).
3. Plane ids accepted by `lockcheck --places` and `map.py validate` (1.7).
4. `check.py` not run at the lock, or given a creation mode, and the `3b` clock value settled one way (1.8, 3.15, 6.3).
5. Output paths named inside the Night 1 and negotiation release templates, and the negotiation release named in `npc-god.md` (2.12, 2.13, 6.2).
6. `map.py reveal` refuses a rumor with no told name (3.1).
7. A rule for reporting god-sense without a count (2.14, 4.1).
8. The leak scan rerun after the morning story and before the close push (4.4), and yearly flags sealed (4.2).
9. Michael's call on reported coordinates in the public knowledge file (1.5).

Should fix (cheap): the god-sense line in `messages.md` (1.1); a plain d100 mode in `roll.py` (1.3); refuse rolls without `--campaign` (3.9); the scale default and `validate` fields (1.4, 3.4); Pacific dates in `map.py` (3.6); stale `map.md` lines (2.6, 2.7); the creation failures list (1.9); the `changes.md` status column (1.12); the `check.py` timing pattern and the engage-rule check (3.13, 3.14).

Before any unattended run, also: install the prompt (6.1), close sim-01's clock (6.8), and give 3a a wait, timeout and failure path for the paintings and the lock (6.4, 6.5).

Every change above is a change to the engine, the tools or the Keeper's standing files and needs Michael's go.
