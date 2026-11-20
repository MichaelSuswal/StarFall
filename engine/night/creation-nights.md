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
```

The overnight session reads the clock. `status: creation` sends it here, to the night the clock names; `status: open` sends it to `engine/night/night-turn.md`. Each night ends by setting `creation_night` to the next number; Night 3b ends by setting `year: 1`, `status: open`, `season_opens` to the player's waking season, and removing `creation_night`.

Michael starts a campaign by creating `campaigns/<name>/state/clock.md` with `creation_night: 1` and posting Day 1. From then on the days and nights run under the approved design (CLAUDE.md).

## Each night

The overnight session starts fresh and knows only the repository. It:
1. pulls, reads the clock, and confirms the day's outputs are present (below); if they are missing, it writes `years/000/night-blocked.md` saying what is missing, commits, pushes and stops, and the 6:30 wake posts a notice;
2. runs the Keeper under `engine/roles/keeper.md` and the runbook for that night, spawning the NPC god agents in parallel where the runbook calls for them, each with only its own folder and release;
3. commits and pushes after each major stage, with messages starting "Creation night N:";
4. records Pacific times in `state/timing.md`;
5. must finish before 6:30, so the DM can open the next day.

The Keeper takes clock times from `TZ=America/Los_Angeles date`, never from memory.

## Night 1: the gods, the star, the blend

- Reads from the day: `P/player/survey-day1.md`, `P/player/rejected-premises.md`.
- Does: creates the sealed folder; rolls seven gods by the rubric (folders labeled by domain, never numbered); rolls the star; each god answers the survey; blends the eight surveys into one world draft; writes follow-ups for the player.
- Leaves for Day 2: `P/player/followups-day2.md` (questions with an (oog) fallback), `P/player/world-rules.md` (what is innate and given: god-sense and bodies as set, and the magic level only as it bears on a god's build). Nothing about what was discovered, voted or pooled.

## Night 2: the gods make themselves

- Reads from the day: `P/player/power-card.md`, `appearance-card.md`, `backstory.md`, `conduct-profile.md`, `power-lean.md`, `rejected-premises.md`, `followups-day2.md` with answers.
- Does: releases the build rules to each NPC god; each god creates itself and proposes its powers; the Keeper negotiates, with reasons on both sides, in at most three rounds; Keeper traits; the common secrets file, then secret backstories and hidden powers for all eight gods, into the sealed god folders; the ruling ledger, with ids written back to the player's card for rulings settled at creation; balance on a 1 to 10 weight; the provisional placement; the Day 3 brief.
- Leaves for Day 3: `P/player/day3-brief.md` (the land as it would show itself, no names for the player's own people or home), `P/player/followups-day3.md`, `P/player/corrections.md` if anything on the player's card needs the DM's attention.

## Night 3a: the peoples and the map

- Reads from the day: `P/civs/<people>/record.md` and `state.md`, `P/player/people-meeting.md`, `hierarchy.md`, `rejected-premises.md`, `followups-day3.md` with answers, and the dated Day 3 entries on the power card and conduct profile.
- Does: each NPC god describes the people it hopes for, in its own folder; the Keeper prices edges with reasons, writes the agreed records and starting states for all eight peoples (the player's starting numbers too), and reconciles every meeting; the godless peoples; the placement plan, written first; the two painting requests (surface and clouds), sealed, plus one underground sheet only if the world has one; the paintings traced per `engine/rules/map.md`, the data following the paint; only then every description of land, written from the map data; starting map knowledge for every god.
- Ends by setting `creation_night: 3b` and running straight on.

## Night 3b: the history, the mysteries, the schedule, the lock

- Does: the deep history to the depth the surveys set, every place with a bracketed map id; the mysteries, one epic, several long, many short, each to the template; the event schedule with every mystery's cost as a clock or trigger; recurring phenomena to `S/state/phenomena.json`; the cast; the world bible; the plane section of the map (other starfalls, data only); the growth files, empty; the Year 1 inputs (`P/world/world.md`, `P/state/models.md`, `P/releases/000/dm.md`, the player's map knowledge, an empty `P/state/rolls.jsonl`).
- Then the continuity checker runs the lock (`engine/roles/checker.md`): the scripts, then the lock checklist line by line against the files. Flags go to `P/years/000/lock-flags.md`; the Keeper fixes; the checker reruns. When every line holds, the checker writes `S/LOCKED.md` with the lock commit id.
- Then the DM agent writes `P/years/001/morning-story.md` and the first painting request, and the clock is set to Year 1 open.

## What the player sees of creation

`P/player/` and `P/civs/<people>/` as the DM wrote them, the files the Keeper left for the DM, `P/world/world.md`, the first morning story and map, and nothing else. No count of gods, no vote, no pool, no history beyond what the people tell, no star, no mystery, no schedule, no hidden power. `tools/lockcheck.py <name> --leaks` enforces this before the lock.
