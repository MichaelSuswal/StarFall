> SPOILER WARNING: the sealed section at the end of this file names secrets of campaign sim-01. A player should read only the summary above the line marked SEALED.

# Continuity check: creation test sim-01, run 01

Checker: an independent agent that built none of this. Date: 2026-11-19. Read: `CLAUDE.md`, `engine/roles/checker.md`, `engine/design/DESIGN.md`, `engine/rules/*.md` (map, time-and-pace and morning-story in full; the rest for what bears on creation), `SPOILERS_do_not_open/keeper/creation-runbook.md` (all, section 4 line by line), `mystery-standard.md`, `deep-lore.md`, and every file of `campaigns/sim-01/` and `SPOILERS_do_not_open/campaigns/sim-01/` except the two paintings and the Night 1 and Night 2 release texts (read only where a check needed them). Nothing was changed except this file. Scripts were run from a scratch folder and read the campaign files only.

## Summary, without spoilers

| Check | Verdict | Problems |
|---|---|---|
| 1. Lock checklist, 14 lines | No. 9 lines hold, 5 do not hold in full | 5 lines (5, 8, 9, 13, 14), with about 20 findings between them |
| 1a. Place ids by script | Yes | 0 of 42 bracketed ids missing; prose references to unmapped ground found by hand |
| 2. Rolls | Yes | 0 substantive; 1 miscount in the log's own tally |
| 3. Leaks to the player's side | No | 1 hard leak, 2 soft exposures; the player's power card is correct |
| 4. Mystery standard, spot check | Mostly yes | the epic passes; 1 of 3 short mysteries passes in full; 1 standing risk |
| 5. Consistency | Mostly yes | 3 backstory issues, 1 small date mismatch, 4 direction or distance mismatches |
| 6. Dashes | Yes | 0 in 178 files |

Problems by procedure only:

1. One player-visible file states how many other gods exist. The design says players never learn this.
2. The player's first-morning release gives distances and lines of sight near the landing that the traced map does not support (one landmark is placed many times farther away in the data than the release says, and could not be seen from where the release says it is seen; one trade journey is given about half the days the pace table needs).
3. Old made-road markers that a clue, the epic, the deep history and one hidden power's trigger all depend on are not in the map, apart from one set. Two collective place names used in the schedule and the history name no region in the map or the gazetteer; one clue site and two settlements in a people's record are unplaced.
4. Four mystery costs are missing from the event schedule (three wholly, one only as a trigger).
5. Six of thirteen short mysteries have no written readings; eleven have no written branches with the world's answers; none records what is never found. The runbook asks for all three for every mystery.
6. Three passages read against the deep lore or leave a deep-lore mystery open to being explained in play.
7. Two world-rule applications look like local exceptions (one rule made to differ at two places; one rule applied to parties it was written not to cover).
8. Names from one sealed backstory source recur in the world's own records, which the deep history says they do not; the echoes cluster near two gods and one sits at the player's landing.
9. A shared-past link is written in two of eight secret files where the runbook asks for it in each pair's files; five touching pairs are not in the keeper log; the log misstates one fact about names.
10. Three NPC releases carry direction or distance errors against the traced map (two quarter-turn errors in river direction, one distance error), and two of those errors were copied into the peoples' agreed records.
11. Two player-visible files carry the year's true counts of recurring things before anyone has seen them, and one carries sealed map ids and placed coordinates for rumors.
12. The keeper log's own roll tally for the Night 1 blend is split wrongly (total right).

Overall verdict: not fit to start play as locked. It needs a short, targeted rework first, not a rebuild. The world's substance is sound: the rolls are clean, the star is right, the history is deep and coherent, the epic is well built, the player's card and agreed people are exactly as agreed. But items 1 to 5 above are failures of the lock checklist itself, and items 2 and 3 touch the player's first days of play directly. Because the runbook forbids changes after the lock, Michael would need to authorize reopening it to make these corrections and re-lock. Item 1 cannot be undone for this run, since the file has already been visible.

---

## SEALED: details, with spoilers

Paths: `P/` is `campaigns/sim-01/`, `S/` is `SPOILERS_do_not_open/campaigns/sim-01/`.

### Check 1. The lock checklist, line by line

1. **Seven NPC gods, files complete. Yes.** Script: every one of the seven has `sheet`, `self`, `goals`, `record-of-gods`, `power-card`, `map-knowledge.json` (valid JSON), `gods-sealed/<g>/hidden-powers.md` with exactly two powers marked `hidden (undiscovered)`, and `gods-sealed/<g>/backstory-secret.md`. Each card has 3 or 4 `Status: main` powers, Description and Drawback present. Seeds 9, 25, 1, 5, 12, 26, 30 and seven distinct domains confirmed against the roll log. Deviation, logged and reasonable: hidden powers and the ceiling number sit in `S/gods-sealed/` and each card's Ceiling line reads "Set by the world. Not shown." The runbook's letter puts both on the card.
2. **Player's sealed backstory and hidden powers; public card. Yes.** `S/player/backstory-secret.md` and `S/player/hidden-powers.md` exist, two powers, ceiling 74 appended. `P/player/power-card.md` says only "Two hidden powers exist (3.9)" and its Ceiling line is exactly `Set by the world. Not shown.` Neither hidden power's name appears anywhere in `P/`.
3. **Eight peoples, edges priced, meetings reconciled. Yes, one small mismatch.** Seven NPC records and states, plus the Carrowfolk record and state in `P/`. Edges: Cutfolk lineage singers and River Households exact books, each priced and made measurable; the player's two edges priced on Day 3. Meetings: see check 5. Mismatch: the Edgefolk record says they were pushed onto the edge "about 500 years" ago; the deep history dates the Tarsk arrival to about 600 BA.
4. **Three to five godless peoples. Yes, five**, each with record (history, code, wants, ties to great events) and state.
5. **map.json holds everything referred to. No.**
   - By script: 187 map ids, no duplicates, every neighbor and feature region and landing region resolves, neighbors symmetric. Every bracketed id in the deep history (32 distinct), mysteries (27), cast (9) and schedule (0 place ids; its 4 backticked names are phenomena) exists in the map: 42 distinct place ids, 0 missing. Every id in the eight map-knowledge files and in `P/civs/carrowfolk/land-knowledge.md` exists.
   - By hand, prose references to ground the map lacks:
     a. **High Road markers.** Only the Old Men are mapped. The epic clue ("markers every forty miles" round the lake), S2's clue ("the next marker stands forty miles off in a straight line across two valleys"), the deep history (the road west along Windlow to the Shut House and east to the Sallow) and the player's cool hidden power (reads the next marker each way) all point at markers with no fixed position. `map.md` bars roads as features but not ruins; markers are ruins and can be points. If the player's god lays a hand on the Old Men in Year 1, the Keeper must invent the next marker's place, which is a fixity breach. The schedule's own check ("the High Roads ... are in `map.json`") is false.
     b. **"the Westermoor"** (schedule, Year 2 signs, and the `geese-days` phenomenon) and **"the Black Plain"** (deep history, mysteries, schedule, Bankfolk, Maundsea, star) name no region in `map.json` and do not appear in the gazetteer. Which regions they cover is not fixed.
     c. **S9's milestone** "up the Lave road" bearing Ilsabet Corr's mark is a clue site with no place.
     d. **Sheerwall and Pinehouse**, two of the six Stair steadings named in the Stairfolk record, are not in the map (the other four are). Outside the four files the line names, but the line ends "Nothing anywhere points at ground the map does not have."
   - `LOCKED.md` copies line 5 without the word "road".
6. **Spacing, terrain, transitions. Yes.** Nearest-neighbor distances by script 371 to 540 miles; the player's nearest god is g2 at 383 miles. Every Night 1 terrain has a region. Transitions follow the paint, as the map order requires.
7. **star.md. Yes.** Nine items, the full list under the lore's `Per-star variation`, each with a roll id; every mapping recomputed and correct; ceiling 74 within 71 to 80.
8. **Mysteries pass rules 1 to 14, every clue placed. No.**
   - Count is right: one epic, four long, thirteen short.
   - Readings (rule 2) are not written for S4, S7, S9, S11, S12, S13.
   - Branches with the world's answers (rule 6, runbook 3.6) are written only for S1 and S2. Some answers exist as schedule triggers (S4, S5, S6, S7, S9); S3, S8, S10, S11, S12, S13 have none anywhere.
   - "What is never found" (runbook 3.6, rule 11) is written for the epic and the four long mysteries and for no short one.
   - Clue placement: S9's milestone is unplaced (line 5c); the S2 and epic markers are unplaced (5a).
9. **Causes, costs, clocks, random weighting, phenomena. No, in part.** Every schedule row has a cause. Random odds: base 30, steps 25, 20, 15, 12, 9, 6, 3 for Years 1 to 7, clamped at 5. `phenomena.json` has four phenomena for twelve years and `tools/phenomena.py` returns them; the Year 2 and Year 5 pass counts (25 and 22 weeks) match the schedule's early shut and seven-month winter. Missing from the schedule, against runbook 3.7 ("the costs-if-ignored from every mystery, as clocks or triggers") and the mysteries file's own claim at its foot:
   - S8: the traveler's death in the winter of Year 4 and the blame on the Marrins. Absent.
   - S3: the stone-wife's loss, "by Year 6 she does not know her own door". Absent.
   - S10: the tasteless field widening a furlong a decade, Reedditch's east fields by Year 30. Absent.
   - S5: the Hall's vote to quarry the Law Stones in Year 4 is not a clocked row; only the trigger "guarded before Year 4" exists.
10. **One rule for the whole world. Borderline.** (a) God-sense is a world rule, yet at the shore of Lake Enner and the Door of Vorn a god feels which way every other god lies. The Keeper calls this a fact of two places reconciling the Q15 vote with Truth 5. It is defensible, but it is the shape the line forbids, and it gives whoever reaches either place every rival's bearing. Michael should rule. (b) The oath rule binds oaths "between gods". Long 1 says the Abider and lake oath shows "what an oath is here (`star.md`, the oath rule's hidden form)", and the epic says a god who swears with the lake "pays what was named". Neither party in the First Oath is a god, and the lake is not one either. Either the rule's scope is wider than written, which is then a local extension, or those two lines overstate it.
11. **Rolls. Yes.** See check 2.
12. **Keeper log completeness. Yes, with two factual errors.** Every Night 1 blend lists eight answers (seven where a god skipped, as logged); medians recomputed and correct for Q3, Q4, Q5, Q6, Q8, Q9, Q13, Q14; vote counts for Q15 (5 to 3, and 5 to 3 on manner) and Q16 (7 to 1); the bodies default; placements; the Q5 and Q6 clamps; leftovers in the world bible. Errors: (a) line 245 splits the ten blend rolls as "three half-median rolls, seven variation rolls"; the file has two half rolls (r-0122, r-0129) and eight variation rolls. (b) Step 3.5 says none of the seven Longwalker names "is a name any god of this campaign chose except 'Orrun'". Garrow is g4's chosen name and is in the list.
13. **Nothing in `P/` reveals sealed matter. No.** See check 3.
14. **Nothing contradicts the deep lore or explains what it keeps mysterious. No, in three places, all fixable in wording or a ruling.**
   - **The Abiders and the anchor.** Truth 8: an anchored god survives the fall "and so will its anchor, and nothing else." The deep history ("came through with it") and Long 3 ("the Abiders came through in its halls. What is stored comes through a fall") read as the Abiders riding the Stayer's anchor through. If they survived by their own storedness (one law, one calendar, one unchanged list, Truth 2), say so and drop "with it" and "in its halls".
   - **The Stayer.** Cast and Long 3: it "answers a question truly, once per asker per year." No limit is set on what it knows. Asked why the plane keeps accounts, what the Between is, or what a risen god becomes, a truthful answer would explain what the lore says is never answered. It needs a sealed line on the edges of its knowledge ("it does not know" is a true answer).
   - **"Never learn whose."** Truth 5: a god can learn it is a remainder and never whose. g3's sealed file makes her hidden song "the only complete record of the country the eight gods came from", in which "every other god's making is a verse". A ruling should fix now that the Roll yields names and never identities, so the night turn does not have to improvise one.
   - Checked and consistent: the ceiling's 80 percent trigger (59) and the three-year rise; the hoarder's 400-year naming; the Longwalkers' first and fourth decade visits (Years 6 and 39); fading on the oldest ground (the tasteless field, the bowl); the pale herds; the star's phase, rain and radius; Enna's lightening signs.

### Check 2. Rolls, by script

- `S/state/rolls.jsonl` has 141 lines; timestamps ascend; `P/state/rolls.jsonl` is empty as required.
- Every id r-0001 to r-0141 is cited in the keeper log, `star.md`, a sheet or a sealed hidden-powers file. No cited id is outside the log.
- Every "roll X maps to Y" in the log (49) recomputed from the log's raw roll with the stated die: all correct. Every lean value (63 plain, 7 Company with +25 capped) matches its raw roll. All seventy sheet leans match. All nine star mappings correct, including the d8 and d6 mappings the Keeper set before rolling.
- Labels rolled more than once: g5 Domain (r-0080, r-0081), g7 seed (r-0114, r-0115), rain density (r-0134, r-0141). Each later roll's `what` names the earlier id and the reason (duplicate domain, duplicate seed, roll of 98 above the d6 range). No other repeat. No d12 roll above 96 and no d30 roll above 90 occurred, so no range rerolls were needed there.
- Half-median rolls at odds 50 read "success rounds up": r-0122 (51) and r-0129 (53) both failures, rounded down, as logged. Variation rolls applied correctly in all eight blends.
- Problem count 0, apart from the tally miscount under line 12.

### Check 3. Leaks, and the player's card

- **Hard leak.** `P/player/power-lean.md` line 3: "not against the other seven." DESIGN.md item 4: "Players never learn how many gods arrived." The DM wrote it, but it sits in `P/` and line 13 covers `P/` whole.
- **Soft exposure 1.** `P/releases/000/dm.md` lists Year 1's true counts, among them "Nights this year on which the blue star dims for an hour or more: 4." The release is prescribed by the runbook and rule 15 wants true counts, but the dimming star is the epic's first visible sign and the count is schedule data. Anyone reading `P/` learns the star dims before the god sees it. `world/world.md` is clean on this point. Better: hand the DM the count only when the god or its people would notice, or keep the release outside `P/`.
- **Soft exposure 2.** `P/civs/carrowfolk/land-knowledge.md` carries map ids and rumor coordinates. Most ids are harmless. `shut-house` gives away the Keeper's name for "a stone on Windlow with a swept doorstep", and `enner` is the stem of the lake's, the kingdom's and the risen god's names. The `near` coordinates choose among the rumor's own alternatives (the sea "south-west, or west, or there isn't one" is given one point). Keep the ids in the sealed side, or use neutral ids for rumors.
- **Clean.** No other god's name, people, power or past; no Abider, Hollin, Enna, Vorn, Longwalker, fever, ceiling, Brennoch, vote, pool, blend or median anywhere in `P/` (searched with a term list across all public files, transcripts included). `player/map-knowledge.json` holds the landing region, the stream, the tops, the pass and the Old Men as seen from below, with `told` names that hide the Keeper's ("three standing shapes on the pass"). `tools/map.py` uses `told.name` below `seen`, so the Keeper's names do not reach the drawn map. One grade inconsistency, not a leak: `world.md` says "Rumored or reported: nothing yet" while the knowledge file has three `reported` entries sourced to the god's own sight.
- **Player's card.** Correct on both counts: two hidden powers stated to exist and not named; Ceiling line exact.

### Check 4. Mystery standard, spot check

**Epic, the Counting Water. Passes.**
- Rule 1: every clue is an effect, object or behavior; mortal accounts are wrong (the names as "modesty"; Enna "went up to plead"). Annis's slats ("looked at by the lake") come closest to naming a cause, and the readings keep it open.
- Rule 2: readings written for all ten clues.
- Rule 4: no decisive clue by visitor. The Longwalkers (Year 6) speak of the bowl only if asked, and say only that its names can no longer be collected. That counts as earned, not delivered.
- Rule 7: body, cost and clock (Years 5, 12, 15, 25, 30, 40); triggers in the schedule.
- Rule 13: immortal power (the hoarder, a risen faction); "to hold the whole ring takes peoples on every side."
- Rule 14: three measurements (edge, speed, link to dim nights), each earnable by own instrument, a counter sent, an alliance (king's chest and tax rolls, the Abiders' Count, the Sallow tallies) or a place (shore, Sighting Stones, Sworn Door, Vorn). None is a scheduled visitor.

**S1, the ones before. Passes.** Clues are objects and behavior (walled fold, two oldest laws, a shared silence, carriers who will not sleep in Carrow in a fever summer, a quern of foreign make). Four readings. The Carrowfolk belief ("turned on each other") is half wrong, satisfying rule 1. The decisive clues are earned: open the fold, or ask the Wardens directly. Cost Year 4, with a trigger that avoids it. The 11-year flare from 7 BA lands on Year 4, consistent.

**S4, the Shut Stair. Fails rules 2 and 6 as written.** Clues are good effects and objects (51 notches, bronze in empty houses, a widening crack, Ysolt's "not this year"), and the cost has a clock (Year 3, 110 people) and a trigger (move Gullet). But no readings are written, and no branches or world answers beyond the one trigger.

**S8, the lampless hours. Passes rules 1 to 4; fails runbook 3.7.** Clues are behavior and effects (lamps out only in one side valley on moonless nights, wet bare footprints, the finder is the walker), with four readings. The decisive clue is earned by watching at night. Its cost (Year 4 winter death, blame on the Marrins) is not in the schedule, and no branches are written.

**Standing risk across the set:** the Stayer as an unlimited truthful answerer (check 1, line 14).

### Check 5. Consistency

**The eight secret backstories against each other and the deep lore.**
- The four events of Vessary are told the same way in all eight files and the common file: Judgment, Calling-In, Closing Winter, the Roll, then the fall. Reciprocal links agree in every case where both files speak: g1 and g7, g1 and g4, g1 and g2, g2 and g4, g2 and g5, g4 and g5, g5 and the player, g6 and g7, g6 and the player, g7 and the player, g1 and the player.
- All consistent with Truth 5: patterns, not persons; the fall unremembered; wounds felt, never explained.
- Problems:
  1. **The g3 link is recorded in two files only.** g3's link to "all seven others" appears in her own file and the player's; the other six files do not mention g3. Runbook 2.6 asks for both files.
  2. **Five touching pairs are not logged.** g1 and g2, g2 and g4, g4 and g5, g5 and the player, g6 and g7 are not in the keeper log's list of touches. The common file's list also omits g6 and g7 and g1 and g2.
  3. **Vessary names recur in this world.** The deep history's check says "The only things of it here are the eight gods and seven names in a Longwalker list." In fact:
     - "Vane" (Vessary's last Tallyman, Edric Vane) is the house of the Debt Door oath and g5's people's Reckoner, Hesper Vane.
     - "Edric" is Maundsea's heir, crowned Year 3, who levies g4's people.
     - "Tallymen" (g4's own institution) is what the Bankfolk record calls Maundsea's levy collectors.
     - "Coll" (Hedra Coll, the Dale's headwoman, g1's people) is the dead shepherd whose small cairn stands a few paces from the player's landing.
     - Together with the Howe's sleeping barrow kings, the Stubble Man and the empty granaries, g4's home ground carries far more likenesses of its sealed past than any other god's. g4's file intends the granaries only.
     - These are unacknowledged clues. Rename them, or log each as a deliberate likeness and check that no god is favored.
  4. The keeper log's claim about the Longwalker names (check 1, line 12b). The list holds Orrun (g1 and g7), Garrow (g4) and Keld and Anwy, the two halves of the player's own lost name. Each god is touched, so the neutrality claim roughly holds, but the stated fact is wrong.

**The eight meetings against the deep history.** All eight are "already there", and each history fits:
- Stair 310 winters and the 311-notch stone; Hask 140 BA and 212 dead.
- Corrford's 420 years and the last Corr king in 421 BA; the Hollin survivors (253 BA) down the Wend.
- The Cutfolk's 700 years on the cuts, with a lineage that begins at Halmer.
- The Bankfolk's 190-year levy.
- The 640-year flood post and 2,500 years of moving towns.
- Lavedale's 3,000 years and freedom since the lake kingdom drew back (about 520 BA).
- The Carrowfolk's ten generations and two bands in 252 to 251 BA.
- One mismatch: the Edgefolk date, about 500 years against about 600 BA.
- Also noted: the Cutfolk record says three singers "can hold the whole lineage word for word", while S11 and the deep history make Wenna Marl the sole holder of Halmer's first line. The edge's own price ("the part only she held is gone") reconciles them if read that way. Worth one sentence in the record.

**The player's agreed people and meeting. Kept unchanged.**
- The DM's record and `people-meeting.md` were not altered.
- The release lands the god at night at the valley head, still for the first week, found by the first shepherd up.
- 1,200 people, no town, no lord, salt and iron over the pass, "the ones before", old slab cairns on the pass: all held.
- The DM's stone-wife ruling stands, with the world's rule adding a slow worsening (S3). That is consistent with the DM's own "subject to the Keeper" note.
- No `corrections.md` was needed and none exists.

**The three compass mismatches the Keeper reported.** Measured from each landing point by script on `map.json`, at 1.6 miles to the pixel:
- **g2-law:** the release says the river comes out of its gorge "upstream, to the east". The Corr runs north to south through the landing, and the gorge lies due north (bearing about 4 degrees), with its mouth about 44 miles off. That is a quarter-turn error. The Sworn record repeats "the walled town ... where the river Corr leaves its gorge", but the town sits about 35 miles below the gorge region in the data.
- **g3-song:** the release says "downstream, to the south-west, the river loses its banks". At the landing the Sarn flows south-east and then east to Sarnmouth (bearings 143 to 168 degrees). The fog sea, the Murk, does lie south-west (about 230 degrees), so the release merged the river's course with the coast's direction. Quarter-turn error. The Drowned Road does run south-west, as the release's last line has it.
- **g4-harvest:** the compass words hold. The Maund runs south; the Howe is north-east at 16 miles ("a morning's walk", generous); the Old Bins are downstream at 15 miles. The error is distance: "beyond the last fields to the west, a dark line of uncut scrub and wood" puts the Westwild in sight, and the Bankfolk record says "a day's walk west". The nearest Westwild edge is about 128 miles off.
- **How bad: low to moderate.** No NPC god has landed or acted on them, and the Keeper notes they will be told the ground as it is. But two of the errors now sit in agreed records (Sworn, Bankfolk) that civ agents will read as fact. Fix the data (`map.md` says to fix mismatches in the data) or the records before Year 1.

**A fourth mismatch the Keeper did not report, in the player's own release.** This matters more than the three above, because the first morning story is written from it.
- `dm.md` puts the pass "half a day's climb above" and has the god see "three tall dark shapes, too regular for outcrops" on it at first light. In the data the pass is 23 miles off and the Old Men 26 miles (bearing about 50 degrees). That is one to three days on the pace table, and slab cairns cannot be told from outcrops by eye at that range.
- The land-knowledge file puts the Sallow "five or six days from Tophouses". Brinehall is about 119 miles over a mountain pass: 9 to 15 mortal days on the pace table.
- Tophouses is "about two miles down" in the release and about four in the data. That one is within the scale's precision and harmless.
- At this scale, features smaller than a mile or two are data only, so the fix is to move the pass and Old Men points (and Brinehall's travel time) in the data to match the fiction already released, or to rewrite the release before the first morning.

### Check 6. Dashes

A script scanned 178 text files under `campaigns/sim-01/`, `SPOILERS_do_not_open/campaigns/sim-01/` and `tests/creation-sim/run-01/` for U+2010 to U+2015, U+2212 and the full-width and small hyphen-minus forms. 0 hits. A second pass for spaced ASCII dashes used as connectives found only two arithmetic minus signs in the keeper log. This report was written without dashes.

### Recommended rework, in order (each needs Michael's go, since the lock forbids changes)

1. Remove the god count from `P/player/power-lean.md`.
2. Reconcile the player's release with the map near the landing (pass, Old Men, Sallow days).
3. Place the High Road markers as ruin points: at least the next marker each way from the Old Men, the ring round the lake and the Windlow line to the Shut House. Define or map "the Black Plain" and "the Westermoor". Place S9's milestone and the two Stair steadings.
4. Add the four missing costs to the event schedule.
5. Write readings, branches with answers, and "never found" for the short mysteries.
6. Rule on the Stayer's limits, the Roll's limit, the oath rule's scope and the Abiders' passage through the fall.
7. Rename or log the Vessary name echoes.
8. Fix the two NPC records that carry direction errors, and correct the release coordinates or the data for g2 and g3.
9. Correct the two keeper-log errors, record the g3 link in the other six files and log the five unlogged pairs.
10. Decide whether Year 1's true counts belong in a `P/` file before they are observed.
