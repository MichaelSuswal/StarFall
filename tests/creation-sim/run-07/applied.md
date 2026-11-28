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

- The pace table has no rate for a climb against a descent on the same ground, so "uphill against downhill" (decision 3, build plan part 2) changes time each way only through the ground of each segment. A rate would go in `time-and-pace.md` and `tools/pace.py` together; I did not invent one. Stated as open in `time-and-pace.md` and DESIGN 10.1.
- Paintings for a further morning while the clock waits: `images.md` has no line for them, so they are held. Whether they are approved is spending, which waits for Michael.
