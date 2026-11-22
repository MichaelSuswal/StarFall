# The Night Turn

How one year of the world is resolved. Runs in the overnight session, which starts fresh and knows only what is in the repository. Begins after the play chat's 1:30 save and handoff. Must finish, with the morning story and painting committed, before 6:30; if it cannot, the 6:30 wake posts a notice and the story follows when done.

The campaign is `campaigns/<name>/`. The sealed campaign folder is `SPOILERS_do_not_open/campaigns/<name>/`. NNN is the year being resolved.

The overnight session runs this file only when `state/clock.md` says `status: open`. When it says `status: creation`, it runs `engine/night/creation-nights.md` instead.

## 0. Setup

- Pull the repository. Confirm `state/clock.md` says year NNN is open.
- **The engage rule.** Look for `player/decisions-NNN.md`. The DM writes it at 1:30 only on a day the player posted in the game. If it is missing, the player did not play today and the world waits: write `years/NNN/waited-YYYY-MM-DD.md` (the Pacific date) holding one (oog) line for the morning ("The world waited. Year NNN is still open.") and the Pacific time, append a line to `state/timing.md` that starts with the Pacific date and contains "waited", commit, push, and stop. Do not advance the clock. Do not run any agent.
- If the decisions file is present, start `years/NNN/` and `releases/NNN/`.
- Spawn agents as needed. Each agent gets only its own files. Use the models set in `state/models.md`. Take every real time from `TZ=America/Los_Angeles date`.

## 1. Decisions in

- The DM's handoff holds decisions only. Musings stayed with the DM.
- Each NPC god agent reads last year's release for it, updates its record and goals, and writes `gods/<god>/decisions-NNN.md`. Seven agents, run in parallel, never one after another.
- Each god's decisions go to its civ agent.

## 2. Keeper pass one: the year's world events

- Advance the clock: which clocked events fire this year, which triggers have been met by last year's state and this year's decisions.
- Weather, seasons, natural events, the godless peoples' actions, and anything else not tied to a god's people.
- Random events: rolled with `tools/roll.py --campaign <name>`, weighted down in Years 1 to 7 as the event schedule says. Where a chance event chooses among targets, apply the sealed factors to the weighting, logged.
- Recurring phenomena: counted by `tools/phenomena.py` from the sealed record (`SPOILERS_do_not_open/campaigns/<name>/state/phenomena.json`).
- Write for each civ agent what its people would experience this year (`releases/NNN/civ-<x>-pass1.md`: the player's people's release public, every NPC people's sealed under `S/releases/NNN/`), and for the Keeper itself a list of every world event with its cause.

## 3. Civ agents act

- Eight civ agents, in parallel, never one after another. Each works out its people's year from its god's decisions and pass one, per `engine/roles/civ.md`, and reports to the Keeper what touches anyone else.
- Unplayed time for the player's god: the avatar follows standing conduct (`player/conduct.md`, then the conduct profile). Minor encounters resolve by conduct. Major encounters are held: note the moment of contact and stop that thread.

## 4. Keeper pass two: resolution

- Overlay every civ's actions and reactions with the world events. Resolve contests by factors and `tools/roll.py`, applying the sealed factors after the stated odds on every roll for a god or its people's acts. Deliver messages per `engine/rules/messages.md` and log each one's fate.
- Check the sealed ruling ledger before any ruling; record every ruling made.
- Record new fixed facts in the keeper log when an action reached something unspecified.
- Each god's waking season is checked against its weaknesses (a god whose weakness holds through its own waking season opens the year unable to act, and the civ agent is told so).
- Growth: for each god, record in its sealed growth file any trigger met, year of practice, failure or near miss this year produced, per `engine/rules/powers.md`. Nothing is recorded that the year did not earn. If a tier is reached, update the card as a dated entry, apply the sealed factors for growth, and note for the release what the god feels.
- Any standing measure the sealed deep lore keeps for a god (its weight or standing on a scale a trigger rests on) is updated here, each year, in sealed state.
- Memory-loss drawbacks on NPC gods: remove the item from the god's record and log it.
- Update state: the player's people and the player's map knowledge in `P/state/` and `P/player/`; every NPC people's numbers, every NPC god's map knowledge and the message log in `S/state/` and the sealed folders; and `P/world/` where public facts changed through the world.
- Write `years/NNN/year.md`: everything that happened, with causes, sealed.
- Write the keeper log for the year, including the neutrality self-check.

## 5. The check

- Run `tools/check.py <name> NNN` and `tools/lockcheck.py <name> --leaks --dashes`.
- The checker agent runs `engine/roles/checker.md` against the year and writes the sealed `S/years/NNN/flags.md`, with the public `years/NNN/flags.md` carrying counts only.
- The Keeper reworks anything flagged and reruns the check. Loop until clean or until 6:00; anything left goes into the morning notice.

## 6. Releases

- For each NPC god and each civ: `releases/NNN/<agent>.md`, only what it could know. Any description of land comes from the map data.
- For the DM: `releases/NNN/dm.md`, everything the player's god would know: what it saw and sensed, what its people report, messages received with their state, held encounters with their moment of contact, deaths of significant people, the map knowledge gained, and what the god feels of any growth the Keeper released this year.

## 7. The morning story

- The DM agent reads its release and writes `years/NNN+1/morning-story.md` per `engine/rules/morning-story.md`: the return sequence, the summary with hooks, the held encounter if any, and the painting prompt.
- Write `years/NNN/closing.md`: the closing sequence for the year just resolved, three or four sentences in the DM's voice, unique to this god, written from what actually happened. The 6:30 wake posts it before the morning story.
- Write `images/requests/<campaign>-NNN+1-morning.json` as early as possible so the painting is back by 6:30.
- Update the chronicle: the civ agent's people side, the DM's god side, condensed per `engine/rules/chronicle.md`.

## 8. Close

- Run `tools/lockcheck.py <name> --leaks --dashes` again, now that the releases, the morning story, the closing and the chronicle exist. Fix any hit before anything is pushed.
- Set `state/clock.md` to year NNN+1 open, and append a line to `state/timing.md` that starts with the Pacific date and reads "clock advanced: year NNN+1 open". Every timing line starts with its Pacific date; no other line uses the words "clock advanced".
- Pull with rebase, then commit everything and push. The 6:30 wake in the play chat reads the morning story and the painting from the repository and posts them.

## Sealed and public outputs

Sealed, in `SPOILERS_do_not_open/campaigns/<name>/`: `years/NNN/year.md` (the full record), every NPC god's release and decisions, every NPC civ's record and years, the message log, the keeper log, the ruling ledger, the growth files, the sealed god folders. Public, in `campaigns/<name>/`: the player's folder, the player's civ record, the DM release, the morning story, the closing, the waited notes, flags, and the state files the player may see (clock, timing, the player's map knowledge). The rolls log is sealed; the player sees only outcomes. Nothing public names the count of gods, a vote, a pool, a hidden power, or a phenomenon's count before it has been seen.

## Public state files

`state/models.md`, `state/timing.md` and `state/images.md` are public. They name the models by role (DM, Keeper, god agent, civ agent, checker) and never carry a line per god, an agent count, or anything that gives the number of gods.

## Timing record

Append to `state/timing.md`: when the turn started, when each stage finished, which models ran, and the token usage if known, all in Pacific time from the clock. Stage B uses this to choose the night model.
