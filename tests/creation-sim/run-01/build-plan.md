# Build 2 plan: applying the run 01 change list

Michael approved this build on 2026-11-19 (21:10 Pacific): apply all 100 items in `changes.md`, with the decisions below. No image requests. No scheduled task is created, changed or re-enabled; the new night prompt is written to `engine/night/scheduled-prompt.md` for Michael to approve separately.

## Michael's decisions

1. **Permission (9, 22).** Once Michael starts a campaign or a test run, its creation days and nights run under the approved design like the scheduled turns. An agent inside such a run takes its release or role file as the go for exactly the files it names, and nothing else. The checker reviews everything they write.
2. **Map (79, 84, 73).** One continent on one painted sheet, in the manner of a map of Middle-earth: less detail at larger scale, towns as points, topography and names only. A letter-number grid of about 16 to 20 cells (5 by 4). Three fog tiers over it (seen, reported, rumored; unknown is cloud). No close-up paintings. An underground layer exists only if the world has one; if it does, it gets its own sheet with the same grid and fog. Fix `map.md`'s small-sheet assumption.
3. **Map prompts (74).** Map painting requests go in a sealed folder, `SPOILERS_do_not_open/images/requests/`, which the paint job also reads. Scene paintings stay in `images/requests/`.
4. **Rulings (28, 48, 58, 76, 82).** The sealed-side agent reads the sim-01 keeper log's rulings and writes only the principle behind each into the Keeper files. Each campaign's own rulings stay its own.
5. **Given and discovered (6, 18, 31).** The player is never told which wishes the world kept, and nothing reads like a vote result. Innate things are given before Day 2: god-sense, bodies, and the god's own power limits. Things learned from the world are discovered in play: the prevalence and feel of magic, how much gods stand out, the strangeness of the wild, scarcities.
6. **God-sense (6, 18, 28).** Per campaign, set by the Day 1 survey. DESIGN 1.5 and 7.3 are reworded to "as set for the campaign". The sealed lore does not fix it.
7. **Oaths.** Cut as a world rule. A promise between gods is worth what the god who gave it is worth; nothing in the world enforces it or punishes breaking it. Reputation applies. Survey question 16 is replaced by the bodies question (below). The oath vote is removed from the Keeper notes and runbook.
8. **Bodies (17).** New Day 1 question 16: "Can a god be in more than one place at once? One body, or several, and if several, what is the cost?" It feeds the bodies vote on Night 1. The survey stays at 19 questions.
9. **NPC gods (47, 54, 81, 87).** Releases are neutral: options offered once, no "you may hope for fewer", no "a people with no edges is full and ordinary" before the god has proposed. Each god's rolled leans set its bargaining stance and the size and shape of people it wants (the rubric says how). A god must give reasons for what it asks, and the Keeper counter-argues, up to three rounds.
10. **Git tag (88).** `LOCKED.md` records the lock commit id. No tag.
11. **The plane.** The sealed map gets a plane section: other starfalls and stars still to fall, placed around the starting lands by roll. They are usually very far apart; a close pair is a rare roll. Data only, never painted. The deep lore must differ from both Michael's 2012 story (a star wrecks a barren spot, life and magic flow from it and dry up over tens of thousands of years, an archmage held forever in a spell binding two starfalls) and the original Telegram game.
12. **Engage rule.** The world turns only on a day the player posted in the game. At 1:30 the DM writes `player/decisions-NNN.md` only if the player posted that day. The 1:45 turn looks for that file; if it is missing, it writes a one-line "the world waited" note for the morning and stops. Reading does not count; a post does.
13. **Held encounters.** Unchanged: a year stops only when another god, a god's envoy or a world-level figure reaches the god in person.
14. **Growth (100).** A sealed growth file per god (`S/player/growth.md`; `S/gods-sealed/<god>/growth.md`), kept by the Keeper: triggers met, years practiced, failures, near misses. The night turn logs progress only when the world earns it. The player learns through what the god feels in the morning story; the public card changes only when a tier lands, as a dated entry.
15. **Creation schedule.** Nights 1 to 3 run as scheduled night sessions on real nights. The clock file carries `status: creation` and `creation_night: N`. Night 3 runs in two sittings back to back: 3a peoples and map, 3b history, mysteries and schedule. The continuity checker runs the lock checklist and writes `LOCKED.md`, not the Keeper. Day 4 is Year 1.
16. **Labels (15).** NPC god folders are `god-<domain word>`, no number. Rolling order lives in the keeper log only.

## Shared specifications (both agents and the orchestrator follow these)

- **Sealed folders per campaign (57, 100):** `S/gods/<god>/` is what the god agent reads. `S/gods-sealed/<god>/` holds `hidden-powers.md`, `backstory-secret.md`, `growth.md`, and the ceiling line; the god agent never receives it. The player's equivalents are in `S/player/`.
- **Negotiation files (45, 53):** Keeper offers in `S/releases/creation/<god>-night2-negotiation.md` and `<god>-night3-negotiation.md`, `## Round N` sections; the god appends `## Round N reply` to `S/gods/<god>/negotiation-night2.md` or `negotiation-night3.md`. Round 1 is draft card text with choices and the Keeper's arguments; the god replies with reasons; round 2 is the Keeper's counter and final text; round 3 is confirmation at most.
- **Roll ids (12, 14):** `tools/roll.py` assigns `r-NNNN` per campaign log and prints it. `--die d6|d8|d10|d12|d20|d30` returns a face with the runbook's mapping and automatic rerolls, logging `face` and no `success`. `--reason` records a reroll's reason and `--replaces r-NNNN` the roll replaced.
- **Place ids (94):** every place named in any sealed file carries a bracketed map id, like `[r12]` or `[s03]`. `tools/lockcheck.py` fails any bracketed id missing from `map.json`, and warns on any capitalized name that matches a map name but carries no id.
- **Map data (85, 86):** `map.json` regions carry `elevation`, `water`, `climate`, `neighbors` (id and travel days at the pace table), and the sheet carries `landings` and a `roads` feature type and a `plane` section. Public map-knowledge files carry opaque ids and grid cells only, never coordinates; `rumored` entries carry a name and a grid cell.
- **Leak scan (92):** `tools/lockcheck.py --leaks` builds a term list from the sealed campaign (god names and labels, the god count, place names not yet known to the player, phenomena counts, mystery and schedule names, star values) and searches `campaigns/<name>/` for them, failing on any hit.
- **Mystery template (95):** every mystery has these headings, checked by `tools/lockcheck.py --mysteries`: Truth; Body; Cost if ignored; Clock or trigger; Clues (each with location, what is shown, readings); Branches (each with what the world does); Never found. `mystery-standard.md` rule 16: every being that answers questions has a written limit on what it knows and how it can be asked.
- **Clock file:** `campaigns/<name>/state/clock.md` holds `campaign`, `year`, `status: creation|open|closed`, `creation_night: 1|2|3` while in creation, `season_opens`.
- **Engage marker:** the DM's decisions file is the marker. Its absence means the world waited; the turn writes `years/NNN/waited.md` and stops. The year does not advance.
- **Time:** every logged real time is Pacific, taken from `TZ=America/Los_Angeles date`.
- **Growth file format:** per power: `trigger met (year, what)`, `years practiced`, `failures (year, what)`, `near misses`, `tier reached (year)`.

## Assignment

- **Orchestrator (engine side):** CLAUDE.md; DESIGN.md and CHANGELIST.md; `engine/creation/*`; `engine/roles/*`; `engine/night/night-turn.md`, new `engine/night/creation-nights.md` and `engine/night/scheduled-prompt.md`; `engine/rules/powers.md`, `map.md`, `failures-checklist.md`; `engine/style/house-style.md`; the test README and stand-in brief.
- **Agent T (tools side):** `tools/roll.py`, `tools/map.py`, `tools/check.py`, `tools/paint.py`, new `tools/lockcheck.py`, `.github/workflows/paint.yml`, with self-tests under `tests/tools/`.
- **Agent K (sealed side):** every file in `SPOILERS_do_not_open/keeper/` (runbook restructure, Keeper notes tables, rubric additions, mystery standard rule 16 and template, clue design), the deep-lore comparison check, and the principles from the sim-01 rulings.

Each side logs what it changed against item numbers in `tests/creation-sim/run-01/applied.md` under its own heading.
