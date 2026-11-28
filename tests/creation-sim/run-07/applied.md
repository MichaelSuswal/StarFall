# Build 8 (1.0): what was applied

## Engine side (Agent E)

Applied 2026-11-27 under Michael's go of 19:37 Pacific (`build-plan.md`). Files: `engine/night/night-turn.md`, `engine/night/creation-nights.md`, `engine/night/scheduled-prompt.md`, `engine/design/DESIGN.md`, `engine/design/CHANGELIST.md`, `engine/roles/dm.md`, `keeper.md`, `civ.md`, `checker.md`, `engine/rules/morning-story.md`, `encounters.md`, `time-and-pace.md`, `map.md`, `failures-checklist.md`, `engine/creation/day1-world-survey.md`, `day2-the-god.md`, `README.md`, `tests/creation-sim/README.md`. `CLAUDE.md` needed no change. `tests/README.md` was not needed and was not created.

### Michael's decisions

- **Decision 1, the clock waits (items 15, 29).** Stated once in `night-turn.md` step 0 ("The clock waits until the story catches up"), replacing the build 7 lag rule there and ledger L-0056; DESIGN 10.5a states it as design. The mechanics it needs: the clock's `play_day` line (K), the play day's decisions file `player/decisions-NNN-K.md`, a new section "A night after the clock waited" (the world's year resolved whole once; NPC gods do not decide again; the player's civ agent works the stretch; short passes for whatever the stretch reaches), the morning `years/NNN/morning-story-<K+1>.md` while the clock waits, `years/NNN+1/morning-story.md` once the year ends, files suffixed `-K` (DM release and sealed companion, closing, flags), and the timing line "clock waited: year NNN open, play day K+1". Agreeing text: DESIGN 1.12, 2.7, 5.8; `morning-story.md` (path, held encounter, closing on a waiting night); `encounters.md` section 6; `dm.md` (morning path, decisions file naming, the played-moment section now `## Played at a held moment` with its date, the one-year bound on a play day); `keeper.md` Releases; `civ.md` step 5; `checker.md` item 6; `scheduled-prompt.md`; `time-and-pace.md` section 8; `README.md`.
- **Decision 1, a minor held moment.** Stated in `night-turn.md` step 0: the Keeper judges minor and logs why; a passed moment resolves by standing conduct and is told as what happened; a prepared scene is never minor. Agreeing text: DESIGN 10.5a, `encounters.md` section 6 (only the Keeper passes one; an unsure civ agent still holds), `morning-story.md`, `keeper.md`, `checker.md` item 6.
- **Decision 1, a play day covers at most one in-game year.** Stated in `night-turn.md` step 0 and DESIGN 10.5a and 1.12; `dm.md` close (a course past the year's end goes in the decisions file as decisions and standing conduct); `morning-story.md` (a morning tells at most one year).
- **Decision 2, paintings (item 14).** Engine side: `morning-story.md` section 2 and `night-turn.md` step 6 state that a play-year morning is approved only by the `images.md` line naming its own year, or by the standing `year morning painting: approved, one per played year` line for a year's first morning; a further morning while the clock waits needs a line naming its year and play day. The fix itself is Agent T's.
- **Decision 3, travel by direction (item 25).** `time-and-pace.md` (after the route paragraph, and the quick reference) and `map.md` 5.1: priced from the start place, segment by segment in the order travelled, the direction picking any directional rate, the tool naming line ends by place. Agreeing text: DESIGN 10.1, `checker.md` item 9.

### Run 07 items

- 1: `day1-world-survey.md` layouts, the `Waking vote: first <month>, second <month>` line; `creation-nights.md` Night 1 reads it.
- 2, 3, 4, 6: sealed (survey notes, runbook, rubric). Nothing in engine files.
- 5: `tests/creation-sim/README.md` step 1, the orchestrator's clock with every line; `creation-nights.md`, Night 1 writes `season_opens` when the month is decided (the runbook side is Agent K's).
- 7, 16: `night-turn.md`, new section "A campaign moved to a new build", in the form of rulings 2, 4 and 37; `keeper.md` points to it.
- 8: `keeper.md` Contests and chance (odds the Keeper prepares) and the sealed-terms line (ruling 8). The rest is `year-turn.md`, Agent K's.
- 9, 10, 19: no change, as proposed.
- 11: `dm.md` close and Held moments: a world question with no turn left goes in the decisions file with the odds the DM would have stated; `keeper.md` rolls it the next night (ruling 18).
- 12: watch, recorded only.
- 13: `day2-the-god.md` kinds gain `## Habit`; `dm.md` Sealed parts in play.
- 14: engine side under decision 2; tools are Agent T's.
- 15, 29: decision 1.
- 17: `dm.md` Sealed parts in play (the `PRIVATE:` line, relayed privately, recorded under `## Act`) and `scheduled-prompt.md` (the night puts a sealed act's result only in `dm-sealed.md`). The installed scheduled task's own prompt is not changed; updating it needs Michael's go.
- 18: `night-turn.md` step 4, `dm.md` Held moments, `keeper.md`, in the form of rulings 6 and 28 (the Keeper rolls a board's chance outcome for the player's people before play and gives it by branch as a fact).
- 20: `dm.md` Held moments, in the form of ruling 43.
- 21: `night-turn.md` step 4 and `keeper.md` Releases (a board lists the readings of the god's own powers and senses); `dm.md` (a reading the board lacks is a world question).
- 22: `dm.md` The day, item 5.
- 23: tools (Agent T). `dm.md` already gives the `--who` form; nothing in engine files.
- 24: `dm.md` The day, item 4 (append-only, never written from the latest post alone, section count checked); the `check.py` test is Agent T's.
- 25: decision 3; the tool change is Agent T's.
- 26: tools (Agent T). Nothing in engine files.
- 27: `failures-checklist.md` check 22, "A result reshaped after its roll"; `keeper.md`; `checker.md` item 6.
- 28: `civ.md` step 6 and `night-turn.md` steps 0 and 2 (the standing line in every civ release; the decide release copies an unsettled attempt only as tried).
- 30: `keeper.md` read list: files read in full each night named, heading reads allowed for creation-only files.

### Rulings (`rulings-to-rules.md`), engine lines

- 2, 4, 37 (with 16, 30, 32, 38 as parts of it): `night-turn.md` "A campaign moved to a new build"; `keeper.md` one line pointing to it.
- 5, 26: `keeper.md` Contests and chance, and DESIGN 12.6 aligned (the sealed factors enter the Keeper's own rolls only, never odds the DM states or a DM roll). DESIGN 12.6 was not named in the line but said the opposite, so it was aligned too.
- 6, 28: `keeper.md`, `dm.md`, `night-turn.md` step 4 (item 18).
- 8: `keeper.md`, the sealed-terms line.
- 11: `night-turn.md` step 4 and `dm.md` (conditional boards for later known held moments, the thread still stopping at the first unplayed one). Owned by `year-turn.md`; the public frame was aligned so the engine does not contradict it.
- 18: `dm.md` and `keeper.md` (item 11).
- 27, 41: `dm.md` and `scheduled-prompt.md` (item 17).
- 42: `dm.md` (item 24).
- 43: `dm.md` (item 20).
- 49, 60, 74: superseded by decision 1, applied in `night-turn.md` step 0.
- 61: `failures-checklist.md` check 22 (item 27).
- 62, 69: `time-and-pace.md` and `map.md` (decision 3).
- 85: `creation-nights.md` (a test run that stops before the lock is closed with the next `creation_night` recorded; Night 1 writes `season_opens`).
- 40: no change, as the line says (`morning-story.md` already gives the held painting's (oog) line).
- Every other line is sealed or tool only, or "No change".

### Version

`CHANGELIST.md` section "Build 8: 1.0, after the short check run 07", with each reversed decision struck through. `README.md` opens with "Version 1.0 (build 8, 2026-11-27)". DESIGN names 1.0 in its opening paragraph and in 1.13 (0.1 kept as history).

### For Agent T (tools)

- `check.py`: the engage check and the clock must accept `play_day: K` and `player/decisions-NNN-K.md` on a night after the clock waited, and the files suffixed `-K` (`releases/NNN/dm-K.md`, `S/releases/NNN/dm-sealed-K.md`, `years/NNN/closing-K.md`, `years/NNN/flags-K.md`, `years/NNN/morning-story-K.md`); the timing check must accept "clock waited: year NNN open, play day K+1" as well as "clock advanced".
- `paint.py` and `check.py`: approval of `<campaign>-NNN-morning-K.json` (a further morning in a waiting year) only by a line naming its year and play day, never by the year's own line or the standing one-per-played-year line.
- `map.py`: `travel` and the gazetteer name each line's ends by place, as `map.md` 5.1 now says.

### For Agent K (sealed)

- `year-turn.md` section 1: the night after the clock waited, as `night-turn.md` now frames it (no NPC god decide on such a night; `play_day`; the `-K` file names).

### Gaps for the build check

- Climb against descent: closed by the coordinator's instruction after Agent T's commit 38e0f70, under the same go. Naismith's rule (+1 hour per 2,000 feet climbed in the direction travelled, a tenth of a ten-hour travel day; descent +0; nothing on water), applied where a line carries `heights_ft` or a per-direction `pace`, which `map.py` reads, is now in `time-and-pace.md` (beside the table, after the route paragraph, and in the quick reference), DESIGN 10.1 and `map.md` 5.1 (which also names the two line fields). The same hour on horse and with a cart is Agent T's reading, noted as such in `time-and-pace.md`, for the build check.
- Paintings for a further morning while the clock waits: `images.md` has no line for them, so they are held. Whether they are approved is spending, which waits for Michael.

## Tools (Agent T)

Applied 2026-11-27 under Michael's go of 19:37 Pacific (`build-plan.md`), with Agent E's notes for the tools. Files: `tools/paint.py`, `tools/check.py`, `tools/map.py`, `tools/pace.py`, `tools/lockcheck.py`, `tools/roll.py`, `tests/tools/test_tools.py`, `tests/tools/README.md`. Tests: `python3 tests/tools/run.py`, 96 passed, 0 failed (pytest the same), ten of them new (`test_build8_*`) and five older ones brought to the new rules.

### Items

- **14, decision 2 (paintings).** `paint.py` `covered()` and `kind_words`: a play-year morning is approved only by a line that names its own year (`Year 2 morning painting: approved` covers Year 2 and no other; a year in figures or words, in the label or the value), by the request's own id, or by the standing `year morning painting: approved, one per played year` line, which names every played year (as Agent E's `morning-story.md` gives). A morning line that names no year and no per-year count covers no play-year morning. `check.py` reads approval through `paint.covered()`, so both read it the same way. Tested: a Year 5 morning is not approved by a "Year 2 morning painting: approved" line; the sim-06 held Year 5 and Year 6 requests are not approved, in both tools; the sim-06 Year 2 to 4 mornings still are.
- **14, Agent E's note (a waiting year's further morning).** `<campaign>-NNN-morning-K.json` is approved only by a line naming its year and its play day (`Year 5 morning painting, play day 2: approved`) or its own id; the year's own line and the standing line never approve it, and a line naming another play day does not approve the year's first morning. Found on the way: an id in a label was matched as a substring, so a line for `zz-005-morning-2` would have approved `zz-005-morning` (and a repaint id its original); ids are now matched whole.
- **24 and ruling 42.** `check.py` reads the year's transcript's committed versions (`git log`) and fails it when its `## ` count falls between two commits, or when the working file is shorter than its last committed version. A fall that a later commit restored, every committed section standing in the file now, is a note, not a finding (a ruling of this agent's, for review: without it the restored sim-06 Year 5 transcript would fail every check for ever). Tested in a scratch git repository.
- **25, decision 3 and rulings 62, 69 (travel by direction).** `map.py travel` prices a line segment by segment in the direction travelled: a river by boat downstream toward its mouth and upstream toward its source, as before; a line's optional `pace` stretches (`{"from": i, "to": j, "forward": row, "back": row}`, a pace table row for each direction) for anything the table has a row for; and a line's optional `heights_ft` (one height per point) for a climb, by Naismith's rule. Every route segment says which end it travels toward, a `:start` or `:end` end is named by its place, and an `Ends:` line names both ends of every line used (the nearest known place within 3 miles, else the nearest within 40 with distance and bearing, then the region and grid cell; only names the god knows). The gazetteer names line ends by their places, and its Travel by route gives each way its own figure ("either way" when they agree). `validate` checks the form of `pace` and `heights_ft`. Tested a route both ways (road by its `pace` stretch and by its heights, river by boat, a bank walk).
- **25, Agent E's note (climb against descent).** The map data carries no height along a line: regions carry an elevation range, which says nothing of where a line runs, and no campaign's lines carry heights. So the tool does not read heights from regions; it takes them only from a line's own `heights_ft`, and no existing price changes. The rule, stated in `tools/pace.py` (docstring, `climb_days()`, `travel --climb FEET` and its help): Naismith's rule (1892), one hour added for every 2,000 feet climbed in the direction travelled, a descent adding nothing; a travel day being ten hours of movement, each 2,000 feet climbed adds a tenth of a day, on foot, on horse or with a cart alike, before the god's endurance, laden, group, season and weather (which bend only miles a day); none on water. For Agent E: `time-and-pace.md` should carry the same rule beside its table and quick reference (for example "Climb: +1 hour per 2,000 feet climbed (Naismith); descent +0; 10 hours a travel day"), since the table and `pace.py` must match. Applying the same hour to horse and cart is this agent's choice, for review; Naismith wrote it for walkers.
- **Decision 1, Agent E's note (the clock waits).** `check.py`: the clock's `play_day: K` (2 or more, only with status open); the night's play day from `--play-day`, else the clock (its `play_day` at steps 4 and 7; after step 8 a clock that waited reads K+1); play day K's files `player/decisions-NNN-K.md` and `releases/NNN/dm-K.md`; the night's morning either `years/NNN+1/morning-story.md` (the clock advances and carries no `play_day`) or `years/NNN/morning-story-<K+1>.md` (the clock stays on NNN with `play_day: K+1`), with its request named to match; a morning request in `images/requests/` that `images.md` does not approve is now a finding too; the timing line "clock waited: year NNN open, play day K+1" is the night's own and not a waited day, and no date may hold two of a waited day, a clock advance and a clock that waited. The sealed companion `dm-sealed-K.md` and `closing-K.md` are not checked, as `dm-sealed.md` and `closing.md` were not before.
- **26 and ruling 68.** `lockcheck.py` `is_flags_file()` takes the path and skips every `years/NNN/flags.md` (every mode, as its docstring says of the checker's files), with a test; `years/000/flags.md` included, which an older test had kept scanned.
- **23.** `roll.py`: `--help` and the docstring give `--who "<party>, rolled by the dm"` (the party whose attempt it is, or plain `dm`), as `engine/roles/dm.md` does. The tool still accepts any `who` with the word dm in it for `--public`; `dm.md` says it refuses any other form. Left as it was (build check C5's text), for the build check.
- Other items: none of 1 to 13, 15 to 22 or 27 to 30 lands in `tools/`. `rulings-to-rules.md` gives the tools lines 42, 62 (with 69) and 68, all applied above.

### The two sim-06 rides (item 25), reported only

No campaign file was edited. The road the rides used carries no `pace` and no `heights_ft`, so the figures do not change; what changes is that the output now says where each end lies. `travel sim-06 f60 f65:end --by foot` (the Year 4 figure) still gives 68.2 miles, 4.9 days, and `travel sim-06 f65:end f70 --by horse` (the Year 5 first figure) still gives 239.4 miles, 12.7 days; but each now prints the end it used as the road's last point (:end) with its region and grid cell, and an `Ends:` line naming both ends the same way, so the two ends read as different places and a ride priced from the wrong one shows on its face (the names are in the sealed record, not here). The corrected figures stand: `f60 f65:start --by foot --via f65` 148.1 miles, 7.4 days; `f65:start f70 --by horse` 117.6 miles, 5.9 days; the segment along the road now says it travels toward the first point, by its region.

### Closing runs

- `python3 tools/lockcheck.py sim-06 --all`: 0 failures (places 98 warnings, leaks 1, releases 8, rolls 1). Before: places 1 failure, the bracketed word in `S/years/004/flags.md`, now skipped (item 26). Warnings unchanged.
- `python3 tools/check.py sim-06 5`: 0 findings, 4 notes. Before: 1 finding, the held Year 6 morning called approved by the Year 2 line (item 14); it is now a note (held, not approved). New notes: the Year 5 transcript fell twice between commits and was restored (item 24).
- `python3 tools/lockcheck.py sim-07 --leaks --dashes`: 0 failures, 0 warnings.

### For others

- Agent E (`engine/rules/time-and-pace.md`): the climb rule above, beside the table and in the quick reference; and, if wanted, a sentence in `map.md` 5.1 naming the line fields `pace` and `heights_ft`.
- Agent K / the Keeper (`SPOILERS_do_not_open/keeper/`): when a map is drawn, a road over a pass may carry `heights_ft` (and a line any directional `pace` stretch); nothing in the sealed files needs it today.
- Campaign files: none edited. sim-06's records of the two rides were corrected by the Keeper in Year 5 and stand.
