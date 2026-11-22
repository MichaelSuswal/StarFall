# Build 4 plan: applying the run 03 change list

Michael approved this build on 2026-11-21 (21:59 Pacific): apply the run 03 change list (`changes.md`, 93 items) with the decisions and specifications below. No image requests. No scheduled task is created, changed or enabled. Run 04 is not approved yet; Michael will be asked again before it runs.

## What is in

Every item whose status is proposed, approved or clarified, except these, which are left out: 1 (watch), 6, 15, 17, 28, 41, 42, 49, 50, 63, 64, 73, 77, 79, 85, 88 (no change or closed), 40 and 72 (folded into 89), 51 (becomes run 04). Item 29 is already applied. Item 75 is half applied (checker.md); the runbook half is in.

Where an item and a ruling disagree, the ruling wins: item 54 yields to ruling 18 (two pending marks for two matters get two ids), and item 74's road rule yields to item 93.

## Michael's decisions (in his words where he gave them)

1. **The rulings (89).** All 41 logged rulings stand as recommended, except four he amended: 6 (91), 10 (90), 25 (92), 40 (93). Ruling 34 is decided: the Keeper updates that sealed measure in pass two each year, in sealed state. Each standing ruling is written into the file it belongs to.
2. **Hidden luck (90).** "Say a god were to take heavier prices willingly, or even in an extreme reject all powers. Then, fortune would often favor him, plans would go well for that god." NPC gods earn it the same way. "Each god has a luck modifier used in its rolls and weight of choice." Craft and technology do not move it; developing god powers moves it back toward normal.
3. **Technology (91).** The starting level is not a ceiling. A god may bring in what it knows, but must build it in play from what the player knows or looks up.
4. **Names (92).** "Names of towns shouldn't change just because a god uses an alternate name a few times."
5. **Travel (93).** "Travel should be priced by how people choose to travel. Different paths to a place will have different times to walk them... and will depend if you are just walking or going by wagon."
6. **Continent (87).** At least 600 miles across at its narrowest and about 1,000 miles across on average.
7. **The landing map (80).** Not a problem: it shows scale. Use it to demonstrate the scale of the map.
8. **Redraw (86).** Redraw the player's map only when the player's map changed; otherwise show the latest version.
9. **The unsaid want (26).** "Seal it, but the DM(s) should confirm with the user, maybe subtly, maybe explicitly, that those desires are still there before acting on them."
10. **Rulings route (76).** Yes, as proposed.
11. **Remote (29).** Done.
12. **Luck is never stated** (answered in this session's chat, 2026-11-21 22:3x, to the question whether stated odds include luck): "never stated. I already told you. it is a hidden mechanic. the player and the NPC-gods should be unaware of it's existence."
13. **Luck caps** (same exchange): odds stay within 5 to 95; in a contest between two gods the luck nets out and only the difference counts.
14. **Narrowest width** (same exchange): the overall shape; a thin neck of land is allowed.
15. **Mirror mode (94)** waits for build 5, opt-in: "Would you like to play mirror-mode, or in standard mode?"

## Shared specifications

- **Luck modifier.** Every god, player and NPC, has one, sealed, in `S/state/luck.md`: one line per god (the player's under `player`), a whole number from 0 (ordinary) to +5, with a dated history line for every change and its reason. It is set at the creation close of Night 2 (2.4) and again at 3a.1 for edges: each priced step a god took beyond what it bought adds one; refusing a power it was offered, or taking none, adds two per power; the Keeper logs the count. It never goes below 0 and is never told to anyone: not in any release, card, morning story or public file. It moves one step toward 0 when a god's growth reaches a tier in a god power (powers.md), never for craft, technology, wealth or numbers. Use: before any roll for that god or its people's acts, the Keeper lists luck as a factor and shifts the odds in the god's favor by 5 points on a d100 per step (or one face per step on a smaller die, never past certain), and in pass one, where the world's chance events choose among targets, weights them away from a lucky god's harm by the same steps. It is a factor on the record, never a judgment in the moment, and the neutrality check names it.
- **Travel by route and means.** Every trip is priced along the route the traveler chooses (road, path, river, open ground, sea), segment by segment, at the pace table's rate for the means (on foot, on horse, by wagon, by boat or barge), each segment by its ground. A trip with no traced route goes over open ground by the ground it crosses. Different routes to one place give different times. `engine/rules/time-and-pace.md` holds the rates by means and ground; `tools/map.py travel <campaign> <from> <to> --by foot|horse|wagon|boat [--via <id>,<id>]` prices it from the data and prints each segment; describe and the gazetteer use it. A place counts as on a route within half a mile of it.
- **Continent size.** The continent's land is at least 600 miles across at its narrowest and about 1,000 miles across on average (the Keeper aims for 800 to 1,200 average); the sheet's `miles_per_pixel` follows from the painted land, set at tracing. `tools/map.py validate` measures both from the traced land and the lock fails on a continent outside them.
- **Landing frame shows scale.** The first morning's (oog) map line names the frame's width in miles and says plainly that at this scale the god and what it sees sit on one mark.
- **Redraw only on change.** `tools/map.py draw` records a hash of the inputs in `map-meta.json` and, with `--if-changed`, keeps the existing `map.png` when nothing changed. The DM shows the latest map when asked and redraws only after a change to the player's map knowledge.
- **The unsaid want, sealed.** At the Day 2 close the DM writes the god's unsaid wants to `SPOILERS_do_not_open/campaigns/<name>/player/unsaid.md`, the one sealed file the DM may read and write (a named exception in dm.md and DESIGN), and keeps them out of the open conduct profile. The Keeper and the checker read it; no NPC god or civ agent does. Before acting on an unsaid want (in play or in the standing conduct the Keeper applies), the DM confirms with the player that it is still there, subtly in voice or plainly in (oog), and writes the date and the player's answer beneath it. A want unconfirmed for three played years is not acted on until confirmed.
- **Rulings route.** `SPOILERS_do_not_open/campaigns/<name>/rulings.md` (per campaign) holds rulings Michael gives in chat during a run. Only the orchestrator writes it, from his words, quoted, with the Pacific time and the question he answered. CLAUDE.md's run exception and every role file name it as carrying Michael's go for exactly what each entry says. No agent writes or edits it.
- **Names.** A place keeps its name; other names a god or anyone uses are recorded as aliases (map.json `aliases`, gazetteer) and never rename it. A name changes only when the people of the place come to use the new one, which the Keeper records as a dated fact.
- **Technology.** The starting level in DESIGN 4.7 is where the world begins, not a ceiling. A god may introduce what it knows; it is built in play, by the people, from materials the world has, at the pace of the work, and the DM asks how the god means it to be made. Nothing is granted by naming it.

## Assignment

Three agents work at once, each on its own files.

- **Agent E (engine text):** CLAUDE.md (items 55, 76); `engine/design/DESIGN.md` and `CHANGELIST.md` (all decisions); `engine/creation/*` (2 to 5, 18 to 25, 27, 43 to 48, 26); `engine/roles/*` (12, 49, 62, 76, 78, 26, 90, 91, 92); `engine/night/*` (84, 90, 76); `engine/rules/*`: powers.md (23, 24, 25, 32, 33, 34, 39, 44, 54 as ruling 18, 66, 90), map.md (59, 74 as 93, 80, 81, 86, 87, 92, 93), time-and-pace.md (93), morning-story.md (80, 81); `engine/style/*` (82); every ruling of 89 whose home is an engine file; the test README.
- **Agent T (tools):** `tools/lockcheck.py` (30, 67, 74, 83), `tools/map.py` (58, 60, 67, 74, 81, 86, 87, 93), `.github/workflows/paint.yml` and `tools/paint.py` (83), and tests for each.
- **Agent K (sealed):** `SPOILERS_do_not_open/keeper/` files: the creation runbook (7 to 14, 16, 31, 35 to 39, 52 to 57, 61, 65, 68 to 71, 75, 78, 84, 90, 91, 92, 93, and every ruling of 89 whose home is the runbook), the NPC god rubric (7, 8, 9, 10, 61, 90), the survey Keeper notes (13, 14), the mystery standard (67), the deep-lore notes and clue design (68, 70, rulings 28, 29, 31, 33, 34).

Each agent logs what it changed in `applied.md` under its own heading, by item number. Then an independent check (`build-check.md`), then fixes.
