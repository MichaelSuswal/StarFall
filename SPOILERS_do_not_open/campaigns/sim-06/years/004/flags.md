> SPOILER WARNING. Sealed. Year 4 continuity flags for campaign sim-06. Players must never read this file.

# Continuity flags: sim-06, Year 4

Rounds 1 to 4. Status now: raised 9, resolved 9, open 0. By severity, as raised: major 0, moderate 3, minor 6. The check passes for Year 4.

## Round 1

Run by the continuity checker at the check step of the Year 4 night turn (run 07 Part B, build 7), 2026-11-26, written at 21:11 Pacific, against commit 7ddccae ("sim-06 Year 4 night: pass two, the year record, releases, and both boards in the sealed day sheet"). Pulled first; already up to date. Every check below was made against the files, not against the keeper log's word. Steps 6 and 8 are not written yet (the morning story, the closing, the chronicle update, the held painting request, the clock); findings that wait on them are not failures now.

Read in full: `CLAUDE.md`, `engine/roles/checker.md`, `engine/night/night-turn.md`, `engine/rules/failures-checklist.md`, `S/keeper/year-turn.md`, `S/keeper/sealed-factors.md`, `engine/rules/encounters.md`, `S/rulings.md`, `tests/creation-sim/run-07/plan.md`, the Year 3 flags (standing rulings), `S/years/004/year.md`, the keeper log from "Year 4 night turn", `P/releases/004/dm.md`, `S/releases/004/dm-sealed.md`, `P/releases/004/civ-unnamed-people-pass1.md` and `civ-unnamed-people.md`, `P/civs/unnamed-people/years/004.md`, `004-report.md`, the lore, state and people diffs, the sealed folder `S/civs/unnamed-people/`, `P/player/decisions-004.md`, `pending.md`, the conduct profile (Now and the Year 4 entry), `S/player/unsaid.md`, the growth diffs (eight files), `S/state/luck.md`, the sealed roll log r-0350 to r-0406, `S/state/phenomena.json`, the message log m-0005 to m-0009, the ledger L-0047 to L-0051, god-sea's and god-beasts's releases, the seven NPC pass-one releases (sky sections). Read by search and in part: the Year 4 transcript (posts 1 to 4), `S/years/004/world-events.md`, the other god and civ pass-two releases, the seven `decisions-004.md`, the seven decide releases, the Longwalk's Year 4 files, the dreams people's Year 4 file, `P/player/chronicle/`, the set-aside Year 3 files, `S/sealed-terms.txt`, `S/leak-allow.txt`, the map for the journeys named.

### Scripts

- `tools/check.py sim-06 4 --step 7`: 2 findings, 1 note. The findings are the missing morning story (`P/years/005/morning-story.md`) and the missing painting request in `images/held/`. Both are step 6. Not flags now. The note is the public roll log's old ids (DM r-0001 to DM r-0015), standing since Year 1.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning; dashes 0. The warning is the `dim-nights` label allow in `S/leak-allow.txt`, standing from the Year 1 check. Every public dim-night line was read for meaning: the stretch gives months, and no count for an untold year. Not a flag.
- `tools/lockcheck.py sim-06 --all`: 0 failures; 58 place warnings (map names without ids in the NPC civ agents' own sealed files, the sealed message files, `S/releases/003/dm-sealed.md`, `S/releases/004/dm-sealed.md` and `S/years/*`), 1 release warning (`S/releases/004/god-thresholds.md` line 20, salt beside a word of scarcity: the Sarrow's own salt store, a fact of its reader's own people; judged not a world fact its reader lacks), 1 roll note as above. Noted, not flagged.
- `tools/phenomena.py` for Years 3 and 4: dim nights 6 (months 1, 5, 5, 7, 7, 8) and 7 (months 2, 3, 4, 8, 10, 11, 12); tide gathering months 2, 8 and 1, 8; cranes month 3 both years. Twenty-one dim nights since the arrival (3, 5, 6, 7), as the releases say.
- `tools/map.py travel` run for: the town to the Maun Flats [f22] (the knowledge file's 1.6 miles to the near edge stands; the tool's 21.8 is to the middle); Marle Ford [f61] to Aldermoot [f70], 246.8 miles, 22 days (m-0009); the winter city [f60] to the end of the Pass Road [f65], 68.2 miles, 5 days; Wellen Ford [f47] down the River Wellen [f08] by boat, 133.6 miles, 4.5 days; the bend town [f50] down the River Ellow [f07], 112.4 miles, 4 days; the Ellow's mouth to Port Sennet [f75], 97.9 miles, 7 days. All agree with the record.

### Flags

**Flag 1 (moderate). Public files still tell the player's thread past the held moment, the held scene's outcome among them.**
- Rule: build 7 point 2 and `year-turn.md` section 1 ("Nothing of them past it is written as what happened, released, or told ... not in any public file"); checker item 6.
- Where: `P/civs/unnamed-people/state.md` line 49, in the Keeper's Year 3 pass-two section: "The potters' third nest, fired to the old six, agrees with itself and with them to a hair. The date the ring set for the town's weight holds." Line 50 tells the netmaker's question as already met with no answer. `P/releases/003/dm.md` lines 118 to 120: the seventh-month firing, the eleven chosen at the gate, "They agree with one another to a hair", and the ring's sitting on the third nest in the ninth month. The set-aside drafts `P/civs/unnamed-people/years/003.md` and `003-report.md` (item B, the third nest) tell the same.
- What the record says instead: the firing and the kiln-opening are held behind the potters' door (`S/years/004/year.md`, "Held past the first moment"; `S/releases/004/dm-sealed.md`, both boards). The two drafts carry the Keeper's set-aside line at their head (ruling for review, keeper log step 2). `state.md` has only a section below saying "the numbers above" were written for a set-aside year, and line 49 is not a number. `releases/003/dm.md` is set aside only by a line in another file (`releases/004/dm.md`). The player may read `releases/` and the people's public folder, so the result of the scene it is about to play stands in two public files with no mark on them.
- Fix (Keeper, correct the record): mark `state.md` lines 49 and 50 and the head of `releases/003/dm.md` as set aside from the fifth day of the first month of Year 3, in the form used on the two drafts; or move the past-the-moment matter to the sealed folder without deleting it. Whether set-aside drafts may stay public at all under build 7 is put to Michael under "Rulings for review".

**Flag 2 (moderate). A chance range for the player's people left to an open DM roll, so the sealed factor cannot enter it.**
- Rule: `sealed-factors.md`, "DM rolls in play", third bullet: luck works only through the odds the Keeper sets, including "the chance ranges on a board it writes for a held moment or prepared scene ... where a range turns on chance for the god or its people ..., the Keeper sets it as it would set a roll's odds, shifted by the god's steps, before the board is written". Checker item 5; the factor's check 1.
- Where: `S/releases/004/dm-sealed.md`, held moment "the kiln-opening", "To roll, only if spares were fired": whether every spare comes out whole, "the master of the potters' attempt", stated odds 45, left to the DM. Keeper log pass two: "The spares' fate in the kiln is left to the DM's open roll at stated odds 45, with no shift: a DM roll takes none."
- What the record says instead: the potters' firing is an act of the player's people, and the player's step is 1 (`S/state/luck.md`). The Keeper set the other range on the same board (the master's leave, r-0378) with the step, as the rule says; this one it handed to the DM, where the factor cannot reach it. Its own ruling for review ("whether the sealed factor can enter a roll the sheet leaves to the DM") answers a question the rule does not put: the rule has the Keeper set the range itself.
- Fix (Keeper, before the play day): set the spares' fate as a board range, rolled by the Keeper with the player's step, on the branch "spares fired" (the count cracked and their sizes by the dice already written), logged in the keeper log only; give the DM the outcome by branch in the sealed sheet and remove the open roll from it. If the Keeper holds the open roll is right, it stands as a ruling for review and this flag goes to Michael.

**Flag 3 (minor). The played held moment is misstated in three files: an answer told to the Stallreeve that was not played.**
- Rule: build 7 point 1 and `year-turn.md` section 1 (the played scene holds, whole); failures checklist 2 (contradiction) and 6 (acting for the player).
- Where: `P/releases/004/civ-unnamed-people-pass1.md` line 24 ("It told the Stallreeve that it answers the master of the smiths, and the woman of the back houses, only when either next asks ..."); `P/civs/unnamed-people/years/004.md` line 23; `P/civs/unnamed-people/years/004-report.md` line 10 ("its standing on the master of the smiths' ask and the woman of the back houses' ask told to the Stallreeve").
- What the record says instead: `P/player/transcript-year-004.md` lines 245 to 247 and `decisions-004.md` item 6: the Weigher told the Stallreeve where it stands on the master of the smiths' ask only, and he said "I'll not carry that one for you either." The woman's answer was "Not carried to her" and was not spoken at the post. Nothing in the year turns on the extra words, so this is the telling, not the world.
- Fix (Keeper, correct the record): reword the pass-one line and have the people's two lines match the transcript. Not yet told to the player; no corrections entry is owed if fixed before the morning.

**Flag 4 (minor). The public DM release tells the god of a name it has not heard.**
- Rule: build 7 point 3 (the public `dm.md` carries only what the god can see, hear and know); checker item 4.
- Where: `P/releases/004/dm.md`, Year 3 again, autumn, second line: "The boatmen saw. They have a name for it, which nobody has said to the Weigher."
- What the record says instead: the people's report (Names said aloud) has "running the cups" not said in its hearing. That the boatmen have a name is not something the Weigher saw or heard. The town's talk of it stands in the people's lore by the long-standing practice for unspoken bynames, and that is not flagged.
- Fix (Keeper, correct the record): end the line at "The boatmen saw." If the name matters to the DM, it goes in the sealed part.

**Flag 5 (minor). god-beasts's release lists as unanswered a question it answered.**
- Rule: checker item 4 (no release contains more or other than its agent could know); failures checklist 3 (forgetting what the god has done).
- Where: `S/releases/004/god-beasts.md`, "Asked of you and not answered": the young herder of the apart clans, "He went home on the third morning with no answer."
- What the record says instead: `S/civs/longwalk/years/004.md` line 60 and the report lines 69 and 87: he asked again in month 10 with the god at the margin, and it answered in its decided words (`gods/god-beasts/decisions-004.md` item 6), and his clan took the answer for a yes. `S/years/004/year.md` agrees: "asked twice about the star and was answered in its decided words." The release drops the second asking and the answer.
- Fix (Keeper, correct the record): move the ask out of the unanswered list and tell both askings, the answer as given and what his clan made of it.

**Flag 6 (minor). A roll factor not in the record, which the board then contradicts.**
- Rule: `encounters.md` section 2 ("an agent may not invent a factor"); failures checklist 2.
- Where: keeper log pass one and the roll log, r-0378, factor -5: "she fires in one kiln so the pieces shrink alike; a larger load does not fit one kiln (her people file)". `S/releases/004/dm-sealed.md`, the first board's parameters and outcome 1: with the spares, all fifty-five pieces go "in the one kiln, in one firing". The kiln board's factor "a kiln half as full again as she is used to -10" sets fifty-five against her usual twenty-two, which is two and a half times as full.
- What the record says instead: `P/civs/unnamed-people/people/master-of-the-potters.md` says she fired her first nest in one kiln so the pieces would shrink alike, and nothing about what a kiln holds. The roll was a success either way (26 against 50 and 55), so the outcome does not change and the roll is not redone.
- Fix (Keeper, correct the record): log the factor as unsupported beside r-0378, and set the kiln's capacity on the sheet as a new fixed fact, conservatively, so the board's single firing and the kiln board's factor agree with it. If that changes the kiln board's stated odds, correct them before the play day.

**Flag 7 (minor). A public day record names the god's sealed act.**
- Rule: `year-turn.md` section 5 and build 7 decision 8 (what a sealed act shows goes to the DM in the sealed part only, never in a public file); checker item 6b in spirit.
- Where: `P/player/decisions-004.md` line 49 ("The Year 3 sealed act (the pocket) was not stated in the open today and was not played") and line 48 ("given in a sealed part"). The people's agent reads this file. Line 49 also now disagrees with the night, which carried the act out (`S/years/004/year.md`).
- What the record says instead: the act and its result are in `S/player/unsaid.md`, `S/years/004/year.md` and `S/releases/004/dm-sealed.md`. The habit is rightly in the open conduct profile as conduct. Year 3's `decisions-003.md` line 55 said the same thing in public and was not flagged; under build 7 it is done, which makes the public line misleading as well.
- Fix (DM, at step 6, correct the record): reword the two "For the Keeper" lines so that no public file names the sealed act or says it was not played. The Year 3 line goes to Michael under "Rulings for review" (whether to reword it too).

### What held, by check

- **Cause and fixity.** Every event in the stretch and in the world's Year 4 traces to a decision, a schedule row, a roll or a logged fixed fact. New fixed facts are logged with causes: the working stones' range before r-0392; the market's unit, the nest's sizes, the clay's loss, the firing's days and the piece table for the boards; the master of the potters' name (on the sealed terms). The old women's bread at the low tide is standing lore (`lore.md` line 143). The door-stone is a table roll, written before the dice.
- **Rules.** Every contested outcome has a logged roll; none is rolled twice; r-0350 is a named tool check that decides nothing; odds stay within 5 to 95. L-0047 to L-0050 read from the cards' own words and narrow nothing beyond them. The second stick's eight rolls name the factor at step 1; none turned on it. Growth: eight files, each "no attempt", knack use only; nothing earned.
- **Knowledge and secrecy.** No sealed name in any public file (Wynne Daub, Osric Marl, Annis Furrow, Tam Wherry, Davin Sculler, Maud Sennet, House Corran searched). The shut sitting is told in public only by what came out at the post. The people's sealed folder holds the hall's matter and the "Past the first held moment" line, empty. No release names another god or a count of gods.
- **The player.** The decisions file is present; the year turned. Questions put to the god while away met silence and are pending; a refusal by the player's own word is treated as refused, not pending. No sealed want was applied.

### Build 7 points

1. The played held moment is accepted whole: held. The keeper log, `year.md` and the people's file keep every played line and the DM's added lines; nothing was reworked, rerolled or taken back. One misstatement in the telling (flag 3), not in the world.
2. The thread stops at the next held moment, and no public file tells past it: held for everything written tonight (`dm.md`, the people's Year 4 files, the chronicle addition, the pass-two release stop at the potters' door; the coasters, the firing and the town's Year 4 are held). Not held for the build 6 matter left standing in public (flag 1).
3. Both boards in `dm-sealed.md` with facts, parameters, outcome ranges and reasons, and `dm.md` carrying only what the god knows: held, both boards complete; one line in `dm.md` past the god's knowledge (flag 4); one board range wrongly left to the DM (flag 2); one unsupported factor (flag 6).
4. The Keeper changed no result the DM rolled: held. The DM rolled nothing on the Year 4 day; `P/state/rolls.jsonl` is unchanged since Year 3. The question the DM left unrolled (the carrier and the house's name) was rolled by the Keeper as the world's question (r-0391) and is in the sealed part only.
5. The search, the day away, the pending asks, the habit and the sealed act, per decisions 3, 4, 5 and 8: held. The search was classed before it was resolved (placed thing, not reached, not rolled; the stones came about in play, rolled by the evidence). The day away: the Stallreeve's leave was his; the empty post met a question with silence, pending. The pending asks are put back, and "what would break it" is refused and not pending. The habit is carried out as conduct, not priced. The sealed act is done and shown in the sealed part only. One public line about the sealed act (flag 7).
6. Months and counts of seen phenomena given by month: held. The seven NPC peoples and the seven gods have months and the true count; the player's people and the DM have months and no count for an untold year; the sealed sheet gives the two dim nights past the stop by day, for play only.
7. No hint of growth before year 70: held. No release, decide release, sheet or board carries a line on a change in powers; the decide releases prompt nothing. All seven gods still wrote "I try to grow no power this year" in their decisions, unprompted, as a habit from earlier years.

### Waiting on step 6 (not failures now)

- The morning story, the closing and the held painting request (the two `check.py` findings).
- `P/player/chronicle/chronicle-god.md` still carries the build 6 "After the held moment (provisional; not yet told to the player)" section for Year 3, including the firing. The DM's step 6 update should set it aside under build 7, as flag 1 does for the Keeper's files.
- `P/player/pending.md`: the morning list must take the three pending asks from `dm.md` and drop the old silences 3 and 4. In the set-aside draft the netmaker of the seventh month was "she"; tonight's record has "he". The draft is set aside and was never told, so this is not a contradiction, but the DM's list should follow tonight's record.

### Rulings for review

- **Set-aside drafts in public (flag 1).** The Keeper ruled to leave the build 6 files unedited but for a head line. Under build 7 ("no public file tells anything past it"), should a set-aside draft that tells past the held moment stay in the public folder at all, or move to the sealed folder?
- **Both prepared scenes boarded (L-0051).** Read and accepted for this run: section 2 of `year-turn.md` gives a board for each prepared scene, the thread still stops at the first, and the second board is written for each way the first can fall. The two lines of `year-turn.md` are still for Michael to settle.
- **The near stone without the sealed factor (r-0392).** The Keeper classed what the stones weigh as "came about in the game", which `year-turn.md` section 7 rolls with the sealed factors after the odds, and then rolled it without the factor, since a near stone that is not the weight is no success of the search and the god's favor has no side. The roll fell at 10 against 40, so 45 would not have changed it. Accepted as a reasoned judgment. For Michael: does a "near miss" world fact turned up by a search take the factor?
- **The Year 3 public line on the sealed act (flag 7).** `decisions-003.md` line 55 names the pocket in public. Reword it too, or let it stand as the record of its day?
- **The `dim-nights` label allow.** Standing from Year 1, against run 06 item 71. Every count read for meaning tonight; none is past what was seen. For Michael, as before: replace it with line allows.

## Round 2

Recheck by the continuity checker, 2026-11-26, written at 21:15 Pacific, against commit 5cadf4c ("sim-06 Year 4 night: the checker's round 1, flags 1 to 6 fixed"). Pulled first; already up to date. Read: the diff 3a8da0f to 5cadf4c in full, the new `S/releases/003/dm-set-aside.md`, the keeper log section "7. The check, round 1", r-0407 in the sealed roll log, the Longwalk's Year 4 report for the lines added to god-beasts's release, and every public file for the firing's outcome by search.

### Scripts

- `tools/check.py sim-06 4 --step 7`: the same 2 findings (the morning story and the held painting request, both step 6) and the same note. Not flags now.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning (the standing `dim-nights` label allow); dashes 0.
- `tools/lockcheck.py sim-06 --all`: 0 failures; 60 place warnings (the two more are in the new sealed `dm-set-aside.md`, the moved build 6 lines, as before in their old place); the same release warning and roll note.

### Round 1 flags, rechecked

- **Flag 1: resolved.** `P/civs/unnamed-people/state.md`: the two lines are moved whole to `S/releases/003/dm-set-aside.md`, with a set-aside line in their place; what remains (the two asks of the Year 2 winter sitting met no answer then) lies before the played moment and is true. `P/releases/003/dm.md`: a set-aside line at its head, and its Year 3 sections from "The rest of autumn" through "Summer" moved whole to the same sealed file, with a marker; the line left at 214 is the second nest of Year 2, before the moment. Nothing deleted. The people's two drafts keep their head line, as the open question to Michael. See flag 8 for a file of the same kind that round 1 did not name.
- **Flag 2: resolved.** The Keeper's ruling is withdrawn and logged. r-0407: the master of the potters' firing of the spares, on the branch "spares fired", factors written before the die and now resting on the fixed kiln capacity (flag 6), sealed factor at player step 1, stated 45, rolled at 50, 1: success either way. `dm-sealed.md` gives the outcome as a fact ("come out whole, every one of them, as many as were shaped") and the kiln board has nothing for the DM to roll. The factor is named in the roll's `--what` and in the keeper log only; nothing the DM reads names it. The reason line no longer marks the spares as at more risk, and agrees with the fact.
- **Flag 3: resolved.** The pass-one release (line 24), the people's year file (line 23) and report (line 10) now say only that the Weigher told the Stallreeve where it stands on the master of the smiths' ask, and that he would not carry that one either; the pass-one release adds that the answer for the woman of the back houses was not spoken at the post. This matches transcript lines 245 to 247 and `decisions-004.md` item 6.
- **Flag 4: resolved.** `P/releases/004/dm.md` now ends the line at "The boatmen saw."
- **Flag 5: resolved.** god-beasts's release tells both askings of the apart clans' herder, the month 10 answer in the words of its decisions (item 6) and what his clan made of it, and lists nothing unanswered. The added line on the herder of the two clans (reading his herd at dusk in month 10) is in the Longwalk report, line 26. "A thing given twice is a custom" is the eldest head's in month 1, in the ring and not to the god (report lines 10 and 66), and the release gives it that way.
- **Flag 6: resolved.** The keeper log names the r-0378 factor as unsupported; the roll stands (26 is a success at 50, 55 and 60). The kiln's capacity is set as a new fixed fact, conservatively (about sixty pieces of these sizes at a stacking; twenty-two its usual load for weights), on the sheet in the master's parameters, and the kiln roll's factor is reworded to "two and a half times as full", which matches fifty-five against twenty-two.
- **Flag 7: open,** the DM's at step 6, as in round 1.

### Raised in round 2

**Flag 8 (moderate). One more public file tells the held scene's outcome.**
- Rule: as flag 1: build 7 point 2 and `year-turn.md` section 1; checker item 6.
- Where: `P/releases/003/civ-unnamed-people.md`, the Keeper's Year 3 pass-two release to the player's people, line 6: "The potters' third nest, fired to the old six, agrees with itself and with them to a hair. The date the ring set for the town's weight holds." Line 7 tells the netmaker's seventh-month question as already met with no answer. The file has no set-aside mark.
- What the record says instead: the same two lines the Keeper moved out of `state.md` for flag 1. The firing is held behind the potters' door, and the netmaker's question is now pending from tonight's stretch (`P/releases/004/dm.md`, pending 3). Round 1 missed this file. The fault is the checker's search as much as the Keeper's fix.
- Fix (Keeper, correct the record): as for `state.md`. Move lines 6 and 7 whole to `S/releases/003/dm-set-aside.md`, put a set-aside line at the file's head, and keep only the part of line 7 that lies before the played moment.

### Build 7 points, round 2

1. The played moment accepted whole: held. The misstatement (flag 3) is corrected.
2. The thread stops at the next held moment, and no public file tells past it: not yet held. Flag 1 is fixed. Flag 8 is a further public file, and the provisional section of `chronicle-god.md` waits on the DM at step 6. The people's two set-aside drafts are with Michael.
3. Both boards in `dm-sealed.md`, and `dm.md` limited to what the god knows: held.
4. No DM result changed: held. The DM still has no roll on the kiln board, and r-0407 is the Keeper's.
5. Search, day away, pending asks, habit, sealed act: held, apart from flag 7.
6. Phenomena months and counts by month: held. Nothing changed.
7. No hint of growth before year 70: held. Nothing in the fixes touches powers.

### Rulings for review, round 2

- The Keeper's three new rulings (build 6 matter moved to a sealed set-aside file and marked; a board's chance range for the player's people rolled by the Keeper with the factor and given as a fact; a roll whose factor proved unsupported stands, with the fact it assumed set conservatively) are read and accepted. Each agrees with the flag it answers and with `sealed-factors.md`.
- The open questions of round 1 stand for Michael: whether set-aside drafts stay in the public folder; the two lines of `year-turn.md` on boarding (L-0051); the near stone and the factor (r-0392); the Year 3 public line on the sealed act; the `dim-nights` label allow.

## Round 3

Recheck by the continuity checker, 2026-11-26, written at 21:18 Pacific, against commit 0cb2e31 ("sim-06 Year 4 night: the checker's round 2, flag 8 fixed and the earlier build's public Year 3 lines set aside"). Pulled first; already up to date. Read: the diff 755068e to 0cb2e31 in full, the additions to `S/releases/003/dm-set-aside.md`, the keeper log's round 2 section, `P/civs/unnamed-people/people/tally-keeper.md`, and the Year 3 flags on the Tally-keeper's answer. Searched every public file under `campaigns/sim-06/` again for the older telling of the firing and of the pending asks.

### Scripts

- `tools/check.py sim-06 4 --step 7`: the same 2 findings (step 6) and the same note. Not flags now.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning (standing); dashes 0.
- `tools/lockcheck.py sim-06 --all`: 0 failures; the same 60 place warnings, release warning and roll note.

### Rechecked

- **Flag 8: resolved.** `P/releases/003/civ-unnamed-people.md` has a set-aside head line; line 6 is moved whole to the sealed set-aside file with a marker; line 7 keeps only the part before the played moment (the two asks of the Year 2 winter sitting, met with no answer then). The further places the Keeper found are moved or marked: nine in the later sections of `P/releases/003/dm.md`, each with a marker (the last "to a hair" hit there, line 214, is the second nest of Year 2, before the moment); the world section of `P/releases/003/civ-unnamed-people-pass1.md`, with a head line; and set-aside lines in `state.md`, `lore.md` (at its close-of-year Year 3 heading) and `chronicle-people.md` (at its Year 3 section). Nothing deleted. The search finds the firing's outcome in no public file except `chronicle-god.md` (the DM's, step 6) and the verbatim transcripts.
- **Flag 7: open,** the DM's at step 6.

### Raised in round 3

**Flag 9 (minor). A people file says that an asking was made behind the shut door, and that it was answered.**
- Rule: `year-turn.md` section 3.3 and DESIGN 12.2 (the public files never say that a sealed question was asked or that a sealed thing was told); checker item 6b.
- Where: `P/civs/unnamed-people/people/tally-keeper.md` line 15, the "Year 2 told again and Year 3" entry: "Asked plainly at the shut sitting whether she held anything of the seventh weight, answered plainly."
- What the record says instead: the Year 3 check (its flag 1, rounds 1 and 2) had this same asking and answer taken out of `years/003.md`, `years/003-report.md` and `people/head-of-reed-and-fish.md`, and recorded that no public file held the Tally-keeper's answer. This people file was missed in that search, by the Year 3 checker as well. The line lies before the played moment (the winter sitting of Year 2), so it is not a build 7 point 2 matter. The god heard none of it.
- Fix (Keeper, correct the record): reword the sentence to what came out of the sitting in the open, or take it out and keep it whole in the people's sealed folder, as the Year 3 fix did for the other three files.

### Build 7 points, round 3

1. Played moment accepted whole: held.
2. The thread stops at the next held moment, and no public file tells past it: held for every file but `chronicle-god.md`, which is the DM's at step 6. The people's two set-aside drafts are marked and with Michael.
3. Both boards in `dm-sealed.md`, and `dm.md` limited to what the god knows: held.
4. No DM result changed: held.
5. Search, day away, pending asks, habit and sealed act: held, apart from flag 7 (step 6).
6. Phenomena months and counts by month: held.
7. No hint of growth before year 70: held.

### Rulings for review, round 3

- The Keeper's marker form ("A line stood here that told Year 3 past the fifth day of its first month. It is set aside and kept in the sealed folder.") is accepted. It says only that something was set aside, not what, and it names no sealed note.
- The open questions of round 1 stand for Michael.

## Round 4

Recheck by the continuity checker after step 6, 2026-11-26, written at 21:32 Pacific, against commit ac9aead (the Keeper's flag 9 fix fa43498; the DM's step 6, 8af19e6 and ac9aead). Pulled first; already up to date. Read in full: `P/years/005/morning-story.md`, `P/years/004/closing.md`, the diffs of `P/player/chronicle/` (canon, chronicle-god, messages, people, threads, years), `P/player/pending.md`, the dated entry in `P/player/power-card.md`, `images/held/sim-06-005-morning.json`, `P/state/images.md`, the reworded lines of `decisions-003.md` and `decisions-004.md`, and the people's Tally-keeper file, public and sealed. Each was read against `P/releases/004/dm.md`, `S/releases/004/dm-sealed.md`, `S/years/004/year.md`, the transcript and the failures checklist.

### Scripts

- `tools/check.py sim-06 4 --step 7`: 1 finding, 1 note. The finding says the held request is approved and belongs in `images/requests/`. That is wrong: `P/state/images.md` approves the Year 2, 3 and 4 morning paintings and "any other painting ... not approved"; no Year 5 morning is approved (run 07: "No paintings"). The request is rightly held. **This is a known tool fault, not a campaign flag:** `tools/paint.py`'s approval match takes any approved play-year morning line as approval for any year. The coordinator is reporting it to Michael. The note is the old public roll ids, standing.
- `tools/lockcheck.py sim-06 --leaks --dashes`: leaks 0 failures, 1 warning (standing); dashes 0.
- `tools/lockcheck.py sim-06 --all`: 0 failures; the same warnings as round 3.

### Flags rechecked

- **Flag 9: resolved.** The public `people/tally-keeper.md` line 15 no longer tells of an asking at the shut sitting; the sentence is kept whole in the people's sealed folder. Searched again: no public file holds the Tally-keeper's answer.
- **Flag 7: resolved.** `decisions-004.md` lines 48 and 49 and `decisions-003.md` line 55 no longer name the act or the pocket, and no longer say the act was not played. They say only that a part of the sealed record was given there and nothing of it was stated in the open, which is the long-standing form of the rolling save's lines ("One sealed answer taken to the sealed record"). The Year 3 rewording answers the round 1 question to Michael on that line.

### The DM's step 6 work

- **The morning story.** It opens with a return sequence where the god stands at the potters' door. It tells the stretch from the gatepost as `dm.md` gives it, every fact matching the release and the record: the stones, the hill weigher's figures, the pans, the door-stone, the counts on the second stick, the one reason, the three silences, and the sky by months with no count. It stops at the board in the release's words, the master of the potters' opening words last, and nothing resolved. No sealed name, nothing of `dm-sealed.md`, no hint of the habit's town name, nothing past the door. Checklist: no invention, contradiction or forgetting found; no flattery, no pointing at signs, no corrected belief; the door-stone is told at the weight of the lines around it; no list beyond the pending asks the rules require; no hint of growth. The (oog) blocks say where the story stands against the clock, once, with the reason; that the provisional matter is set aside; the three asks; the record line; and the map.
- **The closing.** Written from what happened, in the DM's voice, and it tells nothing past the door. It runs to five sentences, where step 6 asks for three or four. Not flagged.
- **The chronicle files.** `canon.md`, `people.md`, `threads.md`, `messages.md` and `years.md` now hold the stretch as told, and stop at the door. The netmaker is "he", as tonight's record has him. "She holds the kept halves" (people, the Tally-keeper) is the played scene's own words (transcript line 295) and is not the sealed jar. `chronicle-god.md` holds the stretch, the held board, and the build 6 provisional section, now marked set aside.
- **`pending.md`.** The Year 5 morning's list matches `dm.md`: one held moment, three silences, one refusal, the asks answered by decided words, the asks waiting inside the held scenes. The older entries 3 and 4 are marked set aside in place.
- **The card entry.** Dated, from the release's "Rulings for the card and the record", and it changes no term of the card. It matches the canon line.
- **The held request.** `images/held/sim-06-005-morning.json`, wide. The house style block opens it, and the figure is described from the appearance card, seen from behind with no face. The scene is the landing at dawn in the first month of Year 3 with an anchor stone carried to the beam: a thing the god saw, inside the told stretch. The open-water owner and the Tally-keeper appear by look only. Nothing is from the sealed part, and nothing lies past the door. Held, not sent, as `state/images.md` requires.

### Rulings on the DM's points

1. **Set-aside marks in place in `chronicle-god.md` and `pending.md`, not moved to the sealed folder: accepted.** These are the DM's working files. Since Year 2 they have carried the older telling marked provisional under the standing ruling. Each mark now says plainly that the matter is not what happened, and the correct telling stands beside it. The text quoted under the marks was never told as fact. The Keeper's files were moved because they read as releases and state. This is the same question already with Michael for the people's two drafts. Until he rules, marking in place meets build 7 point 2 for these files.
2. **The `years.md` Year 3 year-end paragraph replaced by a bracketed set-aside note: accepted.** It keeps the other lines of the entry, says what stood there and why, and points to where the stretch is told.
3. **The card entry with no ledger id: accepted.** No ledger id is owed. The entry restates the standing fee and changes no term, and no ledger ruling was made for it. The only mechanical card write the Keeper makes in play is a gift's ledger id (`year-turn.md` section 6). The entry's last clause ("the Keeper enters it") and the canon line's "No ledger id was released" ask for nothing. They may stand, and nothing waits on them.
4. **No [painting] marker, and an (oog) line that the request is held: accepted.** `morning-story.md` and build check B7 say that a held request means nothing is painted and the morning posts without one. The (oog) line is true and points at nothing.
5. **The sealed act's private answer, written nowhere: accepted, with a step owed on the play day.** No public file may carry it, and the files do not yet say how a sealed part is answered privately. That question is the Keeper's ruling for review and is with Michael. Nothing is owed in a file before the play day. On the Year 5 played day, the DM gives the player what the act showed (the pocket empty, as the card gives) by the private way used for sealed parts, once and plainly. The DM then records it in `S/player/unsaid.md` with the date, under `## Act` (`engine/roles/dm.md`, "Sealed parts in play"). If the DM does not, the next check flags it under failures checklist 21, since what the god's own hand found is its own sense.

### Status

All flags resolved: raised 9, resolved 9, open 0. The check passes for Year 4. The clock may open Year 5 (step 8).

### Build 7 points, final

1. The played held moment accepted whole: held.
2. The thread stops at the next held moment, and no public file tells past it: held. Every set-aside matter is moved to the sealed folder or marked in place. The people's drafts and the DM's in-place marks are with Michael.
3. Both boards in `dm-sealed.md`, and `dm.md` limited to what the god knows: held.
4. No DM result changed: held.
5. Search, day away, pending asks, habit and sealed act: held. The sealed act's private answer is owed on the play day (ruling 5 above).
6. Phenomena months and counts by month: held, in the release, the morning and the chronicle.
7. No hint of growth before year 70: held, in the morning, the closing, the chronicle and the card.
