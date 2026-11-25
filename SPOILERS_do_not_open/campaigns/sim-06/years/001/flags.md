> SPOILER WARNING. Sealed. Year 1 continuity flags for campaign sim-06. Players must never read this file.

# Continuity flags: sim-06, Year 1

Rounds 2 and 3 (the rechecks) are at the end of this file. Status now: raised 9 in all, resolved 9, open 0.

## Round 1

Run by the continuity checker (night turn step 5), 2026-11-24, from 16:34 to 16:43 Pacific, against commit f5f2479 ("pass two, the year resolved, handed to the checker"). Pulled first; already up to date. Every check below was made against the files, not against the keeper log's word. Read in full: `CLAUDE.md`, `engine/roles/checker.md`, `engine/night/night-turn.md`, `engine/design/DESIGN.md`, `S/keeper/sealed-factors.md`, `S/rulings.md`, `S/years/001/year.md` and `world-events.md`, the keeper log from "Year 1 night turn", the ledger L-0031 to L-0036, `S/state/luck.md`, `standing.md`, both roll logs from the year's first roll, the player's decisions, the player's people's year file, the public pass-one release, the god-sea decide release. Read by search and in part, where a check needed them: `engine/rules/*.md` (powers, failures checklist, morning story, time and pace, encounters), the event schedule, mysteries S04 and S07, the seven decisions files, the seven records of gods, the four changed cards, every sealed hidden-powers file, the eight growth files, the eight peoples' Year 1 files, every map log, the player's map knowledge and the people's knowledge file, and the diff of f5f2479.

Result: 6 flags. None blocks the releases; each is a rewording or a log line. Nothing in the year needs a roll redone or an outcome changed.

## Script output

```
tools/check.py sim-06 1
clock not advanced to year 2
missing: the DM release (campaigns/sim-06/releases/001/dm.md)
missing: the morning story (campaigns/sim-06/years/002/morning-story.md)
no painting request for the morning story
campaigns/sim-06/state/rolls.jsonl: rolls in the public log; rolls are sealed
5 finding(s)

tools/lockcheck.py sim-06 --leaks --dashes
leaks: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/lockcheck.py sim-06 --all
FAIL rolls: campaigns/sim-06/state/rolls.jsonl: the public rolls log is not empty; rolls are sealed
places 0, leaks 0, releases 0, mysteries 0, rolls 1, dashes 0
```

Judged: the clock, the DM release, the morning story and the painting request come after step 5 (night-turn.md 6 to 8). Expected at this step, not flags. The public roll log is ruled below under "Rulings for review" and is not a flag against the year.

## Flags

### 1. The sealed factor's name in the Sarrow's own year file
- Check: sealed-factors.md, the checker's check 4; checker.md 5.
- Where: `S/civs/sarrow/years/001.md` line 13: "which was luck, and the people said afterward that it was not luck." Written by the Sarrow's civ agent this year (cb442e3).
- Record says instead: no word of the factor stands in any file a civ agent reads. The ordinary-word allowance covers an NPC god's own files from its own answers only (lock flags, round 1), not a civ file.
- Fix: the Keeper rewords the line (for example "which was chance, and the people said afterward that it was not chance"), no meaning changed, and logs it.

### 2. The sealed factor's name in god-sea's people's lore
- Check: as flag 1.
- Where: `S/civs/unnamed-people-sea/lore.md` line 20: "The Master of Timber is said to have had a lucky year." Written by that people's civ agent this year (cf15792).
- Record says instead: as flag 1.
- Fix: reword (for example "a good year" or "a fortunate year"), and log it.

### 3. The single winter dim night told as several in the player's people's files
- Check: DESIGN 12.8 (a recurring phenomenon appears at its true count, never estimated or varied by an agent); `engine/rules/morning-story.md` (never "a few").
- Where: `P/civs/unnamed-people/years/001.md` line 35, "Some nights in the dead of winter, the blue star went dim"; `P/player/chronicle/chronicle-people.md` line 19, "The star went dim for a time on some nights of the cold season." (the second is the Keeper's own rewording in f5f2479).
- Record says instead: three dim nights in Year 1 by `tools/phenomena.py`, two in month 1 and one in month 5 [r-0244, r-0245, r-0246] (`year.md`, `world-events.md`). Month 5 is the dead of winter in this people's year, and it held one, not several. The other peoples' files give the true counts ("Two nights", "One night in month 5"). The pass-one release itself said only "again in the dead of winter", which is right.
- Fix: reword both lines to the singular ("On a night in the dead of winter ..."; "on a night of the cold season"). The scan's phenomenon check reads counts of two and more only, so the singular passes it. The month-1 lines ("some nights early in the month") are vague but not false; where the Keeper touches them, the true count is better than "some", subject to the scan question ruled below.

### 4. The player's people's state carries no resolved branch for the year
- Check: night-turn.md 4 (update state for the player's people); checker.md 3 and 7 (failures 3, forgetting; 9, stale state).
- Where: `P/civs/unnamed-people/state.md` and `years/001.md`. The keeper log (pass two, "State written") says each people's `state.md` carries the Keeper's line on which branch stands; the seven NPC peoples' files do, the player's people's does not. Its year file still reads, at month 6, "What came of it is for the Keeper (report-001.md). The town knows only what follows from each way."
- Record says instead (`S/years/001/year.md`, Keeper's resolution): the bonded man was taken [r-0255]; the council set a price in measure and the Tally-keeper holds the stick, unclaimed; the month 11 invitation is held at the laid stick. All of it is what the town itself saw and did; none of it is sealed.
- Fix: the Keeper adds its pass-two line to `P/civs/unnamed-people/state.md` (as for the other seven), giving the branch for the month 6 attempt and the held thread, in the town's terms, and corrects the keeper log's "each" if it does not.

### 5. A factor on r-0255 that the record does not hold
- Check: DESIGN 12.6 (odds from factors on the record); DESIGN 10.2 (a god needs no sleep; sleep is optional); checker.md 3.
- Where: sealed roll log r-0255, factor "the god does not sleep", step -20.
- Record says instead: no file of the player's records whether this god sleeps; it is the player's to set, and the people's agent wrote only that it "sits late" at the landing. The other factors stand on the record (the conduct profile's "It guards the scales"; the code of the lit lamp; dark and no watch).
- Effect: none on the outcome. Without the factor the stated odds are 30, rolled at 25 with the sealed factor; the roll was 95 and fails either way. The roll is not redone (DESIGN 12.6).
- Fix: a line in the keeper log naming the unsupported factor, the odds it should have carried, and that the outcome stands. No roll log is edited.

### 6. Keeper edits to the NPC peoples' own files not logged
- Check: DESIGN 12.2a (the keeper log is the index); checker.md 3 (every ruling recorded).
- Where: f5f2479 changed the civ agents' own `years/001.md`, `report-001.md` and `lore.md` for the Sarrow, the Longwalk, and god-dreams's, god-sea's and god-secrets's peoples: map ids added beside named places already there (the Herd Road [f40], Marle Ford [f61], Stair Pass [f62], the Aldermark [r10], the Rudd Hills [r18], the River Ellow [f07], the Iss Levels [r07], the Garrow Skerries [f31], the Iss Track [f37]). The keeper log records the rewording of the player's people's public files and rules on it ("yes for a scan hit, by rewording only"), but names no edit to an NPC people's file, and the ruling covers public files only.
- Record says instead: every edit is a bracketed map id beside a name already there (DESIGN 8.8 asks for one on every named place in a sealed file); no meaning changed (checked line by line in the diff). The appended "Keeper, Year 1, pass two" lines in the `state.md` files are logged.
- Fix: one keeper log line listing the files and saying what was added and why, and the 4.x ruling for review widened (or a second one) to cover the Keeper adding map ids to a civ agent's sealed files.

## Checked and holding

- Cause and fixity. Every event in `year.md` and `world-events.md` traces to a schedule row, a roll, a record fact or a god's decision. The new fixed facts (the Longwalk on the landing morning, the Bank Way [f21] dry-shod, the three named places) are each logged with the action that reached them. The league crew at the River Ellow's [f07] mouth stands on the Harbor League's record (Sutter Strand [r28] to the Ellow's mouth; coasters beached at night; salt pans). The random table, T-1 and the cast-figure roll follow the schedule's own words.
- Rolls. r-0230 to r-0256: every contested outcome has a logged roll, none rolled twice. Faces of r-0242 to r-0246 agree with their rolls. Every odds line is inside 5 to 95.
- The sealed factor. Checks 1 to 5 of sealed-factors.md: luck named in `--what` at its step with stated and rolled odds on r-0252, r-0253 (god-beasts +1) and r-0255 (the player +1); every roll for a god at 0 says so; no roll for god-healing or god-secrets; no contest between gods; no weighting due (the country rolls, T-1 and the dim-night months are no act and no choice among targets, as the schedule says); `luck.md` unchanged with its dated Year 1 line, matching the keeper log; no growth to a tier; no DM roll qualifies for an overrule (all five succeeded), none overruled, no DM roll line touched. Use named: r-0252, r-0253, r-0255; none turned the outcome. Words: flags 1 and 2; the four ordinary uses in god-sea's and god-rivers's own files stand as allowed at the lock, in those files only; the engine's "unlucky" (time-and-pace.md 71) stands as recorded at the lock for Michael.
- Powers. No decision used a power past its card: Calm Under the Lamp (L-0033, and the stilled water barring the god for a season, months 4 to 7), The Listening (L-0035), Keeping Sleep (L-0034), Finding What Was Hidden and the key (L-0036), Mending and Reading the Rot (reading wells "and with what", never who brought it about), the Latch, the Reading of the Host, Warm hands, Kept Word. The five surfaced knacks each meet their sealed "Surfaces when" (Windward Sense: the approach from downwind and the night watch against stalking wolves; Watch-Wakeful: a night at a sickbed; Banked Coal: a lamp kept in a rising swell; Figure-Memory: figures given without the book; Stray's Welcome: a strange hearth as the dog), each on its card the same day under the hidden powers heading as "knack". The hidden powers not surfaced (Sleeper Count, Tally-Reader and the rest) had no moment on the record. Growth: nothing earned, nothing logged against nothing; knack use lines in the player's growth file only where a related skill was used.
- Knowledge. No NPC god's own folder holds an unsurfaced hidden power or knack, its secret past, ceiling or growth (searched by every sealed name). No god's record of gods holds anything it did not meet; no god met another. Each release names only its own god. The player's four rumors and two told roads were said in the god's hearing by the people's report ("Names said aloud") and stood in the people's knowledge file before the year; they were recorded in `player/map-knowledge.json` in the same commit as the first file outside `knowledge.md` that uses them as the god's (`player/corrections.md`). Rumor cells checked against the map: Ruddfold [f25] B3, the Maun Stair [f27] B3 true; Hask and the Aldermark [r10] as told.
- Map and travel, by `tools/map.py travel` (run for each): Bank Way [f21] 1.4 miles; Old Rudd Way [f23] to Ruddfold [f25] 123.9 miles, 7 days on foot; the Iss Track [f37] from god-secrets's town 37.5 miles, 3 days; the River Ellow [f07] from the bend town to its mouth 112.4 miles, 4 days down and 10 back by boat, inside months 11 and 12. All agree with the record.
- Neutrality. The keeper log's self-check names every use of the sealed factor and each temptation; no unsaid want applied (none confirmed); no clue held back (god-healing's wells read as they stand; S07's branch applied); no correction of beliefs; recurring things at the tool's counts in every sealed record and every NPC people's file (flag 3 is the player's people's only). No `requests-answered.md` line added this year.
- The player. Decisions file present; the year turned. The dusk meeting resolved by the handed-off words only (L-0032), five unanswered asks to pending; the month 11 invitation held at contact; the thief's attempt and the Stallreeve's question handled as conduct and r-001 give. Nothing done for the player beyond its decisions and conduct.
- Mystery standard. No clue states a mechanism; no mortal fully right about a cause (the potters, the town on the dim nights, the three clans); no decisive clue by a visitor (the river party went to the coast; the league crew did not come); nothing marked by tone.
- Counts. No public file states a count of gods in any wording (scan clean; the public files changed this year read for meaning).
- Helpers. None forced back; nothing the player left unnamed named by the Keeper.
- Dashes: none in any file of either campaign folder.

## Noted, not flagged

- T-1 sends the coughing sickness to the mining holds, whose own Southhold sold the sick oxen in the first place (S04, the holds' record). The row's conditions were met and its roll stands; the holds' Year 2 is the Keeper's to tell consistently with the sickness having come from them.
- The three clans camped farther apart in the Year 1 winter. S04's clocked rows are triggered away "if the sick herds winter apart"; nothing turns on it until Year 3, and the Keeper should weigh the winters as they come.
- The player's people's report gives the god a lamp at the landing; the Keeper read it as the channel folk's lamp (keeper log). The public year file carries no lamp. No change needed.
- The river party's trip was priced by the checker, not logged by the Keeper; it agrees.

## Rulings for review

- **The public roll log (DESIGN 12.6 against the "rolls are sealed" lines and both scripts).** DESIGN 12.6 and sealed-factors.md ("DM rolls in play") tell the DM to roll in the open into `P/state/rolls.jsonl` and say those lines are never edited; DESIGN's "Sealed and public outputs" says the rolls log is sealed and the player sees only outcomes; `check.py` and `lockcheck --rolls` refuse a non-empty public log. The public lines also carry the die's value, which 12.6 says stays hidden, and their ids r-0001 to r-0005 repeat ids in the sealed log (the keeper log writes "DM r-000N" to tell them apart). Only Michael can settle it. Ruled by the judgment order: fairness to the player's intent (the odds stated in the open, outcomes shown, dice hidden), then fit with the design as written (12.6 and sealed-factors.md name the public log as the DM's and forbid editing it), then balance (nothing in the year turns on it): the five DM lines stand as written, unedited, and the two script findings are not flags against Year 1. For Michael: whether the DM's open rolls stay in `P/state/rolls.jsonl` (and the scripts and the "rolls are sealed" line change), or move to a sealed DM log with the open file holding odds and outcome only; and whether the two logs should share one id sequence.
- **Counts of a seen phenomenon in public files (DESIGN 12.2 and 12.8, morning-story.md, against the scan).** 12.2 bars a phenomenon's count from public files only before it has been seen; 12.8 and the morning story rule require the true count whenever it appears. The scan's phenomenon check refuses any count of two or more beside the phenomenon's words in any public file, seen or not, and the Keeper told the player's people's agent to give no count for that reason. The DM release and the morning story (steps 6 and 7) will meet this if the god saw the dim nights. Ruled by the judgment order: fit with the design comes before the tool, so where the god or its people saw them, the true count stands in the DM release and the morning story, and a scan hit on that line is ruled at step 8 as no leak under 12.2 (the count was seen) and, if needed, its exact phrase written to `S/leak-allow.txt` with its reason, as checker.md allows for a phrase ruled not a leak. For Michael: whether the scan should learn "seen" (from the people's and the god's records) so no allow line is needed.

## Counts, round 1

Raised 6. Resolved 0 at round 1; all 6 resolved at round 2 (below).

## Round 2: the recheck

Run by the continuity checker, 2026-11-24, from 16:50 to 16:53 Pacific, at head 6328501 (after the Keeper's fixes in 7255373 and the step 6 releases in 2cffee8 and 6328501). Read in full: the diff of all three commits, the keeper log from "5. The check, round 1" on, `P/releases/001/dm.md`, `P/releases/001/civ-unnamed-people.md`, the seven god releases and seven civ releases in `S/releases/001/`, and the changed lines of the people's files. Checked against the year record, the people's reports and year files, the ledger, the cards, the map knowledge files and the roll log.

### Scripts at 6328501

```
tools/check.py sim-06 1
clock not advanced to year 2
missing: the morning story (campaigns/sim-06/years/002/morning-story.md)
no painting request for the morning story
campaigns/sim-06/state/rolls.jsonl: rolls in the public log; rolls are sealed
4 finding(s)

tools/lockcheck.py sim-06 --all, before the allow line
FAIL leaks: campaigns/sim-06/releases/001/dm.md:94: phenomenon count "dim-nights"
FAIL rolls: campaigns/sim-06/state/rolls.jsonl: the public rolls log is not empty; rolls are sealed
places 0, leaks 1, releases 0, mysteries 0, rolls 1, dashes 0

after the allow line: places 0, leaks 0, releases 0, mysteries 0, rolls 1, dashes 0
```

The clock, the morning story and the painting request come after this step. The public roll log stands as ruled in round 1.

### The six round 1 flags: all resolved
1. Sarrow year file: "chance" in place of the factor's name. Resolved.
2. god-sea's people's lore: "a good year". Resolved.
3. The winter dim night is singular in the people's year file and the chronicle. Resolved.
4. `P/civs/unnamed-people/state.md` carries the Keeper's pass two section, and the month 6 line of the year file now says what the town saw. Both agree with `year.md`. Resolved.
5. The keeper log names the unsupported factor on r-0255 and the odds it should have carried (30, rolled at 25), and says the outcome stands. No roll line edited. Resolved.
6. The keeper log lists the stamp run and its files, with a ruling for review. Resolved.

### The allow line
`P/releases/001/dm.md` line 94 gives the true count of the Year 1 dim nights: three, two in the first month and one in the dead of winter. The player's people saw all three (their year file; `year.md`), so this is a count already seen. It is no leak under DESIGN 12.2, and DESIGN 12.8 requires it. Allowed: `dim-nights` written to `S/leak-allow.txt` with its reason and date. The scan exempts a phenomenon count only by its label, so the line lets every dim-nights count through in public files from now on. The checker reads each such count for meaning every year. For Michael: a line-level allow for phenomenon counts would be narrower. (Flag 8 is about a different sentence on the same line, not the count.)

### New flags

#### 7. The stamp tool wrote into the checker's sealed flags file
- Check: CLAUDE.md (an agent in a run has a go for exactly the files its role names); checker.md (the checker writes the flags file).
- Where: 2cffee8 changed `S/years/001/flags.md`, adding bracketed map ids beside eleven place names in three lines. The keeper log for that step says the flags file is the checker's and "the Keeper does not edit" it, and does not mention the change.
- Record says instead: the flags file is the checker's alone. No meaning changed, and the checker keeps the ids as its own from this round.
- Fix: a keeper log line naming the change. The stamp tool needs to skip `years/*/flags.md` and the lock flags, and only Michael can change a tool, so that part is for his review.

#### 8. The DM release says the Weigher was awake for every dim night
- Check: DESIGN 10.2 (sleep is optional); checker.md 4 (no release holds more than its agent could know); the Keeper's own note on flag 5.
- Where: `P/releases/001/dm.md` line 94: "The Weigher was awake under a clear sky for each."
- Record says instead: no file of the player's says whether this god sleeps. The Keeper said so in its flag 5 entry, and it told the people's agent "Whether it sleeps, the town does not know" (`P/releases/001/civ-unnamed-people.md`). The record shows that it sits late at the landing and was awake in the dark of month 6. It also shows that the line at the gate talked of the nights in its hearing (the people's year file, month 1).
- Fix: tie the god's knowledge of the nights to the record. Either it heard them spoken of in the line, or it saw them where the record puts it at night. Otherwise log a ruling for review on how the player's god spends its nights in unplayed time when the player has not set it, and let the DM ask in (oog). The count itself stands as allowed above.

#### 9. god-beasts's release leaves out the month 9 return of the cough
- Check: failures checklist 21 (a clue held back) and 2 (contradiction); mystery S04 ("SEEN by anyone who walks the herds").
- Where: `S/releases/001/god-beasts.md`: "The cattle of two clans that coughed last autumn still cough, some of them. A few died in the winter." This is the pass one sentence about the winter before the year began, carried over.
- Record says instead: `S/civs/longwalk/years/001.md` line 39: the cough came back in a small way in the ninth month, a few beasts only. The two clans separated those beasts from the herd and lost four. The god kept the herds' margin all autumn.
- Fix: give the month 9 return as the people report it, and drop or date the winter deaths line.

### Checked and holding, round 2
- The DM release. It holds only what the Weigher saw, heard or was told. It leaves out the Assay-master's reasoning, the nine days, his winter test as a test, the walker, the nicknames and the master's part. The meeting at dusk matches the people's report ask by ask. The held encounter stops at the laid stick, with its board. The pending list holds the five asks from the meeting and the year's, which match the report's list. The names told match `player/map-knowledge.json`. God-sense is nothing. No power was felt new. The L-0031 card text matches the ledger. No count of gods, no other god, no sealed term, no hidden power, no knack, and no trace of the sealed factor.
- The public civ release. It gives only the branches the town saw, and no sealed fact.
- The seven god releases. Each names only its own god. Each gives the Keeper's rulings as outcomes. A surfaced knack is given only as "a small thing of your own", and no unsurfaced one is named. Distances agree with the travel tool (37.5 miles and 3 days on the track; 4 days down the river by boat and 10 back). Every place named is seen or named in that god's map knowledge (the River Farrow [f10] is seen and named for god-beasts). The dim nights are at the true count in each. Nothing names the factor, a standing or a ceiling.
- The seven sealed civ releases. Each agrees with `year.md` and that people's report. The western party's return early in Year 2 lies inside the failure branch of r-0250 as the Keeper set it, and is noted, not flagged.
- Dashes: none in either campaign folder. Leaks: none, with the allow line.

### Counts, round 2
Raised 3 new (9 in all). Resolved 6. Open 3.

## Round 3: the recheck after step 7

Run by the continuity checker, 2026-11-24, from 16:55 to 16:56 Pacific, at head f628b03. It covers the Keeper's round 2 fixes (bd2a43e, f993790) and the DM's step 7 files (80e217a, f628b03), plus the painting the paint job returned (2e07da5). Read in full: the diffs, the Year 1 closing, the Year 2 morning story, the painting request and the painting, the chronicle files (README, years, canon, threads, messages, and the god's and people's working files), the new card entry, the new appearance card and `player/pending.md`. Checked against the DM release, `year.md`, the ledger, the power card, the player's record and the engine rules.

### Scripts at f628b03

```
tools/check.py sim-06 1
clock not advanced to year 2
campaigns/sim-06/state/rolls.jsonl: rolls in the public log; rolls are sealed
2 finding(s)

tools/lockcheck.py sim-06 --all
places 0, leaks 0, releases 0, mysteries 0, rolls 1, dashes 0
```

The clock is step 8's. The public roll log stands as ruled in round 1.

### The three round 2 flags: all resolved
7. The keeper log names the stamp tool's change to this file and says the Keeper runs it no more tonight. The tool change is left for Michael. Resolved.
8. `P/releases/001/dm.md` now gives the dim nights as the town told them in the god's hearing (the line at the gate in month 1; the watch and the boatmen for the winter one), says that whether the god saw them itself is not set, and tells the DM to ask. The count still stands under the allow line. Resolved.
9. god-beasts's release gives the cough's month 9 return as the Longwalk report it, and `year.md` matches. Resolved.

### "It needs no sleep" in the morning's (oog)
Confirmed. The player's card, world rules, transcripts and conduct profile say nothing about sleep (searched). The public engine says it for every god: `engine/rules/time-and-pace.md` 149 ("What a god does not have is a need for food or sleep. Sleep is a choice."), from DESIGN 10.2. The sentence states a need, not a habit. The same (oog) says the record has the Weigher only sitting late at the landing, and asks the player how it keeps its nights. It matches the release, `pending.md` and the chronicle, which all tell the nights as heard and not as seen.

### Checked and holding, round 3
- The morning story. It is made only from the DM release and holds no more than it does. The return sequence gives the year, the season, the people's state and mood, the god's place and body, and no weight in the air. The meeting at dusk, the year's asks and the events agree with the release item by item. The dim nights are at their true count, as heard. The tide gathering is told as the yard said it, with no number. The story stops at the laid stick with the board, and has no "what do you do". The (oog) has four parts: the handling of the year, the L-0031 ruling in plain words, the map names (which match `player/map-knowledge.json`), and the nights question. There is no list of loose threads, no pointing at signs, no correction of a belief, no flattery, no count of gods, no other god, no sealed term, and no trace of the sealed factor.
- The closing. It has five sentences, inside morning-story.md's two to five. It states no outcome, sums up nothing, hints at nothing, and is built from the god's own things (the brass, the pockets, the empty pocket).
- The painting request and the painting. The scene is the gate and yard as seen on the landing day (the rolling save; the new appearance card), with the line of the four kinds of townsfolk as the people's record describes them, the watch, the landing and the reeds. The figure is seen from behind with no face. The house style is copied in. The painting is within Michael's approved count (`S/rulings.md`, the Year 2 morning). It shows nothing the god does not know. One note, not a flag: a short paling shows at the right edge, where the card says no fence. It reveals nothing, and the painting is final.
- The card entry. It matches L-0031 word for word, dated, with the ledger id. No other term of the card changed.
- The chronicle. Only what the god knows. The sky is told as heard. The canon carries L-0031 and L-0025 and the code as seen or told. The threads are the god's open matters, and none is a sealed thread. Messages: none.
- `pending.md`. It holds the held encounter, the five asks from the meeting and the fourteen from the year, matching the release. One note, not a flag: it also lists the DM's own (oog) question about the nights, which no one in the world asked (DESIGN 12.9). It is harmless as a reminder, but it belongs in the conduct or rolling-save notes, not in pending.
- Dashes: none. Leaks: none, with the round 2 allow line.

### Counts, round 3
Raised 0 new (9 in all). Resolved 9. Open 0.
