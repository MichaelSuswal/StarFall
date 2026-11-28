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

## Sealed side (Agent K)

Applied 2026-11-27 under Michael's go of 19:37 Pacific (`build-plan.md`), in `SPOILERS_do_not_open/keeper/` only. Procedure only; no world content. Rulings are cited by their number in `rulings-to-rules.md` (pushed first, 8394fda).

### Files changed

- `year-turn.md`
  - Head: read in full every night, with the year's own records (item 30); build 8 sources named.
  - Section 1, decision 1: "The clock waits", in Michael's words, aligned with Agent E's `night-turn.md` (the world's year resolved once on its first night; no night resolves more than one year; `play_day` K; a night after the clock waited has no NPC god decide and writes the `-K` files). "A minor held moment": the Keeper judges and logs why before resolving; a prepared scene is never minor, nor a moment the player said it means to play, nor one a morning already told the player its story stands at; in doubt, held. "A play day covers at most one in-game year": no sheet, board or run-on reaches past it or past the clock's year. The build 7 line that the clock advances one year a night is gone; L-0056 is replaced.
  - Section 1, L-0051's two lines reconciled (rule 11): "Only the first is boarded" replaced by "Boards": every held moment known when the sheet is written is boarded, each later one conditional on the one before; the thread still stops at the first unplayed moment; no board past the in-game year. Section 2's board line and the public template agree.
  - Section 1, new bullets: running on past a board (item 20, rule 43); an answer given on a played day (rule 44); facts handed over from a live scene (rule 46); a roll already made stands (rule 12); asks and checker conditions past the moment wait (rule 3); a setup pass (rule 1); a campaign moved to a new build (item 7, rules 2, 4, 37 and 38, in the form `night-turn.md` gives, marking in place, the Keeper's sealed files included).
  - Section 2: the day sheet's days are the moment's own (rule 9); a name the Keeper gives leaves `sealed-terms.txt` the night after it is said in the god's hearing (rule 8); a world question left at the close (item 11, rule 18); new paragraph "Set before play" (items 8 and 18, rules 6, 17, 28 and 61: small world facts set before the sheet, every board range set by the Keeper, the DM rolls only the player's own attempts, nothing reshaped after its roll); a board lists the readings of the god's own powers and its "If play runs on" reach (items 20 and 21); world questions on a board replaced by the player's own attempts; common talk of another people's guest (rule 58). Both templates updated (later boards conditional, readings, "To roll" for the player's attempts only, "If play runs on", the private way, the `-K` file names).
  - Section 3.1: phenomenon months by a fixed season or month (rule 13); the telling to the god and the standing template line (item 28, rule 52); a release already read is corrected in pass two (rule 63).
  - Section 3.2: the decide release line for a report with no telling section (rule 10).
  - Section 5: the private way for a sealed act's result (item 17, rule 27); a setup pass carries out no act; a habit stands under `## Habit` (item 13).
  - Section 6: no ledger id for a card entry that restates a standing term (rule 39).
  - Section 7: a near miss is the world's question, with no sealed factor (rule 14).
  - Section 8: a hidden power or knack met in a live scene is read by the Keeper the next night, its condition never given to the DM (item 8); standing for a year not resolved whole (rule 22).
  - New section 9, small standing rulings: a die thrown in error (rule 19), a slip in the Keeper's release (rule 29), a factor found unsupported (rule 31), a conditional roll not made (rule 55), a random event's item (rule 51).
- `sealed-factors.md`: a near miss takes no luck (rule 14); every board range is set by the Keeper and given by branch, the DM rolling only the player's own attempts, and no range reshaped after its roll (item 18).
- `creation-runbook.md`
  - Item 1: 1.4 reads the player's months from its `Waking vote:` line.
  - Item 3: the closing release line drops the pull line; agents do not pull.
  - Item 4: template 7.1's stance line, in the rubric's words, never a price or drawback.
  - Item 5: the clock rule (all four starting lines, whoever makes the clock; `season_opens` written in 1.5 and confirmed in 3b.8); Night 1's Writes list and 1.5 Q3; 3b.8 confirms.
  - Item 6: the Night 1 heading has no number word beside "gods"; the send-back bar gains the example of rule 77; a follow-up no answer could move is not asked, logged; template 7.1's Rule line writes the kind out, never a pointer.
  - Item 13: `habit` among the kinds of `unsaid.md`, under `## Habit`.
  - Rule 85: a test run that stops before the lock closes with the next `creation_night` recorded (the clock rule and 1.9).
  - Decision 2: the Images standing rule, a morning painting covered only by the line naming its own morning.
  - Decision 3: travel priced in the direction actually travelled; line ends named by the places the tool gives, never `:start` or `:end` alone; a line priced one way never reused for the other.
- `survey-keeper-notes.md`: item 2, a first choice counts 2 and a second 1, the month with most carries, a tie by the interesting-game rule; the player's months from its `Waking vote:` line; `season_opens` written on Night 1. Item 6: a moot tie's variation roll is cast for the record. Rule 82: sub-point against extra in a vote answer. Rule 83: one body with a costly way to more counts with more than one.
- `npc-god-rubric.md`: item 4, the three stance bands and the Clever and Freedom marks in words with no price or drawback, said to be the sheet's words so the release carries the sheet whole (rule 76 superseded); item 6 and rule 75, the two rule-lean bands write the kind out with its meaning, no pointer to the table.
- `build7-check-sealed.md`: a closing status: both points it held as awaiting Michael were settled on 2026-11-25 and applied in build 7; nothing in it is open (rules 86 and 87).

### Not applied, or left for the build check

- Agent E's note for Agent K (the night after the clock waited) is applied in `year-turn.md` section 1 and the templates. Agent E's `night-turn.md` marker wording ("where it is kept") and `year-turn.md`'s ("kept where it stands") say the same under marking in place; the build check may want one wording.
- "A minor held moment": the three cases besides a prepared scene that are never minor, and "in doubt, held", are the Keeper's procedure for the judgment Michael gave it, not his words. For the build check to confirm.
- "A play day covers at most one in-game year" is read with the clock waiting as never reaching past the clock's year; Agent E's `dm.md` has the same bound.
- No campaign file was changed. sim-06's standing label allow (rule 36) is a campaign matter for its next night.
