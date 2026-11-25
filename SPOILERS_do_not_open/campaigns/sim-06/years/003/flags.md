> SPOILER WARNING. Sealed. Year 3 continuity flags for campaign sim-06. Players must never read this file.

# Continuity flags: sim-06, Year 3

Status now: raised 11, resolved 0, open 11 (moderate 1, minor 10, major 0).

## Round 1

Run by the continuity checker (night turn step 5, the test's last), 2026-11-25, begun after the hand-off at 11:03 and written at 11:17 Pacific, against commit 5797e18 ("Year 3 night: pass two, the year record, rulings, state and the releases"). Pulled first; already up to date. Every check below was made against the files, not against the keeper log's word. Steps 7 and 8 are not written yet (the morning story, the closing, the painting request, the chronicle's step 7 update, the clock); findings that wait on them are not failures now.

Read in full: `CLAUDE.md`, `engine/roles/checker.md`, `engine/night/night-turn.md`, `engine/rules/failures-checklist.md`, `S/keeper/sealed-factors.md`, `S/rulings.md`, `S/years/002/flags.md` (rounds 1 to 3, the standing rulings carried), the keeper log from "Year 3 night turn", `S/years/003/year.md`, `world-events.md`, `held-coaster-played.md`, `S/state/luck.md`, the sealed roll log r-0300 to r-0341, the public roll log DM r-0011 to DM r-0015, the ledger L-0044 to L-0046, `S/messages/m-0003.md`, `m-0004.md`, `P/messages/m-0002.md`, the message log lines, the sealed notes `S/releases/002/civ-unnamed-people-hall-after.md` and `S/releases/003/civ-unnamed-people-hall.md`, the eight growth diffs, god-secrets's hidden powers diff and card entry, `P/releases/003/dm.md`, `civ-unnamed-people-pass1.md` (by search), `civ-unnamed-people.md`, `P/releases/002/dm.md` (the told stretch, for the comparison), `P/player/decisions-003.md`, `pending.md`, `corrections.md`, the Year 3 transcript (the told stretch and every board), the player's people's `years/003.md` and the needed parts of `years/003-report.md`, the diffs of the people's public folder, `chronicle-people.md`, the player-facing chronicle files, `conduct-profile.md`, `map-knowledge.json`, `map-log.md`, `knowledge.md`, the sealed `S/player/` diffs, god-dreams's, god-sea's and god-secrets's Year 3 releases, the seven gods' record-of-gods diffs, and the deep history lines on the old power's debts and the seventh. Read by search and in part: `engine/rules/encounters.md` 5 and 6, DESIGN 12, the player's card (the Good-Faith Reading), `S/map.json` for the places named, the seven NPC peoples' Year 3 files for other gods' names and the sealed factor's word, the other god and civ releases by search.

Severity, as in Year 2: major means the year is reworked; moderate means the record or state is reworked with no outcome changed; minor means a rewording or a log line.

## Script output

```
tools/check.py sim-06 3
clock not advanced to year 4
missing: the morning story (campaigns/sim-06/years/004/morning-story.md)
no painting request for the morning story
campaigns/sim-06/state/rolls.jsonl: rolls in the public log; rolls are sealed
4 finding(s)

tools/lockcheck.py sim-06 --leaks --dashes
FAIL leaks: campaigns/sim-06/player/conduct-profile.md:7: number word "two" near "god": "two mortals it is a god"
FAIL leaks: campaigns/sim-06/player/rolling-save.md:207: number word "two" near "god": "two mortals it is a god"
FAIL leaks: campaigns/sim-06/player/transcript-year-003.md:295: number word "10" near "came down": "10 because he came down"
FAIL leaks: campaigns/sim-06/player/chronicle/canon.md:50: number word "two" near "god": "god has told two"
FAIL leaks: campaigns/sim-06/player/chronicle/canon.md:50: number word "two" near "god": "two mortals it is a god"
leaks: 5 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/lockcheck.py sim-06 --all
places 0 failures, 41 warnings; leaks 5; releases 0; mysteries 0; rolls 1 (the public roll log); dashes 0
```

Judged: the clock, the morning story and the painting request are steps 7 and 8; not flags. The public roll log stands as ruled in the Year 1 flags and carried in Year 2 (DM r-0011 to DM r-0015 stand unedited); not a flag against Year 3. The 41 place warnings are map names without ids in the NPC civ agents' own sealed files and in `S/years/002/flags.md` (which does not count), plus one in `S/years/003/year.md` ("Aldermark" in a quoted trader's line, with [r10] beside it elsewhere in the file); the stamp tool was not run, as last year, and the keeper log says so. Noted, not flagged. The five leak hits are flags 10 and 11.

`tools/phenomena.py` for Year 3 per the keeper log: dim nights 6, tide gathering 2, crane gathering 1; months r-0300 to r-0305 give 8, 7, 5, 1, 5, 7, that is one in month 1, a pair in 5, a pair in 7 and one in 8. Every release and `year.md` agree. Fourteen since the arrival (3, 5, 6) agrees with every people's count.

## Flags

### 1. Sealed matter of mystery S01 in the player's people's public files (moderate)
- Check: checker.md 4 (the public folder holds no sealed term; no file holds more than its agent may show); DESIGN 12.2 (nothing in the player's campaign folder reveals a mystery); the sealed notes' rule, `S/releases/002/civ-unnamed-people-hall-after.md` and `S/releases/003/civ-unnamed-people-hall.md`: "nothing here goes in a public file unless it is said or shown in the stranger's hearing"; Year 2 round 1, "no public file holds the clerk, the loft's contents or the punt".
- Where, all public (`P/civs/unnamed-people/`):
  - `years/003.md` line 111: the ring set the looking with "the boatmen of every landing asked who else lent a boat on the night", and "It decided nothing of the sealed jar of the old keeper's halves, which nobody raised."
  - `years/003-report.md` line 109 (A3): "asked who else lent a boat on a night he asked about"; line 46: "The sealed jar was not raised and not opened."; line 100: "Circumstances held in the sealed notes bear on where the ring looks".
  - `years/003.md` line 109 and `years/003-report.md` line 36, `people/head-of-reed-and-fish.md` line 13: the Tally-keeper asked plainly "whether she held anything of the seventh weight on any stick of the old keeper's last years. She answered plainly."
  - `years/003.md` line 45 and `years/003-report.md` line 13: the Stallreeve "told the Assay-master in the hall ... what he had been told" by the boatmen, and the pair resolved to take it to the ring; line 109: "the Stallreeve told it what the boatmen had said".
  - `years/003.md` line 3: "What three of the town's people hold of the old keeper's loft and of the landing boatmen is the Keeper's sealed matter"; line 123: "what the Keeper's note has him ask".
- Record says instead: the god heard none of it. A boat lent on the night of the old man's death is the punt (deep history; the note). The sealed jar of kept halves exists only in the sealed note. A plain answer from the Tally-keeper about "any stick of the old keeper's last years" points at the clerk's witnessing. The loft's contents became shown in the god's hearing in month 10 and may stand; nothing else here did. The DM release is clean of all of it (checked); none has reached the player.
- Fix: the Keeper takes these lines out of the public folder: either reworded to what the town as a whole could say without the content (for example "the ring heard the three in the shut hall and set the looking: the hall's rooms, the old man's house, the landings, and the channel at low water") or moved to a sealed note, and the report's sealed circumstances go the same way. No outcome changes. Rerun the scan. No `corrections.md` line is owed, since the player has not been shown it. Owner: the Keeper (the people's agent is not running).

### 2. "A sunk punt" in the drag's failure (minor)
- Check: failures checklist 21 and the Change List rule it cites (no second wrong explanation set beside a true sign); failures checklist 17; the mystery standard (nothing marked by tone or wording); fixity (the roll's own branch).
- Where: r-0330's failure branch reads "silt, old pots, a sunk boat"; the people's agent's A4 reads "a sunk boat or two". The Keeper wrote "a sunk punt" (`S/years/003/year.md` line 16, "a sunk punt of no one's"), and it went to `P/releases/003/dm.md` line 86, `P/releases/003/civ-unnamed-people.md` line 5, `P/civs/unnamed-people/state.md` line 48 and `P/civs/unnamed-people/knowledge.md` line 67.
- Record says instead: the one punt in mystery S01 was lent and returned before light (deep history; note); `year.md` itself says "there is only the one punt". A sunk punt brought up below the hall, told to the player at the same weight as the pots, is a false lead set by a word choice: if the player later hears of a borrowed punt, this one reads as it.
- Fix: the roll's own words, "a sunk boat", in the five places. Owner: the Keeper.

### 3. The DM release's list of what is told differently (minor)
- Check: L-0046 (every told line an answer makes false is listed for the DM, so the DM can tell the player); encounters.md 6; failures checklist 2.
- Where: `P/releases/003/dm.md` lines 9 to 14.
  - Item 4 says "The yard's later cry of 'Weightward' with no answer, and the year-end sitting that 'waits on the Weigher's answer', did not happen." Neither was told to the player: the transcript tells the ninth month's board without its "since then" lines and stops the told year at the tenth month's board (transcript lines 339 to 413; `pending.md` marks both "not yet told to the player"). Telling the player that untold things "did not happen" shows it a provisional resolution it never saw.
  - The list leaves out what the night added to the stretch the player was told as complete: from the first market after the weighing the Assay-master standing at the gate on market mornings watching it, and the Stallreeve's look each dawn (dm.md line 27), and Bren's household's gift in the third month (line 28; see flag 4). The player was told the autumn "as it stood"; the god would have seen these through it.
- Record says instead: the five items are right in what they say happened; the leak check holds (nothing of the overrule, the shut hall, the punt, the clerk or the coaster's name is in the list or the release).
- Fix: drop the first half of item 4 (keep "The key was taken in the ring early in the tenth month", which is the answer the DM promised and is new, not different), and add a line that the told autumn now also holds the Assay-master's watching at the gate and the Stallreeve's daily look, which follow from what it said in the hall. Owner: the Keeper.

### 4. Bren's household's third-month gift added to the stretch that stands as told (minor)
- Check: checker.md 1 (cause); L-0046 (what does not turn on what a mortal now knows stands as told; in doubt the told line stands; nothing is loosened further than the play loosens it).
- Where: `P/civs/unnamed-people/years/003.md` line 53, `years/003-report.md` lines 14 and 150, `people/bren.md` line 13, `P/player/chronicle/chronicle-people.md` line 111, `P/releases/003/dm.md` line 28.
- Record says instead: in the third month of Year 2 only the Assay-master and the Stallreeve knew what the god had said, and Bren's household knew nothing until the sixth month. Nothing played reaches them before then. The told autumn (transcript lines 229 to 245) has no gift. The event is new in a part of the year the ruling keeps as told, with no cause from play; the people's agent's only ground is the old custom (record.md line 58), which held as well in Year 1 and the told Year 2 without a gift.
- Fix: the Keeper either takes the gift out of the reworked stretch and the DM release, or records a cause from play for it and lists it under flag 3. Owner: the Keeper.

### 5. The held moment's thread resolved past contact, not marked provisional (minor)
- Check: encounters.md 6 ("Everything else in the year that does not depend on the outcome continues"; "the Keeper notes the dependency in the release"); failures checklist 7.
- Where: `P/releases/003/dm.md` line 101 ("The coasters went out in the tenth month without a word.") and line 119; `S/years/003/year.md` line 40 ("The coasters went out in month 10 without it. Nothing else in the year turns on it.").
- Record says instead: the held board asks the god for the words, to go with the open-water owner's coasters past the Horn. Whether the word sails in month 10 turns on the answer. The people's agent stopped it rightly (`years/003.md` line 221: "What they carried in the way of a keeper's word is the Keeper's, since the word the ring asked for is held").
- Fix: the release marks the coasters' sailing without a word as provisional on the held answer (or says only that they sailed in month 10), and `year.md` says the same. Owner: the Keeper.

### 6. The hall's rooms searched in two different months (minor)
- Check: failures checklist 2 (contradiction).
- Where: `P/releases/003/dm.md` line 64 and `years/003-report.md` A1: "in the last week of the sixth month" (winter); `P/civs/unnamed-people/years/003.md` line 123: "In the same month [the seventh] the looking began. The three, with the Tally-keeper, went through the rooms of the hall over three days". Also dm.md line 63 and 64 set the sixth month's dim night and the sixth month's search under "Spring"; the sixth month is winter.
- Fix: one month in both, and the sixth month's lines under Winter in the release. No outcome turns on it. Owner: the Keeper.

### 7. Dim nights at the wrong months and uncounted in the people's files (minor)
- Check: DESIGN 12.8 (a phenomenon at its true count, when it is seen); Year 2 flag 11 and Year 1 flag 3 (the same kind).
- Where:
  - `P/civs/unnamed-people/years/003.md` (Year 2 told again): line 75 puts the winter night in the fifth month (record: month 6); line 127 puts the spring night in the eighth (record: month 9); line 167, summer, "on a night with no cloud" (record: two, months 11 and 12).
  - The same file, Year 3: line 183, "on some nights early in the month" (record: one, month 1); line 207, "on nights in the dead of winter" (two, month 5: right in count only by a plural); line 215, "on nights in spring", all under month 8 (record: a pair in month 7 and one in month 8).
  - `P/player/chronicle/chronicle-people.md`, Year 3: "on some nights early in the month"; "on nights in the dead of winter"; "on nights in spring".
- Cause: `P/releases/003/civ-unnamed-people-pass1.md` line 103 gave "certain nights ... in the first month, in the dead of winter and in spring", with no count or month, so the agent could not write them true.
- Fix: the Keeper corrects each line to the record (month 6; month 9; two nights late in summer; one night in month 1; two in month 5; two in month 7 and one in month 8), in the year file and the people's chronicle draft. The scan allows a dim-nights count. For the owner: a pass-one release that names a phenomenon's months for the player's people would have prevented it. Owner: the Keeper.

### 8. A public saying put in the god's mouth from its (oog) answer (minor)
- Check: failures checklist 5 and 6 (musings as orders; acting for the player).
- Where: `P/civs/unnamed-people/years/003.md` line 215: "because by then the Weightward had said it watched the light and meant to learn its habits, and the line was used to it."
- Record says instead: Year 2 decision 16 is the player's answer to the DM's (oog) question on how it keeps its nights (`player/transcript-year-002.md` line 79). It was never said to anyone in the town.
- Fix: reword to what the town sees (it sits at the landing through the night by the lamp, awake); nothing said. Owner: the Keeper.

### 9. Two release faults: an act of the god left out, a contradiction (minor)
- Check: night-turn.md 6 (the DM release holds what the god did); failures checklist 2.
- Where:
  - `P/releases/003/dm.md` line 116: "The ring sat on the third nest". The people's year file (line 217) and the resolved nest (r-0331) have the Weightward call the third nest in its pans before the ring at that sitting. The god's own act is missing from the release.
  - `S/releases/003/god-secrets.md`, "Asked of you and not answered": lists the reed cutter's daughter's ask, notes in brackets that it was answered, and ends "Nothing asked of you went unanswered."
- Fix: add the god's reading of the third nest at the ninth month's sitting to the DM release; in god-secrets's release move the daughter's ask to what was answered, or keep it as asked and drop the last sentence. Owner: the Keeper.

### 10. Four scan hits in the DM's files of the played day (minor)
- Check: checker.md (a hit in a public file is fixed by rewording the file, never by an allow line); DESIGN 12.2.
- Where: `P/player/conduct-profile.md` line 7, `P/player/rolling-save.md` line 207, `P/player/chronicle/canon.md` line 50 (twice): "told two mortals it is a god".
- Record says instead: the phrase counts mortals, not gods, and reveals nothing; but these are not frozen card text, so they are reworded, not allowed. Already put to the DM in `P/player/corrections.md` (Year 3 night).
- Fix: the DM rewords each at step 7 ("it has now told the Assay-master and the Stallreeve what it is"). Owner: the DM at step 7. The step 8 rerun of the scan checks it.

### 11. The scan hit in the day's transcript (minor)
- Check: checker.md (the leak scan, `leak-allow.txt`).
- Where: `P/player/transcript-year-003.md` line 295, the DM's (oog) odds post: "plus 10 because he came down to you himself".
- Ruled: not a leak under DESIGN 12.2. "Came down" is the ship owner walking to the landing; the figure is a step of the stated odds. The transcript is the verbatim record and is not reworded.
- Fix: one line in `S/leak-allow.txt` for the phrase "10 because he came down", with its reason and date. This round's go covers the two flags files only, so the line is not written here; it is the checker's to write at its recheck, with the orchestrator's go, before the step 8 scan. Owner: the checker.

## Checked and holding

- **The rework of the told stretch (L-0046, special attention).** Every played board is reached and none is unmade: the hall in month 1 (words, refusal, the chest locked before the Stallreeve, the Stallreeve told at the door); the landing in month 4 (the board as told, the ship owner not yet told, which is why the release says he did not know; DM r-0013's terms and the Stallreeve's additions word for word); the gatepost in month 9 (the vote six for, four against, one away, as told on the board's lead-in; the board's words; the scale out, DM r-0014 and r-0015; the player's words whole, including "The Assay-master asked, and I told him", which stands as said though the yard had heard it in month 6); the gate in month 10 (her balance, the line, the three asks). The ring arrives at each board with new reasons (the sitting in month 6, the looking) and none is moved. Lines of the released year changed: the month 4 board's aftermath, the ninth month's "since then", the twelfth month's sitting and its waiting on the seat (none of the three was told to the player), each made false by a played answer or overtaken by the played yes; the weather, the river, the sky, the pits, the loft looked in, the Stallreeve among the boatmen, the nest, the tiles and the witnessing stand. The one added line that no answer causes is flag 4; the list's faults are flag 3. Nothing is edited in Year 2's files; the stretch is written again in Year 3's.
- **The overrule (sealed-factors.md, check 5).** DM r-0011: the god's own attempt, the player's god at step 1, stated odds 75, rolled 78, failed by 3, inside the shift of 5; the first DM roll of the god's played year by id, and none from the Year 2 play day was overruled (Year 2 round 1). The told scene leaves room (the refusal told; the sitting's date left open in so many words, transcript line 255). Logged in one line with id, odds, shift and outcome carried. DM r-0012 and r-0014 are the world's questions, DM r-0013 a success, DM r-0015 a draw: none qualifies. No public roll line touched. The release shows only the consequence (the sitting in month 6, the word held by two); no public file names it.
- **The sealed factor, checks 1 to 4.** Named at its step with stated and rolled odds on r-0324, r-0330, r-0331 (the player +1), r-0332, r-0333 (god-beasts +1), r-0341 (god-secrets +1); every roll for a god at 0 says so (r-0334 to r-0340); none for god-healing; no contest between gods; the weighted draw r-0320 has one god among its targets, at 0. Every factor list adds up to its odds; all inside 5 to 95. r-0322 is the tool's void draw, replaced by r-0323. r-0325 to r-0329 are the world's questions and carry no factor, rightly. None of the six turned on the factor. `luck.md` unchanged in value, with its dated Year 3 line matching the keeper log. The word appears in no public file, release, card or civ file of the year; its uses in god-rivers's and god-sea's own `self.md` and `people-hoped.md` are from creation, unchanged this year, and stand as allowed at the lock in those files only.
- **Rolls and cause.** r-0300 to r-0341: every contested outcome has a logged roll, none rolled twice. Every event in `year.md` and `world-events.md` traces to a schedule row, a roll, a record fact or a decision. New fixed facts are logged with what reached them: three of the eleven call a sitting out of turn; the raking household's thin season; the league houses' weights and the council's set at Corrith; the chancery's claim on the Sarrow; the granary figures (a third of the roll, mystery S03's branch). The likeness the Keeper pointed at (the old factory's debt to a salt house of the delta) is set from the deep history's line that the river houses owed the delta's salt rakers (deep history, 361 BA); it holds.
- **Powers and rulings.** L-0044: the sitting's account of the Reading matches the card's Description and Limits and no more; the drawback is not volunteered, inside the god's right to keep silent. L-0045 narrows nothing beyond L-0041 and the card. L-0046 is in the ledger and binds. god-secrets's Tally-Reader surfaced on its written condition (a stranger's tally handed to it), entered on its card dated and as discovered; its drawback is in the release as felt. No other hidden power's moment came for any god (checked against each file's "Surfaces when"); no NPC god folder holds an unsurfaced power. Growth: nothing earned; no attempt stated by any god in three years; each use line stands against an event of the year.
- **Knowledge.** The DM release holds only what the Weigher saw, heard or was told: the shut hall is given only as the town learned it (the looking and the seat's date), the loft only in the Assay-master's words when asked, the coaster's master without name, house or port, and nothing of the punt, the clerk, the jar, the stand-down motion or the overrule. Names: "the Horn" (the Stallreeve, at the held board) is in `player/map-knowledge.json` as a rumor, the Dunmar Horn [r17], grid cell B4 (checked against the map), in the same commit as the release; the Aldermark marked as named; `knowledge.md` carries place names only. Each NPC god release names only its own god and ends "you felt no other like yourself". The two rumors of another god (god-dreams of the player's god, by r-0337 at Port Sennet [f75] where the coaster's news is quay talk by the winter; god-secrets of god-thresholds, by r-0341) came by rolls on the gods' own askings through people who had the news by the world's own carrying, and each is given as heard, with no name and no count. No NPC god acted on what it could not know: god-dreams's mistaken sixth decision met its people's knowledge and was not corrected in its file.
- **Neutrality.** The self-check names every use of the factor and each temptation. The player's sealed wants: none confirmed, none applied; the pocket not checked, nothing resolved from it, and no clue moved. The sealed fear of the Reading question: the question was rolled at the DM's own base and factors for the same question, not chosen. No `requests-answered.md` line added. No correction of a belief; no clue held back (the loft told when asked, the drag rolled with the truth in its favor and failed). Recurring things at the tool's counts in every release and `year.md` (the people's files are flag 7).
- **The player.** Decisions file present; the year turned. Each of the twelve items is applied on its own words and no further. The one held moment of Year 3 stops at contact with its board (flag 5 is its one consequence run past). Questions about a particular power met silence and are pending, by L-0032 (see rulings for review). The witnessing in month 4 of Year 3 acts on Year 2 decision 15, with no power used, as Year 2 accepted.
- **Mystery standard.** No clue states a mechanism. The hill kin's saying ("the six weigh what is and the seventh weighs what is owed") is a people's saying, right in part and wrong about the hall; the people's agent's notes give no "due", so it is not drawn from sealed matter. The loft's words are the Assay-master's answer to a direct ask, at the length of the other quoted answers in the release. No decisive clue by a visitor (the coaster's master told none of her news).
- **Map and travel,** by `tools/map.py travel` (run for each): the unnamed town [f20] to Ruddfold [f25] by the Old Rudd Way [f23], 123.9 miles, 7 days on foot; the unnamed harbor town [f30] to the Drowned Causeway [f33] round the shore, 66.5 miles; Wellen Ford [f47] down the River Wellen [f08] to its mouth by boat, 133.6 miles, 4.5 days (god-rivers's 90 miles down at 30 a day and about eight days back at 12 agree); the unnamed walled town [f35] up the River Iss [f11], 39.7 miles, 3.3 days up, 4 full days with the walk to the water. god-sea's swim in spring falls after the stilled water's season (lamp in month 5, the harbor closed to it through month 8, the swim from the open sea off the point). Directions given in releases ("the delta in the far west" from f35; "in the west" from f75) agree with the map.
- **Messages.** m-0002 (the player's word to Ruddfold, its fate as the god knows it), m-0003 and m-0004 each have a logged journey to the recipient and a fate in `messages.jsonl` and the file; m-0004's failure branch (wintering at the harbor) agrees with r-0336.
- **Counts.** No public file states a count of gods in any wording; the five scan hits are counts of mortals or odds (flags 10 and 11). The dim-nights counts in `dm.md` stand under the Year 1 allow line and are nights the god saw.
- **Helpers.** None forced back; nothing the player left unnamed named by the Keeper (the town stays unnamed; "the Horn" was named by a mortal).
- **Year 2, flag 11.** The two lines of `chronicle-people.md`'s Year 2 part are corrected (the second month's single night, the two nights late in summer, the pits judgment given to Orrin and the west kiln-master). Resolved; Year 2 now stands raised 11, resolved 11, open 0. The public Year 2 flags file still shows round 3; its last line is the checker's to add at the recheck.
- **Dashes:** none in either campaign folder.

## Noted, not flagged

- The stand-down motion, the votes inside the shut hall and the ring's private arguments are in the player's people's public files. They are the ring's own doings, not a mystery's matter, and the Keeper kept them out of the DM release. Whether the player's people's public files should hold what was said behind a shut door outside the god's hearing is for the owner; flag 1 covers only what the notes seal and what points at S01.
- The Keeper reworded a mortal's quoted words to pass the scan ("what the three of us saw" to "what we saw", the Assay-master on the loft), where the note asked for his words exactly. Meaning unchanged; the release quotes the reworded line. Accepted as wording.
- The upriver traders of Year 2's summer went home "as told" with the story of the heavy pieces, though the town had heard the god in month 6 and month 9. The told line stands in doubt, as L-0046 says, and Year 3's traders carry the rest.
- `S/years/003/year.md` line 67 garbles the drovers' line ("no one has seen her eat a second day's road from a door"); god-secrets's release has it plainly ("whom no one has seen eat"). The release is what the agent reads.
- god-secrets's release has "four days up with a day lost to the current"; the tool gives 3.3 days and 4 full days with the walk. Read as the day lost making four. Within the tool's figure.

## Rulings for review

- **Silence on a plain question about a particular power (keeper log pass two; L-0032).** The Keeper's ruling stands and is applied as logged. For Michael, the cost the checker sees: the god had just said before the yard, in the player's words, "I will say yes or no, or I will say I will not answer", and then met three such questions with none of the three, in the same sitting. "I will not answer" is one of the god's own stated answers and decides nothing about the power. The fever question's silence is followed in the people's record by the child's death (an ordinary winter death, with its cause in the told fever) and the back houses' saying. Should standing words that promise one of a closed set of answers default to the least committal one in that set, instead of to silence?
- **The transcript hit (flag 11).** Ruled not a leak; the allow line waits on a go.
- **The told year reworked (L-0046).** Checked as applied; the design question (resolve a year only to its first held moment and resume it after) stands as the Keeper listed it.

## Counts, round 1

Raised 11 (moderate 1, minor 10, major 0). Resolved 0. Open 11. Owners: the Keeper, flags 1 to 9; the DM at step 7, flag 10; the checker at its recheck, flag 11.
