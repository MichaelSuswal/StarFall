# Build 7 plan: applying the run 06 change list

Michael approved this build on 2026-11-25 (21:16 Pacific): "ok.... go build and run .7". It applies every item of `tests/creation-sim/run-06/changes.md` (items 1 to 101) as its status line now reads, and every decision in that file's closing section, "Michael's decisions, 2026-11-25". No image requests. No scheduled task is created, changed or enabled.

## What is in

- Every item marked "approved", applied as its proposed change reads.
- Items whose change is "No change" or "Watch" are recorded only.
- Items 3, 33, 81, 82, 90, 94, 99 and 101 are applied as their status line reads, not as first proposed.
- Every decision in the closing section, as written there, in Michael's words. Where a decision overrides an item or an earlier rule, the decision wins and the earlier text is replaced, not left beside it.

## The decisions, as they land in the engine

1. **Live scenes and held moments (81, 82, 90, 94).**
   - A scene the player prepares for at the table is held by the night turn at its opening moment and played live on the next play day. The same holds for every held moment, prepared or not, including one with a world figure whose words are the Keeper's.
   - The Keeper writes, in the DM's release, the scene's facts, its parameters (what the figures want, what they will and will not do or accept, the ranges outcomes fall in) and the reasons for the parameters. The reasons are for the DM only. The DM may share them, lie about them in a figure's voice, or not mention them.
   - The DM plays the scene (Michael's option a). A played scene holds. The Keeper accepts the result the DM and the civ agent feed up and never unmakes it.
   - The morning tells the year only up to the first held moment. The night after it is played works the played answer in, and the next morning tells the rest. A held moment's date is its own; the decisions file carries what was played under the year it was played in, and `night-turn.md` and `morning-story.md` say how (82 is resolved by this).
   - L-0038 (a prepared event resolved in the night) and L-0046 (the rework rule) are superseded for new campaigns. Item 101 falls away.
2. **Growth and hidden powers (99).**
   - Powers feel limited to their given capabilities. A skill or power progresses slowly, by being done a lot and by pushing at new boundaries. Gods may be a bit faster than mortals. Nothing prevents an attempt, and a god may have a reason to start early.
   - No hint of any kind about a change in powers is given to any god, player or NPC, until at least year 70: no release line, no DM line, no prompt. NPC gods are not prompted to grow.
   - A hidden power surfaces when its condition is met. The Keeper sets the conditions so they are rarely met in the early years.
3. **Clues (Keeper ruling, step 4, Year 3).** A thing that came about in the game is found by a roll with modifiers, weighed by the evidence (Bayesian reasoning). A thing the Keeper placed is there.
4. **An absent god's people.** A town may act on the god's behalf only where the god expressed that intention or obviously assumed it. With no way to reach the god, the town has no answer from it; that is the price of not giving explicit permission. The civ agent may decide that someone in the town took it upon themselves to make the call.
5. **No reply.** A question put to an absent god meets silence and stays pending unless the god noted otherwise (conduct profile, standing words). People know only what happened.
6. **Seasons.** All the world goes through the seasons at the same time. Every god, player and NPC, votes its top two months to wake, in the Day 1 survey. The Keeper decides the waking month on Night 1 and logs why. This replaces each country opening its year in its own season (DESIGN 8.1) and L-0043.
7. **What the god did not witness.** Sealed. The player's people's public files hold only what the god could witness or be told; the rest goes in sealed files.
8. **Acts in a sealed note.** An act the god says it does is done, wherever it is said, sealed note included. An ordinary habit (checking a pocket) is conduct, carried out and never priced. Wants and fears stay feelings.
9. **Powers given to mortals (33).** Giving a power to a mortal costs the god something. The Keeper prices it. One that dies with the person is less powerful and costs less. The DM does not price it at the table; it records the player's wish and the Keeper prices it at night, put back to the player as a cost.

## Assignment

Three agents work at once, each on its own files. Each reads the whole change list (rows and the closing section) and applies every item and decision that lands in its files.

- **Agent E (engine text):** `CLAUDE.md` only if a rule there must change; `engine/design/DESIGN.md` and `engine/design/CHANGELIST.md` (a build 7 section recording every decision); `engine/creation/*`; `engine/roles/*`; `engine/night/*`; `engine/rules/*`; `engine/style/*`; `tests/README.md` and `tests/creation-sim/README.md`; `tests/creation-sim/run-06/stand-in.md` only for item 66.
- **Agent T (tools):** `tools/*.py` and their tests (among them 1, 12, 13, 44, 49, 53, 61, 62, 70, 71, 78, 96), each with a test.
- **Agent K (sealed):** `SPOILERS_do_not_open/keeper/*`: the creation runbook, the rubric, the survey Keeper notes, the sealed factors file, the templates (among them the DM day sheet of item 60 with the parameters and reasons of decision 1, the pass-one release with months and counts of item 98, the sealed-note rule of item 100, the waking vote of decision 6, growth and hidden-power conditions of decision 2).

Each agent logs what it changed in `tests/creation-sim/run-06/applied.md` under its own heading, by item number and decision number. Then an independent check (`build-check.md`), then fixes.

## Then run 07

A short check of the changed parts, not a full run. Its scope is set in `tests/creation-sim/run-07/plan.md` after the build check.
