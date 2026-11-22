> SPOILER WARNING: Keeper material. Players should not read this file.

# Mystery standard (v3)

The rules every mystery, clue and morning story must satisfy. Keeper material.

1. No clue states a mechanism. Clues show effects, objects and behavior. A mortal who explains a cause is always wrong about something important.
2. Every clue admits more than one reading. No planted counter-clues. The evidence itself fits several explanations. Solving a mystery means choosing a branch, acting on it, and seeing what the world does in response.
3. Most of the world is not a clue. Beautiful places, ordinary strangeness, customs, weather, animals exist because the world exists, and are there to be appreciated. A mystery may sit anywhere, public or secret, but it was placed at creation. Nothing is planted after the world locks. A morning story is mostly world and only partly mystery, and nothing in tone marks which is which.
4. The decisive clue is earned by action, never delivered by a visitor.
5. Confidence target: a careful player sits at 40 to 60 on the central questions for most of a campaign and reaches 80 only by acting on a theory and seeing the result.
6. The world answers actions clearly, including wrong branches and restraint. A wrong branch costs time and teaches something. It does not punish forever.
7. Every truth has a body (a place, a being, an event). Every mystery has a cost if ignored, tied to a clock or trigger. Every event has a traceable cause.
8. Clues and secrets are never held back. Everything is placed at creation and is findable from the moment it exists. A god that focuses more energy on a problem, or is cleverer, finds things sooner. The pacing spine is a forecast, not a gate.
9. The world neither guides a god away from a bad conclusion nor supports it. Facts fall as they may. No second wrong cause is planted beside a true sighting to reopen it, and no clue is added later to rescue a line that went quiet. A god discovers its own errors by acting on them.
10. The DM never corrects a god's beliefs about the world. It may, out of game, challenge the player's musings with questions, so the player thinks again. It does not supply the answer.
11. Some things are never discovered. Treasures, secrets and histories may sit unfound for a whole campaign. That is richness, not failure.
12. The world is fully thought out before day one, including a specific deep history: the rise and fall of cities and towns, and individual stories, written concretely at creation. Finding them is hard or a matter of chance.
13. Mysteries are layered by time scale and power. A campaign has about one epic mystery threaded through the whole of it, whose answer still has to be executed by someone once found; several long mysteries or quests at about half the epic's span, possibly related; and many short ones of 3 to 12 years, local and mortal. The epic and the long ones involve immortal power: the other gods, older beings, and the politics between them, and may not be solvable by one god alone.
14. The epic's central measurements are earned, never delivered by a scheduled letter, envoy or visitor. A god learns them by its own instrument, a counter it sent, an alliance it made, or a place it went.
15. The Keeper always reports the god's own senses when they would occur. On any open question that outlasts a session (an envoy's question, a letter, an offer), the Keeper asks the player rather than inferring an answer or supplying an intent. The Keeper never changes what it reports, or how often, because of anything the player said out of game. Recurring phenomena are reported at their true rate or not counted at all.
16. Every being that answers questions (an oracle, an old thing that does not lie, a voice in a dream, a people that keeps records) has a written limit on what it knows and on how it may be asked: what lies outside its knowledge, what it will not say, who may ask, how often, and in what form. A true answer from a being that does not know is "I do not know." No being knows what the deep lore keeps mysterious across campaigns, and none can short-circuit the epic's central measurements.

## Writing a mystery down

- Every mystery is written in the template in `creation-runbook.md` section 7.8, with these headings in this order: Truth; Body; Cost if ignored; Clock or trigger; Clues (each with its location, what is shown, and its readings); Branches (each with what the world does); Never found. `tools/lockcheck.py --mysteries` fails the lock on a missing or empty heading.
- Every cost if ignored appears in the event schedule as a clock or a trigger, naming the mystery.
- Every mystery carries one `Answers questions: yes|no` line under its Kind line: `yes` when any being in it answers questions. On `yes`, its rule 16 limit is a `Limit:` line in the Truth or Body where the being appears, and the same limit in the cast. `tools/lockcheck.py --mysteries` reads the field instead of guessing from wording, and fails a `yes` with no `Limit:`. The limit in the cast is the mystery's `Limit:` line word for word, copied, never retyped; the checker compares the two.
- A being answers questions when, asked, it gives anything back that a god or mortal could learn from: words, signs, a shown thing, or an act done in reply. A thing that only affects those near it (a dream it sends, a pull it exerts) and gives nothing in reply to asking does not answer questions, and its mystery says `no` unless another being in it answers.
- Every place named in a sealed file carries its bracketed map id, like `[r12]` or `[f03]`: every body, every clue location, every site in the deep history, the schedule and the cast. A place that has no id has no ground, and nothing may point at ground the map does not hold. `tools/lockcheck.py --places` fails the lock on a bracketed id missing from `map.json` and warns on a capitalized map name written without its id.
