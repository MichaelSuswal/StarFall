> SPOILER WARNING: Keeper material. Players should not read this file. It describes how the NPC gods, the hidden powers, the deep history and the mysteries are built.

# Creation runbook: the three nights

The Keeper's procedure for Nights 1, 2 and 3 of a new campaign. Each night is a scheduled overnight session on a real night, picked by the campaign clock (`P/state/clock.md`: `status: creation`, `creation_night: N`), per `engine/night/creation-nights.md`. Each night runs after the player's day closes and finishes before the next day opens. Night 3 runs in two sittings back to back, 3a and 3b, and ends with the continuity checker's lock, all before 6:30am on Day 4.

Read with DESIGN.md sections 3, 4, 6, 7 and 11, `engine/creation/*.md`, `engine/rules/powers.md`, `engine/rules/map.md`, `npc-god-rubric.md`, `survey-keeper-notes.md`, `mystery-standard.md`, `clue-design.md` and `deep-lore.md`. The deep lore wins over everything built here.

Paths: `P/` is the public campaign folder `campaigns/<name>/`. `S/` is the sealed folder `SPOILERS_do_not_open/campaigns/<name>/`. Nothing in `S/` is ever released whole; agents receive only what they could know.

Labels: each NPC god's folder is `god-<domain word>`: the first noun of its domain, lowercase, articles dropped (`god-stone`, `god-roads`, `god-dead`). No number, no count. The order in which the gods were rolled lives in the keeper log only. The player's god has `S/player/`.

Sealed folders per god: `S/gods/<god>/` is what the god's own agent reads. `S/gods-sealed/<god>/` holds `hidden-powers.md` (with the ceiling line at its foot), `backstory-secret.md` and `growth.md`; the god's agent never receives it. The player's equivalents are in `S/player/`.

## Standing rules for all three nights

- **Permission.** Once Michael has started the campaign, these nights run under the approved design. The Keeper and every agent it spawns take this runbook and their release as the go for exactly the files named in the night's Writes list and the release, and for nothing else. Nothing here authorizes a change to the engine, the design or the files in `SPOILERS_do_not_open/keeper/`. The only image requests the nights make are the map sheets in 3a.2. A repaint needs Michael's go (3a.3).
- **Rolls.** Every random outcome goes through `tools/roll.py --who keeper --campaign <name>`, so the log lands in `S/state/rolls.jsonl` and never in the public `P/state/rolls.jsonl`. Name every roll plainly in `--what` (which god, which table, which item). The tool assigns and prints an id `r-NNNN`; cite it.
- **Table rolls** use `--die d6|d8|d10|d12|d20|d30`. The tool maps the face and makes any range reroll itself, and logs the face with no success. A lean is a plain roll (1 to 100) with no `--die`. Company adds 25 to its lean and caps at 100. A reroll for a reason the tool cannot see (a duplicate seed or domain) is a new roll with `--reason` and `--replaces r-NNNN`. A d100 table (the star's phase) is a plain roll read as 1 to 100.
- **Blends and votes** follow `survey-keeper-notes.md` exactly: placement of every answer logged before any roll, median of those who answered, a half settled by an even-odds roll, one variation roll, clamp to 1 to 10; rule votes by the counting rules there. Vote counts go in the keeper log and nowhere else.
- **Time.** Every real date and time logged is Pacific, taken from `TZ=America/Los_Angeles date` or from the commit record. Never estimate a time.
- **The keeper log** `S/keeper-log.md` records every choice: what was decided, from what, with which roll ids, in the creation log format below. The continuity checker verifies the world from it. The log is also the index: read earlier files in full only where the step in hand needs them, and their summaries in the log otherwise.
- **Agents.** The night session is the Keeper and spawns the NPC god agents. Each runs under `engine/roles/npc-god.md` and receives its own folder `S/gods/<god>/` plus the release written for it that night. It never sees `S/gods-sealed/`, the rubric tables, another god's folder, the deep lore, the world draft, the map or the player's files.
- **Releases are neutral.** Every option is offered once, in plain words, with no recommendation, no count of who took it, and no line that tells a god what is usual or easiest. Any option offered to the player at creation (on Day 2, Day 3 or in a follow-up) is offered to every NPC god on the same terms. Use the release templates in section 7.
- **The Keeper never speaks to the player.** Anything the DM needs is written to `P/player/` in words the player may read. Nothing in `P/` names a vote, a pool, another god, a count of gods, a sealed place id, a coordinate, a star value, a mystery or a scheduled event.
- **Places.** Every place named in any file under `S/` carries its bracketed map id, like `[r12]` or `[f03]`, from 3a on. Before 3a, places are named by the placement draft's working names and get ids when traced.
- **Land in words comes from the map.** No release or record describes distance, direction, line of sight or travel days except from `S/map.json` after tracing, at the pace table's rates.
- **Close of every night.** Each night ends with its close check: every file in the night's Writes list exists and is complete; a neutrality self-check (each place the Keeper could have leaned toward or against any god, and what was done instead); the night's roll range; the close time. Then commit (message `<name> Night N: closed`), push, and set `creation_night` in the clock to the next night.

### The creation log format

```
## Night N
Began <date> <time> Pacific. Read: <files>. Read in part, and why: <files>.
Found on reading: <anything that bears on tonight>.

### <step number> <step name>
<what was decided>, from <answers, files or rolls>, [r-NNNN].
Decision the files did not make: <the question>. Decided: <the ruling>. Reasons: <why>. Marked for Michael.
Paused <time> for <what>. Resumed <time>.

### Close check, Night N
Files: <each Writes item, present or not>. Rolls: r-NNNN to r-NNNN.
Neutrality: <each temptation, and what was done>.
Closed <date> <time> Pacific.
```

## Night 1: the star, seven gods, eight surveys, the first draft

Reads: `CLAUDE.md`; DESIGN.md 3, 4, 7; `engine/creation/day1-world-survey.md`; `engine/rules/powers.md`; `npc-god-rubric.md`; `survey-keeper-notes.md`; `mystery-standard.md`; `clue-design.md`; `deep-lore.md`; the player's Day 1 answers in `P/player/survey-day1.md`; the DM's note of any premise the player rejected or bent, `P/player/rejected-premises.md`.

Writes: `S/keeper-log.md`; `S/state/rolls.jsonl`; `S/star.md`; `S/gods/<god>/sheet.md` and `survey-day1.md` for seven gods; `S/releases/creation/<god>-night1.md`; `S/world-draft.md`; `P/player/world-rules.md`; `P/player/followups-day2.md`.

### 1.1 Create the sealed folder

- [ ] Make `S/`, `S/state/`, `S/gods/`, `S/gods-sealed/`, `S/player/`, `S/releases/creation/`.
- [ ] Open `S/keeper-log.md` with the campaign name, the date and time Pacific, and a line that Night 1 began.

### 1.2 Roll the star

The star comes first, before the gods and before the blend, because it bounds the magic blend, decides the center body the painting must show, and fixes everything the gods are told before Day 2.

- [ ] Roll every item under the deep lore's `Per-star variation` heading except the ceiling, one roll per item, with the die the lore gives: phase (plain roll, 1 to 100), rain density (d6), living radius (d8), center body (d6), long-game presence (d6), Remainder (d10), star content (d10), ascended temper (d6).
- [ ] Write each result to `S/star.md` with its roll id, and the magic range rain density allows, from the table in `survey-keeper-notes.md`.
- [ ] Note in the log what each result removes or requires for later nights (a rolled result that removes a body the lore names is not replaced; see 3b.2).
- [ ] The ceiling is rolled in 1.6, after the Q8 blend that shades it.

Principle from run 01 (Night 3, order of work): anything that decides what a painting must show or what a god must be told is rolled before the step that needs it. When an order of work would let a later roll change something already released, roll first and log why.

### 1.3 Roll seven gods

For each god, in order, with `tools/roll.py`:

- [ ] Ten leans, plain rolls, in the rubric's order. Company adds 25 and caps at 100.
- [ ] Archetype seed, `--die d30`. If any earlier god in this campaign has the same seed, reroll with `--reason` and `--replaces`.
- [ ] Domain, `--die d20`. Reroll duplicates the same way.
- [ ] Form `--die d12`. Virtue `--die d10`. Flaw `--die d10`. Wound `--die d12`. Voice `--die d10`.
- [ ] Label the god `god-<domain word>` (rubric section 10). The god names itself on Night 2; the folder keeps the label.
- [ ] Work out the god's bargaining stance and its people lean from its leans (rubric sections 11 and 12).
- [ ] Write `S/gods/<god>/sheet.md` in the sheet template (section 7.1).
- [ ] Check across the seven: no shared seed, no shared domain. Log the check, with the seed numbers in the log only.

### 1.4 Each god answers the survey

- [ ] Write `S/releases/creation/<god>-night1.md` from template 7.4: its sheet, the survey's opening paragraph and its 19 questions word for word from `engine/creation/day1-world-survey.md`, and nothing else from that file (its rules block speaks of the player and the sealed notes and is left out). Nothing about the other gods beyond what the survey's own words say, nothing of the deep lore, nothing of the player.
- [ ] Spawn the seven agents in parallel, each with `engine/roles/npc-god.md` and its own release only.
- [ ] Each agent writes `S/gods/<god>/survey-day1.md` in the answer format of template 7.4: all 19 numbers kept, `Skipped.` where it skips, `Premise rejected:` or `Premise bent:` before its own answer where it rejects or bends one, its waking season as the last sentence of answer 3, and no name for itself.
- [ ] Read all seven against their sheets. An answer breaks character when it contradicts the sheet with no reconciliation. Examples: a god leaning hard to hidden that wants to be seen far and wide and says nothing of the pull between the two; a god leaning hard to solitary that hopes for a crowded world of its followers with no word of why; an answer that steps outside the world to speak of the game, the player, the Keeper or other gods' answers.
- [ ] Send a broken answer back once per answer, with the contradiction named, in the god's release under `## Sent back`. The god appends its new answer under `## Answer N, given again`; the first is kept in the file. The redone answer is the one blended. Do not rewrite an agent's answer yourself.
- [ ] While a send-back is out, blend every question it does not touch, and wait for the reply before the affected question. Keep a send-back even when it would not move the blend: the file is the god's character record.
- [ ] Fill each sheet's `Season it wakes into` line from the last sentence of the god's answer 3. The Keeper writes this line; the god does not.

### 1.5 Blend the eight surveys

Per `survey-keeper-notes.md`, the player's answers counting as one voice in eight. For each question, log the eight answers in summary, the Keeper's placement of each on the scale (before any roll), the blend, the roll ids, and what was built.

- [ ] Before rolling any scale question, ask any range follow-up that question needs (1.8) and wait for the answer. A follow-up answer replaces the answer it follows.
- [ ] Q1 feel: pool. The world's tone, light, weather tendency, palette within the house style.
- [ ] Q2 land: placement wishes, one per god. List the terrain the world must contain.
- [ ] Q3 seasons: scale for the climate. Waking seasons are per god (1.4); the player's goes to the clock in 3b.6.
- [ ] Q4 past the borders: scale. Sets the share of land held by godless peoples.
- [ ] Q5 age of the human story: scale. Sets the depth the deep history must reach.
- [ ] Q6 mortal magic: scale, then bounded by the star's magic range (1.2). If the blend falls outside the range it clamps to the nearest end; log the clamp. The level is final tonight.
- [ ] Q7 magic's feel and cost: pool. One system, consistent with the deep lore. Minority answers may survive as local understandings, often wrong.
- [ ] Q8 how much a god stands out: scale. Shades the ceiling roll (1.6) and sets mortals' first reactions to gods.
- [ ] Q9 strangeness of the wild: scale.
- [ ] Q10 fears: pool. Candidate standing threats for the event schedule.
- [ ] Q11 scarcity: pool. One or two world scarcities; the rest local.
- [ ] Q12 buried things: pool. Candidate sites for the deep history and the short mysteries.
- [ ] Q13 non-human peoples: pool and scale.
- [ ] Q14 travelers: scale plus a pool of what they brought.
- [ ] Q15 god-sense: rule by vote.
- [ ] Q16 bodies: rule by vote. The bodies question feeds this vote directly. If no answer speaks to it, the default is one body, logged as a default.
- [ ] Q17 mortals worth following: pool. Candidates for the small cast.
- [ ] Q18 discoveries: pool. Candidates for the layered mysteries and the discoverable powers.
- [ ] Q19 undared wishes: pool, handled with care. Never placed where its own god is certain to find it.
- [ ] Where an answer cannot fit the deep lore or the star, leave it out and log that it was left out.

### 1.6 Roll the ceiling

- [ ] Roll the secret power ceiling, 70 plus a d10, shaded by the Q8 blend by the table in `survey-keeper-notes.md`. Write the method in the log before the first die. Write the result to `S/star.md` with its roll ids. It is copied to every god's sealed `hidden-powers.md` on Night 2 and is never released.

### 1.7 Write the first world draft

- [ ] Write `S/world-draft.md`: the tone; the climate and seasons; the star's results that bear on the land; the magic level (final) and how magic feels and costs; the two rules (god-sense, bodies), with their vote counts kept to the log; how much gods stand out; the wild's strangeness; the terrain list and each god's placement wish; every pool, its widespread features set apart from its rare candidates.
- [ ] Mark every rare candidate as unplaced. Placement happens on Night 3.

### 1.8 The world rules for the DM, and follow-ups for Day 2

- [ ] Write `P/player/world-rules.md` from template 7.9, for the DM: god-sense as set and the bodies rule as set, in words the player may read, and nothing else. Nothing that is discovered in play goes in it (the prevalence and feel of magic, how much gods stand out, the strangeness of the wild, the scarcities). It reads as a fact of being a god here, never as the result of a vote, and gives no hint that a wish was kept in part.
- [ ] Write `P/player/followups-day2.md`: few, each in a form the DM can weave into the fiction, with an (oog) fallback where the question is mechanical. A gap is only an answer the blend cannot place (a range answer that names two far points, a vote answer that fits neither side). A rejected or bent premise is a follow-up only when it leaves such a gap. An answer that asks not to be told something is honored and never becomes a follow-up. No question may reveal a vote, a pool, another god or anything from `S/`.
- [ ] For each NPC god with a gap by the same bar, write the follow-up into its release under `## Follow-up`, have the agent answer it the same night at the end of its `survey-day1.md` under `## Follow-up, answer N`, and blend by the same rules. The follow-up answer replaces the one it follows. A god with no gap gets the line `No follow-up.` in its Night 2 release.

### 1.9 Close

- [ ] Close check (standing rules). Commit `<name> Night 1: closed`, push, set `creation_night: 2`.

## Night 2: the gods make themselves

Reads: the Night 1 entries of the keeper log, and Night 1's files where a step needs them; `engine/creation/day2-the-god.md`; `engine/rules/powers.md`; `deep-lore.md` (the origin of the gods, under its own heading); `S/star.md`; the player's Day 2 outputs written by the DM: `P/player/power-card.md`, `appearance-card.md`, `backstory.md`, `conduct-profile.md`, `power-lean.md`, `rejected-premises.md`, and the player's answers in `P/player/followups-day2.md`.

Writes: per NPC god, in `S/gods/<god>/`: `self.md`, `goals.md`, `record-of-gods.md`, `negotiation-night2.md`, `power-card.md`, updates to `sheet.md`; per NPC god, in `S/gods-sealed/<god>/`: `backstory-secret.md`, `hidden-powers.md`, `growth.md`; `S/gods-sealed/common-past.md`; `S/player/backstory-secret.md`, `hidden-powers.md`, `growth.md`; `S/releases/creation/<god>-night2.md`, `<god>-night2-negotiation.md`, `<god>-day3-questions.md`; `S/balance.md`; `S/ruling-ledger.md`; `S/placement-draft.md`; `P/player/day3-brief.md`; `P/player/followups-day3.md`; ruling ids written back to `P/player/power-card.md` (2.3); the keeper log.

### 2.1 Release the rules to each god

- [ ] Write `S/releases/creation/<god>-night2.md` from template 7.5. It holds:
  - the world rules exactly as `P/player/world-rules.md` gives them to the player, and nothing else that is discovered in play (no magic level, no feel of magic, no word of how much gods stand out);
  - the facts of being a god that every god knows of itself and the DM states to the player on Day 2: no need of food, sleep a choice; it moves at its form's pace; it cannot die; the technology of the peoples it will find, in the words DESIGN 4.7 uses; every power carries a drawback; there is no set number of powers; nothing over the top;
  - the god's own follow-up answers, or `No follow-up.`;
  - its waking season;
  - every option the player was offered on Day 2 and in its follow-ups, each once, in the same terms, with no recommendation;
  - the `self.md` template (section 7.2), the `goals.md` and `record-of-gods.md` instructions, and the instruction to stop after those three files.
- [ ] Nothing about the other gods, the vote counts, the pools, the player, the star or the deep lore.

### 2.2 Each god creates itself

- [ ] Spawn the seven agents in parallel with their release and folder.
- [ ] Each writes `S/gods/<god>/self.md` in the template: name and what it is called and by whom; form in detail, with things carried; its two traits with the rolls they reconcile; its backstory outline as it dimly remembers it (the wound felt, never explained); what it wants; proposed powers, each with what it does, why this god has it, a drawback it would notice losing, and the edge cases it expects; trades; the people it hopes to lead.
- [ ] Each writes `goals.md` (what it wants on arrival, knowing only that it expects a people and does not know why) and `record-of-gods.md` with one entry: others like it came down when it did, and nothing more.
- [ ] Check all seven `self.md` files against their sheets before any pricing, as on Night 1: every section present; traits that reconcile the rolls; voice kept; the people hope within reach of the sheet's people lean, or a reason given for leaving it. Send back once per section that breaks character, the same way.
- [ ] Anything a god carries that does more than an ordinary object is a power and goes into pricing.

Principle from run 01 (Night 2, step 2.2): when gods working apart arrive at the same choice the rules do not forbid (the same name, the same image), the choice stands and neither agent is told. The Keeper accounts for it in the sealed files, and every record tells the two apart by label or byname. Nothing is changed that would tell one god something about another.

### 2.3 Negotiate powers, god by god

Per `engine/rules/powers.md` sections 1, 3 and 6, in the format of the power card. The Keeper takes the DM's side of the Day 2 table and the NPC agent takes the player's. The god's bargaining stance is the god's own; the Keeper prices the same way whatever the stance.

- [ ] First, the player's table rulings: every ruling the DM marked "settled at creation" on `P/player/power-card.md` is copied into `S/ruling-ledger.md` with an id, and the id is written back beside the ruling on the card. Nothing else on the player's card is touched.
- [ ] Round 1, in `S/releases/creation/<god>-night2-negotiation.md` under `## Round 1` (template 7.6): for each proposed power, draft card text (Description, Drawback, Limits), with choices where a price could go two ways, and the Keeper's argument for each price. The god appends `## Round 1 reply` to `S/gods/<god>/negotiation-night2.md`, with its reasons for every acceptance, refusal and counter.
- [ ] Test every power against the edge-case floor (light and dark, distance, falling, carrying, water, being watched, other gods, the god's own people), the cases this god's own powers depend on, and four more: does it touch a world scarcity; does it rule a mind; does it work on things made by more than craft; does it scale across a whole people in a year.
- [ ] A drawback is something the god would notice losing. A drawback that restates the god's voice or form costs nothing and is priced again.
- [ ] A power that reveals information (the past, things far off, what is hidden) is priced against the mystery standard: it may show effects, never mechanisms, and never a central measurement of the epic.
- [ ] A memory-loss drawback is enacted by the Keeper removing an item from the god's own record; write which record and how often into the Limits.
- [ ] An ability bought by a trade is a power with Status `main`, the trade recorded on both entries.
- [ ] Round 2, under `## Round 2`: the Keeper's counter to each reason the god gave, and the final text. The god appends `## Round 2 reply`. Round 3, if needed, is confirmation only.
- [ ] The ledger takes every request settled against the god in whole or in part, with both arguments, and every ruling that binds more than one card. When nothing qualifies, the ledger opens with the line `No disputed rulings at creation.`

### 2.4 Confirmation, Keeper traits and cards

- [ ] The confirmation round (round 2 or 3) restates every weakness and what it bought, and tells the god its Keeper trait in one line: something it knows about itself from arrival that its own rolls and traits did not supply, chosen to sharpen a contradiction on its sheet. Write the trait to `sheet.md`. The player's god gets none.
- [ ] Description and Drawback freeze on the god's confirmation, from the confirmed text.
- [ ] Write `S/gods/<god>/power-card.md` in the `powers.md` format: Form (with Definitions and Things carried, the bodies rule and god-sense as set), each main power with Status `main`, Limits settled at creation, empty Rulings, Trades, and `Growth: Possible. Not shown.`; `Hidden powers` with only the format's line that two exist; Weaknesses taken, each in full with what it bought; Ceiling `Set by the world. Not shown.`; an empty Dated entries block.

Principle from run 01 (Night 2, steps 2.3 and 2.5; Night 3, step 3.4): anything a god must not know (its hidden powers, its secret past, the ceiling, its growth) lives in a folder its agent is never given, never in a section of a file it reads and is told to skip.

### 2.5 Secret backstories, all eight

Written before the hidden powers, which must fit them.

- [ ] Write `S/gods-sealed/common-past.md` first: the far country the eight are the remainder of, under the deep lore's Truth 5, with its names, places and the events near its end, and a shared links table, one row per pair of gods whose pasts touched: the pair, what joined them, which event.
- [ ] For each god, player included, write `backstory-secret.md` (`S/gods-sealed/<god>/` or `S/player/`): the rest of the story behind the outline, tied to the common past and to the god's wound. Specific: names, places, one or two events. What the god lost and does not remember. How this past might surface in the world (a being, a mark, a word) without ever stating the mechanism (mystery standard rule 1).
- [ ] Every row of the shared links table appears in both gods' files, in the same terms, and in the log.
- [ ] Names from the common past are sealed names. If any is used again in the world on Night 3, the use is logged as a deliberate likeness, and no god's home ground carries more of them than another's.
- [ ] No agent, the DM included, reads these files. The god's past reaches it only through play.

### 2.6 Hidden powers, all eight

- [ ] For each god, player included: one cool hidden power and one minor one, both weaker than the god's main power, each fitted to its secret backstory. Each has a drawback, limits, and the kind of trigger that would surface it (a place, a strain, a being met). It is never scheduled.
- [ ] Write both to `hidden-powers.md` in card format, Status `hidden (undiscovered)`: `S/gods-sealed/<god>/` for each NPC, `S/player/` for the player. Append the ceiling line from `S/star.md` at the foot of each.
- [ ] Check that `P/player/power-card.md` says only that two hidden powers exist and that its Ceiling line reads `Set by the world. Not shown.` If the DM wrote it otherwise, write the correction to `P/player/corrections.md` for the DM; do not edit the player's card yourself.
- [ ] A hidden power fitted to the player's backstory may also serve what the player says it wants. That is allowed with narrow limits (it gives the next step, never an end or a cause), and it is flagged in the night's neutrality check.

### 2.7 Growth files

- [ ] Write `growth.md` for every god (`S/gods-sealed/<god>/`, `S/player/`), in template 7.10: one block per power, main and hidden, every field empty. The night turn fills them only when the world earns it.

### 2.8 Balance

- [ ] Write `S/balance.md`: for each of the eight gods a weight from 1 to 10 of its total power (main powers, drawbacks, trades, hidden powers), with a line of reasons, the DM's lean note for the player included.
- [ ] Where one god is far out of line, adjust its card before freezing by negotiation as in 2.3, never by silent edit. Roughly equal, not exactly. If a god stays noticeably stronger, log it as a fact the world's politics will deal with (DESIGN 3.15).
- [ ] The player's card is never changed here. A concern goes to the DM through `P/player/corrections.md` as a question.

### 2.9 Provisional placement and the Day 3 brief

- [ ] Write `S/placement-draft.md`: the region's provisional size (a continent, its rough width and height in miles), each god's landing country from its Q2 wish and the terrain list, spaced evenly in rough terms, and a paragraph of the deep history each land will carry, to be written in full in 3b.
- [ ] Write `P/player/day3-brief.md` for the DM: the kind of country the player's god will land in and what the land itself shows, in words the player may hear, and the season. No distance, compass direction or line of sight (those come from the traced map). Nothing of who lives there beyond what the land would show: smoke, walls, a worn track and grazed turf are land; who the people are, how many, what they are called, are not. Nothing of history, nothing of other gods. The placement plan in 3a must honor this brief.
- [ ] Mortal magic in the brief: only what the DM needs to price a people's magic on Day 3, in player-safe words (that mortal magic is simple, that it costs the worker, and that the Keeper fits a people's magic to the world on Night 3). Its prevalence is discovered in play and is not stated.
- [ ] The brief names the channel for what the DM cannot settle at the table: the DM lists each item in `P/player/people-meeting.md` under `## For the Keeper to reconcile`, and the Keeper answers each on Night 3.

### 2.10 Follow-ups for Day 3

- [ ] Write `P/player/followups-day3.md`: few, from gaps in the player's god that bear on its people (a rejected hierarchy, a form that changes how a people could live, a power that touches its followers). Same bar and constraints as Night 1.
- [ ] Write each NPC god's Day 3 questions to `S/releases/creation/<god>-day3-questions.md`, to go into its Night 3 release.

### 2.11 Close

- [ ] Close check. Commit `<name> Night 2: closed`, push, set `creation_night: 3`.

## Night 3a: the land and the peoples

Reads: the keeper log for Nights 1 and 2, and their files where a step needs them; `engine/creation/day3-the-people.md`; `engine/rules/map.md`; `engine/rules/time-and-pace.md`; `engine/style/house-style.md` (the map style block); `S/star.md`; `S/placement-draft.md`; `S/world-draft.md`; the player's Day 3 outputs written by the DM: `P/civs/<people>/record.md` and `state.md`, `P/player/people-meeting.md` (with its items to reconcile), `P/player/hierarchy.md`, `P/player/rejected-premises.md`, the answers in `P/player/followups-day3.md`, and dated Day 3 entries on `P/player/power-card.md`.

Writes: `S/world/placement-plan.md`; the map sheet requests in `SPOILERS_do_not_open/images/requests/`; `S/map/` (the returned sheets); `S/map.json`; `S/world/gazetteer.md`; `S/releases/creation/<god>-night3.md` and `<god>-night3-negotiation.md`; `S/gods/<god>/people-hoped.md` and `negotiation-night3.md` (by the agents); `S/civs/<people>/record.md` and `state.md` for seven NPC peoples; `S/civs/godless/<people>/record.md` and `state.md` for three to five; `S/civs/<player's people>-sealed.md`; `P/civs/<people>/state.md` (starting numbers); `S/gods/<god>/map-knowledge.json`; `P/player/map-knowledge.json`; the keeper log.

### 3a.1 The placement plan

- [ ] Write `S/world/placement-plan.md`, a written geography and not a drawing: one continent; the eight seats spaced evenly, each in the country its Q2 wish and the placement draft gave it, each many weeks' walk from the next by the pace table, none crowded and none cut off; the player's seat as its Day 3 brief described it; the godless peoples between them; rivers running downhill to a coast, seas, ranges, rain shadows, borders where the land changes; every terrain on the Night 1 list; the center body where the star's center lies.
- [ ] An underground layer exists only if the world has one (the Q12 pool, the deep lore's bodies, the star's results). If it does, the plan describes it as its own sheet under the same grid.
- [ ] The player's descriptions of its land or its past (Day 3) are wishes or its people's beliefs, never facts, until placed here or in 3b. Place them only where the world can hold them, and log each.

### 3a.2 Paint the sheets

- [ ] Write the map painting prompts from the plan, in the map style block of `engine/style/house-style.md`: the continent seen from above in the manner of a map of Middle-earth, less detail at larger scale, topography only, with no text, labels, figures, buildings, borders or grid. One surface sheet and one cloud sheet for the fog; one sheet per underground layer only if the world has one. No close-up sheets.
- [ ] Put the requests in `SPOILERS_do_not_open/images/requests/`, never in the public `images/requests/`. Log each request and its time.

### 3a.3 Trace the sheets

- [ ] When the sheets return (to `SPOILERS_do_not_open/images/out/`), place them in `S/map/` (`surface.png`, `clouds.png`, `under-N.png`) and trace the data onto them per `engine/rules/map.md` into `S/map.json`: the letter-number grid of about 16 to 20 cells (5 by 4); regions with `elevation`, `water`, `climate` and `neighbors` (each neighbor's id and travel days at the pace table); every settlement as a point, ruin, site, `road` feature and underground feature that exists at creation, each with its id, region and who knows of it; the `landings` block; the `plane` section (section 8). The whole world exists here from the lock.
- [ ] Check every feature lands where the paint shows it with a test sheet drawn from a scratch knowledge file, then delete the scratch file. Fix mismatches in the data: the data follows the paint.
- [ ] Measure from `S/map.json` and log: the distance in days between every pair of neighboring seats; that every seat sits in its wished terrain; that the player's seat matches its Day 3 brief.
- [ ] **When the paint misses the plan.** Where the paint departs from the plan, the plan yields and the seats are re-set on the painted ground. The paint misses only when it has lost a god's asked-for country altogether (no coast where a god asked for coast), the player's Day 3 country included. Then one repaint is allowed: write the corrected prompt to `SPOILERS_do_not_open/images/requests/held/`, log it as an image request awaiting Michael's go, and do not send it without that go. Until the go comes, trace on the sheet in hand; if the go comes before 3b ends, repaint once, retrace, and redo 3a.4 to 3a.8 on the new sheet. Never more than one repaint.

Principle from run 01 (Night 3, step 3.2, scale): regions are sized to what play needs, not evenly: finest around the seats, coarser between, coarsest in empty country. Anything smaller than the sheet can paint exists as data only, named and placed in `map.json` like anything painted.

Principle from run 01 (Night 3, step 3.2, location): where this runbook and a tool disagree on a path or a format, follow the tool, log the disagreement for Michael, and change neither.

### 3a.4 The NPC peoples

Only now, from the traced map, is any god told its land.

- [ ] Write `S/releases/creation/<god>-night3.md` from template 7.7: its country as the god will first see it in its waking season, written from `S/map.json` (directions, distances and sight lines measured, not guessed); what is true of the world that bears on a people, the same as the DM's Day 3 brief gave for the player; the Day 3 checklist from `day3-the-people.md` turned toward an NPC; its Day 3 questions from `S/releases/creation/<god>-day3-questions.md`; and the rule that ordinary culture is free and every real edge is priced. Every option the player was offered on Day 3 is offered once, in the same terms. Nothing suggests a size, a shape, or that a people with or without edges is usual.
- [ ] Spawn the seven agents. Each writes `S/gods/<god>/people-hoped.md` in the people record template (section 7.3): who they are, how many, how they live, their code, skills and culture, proposed edges with the weakness it offers for each, their magic, what they believe about gods, their hierarchy or its rejection, how the god hopes to meet them. The god may name its people and their home.
- [ ] Price every proposed edge against a weakness by negotiation, as in 2.3, in `S/releases/creation/<god>-night3-negotiation.md` and `S/gods/<god>/negotiation-night3.md`: round 1 draft and arguments, round 2 counter and final, round 3 confirmation at most. If the god proposed no edge, round 1 says once, as a plain fact, that no edge is required, and asks it to confirm.
- [ ] Write the agreed record to `S/civs/<people>/record.md`, every place with its map id. The world listens and does not obey: each people has a history, neighbors and a trouble its god did not ask for. Fit its magic to the world's level, the same way for every people.
- [ ] Write `S/civs/<people>/state.md` with starting numbers: population, stores, treasure, trade, strength, mood.
- [ ] Decide for each of the eight peoples how the god meets them (already there, waiting, arrived with it), reconciled with the deep history to be written in 3b. The player's agreed meeting is kept unless the history cannot hold it; then the smallest change that fits is made and logged, with a line for the DM in `P/player/corrections.md`.

### 3a.5 The player's people

- [ ] Set the starting numbers in `P/civs/<people>/state.md`, in words the player may read, if the DM left them unset.
- [ ] Answer each item under `## For the Keeper to reconcile` in `P/player/people-meeting.md`. The world's side of each answer goes in `S/civs/<people>-sealed.md`; anything the DM must change goes to `P/player/corrections.md`.
- [ ] The player names its own people and their home. The Keeper names everything else. Named mortals the player made live in `P/civs/<people>/people/`.

### 3a.6 The godless peoples

- [ ] Three to five, their number and held land set by the Q4 scale. Each in `S/civs/godless/<people>/record.md`: who they are, how many, where (with map ids), how they live, their code, their history in the land, what they believe about gods, what they want, and whether and how they touch the great events. Each has a real backstory whether or not it ties in. Each gets a `state.md`. The Keeper runs them in the night turn.

### 3a.7 Starting map knowledge

- [ ] For each god, `S/gods/<god>/map-knowledge.json`, and for the player `P/player/map-knowledge.json`, in three grades: `seen`, `reported` and `rumored`. Draw each from what the god could know at the moment of landing.
- [ ] Where no god has yet spoken to anyone at landing, each file holds only what the god sees from where it lands: the landing region `seen`, what is in view `reported` with its own sight as source. What its people know of the land is written in the people's record under `What they know of the land` and enters the god's map only when someone tells it.
- [ ] Public knowledge files carry opaque public ids and grid cells only, never sealed ids, never coordinates. A `rumored` entry carries a name as told and a grid `cell`, nothing more exact.
- [ ] Confirm the player's file holds no fact beyond the god's own reach.

Principle from run 01 (Night 3, step 3.9): a god's starting map is what it could know, not what its people know. Knowledge reaches a god only through a telling or its own senses, so a god that has met no one starts with its own eyes.

### 3a.8 Close 3a

- [ ] Every 3a Writes item present. Commit `<name> Night 3a: closed`, push. Begin 3b in the same night.

## Night 3b: the history, the mysteries, the schedule

Reads: the keeper log; `deep-lore.md` in full; `mystery-standard.md`; `clue-design.md`; `S/star.md`; `S/map.json`; `S/world/gazetteer.md`; `S/gods-sealed/common-past.md`; every people's record; the world draft.

Writes: `S/deep-history.md`; `S/mysteries.md`; `S/event-schedule.md`; `S/state/phenomena.json`; `S/cast.md`; `S/world-bible.md`; `P/world/world.md`; `P/state/clock.md`; `P/state/models.md`; `P/releases/000/dm.md`; `P/state/rolls.jsonl` (empty); additions to `S/map.json` for any place first needed here; the keeper log.

### 3b.1 The star, if not already rolled

- [ ] If any star item or the ceiling was not rolled on Night 1, roll it now as in 1.2 and 1.6, and log why it was late. Confirm `S/star.md` holds every item with its roll id.

### 3b.2 The deep history

- [ ] Write `S/deep-history.md` to the depth the Q5 scale set: the rise and fall of specific cities and towns, with names, dates in years before the arrival, causes and what remains of each; the roads, ruins, sealed doors and bones from the Q12 pool; the travelers from afar (Q14), when they came, from which entry in the plane section, and what they brought; the non-human peoples (Q13); and individual stories, a dozen at least, of named mortals whose traces could be found. Concrete, per mystery standard rule 12. Every place carries its map id; any place first needed here is added to `S/map.json` now, traced on the paint, and logged.
- [ ] Check it against the deep lore: nothing contradicts a truth, nothing explains a truth.
- [ ] Check it against every god's and people's record: each meeting is possible in this history, and each people's dates agree with it.

Principle from run 01 (Night 3, step 3.5): a body the deep lore needs for one of its truths (an older god who rose, a hoarder, carriers) may be placed in the history when the star's results and phase give it the time; it is never placed on the ground as a rival to the arriving gods. When a star result removes a body the lore names, nothing is invented to stand in for it.

### 3b.3 The mysteries

Per mystery standard rules 13, 14 and 16 and the Q18 and Q19 pools. Write `S/mysteries.md`, one section per mystery, each in the mystery template (section 7.8), every heading present.

- [ ] One epic, threaded through the whole campaign, involving immortal power, whose answer still has to be executed once found and may not be solvable by one god alone. Its central measurements can only be earned (rule 14). List every way they could be earned and confirm none is a scheduled visitor.
- [ ] Several long mysteries at about half the epic's span, some related to it, each with immortal stakes.
- [ ] Many short mysteries of 3 to 12 years, local and mortal, drawn from the deep history and the pools.
- [ ] Every clue placed at a location (with its map id) or on a being, showing an effect, object or behavior and never a mechanism, with more than one reading written. Every branch a god might act on, wrong ones included, with what the world does in answer. What is never found.
- [ ] Every being that answers questions has a written limit on what it knows and on how it may be asked (rule 16), in the mystery that uses it and in `S/cast.md`.
- [ ] Confirm no decisive clue is delivered by a visitor (rule 4), no counter-clue is planted (rule 2), no mortal in the record is fully right about a cause (rule 1), and that most of the world is not a clue (rule 3): each region's ordinary wonders are in the gazetteer with no mystery attached.
- [ ] Confirm each undared wish that was kept is placed away from its own god's certain path, with the distance from its seat.

### 3b.4 The event schedule

- [ ] Write `S/event-schedule.md`. Clocked events: natural, on fixed years and seasons no one controls, each with its lead time, the signs that precede it, where those signs appear (map ids) and who could notice. Triggered events: the condition, what fires, and which clocked events it may speed, delay or redirect. Every mystery's cost if ignored appears here as a clock or a trigger, with the mystery named.
- [ ] Random events: a table with factors for `tools/roll.py`, weighted down in Years 1 to 7 by a stated step, so the opening is quiet and the distance between gods does its work.
- [ ] Recurring phenomena: name each, its true occurrences per year for at least the first ten years, written to `S/state/phenomena.json` in the shape `tools/phenomena.py` reads; the night turn runs that tool with `SPOILERS_do_not_open/campaigns/<name>` as the campaign path.
- [ ] Confirm no event herds the gods toward one place and no path or secret way exists for the plot (DESIGN 8.5).

### 3b.5 The small cast, the names, the world bible

- [ ] Write `S/cast.md`: a few world-level figures, mortal or otherwise, drawn from the Q17 pool and the deep history, each with nature and history fixed, placed with a map id. Whole peoples may count. Everyone else rises from play.
- [ ] Name the world as the Keeper knows it, and record what each people calls it and its star.
- [ ] Write `S/world-bible.md`, the sealed summary of the whole world: the rules made final, the star, the plane, the land, the peoples, the cast, pointers to the deep history, mysteries and schedule, and where each Night 1 candidate went or why it was left out.

### 3b.6 Year 1's first morning inputs

- [ ] `P/world/world.md`: public facts only, as the player's god would know them on waking: its land as it first sees it, measured from `S/map.json`; its people's number and way of life; the technology; the season it wakes into; the land it knows and the land only rumored; the world's name as its people say it. Nothing a god could not know, no count of gods, no history beyond what the people tell, no magic level beyond what is in view.
- [ ] `P/player/map-knowledge.json` from 3a.7.
- [ ] `P/state/clock.md`: campaign, `season_opens` set to the player's waking season; `status` stays `creation` until the lock.
- [ ] `P/state/models.md`: the model for each role for the night turn. Principle from run 01 (Night 3, step 3.11): where no file names a value that is Michael's to choose, the Keeper copies the last value he approved and marks it as his to change; it never chooses one itself.
- [ ] `P/releases/000/dm.md`: everything the player's god senses and knows at the moment of landing, its bodily senses included, god-sense as set, and what is in view, with every distance, direction and sight line measured from `S/map.json`. No count of any recurring phenomenon: the DM takes counts from `tools/phenomena.py` only when the god or its people would notice. The DM writes the first morning story and painting request from it per `engine/rules/morning-story.md`.
- [ ] `P/state/rolls.jsonl` begins empty. Creation rolls stay in `S/state/rolls.jsonl`.

### 3b.7 Hand to the checker

- [ ] Commit `<name> Night 3b: ready for lock`, push, and log the commit id. Start the continuity checker on the lock checklist (section 4). The Keeper does not run the checklist on its own work.

## 4. The lock

The continuity checker runs this checklist, not the Keeper. It reads every file under `S/` and `P/` that a line names, and runs `tools/lockcheck.py` (`--places`, `--mysteries`, `--leaks`). For each line it records yes or a flag with the file and the finding. Flags go to the Keeper, which fixes them, commits, and asks for a rerun of the flagged lines, as in the night turn. When every line is yes, the checker writes `S/LOCKED.md` (template 7.11) with the commit id of the commit it checked, and commits it alone. Then the night session sets `P/state/clock.md` to `year: 1`, `status: open`, removes `creation_night`, commits, and logs that Night 3 closed, with the time. The lock is named by its commit id. No tag.

Principle from run 01 (Night 3, step 3.10): a version is named by something the record already holds, its commit id, written into the lock file; nothing depends on a name the remote may refuse.

Every line must be yes before `LOCKED.md` is written.

- [ ] Seven NPC gods, no shared seed, no shared domain, each labeled by domain with no number, each with sheet, self, goals, record-of-gods, negotiation files, power card (Description and Drawback frozen, `Hidden powers` saying only that two exist, Ceiling `Set by the world. Not shown.`), map knowledge; and in `S/gods-sealed/<god>/` a secret backstory, two hidden powers with the ceiling line, and a growth file.
- [ ] The player's god has in `S/player/` a secret backstory, two hidden powers with the ceiling line, and a growth file; its public card names neither hidden power and its Ceiling line is `Set by the world. Not shown.`; every "settled at creation" ruling on it carries a ledger id.
- [ ] Every row of the shared links table in `common-past.md` appears in both gods' backstories and in the keeper log; sealed names reused in the world are logged as likenesses and cluster near no one god.
- [ ] Eight peoples with records and starting state. Every edge priced. Every meeting reconciled with the deep history; every people's dates agree with it.
- [ ] Three to five godless peoples with backstories and starting state.
- [ ] `tools/lockcheck.py --places` passes: every bracketed id in `S/` exists in `map.json`; no warning stands for a capitalized map name without its id; every region, settlement, ruin, road, site, underground feature, landing and plane entry referred to anywhere exists in `map.json`.
- [ ] Every distance, direction and sight line in every release and record that describes land matches `map.json` at the pace table's rates; the checker measures each.
- [ ] Gods spaced evenly; every terrain from Night 1 present; transitions realistic; one continent on one sheet with the letter-number grid; underground sheets only if the world has a layer below.
- [ ] `star.md` holds every per-star roll and the ceiling, each with a roll id. The plane section holds its rolls with ids.
- [ ] `tools/lockcheck.py --mysteries` passes: one epic, several long, many short mysteries, each with every template heading filled; every clue placed with its readings; every branch with the world's answer; what is never found. Each passes rules 1 to 16 of the mystery standard. Every being that answers questions has its written limit.
- [ ] Every event has a cause, every mystery a cost, every cost a clock or trigger in the schedule. Random events weighted down for Years 1 to 7. Recurring phenomena in `phenomena.json` for at least ten years.
- [ ] Every world rule (god-sense, bodies, magic, how gods stand out) is one rule for the whole world. No wish became a local exception, and no place makes a rule read differently.
- [ ] Every creation roll is in `S/state/rolls.jsonl`; nothing rolled twice; every reroll has a reason and names the roll it replaces.
- [ ] The keeper log records every blend with its placements and eight answers, every vote count, every placement, every clamp, every leftover, every decision the files did not make.
- [ ] `tools/lockcheck.py --leaks` passes, and the checker has read every file in `P/` against this line: nothing in `P/` reveals a vote, a pool, another god, the count of gods, a sealed place id or coordinate, a star value, the deep history, a mystery, the schedule, or a phenomenon's count before it is seen.
- [ ] Nothing in any file contradicts the deep lore, and no file explains what the deep lore keeps mysterious.

## 5. After the lock

Nothing is added. Geography, structures, beings, secrets, clues, history and the schedule exist from the lock and change only through actors in the world during play. When play reaches something the records do not specify, the Keeper resolves it conservatively from the deep lore and deep history, writes the new fixed fact in the keeper log with the date and the action that reached it, and it is fixed forever. No clue is added to rescue a line that went quiet, no second cause is planted beside a true sighting, and no wish, theory or out-of-game remark changes what the world holds or how often it is reported.

## 6. Decisions the files did not make

When a step meets a question no file answers, the Keeper decides it, logs it in the creation log format with its reasons, marks it for Michael, and goes on. It never stops the night for one. A campaign's own rulings stay in its own keeper log; only the principle behind one, once Michael has seen it, comes into these standing files.

## 7. Templates

### 7.1 `sheet.md`

```
# Sheet: god-<domain word>

## Leans
1. Mind: <n> (intelligent 1, clever 100) [r-NNNN]
... all ten, both ends named, Company as "<n> (rolled <m>, +25)"

## Seed
<the seed's text from the rubric, without its table number> [r-NNNN]

## Domain, form, virtue, flaw, wound, voice
<each as text> [r-NNNN each]

## Bargaining stance
<the band and its words, from rubric section 11>

## The people it leans toward
<size band and shape words, from rubric section 12>

## Name
(Night 2)

## Traits (own)
(Night 2)

## Keeper trait
(Night 2)

## Season it wakes into
(filled by the Keeper from answer 3)
```

### 7.2 `self.md`

```
# Self: <name>

## Name
<its name, if it has one; what it is called, and by whom>

## Form
<enough for an appearance card: shape, size, face, senses, how it moves>
### Things carried
<each thing it carries; anything that does more than an ordinary object is also proposed below as a power>

## Traits
<two traits, each with the rolls it reconciles>

## Backstory outline
<who it was and what it lost, as it dimly remembers; the wound felt, never explained>

## What it wants
<on arrival, knowing only that it expects a people>

## Proposed powers
### <power name>
What it does:
Why this god has it:
Drawback (something it would notice losing):
Edge cases it expects:

## Trades
<any weakness it offers, and what it asks in return>

## The people it hopes to lead
<a paragraph>
```

### 7.3 People record (`people-hoped.md`, and the agreed `record.md`)

```
# People: <name, if the god or the people name themselves>

## Who they are
## How many
## How they live
## Their code
## Skills and culture
## Edges and their weaknesses
<each edge, the weakness that pays for it, and one measurable line once priced>
## Their magic
## What they believe about gods
## Hierarchy
<who advises, who rules under the god, how orders travel; or that the god rejected one>
## How the god meets them
## What they know of the land
<agreed record only: each place with its map id and grade of knowledge>
## Named mortals
<agreed record only: pointers to people/<name>.md>
```

### 7.4 Night 1 release, and the answer format

```
# Release: god-<domain word>, Night 1

<the sheet, as written>

You are this being. Answer the questions below from inside your character,
in your own voice. Where your rolls pull against each other, reconcile them;
that pull is where you live. Keep every number. If a question does not speak
to you, write "Skipped." If you refuse a question's premise, write
"Premise rejected:" and give your own answer. If your answer falls outside
the range a question offers, write "Premise bent:" and give it. End answer 3
with one plain sentence naming the season you wake into. Do not name
yourself tonight.

<the survey's opening paragraph and its 19 questions, word for word>
```

Answer format, `S/gods/<god>/survey-day1.md`: a heading `## Answer N` for every N from 1 to 19, then any `## Answer N, given again` and `## Follow-up, answer N` sections appended at the end.

### 7.5 Night 2 release

```
# Release: god-<domain word>, Night 2

## What is so of every god here
<the world rules as world-rules.md gives them; the facts of being a god>

## What you said, and asked
<its follow-up answers, or "No follow-up.">

## The season you wake into

## Options
<each option the player was offered, once, in the same terms, one line each>

## Make yourself
Write self.md in the form below, then goals.md, then record-of-gods.md with one
entry: others like you came down when you did. Then stop. Your powers will be
priced with you afterward; you may accept, refuse or counter any price, and you
give your reasons either way.

<the self.md template>
```

### 7.6 Negotiation round (Night 2 powers, Night 3 edges)

```
# Negotiation: god-<domain word>, Night <2|3>

## Round 1
### <power or edge>
Draft text: <Description, Drawback, Limits; or the edge and its weakness>
Choices: <where the price could go two ways, each way in full>
The Keeper's reasons: <why this price>
Accept, refuse or counter each item, and give your reasons.

## Round 2
### <power or edge>
Your reasons, answered: <the Keeper's counter to each>
Final text: <in card format>
Weaknesses and what each bought: <restated in full>
Keeper trait (Night 2 only): <one line>
Confirm that this is what you meant, or say what is wrong with it.

## Round 3 (only if needed)
<confirmation of any wording changed in round 2>
```

The god appends `## Round N reply` sections to `S/gods/<god>/negotiation-night2.md` or `negotiation-night3.md`.

### 7.7 Night 3 release

```
# Release: god-<domain word>, Night 3

## The land you come down into
<as seen in its waking season, from map.json: what is in view, how far, which way>

## What is so of the world for a people
<the same words the DM's Day 3 brief gave for the player: technology, simple
mortal magic that costs the worker, the Keeper fits each people's magic>

## Options
<each option the player was offered on Day 3, once, in the same terms>

## Questions for you
<from <god>-day3-questions.md>

## Your people
Write people-hoped.md in the form below. Ordinary culture is free. Any real
edge over other peoples is priced against a weakness you offer. You may name
your people and their home. Then stop.

<the people record template, first ten headings>
```

### 7.8 Mystery

Every mystery in `S/mysteries.md` is written in this form, every heading present, in this order. `tools/lockcheck.py --mysteries` checks the headings.

```
## <E|L|S><nn> <name>
Kind: epic | long | short. Span: <years>. Related to: <ids or none>.

### Truth
<what is so, in full>

### Body
<the place, being or event that carries it, with map ids>

### Cost if ignored
<what the world loses, and where>

### Clock or trigger
<the year or the condition, and its row in event-schedule.md>

### Clues
#### <clue name>
Location: <map id, or the being that carries it>
What is shown: <an effect, object or behavior; never a mechanism>
Readings: <every reading the evidence honestly supports, at least two>

### Branches
#### <what a god might do>
What the world does: <its answer, plainly, wrong branches included>

### Never found
<what stays unfound even by a god that solves it>
```

A being that answers questions carries, inside the Truth or Body where it appears, a line `Limit: <what it knows, what it does not, how it may be asked, how often>`.

### 7.9 `P/player/world-rules.md`

```
# What is so of every god here

For the DM, in words the player may hear. These are facts of being a god in
this world, known from the moment of landing.

## Knowing another god
<god-sense as set, plainly>

## Bodies
<how many, and the cost if more than one>
```

Nothing else goes in this file.

### 7.10 `growth.md`

```
# Growth: <god>

Kept by the Keeper. Filled only when the world earns it.

## <power name>
Trigger met (year, what):
Years practiced:
Failures (year, what):
Near misses:
Tier reached (year):
```

When an attempt opens in play, its block in the form of `engine/rules/powers.md` section 5 is added under the power it belongs to (or under `## New` for a new power), and the summary lines above are kept current from it.

### 7.11 `S/LOCKED.md`

```
# Locked: <campaign>

Locked <date> <time> Pacific, by the continuity checker.
Lock commit: <full commit id of the checked commit>

<the checklist, every line with yes and the evidence in one line>

Nothing is added after this lock.
```

## 8. The plane section

Other starfalls and stars still to fall, placed around the starting lands by roll. Data only: it is written in `S/map.json` under `plane.starfalls` in the format `engine/rules/map.md` gives, never painted, never drawn on any sheet, and never released. What any people sees of another star (a second light low on the horizon) is written in that people's record as what they see, never as the entry's values. Rolled in 3a.3, every roll logged with its id.

1. **The throw.** One entry always exists: the starfall that threw the gods here, which fell on the night they arrived (deep lore, Truth 5). Its `age_years` is 0 and it is `alive`. Its distance band is rolled with `--die d20`: 1 to 5 far, 6 to 20 very far. It is never near.
2. **How many others.** `--die d6`: 1 to 2, two others; 3 to 4, three; 5 to 6, four.
3. **Kind of each other entry.** `--die d10`: 1 to 6, a star still hanging (`alive: "not yet fallen"`); 7 to 10, a starfall.
4. **Bearing of each**, from the campaign star's center. `--die d8`: 1 north, 2 north-east, 3 east, 4 south-east, 5 south, 6 south-west, 7 west, 8 north-west.
5. **Distance band of each.** `--die d20`: 1, near; 2 to 5, far; 6 to 20, very far. Very far is the common result and near a rare one. Then the distance in years of walking within the band, `--die d10`: near is the face plus 2 (3 to 12 years); far is 10 plus the face times 9 (19 to 100 years); very far is 100 plus the face times 90 (190 to 1,000 years). Two entries may fall near each other; that is a rare result and stands.
6. **Age, for a hanging star:** `age_years` is null; its phase is a plain roll read by the deep lore's phase table (young, mature, late, falling).
7. **Age, for a starfall:** years since it fell, `--die d10`: 1 to 2, under 1,000 years; 3 to 6, 1,000 to 10,000; 7 to 10, 10,000 to 50,000. Then `--die d10` for the figure within the band: the band's start plus the face times a tenth of the band's width.
8. **Alive, for a starfall:** whether its country still holds life and peoples. Under 1,000 years, alive, no roll. 1,000 to 10,000 years, `--die d10`, 1 to 8 alive. 10,000 to 50,000 years, `--die d10`, 1 to 4 alive.

Each entry, in the `map.md` format with three added fields (`phase`, `throw`, `rolls`):

```json
{"id": "p01", "bearing": "south-west", "distance_years_walk": 460,
 "age_years": 0, "alive": true, "phase": null, "throw": true,
 "rolls": ["r-NNNN"]}
```

Travelers from afar (Q14) in the deep history come from one of these entries, named by id.
