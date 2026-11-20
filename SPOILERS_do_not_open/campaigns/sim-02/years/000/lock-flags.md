> SPOILER WARNING. Sealed. Lock flags for campaign sim-02. Players must never read this file.

# Lock flags: sim-02, round 1

Run by the continuity checker, 2026-11-20 09:43 Pacific, against commit ed55fbb380077e575a118f0c39655ba362e61897 (the last commit touching the campaign; it carries cbd1a94, "ready for lock", and the log of its id). Every line of the lock checklist (runbook section 4) was checked against the files, not against the keeper log. Distances, directions, days and sight lines were measured from `S/map.json` by the checker's own script: every land line in the twelve records and in `S/civs/haldren-sealed.md` (172 lines), every distance in the public world file and the DM release, and every god's starting view.

Result: 14 flags, on 6 of the 17 lines. The lock does not pass. No public `lock.md` and no `LOCKED.md` are written.

## Script output

```
tools/lockcheck.py sim-02 --all
places: 0 failure(s), 0 warning(s)
leaks: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-02
0 problem(s)
```

The same knowledge check passes on all seven sealed `S/gods/<label>/map-knowledge.json` files (run with `--knowledge`, output to the checker's scratch folder, nothing written to `P/`).

## The checklist, line by line

1. Seven NPC gods, files, cards, sealed folders. Yes. Seven folders by domain label with no number; seeds 25, 4, 27, 20, 22, 15, 5 distinct (god-sea's two seed rerolls logged with reason and `--replaces`); seven distinct domains. Each folder holds sheet, self, goals, record-of-gods, both negotiation files, power card and map knowledge. Each card's `Hidden powers` says only that two exist and its Ceiling reads `Set by the world. Not shown.` Each sealed folder holds a backstory, two hidden powers with the ceiling line (79, r-0142) and a growth file.
2. The player's sealed files and public card. Yes. Backstory, two hidden powers with the ceiling line, growth file with every power and both hidden ones. The public card names neither hidden power. Every "settled at creation" ruling carries a ledger id (L-0001 to L-0010, L-0020, L-0021), all present in the ledger.
3. Shared links and likenesses. Yes. All eight rows of `common-past.md` appear word for word in both gods' backstories and in the keeper log (2.5). The eight backstories agree with the common past and with each other. The only reuse of sealed names in the world is Maunt and Issel on the lintel of the Lamp Hut [f61], logged as likenesses; measured 327 miles from god-secrets' landing, the nearest seat, in unheld country.
4. Eight peoples, edges, meetings, dates. Yes. Seven NPC records and states plus the Haldren. Edges priced (Brannow and Pellim, L-0022; the rest none). Every meeting is "already there" and agrees with `deep-history.md`; every people's dates agree (Hodd 700, Tavrek 900, Ushkai 400, Senn and Corrant 120, Loweth and Thessend 600, Pellim 300 and 40). The fourteen reconcile items in `haldren-sealed.md` agree with the deep history (Blight Years, first moot, Corve lamp 27 keepers, the steward's count and the stool).
5. Godless peoples. Yes. Five, each with record, history and state.
6. Places. Flag 1.
7. Distances, directions and sight lines against the map at the pace table's rates. Flags 2 to 8.
8. Spacing, terrains, one sheet. Yes. Nearest seats 465 to 851 miles apart, every pair at least 33 days; every Night 1 terrain present; no desert or ice; one sheet, grid 5 by 4, no underground sheet and no layer. Neighbor days in `map.json` recomputed and symmetric.
9. Star and plane rolls. Yes. `star.md` holds every item with its roll id; the plane entries p01 to p03 match rolls r-0144 to r-0159 by the runbook's section 8 tables, face by face.
10. Mysteries. The script passes; by reading, one epic, five long, eleven short; every clue has location and at least two readings; every branch an answer; every Never found filled; rules 1 to 15 hold. Flags 9 to 11 (rule 16).
11. Causes, costs, clocks, random weighting, phenomena. Every mystery's cost is a row; random events minus 15 in Years 1 to 7; five phenomena for twelve years. Flag 12.
12. God-sense never a tally. Yes. Every release, card and public file gives it as face to face only, nothing at a distance.
13. One rule for the whole world. Flag 13.
14. Rolls. Yes. Script passes; the seed rerolls and void draws carry reasons and the rolls they replace; r-0160 states its method before the face.
15. The keeper log. Yes. Placements before rolls, eight answers per scale, every vote count, clamps (none needed), pools and leftovers, and every decision the files did not make, each marked for Michael.
16. Leaks, by reading every file in `P/`. Flag 14.
17. Nothing contradicts the deep lore or explains what it keeps mysterious. Yes, apart from what flag 13 records. The star results, the remainder, the hoarder, the ceiling (63 and 79), the ascended temper and star content all agree with the lore, and nothing explains what stays mysterious.

## Flags

### Flag 1. Line 6, places: night stones named as places with no map id
Rule: mystery standard, writing down ("Every place named in a sealed file carries its bracketed map id"); runbook line 6 ("every ... site ... referred to anywhere exists in `map.json`").
Where: `S/civs/haldren-sealed.md` item 11 ("a flat night stone", thirty miles above Ostrey beside the old road, no id of any kind); `S/mysteries.md` S01, branch "The god follows the road to the stair" ("thirty miles to the night stone"); S08 Cost if ignored and `S/event-schedule.md` C12 ("the path to the night stone above the terraces"); `S/civs/hodd/record.md` ("a flat stone above the terraces"). These are trade sites the history, two mysteries and a clocked row depend on.
What the record holds instead: no feature in `map.json` for either stone, and in the Haldren file and S01 no region id either. The script cannot catch it because the name is lower case.

### Flag 2. Line 7, distances: the Hald Valley is not within 500 miles of the Sleeper
Rule: runbook line 7; checker rule 9.
Where: `S/event-schedule.md` C03, Year 45: "every people within 500 miles of the Sleeper [f27], the Hald Valley [r01] among the last of them".
What the map holds: the nearest point of the Hald Valley [r01] is 548 miles from the edge of the Sleeper [f27]; Ostrey [f01] is about 620 from its edge and 638 from its middle. By the row's own measure the valley is never reached. The year, the distance, or the naming of the valley must change.

### Flag 3. Line 7, pace: days given at the open ground rate over mountain, marsh and forest, and the same ground priced two ways
Rule: runbook line 7 ("at the pace table's rates"); `engine/rules/time-and-pace.md` section 1 (mountain 8, marsh 6, forest 10, rough ground 14; a known pass counts as rough ground).
Where: 38 land lines in 9 files say "over open ground" while more than half of the straight line runs over mountain, marsh or forest regions: passfolk 13 (every line from Kinhold [f17], e.g. the Hush [f16] 100 miles in 7 days, the High Scarrow [r03] 530 in 38, all ground mountain), reedfolk 6 (from inside the Reedsea [r27], all or mostly marsh), Hodd 5 (the Deep Scarrow [r04] 300 miles in 22 days, the Knot Stair [f07] 340 in 24, the Low Scarrow [r05] 410 in 30), Brannow 4, Thessend 3, Corrant 2, Senn 2, Haldren 2 (the Sundown Sea [r32], Dunmarrow [f18]), Loweth 1.
Against this, `haldren-sealed.md` prices the Knot Stair [f07] (190 miles, 24 days) and the Deep Scarrow [r04] (510 miles, 64 days) entirely "by mountain paths", though the first 110 miles of each line are the Hald Valley floor. So the Knot Stair is 24 days from Ostrey by one rule and 24 days from Undercrag [f13], 150 miles farther, by the other. One rule for the ground named, applied to every line, is needed; where a line follows a known pass or road, the record should name that ground.

### Flag 4. Line 7, records against the map: Saltstairs is not at the mouth of the Pellwater
Rule: runbook line 7; map.md 1.3 step 7 (every description of land read off the data).
Where: `S/civs/pellim/record.md`, Home line: "Saltstairs [f41], the walled city on the tide at the mouth of the Pellwater [f40]". The same record's knowledge list says the Pellwater lies "about 30 miles east"; god-sea's map knowledge reports "the river in its estuary" from the quay.
What the map holds: the Pellwater [f40] ends at the edge of the Drowned Shelf [r35] 28 miles east of Saltstairs [f41]. The record contradicts itself and the map.

### Flag 5. Line 7, records against the map: Ardmoor stands on no river and no barge channel
Rule: runbook line 7; checker rule 9.
Where: `S/civs/godless/thessend/record.md` ("the Crownlands [r25], on the lower Lowe [f03], with the crowns of Vessany [f50] and Ardmoor [f51]"); `S/mysteries.md` S11 (Body and Cost: "the barge channel below Ardmoor [f51]"); `S/event-schedule.md` C15 ("in the barge channel below Ardmoor [f51]").
What the map holds: Ardmoor [f51] is 122 miles from the nearest reach of the Lowe [f03] and 65 miles from the edge of the Reedsea [r27]; no river or channel in `map.json` passes within 120 miles of it. S11's cost (barges lost below the city, the city blaming the reed folk) rests on ground the map does not hold.

### Flag 6. Line 7, the map against its own notes: the Withy does not rise at the Kettle
Rule: runbook line 7; mystery standard rule 7 (a body on the map).
Where: `S/mysteries.md` L01, clue "The melt ring" ("a small spring runs from under it ... It is the highest water of the Withy [f12]"); the Withy's own note in `map.json` and the gazetteer ("Rises under the Kettle").
What the map holds: the Withy [f12] line begins at [228, 326] and comes no nearer than 18 miles to the Kettle [f08] at [240, 338]. Either the river's source moves to the Kettle or the clue and the note change.

### Flag 7. Line 7, sight lines: god-secrets sees snowy mountains 329 miles away
Rule: runbook line 7; map.md 2.1 and 3.4.
Where: `S/releases/creation/god-secrets-night3.md`, The country ("Mountains stand off behind the hills, with snow already on them"); `S/gods/god-secrets/map-knowledge.json`, r05 reported, source "own sight, at the landing", told name "mountains behind the hills, with snow on them", with a told wedge drawn inside the Bendlands [r29] about 15 to 55 miles from the landing.
What the map holds: the nearest edge of the Low Scarrow [r05] is 329 miles from god-secrets' landing. A 9,000 foot range is below the horizon from low hills well before 150 miles. The release's view and the knowledge entry cannot stand as sight; the god's own map will draw mountains on hill ground beside its seat.

### Flag 8. Line 7, sight lines: small things given as seen from the landing at distances the map's rule does not allow
Rule: runbook line 7; map.md 2.1 (the Keeper uses two miles on open ground, half a mile in forest or hill, line of sight in mountains).
Where, each from its god's landing point in `map.json`, each in that god's night 3 release under "What the land shows" and in its starting map knowledge as "own sight":
- god-sea (coast): the Dry Hull [f42], "the ribs of a large old hull", 13.1 miles over flat dyked ground; the Tide Stumps [f43], "lines of worked stone and stumps of old piles", 6.4 miles; the Pellwater [f40], 26.2 miles; the Drowned Shelf [r35], whose nearest edge is 25 miles out, from a quay at the tide.
- god-rivers (valley): Wardwell [f48], "a spring cased in old dressed stone", 4.7 miles; the Stopped Road [f49], "roads that come down to the water's edge and stop, with nothing answering on the far bank", 7.5 miles; the Bankwater [f45] "held behind a straight bank", 9.6 miles; Kessary [f44], 7.7 miles.
- god-secrets (wooded hills): the Bottom Mounds [f58], "too regular to be natural, with trees grown over them", 9.3 miles; the Banked Way [f59], 3.2 miles; Quillan [f55], 3.2 miles; the Sarn [f56], 6.8 miles.
- god-beasts (steppe): the Hardway [f35], "the grass grows thinner over something hard", 4.7 miles on flat grass; the Rib [f29], 8.7 miles.
- god-storms (hill): the Rope Line [f36], 4.2 miles; the Flat Banks [f37], "banks and ditches worn nearly flat", 2.5 miles.
- god-thresholds (hill): Dunmarrow [f18], 1.2 miles; the Bare Gate [f19], 1.1 miles.
The player's three (Ostrey [f01] 1.6, the Haldwater [f02] 1.3, the Fitted Way [f04] 0.9, on a valley floor) and god-stone's (mountain, line of sight) hold. Either the landing points move, or the views and knowledge entries keep only what the map's rule lets a god see from where it stands, or the Keeper's reading of the rule for distant views is written and applied to all eight alike. As written, the player's god is held to the rule and six others are not.

### Flag 9. Line 10, rule 16: the voices in a god's sleep have no written limit
Rule: mystery standard rule 16 (its own list names "a voice in a dream"); writing down ("a Limit: line in the mystery that uses it and in the cast").
Where: `S/mysteries.md` L03, clue "Weather that counts" and branch "The god answers the voices" ("they have little to say and mean it. Once or twice in decades one names a power"); `S/event-schedule.md` T05.
What the record holds instead: no `Limit:` line in L03 and no entry in `S/cast.md`. Nothing says what the voices know or do not, what they will not say, whether a god may put a question to them, how often, or that they cannot give the year of the fall or the rate of the lowering, which are the epic's central measurements (rule 16, last sentence; rule 14).

### Flag 10. Line 10, rule 16: the Hodd count-keepers answer questions with no written limit
Rule: mystery standard rule 16 ("a people that keeps records").
Where: `S/mysteries.md` S08, clue "Listed as living" ("SEEN, from Year 1 by any household head who asks Garran Holt"); `S/civs/hodd/record.md` (the count-keepers "say who is alive, who is owed and who owes").
What the record holds instead: no `Limit:` line in S08 and none in the cast: nothing on what the rolls hold and do not, who may ask besides a household head, or how often.

### Flag 11. Line 10, rule 16: Ikk speaks to lowlanders of a cord count with no written limit
Rule: mystery standard rule 16.
Where: `S/cast.md`, Ikk ("She speaks to lowlanders, which no other of her people does, and is not a cord-keeper: she knows her own house's count and nothing of the long one").
What the record holds instead: a partial statement of what she knows, and nothing on what she will not say, who may ask, how often or in what form. She is the one cord-knower who talks to anyone, so without a limit she is an open way round the cord-keepers' limit (three winters of fair trade, one question a meeting) in E01, L05 and T14, including whether her house's count holds the winter of the notch.

### Flag 12. Line 11, the mild ones: the mystery and the phenomena record disagree
Rule: runbook line 11; mystery standard rule 15 (recurring phenomena at their true rate).
Where: `S/mysteries.md` S08, Cost if ignored: "One or two Hodd each winter, by the count in the phenomena record."
What the record holds instead: `S/state/phenomena.json`, mild-ones, gives 3 in Years 7, 9, 10 and 11 and 4 in Year 12. The words and the count cannot both be true; the count is the authority, so the mystery's words are the ones to change.

### Flag 13. Line 13, one rule for the whole world: a meeting tells more than the world's rule says
Rule: runbook line 13; `P/player/world-rules.md` and every card and release ("It tells only that the other is a god, nothing of its name, its nature or what it can do"); deep lore Truth 5 ("investigation finds whatever that campaign's god-sense gives and no more").
Where: `S/event-schedule.md` T13 ("If their pasts share a row of the common past, each also feels something it cannot place"); `S/mysteries.md` L01, clue "What two gods feel at a meeting" ("that they have stood at the same door, counted the same herd, shut the same room"); the "How this past might surface" lines of the eight backstories.
What the record holds instead: the meeting rule as published says a face to face meeting gives only that the other is a god. The sealed files add a second, felt knowing at the meeting itself for the pairs on the links table, so the rule reads one way for linked pairs and another for the rest, and a god gains at a meeting a sign of the other's past that the published rule says it does not get. Either the published rule makes room for it in words that hold for every pair, or the felt kinship comes through something other than the meeting (a later act, a dream at the stone, a thing done together), as the backstories' other surfacing lines already do.

### Flag 14. Line 16, leaks: a public file gives the count of gods
Rule: DESIGN 12.2 ("Nothing in the player's campaign folder reveals ... the count of gods"); runbook line 16 and the runbook's standing rules ("Nothing in `P/` names ... a count of gods"); DESIGN 1.4.
Where: `campaigns/sim-02/player/power-lean.md`, line 3: "The DM has seen no other god's build, so this is a judgment of the card on its own, not against the other seven."
What the record holds instead: "the other seven" tells the reader there are eight gods. The script did not catch it because the number is a common word. The sentence needs no number. Every other file in `P/` was read in full for counts of gods in any wording (number words, "the other", "all", "each", "both", "builds", "eight surveys") and holds none; no vote, pool, sealed place, coordinate beyond the god's own sight, star value, deep history, mystery, schedule, hidden power name, common past name or phenomenon count was found.

## Counts

Line 6: 1. Line 7: 7. Line 10: 3. Line 11: 1. Line 13: 1. Line 16: 1. Total 14. Every other line: yes.

For the rerun: the Keeper fixes, commits, and asks for the flagged lines again; the checker reruns the scripts and every flagged line, and rechecks any line a fix touches (a moved landing point reopens lines 7 and 8 for every god).

# Lock flags: sim-02, round 2

Run by the continuity checker, 2026-11-20 09:53 Pacific, against commit 5fcebcfcab28a47b460bad23fc474f786b5cea58 ("lock round 1, fourteen flags fixed"). The one later commit, 33fd7e5, touches nothing under either campaign folder. Rerun: the scripts; every flagged line of round 1 (6, 7, 10, 11, 13, 16); lines 7 and 8 for every god, since five landing points moved; and line 3, since every secret backstory and the common past changed. Every land line in the twelve records and the Haldren's sealed file (181 lines) was measured again from `S/map.json` under the Keeper's new pace rule (each stretch at the rate of the region it crosses), with every god's starting view and the ring of seats.

Result: 3 flags, on 3 lines. The lock does not pass. No public `lock.md` and no `LOCKED.md` are written.

## Script output, round 2

```
tools/lockcheck.py sim-02 --all
places: 4 failure(s), 9 warning(s)
leaks: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-02
0 problem(s)
```

Every one of the 4 place failures and 9 place warnings is in this flags file (round 1's bracketed pixel coordinates and map names written without ids). Findings inside `years/000/lock-flags.md` are not counted: the file is the checker's own record, not world content. With it set aside, `--places` has 0 failures and 0 warnings. The seven sealed knowledge files pass the knowledge check.

## Round 1 flags, rechecked

1. Night stones: fixed for the Haldren file, S01, S08, E01, L05, the cast, C12 and T14 (the Leaving Stone [f67], the Night Table [f68], both on the map where their records put them: 30.1 miles south-west of Ostrey [f01] beside the Fitted Way [f04], 1.2 miles north-west of Undercrag [f13]). Not fixed in the pass folk record: round 2 flag 1.
2. Year 45: holds. Ostrey [f01] 638 miles from the Sleeper's middle, inside the 650 now written.
3. Pace: holds. All 181 lines agree with the map within rounding, in distance, direction and days; the two road lines at the road rate; the one sea line marked coastwise.
4. Saltstairs [f41]: holds, 0.4 miles from the Pellwater [f40].
5. Ardmoor [f51]: holds, on the Lowe [f03]; Vessany [f50] 0.6 miles from it.
6. The Withy [f12]: holds, its line 0.9 miles from the Kettle [f08].
7. god-secrets' mountains: holds. Gone from its starting map; its release carries a correction; the Brannow record says what changed.
8. Sight from the landings: holds for seven gods by the Keeper's written reading. Not for god-stone: round 2 flag 3.
9, 10, 11. Rule 16: the voices, the Hodd count-keepers and Ikk now carry written limits in their mysteries and the cast. None can give the epic's measures. One new disagreement in the cord-keepers' limit: round 2 flag 2.
12. The mild ones: holds; S08 now matches the phenomena record year by year.
13. The meeting: holds. T13, L01, the common past and all eight backstories now give a meeting only that the other is a god, for every pair; recognition comes only through a dream at the stone. The links table is unchanged and still appears in both gods' backstories in the same terms (line 3 rechecked).
14. The count in `power-lean.md`: holds. The public folder was read again for counts of gods in any wording; none.

Lines 7 and 8 for every god: the ring is 465 to 850 miles between nearest seats, every seat in its wished terrain; the player's landing, Ostrey [f01], the river, the road, the Highfold [f06] and the valley's head and mouth measure as before, and `world/world.md` and `releases/000/dm.md` still hold.

## Round 2 flags

### Flag 1. Line 6, places: the pass folk record still names a trading stone with no id, in the wrong place
Rule: mystery standard, writing down; runbook line 6; runbook line 7.
Where: `S/civs/godless/passfolk/record.md`, The Hald Valley [r01] line: "from above, at night; a trading stone at its head". Also `S/civs/godless/passfolk/state.md`: "silent trade at night stones with the valleys at the range's foot", plural, with no ids.
What the map holds: the only trading stone in the Hald Valley is the Leaving Stone [f67], 30 miles above Ostrey [f01] and about 79 miles below the valley's head, not at it. The state's plural stones are not on the map; the map holds two.

### Flag 2. Line 10, rule 16: the cord-keepers carry two different limits
Rule: mystery standard rule 16 and writing down (the being's limit in the mystery that uses it and in the cast).
Where: `S/mysteries.md` E01 and `S/cast.md` (and T14) now say a keeper answers only one who has traded fairly for three winters "at the Leaving Stone [f67] or the Night Table [f68], only at that stone". `S/civs/godless/passfolk/record.md` still says "only at a trading stone", any stone, and the state speaks of stones at every valley at the range's foot.
What the record holds instead: one being with two limits that disagree on where it may be asked. The pass folk's civ agent reads its own record, so in play the wider one would govern.

### Flag 3. Line 7, sight lines: god-stone's starting view is not held to the reading the other seven were moved to meet
Rule: runbook line 7; map.md 2.1; the Keeper's reading logged under "Lock, round 1" ("within two miles on open ground (valley, plain, grass, shore), within half a mile in hill or forest, and by line of sight in mountains ... applied to all eight alike").
Where: `S/gods/god-stone/map-knowledge.json` and `S/releases/creation/god-stone-night3.md`: Undercrag [f13] reported from own sight at 7.1 miles ("a walled place at the valley foot, far down") and the Squared Doors [f14] at 2.5 miles, from a landing at [256.0, 450.0].
What the map holds: that landing lies inside the Underfell [r06], terrain valley, 57 miles from the nearest edge of the Deep Scarrow [r04]. By the reading as written it is open ground and the limit is two miles; god-rivers' landing, also in valley ground, was moved six miles to meet it. Round 1 recorded god-stone's view as holding under line of sight in mountains; on the map's own terrain that was the checker's error, and it is corrected here. Either the reading says in words how a high valley under a range counts, and the same words hold for the player's valley, or god-stone's view keeps only what lies within two miles.

## Counts, round 2

Line 6: 1. Line 7: 1. Line 10: 1. Total 3. Every other line: yes.
