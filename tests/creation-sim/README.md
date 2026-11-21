# Creation simulation

A repeatable test of the three creation days and nights. A stand-in player agent plays Days 1 to 3 against the DM agent; the Keeper runs Nights 1 to 3 for real, under the creation runbook, in one sitting. Each run is a fresh campaign: run 01 is `campaigns/sim-01`, run 02 is `campaigns/sim-02`, and so on. A run starts only when Michael says go, and it makes exactly the image requests he approved for it (two in run 01: surface and clouds).

Per run, this folder holds:
- `stand-in.md`: the stand-in player's brief.
- `timing.md`: when each stage started and finished, Pacific, and which models ran.
- `changes.md`: the change list. Proposals only. Nothing in the engine changes until Michael approves a line. Status: proposed, approved, rejected, applied.
- `check-report.md`: the independent checker's report on the locked world, spoiler-free above its SEALED line.
- For a build made from a run: `build-plan.md` (Michael's decisions and the shared specifications) and `applied.md` (what each side changed, by item number).

Agents report process problems (unclear instructions, missing paths, contradictions) without spoilers, so the change list can be read by the player. The transcripts of the table talk live in the campaign's `player/transcript-dayN.md`.

## How a run goes

1. The orchestrator creates `campaigns/sim-NN/state/clock.md` with `status: creation` and `creation_night: 1`, and the test folder.
2. Day 1: the stand-in answers the survey; the DM closes the day.
3. Night 1: the Keeper runs the runbook. The orchestrator spawns the seven god agents for it, each with only its own folder and release, and relays the Keeper's stops.
4. Day 2 and Day 3: the DM and the stand-in talk; the orchestrator relays and appends both sides to the transcript.
5. Nights 2, 3a and 3b: as Night 1, with the negotiation rounds relayed. The continuity checker locks.
6. An independent checker reads everything and writes `check-report.md`.
7. Findings go on `changes.md`, one line each, as proposals.

## Run 01 (2026-11-18, 23:00 to 00:21 Pacific)

Campaign `sim-01`: a cairn god and the Carrowfolk. Creation ran end to end in about 1 hour 20 minutes. The checker found the world not fit to start as locked (a god-count leak, land descriptions written before tracing, underbuilt short mysteries, a self-certified lock). 100 findings; all applied in build 2 (`build-plan.md`, `applied.md`). `sim-01` stays locked as it was, as the record of the run.

## Run 03 (2026-11-20)

Campaign `sim-03`, on build 3. Every NPC god's rule lean forced to a god-king by a sealed test override; wars allowed. Three images approved: surface, clouds, first morning.
