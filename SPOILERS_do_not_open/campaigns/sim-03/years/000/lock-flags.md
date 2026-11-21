> SPOILER WARNING. Sealed. Lock flags for campaign sim-03. Players must never read this file.

# Lock flags: sim-03, round 1

Run by the continuity checker, 2026-11-21, from 00:20 to 00:33 Pacific, against the Keeper's ready-for-lock commit c90dd960104aaba8b38c8b81915c8a30de8d9a3b as it stands at 901ee1da4e301b8b3e2cb3606daab605d7aa3f86 (the last commit touching the campaign: the keeper log line naming the ready-for-lock id, and the hand-off time in `P/state/timing.md`; nothing else in either campaign folder differs). Every line of the lock checklist (runbook section 4) was checked against the files, not against the keeper log. Distances, directions, days and ground were measured from `S/map.json` by the checker's own script: every land line in the seven NPC records, the four godless records and `S/civs/unnamed-people-sealed.md`, every distance in `P/world/world.md`, `P/releases/000/dm.md` and the world bible's table of wishes, and every god's starting view, which was rerun with `tools/map.py describe --landing` for all eight and compared with all eight knowledge files.

Result: 7 flags, on 6 of the 17 lines. Six are the Keeper's to fix. One (flag 7) no permitted path can clear, and it is Michael's. The lock does not pass. No public `lock.md` and no `LOCKED.md` are written.

## Script output

```
tools/lockcheck.py sim-03 --all
FAIL leaks: campaigns/sim-03/player/hierarchy.md:19: number word "two" near "god": "two hear nothing from the god"
FAIL leaks: campaigns/sim-03/player/hierarchy.md:31: number word "three" near "god": "three as knowing the god"
FAIL leaks: campaigns/sim-03/player/power-card.md:21: number word "three" near "god": "three days of the god"
FAIL leaks: campaigns/sim-03/player/power-card.md:21: number word "five" near "god": "god's work for an acre (five"
FAIL leaks: campaigns/sim-03/player/power-card.md:21: number word "five" near "god": "five worker-days by hand, at a god"
FAIL leaks: campaigns/sim-03/player/power-lean.md:13: number word "Two" near "god": "Two things about this god"
FAIL leaks: campaigns/sim-03/player/power-lean.md:23: number word "Three" near "god": "Three days of the god"
FAIL leaks: campaigns/sim-03/player/transcript-day2.md:60: number word "five" near "god": "five worker-days by hand, at a god"
places: 0 failure(s), 0 warning(s)
leaks: 8 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-03
0 problem(s)
```

## The checklist, line by line

1. Seven NPC gods, files, cards, sealed folders. Yes. Seven folders labeled by domain, no number; seven distinct seeds and domains, the duplicate and theme rerolls carrying `--replaces` and reasons in the roll log. Each folder holds sheet, self, goals, record-of-gods, its negotiation files (Night 3 only for the four that proposed an edge), power card and map knowledge. Each card carries the frozen dated entry, `Hidden powers` saying only that two exist, and Ceiling `Set by the world. Not shown.` Each sealed folder holds a secret backstory, two hidden powers (one cool, one minor) with the ceiling line (74), and a growth file with a block for every card power and both hidden ones. No hidden power name, ceiling or common-past name is in any `S/gods/` folder or release.
2. The player's sealed files and public card. Yes. `S/player/` holds the backstory, two hidden powers with the ceiling line and a growth file with all six blocks. The public card names neither hidden power, its Ceiling line is as required, and every "settled at creation" mark carries a ledger id (L-0001 to L-0007, L-0029 to L-0031), each present in the ledger and matching its matter.
3. Shared links and likenesses. Yes. All seven rows of `common-past.md` stand word for word in both gods' backstories and are summarized in the keeper log (2.5). The eight backstories agree with the common past and with each other. No common-past name is used in the world. Likenesses of shape (world bible) fall at three different gods' countries and do not cluster. Note, not a flag: the common past says the far country lies "further than any people here has walked", and the deep history and C12 bring two lines of walkers from under [p01]; read as "a people", it holds, but the Keeper may want the wording to allow for single lines.
4. Eight peoples, edges, meetings, dates. Yes. Seven NPC records and states plus the player's (public record and state, sealed side). Every record has `## Helpers`, with offices; no refusal. Edges priced with one measurable line each (L-0032 to L-0037); none on size; god-beasts' upward departure from its small lean has its reason. Every NPC people is within its god's rule and worship leans as the override forced them. Every meeting and date agrees with `deep-history.md` (unnamed people 405 years; Thessen room 452 BA; Column circuit about 1,400 years; Lowlamp name about 260 years; Arroway seat 1,410 BA; Ussel about 700 BA; Weirfolk since 74 BA). Nothing the player left unnamed is named: town, burial ground, houses, people and the three designed mortals keep placeholders in every file.
5. Godless peoples. Yes. Four (Q4 at 4), each with record, history and state.
6. Places. Yes. `--places` passes with no warning, and `map.py validate` reports nothing. By reading, one location lacks an id; it is recorded under line 10 (flag 4), where it sits.
7. Distances, directions and sight lines against the map at the pace table's rates. Flags 1, 2 and 3. Every other measured line agrees within rounding to the nearest five miles, direction included, and every god's starting view matches its knowledge file and the sight rule.
8. Spacing, terrains, one sheet. Yes. Each god's nearest neighbor lies 371 to 463 miles off (the player's 412); the widest ring edge (717 miles) is no god's nearest and runs across the high range. Every Night 1 terrain is on the sheet; one continent, 5 by 4 grid; the world has a layer below, its sheet held unapproved and the layer traced as data, per `P/state/images.md`.
9. Star and plane rolls. Yes. `star.md` holds every item and the ceiling with roll ids; each face reads to its result by the lore's tables (ceiling 70 plus the lower of 10 and 4). The plane's four entries match r-0149 to r-0171 face by face by runbook section 8, with the count roll kept as `plane.count_roll`.
10. Mysteries. The script passes. By reading: one epic, four long, thirteen short by their `Kind:` lines; every clue has what is shown and at least two readings; every branch has the world's answer; every Never found is filled; six beings answer questions and each `Limit:` stands word for word in `cast.md`; the epic's four central measurements are each earned, none by a scheduled visitor; no mortal in the record is right about a cause. Flags 4 and 5.
11. Causes, costs, clocks, random weighting, phenomena. Yes. Every mystery's cost is a row (C01 to C13, T01 to T16) naming its mystery; every clocked number carries its roll or a stated reason; random events at base 30 less 20 in Years 1 to 7; four phenomena for twelve years in `phenomena.json`, matching the rolls; the weather years fall on five different peoples. (Flag 5 touches a cost, and is counted under line 10.)
12. God-sense never a tally. Yes. `P/player/world-rules.md`, the player's card, all seven NPC cards and releases and `P/releases/000/dm.md` give it as face to face, a weight or unease, never a count.
13. One rule for the whole world. Yes. Magic is three to five workers in five thousand everywhere; the bowl's losses and the Bare Reach are effects of the hoarder and of a working, not local rules.
14. Rolls. Yes. Script passes; r-0146 and r-0195 are the tool's void draws, each replaced with its id; every 3b number names its method in `--what` before the face, and each face reads to the value used.
15. The keeper log. Flag 6. Otherwise yes: placements before rolls with every answer, the eight Q8 voices with the one skip, every vote count (Q15 7 to 1 to 0, Q16 7 to 1), the Q6 clamp, pools and leftovers, every placement, and every decision the files did not make, each marked for Michael.
16. Leaks, by reading every file in `P/`. Flag 7. By reading, nothing in `P/` reveals a vote, a pool, another god, the count of gods, a sealed place id or coordinate, a star value, the deep history, a mystery, the schedule or a phenomenon's count. The transcripts' "every one of you" and "every god here" name no number.
17. Nothing contradicts the deep lore or explains what it keeps mysterious. Yes. The star results, the Remainder and its trigger, the hoarder (small, slow, fed by the thread), the carriers' two visits in the first and fourth decades, the thinners, the ceiling and the voices at four fifths of it, and the three earlier gods (rising, refusal, shedding) all agree with the lore; nothing explains what stays mysterious.

## Flags

### Flag 1. Line 7, sight at landing: the player's god stands on the worn way, and two public files put it a few hundred yards south
Rule: runbook line 7; checker rule 9; `engine/rules/map.md` 1.4.
Where: `P/releases/000/dm.md`, "What is in view" ("A worn way ... a few hundred yards to the south") and `P/world/world.md`, "In view" (the same words).
What the record holds instead: the player's landing point [274.0, 789.0] lies exactly on the Coppice Track [f36] (on its segment from [272.5, 787.5] to [275, 790]; distance 0). The Keeper's own `S/civs/unnamed-people-sealed.md` says "The god comes down in the forest on the worn track", and the keeper log (3a.7) says the landing was set on it. The words come from `tools/map.py describe --landing`, which prints any distance under 0.2 miles as "a few hundred yards" and gives a bearing of south to a zero distance. Both files are the Keeper's (3b.8 Writes). The fix is to say the god stands on the worn way, with about a mile of it in view running north-west to south-east, and to check by the same reading that no other god's view carries a zero-distance bearing (none of the other seven does today).

### Flag 2. Line 7, pace: days and miles given at a rate the ground crossed does not have
Rule: runbook line 7 ("at the pace table's rates"); the sim-02 lock precedent (its flag 3); `engine/rules/time-and-pace.md`.
Where, with the ground the straight line crosses, measured by sampling `S/map.json`:
- `S/civs/lowlamp/record.md` line 102, Stakewater [f28]: 395 miles, 28 days "over rough ground at 14". The line is 78 percent the Rattlereed [r12], marsh.
- `S/civs/weirfolk/record.md` line 114, Lampford [f25]: the same line reversed, the same figures.
- `S/civs/lowlamp/record.md` line 105, Seven Wells [f68]: 280 miles, 20 days "over rough ground". The line is 77 percent marsh, and Seven Wells lies on the Pale Road [f26], which the Lowlamp travel; by that road it is a road walk at 20 a day over the road's own length.
- `S/civs/marrans/record.md` line 78, Saltsteps [f40]: 270 miles, 19 days "on foot over rough ground". The line is 60 percent the Green Sea [r21]; on foot the way runs round the bay and is longer, or it goes by water, which the record does not say.
- `S/civs/marrans/record.md` line 89, the White Acres [f67]: 240 miles, 17 days "over rough ground". The line is 44 percent the Sump [r17], marsh, and the White Acres lie on the Strand Road [f33].
- `S/civs/thessen/record.md` line 103, the Hound Spring [f64]: 280 miles, 28 days "over forest at 10". The line is 54 percent the North Heath [r08].
- `S/civs/marrans/record.md` line 80 and `S/civs/weirfolk/record.md` line 111, Stakewater [f28] and Tallyford [f30] "by the Meadow Road [f32]": 490 miles is the straight line; the road as traced is about 530 miles, about 27 days at 20.
- `S/civs/marrans/record.md` line 77, Averley [f39], 220 miles "by road at 20": no traced road reaches Averley [f39] from Tallyford [f30]; the Meadow Road [f32] passes about 70 miles north of the city.
What is needed: one reading for all twelve records, as the run 02 principle on the lock rounds asks: a line priced by the ground it crosses (or by the road it follows, at that road's length), and every other land line rechecked against the same reading.

### Flag 3. Line 7, and runbook 3b.5: one kept wish's distance from its own god is misstated
Rule: runbook 3b.5 ("Confirm each undared wish that was kept is placed away from its own god's certain path, with the distance from its seat"); runbook line 7.
Where: `S/world-bible.md`, table of undared wishes, god-rivers' wish ("A gate that cannot be made a cage"), kept as the Rattlereed [r12]: "about 220 miles, 16 days".
What the map holds: 220 miles is the distance to Nightstake [f45]. The Rattlereed [r12] itself, the body named, begins about 70 miles from god-rivers' landing, upstream on the god's own river; it is a neighbor of its home region, and `S/civs/weirfolk/record.md` has the god's people with its lower edge seen. The confirmation that the wish lies off its god's certain path rests on the wrong number. The Keeper should measure to the body as kept and confirm or re-judge.

### Flag 4. Line 10, mysteries (and line 6): a clue location with no map id
Rule: runbook 3b.5 ("Every clue placed at a location (with its map id) or on a being"); mystery standard, writing down; runbook line 6.
Where: `S/mysteries.md`, S06, clue "Cut stone in the fall", `Location: the newer of the two sinkholes`.
What the record holds instead: a place with no id; the new sinkholes are not features in `S/map.json`, and the line carries no region id either. The script cannot catch a lower-case place. The location should carry the id of the ground it lies on (the Coppice Track [f36] near the unnamed town [f35], in the Holed Wood [r18], as the clue before it has).

### Flag 5. Line 10, the rules against the record: S05's cost contradicts the Column's agreed weakness
Rule: checker rule 3 ("No ruling contradicting the ledger"); L-0032; `S/civs/column/record.md`, Weakness: Few Holds.
Where: `S/mysteries.md`, S05, Cost if ignored: "the cellars flood to the knee and the hold's whole store spoils: a quarter of the Column's winter grain."
What the record holds instead: Few Holds, agreed and confirmed by the god, says "The loss of one hold (taken, flooded, burned or fouled) takes a third of the winter's grain and a third of its shelter", and only "If the ring grows past four holds" does the loss fall to a quarter. The Column has four holds on the map ([f21] to [f24]). S05 must follow the weakness (a third), or say why a flooded store is not the loss of a hold under the agreed text; C07 in the schedule should agree with whichever it is.

### Flag 6. Line 15, the keeper log: two statements the files contradict
Rule: lock section 4 (the checker verifies against the files); DESIGN 12.2a (the keeper log is the index of a campaign).
Where and what:
- Night 3a, 3a.7: "The player's file holds its landing region `seen` and one `reported` entry, smoke to the north-east". `P/player/map-knowledge.json` holds two reported entries, the worn way [f36] and the smoke [f35], and the smoke is to the south-east, as the map and both public files say.
- Night 3b close, neutrality: "the league's weight lies thirteen miles from that god's seat". By the map the Old Weighhouse [f34] is about 16 miles from god-trade's landing and about 18 from Tallyford [f30] (the Marrans' record says about 20).
Nothing is deleted: a correction line in the log, with the date and the proof, is enough.

### Flag 7. Line 16, leaks: eight script hits that are not leaks, and no permitted path to clear them (for Michael)
Rule: lock line 16 ("`tools/lockcheck.py --leaks` passes"); `tests/tools/README.md` ("Lock only when every check shows 0 failures").
Ruling on each, by reading every hit in its sentence: none states, implies or lets anyone work out a count of gods.
- `player/hierarchy.md` 19, "The other two hear nothing from the god", and 31, "No agent writes any of the three as knowing the god": counts of the player's own three designed helpers.
- `player/power-card.md` 21, "About three days of the god's work for an acre (five worker-days by hand, at a god's work rate)": three hits, all one work rate, settled at creation (L-0001).
- `player/power-lean.md` 13, "Two things about this god are visible to anyone": two visible traits, listed in the same sentence. Line 23, "Three days of the god's work to tend an acre": the same work rate.
- `player/transcript-day2.md` 60, "five worker-days by hand, at a god's rate": the verbatim table text of the same rate.
Paths tried, and why none clears them:
- `S/leak-allow.txt`: the tool exempts a number-word hit by its quoted phrase from this file, and `tests/tools/README.md` says a hit goes in it "only after the checker has read the public line and agreed it reveals nothing". But no role file, runbook Writes list or lock section names who writes the file, and `engine/roles/checker.md` lets the checker write nothing but flags and the lock files. Under CLAUDE.md an agent in a run takes its role file as the go for exactly the files it names, so the checker has not written it. The Keeper declined it on the same ground (keeper log, 3b.9).
- Rewording through `P/player/corrections.md`: possible for `hierarchy.md` and `power-lean.md`, which are DM working files, but not for `power-card.md` line 21 (frozen card text, agreed with the player) or `transcript-day2.md` line 60 (a verbatim record). Four of the eight hits stay whatever the DM rewords.
So line 16 cannot read yes under the files as they stand, and the lock cannot pass while it does not. This is not the Keeper's to fix. Michael's choices include: naming the checker (after its ruling) as the writer of `S/leak-allow.txt` in `engine/roles/checker.md` and runbook section 4; or a tool change for work rates and counts of named things; or another rule. The checker's ruling above stands for whichever he picks: the eight phrases reveal nothing.

## For the rerun

Flags 1 to 6 are the Keeper's. Every file they touch is the Keeper's own (`P/releases/000/dm.md` and `P/world/world.md` are 3b.8 writes); no line needs `P/player/corrections.md`. Flag 7 waits on Michael. On the rerun the checker reads the flagged lines and every line a fix touches, reruns the scripts and its distance and ground script over all twelve records, and rechecks line 16.

# Lock flags: sim-03, round 2

Run by the continuity checker, 2026-11-21, from 00:58 to 01:06 Pacific, against the Keeper's rework commit d6d29c5e5e1da3689ed2448e08cea449347b010e. The flagged lines, and every line the rework touched (14 files, 70 lines added), were read against the files; the scripts and the checker's distance and ground script were rerun over all twelve records, the world bible's table of wishes and both public landing files.

Result: 1 flag open (flag 7). Flags 1 to 6 are resolved. The lock does not pass. No public `lock.md` and no `LOCKED.md` are written.

## Script output

```
tools/lockcheck.py sim-03 --all
(the same eight FAIL lines as in round 1, all leaks, unchanged)
places: 0 failure(s), 0 warning(s)
leaks: 8 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-03
0 problem(s)
```

## Round 1 flags, rechecked

- Flag 1, resolved. `P/releases/000/dm.md` and `P/world/world.md` now put the player's god on the worn way, with about a mile of it in view north-west to south-east, matching the map (distance 0) and the sealed side. The keeper log's claim that no other landing lies within a fifth of a mile of a feature agrees with the round 1 view check of all eight.
- Flag 2, resolved. One reading for every record: a traced road where both ends lie on it, at the road's traced length (checked: Seven Wells [f68] about 297 miles along the Pale Road [f26]; Sedgeby [f65] about 240 and Stakewater [f28] about 530 along the Meadow Road [f32]; the White Acres [f67] about 248 along the Strand Road [f33]); otherwise days by the ground crossed at the pace table's rates, water at the table's coastal sailing rate of 50. Recomputed sums agree (Stakewater [f28] from Lampford [f25] 310 miles at 6 plus 85 at 14, 58 days; Saltsteps [f40] 165 at 50 plus 105 at 14, 11 days). Every straight-line distance and direction still agrees with the map. The reading is a decision the files did not make, marked for Michael in the keeper log.
- Flag 3, resolved. The table gives both distances (about 220 miles to the braided heart at Nightstake [f45], about 70 to the near edge) and the re-judgment with its reason. The judgment is the Keeper's to make and is now made on true numbers.
- Flag 4, resolved. S06's location carries [f36], [f35] and [r18].
- Flag 5, resolved. S05 and C07 now give a third of the grain and a third of the shelter, citing L-0032.
- Flag 6, resolved. Correction lines for 3a.7 and the Night 3b neutrality distance stand in the keeper log, with the proof; nothing deleted.

## Flag 7, still open: the leak scan's eight lines

The checker's ruling of round 1 stands: none of the eight is a leak.

The coordinator relayed, at the start of this round, that Michael has ruled for this run only that the checker writes `S/leak-allow.txt` with the eight phrases and a reason each. The checker has not written it. `CLAUDE.md` gives an agent in a run the go only for the files its role file names, and anything else needs Michael's explicit go; `engine/roles/checker.md` does not name the allow file, and a ruling relayed by another agent is not Michael's own go. No record of the ruling from Michael is in the repository (no commit, no ruling line, no change to the role file or the runbook). When the ruling reaches this session from Michael himself, or stands in the repository in his hand (for example a line in `engine/roles/checker.md` or in runbook section 4, or the allow file committed by him), the checker writes or accepts the file, reruns `--leaks`, and the lock can pass on the next round: every other line is yes.

The eight phrases and the reason each would carry, ready for that file:
- "two hear nothing from the god": the player's two other designed helpers, not gods.
- "three as knowing the god": the player's three designed helpers, not gods.
- "three days of the god": a work rate, three days to tend an acre (L-0001).
- "god's work for an acre (five": the same work rate.
- "five worker-days by hand, at a god": the same work rate, in the card and the Day 2 transcript.
- "Two things about this god": two visible traits of one god, listed in the same sentence.
- "Three days of the god": the same work rate, in the DM's note to the Keeper.

# Lock flags: sim-03, round 3

Run by the continuity checker, 2026-11-21, 01:06 Pacific, against commit 236f5da. The only change since round 2 is two lines added to `S/state/test-overrides.md`. The scripts were rerun: places, mysteries, rolls and dashes 0; leaks 8, unchanged.

Result: 1 flag open (flag 7). The lock does not pass. No public `lock.md` and no `LOCKED.md` are written.

Flag 7. The new paragraph in `S/state/test-overrides.md` records a run-only go for the allow file. Its own words say it was "Recorded here by the orchestrator", and its commit (236f5da) was made by the orchestrator's session, not by Michael. It is the same relayed ruling as in round 2, written into a file rather than a message: the record of an agent, not Michael's own go. The checker therefore still has not written `S/leak-allow.txt`. The file is also the place for forced lean results (DESIGN 3.8, runbook standing rules), which Michael creates before Night 1; a ruling entered there by an agent mid-run sits outside that purpose.

What clears it: Michael's go given to this session directly, or a commit in Michael's own hand (the allow file itself, or a line in `engine/roles/checker.md` or runbook section 4). The eight phrases and their reasons are in round 2 above, ready. Every other line of the checklist is yes.
