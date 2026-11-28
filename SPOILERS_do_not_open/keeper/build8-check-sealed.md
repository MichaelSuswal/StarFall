> SPOILER WARNING: Keeper material. Players should not read this file.

# Build 8 (1.0): the build check, sealed detail

Companion to the public `tests/creation-sim/run-07/build-check.md`, 2026-11-27. Only what needs sealed detail is here. Findings, rulings and counts are in the public file.

## The rulings' coverage, by section

Every "Rulings for review" entry in the sections the build plan names was counted and matched to `rulings-to-rules.md`:

- sim-06 keeper log, run 07 setup: 9 entries, lines 1 to 9.
- sim-06 Year 4 night, steps 1 and 2: 10 entries, lines 10 to 19 (the search by weight is line 14; the second stick, asked of the council, is line 15).
- sim-06 Year 4 night, pass two: 10 entries, lines 20 to 29.
- sim-06 Year 4 night, the check: 3 entries, lines 28 (the chance range, settled at step 7), 30 and 31.
- sim-06 Year 5 night, steps 0 to 2: 10 entries, lines 42 to 51 (the fired piece under L-0037 is line 47, ledger L-0052).
- sim-06 Year 5 night, pass two: 8 entries, lines 52 to 60.
- sim-06 Year 5 night, the check: 3 entries, lines 61 to 63.
- sim-07 Night 1: 11 entries, lines 75 to 85.
- The Year 4 and Year 5 checker flags' "Rulings for review" (rounds 1 to 4 and 1 to 3): lines 32 to 41 and 64 to 71, each one either a rule, "as line N", or "No change" for a reason that holds.

Nothing missing and nothing doubled.

## Agent K's deleted section in applied.md

The section commit 551990b removed is at `git show 212ab64:tests/creation-sim/run-07/applied.md`, its lines 78 to 120. It holds procedure only, with nothing sealed in it, so it goes back in the public file as it was (public finding 1).

## The two sim-06 rides (item 25)

`python3 tools/map.py travel sim-06 f65:start f70 --by horse` and the reverse were run. Both give 117.6 miles, 5.9 days, over open ground, the same each way because no line with heights or a `pace` stretch is used. The `Ends:` line names the road's first and last points by their regions and grid cells (B2 and C2). No known place lies within 40 miles of either end, so the tool falls back to the region, as Agent T describes. The two ends read as different places on the face of the output, which is what item 25 asked for. The corrected Year 4 and Year 5 figures in the campaign record stand.

## Agent K's sealed edits, spot-checked

- `npc-god-rubric.md`: the stance bands and the Clever and Freedom marks no longer speak of prices or drawbacks (item 4). The two rule-lean bands write the kind out with no pointer (item 6, rule 75).
- `survey-keeper-notes.md`: first choice 2, second 1 (item 2); the `Waking vote:` line (item 1); a moot tie cast for the record (rule 78); rules 82 and 83.
- `creation-runbook.md`: no pull line in the closing release line (item 3). The standing permission line still allows a pull, which CLAUDE.md allows, so it does not contradict the template. Also `season_opens` written at 1.5 and confirmed at 3b.8 (item 5); 3a.5 "Lines priced by direction", using `heights_ft` and `pace` as `map.md` 5.1 names them.
- `sealed-factors.md`: the near miss (rule 14), and board ranges set by the Keeper by branch (item 18).
- `build7-check-sealed.md`: the closing status (rules 86 and 87). This was an edit to an earlier check's file by Agent K. The build plan's line 86 and 87 owner names that file, so the go covers it.
- `year-turn.md`: sections 1, 2, 3.1, 3.2, 5 to 9 as Agent K's log gives them. Public findings 7 and 15 are its two remaining fixes.
