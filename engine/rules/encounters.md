# Rules: encounters and odds

How any uncertain outcome is given odds and rolled, how the player argues odds, how the god behaves in time the player did not play, and how encounters in that time are either resolved at night or held for the player. Binding on the DM, the Keeper, every NPC god agent and every civ agent. Sources: DESIGN.md 5.8, 10.4 to 10.7, 12.6, 13.1.

## 1. What is rolled

A roll decides an outcome that is uncertain and contested: a fight, a chase, a search, a persuasion, a crossing, a craft attempt with a real chance of failure, a hazard on a message's route, a random world event. A roll is not used for anything certain or impossible (12.6): a god does not roll to lift a cup, and a mortal does not roll to leap a river. The agent states which it is and moves on. If the player disputes that something is certain or impossible, the dispute is an appeal under section 4 and the DM takes it seriously.

Only `tools/roll.py` rolls (12.6). Every call is appended to `state/rolls.jsonl` before the result is shown. No agent uses any other source of chance, including its own judgment of "probably." The checker flags any contested outcome with no logged roll and anything rolled twice.

## 2. Odds from factors

Odds are the chance of success out of 100 for the party whose attempt is being rolled. They start at even, 50, and move by named factors (12.6).

Steps are fixed:

- small: 5
- moderate: 10
- large: 20

A factor is a named circumstance in the world, written as `name=+step` or `name=-step`. Factors are open-ended: any circumstance in the record may be a factor, and a factor that applies in one case may be absent or reversed in another (12.6). The design names the usual kinds: numbers, ground, preparation, surprise, skill and craft, powers, condition, and any other circumstance. A circumstance is a factor only if it is in the record or plainly in front of the god in the scene; an agent may not invent a factor.

The sum is clamped between 5 and 95 (12.6). Nothing contested is ever certain. If the factors would push past the clamp, the agent should ask whether the thing is really contested at all; if it is not, do not roll.

A ruling may set a step other than 5, 10 or 20 for a specific power or circumstance (roll.py accepts other values when a ruling says so). That ruling is cited in the factor name.

### Procedure

1. The agent writes out, before rolling, what is being attempted, by whom, and what success and failure each mean. In a scene the DM states this to the player: costs, risks and odds first, nothing resolves until the player commits (10.5).
2. The agent lists every factor with its step and the fact in the record it comes from.
3. The agent sums, clamps, and states the odds. In a scene the DM gives the player the odds and the factors in (oog).
4. The player may argue (section 4). The odds are recalculated if the argument is accepted.
5. The agent calls `roll.py` with `--who`, `--what` and every factor. The log line is written before the result prints.
6. The agent reports the outcome only. Dice are hidden from the player (12.6). The DM never says the number rolled, never says "you rolled a 73," never shows the margin. It says what happened in the world.

Each roll's `--what` is specific enough that the checker can match it to a moment in the year: "raid on the salt ford, night 3, attackers' approach," not "raid."

## 3. One roll, one outcome

A roll is never redone after its result is known (12.6). Not for a mistaken factor found afterward, not because the agent dislikes the result, not because the player objects. If a factor was wrongly included or omitted and the roll has already happened, the DM says so in (oog), logs the error in `player/corrections.md`, and the result stands; the correction applies to the next roll of its kind. If the error changed what the roll was about (wrong attempt rolled, wrong party), the Keeper may rule that the roll did not apply to anything and a different attempt is rolled fresh; the Keeper records the ruling and the checker sees both rolls with the ruling beside them.

Big contests are not one roll. A siege of several nights is several rolls, one per contested moment, each with its own factors, as in the original's wolf siege (1.6). The DM breaks a contest into the moments where something could go either way and rolls each.

## 4. Arguing the odds

The player may argue factors with the DM in (oog) before the roll, never after (12.6). The player may argue that a factor is missing, that one does not apply, or that a step is the wrong size. The argument must point to something in the record or in the scene.

- The DM accepts an argument that the record supports and recalculates. The recalculation is written into the roll's factors; the old list is not rolled.
- The DM declines an argument the record does not support and says why in one line.
- If the player and the DM disagree on whether the record supports it, the DM puts it to the Keeper as a ruling (`powers.md` section 2) and the roll waits. If the scene cannot wait, the DM rolls with the factors as it has them, says that the question is going to the Keeper, and a ruling in the player's favor applies to all later rolls of that kind. It does not reopen this one.

A successful appeal recalculates. It never rerolls (12.6). If the roll has been made, there is nothing to appeal; there is only a correction for next time.

NPC gods and civ agents argue factors with the Keeper in the night turn the same way, in their own case, and the Keeper decides.

## 5. Standing conduct in unplayed time

The player does not play every hour of the year (1.7, 10.4). In the time the player did not play, the avatar follows standing conduct (10.6):

1. **What the player set.** `player/conduct.md` holds the player's standing instructions, in their words: where the god is, what it is doing, how it responds to strangers, to threats, to its own people's requests, to news. The player may set these at any time and the DM confirms them back. A scheduled action ("in autumn I go to the ford") is standing conduct for that time.
2. **Else, the conduct profile.** `player/conduct-profile.md`, kept by the DM from the player's choices, musings and answers (10.7). It describes how this god acts: what it fears, what it protects, how it treats the unknown, how it speaks.
3. **Default, under both: cautious and in character, never reckless.** Where neither source speaks, the god does the careful version of what this god would do. It does not start fights, does not accept offers, does not give away anything of its own, does not cross into unknown ground, does not use a power in a new way, does not make a promise. It watches, withdraws if threatened, and holds the matter for the player.

Standing conduct is never a licence for the DM or the civ agent to act for the player (13.1). It is the narrowest reading of what the player already decided. Anything that would be a decision the player has not made is not resolved by conduct; it is held (section 6).

The NPC gods have no unplayed time; their agents decide the whole year. Their peoples and the player's people act under their civ agents' own will (5.7), not under conduct.

## 6. Minor and major encounters

An encounter is anything that reaches the god in unplayed time: a traveler, a beast, a messenger, a storm on the road, a quarrel among its people brought to it, a sign. The civ agent, resolving the player's people's year (night-turn.md 3), and the Keeper in pass two, sort each one.

### Minor

An encounter is minor when standing conduct answers it completely and the answer costs the god nothing it would want to weigh: a merchant greeted and passed, a storm waited out, a path chosen between two known ways, a petitioner heard whose request the player has already decided on. Minor encounters resolve at night by conduct (10.6). Where a minor encounter has an uncertain outcome (the god is caught in the rain crossing a stream), it is rolled with factors like any other. The morning story reports minor encounters briefly or not at all, as the god would recall them.

### Major

An encounter is major when any of these holds:

- it would require a decision the player has not made (an offer, a demand, a question, a stranger god, a chance to use a power);
- it threatens the god's body, freedom or people in a way that could change the year;
- it involves another god, a god's envoy, or a world-level figure placed by the Keeper (9.1);
- it is a pending question (12.9) reaching the god in person;
- the player has marked this kind of event as one they want to play;
- the agent is unsure. Unsure means major.

A major encounter is held (10.6). The civ agent and the Keeper resolve the year up to the moment of contact for that thread and stop it there. Everything else in the year that does not depend on the outcome continues. The Keeper writes the held encounter into the DM's release with the board as it stands: where the god is, what it can see, hear and know, who is present, what has just happened.

The morning story stops at the moment of contact (10.6). The DM writes the year up to that moment, then the board, then waits. The player plays it live as a scene, odds stated before any commitment (10.5). The outcome of the scene goes into the player's decisions for the following night, and the civ agent and the Keeper resolve its consequences into the rest of that held thread then. Time inside the held encounter is the scene's own; the world does not wait for it elsewhere.

If a year has more than one major encounter, each is held at its own moment and the morning story presents them in order; the player plays them in order, and the DM says plainly in (oog) that more than one is waiting. If a held encounter's consequences would have changed something already resolved in the same year, the Keeper notes the dependency in the release, and the DM tells the player which parts of the summary are provisional.

## 7. Example factors

These are examples of the kind and size of factor, not a fixed list. Every factor used must be in the record for the case at hand.

| Situation | Factor (for the attempting side) | Step |
|---|---|---|
| Raid | Outnumber the defenders two to one | +10 |
| Raid | Defenders behind a built wall or on high ground | -20 |
| Raid | Attack at night, defenders unwarned | +20 |
| Raid | Defenders warned by a scout or a sign | -10 |
| Raid | Attackers hungry or on a long march | -5 |
| Raid | A god's power bears on the fight, per its card | +10 or +20 as ruled |
| Negotiation | Envoy speaks the other side's language well | +5 |
| Negotiation | Other side owes a debt or fears the sender | +10 |
| Negotiation | Other side was deceived by the sender before, and knows it | -20 |
| Negotiation | A gift the other side wants is on the table | +10 |
| Negotiation | Asking for something the other side's code forbids | -20 |
| Chase | Pursuers mounted, quarry on foot | +20 |
| Chase | Quarry knows the ground, pursuers do not | -10 |
| Chase | Darkness or heavy weather | -10 |
| Chase | Quarry wounded or burdened | +10 |
| Chase | Fresh tracks in snow or mud | +5 |
| Search | Searchers know roughly where to look | +10 |
| Search | The thing is hidden by someone who meant to hide it | -20 |
| Search | Many searchers over several days | +10 |
| Search | A god's sense bears on it, per its card | +5 or +10 as ruled |
| Search | Searching unknown or hostile country | -10 |
| Craft attempt | Craftsman has done this kind of work before | +10 |
| Craft attempt | Working beyond the people's known technology (4.7) | -20 |
| Craft attempt | Good materials and tools in store | +5 |
| Craft attempt | Rushed, or done in bad season | -10 |
| Craft attempt | A failed attempt last year that was learned from | +5 |

Read the table from the attempting side. A factor that helps the defenders is written as a minus for the attacker. When both sides have a stake, roll once for the side whose action began the contest, and read failure as the other side's success.
