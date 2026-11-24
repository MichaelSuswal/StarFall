# Build 6 plan: applying the run 05 change list

Michael approved this build on 2026-11-23 (23:57 Pacific): "let's build and run". It applies every item of `tests/creation-sim/run-05/changes.md` (82 items), as proposed, with the seven he decided in his words. No image requests. No scheduled task is created, changed or enabled.

## What is in

Every item, except those whose change is "No change" (1, 5, 12, 25, 39, 49, 59, 69, 70, 82), which are recorded only. Watch items 13 and 54 are applied where they name a change (13 by 29; 54's paint-request size line and river check). Item 38 is a checker note. Item 75 becomes a line in `engine/night/scheduled-prompt.md`. Item 73 is settled by 74: the timing file leaves the public folder. Items 43 and 45 are folded into 14 and 3.

## Michael's decisions, in his words

1. **Variety-table ties (7).** "item 7 yes". A variety-table tie is the Keeper's call by what makes the more interesting game, reason logged, no die.
2. **A heavier return (20).** "item 20 yes". A player or NPC god may take a slower, costlier return than the standing rungs, priced by the DM or Keeper; it counts toward the sealed factors as a heavier price taken willingly.
3. **Sealed requests (32).** "yes, but never is strong. I think that should be the case unless there is an explicit reason for the contrary that the DM agrees with". The DM is told, in a sealed line it may read, that each sealed request was received and ruled, not how, unless the Keeper gives an explicit reason to tell it more and the DM agrees.
4. **A bent default (51).** "yes, but it could be that the default change is the price." A god that bends or refuses a default gets a negotiation round on that alone, even with no edge; the change itself may be the price.
5. **Far travelers and cross-country seasons (67).** Far travelers: "that is part of the story that is squarely for the Keeper to decide. I don't want to know." The Keeper decides how each arrived and logs it sealed. An event's season: "the season that it was designed to happen at creation, or determined to occur by actions of the world".
6. **Timing out of the player's view (74).** "I don't think we need the diagnostics for how long the night took. it takes the player out of game for no reason. make your data points relevant to game play. The number of years past is good." `P/state/timing.md` moves to the sealed side (`S/state/timing.md`); nothing public carries night or stage times. The clock's year stays public.
7. **The closing line on a test's first morning (78).** "yes."

## Shared specifications

- **Sealed answers (14, 15, 43, 64, 32).** Any player reply on any creation day may carry a `SEALED:` part on any subject. Each goes to `S/player/unsaid.md` as it arrives, dated, under a heading for its kind: want, fear, request not to be told, request to the Keeper, other. A sealed answer with two kinds is split into two lines. The DM never defers a want to Night 3. When a sealed wish is later said openly, the open words are used and the sealed line stays sealed. The open `Requests not to be told something:` line reads "one, kept in the sealed record" (or the count). The Keeper answers each sealed request in the sealed ledger and writes to a sealed file the DM may read, `S/player/requests-answered.md`, one line per request: its date and "received and ruled", nothing more, unless the Keeper gives an explicit reason to tell more and the DM agrees, both logged.
- **Timing (26, 74).** The campaign's timing file is `S/state/timing.md`, sealed. The orchestrator's test timing file records each agent's reported duration beside the clock times. The ordinal rule stays for the sealed timing file only as a style choice; lockcheck no longer scans for it in public.
- **A bent default (51).** In 3a.1 (and 2.3 where a default is bent on Night 2), a god whose people form bends or refuses a default gets a round on it, the cost stated plainly as the player was told, and the bend itself may be priced as the price. Its sealed factors count it only when it is priced (58).
- **Return (16, 19, 20, 22).** The return takes an item of memory or habit, never a possession. A sealed plea is a factor the Keeper may weigh, logged. A god holding none of its kind of ground gathers at the nearest place the Keeper rules for its kind, written into powers.md as the rule from this run's ruling. A heavier return beyond the rungs may be bought. The player is told, in (oog) after a return, which item was taken; the god in the fiction does not know.
- **Helpers forms (40, 41, 42).** Day 3 adds: an office that stands under the people's own law at landing; one the god creates or converts in play; "designed, not yet serving" is not a refused default and buys nothing. A paid force up to about one in fifty of the people is ordinary. A behavior trait is who a mortal is, never what it will do, unless the player asks for a binding, which is priced.
- **First morning (76, 77, 78, 79, 80, 81).** The landing map draws a seen line only as far as seen; a creation name shows only once heard, or the (oog) line says why. A "Settled for you" block in the closing (oog). The closing "the world turns" line is in every first morning, test or not. The close waits for the painting or logs it pending. The checker reads the first morning story before the clock is set.
- **Landing release template (60, 57).** Template 7.15: corrected view, helpers statement, the hour, what is in view.

## Assignment

Three agents work at once, each on its own files.

- **Agent E (engine text):** `CLAUDE.md` if needed; `engine/design/DESIGN.md` and `CHANGELIST.md` (every decision); `engine/creation/*` (2, 3, 4, 14, 15, 17, 21, 24, 33, 40, 41, 42, 43, 44, 46, 47, 53, 64); `engine/roles/*` (32, 55, 62, 66, 81, 38 as a checker note); `engine/night/*` (74, 75); `engine/rules/*`: powers.md (16, 18, 19, 20, 22), map.md (52, 76), morning-story.md (77, 78, 80); `engine/style/*` (79); the tests README and `tests/creation-sim/README.md` (26, 36, 74).
- **Agent T (tools):** `tools/lockcheck.py` (23, 37, 55, 71, 74), `tools/map.py` (52, 56, 61, 76), `tools/roll.py` (63 weighted draw), and tests for each.
- **Agent K (sealed):** `SPOILERS_do_not_open/keeper/`: the creation runbook (6, 8, 10, 11, 21, 27, 28, 29, 31, 32, 34, 35, 36, 48, 50, 51, 54, 57, 60, 63, 65, 66, 67, 72, 73, 74, 80, 81), the rubric (7, 9, 30, 51), the survey Keeper notes (6), the sealed factors file (20, 31, 58, 63), templates 7.6, 7.10, 7.13, 7.15 (30, 35, 60, 68).

Each agent logs what it changed in `tests/creation-sim/run-05/applied.md` under its own heading, by item number. Then an independent check (`build-check.md`), then fixes.

## Decisions after the build (2026-11-24, 09:51 Pacific)

Asked three questions when build 6 was done; Michael answered:

8. **Creation images for run 06.** "yes". Surface sheet, cloud sheet and first morning painting approved, with the three play-year morning paintings approved on 2026-11-24 00:00.
9. **Knacks and growth (68).** Asked whether knacks never grow: "yes, but only by using related skills". A knack does not grow as a power grows; it grows only through use of the skills related to it, never by any other trigger.
10. **A priced bend toward the sealed factors (check note 13).** Asked whether a player's priced bend of a default counts: "it depends what the default does. Does it make their life harder or easier? how much? are they paying an additional price elsewhere?" The Keeper judges each bend: it counts only when the bend makes the god's life harder, by how much, net of any price paid for it elsewhere; a bend that makes life easier, or is already paid for, counts nothing. The same rule for NPC gods. Reason logged.
