> SPOILER WARNING: Keeper material. Players should not read this file. It describes how the NPC gods, the hidden powers, the deep history and the mysteries are built.

# Creation runbook: the three nights

The Keeper's procedure for Nights 1, 2 and 3 of a new campaign. Each night runs after the player's day closes and must finish before the next day opens (Night 3 before 6:30am on Day 4). Read with DESIGN.md sections 3, 4 and 7, `engine/creation/*.md`, `engine/rules/powers.md`, `npc-god-rubric.md`, `survey-keeper-notes.md`, `mystery-standard.md` and `deep-lore.md`. The deep lore wins over everything built here.

Paths: `P/` is the public campaign folder `campaigns/<name>/`. `S/` is the sealed folder `SPOILERS_do_not_open/campaigns/<name>/`. Nothing in `S/` is ever released whole; agents receive only what they could know.

## Standing rules for all three nights

- Every random outcome goes through `tools/roll.py`. Run it from inside `S/` so the log lands in `S/state/rolls.jsonl`; the labels of creation rolls are spoilers and must not reach the public `P/state/rolls.jsonl`. Name every roll plainly in `--what` (which god, which table).
- Table rolls use the `roll` field of the result (1 to 100), mapped as follows. d20: ((roll - 1) mod 20) + 1. d10: ((roll - 1) mod 10) + 1. d12: reroll if roll is above 96, else ((roll - 1) mod 12) + 1. d30: reroll if roll is above 90, else ((roll - 1) mod 30) + 1. A lean is the roll itself. Company adds 25 and caps at 100. A rerolled value is logged like any other, with its reason.
- Scale blends: each god's answer placed at 1 to 10, median of the eight, then one variation roll: 1 to 33 lowers by one, 34 to 67 leaves it, 68 to 100 raises by one. Clamp to 1 to 10. Rule votes: majority of eight; a tie goes to a roll at even odds. Vote counts go in the keeper log and nowhere else.
- Every choice is logged in `S/keeper-log.md`: what was decided, from what, with which roll ids. The continuity checker verifies the world from this log later.
- Each NPC god agent runs under `engine/roles/npc-god.md` and sees only its own folder `S/gods/<god>/` plus the release written for it that night. It never sees the rubric tables, another god's folder, the deep lore, the world draft, or the player's files.
- The Keeper never speaks to the player. Anything the DM needs is written to `P/player/` in words the player may read.
- Nothing is added after the lock on Night 3. Section 5 of this file is binding.

## Night 1: seven gods, eight surveys, the first draft

Reads: `CLAUDE.md`; DESIGN.md 3, 4, 7; `engine/creation/day1-world-survey.md`; `npc-god-rubric.md`; `survey-keeper-notes.md`; `mystery-standard.md`; `deep-lore.md`; the player's Day 1 answers in `P/player/survey-day1.md`; the DM's note of any premise the player rejected, `P/player/rejected-premises.md`.

Writes: `S/gods/<god>/sheet.md` and `survey-day1.md` for seven gods; `S/releases/creation/<god>-night1.md`; `S/world-draft.md`; `S/keeper-log.md`; `S/state/rolls.jsonl`; `P/player/followups-day2.md`.

### 1.1 Create the sealed folder

- [ ] Make `S/`, `S/state/`, `S/gods/`, `S/releases/creation/`.
- [ ] Open `S/keeper-log.md` with the campaign name, the real date, and a line that Night 1 began.

### 1.2 Roll seven gods

For each god, in order, with `tools/roll.py`:

- [ ] Ten leans, each 1 to 100, in the rubric's order. Add 25 to Company and cap at 100.
- [ ] Archetype seed, d30. If any earlier god in this campaign has the same seed, reroll and log the reroll.
- [ ] Domain, d20. Reroll duplicates the same way.
- [ ] Form, d12. Virtue, d10. Flaw, d10. Wound, d12. Voice, d10.
- [ ] Give the god a Keeper label that never changes, used as its folder name: `g1-<domain>` through `g7-<domain>`. The god names itself on Night 2; the folder keeps the label.
- [ ] Write `S/gods/<god>/sheet.md`: the ten leans with both ends named, the seed's text copied from the table (the table number stays off the sheet), the domain, form, virtue, flaw, wound and voice as text, and the roll ids. Leave headings for `Traits (own)`, `Keeper trait`, `Name`, `Season it wakes into`, filled on Night 2.
- [ ] Check across the seven: no shared seed, no shared domain. Log the check.

### 1.3 Each god answers the survey

- [ ] Write `S/releases/creation/<god>-night1.md` for each god: its sheet, the survey text from `engine/creation/day1-world-survey.md`, and the instruction to answer every question from inside the character, reconciling the contradictions among its rolls rather than ignoring them, skipping what does not speak to it, and rejecting any premise it would reject. Nothing about the other gods, the deep lore, or the player.
- [ ] Spawn the seven agents in parallel, each with `engine/roles/npc-god.md` and its own release only.
- [ ] Each agent writes `S/gods/<god>/survey-day1.md`: the 19 answers, with any rejected premise marked as such and its own answer given in its place.
- [ ] Read all seven. If an answer breaks character against the sheet (a hidden god who wants to be seen with no reconciliation), send it back once with the contradiction named. Do not rewrite an agent's answer yourself.

### 1.4 Blend the eight surveys

Per `survey-keeper-notes.md`, the player's answers counting as one voice in eight. For each question, log the eight answers in summary, the blend, the roll ids, and what was built.

- [ ] Q1 feel: pool. Distill the world's tone, light, weather tendency, palette within the house style.
- [ ] Q2 land: placement wishes, one per god. List the terrain the world must contain.
- [ ] Q3 seasons: scale blend for the climate's harshness. Record each god's waking season on its sheet; the player's goes to `P/state/clock.md` on Night 3.
- [ ] Q4 past the borders: scale. Sets the share of land claimed by godless peoples.
- [ ] Q5 age of the human story: scale. Sets the depth the deep history must reach on Night 3.
- [ ] Q6 mortal magic: scale. Provisional until the star's range is rolled on Night 3 (step 3.9); if the blend falls outside the star's range, it clamps to the nearest end and the clamp is logged.
- [ ] Q7 magic's feel and cost: pool. One system, consistent with the deep lore. Minority answers may survive as local understandings, often wrong.
- [ ] Q8 how much a god stands out: scale. Feeds the ceiling roll on Night 3 and first reactions of mortals to gods.
- [ ] Q9 strangeness of the wild: scale.
- [ ] Q10 fears: pool. Candidate standing threats for the event schedule.
- [ ] Q11 scarcity: pool. One or two world scarcities; the rest local.
- [ ] Q12 buried things: pool. Every answer is a candidate site for the deep history and the short mysteries.
- [ ] Q13 non-human peoples: pool and scale.
- [ ] Q14 travelers: scale plus a pool of what they brought.
- [ ] Q15 god-sense: rule by vote.
- [ ] Q16 oaths: rule by vote.
- [ ] Bodies: rule by vote, from whatever the surveys and rejected premises say about it; if no survey speaks to it, the default is one body, logged as a default rather than a vote.
- [ ] Q17 mortals worth following: pool. Candidates for the small cast.
- [ ] Q18 discoveries: pool. Candidates for the layered mysteries and the discoverable powers.
- [ ] Q19 undared wishes: pool, handled with care. Never placed where its own god is certain to find it.
- [ ] Where an answer cannot fit the deep lore or the star, leave it out and log that it was left out.

### 1.5 Write the first world draft

- [ ] Write `S/world-draft.md`: the tone; the climate and seasons; the magic level (provisional) and how magic feels and costs; the three rules (god-sense, oaths, bodies) with their vote results kept to the log; how much gods stand out; the wild's strangeness; the terrain list and each god's placement wish; and every pool with its widespread features separated from its rare candidates.
- [ ] Mark every rare candidate as unplaced. Placement happens on Night 3.

### 1.6 Follow-ups for Day 2

- [ ] From the player's rejected premises and from gaps the blend exposed that only the player can fill, write `P/player/followups-day2.md`: few, each in a form the DM can weave into the fiction, with an (oog) fallback where the question is mechanical. No question may reveal a vote, a pool, another god, or anything from `S/`.
- [ ] For each NPC god with a gap of its own, write the follow-ups into `S/releases/creation/<god>-night1.md`, have the agent answer them into its `survey-day1.md` the same night, and blend the answers by the same rules.
- [ ] Log that Night 1 closed.

## Night 2: the gods make themselves

Reads: everything from Night 1; `engine/creation/day2-the-god.md`; `engine/rules/powers.md`; `deep-lore.md` (the origin of the gods, under its own heading); the player's Day 2 outputs written by the DM: `P/player/power-card.md`, `appearance-card.md`, `backstory.md`, `conduct-profile.md`, the DM's note of any lean in total power (`P/player/power-lean.md`), `P/player/rejected-premises.md`, and the player's answers under each question in `P/player/followups-day2.md`.

Writes: per NPC god `self.md`, `goals.md`, `record-of-gods.md`, `power-card.md`, `backstory-secret.md`, and updates to `sheet.md`; `S/player/hidden-powers.md` and `S/player/backstory-secret.md`; `S/balance.md`; `S/ruling-ledger.md`; `S/placement-draft.md`; `P/player/day3-brief.md`; `P/player/followups-day3.md`; the keeper log.

### 2.1 Release the rules to each god

- [ ] Write `S/releases/creation/<god>-night2.md`: the world's rules that bear on a god's build only (bodies, god-sense, oaths, how much a god stands out, the magic level and what magic feels like), the god's own follow-up answers, and the Day 2 checklist from `day2-the-god.md` turned toward an NPC: form, bodies, backstory outline, powers, drawbacks, edge cases, trades, what it wants, its name and what it is called. Add the two things the player's guide does not ask: its two traits (rubric section 8), and the people it hopes to lead, in a paragraph, for Night 3.
- [ ] Nothing about the other gods, the vote counts, the pools, the player, or the deep lore.

### 2.2 Each god creates itself

- [ ] Spawn the seven agents in parallel with their release and folder.
- [ ] Each writes `S/gods/<god>/self.md`: form in detail (enough for an appearance card), its two traits with the rolls they reconcile, its backstory outline as it dimly remembers it (the wound felt, never explained), what it is called and by whom, and the people it hopes to lead.
- [ ] Each writes `S/gods/<god>/goals.md`: what it wants on arrival, knowing only that it expects a people and does not know why.
- [ ] Each writes `S/gods/<god>/record-of-gods.md` with one entry: others like it exist, all new arrivals, nothing more.
- [ ] Each proposes its powers in `self.md` under `Proposed powers`: one or several, each with what it does and why this god has it.

### 2.3 Negotiate powers, god by god

Per `engine/rules/powers.md` sections 1, 3 and 6, in the format of the power card. The Keeper takes the DM's side of the Day 2 table and the NPC agent takes the player's.

- [ ] For each proposed power: price a drawback (offer choices where possible), test the main edge cases (light and dark, distance, falling, carrying, water, being watched, other gods, the god's own people), and record any trade of a weakness for an improvement.
- [ ] At most three rounds per god. The Keeper writes the final text; the agent confirms it is the power it meant. Description and Drawback freeze on confirmation.
- [ ] Write `S/gods/<god>/power-card.md`: Form (including the bodies rule and god-sense as set for this campaign), each main power with Status `main`, Limits settled at creation, empty Rulings, Trades, Growth. Ceiling reads `pending Night 3`.
- [ ] Any ruling made in negotiation that goes beyond a Limit (a dispute the Keeper settled) is the first entry in `S/ruling-ledger.md`, with both arguments.

### 2.4 Keeper traits

- [ ] For each NPC god, assign one Keeper trait: something it knows about itself from arrival that its own rolls and traits did not supply, chosen to sharpen a contradiction or to tie it to the world draft. Write it to `sheet.md` under `Keeper trait` and tell the agent in one line. The player's god gets none.

### 2.5 Hidden powers, all eight gods

- [ ] For each god, player included: one cool hidden power and one minor one, both weaker than the god's main power, each fitted to the backstory (the outline the god gave, the wound, and the secret written in 2.6). Each has a drawback and limits.
- [ ] NPC: write both on the card under `Hidden powers`, Status `hidden (undiscovered)`. The agent is not told.
- [ ] Player: write both to `S/player/hidden-powers.md` in card format. Check that `P/player/power-card.md` says only that two hidden powers exist and that its Ceiling line reads `Set by the world. Not shown.` If the DM wrote it otherwise, write the correction to `P/player/corrections.md` for the DM; do not edit the player's card yourself.
- [ ] Note for each hidden power the kind of trigger that would surface it (a place, a strain, a being met), so the night turn can recognize the moment. It is never scheduled.

### 2.6 Secret backstories

- [ ] For each god, player included, write `backstory-secret.md` (`S/gods/<god>/` or `S/player/`): the rest of the story behind the outline, tied to where the gods came from and why under the deep lore's own heading on that truth, and to the god's wound. Specific: names, places, one or two events. What the god lost and does not remember. How this past might surface in the world (a being, a mark, a word) without ever stating the mechanism (mystery standard rule 1).
- [ ] The eight secrets must be consistent with each other and with the deep lore. Where two gods' pasts touched, record it in both files and log it.
- [ ] No agent, the DM included, reads these files. The god's past reaches it only through play.

### 2.7 Balance

- [ ] Write `S/balance.md`: for each of the eight gods, a rough weight of its total power (main powers, drawbacks, trades, hidden powers), the player's lean note from the DM included.
- [ ] Adjust NPC cards before freezing where one god is far out of line, by the negotiation in 2.3, never by silent edit. Roughly equal, not exactly. If a god stays noticeably stronger, log it as a fact the world's politics will deal with (DESIGN.md 3.15).
- [ ] The player's card is never changed here. A concern about it goes to the DM through `P/player/corrections.md` as a question, not an instruction.

### 2.8 Provisional placement and the Day 3 brief

- [ ] Write `S/placement-draft.md`: each god's landing country, chosen from its Q2 wish and the terrain list, spaced evenly in rough terms. A paragraph of the deep history each land will carry, to be written in full on Night 3.
- [ ] Write `P/player/day3-brief.md` for the DM: the kind of country the player's god will land in and what that country is like, in words the player may hear. Nothing of who lives there beyond what the land itself would show, nothing of history, nothing of other gods. The DM opens Day 3 from it.

### 2.9 Follow-ups for Day 3

- [ ] Write `P/player/followups-day3.md`: few, from gaps in the player's god that bear on its people (a rejected hierarchy, a form that changes how a people could live, a power that touches its followers). Same constraints as Night 1.
- [ ] NPC gods' Day 3 questions go into their Night 3 releases.
- [ ] Log that Night 2 closed.

## Night 3: the peoples, the world, the lock

Reads: everything from Nights 1 and 2; `engine/creation/day3-the-people.md`; all of `deep-lore.md`; `mystery-standard.md`; every other file in `SPOILERS_do_not_open/keeper/`; the player's Day 3 outputs written by the DM: `P/civs/<people>/record.md` (who they are, how many, their code, skills, priced edges, magic, beliefs), `P/player/people-meeting.md` (how the god meets them, as agreed), `P/player/hierarchy.md` (or the record that it was rejected), `P/player/rejected-premises.md`, answers in `P/player/followups-day3.md`.

Writes: `S/civs/<people>/record.md` and `state.md` for seven NPC peoples; `S/civs/godless/<people>/record.md` for three to five; `S/world/map.json`, `S/world/gazetteer.md`, `S/star.md`, `S/deep-history.md`, `S/mysteries.md`, `S/event-schedule.md`, `S/state/phenomena.json`, `S/cast.md`, `S/gods/<god>/map-knowledge.json`, `S/world-bible.md`, `S/LOCKED.md`; updates to every NPC power card; `P/world/world.md`, `P/player/map-knowledge.json`, `P/state/clock.md`, `P/state/models.md`, `P/releases/000/dm.md`; the keeper log.

### 3.1 The NPC peoples

- [ ] Write `S/releases/creation/<god>-night3.md` per god: its placement (the country only, as the god will first see it), the Day 3 checklist from `day3-the-people.md` turned toward an NPC, its Day 3 follow-ups, and the rule that ordinary culture is free and every real edge is priced.
- [ ] Spawn the seven agents. Each writes `S/civs/<people>/record.md` in the shape the player's record has: who they are, how many (about 5,000 by default), their code, skills and culture, proposed edges, their magic within the star, what they believe about gods, their hierarchy or its rejection, and how the god hopes to meet them.
- [ ] Price every edge against a weakness, by negotiation as in 2.3, at most two rounds. Write the agreed record.
- [ ] Write `S/civs/<people>/state.md` with the starting numbers: population, stores, treasure, trade, strength, mood.
- [ ] Decide for each of the eight peoples how the god meets them (already there, waiting, arrived with it), reconciled with the deep history in 3.5. The player's agreed meeting is kept unless the deep history cannot hold it, in which case the smallest change that fits is made and logged, with a line for the DM in `P/player/corrections.md`.

### 3.2 Lay out the land

- [ ] Place the eight gods evenly across the region (Europe-sized at least, up to a continent), each in the country its Q2 wish and `placement-draft.md` gave it, each at least many weeks' walk from the next by the pace table. Adjust until no two are crowded and no one is isolated beyond reach.
- [ ] Draw the terrain between them so it shifts as real land does: latitude, altitude, rain shadow, rivers running downhill to a coast, borders emerging where the land changes. Every terrain on the Night 1 list appears somewhere.
- [ ] Divide the world into regions smaller than the original's, each with a general topography and a note of what entering it reveals.
- [ ] Write `S/world/map.json`: regions (id, name as the Keeper calls it, terrain, elevation, water, climate band, neighbors with travel time in days at the pace table), every settlement, ruin, road, site and underground layer that exists at creation (id, region, what it is, who knows of it), and each god's landing point. The whole world exists here from Day 1.
- [ ] Write `S/world/gazetteer.md`: the exact facts in prose, by region.

### 3.3 The godless peoples

- [ ] Three to five, their number and claimed land set by the Q4 scale. Each in `S/civs/godless/<people>/record.md`: who they are, how many, where, how they live, their code, their history in the land (tied to the deep history), what they believe about gods, what they want, and whether and how they touch the great events. Each has a real backstory whether or not it ties in.
- [ ] Give each a `state.md` like the god-led peoples. The Keeper runs them in the night turn.

### 3.4 The star

- [ ] Roll every item listed under the deep lore's `Per-star variation` heading with `tools/roll.py`, one roll per item, and write the results to `S/star.md`.
- [ ] Reconcile the Q6 magic blend with the star's range; clamp and log if needed. Update `world-draft.md`.
- [ ] Roll the secret power ceiling within the small range the deep lore gives, shaded by the Q8 scale as `survey-keeper-notes.md` directs. Write it to `S/star.md`. Fill `Ceiling` on every NPC power card and append it to `S/player/hidden-powers.md`. The number is never released.

### 3.5 The deep history

- [ ] Write `S/deep-history.md` to the depth the Q5 scale set: the rise and fall of specific cities and towns, with names, dates in years before the fall, causes and what remains of each; the roads, ruins, sealed doors and bones from the Q12 pool, each placed in `map.json`; the travelers from afar (Q14) and non-human peoples (Q13), when they came and what they brought; and individual stories, a dozen at least, of named mortals whose traces could be found. Concrete, per mystery standard rule 12. Finding any of it is hard or a matter of chance.
- [ ] Check it against the deep lore: nothing contradicts a truth, nothing explains a truth.
- [ ] Check it against every god's and people's record: each meeting is possible in this history.

### 3.6 The mysteries

Per mystery standard rule 13 and the Q18 and Q19 pools. Write `S/mysteries.md`, one section per mystery:

- [ ] One epic, threaded through the whole campaign, involving immortal power (the other gods, older beings, the politics between them), whose answer still has to be executed once found and may not be solvable by one god alone. Its central measurements can only be earned: by the god's own instrument, a counter it sent, an alliance, a place it went (rule 14). List every way they could be earned and confirm none is a scheduled visitor.
- [ ] Several long mysteries at about half the epic's span, some related to it, each with immortal stakes.
- [ ] Many short mysteries of 3 to 12 years, local and mortal, drawn from the deep history and the pools.
- [ ] For every mystery: the truth; its body (a place, a being, an event in `map.json` or the schedule); its cost if ignored and the clock or trigger that cost rides on (rule 7); its clues, each placed at a location or on a being, each showing an effect, object or behavior and never a mechanism (rule 1), each admitting more than one reading, with the readings written down (rule 2); which branches a god might act on and what the world does in answer to each, wrong branches included (rules 6 and 9); and what is never found (rule 11).
- [ ] Confirm no decisive clue is delivered by a visitor (rule 4), no counter-clue is planted (rule 2), no mortal in the record is fully right about a cause (rule 1), and that most of the world is not a clue (rule 3): the ordinary wonders of each region are listed in the gazetteer with no mystery attached.
- [ ] Confirm each undared wish that was kept is placed away from its own god's certain path.

### 3.7 The event schedule

- [ ] Write `S/event-schedule.md`. Clocked events: natural, on fixed years and seasons no one controls, each with its lead time and the signs that precede it, where those signs appear, and who could notice. Triggered events: the condition, what fires, and which clocked events it may speed, delay or redirect. The costs-if-ignored from every mystery, as clocks or triggers.
- [ ] Random events: a table with factors for `tools/roll.py`, weighted down in Years 1 to 7 by a stated step, so the opening is quiet and the distance between gods does its work.
- [ ] Recurring phenomena: name each, its true occurrences per year for at least the first ten years, written to `S/state/phenomena.json` in the shape `tools/phenomena.py` reads; the night turn runs that tool with `SPOILERS_do_not_open/campaigns/<name>` as the campaign path.
- [ ] Confirm no event herds the gods toward one place and no path or secret way exists for the plot (DESIGN.md 8.5).

### 3.8 The small cast and the world's names

- [ ] Write `S/cast.md`: a few world-level figures, mortal or otherwise, drawn from the Q17 pool and the deep history, each with nature and history fixed, placed in `map.json`. Whole peoples may count. Everyone else rises from play.
- [ ] Name the world as the Keeper knows it, and record in `S/world-bible.md` what each people calls it. Write `S/world-bible.md` as the sealed summary of the whole world: draft rules made final, star, land, peoples, cast, pointers to the deep history, mysteries and schedule.

### 3.9 Starting map knowledge

- [ ] For each god, `S/gods/<god>/map-knowledge.json` and for the player `P/player/map-knowledge.json`, in three grades: `seen` (region ids drawn exactly, usually the landing region alone), `reported` (entries with the region, the source and what was told, possibly wrong), `rumored` (faint notes, given generously). Draw the starting knowledge from what the god's people would know and tell it.
- [ ] Confirm the player's file contains no fact the god's people could not have.

### 3.10 Lock

- [ ] Run the lock checklist in section 4 below, line by line, and record each line in the keeper log with a yes.
- [ ] Write `S/LOCKED.md`: the real date and time, the campaign name, the checklist as completed, and the sentence "Nothing is added after this lock."
- [ ] Commit the whole repository as the version `creation-locked`.

### 3.11 Year 1's first morning inputs

- [ ] `P/world/world.md`: public facts only, as the player's god would know them on waking. Its land as it first sees it, its people's number and way of life, the technology level, magic as its people experience it, the season it wakes into, the land it knows and the land only rumored, and the world's name as its people say it. Nothing a god could not know, no count of gods, no history beyond what the people tell.
- [ ] `P/player/map-knowledge.json` from 3.9.
- [ ] `P/state/clock.md`: campaign, `year: 1`, `status: open`, `season_opens` set to the player's waking season from its sheet.
- [ ] `P/state/models.md`: the model for each role (keeper, npc-god, civ, checker, dm) for the night turn.
- [ ] `P/releases/000/dm.md`: the first release, everything the player's god senses and knows at the moment of landing, its bodily senses included, god-sense as set, and its people's first report, so the DM can write `P/years/001/morning-story.md` and the painting request before 6:30 per `engine/rules/morning-story.md`.
- [ ] `P/state/rolls.jsonl` begins empty. Creation rolls stay in `S/state/rolls.jsonl`.
- [ ] Log that Night 3 closed, and the time.

### Night 3 map order (binding)
1. Write the placement plan first: the gods spaced evenly, each in the terrain it asked for, realistic transitions between, the godless peoples between them, rivers, seas, ranges, the underground layers. This is a written geography, not a drawing.
2. Only then write the painting prompts from the plan (surface, each underground layer, the cloud layer) in the house style, with no text, labels, figures, buildings or borders in the paintings, and send them through images/requests/.
3. When the paintings return, trace the data onto them per engine/rules/map.md: region polygons and features in painting pixels; check every feature lands where the painting shows it; fix mismatches in the data, never by repainting.
4. Lock. Then hand the map down: the sealed whole stays with the Keeper; each civ and god agent receives its region's knowledge; the DM receives the player's map-knowledge.json and draws the first morning's map with tools/map.py.

## 4. The lock checklist

Every line must be yes before `LOCKED.md` is written.

- [ ] Seven NPC gods, no shared seed, no shared domain, each with sheet, self, goals, record-of-gods, power card (Description and Drawback frozen, two hidden powers, Ceiling filled), secret backstory, map knowledge.
- [ ] The player's god has a sealed secret backstory and two sealed hidden powers; its public card names neither and its Ceiling line is `Set by the world. Not shown.`
- [ ] Eight peoples with records and starting state. Every edge priced. Every meeting reconciled with the deep history.
- [ ] Three to five godless peoples with backstories and starting state.
- [ ] `map.json` holds every region, settlement, ruin, road, site, underground layer and landing point referred to anywhere in the deep history, mysteries, schedule or cast. Nothing anywhere points at ground the map does not have.
- [ ] Gods spaced evenly; every terrain from Night 1 present; transitions realistic.
- [ ] `star.md` holds every per-star roll and the ceiling, each with a roll id.
- [ ] One epic, several long, many short mysteries, each passing rules 1 to 14 of the mystery standard, every clue placed.
- [ ] Every event has a cause, every mystery a cost, every cost a clock or trigger. Random events weighted down for Years 1 to 7. Recurring phenomena in `phenomena.json` for at least ten years.
- [ ] Every world rule (god-sense, oaths, bodies, magic, how gods stand out) is one rule for the whole world; no wish became a local exception.
- [ ] Every creation roll is in `S/state/rolls.jsonl`; nothing rolled twice; every reroll has a reason.
- [ ] The keeper log records every blend with its eight answers, every vote count, every placement, every clamp, every leftover.
- [ ] Nothing in `P/` reveals a vote, a pool, another god, the deep history, the star, a mystery or the schedule.
- [ ] Nothing in any file contradicts the deep lore, and no file explains what the deep lore keeps mysterious.

## 5. After the lock

Nothing is added. Geography, structures, beings, secrets, clues, history and the schedule exist from the lock and change only through actors in the world during play. When play reaches something the records do not specify, the Keeper resolves it conservatively from the deep lore and deep history, writes the new fixed fact in the keeper log with the date and the action that reached it, and it is fixed forever. No clue is added to rescue a line that went quiet, no second cause is planted beside a true sighting, and no wish, theory or out-of-game remark changes what the world holds or how often it is reported.
