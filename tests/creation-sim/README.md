# Creation simulation

A repeatable test of the three creation days and nights. A stand-in player agent plays Days 1 to 3 against the DM agent; the Keeper runs Nights 1 to 3 for real, under the creation runbook, in one sitting. Each run is a fresh campaign: run 01 is `campaigns/sim-01`, run 02 is `campaigns/sim-02`, and so on. A run starts only when Michael says go, and it makes exactly the image requests he approved for it (two in run 01: surface and clouds).

Per run, this folder holds:
- `stand-in.md`: the stand-in player's brief.
- `person.md`: a short fictional person file for the stand-in, read by the DM in mirror mode as if it were the player's chat history and memory (DESIGN 3.4c). Invented for the run; no real person's details.
- `timing.md`: when each stage started and finished, Pacific, which models ran, and beside the clock times each agent's own reported duration. The agent durations are the measure: the container clock that stamps commits does not track real time and can run short (run 05 item 26). This is the orchestrator's file; the campaign's own timing file is sealed, `SPOILERS_do_not_open/campaigns/sim-NN/state/timing.md`, and nothing public in the campaign carries night or stage times (run 05 item 74).
- `changes.md`: the change list. Proposals only. Nothing in the engine changes until Michael approves a line. Status: proposed, approved, rejected, applied.
- `check-report.md`: the independent checker's report on the locked world, spoiler-free above its SEALED line.
- For a build made from a run: `build-plan.md` (Michael's decisions and the shared specifications) and `applied.md` (what each side changed, by item number).

Agents report process problems (unclear instructions, missing paths, contradictions) without spoilers, so the change list can be read by the player. The transcripts of the table talk live in the campaign's `player/transcript-dayN.md`.

## How a run goes

1. The orchestrator creates `campaigns/sim-NN/state/clock.md` as `engine/night/creation-nights.md` gives it, every line included (`campaign`, `year: 0`, `status: creation`, `creation_night: 1`, `season_opens: not yet set`), and the test folder (run 07 item 5).
2. Day 1: the stand-in answers the survey; the DM closes the day.
3. Night 1: the Keeper runs the runbook. The orchestrator spawns the seven god agents for it, each with only its own folder and release, and relays the Keeper's stops.
4. Day 2 and Day 3: the DM and the stand-in talk; the orchestrator relays and appends both sides to the transcript.
5. Nights 2, 3a and 3b: as Night 1, with the negotiation rounds relayed. The continuity checker locks. Any ruling Michael gives in chat during the run is written by the orchestrator, and only by it, to the campaign's sealed `rulings.md`, quoted with the Pacific time and the question he answered. Nothing in the run pauses for him: a ruling the files do not settle is made by the Keeper, or by the checker at the lock, by the judgment order and logged for review, as in a real campaign (DESIGN 2.7a). The one exception is a ruling Michael has asked, before or during the run, to make himself.
6. An independent checker reads everything and writes `check-report.md`.
7. Findings go on `changes.md`, one line each, as proposals.

## Setting up the next run

- The stand-in brief names a different kind of player each run (a builder, a conqueror or a trader), keeping Michael's style only in how it plays the table (run 04 item 1).
- One NPC god may be given a forced lean that invites refusal (of helpers, or of the default size), by the sealed test override, so refusal pricing runs for an NPC as well as the player (run 04 item 37).
- The stand-in gets a `person.md` and may choose either mode at the Day 1 question.
- The orchestrator pulls once with `git pull --rebase --autostash` before it spawns agents in parallel, and the parallel agents do not pull, since pulls at once in one working tree fail ("Cannot rebase onto multiple branches", run 06 item 88). An agent that runs alone may pull. God and civ agents write their files and do not commit; the orchestrator commits them (run 05 item 36).

## Run 01 (2026-11-18, 23:00 to 00:21 Pacific)

Campaign `sim-01`: a cairn god and the Carrowfolk. Creation ran end to end in about 1 hour 20 minutes. The checker found the world not fit to start as locked (a god-count leak, land descriptions written before tracing, underbuilt short mysteries, a self-certified lock). 100 findings; all applied in build 2 (`build-plan.md`, `applied.md`). `sim-01` stays locked as it was, as the record of the run.

## Run 03 (2026-11-20)

Campaign `sim-03`, on build 3. Every NPC god's rule lean forced to a god-king by a sealed test override; wars allowed. Three images approved: surface, clouds, first morning. Ran 2026-11-20 22:01 to 2026-11-21 20:53 Pacific, with a pause on a usage limit and a pause for Michael's ruling on the leak scan. A mycelial god and an unnamed woodland people. Locked in four rounds; clock closed. Findings in `run-03/changes.md`. Build 4 applies them (`run-03/build-plan.md`, `run-03/applied.md`); run 04 waits for Michael's go.

## Run 04 (2026-11-21)

Campaign `sim-04`, on build 4. No test override. Three images approved: surface, clouds, first morning. Ran 2026-11-21 22:50 to 2026-11-22 21:22 Pacific, with pauses on a usage limit and for Michael's ruling on the leak scan. A swarm god and the Sallowfolk, a smaller people with no helpers. Locked in three rounds; clock closed. Findings in `run-04/changes.md`.

## Run 05 (2026-11-23)

Campaign `sim-05`, on build 5. Test override: the first NPC god rolled is a lone god that refuses its helpers. Stand-in plays a conqueror, mirror mode on with `person.md`. Three images approved: surface, clouds, first morning.

## Run 06 (2026-11-24)

Campaign `sim-06`, on build 6. No test override. Stand-in plays a trader, standard mode. Three creation images approved (surface, clouds, first morning) and three play-year mornings (Years 2 to 4). After creation, a 3-year play test in the same world: one play day and one night turn per year.

## Run 07 (2026-11-25 to 2026-11-26)

The short check of build 7 (`run-07/plan.md`). Part A: a fresh campaign `sim-07`, Day 1 and Night 1 only, for the waking vote; then closed. Part B: `sim-06` reopened at Year 4 under build 7, with a setup pass, two play days and two night turns, for live scenes and held moments; then closed. No paintings. 30 findings in `run-07/changes.md`, with Michael's decisions of 2026-11-27 (the clock waits until the story catches up; a play-year morning approved only by the line naming its year; travel priced in the direction travelled). Build 8, StarFall 1.0, applies them (`run-07/build-plan.md`, `run-07/applied.md`).
