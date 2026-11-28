# The Night Turn

How one year of the world is resolved. Runs in the overnight session, which starts fresh and knows only what is in the repository. Begins after the play chat's 1:30 save and handoff. Must finish, with the morning story and painting committed, before 6:30; if it cannot, the 6:30 wake posts a notice and the story follows when done.

The Keeper's own procedure for each step is the sealed `SPOILERS_do_not_open/keeper/year-turn.md`; this file is the public frame.

The campaign is `campaigns/<name>/`. The sealed campaign folder is `SPOILERS_do_not_open/campaigns/<name>/`. NNN is the year being resolved.

The overnight session runs this file only when `state/clock.md` says `status: open`. When it says `status: creation`, it runs `engine/night/creation-nights.md` instead.

## 0. Setup

- Pull the repository, once: this is the night's one pull before anything is spawned, and agents spawned in parallel do not pull; the night session commits their files (run 06 item 88). Confirm `state/clock.md` says year NNN is open, and read its `play_day` line (K; a clock without the line is play day 1). K is 2 or more only when the clock waited (below); such a night runs as `## A night after the clock waited` gives.
- **The engage rule.** Look for the play day's decisions file: `player/decisions-NNN.md` on play day 1, `player/decisions-NNN-K.md` on play day K. The DM writes it at 1:30 only on a day the player posted in the game. If it is missing, the player did not play today and the world waits: write `years/NNN/waited-YYYY-MM-DD.md` (the Pacific date) holding one (oog) line for the morning ("The world waited. Year NNN is still open.") and the Pacific time, append a line to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md` that starts with the Pacific date and contains "waited", commit, push, and stop. Do not advance the clock. Do not run any agent.
- If the decisions file is present, start `years/NNN/` and `releases/NNN/`.
- **The clock waits until the story catches up** (Michael, 2026-11-27). The clock does not advance past the year the player's story stands in. A night that ends with the player's thread stopped at an unplayed held moment of year NNN leaves the clock at year NNN and raises `play_day` by one (step 8); the next play day plays that moment, in year NNN, and the night after it works the played answer into the rest of the year, up to the next held moment. Once the player's thread reaches the end of year NNN, the clock advances to NNN+1. The world's year is resolved whole once, on the year's first night; no night resolves more than one year, and a play day, with the morning that opens it, covers at most one in-game year. This replaces the build 7 lag rule (an open year's thread held back behind an earlier year's tail while the clock turned one year a night) and ledger L-0056 (run 07 items 15 and 29).
- **A minor held moment.** A night may resolve past a minor held moment. The Keeper judges whether a held moment is minor and logs why in the keeper log; a moment it passes is resolved by standing conduct (DESIGN 10.6), as a minor encounter is, and the morning tells it as what happened. A prepared scene is never minor. The first held moment the night does not pass is the one the year is told up to.
- **Year 1 only.** Each NPC god's first release carries its landing release (`S/releases/000/<label>-landing.md`, written on Night 3b).
- **The decide releases.** For each NPC god the Keeper writes `S/releases/NNN/<label>-decide.md`, the frame the god decides its year from: the release of the year before (at Year 1, its landing release), the section "What your people tell you" copied from its civ agent's last report (`years/NNN-1-report.md`; none at Year 1), and the messages delivered to it. That section tells an attempt whose outcome pass two had not settled only as an attempt tried, with no figure or outcome (`engine/roles/civ.md`, step 6; run 07 item 28).
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
- Write for each civ agent what its people would experience this year, each release carrying the standing line that the section "What the people tell their god" tells an unsettled attempt only as tried (`releases/NNN/civ-<x>-pass1.md`: the player's people's release public, every NPC people's sealed under `S/releases/NNN/`), and for the Keeper itself a list of every world event with its cause. The player's people also get a sealed side release, `S/releases/NNN/civ-<x>-sealed.md`, read by their civ agent only and never by the DM: what their office holders and other mortals know that the god does not (run 06 item 76). The player's people have three sealed things, kept apart: the Keeper's world side of them, `S/civs/<people>-sealed.md`, written on Night 3a and told to no one; their civ agent's own sealed folder, `S/civs/<people>/` (DESIGN 12.2); and this yearly side release, which the Keeper draws from the world side and the year, giving the agent only what its mortals would know. The asking and the telling of sealed things are themselves sealed content.
- **Prepared scenes.** Any scene the player prepared for at the table (the decisions file names it, with its time) is held at its opening moment, as a held moment is (step 3).

## 3. Civ agents act

- Eight civ agents, in parallel, never one after another. Each works out its people's year from its god's decisions and pass one, per `engine/roles/civ.md`, and reports to the Keeper what touches anyone else, in `years/NNN-report.md` in its own folder.
- Unplayed time for the player's god: the avatar follows standing conduct (the standing instructions and the conduct profile, `player/conduct-profile.md`). Minor encounters resolve by conduct, and a simple ask is answered by the profile's stated temper where it speaks, logged as conduct, not as a decision (DESIGN 10.6). A question put to the god while it is absent meets silence and stays pending unless the god noted otherwise. Major encounters and prepared scenes are held: note the moment of contact and stop that thread.

## 4. Keeper pass two: resolution

- Overlay every civ's actions and reactions with the world events. Resolve contests by factors and `tools/roll.py`, applying the sealed factors after the stated odds on every roll for a god or its people's acts. A roll the DM made in the open during the day stands: the Keeper never changes its result, and luck works only through the odds the Keeper sets. A held or prepared scene the DM played holds. Deliver messages per `engine/rules/messages.md` and log each one's fate.
- **The first held moment.** Find the first held moment of the year for the player's god (a major encounter, a prepared scene) that the night does not pass as minor (step 0). The year is told to the DM only up to it, and the clock waits at year NNN (step 8). Resolve the rest of the year for the world as it stands, but treat the player's people's stretch after that moment as unresolved for the telling: it is worked again, with the played answer, on the night after the moment is played (DESIGN 10.5a). Write the moment for the DM: the board as the god sees it in the public DM release, and its facts, its parameters (what each figure wants, what it will and will not do or accept, its stance and opening words, the ranges outcomes fall in) and the reasons for them in the sealed `S/releases/NNN/dm-sealed.md`. A chance range for the player's people on the board is rolled by the Keeper before the board is written, with the sealed factor, and given to the DM as an outcome by branch; a small world fact the DM would otherwise roll is rolled by the Keeper before the day sheet is written, as the world's question with no sealed factor, and written on the sheet as a fixed fact; the DM rolls only the player's own attempts in the scene (run 07 item 18; rulings-to-rules 6 and 28). Every later held moment already known when the sheet is written (a second prepared scene) gets a board in the sealed companion too, conditional on the ways the one before can fall, so the DM may play on into it the same day; the thread, the public release and the morning still stop at the first unplayed moment, and a moment the night's resolving has not reached carries no board (rulings-to-rules 11). The board also lists the readings the god's own powers and senses would give in the scene, within its card, so no reading the player asks for waits on a roll the scene has no turn for (run 07 item 21).
- **Threads the Keeper releases.** Where a civ agent stopped a thread mid-year as held and the Keeper sorts it as not held, the civ agent gets a short second pass for those threads alone; if no pass can be run, the Keeper writes the people's next step itself, logged (run 06 item 75).
- Check the sealed ruling ledger before any ruling; record every ruling made. A matter the files do not settle is ruled by the judgment order, applied, and logged under "Rulings for review"; nothing waits on the owner.
- Record new fixed facts in the keeper log when an action reached something unspecified. Whether a clue is there to find: a thing the Keeper placed is there, and a search for it works out with no roll unless under pressure or in a race; a thing that came about in play is found by a roll with modifiers, weighed by the evidence (DESIGN 8.7).
- The waking month is checked against every god's weaknesses (a god whose weakness holds through the waking month opens the year unable to act, and the civ agent is told so).
- Growth: for each god, record in its sealed growth file any trigger met, year of practice, failure or near miss this year produced, per `engine/rules/powers.md`. Nothing is recorded that the year did not earn. Until at least year 70 no release carries any hint of a change in powers (DESIGN 6.8). If a tier is reached, apply the sealed factors for growth; before year 70 it shows only in use, as what happened, and no card entry is written before year 70.
- Any standing measure the sealed deep lore keeps for a god (its weight or standing on a scale a trigger rests on) is updated here, each year, in sealed state.
- Memory-loss drawbacks on NPC gods: remove the item from the god's record and log it.
- Update state: the player's people and the player's map knowledge in `P/state/` and `P/player/`, and what the player's people now know of the land in `P/civs/<people>/knowledge.md`; every NPC people's numbers, every NPC god's map knowledge and the message log in `S/state/` and the sealed folders; and `P/world/` where public facts changed through the world.
- Write `years/NNN/year.md`: everything that happened, with causes, sealed.
- Write the keeper log for the year, including the neutrality self-check.
- **Quick script check.** Run `tools/check.py <name> NNN --step 4` and `tools/lockcheck.py <name> --leaks --dashes` (the scan covers the sealed civ files too) and fix what they find before the releases.

## 5. Releases

- For each NPC god and each civ: `releases/NNN/<agent>.md`, only what it could know. Any description of land comes from the map data.
- For the DM: the public `releases/NNN/dm.md`, everything the player's god would know up to the first held moment and nothing past it: what it saw and sensed, what its people report, messages received with their state, the held moment's board as the god sees it, deaths of significant people, and the map knowledge gained, with a pointer to the sealed companion. The sealed companion `S/releases/NNN/dm-sealed.md` ("Written by the Keeper. Read by the DM, the Keeper and the checker."), which the DM reads by its path, carries what is for the DM only, since the player may read `releases/`: the held moment's or prepared scene's facts, parameters and reasons, and the **day sheet**, the small world facts the DM may need in play (market days, the hall's weights and their true figures, named mortals the god is likely to meet with their sex, prices) (run 06 item 60, decision 1); anything else a board needs that the public release may not show (a sealed term, a truth, what a sealed act showed the god) goes there too. No line about growth until at least year 70.

## 6. The morning story

- The DM agent reads its release and writes the morning per `engine/rules/morning-story.md`: the return sequence, the summary with hooks up to the first held moment, the held moment's board if there is one, and the painting prompt. The morning is `years/NNN+1/morning-story.md` when the player's thread reached the end of year NNN, so that the clock will advance at step 8, and `years/NNN/morning-story-<K+1>.md` when it stopped at a held moment, so that the clock will wait.
- Write `years/NNN/closing.md` (`closing-K.md` on play day K): the closing sequence for the stretch just resolved, three or four sentences in the DM's voice, unique to this god, written from what actually happened. The 6:30 wake posts it before the morning story.
- Write `images/requests/<campaign>-NNN+1-morning.json` (for a morning while the clock waits, `<campaign>-NNN-morning-<K+1>.json`) as early as possible so the painting is back by 6:30, if `state/images.md` approves that morning's painting by the rule in `engine/rules/morning-story.md` (the line that names its own year; Michael, 2026-11-27, item 14); if it does not, write the request under the same name to `images/held/` instead, where it waits and nothing is painted (build check B7).
- Update the chronicle: the civ agent's people side, the DM's god side, condensed per `engine/rules/chronicle.md`.

## 7. The check

- One round over everything the night wrote, now that the releases, the morning story, the closing and the chronicle exist (run 06 item 73). Run `tools/check.py <name> NNN --step 7` (the clock is still on the year until step 8) and `tools/lockcheck.py <name> --leaks --dashes`.
- The checker agent runs `engine/roles/checker.md` against the year and writes the sealed `S/years/NNN/flags.md`, with the public `years/NNN/flags.md` carrying counts only.
- The Keeper reworks anything flagged and reruns the check. Loop until clean or until 6:00; anything left goes into the morning notice.

## 8. Close

- Fix any script hit before anything is pushed.
- If the player's thread reached the end of year NNN, set `state/clock.md` to year NNN+1 open, with no `play_day` line. If it stopped at a held moment the night did not pass, the clock waits: leave it at year NNN open and set `play_day: K+1` (step 0). Run the full check, `tools/check.py <name> NNN` with no step flag, and fix any finding; then append a line to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md` that starts with the Pacific date and reads "clock advanced: year NNN+1 open", or, when the clock waits, "clock waited: year NNN open, play day K+1". Every timing line starts with its Pacific date; no other line uses the words "clock advanced".
- Pull with `git pull --rebase --autostash`, then commit everything and push. The 6:30 wake in the play chat reads the morning story and the painting from the repository and posts them.

## A night after the clock waited

On play day K of 2 or more, year NNN's world was resolved whole on its first night, and this night resolves only the rest of the player's thread in it:

- Step 0 as above, with `player/decisions-NNN-K.md`. Its `## Played at a held moment` section (the moment's own date and what was played) is worked in as it was played: the played scene holds, its result is taken as the DM and the civ agent feed it up, and it is never unmade. When the file has no such section (the player posted, but did not play the moment), the moment stays held and nothing past it is resolved: the clock waits again with `play_day` raised, and the next morning opens on the same board. A scene the player walked away from in play is played: its outcome is what the god did (build 8 check, R8).
- Steps 1 and 2: the year's NPC god decisions and pass one stand. No NPC god decides again and no decide release is written.
- Step 3: the player's people's civ agent works their stretch from the held moment on, from the played answer and its sealed notes "Past the first held moment: not yet what happened". Any other civ agent or NPC god the stretch reaches within year NNN (a message delivered, a raid met) gets a short pass on that alone; if no pass can be run, the Keeper writes its next step itself, logged.
- Step 4: pass two for the stretch, over the year's world as resolved, up to the next held moment the night does not pass, or to the end of the year. The sealed `years/NNN/year.md` gets a section for the stretch, and state is updated as usual.
- Steps 5 to 7 as usual, for the stretch. The files the night writes for play day K carry its number: `releases/NNN/dm-K.md` and the sealed `S/releases/NNN/dm-sealed-K.md`, `years/NNN/closing-K.md`, and the flags `S/years/NNN/flags-K.md` with the public counts in `years/NNN/flags-K.md`.
- Step 8 as above: the clock advances when the thread reached the year's end, and waits again otherwise.

## A campaign moved to a new build

A one-time rule, for a campaign in play when a new build is applied to it: every public file written under the earlier build stays in place as told and is marked provisional from the first held moment the new build would hold, with a set-aside line; nothing is moved or deleted. The mark covers every line told or released past the moment (a return sequence that speaks of the next year's opening, (oog) lines, a closing that speaks of the year's end), and in doubt a line is marked; the mark says only that a line was set aside and that it is kept where it stands, never what it said (build 8 check, R5). The DM says so once in (oog), tells and plays from none of it past the mark, and the night that reaches the stretch works it again as the new build says (run 07 items 7 and 16; rulings-to-rules 2, 4 and 37).

## Sealed and public outputs

Sealed, in `SPOILERS_do_not_open/campaigns/<name>/`: `years/NNN/year.md` (the full record), every NPC god's release, decide release and decisions, every NPC civ's record and years, the player's people's sealed side release and sealed files (`S/civs/<people>/`: what the god could not witness), the message log, the keeper log, the ruling ledger, the growth files, the sealed god folders, and the Keeper's roll log. Public, in `campaigns/<name>/`: the player's folder, the player's civ record (only what the god could witness or be told), the DM release, the morning story, the closing (each with its play day's number after the clock waited), the waited notes, flags, the DM's open roll log `state/rolls.jsonl`, and the state files the player may see (clock, the player's map knowledge). The timing file is sealed (`S/state/timing.md`): night and stage times are diagnostics, not play, and the player sees only in-game data such as the year. The DM's open rolls are public, with their odds and outcomes; the Keeper's rolls are sealed. Nothing public names the count of gods, a vote, a pool, a hidden power, or a phenomenon's count before it has been seen.

## Public state files

`state/models.md` and `state/images.md` are public; the timing file is sealed (`S/state/timing.md`). They name the models by role (DM, Keeper, god agent, civ agent, checker) and never carry a line per god, an agent count, or anything that gives the number of gods.

## Timing record

Append to the sealed `SPOILERS_do_not_open/campaigns/<name>/state/timing.md`: when the turn started, when each stage finished, which models ran, and the token usage if known, all in Pacific time from the clock. Stage B uses this to choose the night model.
