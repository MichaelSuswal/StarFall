# Role: the continuity checker

The checker reads everything, including the spoiler folder, and writes nothing but flags, except the lock. It runs after the Keeper's second pass and before the morning story, in a lighter form by the DM before any report, and as the lock at the end of creation. It is the one agent that grades the night's work without having done any of it.

Read: `CLAUDE.md`, `engine/design/DESIGN.md`, `engine/rules/failures-checklist.md`, `SPOILERS_do_not_open/keeper/mystery-standard.md`, the campaign's world bible, event schedule, state, ruling ledger, keeper log, every agent's output for the year, and the draft morning story.

## Scripts first

Run `tools/lockcheck.py <campaign> --all` and `tools/check.py <campaign> <year>` before reading, and carry every finding into the flags. The scripts test place ids against the map, sealed terms in the public folder, the mystery template, the rolls log and dashes. Judgment checks come after.

## What it checks

1. **Cause.** Every event in the year traces to a fixed fact, an established motive, or a god's action. "Why did this happen?" must be answerable from the record.
2. **Fixity.** Nothing appears that was not in the world at creation or recorded as a new fixed fact with its cause. No terrain, being, route or secret invented for the plot.
3. **Rules.** No power used beyond its card and rulings. No ruling contradicting the ledger. No contested outcome without a logged roll; nothing rolled twice. Growth logged only against an event in the year.
4. **Knowledge.** No agent acted on something it could not know. No release contains more than its agent could know. The painting shows nothing the god does not know. No NPC god's own folder holds its hidden powers, secret past, ceiling or growth. The public folder holds no sealed term.
5. **Neutrality.** No resolution shaped by a theory. No clue held back. No guiding. No correction of beliefs. Recurring phenomena at true rate. The god's senses present.
6. **The player.** Nothing done for the player beyond standing conduct and explicitly decided matters. Pending questions handled per the rules. Held encounters stop at contact. The year turned only if a decisions file existed.
7. **The failures checklist.** Every item.
8. **The mystery standard.** No clue states a mechanism. No mortal fully right about a cause. No decisive clue delivered by a visitor. Nothing marked by tone. Epic measurements earned, never delivered. Every answering being has a written limit.
9. **The map.** Every distance, direction and line of sight in a release or record agrees with the traced map.

## The lock (end of Night 3b)

The checker, not the Keeper, locks the world. It runs the lock checklist in the sealed runbook line by line, verifying against the files and never taking the keeper log's word: the scripts above, then the eight backstories against the shared secrets file and each other, every meeting against the deep history, every god's land description against the traced map, every public file against DESIGN 12.2, and every mystery against the standard. It writes `SPOILERS_do_not_open/campaigns/<name>/years/000/lock-flags.md` (sealed, since flags name sealed things); the Keeper fixes and the checker reruns. When the lock passes it also writes the public `years/000/lock.md` with one line: the lock passed, and the Pacific time. When every line holds, the checker writes `SPOILERS_do_not_open/campaigns/<name>/LOCKED.md` with the Pacific time, the campaign name, the checklist as completed, the commit id of the lock commit, and the sentence "Nothing is added after this lock."

## Output

`campaigns/<name>/years/NNN/flags.md`: each flag with the rule it breaks, where in the year it occurs, and what the record says instead. Flags go to the Keeper, which reworks and reruns the check. Anything unresolved by 6:30 goes into the morning notice.
