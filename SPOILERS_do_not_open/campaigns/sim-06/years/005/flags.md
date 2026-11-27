> SPOILER WARNING. Sealed. Year 5 continuity flags for campaign sim-06. Players must never read this file.

# Continuity flags: sim-06, Year 5

Rounds 1 to 3. Status now: raised 11, resolved 10, open 1. By severity, as raised: major 0, moderate 2, minor 9. Open: flag 11 (minor, the Keeper's, one word in `P/releases/005/dm.md`). The check fails until it is fixed; it needs no rework of the year and nothing told to the player turns on it.

## Round 1

Run by the continuity checker at the check step of the Year 5 night turn (run 07 Part B, build 7, its last night), 2026-11-26, written at 22:46 Pacific, against commit cfabad6 ("sim-06 Year 5 night: pass two, the year record, the releases and the held moment's board"). Pulled first; already up to date. Every check below was made against the files, not against the keeper log's word. Steps 6 and 8 are not written yet (the Year 6 morning story, the Year 5 closing, the chronicle's god side, the held painting request, the clock). Findings that wait on them are not failures now.

Read in full: `CLAUDE.md`, `engine/roles/checker.md`, `engine/night/night-turn.md`, `engine/rules/failures-checklist.md`, `S/keeper/year-turn.md`, `S/rulings.md`, `tests/creation-sim/run-07/plan.md`, the Year 4 flags (standing rulings), the keeper log from "Year 5 night turn", `S/years/005/year.md`, `P/releases/005/dm.md`, `S/releases/005/dm-sealed.md`, `S/releases/004/dm-sealed.md` (both boards the day was played under), `P/releases/005/civ-unnamed-people-pass1.md` and `civ-unnamed-people.md`, `S/releases/005/civ-unnamed-people-sealed.md`, `P/civs/unnamed-people/years/005.md`, the people's state diff, the people's chronicle addition, the tide-reckoner's and the master of the potters' people files, `P/player/transcript-year-005.md`, `decisions-005.md`, `pending.md`, the Year 5 sections of `rolling-save.md` and `conduct-profile.md`, the Year 5 diff of `S/player/unsaid.md` with its `## Act` entry, the ledger L-0052 to L-0056, the eight growth diffs, the sealed roll log r-0408 to r-0464, `S/state/phenomena.json` by the tool, the Year 5 message log lines, the Sarrow's Year 5 file and report, the spring town's report, `S/releases/005/civ-sarrow.md`, `god-thresholds.md`, `civ-unnamed-people-rivers.md`, `god-rivers.md`, the seven NPC pass-one releases (sky sections), and god-thresholds's decisions. Read by search and in part: the spring town's year file and state, the other god and civ releases, the seven decisions, `m-0012.md`, the people's public report, the sealed people's folder, the hidden powers file, mystery L05, the event schedule's random table, the Years 2 to 4 records on the coaster's master, the map.

### Scripts

- `tools/check.py sim-06 5 --step 7`: 2 findings, 1 note. The findings are the missing morning story (`P/years/006/morning-story.md`) and the missing painting request. Both are step 6. Not flags now. The note is the public roll log's old ids (DM r-0001 to DM r-0015), standing since Year 1.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning; dashes 0. The warning is the standing `dim-nights` label allow. Every public dim-night line written tonight was read for meaning: Year 3's six is given now that Year 3 is told whole and the god saw each night; Year 4 gives months and no count. Not a flag.
- `tools/lockcheck.py sim-06 --all`: 1 failure, 98 place warnings, 8 release warnings, 1 roll note. The failure is in `S/years/004/flags.md` line 206, a bracketed word in a quoted ruling read as a place id. The role says the scripts skip the flags file and findings inside it never count, so this is a tool fault, not a campaign flag: the place scan does not skip an earlier year's flags file. Reported for the coordinator. The place warnings are map names without ids in sealed files only. The release warnings are salt and iron beside a word of scarcity in releases whose readers met that scarcity themselves (the Longwalk's and the Sarrow's own trade, god-beasts's people's telling, the coaster master's trade on the sheet); judged not a world fact the reader lacks.
- `tools/phenomena.py` for Years 3, 4 and 5: dim nights 6 (months 1, 5, 5, 7, 7, 8), 7 (months 2, 3, 4, 8, 10, 11, 12) and 3 (months 2, 2, 7); tide gathering months 2, 8; 1, 8; 1, 9; cranes month 3 each year. Twenty-four dim nights since the arrival, as the releases say.
- `tools/map.py travel` run for: the bend town [f50] to the Ellow's mouth on foot, 109.5 miles, 8 full days, and on to Port Sennet [f75], 97.9 miles, 7 days; Wellen Ford [f47] toward Southhold of Hask [f73] on foot, 215.6 miles, 17 full days; the far end of the Pass Road [f65] to Aldermoot [f70] by horse, 239.4 miles, 13 full days; the first point of the Pass Road to Aldermoot by horse, 117.6 miles, 6 full days; the winter city [f60] to each end of the Pass Road by road. See flag 2.
- The transcript. `P/player/transcript-year-005.md` at cfabad6 is byte for byte the concatenation of the file at c042791, at 423f5c3 and at 8e86a3d, in that order. The file at c042791 begins with the file at 72adea0, bb816d2 and 9bee2fd; the DM's third post as committed at 9c1d958 stands whole inside the file at 423f5c3. All seven sections are present in order (DM, player, DM, player, DM, player, DM). Whole and verbatim.
- Arithmetic. The halves table against r-0436 to r-0446 (larger half = whole times 50 plus a fifth of the roll, in a hundred) and the not-clay column against a twentieth of each fifth spare's green weight: every figure agrees, to the tenth, in all three files that carry it.

### Flags

**Flag 1 (moderate). A condition was added after the die to a board range rolled with the sealed factor, and it narrows the success.**
- Rule: `sealed-factors.md` as `year-turn.md` section 2 applies it to a board (a range that turns on chance for the god or its people is set with the god's steps before the board is written; luck works only through the odds); checker item 5; checker item 3 (no contested outcome reshaped after its roll).
- Where: r-0464, "if the ring sits, it gives the coaster master the first carrying of the hall's word each summer (success = it does)", stated 30, rolled at 35 with player step 1, success. `S/releases/005/dm-sealed.md`, the eleven's parameter ("they take that too, for as long as the town's own carrier is given the same word on the same day") and its reason line ("on equal terms with their own carrier"); `S/years/005/year.md` ("gives her the first carrying on equal terms with its own carrier"). The keeper log's neutrality self-check names the condition as added after the die.
- What the record says instead: the success was written before the die as the first carrying each summer. Her own parameter on the same board wants the word "to go south by her hull first each summer, before any delta hull says it on another port's quay". The same word given the town's own carrier on the same day is not a first carrying: it lets the delta hull say it on the Corrith quay at the same time. So the condition takes from what the roll gave.
- Fix (Keeper, correct the record): give the eleven's answer as the success was written, the first carrying each summer, in the parameter, the outcome line and `year.md`. If the ring's record truly sets terms for it, they had to be written into the success before the die; they were not, so the success stands as written. Nothing played turns on it yet.

**Flag 2 (moderate). The Sarrow riders' ride is priced from the wrong end of the Pass Road.**
- Rule: checker item 9 (every travel time agrees with `tools/map.py travel` for the route its line names); failures checklist 12 and 2.
- Where: keeper log pass two ("the far end of the Pass Road [f65] to Aldermoot [f70] by horse, 239.4 miles, 12.7 days (13 full days)"); `S/releases/005/god-thresholds.md` ("By the road north-east and the river it is 239.4 miles from the road's far end to the river king's town, thirteen days on horse"); `S/years/005/year.md` (the god-thresholds section); `S/messages/m-0014.md` and its line in `S/state/messages.jsonl` (route, "239.4 miles, 13 days on horse by the tool"); `S/releases/005/civ-sarrow.md` ("thirteen days").
- What the record says instead: the riders left from the farthest toll house. The Year 2 ruling in the keeper log placed the two farthest houses "on the Pass Road [f65] in the Kennoch Heights [r02], the last of the Sarrow's hold on it, short of the road's end and short of the Aldermark [r10]". The road's points lie in the Aldermark at its first point (300, 330), in the Kennoch Heights at (340, 270), and in Marle Gorge [r03] from the winter city to its last point (440, 262). So the farthest houses are on the western stretch, toward the Aldermark, and the tool's "far end" (`f65:end`) is the other end, in Marle Gorge, beyond the winter city. From the first point of the road the tool gives 117.6 miles and 6 full days by horse to Aldermoot; from the houses, short of it, a little more. "North-east" is wrong too: from the Sarrow, Aldermoot lies south-west. The phrase came from the Sarrow's own Year 4 file and was carried into a god's release as fact. The riders' outcome (r-0456) and their return before the snow do not turn on the figure, so this is the telling.
- Fix (Keeper, correct the record): price the ride from the Kennoch Heights end, by `tools/map.py travel sim-06 f65:start f70 --by horse` plus the stretch of road from the houses, and correct the five places above; drop "north-east" from the god's release, or give it as the riders' own word. For review: the Year 4 log's "the winter city to the far end of the Pass Road, 68.2 miles" used the same end, and the Year 4 check passed it. That miss is the checker's as much as the Keeper's.

**Flag 3 (minor). god-thresholds's release says nothing is pending; two asks are.**
- Rule: checker item 4 (no release holds more or other than its agent could know); failures checklist 3 (forgetting what was asked of the god); `year-turn.md` section 4 (a question put to a god meets silence and stays pending).
- Where: `S/releases/005/god-thresholds.md`, "Asked of you and not answered: Nothing stands unanswered that reached you."
- What the record says instead: `S/civs/sarrow/years/005-report.md`, "Asked of the god": the Marshal, month 7, at the ford, in front of the older watcher, asked her whether the river's coughing beasts were to be penned apart from the herds, and "the decisions give her no word"; and the third question of month 11 (whether a master with coughing beasts who would not leave them penned apart was to be turned from the sill), which Kessan and Idris answered differently and which waited: "It stays pending until she answers it. The Guest was told when she came down." Her decisions answer neither.
- Fix (Keeper, correct the record): list both asks in the asker's words with month and place, and that the Marshal acted on each on his own order.

**Flag 4 (minor). The played scene is misstated: who set the green pieces on the potters' beam.**
- Rule: build 7 point 1 and `year-turn.md` section 1 (the played scene holds, whole); failures checklist 2.
- Where: `P/releases/005/civ-unnamed-people-pass1.md`, the first bullet of "What was played" ("The Assay-master set the sevens and the twelves pair against pair on the potters' beam and said the beam agrees"); `P/civs/unnamed-people/years/005.md`, "The played days, in short" (the same words).
- What the record says instead: `P/player/transcript-year-005.md` line 143: "The Assay-master asks to see a pair of pairs again on her beam ... She sets them in the brass pans herself." Her term on the board and in the scene was that no hand but hers and her firemen's carries a green piece. `decisions-005.md` item 3 has "saw". The kiln day's lines are right.
- Fix (Keeper, correct the record, both files): the Assay-master asked, and the master set them on her own beam. Not yet told to the player; no corrections entry is owed if fixed before the morning.

**Flag 5 (minor). The board is short of stance, opening words and reasons for two figures.**
- Rule: `year-turn.md` section 2 (parameters are what each figure wants, will and will not do or accept, its stance and its opening words; the reasons, one for each parameter); build 7 point 3.
- Where: `S/releases/005/dm-sealed.md`, held moment "the coaster's master at the head of the line". The Tally-keeper has a will and a will not, and no stance, opening words or reason. The ship owner of the open water has his conduct if sent for, and no stance, opening words or reason. The mate has no reason for his silence. The Reasons list covers the coaster's master, the Stallreeve and the eleven only.
- What the record says instead: the Year 4 boards gave each figure on them a stance, opening words and a reason, the Tally-keeper included.
- Fix (Keeper, before the play day): add the missing stance, opening words and one reason for each of those parameters, from the earlier sheets and the record. No range or outcome changes.

**Flag 6 (minor). The board misdates what the coaster's master knows.**
- Rule: failures checklist 2 (contradiction); checker item 4.
- Where: `S/releases/005/dm-sealed.md`, the cast line for her: "She knows: what her own quay has had since the winter of Year 3 by way of Corrith (the six old weights and their figures, the fired pieces, the ring's day)".
- What the record says instead: the town's word with the figures and the ring's day was first said at Corrith in month 10 of Year 3 (r-0432; `S/years/005/year.md`), and the sealed side release has the Corrith quays telling the carrier that what was new to them was "the figures and the ring's day". So none of that can have reached her quay by way of Corrith before month 10 of Year 3. What her quay had since the winter of Year 3 is her own news of Year 2, sold by her (`S/years/003/held-coaster-played.md`; `S/years/003/world-events.md`): a reader of scales seated as keeper who says it is a god, the hall's pieces a twentieth heavy, the old weights six of seven. The board's own fact line ("It reached her as quay talk from another port, months late") agrees with the record, not with the cast line.
- Fix (Keeper, correct the record): split the cast line: her own news on her quay since the winter of Year 3; the word's figures and the ring's day by way of Corrith, after month 10 of Year 3.

**Flag 7 (minor). The player's people are told a fixed fact is not settled.**
- Rule: failures checklist 2 (contradiction); checker item 4 (a release says what its reader may know and use).
- Where: `P/releases/005/civ-unnamed-people.md`: "Orrin's stick of tile weights is not settled in this stretch. Write nothing of what it tells him until you are told." The keeper log, pass two: "Fixed fact; it is in a stretch not yet told (Year 4, the winter on), and it is told only as his tiles telling him nothing."
- What the record says instead: `S/years/005/year.md`: "Orrin's stick of tile weights, kept from month 3: it tells him nothing, and will not ... Not rolled; fixed". The stretch from month 3 of Year 4 to month 10 is told tonight; the people's public file already has him keeping the stick and saying nothing of it. The fact is settled, and the agent is told it is not.
- Fix (Keeper, correct the record): tell the agent what is fixed, in plain words that state no cause (his stick shows him nothing that tells one load from another), and correct the log line on which stretch it is in.

**Flag 8 (minor). Two public day records name the sealed act and say its result was told privately.**
- Rule: `year-turn.md` section 5 (what a sealed act shows goes to the DM in the sealed part only, never in a public file); checker item 6b; the Year 4 check's flag 7 and its accepted form.
- Where: `P/player/decisions-005.md` line 53 ("The sealed act (the Year 4 flags' duty): its result was told to the player privately with the first post and recorded, dated, in the sealed record under Act."); `P/player/rolling-save.md` line 364 ("the sealed act's result was told privately with the first post"). The people's agent reads `decisions-005.md`.
- What the record says instead: the act, its result and the private telling are in `S/player/unsaid.md` under `## Act`, which is complete and dated (21:34 Pacific). The Year 4 fix reworded the same kind of line to say only that a part of the sealed record was given and nothing of it was stated in the open.
- Fix (DM, at step 6, correct the record): reword both lines to the accepted form, naming no act and no private telling.

**Flag 9 (minor). god-rivers's release drops the god's second pasture night and the ask that waited for it.**
- Rule: failures checklist 3 (what the god has done); checker item 4.
- Where: `S/releases/005/god-rivers.md`, "What you did": one walk of the pasture at the dark of the moon.
- What the record says instead: `S/civs/unnamed-people-rivers/years/005-report.md`: the pasture at the dark of the moon in month 3, and again in month 7 at the herd keepers' asking; and the head herd keeper's question left with the Seat Warden in month 5 while she was on the road, met with silence, and answered yes when she came home. The Keeper said it read only part of this report; the rest of the release agrees with it (the carrier family's no, the ford, the run of fish and the child's ask, the measures).
- Fix (Keeper, correct the record): add the second night and the waited question with its answer.

### The two reports the Keeper read in part

- The Sarrow. The year file and the report agree with `civ-sarrow.md` and `god-thresholds.md` on the riders (seven, four laden beasts, the twelfth day of month 1, the clerk, the written answer, salt bought, home on the twentieth of month 2), Branch B of the stores (about four hundred over the ordinary, the seed seal broken in the last week, a short sowing), Branch D2 large at the farthest door, the god's view given last as its decisions set it, the hand that moved, the step back (L-0053), the cairns, the river's trains at half with coughing beasts and none of the Sarrow's own herds sick by month 11, and the sky. The two disagreements are flags 2 and 3.
- The spring town. The year file and report agree with `civ-unnamed-people-rivers.md` and `god-rivers.md` on the council's answers, the measures, the carrier family's no and the five days at the ford, no pull in the larger river, the run of fish in month 11 and the child's ask, and the people better fed at the year's turn (the largest fish store any weir hand remembers). The one gap is flag 9.

### The judgment checks

- **Cause and fixity.** Every event of the stretch and of the world's Year 5 traces to a decision, a schedule row, a roll or a logged fixed fact. New fixed facts are logged with causes: the halves by table rolls; the clay figure from the Year 2 reading at the pits; the tide-reckoner's cost as common talk (her own card entry and people file carry it, and the netmaker's public line agrees); her opening words, the wind, her sailing day, the bend town's guest as common talk at her port (supported by the bend town's record of a guest with a lamp and its parties at Port Sennet since Year 2). The woman of the back houses was answered in the player's own words of Year 4 (`decisions-004.md` item 6).
- **Rules.** Every contested outcome has a logged roll, none rolled twice. r-0412 is a void draw the tool replaced itself (r-0413), logged as such. Odds stay within 5 to 95. L-0052 reads L-0037 and narrows nothing; L-0053 to L-0055 read the cards' own words. Flag 1 is the one result reshaped.
- **Knowledge and secrecy.** No sealed name in any public file (Wynne Daub, Osric Marl, Annis Furrow, Tam Wherry, Davin Sculler, Maud Sennet, Port Sennet, House Corran searched). Corrith, the Aldermark, Ruddfold and the Alder were in `player/map-knowledge.json` before tonight. The shut sittings are told in public only by what came out at the post. No release names another god or a count of gods; the bend town's guest stands on the sealed sheet only, to a plain asking (ruled below).
- **The player.** The decisions file is present; the year turned. No sealed want was applied; the Want and Other parts of the day were not acted on, and the not-clay figure was set by a rule the same for all eleven pieces, so the belief in the Other part is neither met nor corrected by anything chosen. The asks met with silence are pending, the boy's question now asked five times.
- **Growth.** Eight growth lines: no attempt, no trigger, knack use only. The player's hidden power's condition was not met: no food was set in its own pans.
- **The sealed act's private answer** (Year 4 ruling 5): given on the play day and recorded under `## Act` in `S/player/unsaid.md` with the date and time and the line as given. Held. Flag 8 is the public mention.

### Build 7 points

1. Both prepared scenes accepted whole, and the DM's run-on ruled: held. The weighing green (days 14 and 25) and the kiln-opening (month 8, day 1) are taken whole; nothing reworked, rerolled or taken back. The run-on to day 4 is inside the second board's "if play runs on" paragraph, and the answer given at the gate on day 2 is ruled and accepted in the keeper log with its reason. The three departures from parameters are logged as findings, not corrected. One misstatement in the telling (flag 4).
2. The two unrolled facts settled as the files give: held. Each half alone by eleven table rolls written before the dice; clay against not clay set from the record with no roll, under L-0037 read by L-0052, entered in the ledger and on the card line in `dm.md`; told as part of the kiln yard's day, completing an act the player committed in the scene and changing nothing played. Every figure checks.
3. The player's thread run as one untold stretch to the first held moment, with nothing public past it: held. From the evening of day 4 of month 8 of Year 3, through the end of Year 3, into Year 4, to the gatepost on day 14 of month 10 (L-0056). Her coming is a major encounter by `engine/rules/encounters.md` section 6. The public year file, report, lore, state, chronicle addition, pass-two release and `dm.md` stop at it; the people's sealed file keeps the past-the-moment matter under its marker line; the dim night of that evening and the river boats are sealed only. Nothing of the god's Year 5 is told.
4. The board in `dm-sealed.md` complete with no open roll, and `dm.md` limited to what the god knows: the board has its facts, parameters, outcomes and "To roll: nothing", and every range was rolled by the Keeper first; not complete in two figures' stance, words and reasons (flag 5), one cast line misdated (flag 6), one result reshaped (flag 1). `dm.md` carries only what the god saw, heard or was told; no flag on it.
5. No DM result changed: held. No DM roll was made on the Year 5 day; `P/state/rolls.jsonl` is unchanged since Year 3's played day.
6. Phenomena months and counts: held. The seven NPC peoples and gods have months 2, 2 and 7 and three in all, the cranes in month 3 for the three peoples that see them, twenty-four since the arrival; the player's people and the DM have Year 3's six with months now that the year is told whole, and Year 4's months to the stop with no count. The board gives the night of day 14 for play only, with no count.
7. No hint of growth before year 70: held. No release, decide release, sheet, board or card line carries one; the decide releases prompt nothing. The seven gods again wrote, unprompted, that they try to grow nothing.
8. The lag entry and L-0056: held. The figures check: fourteen and a half months behind the opening of Year 6 (two and a half of Year 4 and all of Year 5), seventeen and a half this morning, fifteen months covered tonight. L-0056 fills a gap step 0 leaves (a whole unresolved year between the tail and the open year) and changes no engine text. It and the three questions under it are for Michael.

### Waiting on step 6 (not failures now)

- The Year 6 morning story, the Year 5 closing, the chronicle's god side and the painting request, which belongs in `images/held/` (`P/state/images.md` approves no Year 6 morning; the known tool fault in `paint.py` and `check.py` will read an approved play-year morning as approval for any year, and that fault is reported to Michael, not a campaign flag).
- Flag 8 is the DM's at step 6.
- `P/player/pending.md`: the next morning's list should carry the one question asked five times, and drop the Stallreeve's and the netmaker's, both now answered.

### Rulings for review

- **The kind of the one random event.** The table gives four things of the kind beasts and no die among them; the Keeper chose by fit with the country's record and "by what makes the more interesting game". DESIGN uses that test for a tie on a variety table and in the blend, not for a random event's item. Accepted as a reasoned judgment for this run, since the event is the world's and touches no god's act. For Michael: should a random event's item be rolled among the four?
- **The bend town's guest on the board.** The sealed sheet lets the coaster's master say, to a plain asking only, what is common talk at her port of a guest with a lamp at the bend town. `year-turn.md` section 2 keeps another god off the sheet beyond what the scene puts before the god's own senses. Read and accepted: a figure carries what she knows, the talk is supported by the record, she does not offer it, and it calls nobody a god. For Michael: whether common talk of another god may stand on a board at all.
- **The pass-one releases' "of their coming fewer this year than last"** (dim nights, the seven NPC peoples). Not flagged: each people keeps its own count. Noted as close to pointing.
- **The `dim-nights` label allow.** Standing from Year 1, as before.
- **The place scan reading an earlier year's flags file.** A tool fault, for the coordinator.
- The Keeper's other rulings for review in the Year 5 log are read and accepted for this run: the tide-reckoner's cost as known; the asking in session held as pending; a conditional roll not made; the player's standing not entered for a year told in part; the people's report reworded for the scan; the bell and the lamp; salt in water; a watcher at a god's door; the kiln-master's tiles (apart from flag 7).

## Round 2

Recheck by the continuity checker, 2026-11-26, written at 22:51 Pacific, against commit 50a317f ("sim-06 Year 5 night: the checker's round 1, flags 1 to 7 and 9 fixed"). Pulled first; already up to date. Read: the diff b2d2d36 to 50a317f in full, the keeper log section "7. The check, round 1: nine flags" and its rulings for review, the new cast line, parameters and reasons on the sealed sheet, the appended correction in `S/years/004/year.md` and its Year 4 god-thresholds paragraph, the new m-0014 line in the message log. No roll was added or changed (r-0464 is the last id).

### Scripts

- `tools/check.py sim-06 5 --step 7`: the same 2 findings (the morning story and the painting request, both step 6) and the same note. Not flags now.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning (the standing label allow); dashes 0.
- `tools/map.py travel sim-06 f60 f65:start --by foot --via f65`: 148.1 miles, 8 full days, as the correction gives. `f65:start` to Aldermoot by horse: 117.6 miles, 6 full days, as the releases now give.

### Round 1 flags, rechecked

- **Flag 1: resolved.** The eleven's parameter, outcome 4, the reason line and `year.md` now give the success as written before the die: the first carrying each summer is hers. The keeper log withdraws the condition and marks its earlier lines superseded. No roll redone.
- **Flag 2: resolved.** All five places now give 117.6 miles and 6 days by horse from the road's first point, with Aldermoot south-west and "north-east" kept only as the people's own phrase; the old message log line stands and a new one corrects it, as the log is never rewritten. The timeline holds: out from the farthest house on day 12 of month 1, there about day 19, some three weeks waiting, home on day 20 of month 2, which the road back (6 days to the road's end and some 5 by horse on the road to the city) allows. Year 4's 68.2 miles is corrected to 148.1 and 8 days on foot by a dated entry appended to `S/years/004/year.md`; no Year 4 outcome turns on it, since her blessing was laid in month 7 and her next act falls in month 8. Ruled on the Keeper's question: the Sarrow pass-one release, already read by its agent, may stand unedited. Its pass-two release corrects it and says that where it differs this is what happened, and the agent reads it at the next turn; editing a read release would change what the agent was given. Accepted.
- **Flag 3: resolved.** Both asks are listed in god-thresholds's release, with month, place and the Marshal's own orders, and the second "still waits for your word".
- **Flag 4: resolved.** Both public files now have the Assay-master asking and the master setting the pairs in her own beam's pans, as transcript line 143.
- **Flag 5: resolved.** The Tally-keeper, the ship owner of the open water and the mate each have wants, stance, opening words and a reason, each in keeping with the earlier sheets and the record. No range or outcome moved.
- **Flag 6: resolved.** The cast line now holds her own Year 2 news on her quay since the winter of Year 3, and the word's figures and the ring's day by way of Corrith after month 10 of Year 3.
- **Flag 7: resolved** as a contradiction; see flag 10 for where the fixed fact now stands.
- **Flag 8: open,** the DM's at step 6.
- **Flag 9: resolved.** god-rivers's release has both pasture nights (months 3 and 7) and the question left with the Seat Warden in month 5, met with silence and answered yes on its return.

### Raised in round 2

**Flag 10 (minor). A public release now states what a mortal's private record shows him.**
- Rule: DESIGN 12.2 and `year-turn.md` section 3.1 (the player's people's public files hold only what the god could witness or be told); checker item 6b; mystery standard rule 15 (nothing given before it is earned).
- Where: `P/releases/005/civ-unnamed-people.md`, the Orrin line: "it shows him nothing that tells one load from another. His tiles lose in the fire alike, whichever loads go on to crack."
- What the record says instead: the people's public year file has Orrin keeping his stick from month 3 of Year 4, and "What it showed him he did not say." Nobody has told the god what the stick shows, and `S/years/005/year.md` gives it as "not told". The player may read `releases/`. The fault is in part the checker's: the round 1 fix asked for the fact to be told to the agent and did not say where.
- Fix (Keeper, correct the record): move the sentence to the sealed side release, `S/releases/005/civ-unnamed-people-sealed.md`, as what Orrin knows; in the public release keep only that the stick is settled and that nothing of it has been said where the Weightward hears, without saying where the rest is written.

### Build 7 points, round 2

1. Both prepared scenes accepted whole, and the run-on ruled: held. The misstatement (flag 4) is corrected.
2. The two unrolled facts settled as the files give: held.
3. The player's thread as one untold stretch to the first held moment, nothing public past it: held. Flag 10 is a fact inside the told stretch that the god does not know, not a fact past the moment.
4. The board complete with no open roll, and `dm.md` limited to what the god knows: held.
5. No DM result changed: held.
6. Phenomena months and counts: held.
7. No hint of growth before year 70: held. Nothing in the fixes touches powers.
8. The lag entry and L-0056: held.

### Rulings for review, round 2

- The Keeper's three rulings of the check are read and accepted: the condition withdrawn with the success as written; the wrong end corrected by dated entries in both years with the old message line kept; a pass-one release already read left unedited and corrected in pass two.
- The tool-clarity point (which end of a line `:start` and `:end` name on the ground) is for Michael, with the place scan reading an earlier year's flags file. Both are tool matters, not campaign flags.
- The open questions of round 1 stand for Michael.

## Round 3

Recheck by the continuity checker after step 6, 2026-11-26, written at 23:01 Pacific, against commit fa94ac6 (the Keeper's flag 10 fix d2ccaa7; the DM's step 6, fa94ac6). Pulled first; already up to date. Read in full: `P/years/006/morning-story.md`, `P/years/005/closing.md`, `images/held/sim-06-006-morning.json`, the dated entries in `P/player/power-card.md`, the diffs of `P/player/pending.md` and of every file in `P/player/chronicle/` (canon, chronicle-god, messages, people, threads, years), the reworded lines of `decisions-005.md` and `rolling-save.md`, and the d2ccaa7 diff. Each was read against `P/releases/005/dm.md`, `S/releases/005/dm-sealed.md`, `S/years/005/year.md`, the people files, the transcript and the failures checklist.

### Scripts

- `tools/check.py sim-06 5 --step 7`: 1 finding, 1 note. The finding says the held request is approved and belongs in `images/requests/`. That is the known tool fault (an approved play-year morning read as approval for any year), reported to Michael; `P/state/images.md` approves no Year 6 morning and run 07 approves no paintings, so the request is rightly held. Not a campaign flag. The note is the old public roll ids, standing.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning (the standing label allow); dashes 0.

### Flags rechecked

- **Flag 10: resolved.** The public pass-two release now says only that Orrin's stick is settled and that the people's public files say of it only that he keeps it. What it shows him is in the sealed side release as his own knowledge, told to nobody. No public file holds it.
- **Flag 8: resolved.** `decisions-005.md` line 53 and the closing clause of `rolling-save.md` line 364 now say only that a part of the sealed record was given and nothing of it was stated in the open, the accepted form. Searched again: no public file outside the verbatim transcripts names the act, the pocket as checked, or a private telling.

### The DM's step 6 work

- **The morning story.** The first paragraph is the return sequence: the year, the month and the country's season, the town after its winter and its new weight, the god at the post, its body, its senses (no weight in the air), and where the telling runs. Then the played days as standing, the kiln yard's figures (every one matches `dm.md`), Year 3 to its end, Year 4 to the gate, and the board in the release's words; nothing resolved, and the coaster's master says nothing. Every fact was checked against `dm.md` and the people's public file. Nothing from `dm-sealed.md` appears: no name, house or port, nothing of her balance or her wants, no dim night of the fourteenth, no river boats. Bren is given no pronoun in the story. The sky: Year 3's six by month, from the release, which matches `tools/phenomena.py` (months 1, 5, 5, 7, 7, 8); Year 4's four nights to the stop with no count. One (oog) on where the story stands against the clock, with its reason. The one pending question named, with all five askings, and nothing read into the silence; the refusal named as not waiting. Checklist: no invention, contradiction or forgetting in the story; no flattery; no pointing at signs (the dim nights are told at the weight of the lines around them); no corrected belief; the lists given are the pending and answered asks the rules require; no hint of growth. The last line, that the clock is closed after this night, is true by the run 07 plan and the ruling of 2026-11-25.
- **The closing.** Written from what happened in the stretch, in the DM's voice, and it tells nothing past the gate. It runs to five sentences where step 6 asks three or four; as in Year 4, not flagged.
- **The held request.** `images/held/sim-06-006-morning.json`, wide, the house style block first, the figure from the appearance card seen from behind with no face. The scene is the ring's day, the second day of the first month of Year 4: the eleven on the hall's bench, the god's scales with the smallest piece in a pan, the Assay-master watching and the Tally-keeper cutting, the ring along the wall, the yard through the open door. A thing the god saw, inside the told stretch. The grey-haired Assay-master matches the approved Year 3 painting the player has already seen. Nothing from the sealed part and nothing past the gate. Held, not sent.
- **The card.** L-0052 is entered twice: once under The True Measure, Rulings, and once as a dated entry quoting the release, the same practice as L-0037. Both carry the release's words exactly and change no term of the card. Accepted.
- **`pending.md`.** The Year 6 list holds the one question asked five times and the refusal, and marks the Stallreeve's and the netmaker's as answered. It matches `dm.md`.
- **The chronicle.** `canon.md`, `chronicle-god.md`, `messages.md`, `people.md`, `threads.md` and `years.md` hold the Year 5 played day, from the save, the decisions and the transcript, and the stretch as told, and stop at the gate. No sealed name, no figure of the master of the potters' working-out, nothing of the carrier's quay account beyond what he said at the post. `people.md` has Bren as a woman, as her people file has her (see flag 11).

### Raised in round 3

**Flag 11 (minor). The public DM release gets Bren's sex wrong.**
- Rule: failures checklist 3 (forgetting: sex); checker item 4; `year-turn.md` section 2 (the cast with a name and sex).
- Where: `P/releases/005/dm.md`, Day sheet, "The cast the god knows": "Bren (man): at the fish landing most dawns."
- What the record says instead: `P/civs/unnamed-people/people/bren.md`: "A channel woman of about 40"; `P/releases/003/dm.md`: "Bren (woman)"; `P/player/chronicle/people.md`: "A woman of the channel folk". The morning story gives Bren no pronoun, so nothing told to the player is wrong.
- Fix (Keeper, correct the record, before the next played day): "Bren (woman)". No corrections entry is owed, since the player has not been told otherwise.

### Build 7 points, round 3

1. Both prepared scenes accepted whole, and the run-on ruled: held, in the morning and the chronicle as in the record.
2. The two unrolled facts settled as the files give: held; the morning tells them as what the pans gave that day, every figure matching.
3. The player's thread as one untold stretch to the first held moment, nothing public past it: held, in the morning, the closing, the chronicle, pending and the held request.
4. The board complete with no open roll, and `dm.md` limited to what the god knows: held, apart from flag 11, which is a slip of the record and not past the god's knowledge.
5. No DM result changed: held. No roll was made.
6. Phenomena months and counts: held. Year 3's six counted, Year 4 uncounted, in the morning, `dm.md` and the chronicle.
7. No hint of growth before year 70: held, in the morning, the closing, the chronicle and the card.
8. The lag entry and L-0056: held; the morning's (oog) states the same place against the clock.

### Status

Raised 11, resolved 10, open 1. The check fails until flag 11 is fixed. When it is, the check passes for Year 5 and the clock may close (step 8).
