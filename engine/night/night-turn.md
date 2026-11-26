# The Night Turn

How one year of the world is resolved. Runs in the overnight session, which starts fresh and knows only what is in the repository. Begins after the play chat's 1:30 save and handoff. Must finish, with the morning story and painting committed, before 6:30; if it cannot, the 6:30 wake posts a notice and the story follows when done.

The campaign is `campaigns/<name>/`. The sealed campaign folder is `SPOILERS_do_not_open/campaigns/<name>/`. NNN is the year being resolved.

The overnight session runs this file only when `state/clock.md` says `status: open`. When it says `status: creation`, it runs `engine/night/creation-nights.md` instead.

## 0. Setup

- Pull the repository. Confirm `state/clock.md` says year NNN is open.
- **The engage rule.** Look for `player/decisions-NNN.md`. The DM writes it at 1:30 only on a day the player posted in the game. If it is missing, the player did not play today and the world waits: write `years/NNN/waited-YYYY-MM-DD.md` (the Pacific date) holding one (oog) line for the morning ("The world waited. Year NNN is still open.") and the Pacific time, append a line to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md` that starts with the Pacific date and contains "waited", commit, push, and stop. Do not advance the clock. Do not run any agent.
- If the decisions file is present, start `years/NNN/` and `releases/NNN/`.
- **A held year's tail.** If the decisions file carries a section for an earlier year (what the player played at a held moment of that year, DESIGN 10.5a), that year's stretch after the held moment is resolved first, in steps 1 to 4 below, with the played answer worked in as it was played, before year NNN. The played scene holds: its result is taken as the DM and the civ agent feed it up and is never unmade.
- **Year 1 only.** Each NPC god's first release carries its landing release (`S/releases/000/<label>-landing.md`, written on Night 3b).
- **The decide releases.** For each NPC god the Keeper writes `S/releases/NNN/<label>-decide.md`, the frame the god decides its year from: the release of the year before (at Year 1, its landing release), the section "What your people tell you" copied from its civ agent's last report (`years/NNN-1-report.md`; none at Year 1), and the messages delivered to it.
- Pull once, here, before spawning anything. Agents spawned in parallel do not pull; the night session commits their files (run 06 item 88).
- Spawn agents as needed. Each agent gets only its own files. Use the models set in `state/models.md`. Take every real time from `python3 tools/stamp_time.py` (`--time` for the time alone, `--date` for the date), which prints the Pacific clock time in the log's format.

## 1. Decisions in

- The DM's handoff holds decisions only. Musings stayed with the DM.
- Each NPC god agent reads its decide release, `S/releases/NNN/<label>-decide.md`, updates its record and goals, and writes `gods/<god>/decisions-NNN.md`. Seven agents, run in parallel, never one after another. The decide release prompts nothing about growth (DESIGN 6.5).
- Each god's decisions go to its civ agent.

## 2. Keeper pass one: the year's world events

- Advance the clock: which clocked events fire this year, which triggers have been met by last year's state and this year's decisions.
- Weather, seasons (the whole world in the same season, the year opening in the waking month, DESIGN 8.1), natural events, the godless peoples' actions, and anything else not tied to a god's people.
- Random events: rolled with `tools/roll.py --campaign <name>`, weighted down in Years 1 to 7 as the event schedule says. Where a chance event chooses among targets, apply the sealed factors to the weighting, logged.
- Recurring phenomena: counted by `tools/phenomena.py` from the sealed record (`SPOILERS_do_not_open/campaigns/<name>/state/phenomena.json`).
- Write for each civ agent what its people would experience this year (`releases/NNN/civ-<x>-pass1.md`: the player's people's release public, every NPC people's sealed under `S/releases/NNN/`), and for the Keeper itself a list of every world event with its cause. The player's people also get a sealed side release, `S/releases/NNN/civ-<x>-sealed.md`, read by their civ agent only and never by the DM: what their office holders and other mortals know that the god does not (run 06 item 76). The asking and the telling of sealed things are themselves sealed content.
- **Prepared scenes.** Any scene the player prepared for at the table (the decisions file names it, with its time) is held at its opening moment, as a held moment is (step 3).

## 3. Civ agents act

- Eight civ agents, in parallel, never one after another. Each works out its people's year from its god's decisions and pass one, per `engine/roles/civ.md`, and reports to the Keeper what touches anyone else, in `years/NNN-report.md` in its own folder.
- Unplayed time for the player's god: the avatar follows standing conduct (the standing instructions and the conduct profile, `player/conduct-profile.md`). Minor encounters resolve by conduct, and a simple ask is answered by the profile's stated temper where it speaks, logged as conduct, not as a decision (DESIGN 10.6). A question put to the god while it is absent meets silence and stays pending unless the god noted otherwise. Major encounters and prepared scenes are held: note the moment of contact and stop that thread.

## 4. Keeper pass two: resolution

- Overlay every civ's actions and reactions with the world events. Resolve contests by factors and `tools/roll.py`, applying the sealed factors after the stated odds on every roll for a god or its people's acts. A roll the DM made in the open during the day stands unless the Keeper overrules its outcome by the sealed factors, as that file gives; any overrule is logged in the keeper log only. A held or prepared scene the DM played under the Keeper's parameters is never overruled: it holds. Deliver messages per `engine/rules/messages.md` and log each one's fate.
- **The first held moment.** Find the first held moment of the year for the player's god (a major encounter, a prepared scene). The year is told to the DM only up to it. Resolve the rest of the year for the world as it stands, but treat the player's people's stretch after that moment as unresolved for the telling: it is worked again, with the played answer, on the night after the moment is played (DESIGN 10.5a). Write the moment for the DM as a board with its facts, its parameters (what each figure wants, what it will and will not do or accept, its stance and opening words, the ranges outcomes fall in) and the reasons for them.
- **Threads the Keeper releases.** Where a civ agent stopped a thread mid-year as held and the Keeper sorts it as not held, the civ agent gets a short second pass for those threads alone; if no pass can be run, the Keeper writes the people's next step itself, logged (run 06 item 75).
- Check the sealed ruling ledger before any ruling; record every ruling made. A matter the files do not settle is ruled by the judgment order, applied, and logged under "Rulings for review"; nothing waits on the owner.
- Record new fixed facts in the keeper log when an action reached something unspecified. Whether a clue is there to find: a thing the Keeper placed is there; a thing that came about in play is found by a roll with modifiers, weighed by the evidence (DESIGN 8.7).
- The waking month is checked against every god's weaknesses (a god whose weakness holds through the waking month opens the year unable to act, and the civ agent is told so).
- Growth: for each god, record in its sealed growth file any trigger met, year of practice, failure or near miss this year produced, per `engine/rules/powers.md`. Nothing is recorded that the year did not earn. Until at least year 70 no release carries any hint of a change in powers (DESIGN 6.8). If a tier is reached, apply the sealed factors for growth; it is found in use, and the card gets its dated entry when it shows.
- Any standing measure the sealed deep lore keeps for a god (its weight or standing on a scale a trigger rests on) is updated here, each year, in sealed state.
- Memory-loss drawbacks on NPC gods: remove the item from the god's record and log it.
- Update state: the player's people and the player's map knowledge in `P/state/` and `P/player/`, and what the player's people now know of the land in `P/civs/<people>/knowledge.md`; every NPC people's numbers, every NPC god's map knowledge and the message log in `S/state/` and the sealed folders; and `P/world/` where public facts changed through the world.
- Write `years/NNN/year.md`: everything that happened, with causes, sealed.
- Write the keeper log for the year, including the neutrality self-check.
- **Quick script check.** Run `tools/check.py <name> NNN` and `tools/lockcheck.py <name> --leaks --dashes` (the scan covers the sealed civ files too) and fix what they find before the releases.

## 5. Releases

- For each NPC god and each civ: `releases/NNN/<agent>.md`, only what it could know. Any description of land comes from the map data.
- For the DM: `releases/NNN/dm.md`, everything the player's god would know up to the first held moment and nothing past it: what it saw and sensed, what its people report, messages received with their state, the held moment as a board with its facts, parameters and reasons (for the DM only), deaths of significant people, and the map knowledge gained. Its **day sheet**: the small world facts the DM may need in play (market days, the hall's weights and their true figures, named mortals the god is likely to meet with their sex, prices), for the DM only (run 06 item 60). No line about growth until at least year 70.

## 6. The morning story

- The DM agent reads its release and writes `years/NNN+1/morning-story.md` per `engine/rules/morning-story.md`: the return sequence, the summary with hooks up to the first held moment, the held moment's board if there is one, and the painting prompt. A held year's tail, resolved tonight, is told first, then year NNN.
- Write `years/NNN/closing.md`: the closing sequence for the year just resolved, three or four sentences in the DM's voice, unique to this god, written from what actually happened. The 6:30 wake posts it before the morning story.
- Write `images/requests/<campaign>-NNN+1-morning.json` as early as possible so the painting is back by 6:30.
- Update the chronicle: the civ agent's people side, the DM's god side, condensed per `engine/rules/chronicle.md`.

## 7. The check

- One round over everything the night wrote, now that the releases, the morning story, the closing and the chronicle exist (run 06 item 73). Run `tools/check.py <name> NNN` and `tools/lockcheck.py <name> --leaks --dashes`.
- The checker agent runs `engine/roles/checker.md` against the year and writes the sealed `S/years/NNN/flags.md`, with the public `years/NNN/flags.md` carrying counts only.
- The Keeper reworks anything flagged and reruns the check. Loop until clean or until 6:00; anything left goes into the morning notice.

## 8. Close

- Fix any script hit before anything is pushed.
- Set `state/clock.md` to year NNN+1 open, and append a line to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md` that starts with the Pacific date and reads "clock advanced: year NNN+1 open". Every timing line starts with its Pacific date; no other line uses the words "clock advanced".
- Pull with `git pull --rebase --autostash`, then commit everything and push. The 6:30 wake in the play chat reads the morning story and the painting from the repository and posts them.

## Sealed and public outputs

Sealed, in `SPOILERS_do_not_open/campaigns/<name>/`: `years/NNN/year.md` (the full record), every NPC god's release, decide release and decisions, every NPC civ's record and years, the player's people's sealed side release and sealed files (`S/civs/<people>/`: what the god could not witness), the message log, the keeper log, the ruling ledger, the growth files, the sealed god folders, and the Keeper's roll log. Public, in `campaigns/<name>/`: the player's folder, the player's civ record (only what the god could witness or be told), the DM release, the morning story, the closing, the waited notes, flags, the DM's open roll log `state/rolls.jsonl`, and the state files the player may see (clock, the player's map knowledge). The timing file is sealed (`S/state/timing.md`): night and stage times are diagnostics, not play, and the player sees only in-game data such as the year. The DM's open rolls are public, with their odds and outcomes; the Keeper's rolls are sealed. Nothing public names the count of gods, a vote, a pool, a hidden power, or a phenomenon's count before it has been seen.

## Public state files

`state/models.md` and `state/images.md` are public; the timing file is sealed (`S/state/timing.md`). They name the models by role (DM, Keeper, god agent, civ agent, checker) and never carry a line per god, an agent count, or anything that gives the number of gods.

## Timing record

Append to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md`: when the turn started, when each stage finished, which models ran, and the token usage if known, all in Pacific time from the clock. Stage B uses this to choose the night model.
