> SPOILER WARNING. Sealed. Year 2 continuity flags for campaign sim-06. Players must never read this file.

# Continuity flags: sim-06, Year 2

Status now: raised 10, resolved 0, open 10.

## Round 1

Run by the continuity checker (night turn step 5), 2026-11-24, begun after the hand-off at 22:46 and written at 22:57 Pacific, against commit 63edf18 ("pass two, the year record, rulings, state and the releases"). Pulled first; already up to date. Every check below was made against the files, not against the keeper log's word.

Read in full: `CLAUDE.md`, `engine/roles/checker.md`, `engine/night/night-turn.md`, `engine/rules/failures-checklist.md`, `S/keeper/sealed-factors.md`, `S/rulings.md`, `S/years/001/flags.md`, `S/years/002/year.md`, `world-events.md`, `hall-notes.md`, `held-coaster.md`, the keeper log from "Year 2 night turn", `S/state/luck.md`, the standing diff, the sealed roll log r-0257 to r-0299, `S/messages/m-0001.md` and `S/state/messages.jsonl`, the ledger L-0037 to L-0042, the four new card entries, the eight growth diffs, `P/player/decisions-002.md`, `P/releases/002/dm.md`, `P/releases/002/civ-unnamed-people.md`, the sealed notes `civ-unnamed-people-hall.md` and `civ-unnamed-people-hall-after.md`, the seven `decisions-002.md`, the seven god releases, the seven sealed civ pass-two releases (four in full, three by search), the Longwalk pass-one release, the five sealed player files, mystery S01 and the last Weightward's section of the deep history, mystery S04 and S06 (branches), the S04 and PH rows and the month rule of the event schedule, and the diff of 63edf18 to the player's public files. Read by search and in part, where a check needed them: `engine/rules/encounters.md` 5 and 6, `engine/rules/map.md` and the grade rules in `tools/map.py`, the eight peoples' Year 2 files and reports, the other pass-one releases, every NPC god's `map-knowledge.json` for the places reached this year, the cards of god-sea and god-beasts and the player's The True Measure, the eight hidden powers files, the gods' records of gods, the conduct profile, `P/player/unsaid.md`, `requests-answered.md`, the Year 2 transcript, and the run's change list items 81 to 89.

Result: 10 flags, none of them a reworked outcome: no roll is redone and no branch changes. Three are moderate (record or state that the Keeper must rework, and which a later year would build on); seven are minor (a rewording or a line). Severity here: major means the year is reworked; moderate means the record or state is reworked with no outcome changed; minor means a rewording or a log line.

## Script output

```
tools/check.py sim-06 2
clock not advanced to year 3
missing: the morning story (campaigns/sim-06/years/003/morning-story.md)
no painting request for the morning story
campaigns/sim-06/state/rolls.jsonl: rolls in the public log; rolls are sealed
4 finding(s)

tools/lockcheck.py sim-06 --leaks --dashes
leaks: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/lockcheck.py sim-06 --all
FAIL rolls: campaigns/sim-06/state/rolls.jsonl: the public rolls log is not empty; rolls are sealed
places 0 failures, 24 warnings; leaks 0; releases 0; mysteries 0; rolls 1; dashes 0
```

Judged: the clock, the morning story and the painting request are steps 7 and 8 (night-turn.md), not written yet; expected at this step, not flags. The public roll log stands as ruled in the Year 1 flags ("Rulings for review", the public roll log), and that ruling is carried: the DM's lines DM r-0006 to DM r-0010 stand unedited and the two script findings are not flags against Year 2. The 24 place warnings are map names without ids in the civ agents' own sealed files (the Longwalk, the Sarrow, god-rivers's and god-sea's peoples); the Keeper chose not to run the stamp tool this year so that it would not touch the checker's files again (Year 1 flag 7), and logged it. Noted, not flagged; the tool's skip list is Michael's.

`tools/phenomena.py` rerun: Year 2 dim nights 5, tide gathering 2, crane gathering 1; Year 1 3, 2, 1. They match the record.

## Flags

### 1. The dim nights told at the wrong months to the three spring countries (moderate)
- Check: failures checklist 2 (contradiction); DESIGN 12.8 (a phenomenon at its true time and count); `S/event-schedule.md` line 7, the month rule.
- Where: the dim nights were rolled by the clock's count [r-0269 to r-0272, r-0274: "the month by the clock's count"], months 2, 6, 9, 11 and 12, where the clock opens in autumn. Every release then gave the same numbers as months "of your year", including to the three countries whose year opens in spring: `S/releases/002/civ-longwalk-pass1.md` line 18, `civ-unnamed-people-rivers-pass1.md` line 17, `civ-unnamed-people-healing-pass1.md` line 18, `god-beasts.md` line 26, `god-rivers.md` line 28, `god-healing.md` line 25. The three peoples' agents built on it: `S/civs/longwalk/years/002.md` (lines 15, 57, 61: "In the twelfth month, at the end of winter, the star dimmed"), `S/civs/unnamed-people-rivers/years/002.md` (lines 26, 45, 67, 76), `S/civs/unnamed-people-healing/years/002.md` (lines 13, 31, 47: the third tied to the Reckoner's autumn count). `S/years/002/year.md` says "months 2, 6, 9, 11 and 12 of every people's year".
- Record says instead: the schedule counts a month from the waking season of the country it names; the spring countries run spring, summer, autumn, winter. One night in the sky is one night everywhere, so in those three countries the five nights fall six months away from the numbers given (clock month 2, late autumn, is not their second month, which is spring). As written, the sky dims in autumn for one people and in spring for its neighbor on the same night.
- The same fault stands in Year 1, uncaught then: `S/releases/001/god-rivers.md` line 26, `god-healing.md` line 27, `god-beasts.md` line 30 ("two in the first month ... one in the fifth" of a spring year), from r-0244 to r-0246 by the clock's count.
- Effect: no roll and no outcome turns on a dim night's month. The peoples' sayings and some lore tie to the months (healing's court ties one to the hearth sitting; the Longwalk count to the going up).
- Fix: the Keeper rules how a spring country's year lines up with the clock (which clock months fall in its Year 2, and whether any of the five fall in its Year 1 or Year 3), logs it, corrects the six Year 2 releases and the three Year 1 god releases to the true months in each country's own count, corrects `year.md`, and reworks the dim-night lines in the three peoples' Year 2 files (and their lore where it ties to a month). No count changes.

### 2. The sealed factor's name in two peoples' files (minor)
- Check: sealed-factors.md, the checker's check 4; Year 1 flags 1 and 2 (same kind).
- Where: `S/civs/unnamed-people-sea/lore.md` line 42, "The yard says the keel is lucky." (written this year, 4e50afa). `S/civs/unnamed-people-secrets/years/002.md` line 80, `years/002-report.md` line 76 and `people/steersman-of-the-first-boat.md` line 11: the boat families' words "Ivo Strand's water, Ivo Strand's luck" (written this year, c2d97eb).
- Record says instead: no word of the factor stands in any file a civ agent reads. The allowance for an ordinary word covers an NPC god's own files from its own answers only, not a civ file. The keeper log's neutrality self-check does not name these.
- Fix: the Keeper rewords each (for example "the keel is blessed"; "Ivo Strand's water, Ivo Strand's fortune" or another word of the boat families'), no meaning changed, and logs it.

### 3. The NPC gods' map knowledge not raised for ground they entered (moderate)
- Check: failures checklist 11 (map ground lost); night-turn.md 4 ("every NPC god's map knowledge"); `engine/rules/map.md` 2.1 and 2.2 (entering a region raises it to seen; walking a river reveals the river; point features within sight).
- Where: the keeper log, pass two, "State written": "No NPC god's map knowledge changed: none saw new ground beyond its own country but god-secrets, whose river was already seen". The files say otherwise:
  - god-rivers: went down Wellen Brook [f12] by barge, six days at Wellen Ford [f47], stood in the River Wellen [f08], came home by the Brook Path [f46] (its release). In `S/gods/god-rivers/map-knowledge.json` f12 and f46 are `reported` ("own sight at landing"), f47 and f08 are absent.
  - god-secrets: down the River Iss [f11] to its mouth and a fortnight there (its release). f11 is `reported`; r06 is `reported`.
  - god-sea: swam the Garrow Skerries [f31] and the floor of the nearer bay (its release). f31 is `reported`; r30 is `reported`.
  - god-thresholds: walked the Pass Road [f65] "house by house ... to its far end, eight days out" (its release; keeper log "up to 148.1 miles"). The road runs through r02 (`reported`) and its far end lies inside the Aldermark [r10] (no grade). If she reached the far end she entered the Aldermark. The Kennoch Gates [f64] (no grade) is where she saw the flower missing in month 10, if that was at the gates.
- Fix: the Keeper raises each by `tools/map.py reveal` with the god's own source, and settles where the two farthest toll houses stand: if short of the Aldermark, the release's "to its far end" is corrected to the houses; if at the end, r10 is entered and seen, and the keeper log line is corrected. A god now holding seen ground beyond its own country is the Keeper's to note for Year 3.

### 4. god-sea's Sound Timber counted three times (minor)
- Check: checker.md 3 (growth and use logged against the year's events); failures checklist 2.
- Where: `S/years/002/year.md`, god-sea: "Sound Timber three times in the year, ... a quay step-board, month 2; the keel of the stand-by boat, month 11; the first keel, joined in Year 1, hauled clean after a year." `S/gods-sealed/god-sea/growth.md`, Year 2 note: "Sound Timber three times".
- Record says instead: two pieces were joined this year (its release: "You joined a step-board ... in the second month, the keel of the stand-by boat in the eleventh, and each cost you the hand for a day"; its people's files). The third item is last year's keel, hauled and found sound; no power was used on it. L-0042 rules on three as asked and stands.
- Fix: correct both lines to two uses and the Year 1 keel found sound.

### 5. god-sea's harbor-bed swim against the stilled water's season (minor)
- Check: checker.md 3 (no power used beyond its card); god-sea's card, Calm Under the Lamp, Drawback ("The water it stilled will not take the god for a season after. It cannot swim there").
- Where: the lamp stilled the mouth and the inner water in month 5 (release; L-0033). The keeper log has the stilled water taking it again "from the eighth month". The spring swim covered "the harbor bed, the skerries and the floor of the nearer bay" (release, `year.md`), and the keeper log has it searching the harbor bed "through a spring". Spring is months 7 to 9.
- Record says instead: the harbor bed inside the mouth is the stilled water and is closed to it through month 7. Nothing in the record puts the inner-harbor part of the swim in months 8 and 9. What lies there is unchanged and was not rolled.
- Fix: correct the record (`year.md`, the keeper log line, `S/releases/002/god-sea.md`) so the inner harbor is swum from the eighth month, the skerries and the nearer bay outside the bar at any time in spring.

### 6. god-beasts's Listening gives a count of the cutters it cannot give beyond a mile (moderate)
- Check: checker.md 3 (no power beyond its card); checker.md 4 (no release holds more than its agent could know); god-beasts's card, The Listening.
- Where: `S/releases/002/god-beasts.md` line 13: "What the Listening gave you of the cutters ...: about eighty, in three camps, with draught oxen". The same in `S/releases/002/civ-longwalk.md` line 10, `year.md`, and `S/civs/longwalk/years/002.md` line 45. The keeper log: "The cutters' count set by the Keeper from the holds' record".
- Record says instead: the card gives "where, how large, which way they move" within about a mile; beyond the first mile, in timber up to about three, "only gatherings ..., where, which way they move and their state, and not a single beast or person", with no size, and it "does not tell two persons of a size apart". The god's decision 5 says it does not approach the cutters. Nothing in the record puts it within a mile of each camp. The count of eighty is the holds' truth, not what the power read.
- Fix: either the record puts the god within a mile of each camp in the nights of months 7 and 8 (and the Keeper rules that this is not "approaching" under its decision), and says so, or the release, the civ release and `year.md` give what the Listening gives past a mile: three gatherings of people with draught beasts, where, which way, their state. The Longwalk's file then follows the civ release in Year 3.

### 7. At the pits the god says what the player gave the potters to say (minor)
- Check: failures checklist 6 (acting for the player); encounters.md 5 (the narrowest reading of what the player decided).
- Where: `P/releases/002/dm.md` line 75: "It said, in its own words, that the two sets do not look different, that it had told them nothing about the cracking". `S/years/002/year.md`: "The god said, in its decided words, that the sets do not look different". `P/civs/unnamed-people/years/002.md` line 81: "It said so: the two sets do not look different to it".
- Record says instead: decision 11, the player's words: "I'll tell you what I read of each, and you tell me if the two sets look different. If they don't, I've told you nothing, and I'll say so." The judgment of the two sets is the potters' and kiln-masters'; the god's line is that it has told them nothing.
- Fix: correct the three lines so a potter or kiln-master says the sets do not differ and the god says it has told them nothing, in its decided words. Nothing else changes.

### 8. The card text for L-0037 in the DM release is not the ruling (minor)
- Check: checker.md 3 (no ruling contradicting the ledger); Year 1 round 3 (the card entry matches the ledger word for word).
- Where: `P/releases/002/dm.md` line 167, the text given "For the card".
- Record says instead: L-0037's ruling also holds "The water a worked clay holds is part of the clay as it is" (on which the pit readings rest: clay 91 of 96 counts its water as clay), names the stuffs ("salt, grain, charcoal, ore"), and ends "how much is the stuff and how much is not, never how good the stuff is". The release text drops all three.
- Fix: give the ledger's ruling whole as the card text, so the DM copies it at step 7.

### 9. "the Aldermark" begun in lower case in two public lines (minor)
- Check: checker.md (a scan hit in a public file is fixed by rewording the file); the writing rules.
- Where: `P/civs/unnamed-people/lore.md` line 109, "- the Aldermark traders went home ..."; `P/civs/unnamed-people/years/002-report.md` line 134, "- the Aldermark: boats came down ...". Both were "The Aldermark" and were lowered by the Keeper to pass the scan.
- Record says instead: the god knows the name as "Aldermark" (`player/map-knowledge.json` r10); the fix by rewording is right, but a lower-case sentence start is not a rewording.
- Fix: reword, for example "Traders from the Aldermark went home ..." and "Boats from the Aldermark came down ...", and rerun the scan.

### 10. god-sea's people told that the god heard the Warden-Monarch (minor)
- Check: checker.md 4 (no release contains more than its agent could know).
- Where: `S/releases/002/civ-unnamed-people-sea.md` line 10: "The keeping heard what the Warden-Monarch told the water in month 3." The release opens "Your people know these as people know things: by what they saw and were told."
- Record says instead: the god heard it (keeper log, ruled), but no one of its people saw or was told that it did; no answer came to her telling (the same line).
- Fix: drop the clause or give only what the people know (she told the water; no stick answered).

## Checked and holding

- Cause and fixity. Every event in `year.md` and `world-events.md` traces to a schedule row, a roll, a record fact or a decision. The new fixed facts of pass one and pass two are each logged with the act that reached them: the hill weigher (the hill-goods head's split stick of Year 1), the pits on the Reedmouths [r14], the six weights and their figures, the drift of a twentieth, the nest's scatter, the two keys, the third motion, the ship owner's bargain, the coaster's master and what she carries (`held-coaster.md`, each item already in the record: r-0284, m-0001, the league's record of Corran and Sennet). The nest figures check: each of 1, 2, 3, 4, 6, 7, 8, 10, 12, 14, 15 hall pieces at twelve and a half, moved by the note's amounts and rounded, gives 13, 25, 37, 52, 75, 89, 98, 130, 150, 179, 181; the report's beam readings agree with each move. The six weights double from 48, the fifth light by two in 768. The clay readings lie inside the Keeper's line (about a twentieth, 4 to 6 parts in a hundred).
- The clerk's dating: `civ-unnamed-people-hall-after.md` puts the visit in the summer before the old man's last winter, which agrees with the deep history's order (the visit, the winter, the spring flood, the death in the spring before the arrival). The hall note's "last summer, before the stranger came" was the fault, and the civ agent wrote nothing from it.
- Rolls. r-0257 to r-0299: every contested outcome has a logged roll; none rolled twice (r-0273 is the tool's void draw, replaced by r-0274). Every odds line adds up from its factors and lies inside 5 to 95. The weighted draw r-0284 has three targets and the one god among them (the Sarrow's) is at 0.
- The sealed factor. Checks 1 to 5 of sealed-factors.md: named in `--what` at its step with stated and rolled odds on r-0285 to r-0290 (the player +1), r-0291 and r-0292 (god-beasts +1), r-0297 to r-0299 (god-secrets +1); every roll for a god at 0 says so (r-0293 to r-0296); no roll for god-healing; no contest between gods; no weighting moved (r-0284: the target god at 0; the country rolls, the kinds, the d8 examples and the months are no act and no choice among targets). None of the ten turned on the factor. `luck.md` unchanged in value with its dated Year 2 line, matching the keeper log. No DM roll qualifies for an overrule (DM r-0006, r-0009, r-0010 succeeded; r-0007 and r-0008 are draws); none overruled; no DM line touched. Words: flag 2; the uses in god-sea's and god-rivers's own `self.md` stand as allowed at the lock, in those files only; the engine's "unlucky" stands as recorded at the lock.
- Powers. L-0037 (purity of clay) narrows to the card's own "what a thing is now". L-0038 (the weighing) resolves on the handed-off terms and stops at the three named stops; the weighing's text keeps to decisions 1 to 3, 5 and 11 at every step but flag 7. L-0039 to L-0042 are undisputed readings within the cards, each entered on its card dated with its ledger id. Mending, Warm hands, Listening water, the Latch, Keeping Sleep (two a night, three on three named nights, the Night Sitter's household kept on a household's own asking within the cap) as the cards give. Hidden powers and knacks: none surfaced, and no "Surfaces when" moment is on the record for any god (checked against all eight files: no house entered at night with someone failing, no table with a place kept for the newly dead, no butchering, no stranger's tally, no old bargain disputed, no food that does not feed). No NPC god's folder holds an unsurfaced hidden power or knack (searched by every sealed name; the five in the cards surfaced in Year 1). Growth: nothing earned; the use lines stand against the year's events but flag 4.
- Knowledge. The DM release holds only what the Weigher saw, heard or was told: the loft told as three going up and coming down quiet, the boatmen as seen and not heard [r-0290], the Tally-keeper's half, the Assay-master's private word and the coaster's name, house and news all left out. Names: the Alder (the Stallreeve, month 5), Ruddfold (the weigher, in the ring), Corrith (a boatman, month 10, wrong and recorded as a rumor at C4, which is where Corrith lies) and the Maun Stair are each in `player/map-knowledge.json` in the same commit as the release that first uses them; `civs/unnamed-people/knowledge.md` carries place names only. No god met another; each god release names only its own god and ends "you felt no other like yourself". The gods' records of gods hold nothing they did not meet. The sealed notes to the player's people's agent worked: no public file holds the clerk, the loft's contents or the punt.
- Map and travel, by `tools/map.py travel` (run for each): the bend town [f50] to the Ellow's mouth by boat, 112.4 miles, 4 days; the mouth to Port Sennet [f75] on foot, 97.9 miles, 7 days; the spring town [f45] to Wellen Ford [f47], 25.1 miles, 1 day by boat, 2 on foot by the Brook Path [f46]; Marle Ford [f61] to Far Notch [f63] 1.9 miles; the winter city [f60] to Far Notch 2.4 miles; the walled town [f35] to the Iss mouth, 31.9 miles, 2 days down; the court steading [f55] to the Morrow Mounds [f56], 2.9 miles; the winter city along the Pass Road [f65] to its far end 148.1 miles, 8 days on foot (to its other end 72.1). All agree with the record. m-0001's dates fit the travel and r-0294's failure branch (home in spring, month 8).
- Messages. m-0001 has its journey logged to the recipient (House Corran's factor at Port Sennet, played by the Keeper from the league's record), its fate in `messages.jsonl` and the file; the answer is mystery S06's "treats with the House" branch ("it wants stone"), and the salt bought at another house's pans is its "another way" branch. Nothing claimed delivered that was not.
- Neutrality. The keeper log's self-check names every use of the factor and each temptation. The two cases the Keeper pointed at: the seat's terms answer the player's open words of decision 4, which that agent read, and apply no sealed want (every Confirmations line reads none); the old set's doubling is the Keeper's plain choice for a standard set, and nothing in the sealed past (`backstory-secret.md`: the even stone, the pocket, the door scales) gives a doubling or a seven, so it is not drawn from the sealed past. The seventh weight's absence is mystery S01 as locked, not new. No `requests-answered.md` line added. No correction of a belief; no clue held back (the rack, the harbor bed, the moss, the wells and the far bins are shown as they stand); the overheard boatman was rolled and failed. Recurring things at the tool's counts in every file (flag 1 is their months, not their counts).
- The player. Decisions file present; the year turned. Four held moments, each stopped at contact with its board: the Assay-master's "What are you?" (a promise given, L-0038), the ship owner's bargain (binds the god), the seat (decision 4 keeps the answer for the table), the coaster's master (a world-level figure). The release marks what is provisional on the first and third, as encounters.md 6 asks. The witnessing in month 6 acts on decision 15, the player's own words at the table, with no power used, as the DM's marker and the sealed fear require. Nothing done for the player beyond its decisions and conduct but flag 7.
- Mystery standard. No clue states a mechanism; no mortal fully right about a cause (the Longwalk's "the cough was the stone towns'" comes with three ways it might have come, one of them right; the town's guesses at the empty seat; the hill kin's "supposed heavy"); no decisive clue by a visitor (the coaster is held before she speaks); nothing marked by tone (the rack's lines and the loft's are at the weight of the day around them).
- Counts. No public file states a count of gods in any wording (scan clean; the changed public files and `dm.md` read for meaning). The dim-nights counts in `dm.md` stand under the Year 1 allow line, and are counts the god saw.
- Helpers. None forced back; nothing the player left unnamed named by the Keeper (the town and its offices stay unnamed; the hill village, the river and Corrith were named by mortals).
- Dashes: none in either campaign folder.

## Noted, not flagged

- The Year 1 dim nights released as seen (pass one, listed for review). Decision 16 is the player's own present-tense account of how the god keeps its nights, given in answer to the DM's (oog) question about them; the Keeper read it as covering Year 1. The morning story and the chronicle told them as heard; the DM's step 7 should say in (oog) that they are now told as seen because of the player's answer, and log it in `player/corrections.md` if the chronicle changes.
- Two `player/map-knowledge.json` entries changed source and year without a rise in grade (f03 "own sight at landing" to the Stallreeve, year 1 to 2; f25 the same way). map.md 2.1 overwrites them only when a grade rises; `map-log.md` keeps the history. This is how `tools/map.py reveal` writes a told name; for Michael.
- god-thresholds's decision 7 says she judges disputes at the nearest sill if the Doorwarden asks. The record leaves the grass dispute waiting because her decisions give no verdict. That is right: a verdict is hers to give, and none can be written for her.
- god-sea's people's agent dropped the Keeper's Year 1 pass-two note from `state.md`; the Keeper ruled it not restored by hand (change list item 87). The Year 1 note is in `S/years/001/year.md`.
- The timing file and the keeper log put step 0 done and the decide releases at 22:06, after step 1 done at 22:05; the commit of the releases is 7ea7e6f, at 22:03. A diagnostic only.
- Row S04-c read as met by the two clans' herds wintered at the downwind end of the camp on their own ground and browse, the coughing beasts penned apart (listed for review). It is a fair reading of "wintered apart". The schedule rows stand as written.
- The DM release's line on the sky ("That is what its watching has given it of the blue light's habits so far") is a summary for the DM, not text for the player; the morning story should not carry it as a pointer.

## Rulings for review

None new from the checker this round. The Keeper's own list for Year 2 (keeper log, three blocks) was read; each ruling is applied as logged, and none contradicts the ledger or the cards. The largest, L-0038 (a prepared main event resolved in the night), stands as change list item 81 for Michael.

## Counts, round 1

Raised 10 (moderate 3, minor 7, major 0). Resolved 0. Open 10.
