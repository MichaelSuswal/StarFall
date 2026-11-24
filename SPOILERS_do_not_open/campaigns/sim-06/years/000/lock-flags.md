> SPOILER WARNING. Sealed. Lock flags for campaign sim-06. Players must never read this file.

# Lock flags: sim-06, round 1

Run by the continuity checker, 2026-11-24, from 15:35 to 15:42 Pacific, against the Keeper's ready-for-lock commit 2550a79e74f275a031580cbeedff46aa93c43098 as it stands at 8eef513 (the keeper log line naming the ready-for-lock id; nothing else in either campaign folder differs; the later commit 8e461da touches only `tests/`). Times of each state: running 15:36 (commit bdef546), passed 15:42. There is no `S/rulings.md`: no in-run ruling of Michael's stands. No test override. Every line of the lock checklist (runbook section 4) was checked against the files, not against the keeper log.

Result: 0 flags. Every line is yes. `S/leak-allow.txt` written with two phrases (below). `P/years/000/lock.md` reads passed; `S/LOCKED.md` follows in a commit of its own.

## Script output

Before the allow file:
```
tools/lockcheck.py sim-06 --all
FAIL leaks: campaigns/sim-06/player/transcript-day2.md:13: number word "three" near "god": "three are given, the same for every god"
FAIL leaks: campaigns/sim-06/player/transcript-day2.md:23: number word "two" near "god": "god of the moment two"
places: 0 failure(s), 0 warning(s)
leaks: 2 failure(s), 0 warning(s)
releases: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-06
warning: traced land runs off the sheet's west, east edge(s) (west: r02, r11, r12; east: r06, r07, r22, r23, r25, r26); the land touches the painting border, so the sheet does not show where it ends
continent: 29 land region(s), narrowest about 802 miles across (north to south), average about 1,065 miles, widest about 1,195; east to west 1,075, north to south 807 miles; the land runs to the sheet's west, east edge(s), measured as traced
0 problem(s), 1 warning(s)
```

After the allow file (rerun 15:42):
```
places: 0 failure(s), 0 warning(s)
leaks: 0 failure(s), 0 warning(s)
releases: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)
tools/map.py validate sim-06: 0 problem(s), 1 warning(s), the same warning
```

## The known items, judged

- **The two Day 2 transcript hits.** Read in their sentences. Line 13, the DM's opening: "Those three are given, the same for every god" counts the three world rules just stated (one body, god-sense at close quarters, mortal magic's price), not gods. Line 23, the player: "a god of the moment two people agree on what a thing is worth" counts two mortals at a bargain. Neither states, implies or lets anyone work out a count of gods (DESIGN 12.2). The transcript is verbatim and is not edited. Both phrases written to `S/leak-allow.txt`, each with its reason and date.
- **The `validate` warning, land at the sheet's west and east edges.** Not a flag. The data follows the paint (DESIGN 11.1); nothing beyond the sheet's edge is drawn and the edges stay in fog (DESIGN 4.5); the land as traced passes the measures (narrowest about 802, average about 1,065, inside 800 to 1,200); no god's asked-for country is lost; the one people planned for the east coast was moved to a sea the sheet shows (keeper log 3a.5); no record points at ground off the sheet (the history's "beyond the sheet" is the plane, not a place). A repaint would need Michael's go and is not asked for. Listed under Rulings for review.
- **The sealed factor's name in NPC gods' own files.** Found in `S/gods/god-sea/self.md` 35 ("Calm water looks like luck."), `S/gods/god-sea/people-hoped.md` 42, `S/gods/god-rivers/self.md` 59 and `S/gods/god-rivers/people-hoped.md` 53: each an ordinary word in the god's own answers, written by its own agent. Allowed in those gods' own files and nowhere else (checker.md 5). Not in any card, sheet, release, negotiation text the Keeper wrote, record, civ file or public file: searched, none (the Keeper's 2.4 fix of the god-sea intent line holds).
- **Bynames that are ordinary words** ("friend", "the stranger" for god-secrets; "Guest" for god-thresholds; "the river" for god-rivers), and the 3b misses (the root of one earlier god's name inside the Gulf of Maun, the Maun Stair and the Maun Flats; the peoples' own words for the carriers; other peoples' one-word names for the world with an article). Every public file but the transcripts read for them by meaning: "friend" stands twice, in the player's own words about its people ("quick to notice when a friend gives short measure"), an ordinary word; "the river" stands only as a river; "Guest", "the stranger" and the world names do not stand as names. The Gulf, the Flats and the Maun Stair stand in the player's people's knowledge file as map names told to the people (DESIGN 11.4); the earlier god's name does not. "Walkers ... who sang lists of names" and "the list-singers" are the delta's own telling and own word, told to the people. None reveals a god, a count or the history.
- **The player's sealed answers and the channel's lines.** `S/player/unsaid.md` holds one request to the Keeper (Day 3) and a Day 2 line the DM flagged for weighing. `S/player/requests-answered.md`: Day 2, "received and ruled", then the Keeper's reason as an indented line, then the further line, added on Night 3a beneath the DM's dated agreement in `unsaid.md` (2026-11-24, Day 3; the commit order agrees: the agreement at the Day 3 close b037022, the further line at ded6c6a); it says only that the filing stands. Day 3: "received and ruled" for the request and for the line set beside it, with no reason line. No line tells the DM more than the rule allows. The request is ruled in the ledger (L-0029) and carried out as S01. No want has a confirmation, and none was applied: S01's truth (an old man, a chill in the flood, a fever) is traced in the keeper log (3b.4) to the 3a record (the chancery clerk, the old measure claim, the old weights), and it holds a deliberate act behind the death, so it is neither the player's sealed wish nor its opposite. Noted, not a flag.

## The checklist

1. Seven NPC gods. Yes. Labels god-sea, god-dreams, god-rivers, god-healing, god-beasts, god-secrets, god-thresholds, no number; seeds 2, 9, 1, 4, 7, 27, 30 and domains 7, 16, 17, 12, 11, 4, 19, none shared, none 14 (keeper log 1.3, rolls r-0009 to r-0131, rerolls with reasons). Each folder holds sheet, self, goals, record-of-gods, both negotiation files, power card and map knowledge; each has a landing release in `S/releases/000/`. Every card: `Hidden powers` says only that two exist; Ceiling `Set by the world. Not shown.` Each sealed folder: secret backstory, two hidden powers, knacks (3 for god-sea, god-dreams, god-secrets; 2 for the rest), each knack with Status `knack (undiscovered)`, Limit, Surfaces when and Drawn from, the ceiling line (73), a growth file. `S/balance.md` counts the knacks in its second weights. All 36 hidden power and knack names (16 and 20) are on `S/sealed-terms.txt`, and none appears in any god's own folder, any release or any public file (searched by script).
2. The player's god. Yes. `S/player/` holds the secret backstory, two hidden powers and three knacks with the ceiling line, standard mode (no `mirror.md`), and a growth file. `P/civs/unnamed-people/knowledge.md` gives names and grid cells and no map id. The public card names neither hidden power; Ceiling `Set by the world. Not shown.`; every settled ruling carries its ledger id (L-0001 to L-0005, L-0024 to L-0028; no `pending` left).
3. The common past. Yes. All six rows of the shared links table appear, in the table's event words, in both gods' backstories (checked by script) and in the keeper log (2.5). The likenesses are logged in `world-bible.md`: the gate's name under the sea-door of Port Sennet [f75] (by foot 152.8 miles from god-dreams, 363.5 from the player, 694.2 from god-secrets and 688.7 from god-thresholds, the two whose past holds the gate); a harbor chain from god-sea's own hope; a standard weight lost (S01) at the player's seat, from the sealed request's ruling and the weights already there; places kept for one awaited, from the carriers. They cluster near no one god.
4. Eight peoples. Yes. Seven agreed records and states, and the player's people's record and state; each with `## Helpers` (six "Designed, not yet serving, 2026-11-24" with the cost; the Sarrow "Served from landing" by their god's own rewritten meeting; the player's "Designed, not yet serving", Day 3). No NPC edge proposed; the one force over the measure (god-thresholds's sworn band) was offered both ways and taken at the ordinary size (L-0030); the player's edge (the tide-reckoner) priced at the table and confirmed (L-0024). No size priced as an edge. Every people inside its god's rule and worship leans (keeper log 3a.1). Every meeting reconciled with the deep history (keeper log 3b.4, read against `deep-history.md`: the promise's maker gone from the ground; the awaited figure from the carriers since 317 BA; dates agree). Nothing left unnamed for play is named: six homes carry placeholders, and the player's people and home are unnamed.
5. Godless peoples. Yes. Four (aldermark, hask-holds, harbor-league, water-folk), each with record and state and its telling of the history; Q4 at 5 gives four.
6. Places. Yes. `--places` 0 failures, 0 warnings. The one place added on 3b, the Gannel Stones [f80], is in `map.json`, the gazetteer (marked) and the Aldermark's land list.
7. Releases. Yes. `--releases` 0 failures, 0 warnings; no scarcity warning to keep.
8. Distances, directions, travel. Yes. Every travel line with a route and means in the seven agreed records, the four godless records, the world's-side file and the player's people's knowledge file was rerun through `tools/map.py travel` (26 trips, both ways where the line gives both): every figure matches the tool in miles and full days. For all eight landings, every distance figure in the DM release and each landing release stands in `tools/map.py describe --landing` (with that god's own knowledge file for the seven), and every id in each god's map knowledge matches the ids that view gives, and no other.
9. Spacing and the sheet. Yes. Nearest neighbors in straight miles from the landings: player 192.9, god-sea 251.2, god-secrets 188.1, god-beasts 188.1, god-rivers 191.8, god-dreams 191.8, god-healing 192.9, god-thresholds 281.5; shortest 188.1, at least half the longest (140.75). Every Night 1 terrain present (keeper log 3a.5). One continent on one sheet, grid 5 by 4, narrowest about 802, average about 1,065, as `validate` measures; the edge warning judged above. No underground (Night 1), none in `map.json`, no underground sheet; `validate` passes.
10. Luck. Yes. `S/state/luck.md`: a line for all eight, the player's under `player` (+1; god-healing +1; god-beasts +1; god-secrets +1; the rest 0), each change with its dated reason, matching the keeper log at 2.4 and 3a.1. Used only in the four weighted weather draws (r-0226 to r-0229), each named with its step and shares written before the cast; no other roll was for an act. No word of it in any release, card, sheet or public file.
11. Star and plane. Yes. `S/star.md` holds the eight star items and the ceiling with ids (r-0001 to r-0008, r-0140). The plane holds p01 to p03 with their rolls (r-0144 to r-0158) and `count_roll`.
12. Mysteries. Yes. `--mysteries` 0 and 0. By `Kind:` lines: one epic, five long, eleven short. Every clue has a location (an id or a being) and readings; every branch says what the world does; every `Never found` filled. Every mystery marked `yes` (E01, L03, L04, S09) carries its being's `Limit:` line, word for word as in `cast.md`; no mystery marked `no` has a being that answers questions in its clues or branches (read for the voices, the carriers, the Mollen and the dreams). The epic's measurements are each earned and none is delivered by a visitor; the dim night measurement is earned at the clue that L01 places on Whitmoor [r09]. Read against rules 1 to 16: no clue states a mechanism; no mortal telling is fully right about a cause; no counter-clue; nothing marked by tone; most of the world is no clue (the Whitmoor wonders line rewritten, logged).
13. Causes, costs, clocks. Yes. Every mystery names a row in `event-schedule.md`, and each named row stands (E01 to S11, one to fifteen rows each). Random events at base 30 with `opening=-20` in Years 1 to 7. `phenomena.json` holds three phenomena for twelve years each.
14. God-sense. Yes. Close quarters, a weight that settles into knowing, never a tally, in `world-rules.md`, the Day 2 transcript, every card, the DM release and every landing release.
15. One rule for the world. Yes. One body; god-sense as above; magic at 7 for every people, fitted the same way to all eight (keeper log 3a.1); no local exception.
16. Rolls. Yes. `--rolls` passes; r-0001 to r-0229, the duplicate rerolls (r-0128 to r-0131) and the tool's own rerolls (r-0190, r-0192) each name the roll replaced. `P/state/rolls.jsonl` is empty.
17. The keeper log. Yes. Every blend with its placements and eight answers, the two ties decided before their variation rolls, the vote counts (Q15, Q16), the clamps (Q6 by the star), every placement, every leftover, and every decision the files did not make, listed for review night by night.
18. Sealed terms and leaks. Yes. `S/sealed-terms.txt` holds every god name and byname that is not one ordinary word, every hidden power and knack name, every common-past name, peoples' and mortals' names, the 3b names, and `!luck` and `!Luck`. `--leaks` passes with the two allow phrases above. Every non-transcript file in `P/` read: nothing reveals a vote, a pool, another god, a count of gods in any wording, a sealed place id or coordinate, a star value, the deep history beyond what the people tell, a mystery, the schedule or a phenomenon's count. The people's tellings (the drowned larger god at the Maun Stair, the list-singers, the old keeper's chill) are what the people say, partly wrong. `P/state/images.md` carries the time of Michael's image approval, a record of his go and no stage time.
19. Deep lore. Yes. Read against Truths 5 to 8 and the numbers section: the Remainder in godless hills between two seats; the hoarder a ring of stones at the center, fed by the thread, its clock in Year 38; the carriers present, the thinners absent and nothing in their place; the voices at 58, four fifths of 73; rising after three years above 73; the earlier gods both off the ground before the arrival. The carriers' second round (Year 43) and other years are this star's own, set from ranges written before the rolls, as the numbers section gives. Nothing explains what the lore keeps mysterious.

## Flags

None.

## Leak allow file

`S/leak-allow.txt`, written this round: "three are given, the same for every god" and "god of the moment two", both for the reasons above.

## Rulings for review

- Line 9: the `validate` warning that traced land runs off the sheet's west and east edges. Ruled: not a flag. Reasons, by the judgment order: fairness (no god's asked-for country is lost, the player's included); fit (the data follows the paint, DESIGN 11.1, and the edges stay in fog, DESIGN 4.5; the measures pass as traced); balance (no seat touches an edge; the one people planned for an edge coast was moved before any land was described). A repaint is the owner's and is not asked for.
- Outside the campaign: `engine/rules/time-and-pace.md` 71, the pace table's swimming row, reads "kills the unlucky", which holds the sealed factor's name inside an ordinary word in an engine file the DM reads (`sealed-factors.md`, the checker's check, item 4). It has stood since the pace table was written (890ccf9, 2026-11-16), reveals nothing of the mechanic, and is no campaign file, so it does not bear on this lock. Only Michael can change an engine file. Ruled: recorded here for his review, with the plain rewording "and kills the weak" if he wants it changed; the lock goes on.
