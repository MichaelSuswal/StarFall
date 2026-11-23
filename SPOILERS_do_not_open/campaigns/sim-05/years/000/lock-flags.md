> SPOILER WARNING. Sealed. Lock flags for campaign sim-05. Players must never read this file.

# Lock flags: sim-05, round 1

Run by the continuity checker, 2026-11-23, from 10:26 to 14:58 Pacific (the run was paused for a usage limit between the two; nothing in either campaign folder changed in the pause), against the Keeper's ready-for-lock commit 2ceab7f8ed9eb073859d0de62ae92fbc7f9aa5fd as it stands at 5d2e063 (the keeper log line naming the ready-for-lock id; nothing else in either campaign folder differs; the later commit 72adb94 touches only `tests/`). There is no `S/rulings.md`: no in-run ruling of Michael's stands. Every line of the lock checklist (runbook section 4) was checked against the files, not against the keeper log. Every travel line with a route and means in the sealed records, the world bible and the Carrow's knowledge was rerun through `tools/map.py travel`; every god's view was rerun with `tools/map.py describe --landing` for all eight and compared, by id, with all eight knowledge files and the landing releases; the spacing was measured from the `landings` block; the star's bearing and height word in each landing view was measured from the center point [f65].

Result: 2 flags, on 2 of the 18 lines, both the Keeper's to fix in files it owns. No `S/leak-allow.txt` is needed (no leak hit). No `LOCKED.md` is written. The public `P/years/000/lock.md` reads flagged.

## Script output

```
tools/lockcheck.py sim-05 --all
WARN places: SPOILERS_do_not_open/campaigns/sim-05/keeper-log.md: map name "capped spring" written in lower case 5 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/keeper-log.md: map name "hill road" written in lower case 2 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/keeper-log.md: map name "roofless hall" written in lower case 2 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/placement-draft.md: map name "capped spring" written in lower case 1 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/world-draft.md: map name "capped spring" written in lower case 2 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/world-draft.md: map name "roofless hall" written in lower case 1 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/civs/fordfolk/record.md: map name "hill road" written in lower case 1 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/gods/god-fate/negotiation-night2.md: map name "old tollhouse" written in lower case 1 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/gods/god-roads/people-hoped.md: map name "hill road" written in lower case 1 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/world/placement-plan.md: map name "capped spring" written in lower case 2 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/world/placement-plan.md: map name "cold sea" written in lower case 2 time(s) with no id
WARN places: SPOILERS_do_not_open/campaigns/sim-05/world/placement-plan.md: map name "roofless hall" written in lower case 1 time(s) with no id
places: 0 failure(s), 12 warning(s)
leaks: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-05
continent: 26 land region(s), narrowest about 811 miles across (north to south), average about 956 miles, widest about 1,046; east to west 916, north to south 813 miles
0 problem(s), 0 warning(s)
```

## The known items, judged

- **The 12 place warnings.** Each was read in its sentence. Every one is an ordinary lower-case description written before tracing or in a god's own words, not a reference to a map name without its id: the Night 1 pools and underground decision in the log, the world draft, the placement draft and plan ("a capped spring", "a roofless hall with the weather for its ceiling", "a narrower cold sea"); `god-fate`'s "the old tollhouse bargains I expect to find"; `god-roads`'s own hope and the Fordfolk record copying it ("the hill road"); the 3a.5 log line "the hill road west of the crossing". None is capitalized. No flag.
- **The sealed factor's name in `god-fate`'s own files.** `gods/god-fate/survey-day1.md` 21 ("a year of luck") and `gods/god-fate/self.md` 34 and 35 ("It is a creditor of luck") are the god's own words, from its own Day 1 answer, in its own sealed folder. They name a thing a mortal might pay, not the mechanic, and nothing the Keeper wrote put the word there; the card and negotiation say "chance" and "fortune" (log 2.2, 2.3). No public file, release, card or sheet holds it. Ruled under "Rulings for review". No flag, and no allow line (none could clear a `!` term, and none is needed: the scan reads `P/` only).
- **The player's sealed answers that are requests.** Ruled under "Rulings for review". No flag.
- **The overrule of DM rolls.** Sealed-factors check 5 holds vacuously: `P/state/rolls.jsonl` is empty, no DM roll exists, none was overruled, and the keeper log says so (3b close). No flag.

## The checklist, line by line

1. Seven NPC gods. Yes. Seven folders labeled by domain (rivers, roads, sea, fate, beasts, harvest, storms), no number; seeds 14, 5, 30, 18, 22, 21, 23 and domains 17, 5, 7, 20, 11, 2, 8, none shared (rerolls r-0129 to r-0133 each name their reason and the roll replaced). Each folder holds sheet, self, goals, record-of-gods, Night 2 negotiation (no Night 3 file: no edge proposed, log 3a.1), power card and map knowledge; each landing release is in `S/releases/000/`. Each card: Description and Drawback as confirmed, `Hidden powers` saying only that two exist, Ceiling `Set by the world. Not shown.` Each sealed folder: secret backstory, two hidden powers and two or three knacks (rivers 3, roads 2, sea 3, fate 2, beasts 3, harvest 2, storms 2), each knack with its Limit, its "Shows when" line and Status `knack (undiscovered)`, the ceiling line (80), and a growth file. `balance.md`'s second weights count the knacks. No hidden power or knack name stands in any god's own folder, any release, any people's record or any public file, and every one is on `sealed-terms.txt` (checked by script, name by name).
2. The player's god. Yes. `S/player/` holds the secret backstory, two hidden powers and three knacks drawn from `mirror.md` (lines 1, 4, 5, 6, 7; line 10 left out as possibly sensitive), the ceiling line, and the growth file. `P/civs/carrow/knowledge.md` gives names and grid cells and no map id. The card names neither hidden power; its Ceiling line is as required; every "Settled at creation" mark carries a ledger id (L-0001 to L-0006, L-0009 to L-0011, L-0036 to L-0039). Note, not a flag: `P/civs/carrow/record.md` 40 and 41 and `P/player/rejected-premises.md` still read "Ledger: pending, Night 3", and three card Limits still end "Provisional, for the Keeper"; the ids and confirmations (L-0007, L-0008, L-0037 to L-0039) are in `P/player/corrections.md` for the DM, as the DM-owned rule requires.
3. Shared links. Yes. All ten rows of the table in `common-past.md` stand word for word in both named backstories (checked by script) and are summarized in the keeper log (2.5). No common-past name is used in the world (log 3b.4); the likenesses logged there (a door with a chain behind it, a door with terms, a great granary, a harbor under a harbor, a shut spring) each sit near the god whose own Night 1 answer asked for it and near no one god as a group.
4. Eight peoples. Yes. Seven NPC records with states, and the player's public record, state and sealed side; every one has `## Helpers` (offices under the people's own law, or for `god-rivers` the refusal of 2026-11-23 with its reasons and cost). No edge was proposed by any god or the player, so none was priced and no size was priced. Every NPC people is inside its god's rule and worship leans (log 3a.1). Every meeting is "already there, did not know its god", and each is possible in `deep-history.md`; the dates agree (spot-checked against the history: the Carrow about 310 BA against their own three hundred years; Kes Orvan about 240 BA; Kellgarth about 700 BA, the Askeld's "five hundred years" a telling held wrong; Orrenmark's walls 1,100 BA; Saltgate's wall 1,250 BA; Threeways from about 500 BA). Nothing the player left unnamed is named: the five office holders stay filed by office everywhere.
5. Godless peoples. Yes. Four (the Varrun, the Ilwe, the Meldrin, the Vessari), each with record, history in outline and depth on 3b, and state.
6. Places. Yes. `--places` 0 failures; the 12 warnings are ruled above; `map.py validate` 0 problems; Lastlanding [f72], first needed on 3b, is in `map.json`, the gazetteer and the Orvanni's land list.
7. Distances, directions, sight lines, travel. Flag 2. Otherwise yes: every other travel line in the records (31 lines) matches `tools/map.py travel` for the route and means it names, to the tenth; the Carrow's knowledge (the gate 17 miles and a short day by the road, Threeways 10 days on foot and 20 by wagon by the road, Meldry nearly three weeks and the horse-herders three weeks over open ground, the chief hold about a week above the gate) agrees with the sealed side and the tool; the undared-wish distances and the Fallen Stone's 59.7 miles from Kes Orvan [f21] agree. `P/world/world.md`, `P/releases/000/dm.md` and all seven landing releases agree with `describe --landing` line for line, and all eight knowledge files hold exactly the ids the tool puts in view. The blue star's direction in each of the eight views is the bearing to the center point [f65] (player south at 347 miles, rivers south-west 351, roads south-east 200, sea west 432, fate west 284, beasts north-east 189, harvest north-west 280, storms south-east 480), and "high" or "well up" follows the 300-mile reading in every case.
8. Spacing, terrains, one sheet, underground. Yes. Each landing's nearest neighbor lies 164 to 294 miles off; the shortest is 0.56 of the longest, above the half the rule asks. Every Night 1 terrain is on the sheet (great rivers with springs, a braided river, fords, flood plain, high plain, steppe, hill country, mountains with ice and passes, grassland at a forest edge, marsh, coasts with harbors, sea). One continent on one sheet, 5 by 4 grid, about 811 miles at its narrowest and 956 on average. The underground layer `under-1` stands in `map.json`, as the Night 1 decision, the history and the plan give it (hollows only), `validate` passes it, and no underground sheet exists (none approved; the house style paints no layer of hollows).
9. Luck. Yes. `S/state/luck.md` has a line for all eight (`god-roads` +1, every other 0, the player under `player`), each with dated history lines and reasons matching the log (2.4, 3a.1), within 0 to +5. The three pass-one weightings (r-0196, r-0197, r-0198) name the sealed factor and its step in `--what` before the roll, with the even share and the share rolled; the second casts (r-0199 to r-0201) and r-0202 choose evenly; the two-cast method gives the lucky people exactly the even share less five and the rest equal shares, which is the rule's own arithmetic. No word of the mechanic is in any file the player, the DM, an NPC god agent or a civ agent reads, save the god's own words ruled above and "the unlucky" in `engine/rules/time-and-pace.md` 71, an ordinary word in a pace table that reveals nothing, as the sim-04 lock read it (ruled under "Rulings for review").
10. Star and plane. Yes. `star.md` holds every per-star roll and the ceiling (r-0001 to r-0008, r-0142, r-0143). The plane's four entries match r-0146 to r-0164 face by face, with `count_roll` r-0149; p01, the throw, north, 1,000 years' walk, age 0, agrees with the common past.
11. Mysteries. Flag 1. Otherwise yes: the script passes; one epic, four long (30 years, half the epic's 60), eight short (3 to 8 years) by their `Kind:` lines; every clue has a location with an id or a being and two or more readings; every branch has the world's answer, wrong branches and restraint among them; every `Never found` is filled; the four `Limit:` lines stand word for word in `cast.md` (checked by script). No clue states a mechanism. No decisive clue comes by a visitor: the Venn carry names and no measure, and the epic's measurements are earned only by marks, counters, an alliance, or going. No mortal is fully right about a cause (Orrick is wrong that the star is a lamp; the eldest teacher about who did the saying; each people's telling wrong where it explains). Every cost check names the card lines and ledger ids it read and contradicts none.
12. Causes, costs, clocks, weighting, phenomena. Yes. Every mystery's cost is a schedule row naming it (the schedule's own check line, verified row by row); every rolled year carries its roll; random events at base 30 with "the quiet opening=-20" in Years 1 to 7; `phenomena.json` holds the dim nights for Years 1 to 12, read by `tools/phenomena.py`; the only other recurring things in the sealed files are customs (the twice-yearly trade, the autumn gathering) and ordinary wonders with nothing to count. No event herds the gods; no road or way was laid for a plot.
13. God-sense. Yes. Nothing at a distance, a knowing that comes by nearness in a meeting, never a tally, in `P/player/world-rules.md`, the player's card, every NPC card, the DM release and every landing release.
14. One rule for the whole world. Yes. One body; god-sense as above; magic at one rate for every people (about one worker in six hundred), the school a gathering and not a local rule.
15. Rolls. Yes. Script passes; r-0001 to r-0202, no id twice; the tool's own void draws (r-0024, r-0178) are replaced by its rerolls; every other reroll names its reason and the roll replaced. `P/state/rolls.jsonl` is empty.
16. The keeper log. Yes. Every blend with its placements and eight answers, every tie decided before its variation roll, the vote counts (Q15, Q16), every clamp (Q5, Q6 by the star), every placement, every leftover, and every decision the files did not make with its reasons, listed for review night by night.
17. Sealed terms and leaks. Yes. `S/sealed-terms.txt` holds every god name and byname, every hidden power and knack name, every common-past name, the peoples' and mortals' names, the 3b names in the history and cast, the other peoples' names for the world and star, and `!luck` and `!Luck`; the Carrow's two names for the world and star were never listed, made public in the same commit, logged. `--leaks` passes with no allow file. By reading every non-transcript file in `P/` and scanning the transcripts: nothing reveals a vote, a pool, another god, a count of gods in any wording, a sealed place id or coordinate, a star value, the deep history, a mystery, the schedule or a phenomenon's count. The carters' story of hills like a sleeping beast in the Carrow's knowledge is what the downs look like, no name and no cause.
18. Deep lore. Yes. The star's results hold (the hoarder a beast in plain shape at the center; carriers; no thinners and nothing in their place; the Remainder in godless country; no measurable descent); the earlier gods all rose before the arrival and none is on the ground; nothing explains what the lore keeps mysterious. The lore's "a stone fell in the hills" is its test world's shape; here it fell on the steppe by the placement roll (r-0144, r-0145), which the runbook gives.

## Flags

### Flag 1. Line 11, the mystery template: three mysteries say no being answers questions while one does in them, and one gives a being without its limit
Rule: `mystery-standard.md`, "Writing a mystery down": "Every mystery carries one `Answers questions: yes|no` line ... `yes` when any being in it answers questions. On `yes`, its rule 16 limit is a `Limit:` line in the Truth or Body where the being appears"; rule 16; lock line 11.
Where, in `S/mysteries.md`:
- E01 (line 9, `no`): its Truth (line 14) makes the rolls of Meldry [f27] a way to earn the epic's measurements, and its clue "The dream on the downs" is a dream on a dim night within a day's walk of the Brow, where the voices in the star speak (L02's own Limit). Both answer questions (L02, `yes`). The cast already lists both under E01.
- L01 (line 97, `no`): the Venn appear in its clue "The singers will not sing there"; the cast lists them under L01.
- S06 (line 568, `no`): its Truth and its branch "The god searches the rolls at Meldry" rest on the rolls of Meldry [f27]; the cast lists them under S06.
- L03 (line 230, `yes`): its clue "The same names behind the door" has the Doorward saying names aloud, and her Limit stands only in L04 and the cast.
What it matters for: a Keeper resolving E01 or S06 from the mystery reads no limit on how fast the rolls give up a reign or a payment (one roll a day, no index), and none on the voices near the Brow, though both bear on how the epic's measurements are earned. The fix is in the Keeper's own file: set `Answers questions: yes` in E01, L01 and S06, and copy into the Truth or Body of E01 (voices, rolls), L01 (Venn), S06 (rolls) and L03 (Doorward) the `Limit:` line of each being word for word from `cast.md`; rerun `--mysteries`.

### Flag 2. Line 7, travel: one Ferrow land line does not match the tool
Rule: lock line 7; runbook standing rule "Travel by route and means" (the Keeper copies the tool's days and never works them by hand).
Where: `S/civs/ferrow/record.md` 76: "by boat from the First Ford [f67] down the Tessen [f07] and the Meld [f04] to Meldry [f27], 279.3 miles, 9.3 days downstream; back up, 23.3 days."
What the tool gives for that route and means: `tools/map.py travel sim-05 f67 f27 --by boat --via f07,f04`, 278.6 miles, 9.3 days; back up, `f27 f67 --by boat --via f04,f07`, 278.8 miles, 23.2 days. The fix is to copy those figures into the line, logged. Every other travel line in every record matches.

## Notes, not flags

- `Tessaly Vaun` (the Doorward) reuses as a first name a common-past name of campaign sim-04. Within sim-05 it is a sealed term on the list and names nothing of this campaign's common past, so nothing leaks; logged only so that the review can see a name came from another campaign's files.
- `P/years/001/` does not exist yet, as it should not before 4.1.

## Rulings for review

- The sealed factor's name in an NPC god's own files (`god-fate`, survey answer and `self.md`, its own Day 1 words). Ruled: not a leak and no flag. Reasons, by the judgment order: fair to the god's own intent, which is a price a mortal pays and not the mechanic; it is the same reason the player's transcripts are not scanned (an agent using an ordinary word reveals nothing); and nothing the Keeper wrote carries it. Sealed-factors check 4 still binds every release, card and sheet, which are clean. To watch in play: whatever `god-fate` writes that reaches a public file or a morning story is scanned as usual.
- "the unlucky" in `engine/rules/time-and-pace.md` 71. Ruled: an ordinary word in an engine pace table, revealing nothing, as sim-04's lock read it; no flag. Rewording it is an engine change and needs Michael's go; it is listed here for him.
- The player's sealed answers that are requests, honored without a dated confirmation (L-0012, the worn stake and the return's roll; L-0013, what it asked not to be told at the table; the fifth answer's request about who tells the lost name, log 3b.5). Ruled: they stand. Reasons: the three-year confirmation rule governs wants applied in fitting and standing conduct; these are requests to the Keeper about the table and about how a ruled price is taken, which DESIGN 3.4 honors as asked, and each puts nothing in the god's path and gives it no advantage (the stake is a possession and not a memory item in any case; the name stands only in the Venn's list, as far from the god as from any). The wants among the six (the first, the fourth, the wish half of the fifth) were fitted nowhere, and the sixth's held line stands held. Sealed ledger entries drawn from `unsaid.md` are allowed: the ledger takes every ruling made at creation, and the sealed ledger is the place for a ruling whose ground is sealed.
- Mystery standard rule 1 and the short mortal mysteries (S01 the Master Drover, S02 the apprentice). Ruled: a mortal who did a thing knowing what he did is not a mortal explaining a cause; each is still wrong about something important (the Drover's expectation of the rite's keeper; the apprentice that he did right). No flag.
- The pending ledger marks and provisional card lines in DM-owned files. Ruled: notes for the DM through `corrections.md`, not lock flags, since the card's own marks all carry ids and the DM-owned rule forbids the Keeper's edit.

## For the rerun

Both flags are the Keeper's, in files it owns (`S/mysteries.md`, `S/civs/ferrow/record.md`, and its log). No line needs `P/player/corrections.md`. On the rerun the checker reruns both scripts, reads every line the fix touches, compares the copied `Limit:` lines with `cast.md` word for word, reruns the Ferrow line through the tool, and rechecks lines 7 and 11.

# Lock flags: sim-05, round 2

Run by the continuity checker, 2026-11-23, from 15:00 to 15:01 Pacific, against the Keeper's fix commit 13f1ec338215bbdf39e617be12ac91e20e4da70a (`Creation night 3b: sim-05 lock flags fixed, round 1`). There is still no `S/rulings.md`. Both scripts were rerun; every line the fix touches was read; the copied `Limit:` lines were compared with `cast.md` by script; the Ferrow line was rerun through the tool; lines 7, 11 and 17 were checked again, and every file the commit changed was read in full for its diff.

Result: 1 flag open (flag 3, new, the Keeper's). Flags 1 and 2 are resolved. The lock does not pass. No `LOCKED.md` is written. The public `P/years/000/lock.md` reads flagged.

## Script output

```
tools/lockcheck.py sim-05 --all
(the same 12 place warnings as round 1, ruled there)
places: 0 failure(s), 12 warning(s)
leaks: 0 failure(s), 0 warning(s)
mysteries: 0 failure(s), 0 warning(s)
rolls: 0 failure(s), 0 warning(s)
dashes: 0 failure(s), 0 warning(s)

tools/map.py validate sim-05
0 problem(s), 0 warning(s)
```

## Round 1 flags

- Flag 1, resolved. E01, L01 and S06 now say `Answers questions: yes`; E01 carries the limits of the voices, the rolls of Meldry [f27] and the Venn, L01 the Venn's, S06 the rolls', and L03 now also the Doorward's. All ten `Limit:` lines in `mysteries.md` stand word for word in `cast.md` (by script), and the cast's line for the Venn now names E01. By reading, the answering beings stand only in E01, L01, L02, L03, L04 and S06, each with every limit it needs; S01 to S05, S07 and S08 hold none. No truth, clue, branch or cost changed. Note, not a flag: the keeper log says the lines were put in each Truth; they stand in each Body, which the standard equally allows.
- Flag 2, resolved. `S/civs/ferrow/record.md` 76 now reads 278.6 miles, 9.3 days down and 278.8 miles, 23.2 days up, as `tools/map.py travel` prints for the route and means named.

## Flag 3. Line 17, the public folder: the timing file names a round of the lock by its ordinal

Rule: runbook standing rules, "Close of every night": "`P/state/timing.md` is public: it carries stages and times only, each stage named by what was written ..., never by an ordinal or a count, with no per-god line and no count of agents, gods, rolls or rounds"; lock line 17 (the checker reads every file in `P/`).
Where: `campaigns/sim-05/state/timing.md` 39, added in 13f1ec3: "- lock flags fixed, round 1: 15:00".
What the record should hold instead: the stage named by what was written, with no round number, for example "- lock flags fixed: 15:00". The file is the Keeper's own (it writes the campaign's timing file), so the fix is the Keeper's, logged; no other public file carries a round number (`P/years/000/lock.md` reads flagged with the time only).

## For the rerun

Flag 3 is the Keeper's. On the rerun the checker reruns both scripts, reads `P/state/timing.md` and every other file the fix touches, and checks line 17 again.
