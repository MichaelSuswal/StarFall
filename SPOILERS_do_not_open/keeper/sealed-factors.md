# The sealed factors: luck

> SPOILER WARNING: Keeper material. Players should not read this file.

The public engine says only that, where a roll is made, the Keeper applies "the sealed factors" after the stated odds. This file is what that means. It is read by the Keeper and the continuity checker, and by no other agent. Its rules come from change list item 90 (run 03) and Michael's decisions of 2026-11-21.

## Secrecy (Michael, 2026-11-21)

Luck is a hidden mechanic and is never stated. The player and the NPC gods must be unaware it exists. Its existence appears in no file the player, the DM, an NPC god agent or a civ agent reads: no engine file, release, card, sheet, morning story, public file or roll line they can see. The DM is never told it and never mentions it. The odds stated to the player, and argued with the DM, leave it out.

## The modifier

Every god, the player's and each NPC's, has a luck modifier, sealed in `S/state/luck.md` (runbook template 7.14): one line per god (the player's under `player`), a whole number from 0 (ordinary) to +5, with a dated history line for every change and its reason.

- **Earned.** A god earns it by taking heavier prices than it needs, or by refusing powers: each priced step taken beyond what it bought adds one; each power offered and refused, or a god taking none, adds two per power. The Keeper sets it at the Night 2 close (runbook 2.4) and again on Night 3a for edges (runbook 3a.1), and logs each count.
- **Bounds.** Never below 0, never above +5.
- **Moved back.** It moves one step toward 0 when a god's growth reaches a tier in a god power (`engine/rules/powers.md`), with a dated history line, in pass two of the night turn. Craft, technology, wealth and numbers never move it.

## Use

- **On a roll.** Before any roll the Keeper makes for a god or its people's acts, it works out the stated odds from the open factors (DESIGN 12.6), then applies luck after them: 5 points in the god's favor on a d100 per step, or one face per step on a smaller die. Luck is named in the roll's `--what` as a factor at its step, in the sealed roll log (`tools/roll.py --campaign <name>`), with the stated odds and the odds rolled both written there.
- **The clamp (Michael, 2026-11-21).** Odds with luck stay capped at 5 to 95, as every roll is (DESIGN 12.6). On a smaller die the shifted target leaves at least one face that fails and one that succeeds. Luck never makes a roll certain, and a thing certain or impossible by the open factors is not rolled at all.
- **A contest between two gods (Michael, 2026-11-21).** Where a roll sets one god or its people against another god or its people, the two gods' luck nets out and only the difference counts, toward the god with more. Equal luck shifts nothing.
- **Weighting.** In pass one, where a chance event chooses among targets (a weather year, a murrain, a schedule roll that chooses which people a natural harm falls on), the Keeper weights the choice away from a lucky god's harm by the same steps, logged as a factor. Where two lucky gods' peoples are among the targets, each is weighted by its own steps.
- **Not acts.** The table rolls that build a god or the world (leans, seeds, the star, the plane) are not acts and take no luck.
- It is a factor on the record, never a judgment in the moment.

## The Keeper's record

The neutrality self-check of every night and every turn names every roll or weighting where luck was a factor, by roll id and step. The keeper log's counts match `S/state/luck.md`.

## The checker's check

The continuity checker reads `S/state/luck.md`, the sealed roll log and the keeper log, and checks:

1. Every roll for a god with luck above 0, or for its people's acts, names luck in its `--what` at its logged step, with the stated odds and the odds rolled; every contest between two gods uses the difference only; no odds outside 5 to 95.
2. Every pass-one weighting of a chance event among targets names luck where it applied.
3. Every change in `S/state/luck.md` has its dated reason, matches the keeper log, and stays within 0 to +5; growth to a tier in a god power moved it one step toward 0, and nothing else moved it down.
4. No word of luck in any file the player, the DM, an NPC god agent or a civ agent reads: every public file, every release, card and sheet, every engine file. A hit is a flag.
