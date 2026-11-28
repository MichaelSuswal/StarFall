# Build 8 plan: 1.0

Michael approved this build on 2026-11-27 (19:37 Pacific): "1. go and make changes as you suggest 2. let's make this 1.0 and make the changes the keepers' rulings call for." Build 8 is StarFall 1.0. No image requests. No scheduled task is created, changed or enabled.

## What is in

1. **Every item of `tests/creation-sim/run-07/changes.md`** (items 1 to 30), applied as its proposed change reads, except where Michael's decisions in that file's closing section, "Michael's decisions, 2026-11-27", say otherwise. Those decisions win. Items whose change is "No change" or "Watch" are recorded only. Item 26 is approved as proposed (19:37, "make changes as you suggest").
2. **Michael's three decisions of 2026-11-27**, in his words:
   - **The clock waits.** The clock does not advance past the year the player's story stands in. A night may resolve past a minor held moment (the Keeper judges minor, logs why; a prepared scene is never minor). A play day covers at most one in-game year. This replaces L-0056 and the lag rule in `night-turn.md` step 0.
   - **Paintings.** A play-year morning is approved only by the `images.md` line that names its own year. Fix `paint.py` and `check.py`, with tests.
   - **Travel by direction.** Travel along a line (river, road, coast) is priced segment by segment in the direction actually travelled, so the same line can take a different time each way (uphill against downhill, upstream against downstream, wind and current where the pace table has them). The tool names each line's ends by their places in its output, so no agent can price from the wrong end.
3. **The Keepers' rulings for review.** Every "Rulings for review" entry in the sim-06 keeper log (Run 07 setup, Year 4 night, Year 5 night) and the sim-07 keeper log (Night 1), and the checkers' "Rulings for review" in the sim-06 Year 4 and Year 5 flags. Each ruling that settles a gap in the files becomes a rule in the file it belongs in, in the form the Keeper (or checker) ruled. A ruling that only applied a rule already in the files needs nothing. A ruling one of Michael's decisions overrides is recorded as superseded.
4. **The version.** `engine/design/CHANGELIST.md` gets a Build 8 section headed "1.0", and `README.md` and `engine/design/DESIGN.md` name the version as 1.0.

## Assignment

- **Agent K (sealed) goes first on part 3.** It reads the sealed keeper logs, ledgers and flags, and writes `tests/creation-sim/run-07/rulings-to-rules.md`: one line per ruling, numbered, saying in procedure only (no world content, no names, no figures) what rule it becomes and which file owns it (engine, tool or sealed). Then it applies those that land in `SPOILERS_do_not_open/keeper/` along with parts 1 and 2 there.
- **Agent E (engine text)** applies parts 1, 2 and 4 in `CLAUDE.md` (only if needed), `engine/*`, `README.md`, `tests/README.md` and `tests/creation-sim/README.md`, then the engine lines of `rulings-to-rules.md` once K has written it.
- **Agent T (tools)** applies the tool items (14, 23, 24, 25, 26, and any other that lands in `tools/`), each with a test, then the tool lines of `rulings-to-rules.md`.

Each agent logs what it changed in `tests/creation-sim/run-07/applied.md` under its own heading. Then an independent check (`tests/creation-sim/run-07/build-check.md`), then fixes. Nothing waits on Michael: a gap the files and these decisions do not settle is ruled by the build check by the judgment order and logged for review.
