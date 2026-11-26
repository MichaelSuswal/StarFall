# Run 07: the short check of build 7

Michael approved on 2026-11-25: "ok.... go build and run .7" (21:16 Pacific), then chose the scope "Fresh Day 1 + reopen sim-06" and "No paintings" (21:2x Pacific).

Run 07 tests only the parts build 7 changed. It is not a full run.

## Part A: the waking vote (fresh campaign `sim-07`)

- Creation Day 1 (the world survey, with the waking vote) with a stand-in player, then Night 1.
- What it checks: the player votes its top two waking months on Day 1 and each NPC god votes on Night 1; the Keeper decides the month on Night 1 and logs why; one season for the whole world.
- It stops after Night 1. No Day 2, no map sheets, no paintings. The sim-07 clock is then set to `status: closed` under its `rulings.md` entry, so no scheduled task can run it.

## Part B: live scenes (reopen `sim-06`)

- The sim-06 clock reopens at Year 4 under a `rulings.md` entry, written by the orchestrator from Michael's words. That entry also says: from Year 4, build 7 governs sim-06; L-0038 and L-0046 are set aside; sim-06 keeps its per-country seasons and L-0043, since its world was built on them and a season rework is not what this run tests.
- Setup, before the play day: a Keeper pass writes the carried Year 4 held moment's board under build 7 (its facts, parameters and reasons in `S/releases/003/dm-sealed.md`) and a day sheet for the Year 4 play day. Whatever the Year 4 morning already told past the held moment is told again as provisional: the DM says so in (oog), and the night after it is played works it in as build 7 says. The Year 3 civ reports are used as they stand; where a Year 4 decide release needs a section they lack, the Keeper writes it from the Year 3 record and logs it.
- Year 4 play day: the held moment is played live under build 7, and the stand-in prepares a scene for later.
- Year 4 night: the Keeper holds the prepared scene at its opening moment, writing facts, parameters and the DM's reasons in the day sheet. The morning tells the year only up to the first held moment.
- Year 5 play day: the prepared scene and any held moment are played live. The result holds.
- Year 5 night: the Keeper accepts the played result. Then the clock closes again.
- What it checks: decision 1 of the build 7 plan for certain, and decision 7 and items 60, 69, 70, 87, 88, 91, 92, 96, 98 and 100 as the days run.
- Decisions 3, 4, 5 and 8 need a search, the god's absence, an ask met with silence and an act in a sealed note. The stand-in brief asks for one of each where it fits the play (a search for something, a short absence that leaves an ask unanswered, one ordinary habit stated only in a sealed note). Any that play does not bring is logged as not tested.

## Paintings

None. Morning painting requests are written and held in `images/held/`, not sent. `campaigns/sim-06/state/images.md` approves nothing new.

## Findings

Logged in `tests/creation-sim/run-07/changes.md`, timing in `tests/creation-sim/run-07/timing.md`.
