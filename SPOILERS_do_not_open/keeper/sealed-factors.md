# The sealed factors: luck

> SPOILER WARNING: Keeper material. Players should not read this file.

The public engine says only that, where a roll is made, the Keeper applies "the sealed factors" after the stated odds. This file is what that means. It is read by the Keeper and the continuity checker, and by no other agent. Its rules come from change list item 90 (run 03), Michael's decisions of 2026-11-21, run 04 items 23, 43, 52 and 66 (approved 2026-11-22), and run 05 items 20, 31, 58 and 63 (approved 2026-11-23).

## Secrecy (Michael, 2026-11-21)

Luck is a hidden mechanic and is never stated. The player and the NPC gods must be unaware it exists. Its existence appears in no file the player, the DM, an NPC god agent or a civ agent reads: no engine file, release, card, sheet, morning story, public file or roll line they can see. The DM is never told it and never mentions it. The odds stated to the player, and argued with the DM, leave it out. Since the scan cannot know an ordinary word is sealed, every campaign's `S/sealed-terms.txt` carries the factor's name from Night 1, `!luck` and `!Luck`, each on its own line, the `!` marking a term the scan never exempts (runbook 1.1 and template 7.12). It never comes off the list, even where the player says the word at the table: that conversation stays sealed (Michael, 2026-11-22). The creation transcripts are the player's own words, kept verbatim, and the scan does not check them for it; it checks every other public file, so no agent ever writes it (runbook section 4).

## The modifier

Every god, the player's and each NPC's, has a luck modifier, sealed in `S/state/luck.md` (runbook template 7.14): one line per god (the player's under `player`), a whole number from 0 (ordinary) to +5, with a dated history line for every change and its reason.

- **Earned.** A god earns it by taking heavier prices than it needs, or by refusing powers: each priced step taken beyond what it bought adds one; each power offered and refused, or a god taking none, adds two per power. The Keeper sets it at the Night 2 close (runbook 2.4) and again on Night 3a for edges (runbook 3a.1), and logs each count.
- **What counts.** A power a god shrinks of its own accord, keeping it under its name, is not a power refused: the rule counts powers, not parts of one. A choice between prices the table itself offered as equal is the price, not a step beyond it, whichever is taken; so is the rung of a standing scale the god chooses. A slower, costlier return than the standing rungs, which a god (the player's or an NPC's) may take, priced by the DM or the Keeper, is a heavier price taken willingly and counts as a priced step beyond what was bought (Michael, 2026-11-23). Choosing the heavier side of a pair the table offered, a price against a narrower power, does not count: the pair is the table's own choice. A stricter wording a god asks for itself, beyond the price agreed, counts as a priced step. Bending or refusing a default (its helpers, most often) counts only when it is priced in its negotiation round (runbook 3a.1); unpriced, it counts nothing. "Taking none" counts only powers that were offered: a god offered nothing (one that proposed no edge, or whose ask was no power) has refused nothing and earns nothing for it.
- **Bounds.** Never below 0, never above +5.
- **Moved back.** It moves one step toward 0 when a god's growth reaches a tier in a god power (`engine/rules/powers.md`), with a dated history line, in pass two of the night turn. Craft, technology, wealth and numbers never move it.

## Use

- **On a roll.** Before any roll the Keeper makes for a god or its people's acts, it works out the stated odds from the open factors (DESIGN 12.6), then applies luck after them: 5 points in the god's favor on a d100 per step, or one face per step on a smaller die. Luck is named in the roll's `--what` as a factor at its step, in the sealed roll log (`tools/roll.py --campaign <name>`), with the stated odds and the odds rolled both written there.
- **The clamp (Michael, 2026-11-21).** Odds with luck stay capped at 5 to 95, as every roll is (DESIGN 12.6). On a smaller die the shifted target leaves at least one face that fails and one that succeeds. Luck never makes a roll certain, and a thing certain or impossible by the open factors is not rolled at all.
- **A contest between two gods (Michael, 2026-11-21).** Where a roll sets one god or its people against another god or its people, the two gods' luck nets out and only the difference counts, toward the god with more. Equal luck shifts nothing.
- **Weighting.** In pass one, where a chance event chooses among targets (a weather year, a murrain, a schedule roll that chooses which people a natural harm falls on), the Keeper weights the choice away from a lucky god's harm by the same steps, logged as a factor. Where two lucky gods' peoples are among the targets, each is weighted by its own steps. The method, on a `--die d100`: each target starts with an even share of the hundred; each step of a target's god takes 5 points from its share (never below 1); the points freed are spread evenly over the targets whose gods have no luck, or, if every target's god has some, over those with less; the bands are written in the log before the roll. Rounding: the freed points are divided by the number of targets that take them, in whole points; the remainder goes one point each to those targets in the order the log lists them, by label, alphabetically, so the bands always sum to a hundred. A people the same harm has already struck is removed before the cast (runbook 3b.6).
- **A fixed target.** A natural harm whose target the schedule fixes (one place, one people) and whose year is rolled takes no luck on the year: a year is not a choice among targets, and luck never moves a harm sooner or later. When the harm comes, any roll for how hard it falls on the people, or for what they save, is a roll for their acts and takes luck as any roll does.
- **Not acts.** The table rolls that build a god or the world (leans, seeds, the star, the plane) are not acts and take no luck.
- It is a factor on the record, never a judgment in the moment.

## DM rolls in play (Michael, 2026-11-22)

The DM rolls in the open on played days, with the stated odds, as the public engine gives it, and never knows of this file. Its roll lines in `P/state/rolls.jsonl` are never edited. There is no sealed re-roll of a DM roll. Resolving the year, in pass two, the Keeper reads the year's DM rolls and may overrule an outcome by the sealed factors, as a hidden stat would:

- **Which rolls.** Only a roll for an act of a god with luck above 0, or of its people, that failed by no more than the god's shift (5 points a step on a d100, one face a step on a smaller die), within the 5 to 95 clamp. In a contest between two gods, only the difference counts, toward the god with more. A success is never overruled, and nothing turns a roll against a god.
- **What it changes.** What the player was shown stays as shown, and nothing the DM narrated as seen is undone. The overrule falls on what follows from the roll in the world's year: the consequence the year carries is that of the success, where the told scene leaves room for it (what slipped away is found later, what seemed lost held, the blow told as glancing did its work).
- **How often.** At most once per god per played year: the first roll of the year, by roll id, that qualifies and whose told scene leaves room for it. It is a factor on the record, never a judgment: no qualifying roll is passed over by choice.
- **Record.** Logged in the sealed keeper log for the year, one line naming the DM's roll id, its stated odds, the shift and the outcome carried. `tools/roll.py` has no note option and is the only writer of either roll log, so nothing is added to the sealed or the public roll log for an overrule, and the DM's roll line stands as rolled. No public file names it, and the year's release and morning story show only the consequence, as any consequence is shown.

## The Keeper's record

The neutrality self-check of every night and every turn names every roll, weighting or overruled DM roll where luck was a factor, by roll id and step. The keeper log's counts match `S/state/luck.md`.

## The checker's check

The continuity checker reads `S/state/luck.md`, the sealed roll log and the keeper log, and checks:

1. Every roll for a god with luck above 0, or for its people's acts, names luck in its `--what` at its logged step, with the stated odds and the odds rolled; every contest between two gods uses the difference only; no odds outside 5 to 95.
2. Every pass-one weighting of a chance event among targets names luck where it applied.
3. Every change in `S/state/luck.md` has its dated reason, matches the keeper log, and stays within 0 to +5; growth to a tier in a god power moved it one step toward 0, and nothing else moved it down.
4. No word of luck in any file the player, the DM, an NPC god agent or a civ agent reads: every public file, every release, card and sheet, every engine file, the creation transcripts excepted, which are the player's own words kept verbatim and are not scanned for it. A hit is a flag, fixed by rewording (the Keeper's own replacement in a DM-owned file, runbook section 4), never by an allow line. The factor's name stands on the campaign's sealed term list on `!` lines.
5. Every overruled DM roll is a roll that qualifies by the rule above, the first such in its god's year, logged in the keeper log with its DM roll id, stated odds, shift and outcome carried; no DM roll line in the public roll log is changed.
