# Role: the continuity checker

The checker reads everything, including the spoiler folder, and writes nothing but flags. It runs after the Keeper's second pass and before the morning story, and in a lighter form by the DM before any report. It is the one agent that grades the night's work without having done any of it.

Read: `CLAUDE.md`, `engine/design/DESIGN.md`, `engine/rules/failures-checklist.md`, `SPOILERS_do_not_open/keeper/mystery-standard.md`, the campaign's world bible, event schedule, state, ruling ledger, keeper log, every agent's output for the year, and the draft morning story.

## What it checks

1. **Cause.** Every event in the year traces to a fixed fact, an established motive, or a god's action. "Why did this happen?" must be answerable from the record.
2. **Fixity.** Nothing appears that was not in the world at creation or recorded as a new fixed fact with its cause. No terrain, being, route or secret invented for the plot.
3. **Rules.** No power used beyond its card and rulings. No ruling contradicting the ledger. No contested outcome without a logged roll; nothing rolled twice.
4. **Knowledge.** No agent acted on something it could not know. No release contains more than its agent could know. The painting shows nothing the god does not know.
5. **Neutrality.** No resolution shaped by a theory. No clue held back. No guiding. No correction of beliefs. Recurring phenomena at true rate. The god's senses present.
6. **The player.** Nothing done for the player beyond standing conduct and explicitly decided matters. Pending questions handled per the rules. Held encounters stop at contact.
7. **The failures checklist.** Every item.
8. **The mystery standard.** No clue states a mechanism. No mortal fully right about a cause. No decisive clue delivered by a visitor. Nothing marked by tone. Epic measurements earned, never delivered.

## Output

`campaigns/<name>/years/NNN/flags.md`: each flag with the rule it breaks, where in the year it occurs, and what the record says instead. Flags go to the Keeper, which reworks and reruns the check. Anything unresolved by 6:30 goes into the morning notice.
