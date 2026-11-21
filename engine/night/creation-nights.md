# The Creation Nights

How the three creation nights run in the overnight session. The Keeper's procedure, step by step, is the sealed runbook `SPOILERS_do_not_open/keeper/creation-runbook.md`; this file is the public frame: when each night runs, what it reads from the player's day, what it leaves for the next day, and who locks the world.

The campaign is `campaigns/<name>/` (P/). The sealed campaign folder is `SPOILERS_do_not_open/campaigns/<name>/` (S/).

## The clock

A campaign in creation has `state/clock.md`:

```
campaign: <name>
year: 0
status: creation
creation_night: 1
season_opens: not yet set
```

`creation_night` takes the values `1`, `2`, `3a` and `3b`.

The overnight session reads the clock. `status: creation` sends it here, to the night the clock names; `status: open` sends it to `engine/night/night-turn.md`. Each night ends by setting `creation_night` to the next number; Night 3b ends by setting `year: 1`, `status: open`, `season_opens` to the player's waking season, and removing `creation_night`.

Michael starts a campaign by creating `campaigns/<name>/state/clock.md` with `creation_night: 1` and posting Day 1. At that moment the image count for creation is settled once: the surface and cloud paintings, the first morning's painting, and an underground sheet only if the world turns out to have one (a repaint is asked for separately). From then on the days and nights run under the approved design (CLAUDE.md). A test campaign may carry `S/state/test-overrides.md` (sealed, since it names NPC results), forcing lean results for the test; the Keeper applies and logs it.

## Each night

The overnight session starts fresh and knows only the repository. It:
1. pulls, reads the clock, and confirms the day's outputs are present (below); if they are missing, it writes `years/000/night-blocked.md` saying what is missing, commits, pushes and stops, and the 6:30 wake posts a notice;
2. runs the Keeper under `engine/roles/keeper.md` and the runbook for that night, spawning the NPC god agents in parallel where the runbook calls for them, each with only its own folder and release;
3. commits and pushes after each major stage, with messages starting "Creation night N:", pulling with rebase before each push because the paint job pushes to the same branch;
4. records Pacific times in `state/timing.md` (the campaign's file is the Keeper's; a test run's own timing file is the orchestrator's);
5. must finish before 6:30, so the DM can open the next day.

The Keeper takes clock times from `TZ=America/Los_Angeles date`, never from memory.

## Night 1: the gods, the star, the blend

- Reads from the day: `P/player/survey-day1.md`, `P/player/rejected-premises.md`.
- Does: creates the sealed folder; rolls seven gods by the rubric (folders labeled by domain, never numbered; a domain matching what the player has said their god is about is rerolled), with their rule and worship leans; rolls the star; each god answers the survey; blends the eight surveys into one world draft; writes follow-ups for the player; opens `S/sealed-terms.txt`.
- Leaves for Day 2: `P/player/followups-day2.md` (questions with an (oog) fallback), `P/player/world-rules.md` (what is innate and given: god-sense and bodies as set, and the pricing terms for mortal magic, that it is simple and costs the worker, never how common it is). Nothing about what was discovered, voted or pooled.

## Night 2: the gods make themselves

- Reads from the day: `P/player/power-card.md`, `appearance-card.md`, `backstory.md`, `conduct-profile.md`, `power-lean.md`, `rejected-premises.md`, `followups-day2.md` with answers.
- Does: releases the build rules to each NPC god; each god creates itself and proposes its powers; the Keeper negotiates, with reasons on both sides, in at most three rounds; Keeper traits; the common secrets file, then secret backstories and hidden powers for all eight gods, into the sealed god folders; the ruling ledger, with ids written back to the player's card for rulings settled at creation; balance on a 1 to 10 weight; the provisional placement; the Day 3 brief.
- Leaves for Day 3: `P/player/day3-brief.md` (the land as it would show itself, no names for the player's own people or home), `P/player/followups-day3.md`, `P/player/corrections.md` if anything on the player's card needs the DM's attention.

## Night 3a: the peoples and the map

- Reads from the day: `P/civs/<people>/record.md` and `state.md`, `P/player/people-meeting.md`, `hierarchy.md`, `rejected-premises.md`, `followups-day3.md` with answers, and the dated Day 3 entries on the power card and conduct profile.
- Does: each NPC god describes the people it will lead, within its rule and worship leans and with helpers by default, in its own folder; the Keeper prices edges with reasons (skipping the round for gods that proposed none), writes the agreed records with their Helpers sections and starting states for all eight peoples (the player's starting numbers too), enters the player's Day 3 rulings in the ledger and writes the ids back, and reconciles every meeting, naming nothing the player left for play; the godless peoples; the placement plan, written first; the two painting requests (surface and clouds), sealed, plus one underground sheet only if the world has one; the paintings awaited (pull every 30 seconds, up to 20 minutes; if a painting has not returned by then, or the paint job failed, write `years/000/night-blocked.md` naming the request, commit, push and stop, and the next overnight session resumes 3a from the tracing step); the paintings traced per `engine/rules/map.md`, the data following the paint (a repaint is requested only if the paint lost a god's asked-for country, and it is made only if Michael's go arrives before 3b ends; otherwise the sheet in hand is traced); only then every description of land, written from the map data with `tools/map.py describe` after the sight rule is settled and `tools/map.py stamp` has placed every id; starting map knowledge for every god.
- Ends by setting `creation_night: 3b` and running straight on. Land descriptions released on 3a name no count of gods, and god-sense is described as direction, nearness or weight, never as a tally (DESIGN 7.2).

## Night 3b: the history, the mysteries, the schedule, the lock

- Does: the deep history to the depth the surveys set, every place with a bracketed map id; the mysteries, one epic, several long, many short, each to the template; the event schedule with every mystery's cost as a clock or trigger; recurring phenomena to `S/state/phenomena.json`; the cast; the world bible; the plane section of the map (other starfalls, data only); the growth files, empty; the Year 1 inputs (`P/world/world.md`, `P/state/models.md`, `P/releases/000/dm.md`, the player's map knowledge, an empty `P/state/rolls.jsonl`).
- Then the continuity checker runs the lock (`engine/roles/checker.md`): the scripts (`lockcheck.py --all`, not `check.py`, which is for resolved years), then the lock checklist line by line against the files. Flags go to `S/years/000/lock-flags.md`, sealed, since they name sealed things; the Keeper fixes; the checker reruns. The public `P/years/000/lock.md` says only that the lock passed and when. When every line holds, the checker writes `S/LOCKED.md` naming the commit it checked, committed alone after it.
- If the lock has not passed by 6:00, the session stops: the clock stays `status: creation`, `creation_night: 3b`, the 6:30 wake posts "(oog) The world is still being built. Day 4 will open when it is locked.", and the next overnight session resumes 3b from the open flags.
- Then the DM agent writes `P/years/001/morning-story.md` and the first morning's painting request (approved with the run's image count; a scene request not yet approved waits in `images/held/`, a map request in `SPOILERS_do_not_open/images/held/`), and draws the first map with `--zoom landing`; `tools/lockcheck.py <name> --leaks --dashes` runs once more over the public folder; and the Keeper sets the clock to Year 1 open, or to closed for a test run.

## What the player sees of creation

`P/player/` and `P/civs/<people>/` as the DM wrote them, the files the Keeper left for the DM, `P/world/world.md`, the first morning story and map, and nothing else. No count of gods, no vote, no pool, no history beyond what the people tell, no star, no mystery, no schedule, no hidden power. `tools/lockcheck.py <name> --leaks` enforces this before the lock.
