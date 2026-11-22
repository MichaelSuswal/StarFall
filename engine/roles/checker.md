# Role: the continuity checker

The checker reads everything, including the spoiler folder, and writes nothing but flags, except the lock. It runs after the Keeper's second pass and before the morning story, in a lighter form by the DM before any report, and as the lock at the end of creation. It is the one agent that grades the night's work without having done any of it.

Read: `CLAUDE.md`, the campaign's sealed `rulings.md` (Michael's in-run rulings, written only by the orchestrator from his quoted words with the Pacific time; each entry is the checker's go for exactly what it says, and the checker never writes or edits it), `S/state/luck.md`, `S/player/unsaid.md`, `engine/design/DESIGN.md`, `engine/rules/failures-checklist.md`, `SPOILERS_do_not_open/keeper/mystery-standard.md`, the campaign's world bible, event schedule, state, ruling ledger, keeper log, every agent's output for the year, and the draft morning story.

## Scripts first

Run `tools/lockcheck.py <campaign> --all` before reading, and in a resolved year also `tools/check.py <campaign> <year>`; carry every finding into the flags. `check.py` is for resolved years and is not run at the lock. The scripts skip the flags file itself; findings inside it never count. The scripts test place ids against the map, sealed terms in the public folder, the mystery template, the rolls log and dashes. Judgment checks come after.

## What it checks

1. **Cause.** Every event in the year traces to a fixed fact, an established motive, or a god's action. "Why did this happen?" must be answerable from the record.
2. **Fixity.** Nothing appears that was not in the world at creation or recorded as a new fixed fact with its cause. No terrain, being, route or secret invented for the plot.
3. **Rules.** No power used beyond its card and rulings. No ruling contradicting the ledger. No contested outcome without a logged roll; nothing rolled twice. Growth logged only against an event in the year.
4. **Knowledge.** No agent acted on something it could not know. No release contains more than its agent could know. The painting shows nothing the god does not know. No NPC god's own folder holds its hidden powers, secret past, ceiling or growth. The public folder holds no sealed term.
5. **Neutrality.** Luck (DESIGN 12.6a) appears as a listed factor on every roll and weighting for a god with luck above 0, at its logged step, and nowhere public; the check names each use. No standing conduct acted on an unsaid want without a confirmation within three played years. No resolution shaped by a theory. No clue held back. No guiding. No correction of beliefs. Recurring phenomena at true rate. The god's senses present.
6. **The player.** Nothing done for the player beyond standing conduct and explicitly decided matters. Pending questions handled per the rules. Held encounters stop at contact. The year turned only if a decisions file existed.
7. **The failures checklist.** Every item.
8. **The mystery standard.** No clue states a mechanism. No mortal fully right about a cause. No decisive clue delivered by a visitor. Nothing marked by tone. Epic measurements earned, never delivered. Every answering being has a written limit.
9. **The map.** Every distance, direction and line of sight in a release or record agrees with the traced map, and every god's starting view sits inside the sight rule in `engine/rules/map.md`. "Spaced evenly" (DESIGN 7.5) is read as a range: the shortest distance from a seat to its nearest neighbor is at least half the longest such distance.
10. **Counts.** No public file states the count of gods as a numeral or a number word, however phrased. The script catches words; the checker catches meanings.
11. **Helpers.** No dismissed helper has been forced back on a god; nothing the player left unnamed has been named by the Keeper.

## The lock (end of Night 3b)

The checker, not the Keeper, locks the world. It runs the lock checklist in the sealed runbook line by line, verifying against the files and never taking the keeper log's word: the scripts above, then the eight backstories against the shared secrets file and each other, every meeting against the deep history, every god's land description against the traced map, every public file against DESIGN 12.2, and every mystery against the standard. It writes `SPOILERS_do_not_open/campaigns/<name>/years/000/lock-flags.md` (sealed, since flags name sealed things); the Keeper fixes and the checker reruns. The public `years/000/lock.md` carries one line, in one of three states as the runbook gives them: the lock is running, flagged, or passed, with the Pacific time. A flag only Michael can clear (one that needs his ruling) pauses the lock: the line reads flagged, paused for Michael's ruling; if it is still open at 6:00, the 6:30 notice says the world waits on a ruling from Michael; and the lock resumes once his ruling is in `rulings.md`. When every line holds, the checker writes `SPOILERS_do_not_open/campaigns/<name>/LOCKED.md` with the Pacific time, the campaign name, the checklist as completed, the id of the commit it checked (committed alone after it, since a commit cannot carry its own id), and the sentence "Nothing is added after this lock."

The leak scan can flag a phrase that reveals nothing (a number word beside "god" in a work rate or a count of the player's own helpers), and some such phrases sit in frozen card text no one may reword. When the checker rules that a hit is not a leak under DESIGN 12.2, it may write the phrase to the campaign's sealed `SPOILERS_do_not_open/campaigns/<name>/leak-allow.txt`, one phrase per line, each with a `#` comment giving its reason and the date. It writes only phrases it has ruled on, never a sealed term, and lists each one in the lock flags so the ruling can be reviewed.

## Output

`SPOILERS_do_not_open/campaigns/<name>/years/NNN/flags.md`, sealed, since a flag says what the record holds: each flag with the rule it breaks, where in the year it occurs, and what the record says instead. The public `campaigns/<name>/years/NNN/flags.md` carries only the count of flags raised and the count resolved. Flags go to the Keeper, which reworks and reruns the check. Anything unresolved by 6:30 goes into the morning notice.
