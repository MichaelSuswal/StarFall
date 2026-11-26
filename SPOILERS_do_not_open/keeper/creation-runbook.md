> SPOILER WARNING: Keeper material. Players should not read this file. It describes how the NPC gods, the hidden powers, the deep history and the mysteries are built.

# Creation runbook: the three nights

The Keeper's procedure for Nights 1, 2 and 3 of a new campaign. Each night is a scheduled overnight session on a real night, picked by the campaign clock (`P/state/clock.md`: `status: creation`, `creation_night: N`), per `engine/night/creation-nights.md`. Each night runs after the player's day closes and finishes before the next day opens. Night 3 runs in two sittings back to back, 3a and 3b, and ends with the continuity checker's lock, all before 6:30am on Day 4 (see the lock deadline in section 4).

Read with DESIGN.md sections 3, 4, 6, 7 and 11, `engine/creation/*.md`, `engine/rules/powers.md`, `engine/rules/map.md`, `npc-god-rubric.md`, `survey-keeper-notes.md`, `mystery-standard.md`, `clue-design.md` and `deep-lore.md`. The deep lore wins over everything built here.

Paths: `P/` is the public campaign folder `campaigns/<name>/`. `S/` is the sealed folder `SPOILERS_do_not_open/campaigns/<name>/`. Nothing in `S/` is ever released whole; agents receive only what they could know. The shorthand is the Keeper's alone: every template in section 7 and every release, negotiation file and instruction written for another agent spells out the full path (`SPOILERS_do_not_open/campaigns/<name>/gods/<god>/...`, `campaigns/<name>/...`), never `S/` or `P/`.

Principle from run 02 (Night 1, step 1.4): an agent is told only what its release says, so a release never relies on a key the agent was not given. Anything another agent must act on (a path, a term, a format) is written out in full in that agent's own release.

Labels: each NPC god's folder is `god-<domain word>`: the first noun of its domain, lowercase, articles dropped (`god-stone`, `god-roads`, `god-dead`). No number, no count. The order in which the gods were rolled lives in the keeper log only. The player's god has `S/player/`.

Sealed folders per god: `S/gods/<god>/` is what the god's own agent reads. `S/gods-sealed/<god>/` holds `hidden-powers.md` (with the ceiling line at its foot), `backstory-secret.md` and `growth.md`; the god's agent never receives it. The player's equivalents are in `S/player/`.

## Standing rules for all three nights

- **Permission.** Once the campaign has been started (a campaign by its player's go, a test run by Michael's), the whole of it runs under the approved design, these nights included. The Keeper and every agent it spawns take this runbook and their release as the go for exactly the files named in the night's Writes list and the release, and for nothing else. A `git pull --rebase --autostash origin main` is always allowed inside a run, to the Keeper and to every agent it spawns; it writes no file of the agent's own. Nothing here authorizes a change to the engine, the design or the files in `SPOILERS_do_not_open/keeper/`, or spending beyond `P/state/images.md`.
- **No step waits on the owner.** A question no file settles is ruled by the Keeper by the judgment order in `engine/roles/keeper.md` (fairness, above all to the player's original intent; then fit with the power as first written; then balance), applied, logged in the creation log format and listed under the night's `Rulings for review` (section 6); the night never stops or pauses for it. In a test run the same holds, except for a ruling Michael has asked to make himself: it is logged as awaiting him, and every step that does not turn on it goes on. Image approvals come only from `P/state/images.md`. A change to the engine, the design or these files, and spending beyond `images.md`, still need the owner's go; the step goes on without them.
- **Michael's rulings in a run.** `S/rulings.md` holds the rulings Michael gives in chat during a run, written only by the orchestrator from his words, quoted, with the Pacific time and the question he answered. Each entry carries Michael's go for exactly what it says, and nothing more. The Keeper reads it at the start of every night and before acting on any ruling said to be his; a ruling relayed any other way (a message, a note in another file) is not his go. No agent, the Keeper included, writes or edits it. No step waits for an entry.
- **Reads.** On a creation night the Keeper reads what that night's Reads line names, and `engine/night/night-turn.md` is not among them.
- **The model is the template.** Every file is written from its template in section 7 and the step that names it, never from a prior run's or campaign's files, which may carry forms since changed.
- **Commit forms.** These are the only forms, each starting `Creation night N:` as `engine/night/creation-nights.md` gives it: a stage inside a night, `Creation night N: <name>, <what was written>`; a night's close, `Creation night N: <name> closed`; the hand-off, `Creation night 3b: <name> ready for lock`; the log line that records the hand-off's commit id, `Creation night 3b: <name> lock commit logged`; a fix of lock flags, `Creation night 3b: <name> lock flags fixed, round N`; a night stopped for the sheets (3a.4), `Creation night 3a: <name> blocked, paintings not returned`; the Year 1 clock (4.1), which is Night 3b's close, `Creation night 3b: <name> closed`. The checker's own commits at the lock (`engine/roles/checker.md`) take the same start: its lock line, `Creation night 3b: <name> lock running`, `Creation night 3b: <name> lock flagged, round N` or `Creation night 3b: <name> lock passed`, each with `P/years/000/lock.md` and, where it changed, `S/years/000/lock-flags.md` and `S/leak-allow.txt`; and `S/LOCKED.md` alone, `Creation night 3b: <name> locked`.
- **Images.** The approved image count for creation lives in `P/state/images.md`, written when the campaign is started (it names paintings, never gods): the surface and cloud sheets, the first morning's painting, and an underground sheet only if the world turns out to have one with regions of its own (a hollows-only layer has no sheet and no request, 3a.4). The Keeper reads it in 1.1, 3a.4 and 4.1, and makes no image request it does not cover. A request it does not cover is written to the held folder (`SPOILERS_do_not_open/images/held/` for a map sheet, `images/held/` for a scene) and logged as awaiting Michael's go, and the step continues without it: an unapproved underground sheet means the underground stays as data only, in `map.json`, where it is written before any painting either way (3a.4). A repaint is never in the count and always needs Michael's own go (3a.5); no step waits for it.
- **The premise.** Gods come down to lead a people: to find or gather them, to build, to rule and to spread (DESIGN 3.0). Every god release states it in the words of template 7.0 (the Night 1 release excepted, where the survey's own opening carries it) as the expected course of every god, on the same terms as the player's descent, with no invitation to refuse it. A god may push back unprompted; its pushback is recorded where it writes it (a `Premise rejected:` or `Premise bent:` line) and honored, and the Keeper's records then say plainly that this god does not play the usual way. The releases offer no alternative to the premise unasked.
- **Helpers by default.** Every people record, the player's and every NPC god's, carries a `## Helpers` section (template 7.3): the offices that run things when the god is absent (named offices, not named people, unless play names them) and how orders travel. A god may refuse them unprompted, with its reasons, dismiss any of them, or never meet or employ them; a refusal or dismissal is recorded with its date and reasons, the section then stays empty until play fills it, and dismissed helpers are never forced back. New loyal helpers may come later through play. When a god refuses or dismisses its helpers, the Keeper states the cost of having none plainly, in the negotiation and in the record: its unplayed time runs on its own conduct alone, no one acts for it while it is away, and its people drift.
- **Naming.** The player names its own people and their home; the Keeper names everything else, and never names what the player left unnamed for play. For its own records it uses a placeholder ("unnamed house 1", "unnamed location") until play names the thing, and releases a name only when play has given one. A place keeps its name: other names a god or anyone uses for it, however often, are recorded as aliases (`map.json` `aliases`, the gazetteer) and never rename it. A name changes only when the people of the place come to use the new one, which the Keeper records as a dated fact. A name a god gives its own people or their home, as a wish or plainly, is a name given; a name it gives a place its people already call otherwise is an alias. The player's name for its people's home is that home's map name in `S/map.json`, marked `"named_by": "player"` on its element (3a.5), never an alias.
- **Sealed terms.** From Night 1 on, the Keeper keeps `S/sealed-terms.txt` (template 7.12), which `tools/lockcheck.py --leaks` reads. Every sealed name goes in on the night it is made: god names and bynames, hidden power and knack names (every god's), names in the common past, place names that are not on the map. A term is written once, exactly as it is used, case and all. A sealed name that is also a short ordinary word, or a byname that is a capitalized common word, is written with the words it is used with (its article included), so the scan does not hit the ordinary word, and is logged as a possible false hit for the checker. A sealed name that is also the root of a public map name (a short root a gulf and a god's old name share) is never listed bare, since a bare line would strike the map name wherever the god comes to know it: it is listed only in the longer forms the sealed files use, and logged for the checker as a possible miss (run 06 item 53). The old guesses the tool makes from prose are warnings only; the file is the list. A name the player said in the open table talk is the player's own word and never sealed, even where a sealed file also holds it; the scan lets it through, and the Keeper takes it off the list when it finds it, logged (Michael's ruling, 2026-11-22; template 7.12). Every campaign's list carries, from Night 1, the name of the sealed factor in `SPOILERS_do_not_open/keeper/sealed-factors.md`, in each case form it may be written in, each line starting with `!` (template 7.12), since the scan cannot know an ordinary word is sealed. It never comes off the list, even where the player says the word at the table: that conversation stays sealed (Michael, 2026-11-22). A `!` term is never exempted by the scan, not as the player's open word, a known map name, a people's knowledge name or a `leak-allow.txt` phrase. The creation transcripts are the player's own words, kept verbatim, and the scan does not check them for it (the player using an ordinary word reveals nothing); it checks every other public file, so no agent ever writes it (section 4, the sealed factor's name in the player's words).
- **Test overrides.** A test campaign's override, if it has one, lives only at `S/state/test-overrides.md` (`SPOILERS_do_not_open/campaigns/<name>/state/test-overrides.md`), created by Michael before Night 1. The Keeper never looks for one on a public path. It applies exactly what the file names, as `npc-god-rubric.md` section 13 says, and logs each forced result beside the rubric's own. Nothing else bends to it, and it never changes a standing file.
- **DM-owned files.** The Keeper never edits a public file the DM owns (anything under `P/player/` that the DM wrote, and `P/civs/<people>/` for the player's people), with two mechanical exceptions: it writes a ledger id beside "Ledger: pending" on `P/player/power-card.md` (2.3, 3a.2), it writes the starting numbers in `P/civs/<people>/state.md` on 3a (3a.2); and it replaces the sealed factor's name, where the leak scan finds it in a DM-owned file other than a transcript, with a plain word of the same sense, logged in the sealed keeper log only, with no correction written (section 4). `P/civs/<people>/knowledge.md` is the Keeper's own file, not the DM's (3a.7). Every other change, however small, goes to `P/player/corrections.md` for the DM to make or put to the player. Where the player may not agree to a correction, it names `P/player/rulings-pending.md` for the player's argument: the DM writes it there as a case in the form `engine/rules/powers.md` section 2 gives (the power or term, the matter, the player's stated original intent, the player's argument, the DM's argument), one `## <date> <power or term>` heading per case, making the file if it is missing; the Keeper reads it on the next night and rules by the ledger rules of 2.3.
- **Rolls.** Every random outcome goes through `tools/roll.py --who keeper --campaign <name>`, so the log lands in `S/state/rolls.jsonl` and never in the public `P/state/rolls.jsonl`. Name every roll plainly in `--what` (which god, which table, which item). The tool assigns and prints an id `r-NNNN`; cite it.
- **Table rolls** use `--die d6|d8|d10|d12|d20|d30`. The tool maps the face and makes any range reroll itself, and logs the face with no success. A lean, the star's phase, a variation roll and every other 1 to 100 roll use `--die d100`, which logs the roll and no success. Company adds 25 to its lean and caps at 100. A reroll for a reason the tool cannot see (a duplicate seed or domain) is a new roll with `--reason` and `--replaces r-NNNN`. When one result takes two dice (the ceiling's shading), each die is its own roll with its own name in `--what` ("ceiling, first d10", "ceiling, second d10"), never two rolls under one name.
- **Luck.** Every god, the player's and each NPC's, has a luck modifier, sealed, in `S/state/luck.md` (template 7.14): one line per god (the player's under `player`), a whole number from 0 (ordinary) to +5, with a dated history line for every change and its reason. The Keeper sets it at 2.4 and again at 3a.1 for edges: each priced step a god took beyond what it bought adds one; refusing a power it was offered, or taking none, adds two per power; the count is logged. It never goes below 0 and never above +5. It moves one step toward 0 when a god's growth reaches a tier in a god power (`engine/rules/powers.md`), never for craft, technology, wealth or numbers. Use: before any roll for a god or its people's acts, the Keeper lists luck as a factor, named in `--what` before the roll, and, after the stated odds, shifts them in the god's favor by 5 points on a d100 per step (one face per step on a smaller die), the odds with luck still capped at 5 to 95; in a contest between two gods the luck nets out and only the difference counts (Michael, 2026-11-21); where a chance event chooses among targets, it weights them away from a lucky god's harm by the same steps. The table rolls that build a god or the world (leans, seeds, the star, the plane) are not acts and take no luck. A power a god shrinks of its own accord is not a power refused; a choice between prices the table offered as equal is the price, not a step beyond it; and "taking none" counts only powers that were offered, so a god offered nothing refuses nothing. In play, resolving the year, the Keeper may overrule the outcome of a DM roll by it, logged in the sealed log only. It is a factor on the record, never a judgment in the moment, and it is never told to anyone: not in any release, card, sheet, morning story or public file, and not to the DM. The full rules, the secrecy rule and the checker's check are in `SPOILERS_do_not_open/keeper/sealed-factors.md`; the public engine says only that the Keeper applies "the sealed factors" after the stated odds.
- **The unsaid want.** The player's god's unsaid wants are sealed in `S/player/unsaid.md` (`SPOILERS_do_not_open/campaigns/<name>/player/unsaid.md`), kept out of the open conduct profile and out of every transcript. It is written from the `SEALED:` part any player reply on any creation day may carry, on any subject, by the orchestrator or, in a live chat, by the DM, straight to the file as each arrives, dated, under a heading for its kind (want, fear, act, request not to be told, request to the Keeper, other), a sealed answer of two kinds split into two lines; the transcript keeps only "(One more answer was given privately, for the sealed record.)". A Day 1 with no sealed answer leaves the file with the DM's one line, "No sealed answers on Day 1.", so the file is always there from Night 1 (run 06 item 8). When two sealed lines pull against each other (a want against a request of the same day, most often), both stand, and the Keeper weighs them together wherever either bears, logged (run 06 item 34). An act the god says it does is done, wherever it is said, a sealed line included, under `## Act` or under any other heading (Michael, 2026-11-25): it is a decision, carried out in unplayed time or at the time it names, and needs no confirmation; what it shows the god goes to the DM in the sealed day sheet (`SPOILERS_do_not_open/keeper/year-turn.md`), never in a public file. An ordinary habit the god states (checking a pocket, touching a doorpost) is conduct: carried out, and never priced. Wants and fears stay feelings, and only they wait on the confirmation rule below. A sealed wish later said openly is used in its open words, and the sealed line stays sealed. Its header, as `engine/creation/day2-the-god.md` gives it, reads "Written by the DM. Read by the DM, the Keeper and the checker." The header stands as written when the orchestrator writes the file in a test run: the orchestrator writes in the DM's place, and the header names the role, not the hand. No NPC god or civ agent is given it, and nothing from it goes into a release. The Keeper applies an unsaid want (in fitting, or in the standing conduct it applies) only when a dated confirmation from the DM, with the player's answer, stands beneath it, and never one whose last confirmation is more than three played years old. An open conduct line marked "check with the player before acting" is one a sealed answer qualifies: the Keeper reads it with that answer and applies it only as the answer and this rule allow. The Keeper never writes the file.
- **Sealed requests.** On the night after the day it arrived, the Keeper answers each sealed request in `unsaid.md` (a request not to be told, a request to the Keeper) in `S/ruling-ledger.md`, and writes one line for it to `S/player/requests-answered.md` (`SPOILERS_do_not_open/campaigns/<name>/player/requests-answered.md`), a sealed file the DM may read: the request's date and "received and ruled", nothing more (Michael, 2026-11-23). A sealed line the DM flagged for the Keeper to weigh (one whose kind or reach the DM could not settle, filed as a want and marked as a possible request, say) is answered the same way, on the same night, with its date and "received and ruled", so the DM runs the next day knowing it is ruled; on Night 2 its line is in the Night 2 file (run 06 item 26). The file is written only when there is a request or a flagged line to answer. The agreeing step is only for telling the DM more. When the Keeper has an explicit reason to tell the DM more about a sealed request or a flagged line, it writes the reason as an indented line under that entry in `S/player/requests-answered.md`. The DM records whether it agrees in `S/player/unsaid.md`, beneath the request, dated. Only when the DM agrees does the Keeper add the further line. The Keeper reads `unsaid.md` for the DM's answer at the first step of the night after it, adds the further line there, only beneath a dated agreement, lifts there any conduct marks the further line lifts (run 06 item 32), and logs the reason, the answer, any further line and any mark lifted in the keeper log. Day 3's requests, answered on 3a.2, reach the player in the first morning's closing (oog) block (3b.8). The file's header reads "Written by the Keeper. Read by the DM, the Keeper and the checker." No NPC god or civ agent is given it.
- **Blends and votes** follow `survey-keeper-notes.md` exactly: placement of every answer logged before any roll, median of those who answered, a tie (an even vote, a half or quarter median, any even-odds tie) decided by the Keeper by what makes the more interesting game, with its reason logged and no die, one variation roll, which still follows a tie, clamp to 1 to 10; a tie that a later bound makes moot (both sides clamp to one value whatever the variation roll gives) needs no decision, logged as moot; rule votes by the counting rules there. Vote counts go in the keeper log and nowhere else.
- **Time.** Every real date and time logged is Pacific, taken from `python3 tools/stamp_time.py` (`--time` for the time alone, `--date` for the date), which prints the Pacific clock time in the log's format, or from the commit record. Never estimate a time. A log line is stamped after its step finishes, from the clock at that moment, never written ahead of the work. What a step must write before a roll (a method, a placement, a share, the odds and their factors) is written before the roll, unstamped, and the step's stamp follows when the step is done; the two rules never conflict (run 06 item 53).
- **The keeper log** `S/keeper-log.md` records every choice: what was decided, from what, with which roll ids, in the creation log format below. The continuity checker verifies the world from it. The log is also the index: read earlier files in full only where the step in hand needs them, and their summaries in the log otherwise.
- **Agents.** The night session is the Keeper and spawns the NPC god agents. Each runs under `engine/roles/npc-god.md` and receives its own folder `S/gods/<god>/` plus the release written for it that night. It never sees `S/gods-sealed/`, the rubric tables, another god's folder, the deep lore, the world draft, the map or the player's files. A god agent does not commit: the session that spawned it (the night session, or the orchestrator in a test run) commits its files with the stage they belong to.
- **Releases are neutral.** Every option is offered once, in plain words, with no recommendation, no count of who took it, and no line that tells a god what is usual or easiest. Any option offered to the player at creation (on Day 2, Day 3 or in a follow-up) is offered to every NPC god on the same terms, prices excepted (below). Use the release templates in section 7.
- **No price in a release.** No god release says anything of prices, trades, drawbacks or weaknesses, and none gives a worked example of a power, an edge or a price (Michael, 2026-11-24: "do not make the payment explicit. It is done in negotiations with the god"; "you should not say anything about a price"). The god proposes its powers and its people's edges; every price is found in the negotiation with that god, as it was with the player at the table. What the DM put to the player about prices (that every power carries a drawback, that a weakness taken on can buy an improvement, the return scale and that its faster rung costs more, a heavier price written as asked, a choice where a drawback could go two ways) is put to the god in its negotiation round 1, once, by kind, where the god's own proposal makes it bear, and never as a worked example with its price attached (run 06 item 24).
- **The Keeper never speaks to the player.** Anything the DM needs is written to `P/player/` in words the player may read. Nothing in `P/` names a vote, a pool, another god, a count of gods, a sealed place id, a coordinate, a star value, a mystery or a scheduled event.
- **Places.** Every place named in any file under `S/` carries its bracketed map id, like `[r12]` or `[f03]`, from 3a on, except the files `tools/map.py stamp` skips: the keeper log, `LOCKED.md` and the files a god's agent writes in `S/gods/<god>/`, which keep their writers' words (`tools/lockcheck.py --places` warns on no bare name there, and still fails a bracketed id the map lacks). Before 3a, places are named by the placement draft's working names and get ids when traced.
- **Land in words comes from the map.** No release or record describes distance, direction, line of sight or travel days except from `S/map.json` after tracing, at the pace table's rates.
- **Travel by route and means.** Every trip is priced along the route the traveler takes (road, path, river, open ground, sea), segment by segment, at the rate `engine/rules/time-and-pace.md` gives for the means (on foot, on horse, by wagon, by boat or barge) on each segment's ground. A trip with no traced route goes over open ground by the ground it crosses. Different routes to one place give different times, and a land line names the route and the means it priced. A place counts as on a route within half a mile of it. The price comes from `tools/map.py travel <name> <from> <to> --by foot|horse|wagon|boat [--via <id>,<id>]`, which prints each segment; the Keeper copies its days and never works them by hand.
- **Close of every night.** Each night ends with its close check: every file in the night's Writes list exists and is complete; a neutrality self-check (each place the Keeper could have leaned toward or against any god, and what was done instead, with every luck count set or used tonight named as a factor); the night's roll range, or `Rolls: none tonight.`; the close time. A leak scan hit on the sealed factor's name in a DM-owned file other than a transcript is replaced by the Keeper (DM-owned files, above). Any other leak scan hit in a file the Keeper may not edit is logged with its file and line for the checker; where it sits in frozen card text or verbatim transcript no correction is written, and the close goes on. The Keeper never writes the leak allow file (section 4). Then the close order, one for every night: record the times in `S/state/timing.md`, set `creation_night` in the clock to the next night, commit (`Creation night N: <name> closed`), pull with rebase and autostash, push. The Keeper writes only the campaign's own timing file; a test run's timing file under `tests/` is the orchestrator's, and the Keeper does not write it. `S/state/timing.md` is sealed (Michael, 2026-11-23): nothing public carries a night's or a stage's times, and the clock's year is the only time the player sees. As a style choice it names each stage by what was written (`powers drafted`, `replies read`, `records agreed`), not by an ordinal.
- **Pushing.** Before every push, run `git pull --rebase --autostash origin main`: the paint job and other sessions push to main while a night runs.
- **The clock.** `creation_night` takes the values `1`, `2`, `3a` and `3b`. The starting clock, made when the campaign is started, carries `year: 0`, `status: creation`, `creation_night: 1` and `season_opens: not yet set`; the Keeper sets `season_opens` in 3b.8, to the waking month decided on Night 1 (1.5). The Keeper sets the clock to Year 1 only after the DM's first morning story and the final leak check (section 4.1). A test run ends at `year: 1` with `status: closed`, never open, so no scheduled turn ever turns a test campaign, unless it continues into a play test under an entry in `S/rulings.md`: then it is set to `year: 1`, `status: open`, and the play test's last night sets it closed (4.1; run 06 item 56).
- **Rounding** of every score follows `npc-god-rubric.md` section 11 (a half rounds up). The survey blend is not rounded: a blend that falls between two whole steps is a tie, decided by the Keeper by what makes the more interesting game, with its reason logged and no die (`survey-keeper-notes.md`; Michael, 2026-11-22).

### The creation log format

```
## Night N
Began <date> <time> Pacific. Read: <files>. Read in part, and why: <files>.
Found on reading: <anything that bears on tonight>.

### <step number> <step name>
<what was decided>, from <answers, files or rolls>, [r-NNNN].
Decision the files did not make: <the question>. Decided: <the ruling>. Reasons, by the judgment order: <why>. Applied; listed for review.
Paused <time> for <what an agent is writing>. Resumed <time>.

### Rulings for review, Night N
- <step>: <the question, in one line>. Ruled: <the ruling>. (Or "None tonight.")

### Close check, Night N
Files: <each Writes item, present or not>. Rolls: r-NNNN to r-NNNN (or "none tonight").
Neutrality: <each temptation, and what was done>.
Closed <date> <time> Pacific.
```

## Night 1: the star, seven gods, eight surveys, the first draft

Reads: `CLAUDE.md`; DESIGN.md 3, 4, 7; `engine/creation/day1-world-survey.md`; `engine/rules/powers.md`; `npc-god-rubric.md`; `survey-keeper-notes.md`; `mystery-standard.md`; `clue-design.md`; `deep-lore.md`; the player's Day 1 answers in `P/player/survey-day1.md`, with any remarks kept under `Also said`; the DM's note of any premise the player rejected or bent, `P/player/rejected-premises.md`; `S/player/unsaid.md`, under the standing rule (one line when Day 1 brought no sealed answer); `state/test-overrides.md`, if the campaign has one.

Writes: `S/keeper-log.md`; `S/state/rolls.jsonl`; `S/star.md`; `S/sealed-terms.txt`; `S/gods/<god>/sheet.md` and `survey-day1.md` for seven gods; `S/gods-sealed/<god>/.keep` for seven gods; `S/player/.keep` if `S/player/` holds no other file at the close (run 06 item 7); `S/releases/creation/<god>-night1.md`; `S/world-draft.md`, with the waking month (1.5); `P/player/world-rules.md`; `P/player/followups-day2.md`; `S/ruling-ledger.md` and `S/player/requests-answered.md`, if Day 1 carried a sealed request or a flagged line (standing rules).

### 1.1 Create the sealed folder

- [ ] Make `S/`, `S/state/`, `S/gods/`, `S/gods-sealed/`, `S/player/`, `S/releases/creation/`. If `S/state/test-overrides.md` is already there (Michael creates it before Night 1 for a test run), make only the folders that are missing and leave the file as it is. Git does not carry an empty folder, so each god's sealed folder `S/gods-sealed/<god>/` is made with an empty `.keep` file when its label is set (1.3), and any folder made here that holds no file at the close gets one too: `S/player/` most often, since its first file may not come until Night 2 (`S/player/.keep`, in the Writes list and the close check).
- [ ] Open `S/keeper-log.md` with the campaign name, the date and time Pacific, and a line that Night 1 began. Read `P/state/images.md` and log the approved image count; if the file is missing, log that no image is approved and treat every request as held. Log whether `S/state/test-overrides.md` exists.
- [ ] Open `S/sealed-terms.txt` in template 7.12, empty but for its header and the sealed factor's name in each case form, each on a `!` line (standing rules).

### 1.2 Roll the star

The star comes first, before the gods and before the blend, because it bounds the magic blend, decides the center body the painting must show, and fixes everything the gods are told before Day 2.

- [ ] Roll every item under the deep lore's `Per-star variation` heading except the ceiling, one roll per item, with the die the lore gives: phase (`--die d100`), rain density (d6), living radius (d8), center body (d6), long-game presence (d6), Remainder (d10), star content (d10), ascended temper (d6).
- [ ] Write each result to `S/star.md` with its roll id, and the magic range rain density allows, from the table in `survey-keeper-notes.md`.
- [ ] Note in the log what each result removes or requires for later nights (a rolled result that removes a body the lore names is not replaced; see 3b.4).
- [ ] Where two results pull against each other in wording, settle it by `survey-keeper-notes.md`, "When two star results pull against each other", and log which governs what.
- [ ] The ceiling is rolled in 1.6, after the Q8 blend that shades it.

Principle from run 01 (Night 3, order of work): anything that decides what a painting must show or what a god must be told is rolled before the step that needs it. When an order of work would let a later roll change something already released, roll first and log why.

Principle from run 02 (Night 1, step 1.2): two rolled results are never set against each other so that one cancels the other. Each governs its own part of the matter (one when, how often and how strongly; the other what, and in what voice), and both stand as rolled.

### 1.3 Roll the NPC gods

For each god, in order, with `tools/roll.py`. Each god's rolls are cast and checked (its seed and domain against every earlier god's, the domain against the player's stated theme, each reroll made) before the next god's first roll; never all seven at once (run 06 item 11).

- [ ] Ten leans, `--die d100`, in the rubric's order. Company adds 25 and caps at 100.
- [ ] Archetype seed, `--die d30`. If any earlier god in this campaign has the same seed, reroll with `--reason` and `--replaces`.
- [ ] Domain, `--die d20`. Reroll duplicates the same way. Then reroll, the same way, a domain that matches what the player has said its own god is about: in its Day 1 answers, in the remarks under `Also said`, or in `rejected-premises.md`. The reason names only "matches the player's stated theme", never the player's words. No one is told. A match is the same domain, or a domain the player named as its god's center (rubric section 3); a domain that only neighbors the theme is not a match. The Keeper writes which table entries match, and which neighbors were held not to, in the log before the first domain roll, and never after.
- [ ] Form `--die d12`. Virtue `--die d10`. Flaw `--die d10`. Wound `--die d12`. Voice `--die d10`.
- [ ] Label the god `god-<domain word>` (rubric section 10), and make `S/gods-sealed/<god>/` with its `.keep` file (1.1). The god names itself on Night 2; the folder keeps the label.
- [ ] Work out the god's bargaining stance and its people lean from its leans (rubric sections 11 and 12): size, settlement, the rule lean with its variety, and the worship lean, each with its score, rounded by rubric section 11.
- [ ] If the campaign carries a test overrides file, apply what it names now (rubric section 13), and log the rubric's own result, the forced result and the file's line together.
- [ ] Write `S/gods/<god>/sheet.md` in the sheet template (section 7.1). No roll id goes on a sheet; the ids stay in the keeper log.
- [ ] Check across the seven: no shared seed, no shared domain, no domain matching the player's stated theme. Log the check, with the seed numbers in the log only.
- [ ] Add every label to `S/sealed-terms.txt`.

Principle from run 02 (Night 1, step 1.3): a thing to watch is logged as such and not decided; the Keeper acts on it only when a file gives it the rule. (The theme reroll above is that rule for a domain that matches the player's.)

### 1.4 Each god answers the survey

- [ ] Write `S/releases/creation/<god>-night1.md` from template 7.4: its sheet, the survey's opening paragraph and all its questions word for word from `engine/creation/day1-world-survey.md`, and nothing else from that file (its rules block speaks of the player and the sealed notes and is left out). Nothing about the other gods beyond what the survey's own words say, nothing of the deep lore, nothing of the player.
- [ ] Spawn the seven agents in parallel, each with `engine/roles/npc-god.md` and its own release only.
- [ ] Each agent writes `S/gods/<god>/survey-day1.md` in the answer format of template 7.4: every question's number kept, `Skipped.` where it skips, `Premise rejected:` or `Premise bent:` before its own answer where it rejects or bends one, its two waking months in the closing sentence template 7.4 gives, the file opening at `## Answer 1` with no title of its own (run 06 item 9), and no name for itself. A marker with extra words ("Premise partly bent", "Premise rejected in part") is read as the nearer of the two markers, by the Keeper's reading, logged. Every marker is read by the answer's words: an answer that bends with no marker is read as bent, and a marker the words do not bear out (a "Premise rejected" on an answer that answers, a "Premise bent" inside the range) is read as what the words do, logged. A marker counts only at the start of an answer; one placed anywhere else is read as no marker, and the answer by its words. An answer to a question that offers "or something else" is inside the range and is never bent, whatever its marker.
- [ ] Read all seven against their sheets. An answer breaks character when it contradicts the sheet with no reconciliation. Examples: a god leaning hard to hidden that wants to be seen far and wide and says nothing of the pull between the two; a god leaning hard to solitary that hopes for a crowded world of its followers with no word of why; an answer that steps outside the world to speak of the game, the player, the Keeper or other gods' answers.
- [ ] Send a broken answer back once per answer, with the contradiction named, in the god's release under `## Sent back`. The god appends its new answer under `## Answer N, given again`; the first is kept in the file. The redone answer is the one blended. Do not rewrite an agent's answer yourself.
- [ ] While a send-back is out, blend every question it does not touch, and wait for the reply before the affected question. Keep a send-back even when it would not move the blend: the file is the god's character record.
- [ ] Log each god's two waking months, first and second, from its closing sentence (the player's from `P/player/survey-day1.md`), for the vote in 1.5. Once 1.5 has decided the month, fill every sheet's `The month the world wakes in` line with it, the same words on all seven. The Keeper writes this line; the god does not.

### 1.5 Blend the eight surveys

Per `survey-keeper-notes.md`, the player's answers counting as one voice in eight. For each question, log the eight answers in summary, the Keeper's placement of each on the scale (before any roll), the blend, the roll ids, and what was built.

- [ ] Before rolling any scale question, ask any NPC god's range follow-up that question needs (1.8) and wait for the answer. A follow-up answer replaces the answer it follows. The player cannot be asked until Day 2, after the blend is final: a player's scale answer the blend cannot place is placed at the midpoint of the points it names, and the placement is logged. A Day 2 follow-up on it may shape the player's own god, never the blend.
- [ ] Q1 feel: pool. The world's tone, light, weather tendency, palette within the house style.
- [ ] Q2 land: placement wishes, one per god. List the terrain the world must contain.
- [ ] Q3 seasons: scale for the climate. All the world goes through the seasons at the same time. The waking vote: count every god's two months (1.4) in the log only, and decide the one month the world wakes in by `survey-keeper-notes.md` (Q3), logging why. It is final tonight, the same for every god, month 1 of every country's count; it goes on the sheets (1.4), in the world draft (1.7) and to the clock in 3b.8. This replaces each country opening its year in its own season and L-0043 (Michael, 2026-11-25).
- [ ] Q4 past the borders: scale. Sets the share of land held by godless peoples.
- [ ] Q5 age of the human story: scale. Sets the depth the deep history must reach.
- [ ] Q6 mortal magic: scale, then bounded by the star's magic range (1.2). If the blend falls outside the range it clamps to the nearest end; log the clamp. The level is final tonight.
- [ ] Q7 magic's feel and cost: pool. One system, consistent with the deep lore. Minority answers may survive as local understandings, often wrong.
- [ ] Q8 how much a god stands out: scale. Shades the ceiling roll (1.6) and sets mortals' first reactions to gods.
- [ ] Q9 strangeness of the wild: scale.
- [ ] Q10 fears: pool. Candidate standing threats for the event schedule.
- [ ] Q11 scarcity: pool. One or two world scarcities; the rest local.
- [ ] Q12 buried things: pool. Candidate sites for the deep history and the short mysteries.
- [ ] The underground: decide tonight whether the world has an underground layer, from the Q12 pool, the deep lore's bodies and the star's results, never from whether a sheet is approved. The threshold: buried material makes an underground only when it is more than sites, that is, hollows or passages that join places to one another or run beneath more than one region; a few rooms, doors or single deep places are sites on the surface sheet and make no layer (3a.3). One lone answer never passes the threshold by itself, even one that describes a single long thing that could read as running beneath more than one region: it is a single site (run 06 item 6). Log yes or no with its reasons. If yes, the world draft says what it is: its depth, and its hollows by working name, or that it is mostly solid rock with those hollows only, all of it unplaced like every rare candidate (1.7). If no, the world has no layer and no underground sheet. The world draft carries the decision on one line of its own, in one of two forms, which `tools/map.py validate` reads: `Underground: yes, location not set` until 3a places it, or `Underground: none`. 3a writes a yes into `map.json` before any painting (3a.4).
- [ ] Q13 non-human peoples: pool and scale.
- [ ] Q14 travelers: scale plus a pool of what they brought.
- [ ] Q15 god-sense: rule by vote.
- [ ] Q16 bodies: rule by vote. The bodies question feeds this vote directly. If no answer speaks to it, the default is one body, logged as a default.
- [ ] Q17 mortals worth following: pool. Candidates for the small cast.
- [ ] Q18 discoveries: pool. Candidates for the layered mysteries and the discoverable powers.
- [ ] Q19 undared wishes: pool, handled with care. Never placed where its own god is certain to find it.
- [ ] Where an answer cannot fit the deep lore or the star, leave it out and log that it was left out.
- [ ] A star result and a scale blend that speak to one matter (a young star over an old human story) both stand. The star bounds the blend only where a table says so (rain density and Q6); otherwise the star governs its own part by the order in `survey-keeper-notes.md` ("When two star results pull against each other"), the blend sets the rest, and the deep history (3b.4) holds both. Log the reading here, before anything is built on it.

### 1.6 Roll the ceiling

- [ ] Roll the secret power ceiling, 70 plus a d10, shaded by the Q8 blend by the table in `survey-keeper-notes.md`. Write the method in the log before the first die. Where the table takes two dice, they are two rolls, each named for itself ("ceiling, first d10", "ceiling, second d10"). Write the result to `S/star.md` with its roll ids. It is copied to every god's sealed `hidden-powers.md` on Night 2 and is never released.

### 1.7 Write the first world draft

- [ ] Write `S/world-draft.md`: the tone; the climate and seasons, and the waking month on a line of its own (`Waking month: <the month, and its season>`), with its vote counts kept to the log; the star's results that bear on the land; the magic level (final) and how magic feels and costs; the two rules (god-sense, bodies), with their vote counts kept to the log; how much gods stand out; the wild's strangeness; the terrain list and each god's placement wish; the underground as decided, on its `Underground: yes, location not set` or `Underground: none` line (1.5), with what it is in the text beside it; every pool, its widespread features set apart from its rare candidates.
- [ ] Mark every rare candidate as unplaced. Placement happens on Night 3.

### 1.8 The world rules for the DM, and follow-ups for Day 2

- [ ] Write `P/player/world-rules.md` from template 7.9 (its cost line only where the rule allows more than one body), for the DM: god-sense as set, the bodies rule as set, and the pricing terms for mortal magic (it is simple, and it costs the worker), in words the player may read, and nothing else. The god's own power limits are not in it; they are settled at the Day 2 table. Nothing that is discovered in play goes in it: the prevalence of magic and the rest of its feel, how much gods stand out, the strangeness of the wild, the scarcities. God-sense is written as direction, nearness or weight, never as a count. It reads as a fact of being a god here, never as the result of a vote, and gives no hint that a wish was kept in part.
- [ ] Write `P/player/followups-day2.md`: few, each in a form the DM can weave into the fiction, with an (oog) fallback where the question is mechanical. A gap is only an answer the blend cannot place (a range answer that names two far points, a vote answer that fits neither side). A rejected or bent premise is a follow-up only when it leaves such a gap. An answer that asks not to be told something is honored and never becomes a follow-up. No question may reveal a vote, a pool, another god or anything from `S/`. With no follow-up, the file is one line: `No follow-ups for Day 2.` (run 06 item 10).
- [ ] For each NPC god with a gap by the same bar, write the follow-up into its release under `## Follow-up`, have the agent answer it the same night at the end of its `survey-day1.md` under `## Follow-up, answer N`, and blend by the same rules. The follow-up answer replaces the one it follows. A god with no gap gets the line `No follow-up.` in its Night 2 release.
- [ ] Answer each sealed request and flagged line that arrived on Day 1 (standing rules, sealed requests).

### 1.9 Close

- [ ] Confirm `S/sealed-terms.txt` holds every label, and run `tools/lockcheck.py <name> --leaks --dashes`.
- [ ] Close check (standing rules), naming `S/player/.keep` where `S/player/` holds no other file, then the close order, setting `creation_night: 2`.

## Night 2: the gods make themselves

Reads: the Night 1 entries of the keeper log, and Night 1's files where a step needs them; `engine/creation/day2-the-god.md`; `engine/rules/powers.md`; `deep-lore.md` (the origin of the gods, under its own heading); `S/star.md`; the player's Day 2 outputs written by the DM: `P/player/power-card.md`, `appearance-card.md`, `backstory.md`, `conduct-profile.md`, `power-lean.md`, `rejected-premises.md`, and the player's answers in `P/player/followups-day2.md`; the sealed `S/player/unsaid.md`, under the standing rule; the mode the player chose, in `P/player/survey-day1.md`, and in mirror mode the sealed `S/player/mirror.md` (2.7).

Writes: `S/state/luck.md` (2.4); per NPC god, in `S/gods/<god>/`: `self.md`, `goals.md`, `record-of-gods.md`, `negotiation-night2.md`, `power-card.md`, `card-summary.md`, updates to `sheet.md`; per NPC god, in `S/gods-sealed/<god>/`: `backstory-secret.md`, `hidden-powers.md`; `S/gods-sealed/common-past.md`; `S/player/backstory-secret.md`, `hidden-powers.md`; `S/releases/creation/<god>-night2.md`, `<god>-night2-negotiation.md`, `<god>-day3-questions.md`; `S/balance.md`; `S/ruling-ledger.md`; `S/placement-draft.md`; `P/player/day3-brief.md`; `P/player/followups-day3.md`; ruling ids written back to `P/player/power-card.md` (2.3); `P/player/corrections.md` if anything on the player's card needs the DM (2.3, 2.7); `S/player/requests-answered.md` and the ledger entries for any sealed request or flagged line (standing rules); additions to `S/sealed-terms.txt`; the keeper log.

### 2.1 Release the rules to each god

- [ ] Write `S/releases/creation/<god>-night2.md` from template 7.5. It holds:
  - the world rules exactly as `P/player/world-rules.md` gives them to the player (god-sense, bodies, magic's pricing terms), and nothing else that is discovered in play (no magic level, no word of how much gods stand out);
  - the premise, in the words of template 7.0;
  - the facts of being a god that every god knows of itself, these six and no others (the DM states five of them to the player on Day 2; the technology fact no Day 2 line gives the DM, so the Keeper states it itself in every release, as below): no need of food, sleep a choice; it moves at its form's pace; it cannot die; the technology of the peoples it will find, as the world's starting level, in DESIGN 4.7's first sentence only (its second is discovered in play), with the line that the level is where the world begins and not a ceiling (template 7.5); there is no set number of powers; nothing over the top. That every power carries a drawback is a price, and is put to the god in its round 1, not in the release (standing rules, no price in a release);
  - its rule lean and its worship lean, one line each, from its sheet, with the line that it builds its people within them on Night 3 and may give reasons to depart from them;
  - the god's own follow-up answers, or `No follow-up.`;
  - the month the world wakes in, and its season, from Night 1 (1.5), in the same words in every release;
  - that its people come with helpers who run things when it is away, and that both are settled on Night 3 (template 7.5), and nothing of what refusing them costs: that cost is stated only to a god that refuses or asks;
  - every option the player was offered on Day 2 and in its follow-ups that is not a price, each once, in the same terms, by kind, with no recommendation and no example: what the god may ask for, never what it would pay (where the return scale was offered, only that a god whose body is broken returns, and that it may say how it wishes to return);
  - the `self.md` template (section 7.2), the `goals.md` and `record-of-gods.md` instructions, and the instruction to stop after those three files.
- [ ] Nothing about the other gods, the vote counts, the pools, the player, the star or the deep lore. Nothing about prices, trades, drawbacks or weaknesses, and no worked example.

Principle from run 06 (Night 2, step 2.1; item 24): a worked example with its price attached acts as a default (six of the seven took the DM's instrument trade by its shape). So a release offers nothing priced and gives no example; the god proposes, and the price is found god by god in the negotiation, where the Keeper puts what the DM put to the player, by kind, once, as it bears on what this god proposed. Michael, 2026-11-24: "Explicit takes a player out of the game."

The Keeper states the technology line in every release itself, in the words above, whether or not the DM stated it to the player at the table.

### 2.2 Each god creates itself

- [ ] Spawn the seven agents in parallel with their release and folder.
- [ ] Each writes `S/gods/<god>/self.md` in the template: name and what it is called and by whom; form in detail, with things carried, what breaks it and what it wishes happens when its body is broken; its two traits with the rolls they reconcile; its backstory outline as it dimly remembers it (the wound felt, never explained); what it wants; proposed powers, each with what it does, why this god has it, and the edge cases it expects; the people it will lead. It proposes no drawback and no trade: those are found in round 1 (2.3). A god that offers a drawback, a weakness or a trade unprompted has it read in round 1 like any other proposal.
- [ ] Each writes `goals.md` (what it wants on arrival, knowing only that it expects a people and does not know why; wants of any kind, among them knowledge, trade, justice for an offence and security against a threat as much as land or worship) and `record-of-gods.md` with one entry: others like it came down when it did, and nothing more.
- [ ] Check all seven `self.md` files against their sheets before any pricing, as on Night 1: every section present; traits that reconcile the rolls; voice kept; the people hope within reach of the sheet's people lean, or a reason given for leaving it. Send back once per section that breaks character, the same way. A Night 2 send-back rides at the head of the god's round 1 file (2.3), with its own path and heading (`## <section>, given again` in its `self.md`); pricing does not wait for it unless a price turns on the section sent back.
- [ ] Anything a god carries that does more than an ordinary object is a power and goes into pricing. So is a Form entry that carries a cost and a trigger (the body broken, with a price and a return): it is written as a power, with Description and Drawback.
- [ ] Every form says what breaks it. A form nothing can strike (a body of weather, a fog) is not finished until it does: the Keeper puts the breaking to the god as a choice in round 1, and does not rule it alone.

Principle from run 01 (Night 2, step 2.2): when gods working apart arrive at the same choice the rules do not forbid (the same name, the same image), the choice stands and neither agent is told. The Keeper accounts for it in the sealed files, and every record tells the two apart by label or byname. Nothing is changed that would tell one god something about another.

### 2.3 Negotiate powers, god by god

Per `engine/rules/powers.md` sections 1, 3 and 6, in the format of the power card. The Keeper takes the DM's side of the Day 2 table and the NPC agent takes the player's. The god's bargaining stance is the god's own; the Keeper prices the same way whatever the stance.

- [ ] First, the player's table rulings: every ruling the DM marked "settled at creation. Ledger: pending, Night 2" on `P/player/power-card.md` is copied into `S/ruling-ledger.md` with an id `L-NNNN` (in order entered, from L-0001), and the id replaces the word `pending` and its night on the card. Nothing else on the player's card is touched.
- [ ] Review the player's card against the real world: an information power against the mystery standard, and any limit the DM priced by shape against a scarcity the player wished for, against the scarcities the world kept. A Limit the Keeper would add, or any other change, is written to `P/player/corrections.md` for the DM to put to the player; the Keeper does not edit the card. Every provisional term reviewed gets its own entry there, with its ledger id: a changed term, in plain words, for the DM to open Day 3 with and put to the player for a yes; a term confirmed unchanged, so that the DM lifts its provisional mark with a dated entry citing the id.
- [ ] Answer each sealed request and flagged line that arrived on Day 2 (standing rules, sealed requests), in `S/player/requests-answered.md` tonight, so the DM opens Day 3 knowing each is ruled.
- [ ] Round 1, in `S/releases/creation/<god>-night2-negotiation.md` under `## Round 1` (template 7.6): for each proposed power, draft card text written as card lines (Description, Drawback, Limits, in the `powers.md` format), with choices where a price could go two ways, and the Keeper's argument for each price, so that the final text can be copied from it line for line. Here, and not before, the god meets the prices: the drawback each power carries, and, once, by kind and with no worked example, what the DM put to the player about prices (a weakness taken on may buy an improvement elsewhere, which the god need not take; a broken body's return is a power on the standing scale, whose faster rung costs more, with the god's own wish asked first; a heavier price is written as asked), each where this god's proposals make it bear (standing rules, no price in a release). The god appends `## Round 1 reply` to `S/gods/<god>/negotiation-night2.md`, with its reasons for every acceptance, refusal and counter.
- [ ] Test every power against the edge-case floor (light and dark, distance, falling, carrying, water, being watched, other gods, the god's own people), the cases this god's own powers depend on, and four more: does it touch a world scarcity; does it rule a mind; does it work on things made by more than craft; does it scale across a whole people in a year.
- [ ] A drawback is something the god would notice losing. A drawback that restates the god's voice or form costs nothing and is priced again.
- [ ] A power that reveals information (the past, things far off, what is hidden) is priced against the mystery standard: it may show effects, never mechanisms, and never a central measurement of the epic.
- [ ] A memory-loss drawback is enacted by the Keeper removing an item from the god's own record; write which record and how often into the Limits. The rate is the god's own words where it gave one, else one item per use.
- [ ] An ability bought by a trade is a power with Status `main`, the trade recorded on both entries.
- [ ] A heavier price a god takes willingly, beyond what its power needs, is written as it asks, is not traded for anything, and is counted toward its luck at 2.4 as a priced step beyond what it bought.
- [ ] A god whose self bends or refuses a default on Night 2 has the cost stated plainly in its round 1, as in 3a.1: once, the cost only, in the terms the player was told, beside its powers or in a round 1 of its own with no power at stake, and the bend itself may be priced as the price (Michael, 2026-11-23; run 06 item 38).
- [ ] Before round 2, a rough balance pass: a first weight for each god from its round 1 draft and reply, by the measure of 2.6, logged, so that a god above the band is told so in its round 2 counter (2.6). A god under the band is not told: it is raised by its sealed parts at 2.7 (run 06 item 27). 2.6 then sets the weights in full.
- [ ] Round 2, under `## Round 2`: the Keeper's counter to each reason the god gave, and the final text. The final text is copied from round 1 and changed only where a reply changes it: no tidying, no widening, no narrowing of anything the god did not reply to. The god appends `## Round 2 reply`. Round 3, if needed, is confirmation of wording only.
- [ ] A counter the Keeper makes for the first time in round 2 gets one reply of substance: the god may answer it in its round 2 reply, or take in its place one choice drafted earlier that the round 2 text names, and the Keeper settles it in round 3. Nothing else is reopened.
- [ ] A clarification a god asks, in any round, is wording if it changes no number, reach or cost, and is written in as wording; one that changes any of the three is substance and is priced as any request is.
- [ ] A substance objection that arrives in round 3 is logged, with the god's words, and the round 2 text stands. A wording the god asks in its confirmation that the Keeper will not write as asked: the Keeper writes its own version into the Limits, tells the god in a round 3 note with its reasons, and logs the god's wording beside it. Description and Drawback are never changed in round 3 in substance; a pure wording fix the god asks for at confirmation, which changes no term, is made in the Description itself and logged.
- [ ] A rule argued by one god binds only that god's card, unless it is a world rule (the same for every god by its nature, such as how the table prices memory); a world rule is entered once in the ledger as binding every card, and no god is told that another argued it.
- [ ] The ledger takes every request settled against the god in whole or in part, with both arguments, and every ruling that binds more than one card, one entry per matter: several matters settled against one god are several entries, each with its own id. Entries are made at round 2, when the final text is written, and noted as confirmed when the god confirms; a confirmation that changes the text amends its entry, with a dated line saying what changed. A ruling set at the table with no argument against it is entered with `Arguments: none against; set by <who>, by <what>.` An entry that names a file not yet written (a growth file, before 3b.3) names it with the step that writes it. When nothing qualifies, the ledger opens with the line `No disputed rulings at creation.`

Principle from run 02 (Night 2, step 2.3): a value the table needs and no file sets (an id format, a rate) is set once, the plainest way that cannot collide with another, logged, and then used the same way for every god. A body that cannot be struck is still a body that can be wounded (DESIGN 7.8), so what wounds it is written, never left open.

### 2.4 Confirmation, Keeper traits and cards

- [ ] The confirmation round (round 2 or 3) restates every weakness and what it bought, and tells the god its Keeper trait in one line: a new fact, one its rolls and its own traits did not supply, that presses on a contradiction already on its sheet (rubric section 8). Write the trait to `sheet.md`. The player's god gets none. Before telling it, check the trait against every power the god has confirmed, and state its reach in that line: what it touches and what it leaves alone, so that it cuts across no price just agreed. The trait and its reach are written on the god's card, as one line under Form headed `Keeper trait:`.
- [ ] Description and Drawback freeze on the god's confirmation, from the confirmed text.
- [ ] Check the waking month against each god's weaknesses: a weakness that leaves the god unable to act when the year opens (asleep, bound, scattered in that month or its season) is logged, so the night turn knows the god's year opens while it cannot act. Nothing on the card is changed for it.
- [ ] Write `S/gods/<god>/power-card.md` by copying the confirmed round 2 text (with any round 3 wording) into the `powers.md` format, never rewriting it: Form, taken from the god's own `S/gods/<god>/self.md` (round 2 carries no Form; run 06 item 28), with Definitions and Things carried, the bodies rule and god-sense as set, each main power with Status `main`, Limits settled at creation, empty Rulings, Trades, and `Growth: Possible. Not shown.`; `Hidden powers` with only the format's line that two exist; Weaknesses taken, each in full with what it bought; Ceiling `Set by the world. Not shown.`; an empty Dated entries block.
- [ ] Write `S/gods/<god>/card-summary.md` beside the card, under 2,000 words: the card's powers, drawbacks and limits in brief, pointing to the full card, so the god's agent can read its own folder in full (run 06 item 77). It is written again whenever the card changes.

Principle from run 02 (Night 2, step 2.4): the god's confirmation is a check on the Keeper's copy, not a fourth round. Where the god asks for wording the Keeper will not give, the Keeper's reading goes in and the god's is kept in the log, so the disagreement is on the record without reopening the price.

- [ ] Add every god's name and bynames to `S/sealed-terms.txt`.
- [ ] Set luck (standing rules), for all eight, once every card is confirmed: for each NPC god from its negotiation files and card, for the player's god from `P/player/power-card.md` and the DM's Day 2 files. Count each priced step taken beyond what was bought (one each), and each power offered and refused, or a god taking none (two per power), reading the cases in `sealed-factors.md` (What counts). A bend of a default priced in its round (2.3) counts only by the Keeper's judgment there: whether it makes the god's life harder, by how much, net of any price paid for it elsewhere, the reason logged. Write `S/state/luck.md` in template 7.14, every god's line present, 0 where nothing counts, each change with its dated history line; log every count with its source.

Principle from run 01 (Night 2, steps 2.3 and 2.5; Night 3, step 3.4): anything a god must not know (its hidden powers, its secret past, the ceiling, its growth) lives in a folder its agent is never given, never in a section of a file it reads and is told to skip.

### 2.5 Secret backstories, all eight

Written before the hidden powers, which must fit them.

- [ ] Write `S/gods-sealed/common-past.md` first: the far country the eight are the remainder of, under the deep lore's Truth 5, with its names, places and the events near its end, and a shared links table, one row per pair of gods whose pasts touched: the pair, what joined them, which event.
- [ ] Check it against section 8 before it is final: the plane is set only on 3b.2, and its first entry is fixed there. The common past gives nothing a section 8 entry sets (no bearing, no distance, no count of entries) and nothing that contradicts its fixed first entry. A Night 2 sealed file found on 3b to contradict the plane as rolled is corrected on 3b (3b Writes), logged.
- [ ] For each god, player included, write `backstory-secret.md` (`S/gods-sealed/<god>/` or `S/player/`): the rest of the story behind the outline, tied to the common past and to the god's wound. Specific: names, places, one or two events. What the god lost and does not remember. How this past might surface in the world (a being, a mark, a word) without ever stating the mechanism (mystery standard rule 1).
- [ ] Every row of the shared links table appears in both gods' files, in the same terms, and in the log.
- [ ] Names from the common past are sealed names: add every one to `S/sealed-terms.txt`. If any is used again in the world on Night 3, the use is logged as a deliberate likeness, and no god's home ground carries more of them than another's.
- [ ] The common past's title is `# The common past` (no colon, no campaign name), the gods in it are named by label or as "the player's god", and its events are named in lower case unless the name is itself a sealed term on the list.
- [ ] No agent, the DM included, reads these files. The god's past reaches it only through play.

Principle from run 02 (Night 2, steps 2.5 and 2.6): a sealed file is written so that no ordinary word in it can be mistaken for a sealed name. Titles and headings are plain and safe (template 7.13), and what is sealed is named on the sealed terms list, not guessed from how a file is written.

### 2.6 Balance

- [ ] Write `S/balance.md`: for each of the eight gods a weight from 1 to 10 of its total power (main powers, drawbacks, trades), with a line of reasons, the DM's lean note for the player included. The measure (run 06 item 27): a card's weight is what it can do to the world in a year (force, reach, how many it falls on, what it lets the god know from afar), less what its drawbacks and weaknesses take from the god on an ordinary day. 5 is a god plainly more than any mortal worker, whom a gathered people can still trouble, answer and hurt, read against the Q8 blend. The band is 4 to 6. Resemblance between cards counts for nothing. The measure is written at the head of the file. The hidden powers (2.7) are then fitted to bring each god toward the band, and the weights are written again with them and with every god's knacks (2.7), the player's and each NPC god's, in the same file.
- [ ] Where one god looks far out of line before confirmation, say so in its round 2 counter, with reasons, as part of the negotiation. After confirmation a card is frozen: bring a god toward the band only through its hidden powers and knacks, which no agent has seen, and never by any edit of a card. A god under the band is raised by those sealed parts and is never told, in any round or release. Roughly equal, not exactly. If a god stays noticeably stronger, log it as a fact the world's politics will deal with (DESIGN 3.15).
- [ ] The player's card is never changed here. A concern goes to the DM through `P/player/corrections.md` as a question.

### 2.7 Hidden powers and knacks, all eight

Written after the balance weights (2.6), since the hidden powers and knacks are how a god is brought toward the band. Growth files are not written here; they come in 3b.3.

- [ ] For each god, player included: one cool hidden power and one minor one, both weaker than the god's main power, each fitted to its secret backstory and to the god's weight in `S/balance.md`. Each has a drawback, limits, and the condition that surfaces it (a place, a strain, a being met). The condition is set so that it is rarely met in the early years: nothing in the god's first years' ordinary course (its landing ground, its people's daily round, the first things its powers touch) meets it, and the log says why it is rarely met early. When the condition is met in play, the power surfaces (Michael, 2026-11-25: "if conditions are met, then the power is exposed. however, those conditions should rarely be reached so soon."). The Keeper never arranges the condition and never steers away from it. It is never scheduled.
- [ ] For each NPC god: two or three small innate knacks, drawn from its own `S/gods-sealed/<god>/backstory-secret.md` (a craft it kept, a habit of the life it lost, a sense its past left it), each smaller than its minor hidden power, with a limit and the kind of moment that would surface it, never scheduled, and counted in its weight in `S/balance.md` (Michael, 2026-11-22). Whether two or three is a balance tool (rubric section 15), logged with its reason; each is written in the knack format of template 7.13. Nothing in the god's own folder, its releases or any public file names one; it is found only in play (`engine/rules/powers.md`).
- [ ] The player's god, by the mode in `P/player/survey-day1.md`. In mirror mode, its two hidden powers and two or three small innate knacks are drawn from `S/player/mirror.md` (the person's small skills, habits and knacks the DM found, each with its source), made into gifts of this god in this world, and fitted to its secret backstory and its weight as above. In standard mode, the hidden powers come from the secret backstory and the world as for every god, and the knacks from the world and the card. Either way the mode never sets the god's form, core or name, or touches any power the player chose; a knack is smaller than the minor hidden power, with a limit and the kind of moment that would surface it, and is never scheduled. Before drawing, check the card: a trait the card already holds is not drawn again. Nothing touching health, money, relationships or anything sensitive is drawn, even where `mirror.md` holds it; such a line is logged as left out, without its words. Sensitive, for example: an illness or a medicine taken; a debt, a wage or a loss of money; a partner, a parted marriage or a family quarrel. Not sensitive: the survey's own items, a small fear or a habit. A line that is not sensitive is still skipped, logged the same way, if as a gift it would exceed the starting technology or alter a priced term on the card. No line of `mirror.md` is quoted into any file but the sealed log; the sealed hidden-powers file may cite the line a gift came from by its position (`mirror.md`, Found, line N), with its description kept to the log.
- [ ] Write the powers to `hidden-powers.md` in card format, Status `hidden (undiscovered)`, and the god's knacks in the same file, Status `knack (undiscovered)`, for every god: `S/gods-sealed/<god>/` for each NPC, `S/player/` for the player. Append the ceiling line from `S/star.md` at the foot of each. Each file has one top title, `# Sealed: <label>` (never the words "hidden powers"), and one three-hash heading per power or knack, nothing else. Add each power's and knack's name to `S/sealed-terms.txt`. Nothing public names a knack.
- [ ] Check that `P/player/power-card.md` says only that two hidden powers exist and that its Ceiling line reads `Set by the world. Not shown.` If the DM wrote it otherwise, write the correction to `P/player/corrections.md` for the DM; do not edit the player's card yourself.
- [ ] A hidden power fitted to the player's backstory may also serve what the player says it wants. That is allowed with narrow limits (it gives the next step, never an end or a cause), and it is flagged in the night's neutrality check.

### 2.8 Provisional placement and the Day 3 brief

- [ ] Write `S/placement-draft.md`: the region's provisional size (a continent, its rough width and height in miles: its land at least 600 miles across at its narrowest and about 1,000 across on average, aiming for 800 to 1,200), each god's landing country from its Q2 wish and the terrain list, spaced evenly in rough terms, each god's landing spot within its country (what ground it stands on and what lies in reach of its eyes), and a paragraph of the deep history each land will carry, to be written in full in 3b. The landing spots are set here, before the Day 3 brief or any Night 3 release names what is seen from where a god comes down, and those texts are written from them.
- [ ] A thing the star or the lore places "between two gods" (or by any other choice among the seats) is not placed by the Keeper's preference: it is left to the placement roll in 3a.3, among the adjacent pairs of seats once the ring is set, and the draft says so.
- [ ] Write `P/player/day3-brief.md` for the DM: the kind of country the player's god will land in and what the land itself shows, in words the player may hear, and the season. No distance, compass direction or line of sight (those come from the traced map). Nothing of who lives there beyond what the land would show. Land is the ground, its water, growth and weather in the season, and the marks any people anywhere leave in plain sight: smoke, walls, a worn track, laid hedges, grazed turf. Not land, and never in the brief: a mark of one people's craft or way of life (a row of hives, a smithy's slag, a shrine, a boat drawn up), which would answer a Day 3 question before it is asked; anything of the sky (the star, its place or height, a light), which is a star value; who the people are, how many, what they are called. Nothing of history, nothing of other gods. The season is the month the world wakes in, decided on Night 1, given with its season in the same words the NPC gods' releases give it. The brief names only what the placement draft fixes; anything it says is in view is confirmed at tracing (3a.6), and where the trace does not hold it, the Keeper writes the correction to `P/player/corrections.md` for the DM, in words the player may hear. The placement plan in 3a must honor this brief.
- [ ] Mortal magic in the brief: only the pricing terms `world-rules.md` already gives (simple, costs the worker), and that the Keeper fits a people's magic to the world on Night 3. Its prevalence is discovered in play and is not stated.
- [ ] Technology in the brief: the starting level in the words the Night 2 releases gave it (2.1, template 7.5), and nothing more.
- [ ] The brief names the channel for what the DM cannot settle at the table: the DM lists each item in `P/player/people-meeting.md` under `## For the Keeper to reconcile`, and the Keeper answers each on Night 3.

### 2.9 Follow-ups for Day 3

- [ ] Write `P/player/followups-day3.md`: few, from gaps in the player's god that bear on its people (a rejected hierarchy, a form that changes how a people could live, a power that touches its followers). Same bar and constraints as Night 1.
- [ ] Write each NPC god's Day 3 questions to `S/releases/creation/<god>-day3-questions.md`, to go into its Night 3 release. It is an instruction file like the releases: if the god answers it directly, the file names where the answers go (`S/gods/<god>/people-hoped.md`, under `## Questions for you`).

### 2.10 Close

- [ ] Confirm `S/sealed-terms.txt` holds every name, byname, hidden power and knack name and common-past name made tonight, and run `tools/lockcheck.py <name> --leaks --dashes --releases`; read each `--releases` warning and reword the release or brief, or keep it by reading, logged.
- [ ] Close check, then the close order, setting `creation_night: 3a`.

## Night 3a: the peoples and the map

Reads: the keeper log for Nights 1 and 2, and their files where a step needs them; `engine/creation/day3-the-people.md`; `engine/rules/map.md`; `engine/rules/time-and-pace.md`; `engine/style/house-style.md` (the map style block); `S/star.md`; `S/placement-draft.md`; `S/world-draft.md`; the player's Day 3 outputs written by the DM: `P/civs/<people>/record.md` and `state.md`, `P/player/people-meeting.md` (with its items to reconcile and its `## Heard, not promised` section), `P/player/hierarchy.md`, `P/player/rejected-premises.md`, the answers in `P/player/followups-day3.md`, and the Day 3 power blocks (marked "added Day 3") and dated Day 3 entries on `P/player/power-card.md`, and the conduct profile; `P/player/rulings-pending.md`, if the DM wrote one; `P/player/power-lean.md`, for the wishes marked "price: for the Keeper" (3a.2); `S/player/unsaid.md`, under the standing rule; `S/state/luck.md`.

Writes: `S/state/luck.md` (3a.1); `S/releases/creation/<god>-night3.md` and `<god>-night3-negotiation.md`; `S/gods/<god>/people-hoped.md` and `negotiation-night3.md` (by the agents); `S/civs/<people>/record.md` and `state.md` for seven NPC peoples; `S/civs/godless/<people>/record.md` and `state.md` for three to five; `S/civs/<player's people>-sealed.md`; `P/civs/<people>/state.md` (starting numbers); `S/world/placement-plan.md`; the map sheet requests in `SPOILERS_do_not_open/images/requests/`; `S/map/` (the returned sheets); `S/map.json` (the underground layer first, if the world has one, 3a.4); `S/world/gazetteer.md`; `S/gods/<god>/map-knowledge.json`; `P/player/map-knowledge.json`; `P/civs/<people>/knowledge.md` (3a.7); `S/ruling-ledger.md` (the Day 3 rulings) and the ids written back to `P/player/power-card.md`; `P/player/corrections.md` if the DM must change anything; `S/player/requests-answered.md` and the ledger entries for any sealed request or flagged line (standing rules); additions to `S/sealed-terms.txt`; the keeper log.

### 3a.1 The NPC peoples

Order of work: the player's Day 3 ledger entries (3a.2) are entered first, before any pricing tonight, so the ledger's ids run in order. The placement plan (3a.3) and the paint requests (3a.4) may be written and sent as soon as each seat's country is set by the placement draft, before the agreed records, and the records are then written while the sheets are painted, since every land section waits for the tracing anyway. Every checkbox is still run, and the log says the order used.

- [ ] Write `S/releases/creation/<god>-night3.md` from template 7.7: the kind of country the god will land in and what the land itself shows, in the month the world wakes in, written from the placement draft exactly as the player's Day 3 brief was written for the player (no distance, compass direction or line of sight; those come only after tracing), with one line on the sheet's planned scale from the placement draft (the continent's rough width in miles, and that a day's walk is a small fraction of one grid cell), so a god can judge how far its hopes reach; what is true of the world that bears on a people, in the same words the Day 3 brief gave the DM (its mortal magic sentences word for word, and the technology sentence exactly as the god's Night 2 release gave it, nothing new); the Day 3 checklist from `day3-the-people.md` turned toward an NPC; its Day 3 questions from `S/releases/creation/<god>-day3-questions.md`; and the force measure as the Day 3 guide gives it, in plain words: a paid or drilled force of up to about one in fifty of the people is ordinary, and a call-up of the people in need (a levy, a muster) is not counted in it (run 06 item 42). Nothing of prices: no line that culture is free or that an edge is priced, and no weakness asked for (standing rules, no price in a release). The release opens from the premise (template 7.0) and, as Day 3 opened for the player, assumes the god leads a people with a seat, a court or council, and helpers who run things when it is absent, and asks who they are. It carries the god's size lean, rule lean and worship lean in one line each, from its sheet, and asks it to build its people within them and to give its reasons for any departure. The usual number, about 5,000 with a town or city, is given beside the size lean as the middle of the range, never as what is expected; a god whose size lean is not the middle builds within its lean like any other. Every option the player was offered on Day 3 that is not a price is offered once, in the same terms, by kind. Refusal of a default is not listed or invited, as the DM does not offer it to the player unasked: a god that wants to refuse its helpers or any default says so unprompted, with its reasons, and the Keeper prices it in the negotiation, stating the cost plainly (with no helpers, its unplayed time runs on its own conduct alone, no one acts for it while it is away, and its people drift). The people form in the release keeps every heading of template 7.3, with the Helpers hint given without its refusal words, the same in all seven. What the DM told the player in answer to its own questions about turning down or bending a default (what it costs, how it counts when an edge is priced) is not in any release; it is stated in the negotiation, in the same terms, to any god that refuses or bends a default or asks. A larger people is described by its practical costs from the world, as the player was told them, with no word of pricing. Nothing suggests that a people with or without edges is usual. The release gives no example of an edge, of its size or of its price.
- [ ] Spawn the seven agents. Each writes `S/gods/<god>/people-hoped.md` in the people record template (section 7.3): who they are, how many, how they live, their code, skills and culture, any edges it proposes (a god that offers a weakness for one unprompted has it read in round 1), their magic, what they believe about gods, how they are ruled and worship, their helpers or the god's refusal of them, how the god hopes to meet them. The god may name its people and their home.
- [ ] Price every proposed edge against a weakness by negotiation, as in 2.3, in `S/releases/creation/<god>-night3-negotiation.md` and `S/gods/<god>/negotiation-night3.md`: round 1 draft and arguments, round 2 counter and final, round 3 confirmation at most. Round 1 is where the god first meets the price of an edge, put by kind as the DM put it to the player, with no worked example (standing rules, no price in a release). A god that proposed no edge, and bent no default, gets no round: the Keeper logs that none was proposed and goes on. A god whose people form bends or refuses a default (its helpers, most often) has the cost stated plainly, once, in the terms the player was told, in the same round 1 as its edges, or, with no edge, in a round 1 that holds only the bend; it is not a separate stage of the night (run 06 item 38). The round states the cost only: it does not restate the unbent way as a second offer. The god keeps its bend at that cost or changes it of its own accord, with its reasons, and the bend itself may be priced as the price (Michael, 2026-11-23). An edge the god did not propose, which the Keeper finds on reading its people form (a skill most peoples lack, written as ordinary culture), is put to the god once in round 1, both ways: as an ordinary act of its people, narrowed to what most peoples can do, or as an edge priced in the round (run 06 item 45). "Designed, not yet serving" (helpers the god designs who do not know it at landing) is a bend and has its cost stated the same way, so that its cost is stated as the DM states it to the player (the god lands with no helpers in fact, and until each is won in play its unplayed time runs as with none); it is not a refused default, is never priced, and buys nothing. An ask that describes no act only a god can do (one copied from an example, most often) is offered both ways, as an ordinary act of its people at no price and as a real power inside the card's limits, and the god chooses.
- [ ] Set luck again for edges (standing rules), for all eight, the player's from its Day 3 card entries: each priced step a god took beyond what its edges bought adds one; refusing a power it was offered tonight (a power added to the card for an edge), or taking none, adds two per power; a bent or refused default counts only where it was priced in its round, the player's on Day 3 included, and then only by the Keeper's judgment of whether it makes the god's life harder, by how much, net of any price paid for it elsewhere, reason logged, reading the cases in `sealed-factors.md` (What counts), as 2.4 does. Update `S/state/luck.md` with a dated history line for each change, and log every count.
- [ ] A power given to a mortal (a worker who can do what most cannot by the god's gift, a helper who does what the god does) costs the god something (Michael, 2026-11-25; run 06 item 33). The Keeper prices it on the god, in the god's round 1, by the judgment order and the same measure for every god: what the gift lets the mortal do in a year, and for how long. One that dies with the person is less powerful, and costs less, than one that passes on or outlasts its holder. The mortal's own cost of working it (mortal magic costs the worker) is the mortal's and is not the god's price. The price goes on the god's card as a power block or a weakness, as with any power, and the gift is in the people's record with a pointer to it.
- [ ] Size is not an edge. A people larger than the default buys nothing and is priced against no weakness. Its costs are practical and come from the world (more food and fuel, slower growth, harder to move, a longer gestation for a larger kind of people): the Keeper argues them case by case in the negotiation file, the god may argue back, and what is agreed is written in the record's `## How many` section as costs the Keeper applies in play. The same reasoning applies to every god of every size, and more than a few large peoples is possible.
- [ ] Draft the agreed record in `S/civs/<people>/record.md`, every heading of template 7.3 present, `## Helpers` included: the offices the god's rule lean gives it by default, or its refusal with the date. Helpers serve the god from landing only if its meeting says its people already know it. Otherwise the offices exist and are filled, each becomes the god's helper as it hears the god, in play, and until then each runs on the people's own custom, the same for every god (rubric section 12). The world listens and does not obey: each people has a history, neighbors and a trouble its god did not ask for. Fit its magic to the world's level, the same way for every people. Its sections on places and the land are finished in 3a.6, from the traced map.
- [ ] From Year 1 an NPC people's civ agent reads its whole folder `S/civs/<people>/` (`engine/roles/civ.md`). Its record and state hold only what the people know and believe; a truth they do not know goes in the deep history, the god's sealed files or the keeper log, never in that folder.
- [ ] A holding note for 3b.8: each god's corrected view (where its Night 3 release promised what the plan does not hold) and its helpers statement (who serves it from landing, or that the offices run on the people's own custom until they hear it, or its refusal with the date) go into the keeper log under `Held for 3b.8`, by label, for its landing release (template 7.15).
- [ ] Write `S/civs/<people>/state.md` with starting numbers: population, stores, treasure, trade, strength, mood.
- [ ] Decide for each of the eight peoples how the god meets them (already there, waiting, arrived with it), to be reconciled with the deep history in 3b. The player's agreed meeting is kept unless the history cannot hold it; then the smallest change that fits is made and logged, with a line for the DM in `P/player/corrections.md`.
- [ ] Add every NPC people's own name, and every name of a mortal in the sealed records, to `S/sealed-terms.txt`.

Principle from run 02 (Night 3a, step 3a.1): a release offers an NPC god exactly what the player was offered, in the DM's words; where the DM said nothing of a choice the god's sheet leans toward, the release adds only the design's own neutral line for it, never a suggestion. And where two lines of the design seem to pull, both stand: the general one is read as the frame and the particular one as what happens inside it. (The example run 02 gave, all gods coming down at one moment while each woke into its own season, no longer stands: all the world wakes in one month, decided on Night 1.)

### 3a.2 The player's people

- [ ] Set the starting numbers in `P/civs/<people>/state.md`, in words the player may read, if the DM left them unset.
- [ ] Enter the player's Day 3 rulings first, at the head of 3a.1, as on Night 2 (2.3): every ruling marked "settled at creation. Ledger: pending, Night 3" (a Day 3 power block marked "added Day 3", or a dated entry that narrows a Day 2 definition or weakness) is copied into `S/ruling-ledger.md` with the next `L-NNNN`, and the id replaces `pending` on the card. Each pending mark gets its own id, two marks for two matters two ids (`engine/rules/powers.md`). Nothing else on the card is touched.
- [ ] Answer each sealed request and flagged line that arrived on Day 3 (standing rules, sealed requests), and rule each case in `P/player/rulings-pending.md` (standing rules, DM-owned files).
- [ ] A power the player gave a mortal on Day 3 (a mortal knack, a helper who does what the god does) was recorded by the DM as the player's wish and not priced at the table (Michael, 2026-11-25; run 06 item 33): a card block marked "added Day 3, price: for the Keeper", with whom it is for and whether it dies with that person, and a line in `P/player/power-lean.md`. The Keeper prices it tonight on the god, as 3a.1 gives for every god: it costs the god something, less where it dies with the person. The price goes to `P/player/corrections.md` as a cost, in plain words, with its ledger id, for the DM to put to the player before the landing (`Settled for you` never carries it). The player takes the cost or lets the wish go; the card is the DM's to change. Logged, with the measure used.
- [ ] Answer each item under `## For the Keeper to reconcile` in `P/player/people-meeting.md` (each is about the past, or a custom that claims an origin). The world's side of each answer goes in `S/civs/<people>-sealed.md`; anything the DM must change goes to `P/player/corrections.md`.
- [ ] Where a designed mortal's description holds a thing of the land (a ruin, a place, a creature's ways) that the plan and 3b do not place, the Keeper writes to `P/player/corrections.md` what the mortal noticed in its place, from what the world holds there, for the DM to put to the player.
- [ ] Read `## Heard, not promised` as hope only: what the player hopes mortals will do is never written as what they will do. Nothing in it is placed, scheduled or refused; the people's own will decides in play.
- [ ] The player's people record carries a `## Helpers` section as the DM wrote it (offices, or the refusal with its date). If it is missing, ask for it through `P/player/corrections.md`; the Keeper does not write it.
- [ ] The player names its own people and their home. The Keeper names everything else, but never what the player left unnamed for play: houses, clans, places the player chose to leave open are recorded in the sealed files as "unnamed house 1", "unnamed location" and the like, and the civ agent uses the placeholder until play gives a name. Named mortals the player made live in `P/civs/<people>/people/`.
- [ ] The player's descriptions of its land or its past (Day 3) are wishes or its people's beliefs, never facts, until placed in the placement plan (3a.3) or in 3b. Naming a home does not place it: whether a walled town stands where the player said is decided by the plan and the paint. Place each only where the world can hold it, and log each.

Principle from run 02 (Night 3a, steps 3a.5 and 3a.6): land around the player's home that the player did not name and did not leave for play is the Keeper's to name, and may take its name from the player's own names for its people and home, since a people's land is commonly called for them; a thing the player left unnamed for play keeps a placeholder until play names it (build 3, decision 6).
### 3a.3 The godless peoples and the placement plan

- [ ] The godless peoples: three to five, their number and held land set by the Q4 scale: a Q4 result of 1 to 3 gives three peoples, 4 to 7 four, 8 to 10 five. Each in `S/civs/godless/<people>/record.md`: who they are, how many, where, how they live, their code, their history in the land, what they believe about gods, what they want, and whether and how they touch the great events. Each has a real backstory whether or not it ties in. Each gets a `state.md`. The Keeper runs them in the night turn. Non-human peoples with no god count among the three to five, like any godless people.
- [ ] Then write `S/world/placement-plan.md`, a written geography and not a drawing: one continent, its land at least 600 miles across at its narrowest and about 1,000 across on average (aim for 800 to 1,200); the eight seats spaced evenly, each in the country its Q2 wish and the placement draft gave it, each many weeks' walk from the next by the pace table, none crowded and none cut off; the player's seat as its Day 3 brief described it; the godless peoples between them; rivers running downhill to a coast, seas, ranges, rain shadows, borders where the land changes; every terrain on the Night 1 list; the center body where the star's center lies.
- [ ] An underground layer exists only if Night 1 decided the world has one (1.5). If it does, the plan describes it as a layer under the same grid: its depth, its hollows and the mouths that reach them; where it is mostly solid, it says so and names the hollows as its only features. If it does not, the plan has no underground.
- [ ] The placement roll: anything the star or the lore places by a choice among the seats ("between two gods", "near one god") is placed by one roll among the candidates (for "between two gods", the adjacent pairs round the ring of seats in the plan), the method named in `--what` before the roll, and logged. Where the choice leaves a stretch between two seats, a second roll sets where along it, `--die d100` kept to the middle half (25 plus half the face, as hundredths of the way from the first-named seat), so it lies in neither seat's country; named and logged the same way.

Principle from run 02 (Night 3a, step 3a.3): a few rooms, doors or deep places in the pool are sites on the surface sheet, with what lies inside them as data; an underground sheet is for a country below, not for rooms. And a count the design gives the Keeper to run (three to five godless peoples) counts every people that fits its terms, of any kind.

### 3a.4 Paint the sheets

- [ ] The underground in the data first. If the world has one (1.5), write it into `S/map.json` before any painting request: a layer in `layers` with id `under-N`, its `depth` and `painting` (`engine/rules/map.md`), each hollow and mouth a feature `uNN` (type, place in pixels on the sheet's grid from the plan's proportions, who knows of it, notes), and its own regions only where the layer needs them. When the surface is traced (3a.5), each mouth is matched to its surface point and the layer's places moved with it, logged. If the world has none, there is no layer and no underground sheet.
- [ ] Write the map painting prompts from the plan, in the map style block of `engine/style/house-style.md`: the continent seen from above in the manner of a map of Middle-earth, less detail at larger scale, topography only, with no text, labels, figures, buildings, borders or grid. One surface sheet and one cloud sheet for the fog; one sheet per underground layer only if the world has one, asked for as the layer is in the data: where it is mostly solid, as solid rock with the hollows named as the only features. A layer that is one small gallery, or a few hollows with no regions of its own, is not painted: it has no sheet and no request, sent or held, and stays as data with no `painting` (`engine/style/house-style.md`). No close-up sheets. Where the plan gives sea all round, the prompt says so as a hard rule, on a line of its own and again at its end: sea on every side, no land touching any edge of the sheet (run 06 item 43). Every feature the plan sizes (the central feature above all) is asked for by its size in miles, and every planned river is named in the prompt by its course.
- [ ] Read `P/state/images.md`. Send only the requests it covers. A sheet it does not cover (an underground sheet, most often) is written to `SPOILERS_do_not_open/images/held/` and logged as awaiting Michael's go, and the night goes on: an underground sheet it does not cover leaves the layer as data only, already in `map.json`.
- [ ] Put the requests in `SPOILERS_do_not_open/images/requests/`, never in the public `images/requests/`. Log each request and its time. Pull with rebase, push.
- [ ] Wait for the sheets: pull every 30 seconds, for up to 20 minutes. If the job fails or the time runs out, write `P/years/000/night-blocked.md` in one line of procedure (the paintings did not return), commit `Creation night 3a: <name> blocked, paintings not returned`, pull with rebase and autostash, push, and stop with the clock at `3a`. The next session resumes 3a from tracing (3a.5), once the sheets are in.

### 3a.5 Trace the sheets

- [ ] Before tracing, read the sight rule for landing in `engine/rules/map.md` (section 1.4) and log that it is the reading for all eight gods alike. Nothing about any god's view is decided later by a reading of the Keeper's own.
- [ ] When the sheets return (to `SPOILERS_do_not_open/images/out/`), place them in `S/map/` (`surface.png`, `clouds.png`, `under-N.png`) and trace the data onto them per `engine/rules/map.md` into `S/map.json`: the sheet's `miles_per_pixel`, set from the painted land so that the continent's land is at least 600 miles across at its narrowest and about 1,000 across on average (aim for 800 to 1,200), with both widths logged and checked by `tools/map.py validate <name>` before anything is measured; the letter-number grid of about 16 to 20 cells (5 by 4); regions with `elevation`, `water`, `climate` and `neighbors` (each neighbor's id and travel days at the pace table); every settlement as a point, ruin, site, route (`road` features, paths and rivers travel is priced along) and underground feature that exists at creation, each with its id, region and who knows of it; the `landings` block, each landing a region, a point and `ground_ft`, the point's own height in feet read off the region's elevation where the paint shows the landing (`engine/rules/map.md` 1.2), so that describe reports the standing height and does not read it as not given. The plane section is added in 3b.2. The whole world exists here from the lock.
- [ ] Where a thing does not fit the map's feature types, give it the nearest listed type and say what it is in `notes`; where the scale puts things a mile or two apart inside one pixel, carry coordinates to one decimal place. Log both; change neither the tool nor the format.
- [ ] List every planned river in the log against the painting: painted, painted otherwise, or missing. A missing river is traced only where the paint shows its water, and the plan yields as below; log each.
- [ ] Where the paint draws a thing far larger than the plan asked (many times the size the plan gave it), no repaint is asked unless a god's country is lost. The painted shape is traced as a region of the ground it shows, and the thing itself is a feature inside it at its true size, with the truth in `notes`; log it.
- [ ] Every place carries one map name; other names for it go in its `aliases`, which the stamp never marks and which print in the gazetteer only. A place its people call only by a common word ("the hold") takes as its map name the proper name its neighbors or traders use, with the common word among its aliases, since the stamp marks a map name wherever it is written. The one exception is the player's people's home: its map name is the name the player gave it on Day 3, a common word or not, and its element carries `"named_by": "player"` (`engine/rules/map.md` 1.2); that name is never put in `aliases`. A home the player left unnamed carries a plain placeholder as its map name ("the town", "the hold", by its kind), with no `named_by`, and the placeholder is replaced, logged as a dated fact, when a mortal names the place in play (run 06 item 40). Where that name is a common word, the stamp marks it wherever it is written, so after the stamp read each mark and reword any place the word was used in its ordinary sense, logged.
- [ ] An underground sheet, when one returns, is checked against the layer already in `map.json`. Here the data rules, not the paint: the layer is never retraced to the painting, every difference is logged, and the player's sheet shows only the hollows its god knows.

Principle from run 02 (Night 3a, step 3a.5): the data must be able to say what the records say. Where a measurement needs more than the format names (a point where only a region was named, a place finer than a pixel), the Keeper adds the least the tool accepts and logs it; where the format offers too few kinds, the nearest kind is used and the truth kept in notes.
- [ ] Check every feature lands where the paint shows it with a test sheet drawn from a scratch knowledge file, then delete the scratch file. Fix mismatches in the data: the data follows the paint.
- [ ] Stamp the ids: run `tools/map.py stamp <name>`, which appends the bracketed map id after every map name in the sealed files (it is safe to run again). Run it again after any later step that writes map names into a sealed file. Add every map name to `S/sealed-terms.txt` only where it is also sealed for another reason; unseen map names are read from the map by the tool.
- [ ] Measure from `S/map.json` and log: the distance in days between every pair of neighboring seats, on foot by `tools/map.py travel`, by the route it prints; that every seat sits in its wished terrain; that the player's seat matches its Day 3 brief. After any landing move, every seat distance and every landing view is measured again before anything is written from it.
- [ ] **When the paint misses the plan.** Where the paint departs from the plan, the plan yields and the seats are re-set on the painted ground. The paint misses only when it has lost a god's asked-for country altogether (no coast where a god asked for coast), the player's Day 3 country included. Then one repaint is allowed: write the corrected prompt, under a new request id (the paint job skips an id whose painting already exists), to `SPOILERS_do_not_open/images/held/` (sealed, and outside the paint job's trigger paths), log it as an image request awaiting Michael's go, and do not send it without that go. Until the go comes, trace on the sheet in hand; if the go comes before 3b ends, repaint once, retrace, and redo 3a.5 to 3a.7 on the new sheet. Never more than one repaint.
- [ ] Write `S/world/gazetteer.md` from the traced map (its land text from `tools/map.py describe <name> --region <id> --names`, since without `--names` the tool gives places generic names): every region with terrain, elevation, climate, water, neighbors and days, its places, and its ordinary wonders with no mystery attached. Every region has its wonders line; none is left for later.

Principle from run 01 (Night 3, step 3.2, scale): regions are sized to what play needs, not evenly: finest around the seats, coarser between, coarsest in empty country. Anything smaller than the sheet can paint exists as data only, named and placed in `map.json` like anything painted.

Principle from run 01 (Night 3, step 3.2, location): where this runbook and a tool disagree on a path or a format, follow the tool, log the disagreement for review, and change neither.

### 3a.6 Land in the records

Only now, from the traced map, is any land described in distances, directions or sight lines.

- [ ] Every land description starts from the tool's text: `tools/map.py describe <name> --landing <god>` for what a god sees and knows at landing, by the sight rule, and `tools/map.py describe <name> --region <id>` for a region. The Keeper may rewrite the words for a people's voice; every distance, direction, travel time and sight line stays the tool's. The `Neighbors:` block of `describe --landing` lists every neighboring region whether or not it is in view: it is Keeper reference only, and nothing from it goes into a release or record as ground the god has seen; what is in view is only what the sight rule gives. Every Keeper sentence about what is in view, or where a thing stands from the landing (which bank, which side, how far), comes from `describe` or `travel` output, never by hand, in every file it is written into, `P/player/corrections.md` included; a sentence carried from an earlier night is read again against the tool before it is reused (run 06 item 57).
- [ ] Wherever a land description or a knowledge file touches god-sense, it gives direction, nearness or weight only, never how many gods are felt.
- [ ] Finish every people's record (the eight god-led and the godless): every place with its map id; `What they know of the land`, each place with its id and the grade of that knowledge; every distance, direction and travel time measured from `S/map.json` at the pace table's rates. Every land line that gives a travel time names its route and its means, priced by `tools/map.py travel` (standing rules); where a people would go two ways (a road and a short cut, on foot and by boat), the line may give both, each priced.
- [ ] Re-read each NPC god's people-hoped and agreed record against the map. Where a god hoped for ground the paint did not give, the record says what the land holds, and the log says what changed.
- [ ] Run `tools/map.py stamp <name>` again over the finished records.

### 3a.7 Starting map knowledge

- [ ] For each god, `S/gods/<god>/map-knowledge.json`, and for the player `P/player/map-knowledge.json`, in three grades: `seen`, `reported` and `rumored`. Draw each from what the god could know at the moment of landing.
- [ ] Where no god has yet spoken to anyone at landing, each file holds only what the god sees from where it lands by the sight rule (`engine/rules/map.md` 1.4), the same for all eight: the landing region `seen`, what is in view `reported` with its own sight as source. What its people know of the land is in the people's record and enters the god's map only when someone tells it.
- [ ] Public knowledge files carry opaque ids and grid cells only, never coordinates for rumors. A `rumored` entry carries a name as told and a grid `cell`, nothing more exact.
- [ ] Confirm the player's file holds no fact beyond the god's own reach.
- [ ] Write `P/civs/<people>/knowledge.md` for the player's people: what they know of their own land and its neighbors, in plain prose, by the names they use, with grid cells and no map ids, from the map and the people's record (`What they know of the land`). It is public, the Keeper's own, and read by the DM for what mortals say. It is not the god's map knowledge: a name in it reaches the god only when a mortal says it in play. The Keeper updates it each year in pass two of the night turn, with what the people have learned.

Principle from run 01 (Night 3, step 3.9): a god's starting map is what it could know, not what its people know. Knowledge reaches a god only through a telling or its own senses, so a god that has met no one starts with its own eyes.

### 3a.8 Close 3a

- [ ] Every 3a Writes item present. `S/sealed-terms.txt` holds every name made tonight; `tools/lockcheck.py <name> --leaks --dashes --places --releases` runs, each `--releases` warning reworded or kept by reading, logged. Read every record written tonight for a hidden power, a knack or a mirror gift surfaced in it, and log one line that none is. Close check, then the close order, setting `creation_night: 3b`. Begin 3b in the same night.

## Night 3b: the history, the mysteries, the schedule

Reads: the keeper log; `deep-lore.md` in full; `mystery-standard.md`; `clue-design.md`; `S/star.md`; `S/map.json`; `S/world/gazetteer.md`; `S/gods-sealed/common-past.md`; every people's record; the world draft; `S/state/luck.md` (3b.6); `S/player/unsaid.md`, under the standing rule, `P/player/conduct-profile.md` and `P/player/corrections.md` (3b.5, 3b.8).

Writes: `S/map.json` (`plane`); `growth.md` in every sealed god folder and `S/player/`; additions to `S/sealed-terms.txt`; `S/deep-history.md`; `S/mysteries.md`; `S/event-schedule.md`; `S/state/phenomena.json`; `S/cast.md`; `S/world-bible.md`; `S/state/standing.md` (3b.6); `P/world/world.md`; `P/state/clock.md`; `P/state/models.md`; `P/releases/000/dm.md`, with its day sheet; `S/releases/000/dm-sealed.md`, whenever the day sheet has a held moment, a prepared scene or other sealed matter; `S/releases/000/<god>-landing.md` for each NPC god (3b.8); `P/state/rolls.jsonl` (empty); corrections to a Night 2 sealed file (`S/gods-sealed/common-past.md`, a secret backstory) where it contradicts the plane as rolled in 3b.2, each logged with what changed; additions to `S/map.json` for any place first needed here, with the same places added to `S/world/gazetteer.md` (each marked as added on 3b) and to the land lists of the peoples who know them; additions to every people's sealed record that the history requires (what the old tell, partly wrong), never changing anything agreed with a god on 3a; the keeper log.

### 3b.1 The star, if not already rolled

- [ ] If any star item or the ceiling was not rolled on Night 1, roll it now as in 1.2 and 1.6, and log why it was late. Confirm `S/star.md` holds every item with its roll id.

### 3b.2 The plane

- [ ] Roll the plane section by section 8 and write it to `S/map.json` under `plane`, every roll logged with its id, the roll that set how many entries there are kept beside the list as `plane.count_roll`.

Principle from run 02 (Night 3b, step 3b.2): where a format carries a field and no table says how to fill it, the field is filled by the same roll the nearest table uses for that field, logged; it is never left to the Keeper's choice.

### 3b.3 Growth files

- [ ] Write `growth.md` for every god (`S/gods-sealed/<god>/`, `S/player/`), in template 7.10: one block per power, main and hidden, and one per knack, its `Related skills` line filled from `hidden-powers.md` and every other field empty. The night turn fills them only when the world earns it.

### 3b.4 The deep history

- [ ] Write `S/deep-history.md` to the depth the Q5 scale set: the rise and fall of specific cities and towns, with names, dates in years before the arrival, causes and what remains of each; the roads, ruins, sealed doors and bones from the Q12 pool; the travelers from afar (Q14), when they came, from which entry in the plane section, and what they brought; the non-human peoples (Q13); and individual stories, a dozen at least, of named mortals whose traces could be found. Concrete, per mystery standard rule 12. Every place carries its map id; any place first needed here is added to `S/map.json` now, traced on the paint, and logged, and goes into the gazetteer and the land lists of the peoples who know it, measured from the map. Each people's sealed record gains what its old tell of this history, partly wrong where they would be wrong, so that the record agrees with the history it is checked against; the record holds the telling only, and the truth stays in `S/deep-history.md`, since a civ agent reads its people's folder (3a.1). How each traveler or line from afar came across the distance is the Keeper's to decide, for each, within the pace table and the lore, and is logged in the sealed files only (Michael, 2026-11-23). Dates the lore gives no range for (the last fall here, when earlier gods came) are rolled inside a range set from this star's phase and the Q5 depth, written before the roll (deep lore, "Setting this star's numbers").
- [ ] Check it against the deep lore: nothing contradicts a truth, nothing explains a truth.
- [ ] Check it against every god's and people's record: each meeting is possible in this history, and each people's dates agree with it.

Principle from run 01 (Night 3, step 3.5): a body the deep lore needs for one of its truths (an older god who rose, a hoarder, carriers) may be placed in the history when the star's results and phase give it the time; it is never placed on the ground as a rival to the arriving gods. When a star result removes a body the lore names, nothing is invented to stand in for it.

Principle from run 02 (Night 3b, step 3b.4): earlier gods may stand in the deep history on the same terms, when the lore needs their bodies and the phase gives the time; none is on the ground at the arrival. And everything in the history keeps to the pace table: a traveler from an entry in the plane farther than one life can walk or sail is the last of a line that set out generations before, never one who made the whole journey.

### 3b.5 The mysteries

Per mystery standard rules 13, 14 and 16 and the Q18 and Q19 pools. Write `S/mysteries.md`, one section per mystery, each in the mystery template (section 7.8), every heading present.

- [ ] One epic, threaded through the whole campaign, involving immortal power, whose answer still has to be executed once found and may not be solvable by one god alone. Its central measurements can only be earned (rule 14). List every way they could be earned and confirm none is a scheduled visitor.
- [ ] Several long mysteries at about half the epic's span, some related to it, each with immortal stakes.
- [ ] Many short mysteries of 3 to 12 years, local and mortal, drawn from the deep history and the pools.
- [ ] Every clue placed at a location (with its map id) or on a being, showing an effect, object or behavior and never a mechanism, with more than one reading written. Every branch a god might act on, wrong ones included, with what the world does in answer. What is never found.
- [ ] Every being that answers questions has a written limit on what it knows and on how it may be asked (rule 16), in the mystery that uses it and in `S/cast.md`.
- [ ] Confirm no decisive clue is delivered by a visitor (rule 4), no counter-clue is planted (rule 2), no mortal in the record is fully right about a cause (rule 1), and that most of the world is not a clue (rule 3): each region's ordinary wonders are in the gazetteer with no mystery attached. Read every gazetteer wonders line against the mysteries; a line that is a clue is rewritten as an ordinary wonder, logged.
- [ ] Confirm each undared wish that was kept is placed away from its own god's certain path, with the distance from its seat.

### 3b.6 The event schedule

- [ ] Write `S/event-schedule.md`. Clocked events: natural, on fixed years and seasons no one controls, each with its lead time, the signs that precede it, where those signs appear (map ids) and who could notice. Triggered events: the condition, what fires, and which clocked events it may speed, delay or redirect. Every mystery's cost if ignored appears here as a clock or a trigger, with the mystery named.
- [ ] Clocked rows name their month. There is one count of months for the whole world: month 1 is the waking month decided on Night 1 (1.5), the clock's `season_opens`, and month N is the same month, in the same season, in every country, on the same nights (Michael, 2026-11-25). A season named in a row is that season everywhere. An event that crosses countries, or runs over more than one season, is written as one row for each stop or stage, each with its month in the one count; its legs are priced by the tool in the year they run (run 06 item 53). This replaces counting each country from its own god's waking season, the one-season rule for crossing events that followed from it (Michael, 2026-11-23), and L-0043. A cycle (a herd's round, a recurring visit) runs both ways from its rolled year: that year is one of its years, and earlier years in the cycle are too. No row names, or has any mortal give, a thing the player left unnamed for play: the people answer with whatever play has named it by then, or the record keeps the placeholder and the telling says only that they were answered.
- [ ] Random events: a table with factors for `tools/roll.py`, at the base and opening step `clue-design.md` gives (its pacing spine), weighted down in Years 1 to 7 by that step, so the opening is quiet and the distance between gods does its work.
- [ ] Where a schedule roll chooses which people a natural harm falls on (a weather year, a murrain), it weights the choice away from a lucky god's people by the god's luck steps (standing rules), named in `--what` before the roll. A people the same harm has already struck in that year's window is removed from the targets before the cast, logged; the bands are set over those left, by the method in `sealed-factors.md` (Weighting), and cast as one weighted draw, `tools/roll.py --campaign <name> --who keeper --what "<the harm>, which people" --weight <label>=<share>` with one `--weight` for each target, which logs the bands with the draw.
- [ ] Write `S/state/standing.md`: each god's standing on the lore's scale (the ceiling from `S/star.md`), one line per god (the player's under `player`), at the landing value, which is 20 for every god (run 06 item 53): a people that awaits a god holds a tale in mind and not yet this god, and a people that knows its god on sight has known it for no time at all. The triggers that rest on it (the voices, the rising) read it. The Keeper updates it in pass two of each year's night turn, in sealed state, by the yearly rule in `SPOILERS_do_not_open/keeper/year-turn.md`, with a dated line for every change and its reason. It is never released.
- [ ] Recurring phenomena: name each, its true occurrences per year for at least the first ten years, written to `S/state/phenomena.json` in the shape `tools/phenomena.py` reads; the night turn runs that tool with `SPOILERS_do_not_open/campaigns/<name>` as the campaign path. Each entry's key is its label; its `name` field is the phenomenon's words as public prose would write them, which `tools/lockcheck.py --leaks` reads to find a true count written beside them (run 06 item 53). Its months may be written now under the optional `months` field, each year's list counted from the waking month and as long as that year's count; years without them are rolled in pass one (`SPOILERS_do_not_open/keeper/year-turn.md` section 3.1).
- [ ] Confirm no event herds the gods toward one place and no path or secret way exists for the plot (DESIGN 8.5).
- [ ] The schedule's headings are kept to two levels and its events to table rows; every schedule and mystery title is one no public file uses as an ordinary word.

Principle from run 02 (Night 3b, step 3b.6): a number chosen inside a range the lore gives (the year of a fall, a span) is a random outcome: it goes through `tools/roll.py`, with the method named in `--what` before the roll. Years the lore gives for its own test world are shapes, not dates; the Keeper sets this world's years from this star's own results, logs each with its reason, and moves none closer to any god for a story. Natural clocks the Keeper sets itself (weather years) are spread so that no one people takes more than one in the quiet opening years.

### 3b.7 The small cast, the names, the world bible

- [ ] Write `S/cast.md`: a few world-level figures, mortal or otherwise, drawn from the Q17 pool and the deep history, each with nature and history fixed, placed with a map id. Whole peoples may count. Everyone else rises from play.
- [ ] Name the world as the Keeper knows it, and record what each people calls it and its star.
- [ ] Write `S/world-bible.md` (no codex or other public summary is built; the player's files and the morning stories carry the history), the sealed summary of the whole world: the rules made final, the star, the plane, the land, the peoples, the cast, pointers to the deep history, mysteries and schedule, and where each Night 1 candidate went or why it was left out.

### 3b.8 Year 1's first morning inputs

- [ ] `P/world/world.md`: public facts only, as the player's god would know them on waking: its land as it first sees it, measured from `S/map.json`; its landing given by grid cell only, the cell it stands in, never a region's centroid cell (`engine/rules/morning-story.md`); its people's number and way of life; the technology, as the starting level (2.1); the month the world wakes in, with its season, and the hour of landing; the land it knows and the land only rumored; the world's name as its people say it, under a line telling the DM that such names reach the god only when first said in its hearing. What the god knows on waking comes only from its own senses and what it has been told, and at landing no one has spoken to it. Nothing a god could not know, no count of gods, no history beyond what the people tell, no magic level beyond what is in view.
- [ ] `P/player/map-knowledge.json` from 3a.7.
- [ ] `P/state/clock.md`: campaign, `season_opens` set to the waking month decided on Night 1 (1.5), in the world draft's words; `status` stays `creation` until the first morning is done (section 4.1).
- [ ] `P/state/models.md`: the model for each role for the night turn, by role only (one line for the NPC gods as a role), with no per-god line and no count of agents or gods. Principle from run 01 (Night 3, step 3.11): where no file names a value that is Michael's to choose, the Keeper copies the last value he approved and marks it as his to change; it never chooses one itself.
- [ ] `P/releases/000/dm.md`: everything the player's god senses and knows at the moment of landing, its bodily senses included, god-sense as set (felt as direction, nearness or weight, never as a count or a number of pulls), and what is in view, with every distance, direction and sight line measured from `S/map.json`, from `tools/map.py describe <name> --landing player --knowledge campaigns/<name>/player/map-knowledge.json` with its `Standing ground:` line checked the same way. No count of any recurring phenomenon: the DM takes counts from `tools/phenomena.py` only when the god or its people would notice. What the god's people know of the land is not in it; it points the DM to `P/civs/<people>/knowledge.md` (3a.7) for what mortals may say. Under `## Settled for you`, only the Keeper's rulings on what the player itself designed or priced at the table and has not yet heard the outcome of (whether a force it designed stands at landing, whether an office it designed serves), one plain sentence each, without a name or a number the town would have to tell it, for the closing block of the first morning (`engine/rules/morning-story.md`). What the people would tell (their past, their neighbors, the land, the names they use) is never settled there: it comes in play, from mortals (run 06 item 51). What belongs before the landing stays in `P/player/corrections.md`. The Day 3 sealed requests answered on 3a.2 are not in it: the DM reads their lines in `S/player/requests-answered.md` itself. It carries the `## Day sheet` for the first played day, with its sealed part in `S/releases/000/dm-sealed.md` (every held moment's and prepared scene's facts, parameters and reasons), in the form `SPOILERS_do_not_open/keeper/year-turn.md` section 2 gives (run 06 item 60). The DM writes the first morning story and painting request from it per `engine/rules/morning-story.md`.
- [ ] For each NPC god, `S/releases/000/<god>-landing.md`, in template 7.15: what it senses and knows at the moment of landing, by the same reading as `P/releases/000/dm.md` gives the player's god, every view from `tools/map.py describe <name> --landing <god> --knowledge SPOILERS_do_not_open/campaigns/<name>/gods/<god>/map-knowledge.json` after tracing (without `--knowledge` the tool names places as the player knows them; run 06 item 49), whose `Standing ground:` line gives the landing's own height (a line saying the height is not given means `ground_ft` is missing in `map.json`: set it, log it, and describe again); the hour of landing; what is in view; its helpers statement and its corrected view, from the 3a.1 holding note. Where its Night 3 release promised something in view that the trace does not hold, this release says what is there instead. The night turn gives each NPC god its landing release at Year 1 setup, as part of its first release (`engine/night/night-turn.md`).
- [ ] `P/state/rolls.jsonl` begins empty. Creation rolls stay in `S/state/rolls.jsonl`.
- [ ] The hour of landing is one hour for all eight gods, taken from what the 3a records already say of the gods' coming down; where they say nothing, the Keeper sets it once, the same for all, and logs it. A night hour is read by the night-landing reading in `engine/rules/map.md`, for all eight alike.
- [ ] The sky, in every landing release and the player's: the star is no map feature, so its place is set by one method for all eight, written in the log before the first release: the bearing from the landing point to the map point under the star's center, from `S/map.json`, to the nearest of eight; its height from the tool's miles between the two points and the star's sealed height in `S/star.md`, said as a rough share of the way up the sky and never as a figure. Told among the things in view, with no name and no weight (run 06 item 48).
- [ ] `S/sealed-terms.txt` holds every name made tonight (mystery and schedule titles are read by the tool; add any sealed name inside them that is not a title). A name this step makes public (the player's people's names for the world and its star) comes off the list in the same commit, logged. Run `tools/map.py stamp <name>` over the 3b files.

Principle from run 02 (Night 3b, step 3b.8): a date or fact the record needs and no file sets is set from what the record already shows, and never where it would hand a god a gift or a blow the world has no reason to give. What is in plain sight at landing is given among the god's senses like anything else in view, with no name, weight or place in the telling that marks it out.

### 3b.9 Hand to the checker

- [ ] The 3b hand-off check, before the commit: every 3b Writes item present and complete, a landing release for every NPC god among them; `S/sealed-terms.txt` holds every name made tonight; `tools/lockcheck.py <name> --leaks --dashes --places --releases` and `tools/map.py validate <name>` run, every hit fixed in the files the Keeper owns or logged for the checker; the neutrality self-check and the night's roll range written (standing rules, close of every night).
- [ ] Rerun every travel line in the records, earlier nights' included, through `tools/map.py travel` for the route and means it names; correct any that differ, logged. The travel lines live in: every NPC people's agreed record (`S/civs/<people>/record.md`), every godless people's record (`S/civs/godless/<people>/record.md`), `S/civs/<player's people>-sealed.md`, `P/civs/<people>/knowledge.md`, the gazetteer's neighbor lines (`S/world/gazetteer.md`, regenerated with `describe --region` and compared), and any release or record that gives a trip's miles or days. A record states the tool's figure to the tenth of a day as the tool prints it, with its full days beside it where a people counts in days ("12.0 days, 13 full days"). Every travel line names its start point and its end point by name or map id, or by the tool's own point (`f22:edge`); a line with no start is given one before it is run, logged (run 06 item 52).
- [ ] Record the times in `S/state/timing.md`, commit `Creation night 3b: <name> ready for lock`, pull with rebase and autostash, push. Log the commit id in the keeper log, then commit that line alone as `Creation night 3b: <name> lock commit logged`, pull, push. Start the continuity checker on the lock checklist (section 4). The Keeper does not run the checklist on its own work.

## 4. The lock

Writes (the checker's, for the lock): `S/years/000/lock-flags.md` and the full script output beside it; `S/leak-allow.txt`; `P/years/000/lock.md`; `S/LOCKED.md`. The Keeper writes none of these.

The continuity checker runs this checklist, not the Keeper. It reads every file under `S/` and `P/` that a line names, and runs `tools/lockcheck.py <name> --all` (places, leaks, releases, mysteries, rolls and dashes; `engine/roles/checker.md`). For each line it records yes or a flag with the file and the finding in the sealed lock flags file `S/years/000/lock-flags.md`, and the full script output beside it. The public `P/years/000/lock.md` is the checker's, and carries one line only, in one of three states (the lock is running, flagged, or passed), with no time and no sealed term (a stage time is not play; the time of each state goes in the lock flags), as `engine/roles/checker.md` gives it. The Keeper fixes, commits, and asks for a rerun of the flagged lines, as in the night turn. When every line is yes, the checker writes `S/LOCKED.md` (template 7.11) naming the commit it checked, and commits `LOCKED.md` alone, after that commit; a commit cannot carry its own id.

The scripts check only what they check: `--places`, the bracketed ids and bare map names; `--mysteries`, that each mystery has every template heading, that its Clues section mentions readings and its Branches section says what the world does; `--leaks`, the sealed term list against `P/`; `--releases`, the Keeper's releases under `S/releases/` and the Day 3 brief against the world draft's scarcities (a warning, read and reworded or kept) and the kept sealed terms (a failure); `--rolls`, the rolls log; `--dashes`, em and en dashes. Everything else the checker does by reading: the count of epic, long and short mysteries from their `Kind:` lines; that every clue has a location and its readings, and every branch its answer; every rule 16 `Limit:` line; the mysteries against rules 1 to 17; the backstories against the shared links table; every meeting against the deep history; every distance, direction and sight line against the map; every public file, line by line, including hidden power names, common-past names and the count of gods in any wording.

**The leak allow file.** `S/leak-allow.txt` (`SPOILERS_do_not_open/campaigns/<name>/leak-allow.txt`) is the checker's, not the Keeper's: it is in the checker's Writes for the lock, and the Keeper never writes or edits it. When the checker rules that a `--leaks` hit reveals nothing (a number word in a work rate, a count of the player's own helpers, often in frozen card text or verbatim transcript no one may reword), it writes the phrase there, one per line, each with a `#` comment giving its reason and the date, either as the bare phrase or, to allow it only on a line of one file, in the line form `in <file>: "<phrase>"` that `engine/roles/checker.md` and `tools/lockcheck.py` read (build 7 check, minor 2), and lists it in the lock flags; `tools/lockcheck.py --leaks` reads it. It never holds a sealed term.

**The sealed factor's name in the player's words.** The creation transcripts (`P/player/transcript-day*.md`) are the player's own words, kept verbatim, and are never reworded. The leak scan does not check them for the sealed factor's name: the player using an ordinary word reveals nothing, and that conversation stays sealed (Michael, 2026-11-22). It checks every other public file for it, so no agent ever writes it. A hit in a file the Keeper owns is reworded by the Keeper. A hit in a DM-owned file (a survey answer, card, backstory or profile line that copies the player, or the DM's own prose) is replaced by the Keeper itself with a plain word of the same sense, logged in the sealed keeper log only: no correction is written to `P/player/corrections.md`, no flag text in a public file names the word, and the DM keeps the changed word (`engine/creation/day1-world-survey.md`, `day2-the-god.md` and `day3-the-people.md`). The checker flags a hit in any file but the transcripts, and never clears one by an allow line; a `!` term in `leak-allow.txt` does nothing, since the scan never exempts it. The same holds after the lock, in the morning scan and the night turn.

**A flag no file settles.** The lock never pauses for a ruling. A flag that only an owner could clear (a ruling no file and no entry in `S/rulings.md` gives) is ruled by the checker by the judgment order in `engine/roles/keeper.md`, recorded with its reasons in the lock flags under `Rulings for review`, and the lock goes on; the Keeper applies what the ruling needs in the files it owns, logs it, and lists it under its own `Rulings for review`. In a test run the same holds, except for a ruling Michael has asked to make himself: that one flag waits for his entry in `S/rulings.md`, and every other line is checked and fixed meanwhile.

**Deadline.** If the lock has not passed by 6:00 Pacific, the checker stops. The clock stays at `creation_night: 3b`, `P/years/000/lock.md` reads flagged, the 6:30 wake posts its notice that the world is still being built (`engine/night/creation-nights.md`), and the night session commits, pulls with rebase, pushes and stops. The next session resumes 3b from the flags. When the lock passes, the night goes on to section 4.1. The lock is named by its commit id. No tag.

**Fixing flags.** The Keeper fixes flags in the files it owns. A flag on a DM-owned public file is never fixed by the Keeper's own edit, except the sealed factor's name, replaced as above: the Keeper writes the change to `P/player/corrections.md` for the DM, and the line stays flagged until the DM has made it. After any fix that changes a region's shape, the Keeper rereads every record line that places a fixed point in or beside that region (a landing, a settlement, a feature, a seat distance, a landing view) and measures it again with the tool, logged, before asking for the rerun. Each round of fixes is committed as `Creation night 3b: <name> lock flags fixed, round N`. The round number stays in the commit; its line in the sealed `S/state/timing.md` names the fix by what was written (`lock flags fixed`), by the same style choice as every stage, and no public file carries it. `tools/lockcheck.py` skips the checker's own `lock-flags.md`.

Principle from run 02 (the lock rounds): a flag on one god's view, distance or rule is fixed by one reading applied to all eight gods alike, and every god's lines are rechecked against it, never by a special case for the god that was flagged.

Principle from run 01 (Night 3, step 3.10): a version is named by something the record already holds, its commit id, written into the lock file; nothing depends on a name the remote may refuse.

Every line must be yes before `LOCKED.md` is written.

- [ ] Seven NPC gods, no shared seed, no shared domain, each labeled by domain with no number, each with sheet, self, goals, record-of-gods, negotiation files, power card (Description and Drawback frozen, `Hidden powers` saying only that two exist, Ceiling `Set by the world. Not shown.`), map knowledge, a landing release in `S/releases/000/`; and in `S/gods-sealed/<god>/` a secret backstory, two hidden powers and two or three knacks drawn from that backstory, each knack with its limit and surfacing moment and Status `knack (undiscovered)`, with the ceiling line, and a growth file; every god's weight in `S/balance.md` counts its knacks; no knack is named in the god's own folder, its releases or any public file, and every knack name is on `S/sealed-terms.txt`.
- [ ] The player's god has in `S/player/` a secret backstory, two hidden powers and its knacks with the ceiling line (drawn by the mode the player chose, nothing sensitive drawn), and a growth file; its people have `P/civs/<people>/knowledge.md`, with names and grid cells and no map id; its public card names neither hidden power and its Ceiling line is `Set by the world. Not shown.`; every "settled at creation" ruling on it carries a ledger id.
- [ ] Every row of the shared links table in `common-past.md` appears in both gods' backstories and in the keeper log; sealed names reused in the world are logged as likenesses and cluster near no one god.
- [ ] Eight peoples with records and starting state, each record with a `## Helpers` section (offices, or a refusal with its date). Every edge priced; no size priced as an edge. Every NPC people built within its god's rule and worship leans, or with the god's reasons for departing. Every meeting reconciled with the deep history; every people's dates agree with it. Nothing the player left unnamed for play is named in any file.
- [ ] Three to five godless peoples with backstories and starting state.
- [ ] `tools/lockcheck.py --places` passes: every bracketed id in `S/` exists in `map.json`; no warning stands for a capitalized map name without its id (the files the stamp skips are not warned on, standing rules, Places); every region, settlement, ruin, road, site, underground feature, landing and plane entry referred to anywhere exists in `map.json`.
- [ ] `tools/lockcheck.py --releases` passes: no kept sealed term in any release or the Day 3 brief; every warning on a world scarcity is read, and each one kept is listed in the lock flags with the reason it reveals nothing.
- [ ] Every distance, direction and sight line in every release and record that describes land matches `map.json`, and every travel time matches `tools/map.py travel` for the route and means its line names; the checker measures each.
- [ ] Gods spaced evenly, read as a range (`engine/roles/checker.md` 9): the shortest distance from a seat to its nearest neighbor is at least half the longest such distance; every terrain from Night 1 present; transitions realistic; one continent on one sheet with the letter-number grid, its land at least 600 miles across at its narrowest and about 1,000 across on average, as `tools/map.py validate` measures; an underground layer (`under-N`) in `map.json` exactly when the Night 1 decision, the history and the placement plan give one, with `validate` passing it, and no underground sheet when there is none.
- [ ] `S/state/luck.md` holds a line for every god, the player's under `player`, each from 0 to +5 with a dated history line and reason for every change, matching the counts in the keeper log; no luck value or word of luck appears in any release, card, sheet or public file.
- [ ] `star.md` holds every per-star roll and the ceiling, each with a roll id. The plane section holds its rolls with ids.
- [ ] `tools/lockcheck.py --mysteries` passes (every template heading present, an `Answers questions: yes|no` line in each, a `Limit:` line wherever it is yes, readings in Clues, the world's answer in Branches). By reading: one epic, several long, many short mysteries by their `Kind:` lines; every clue with its location and readings; every branch with the world's answer; what is never found filled; each passes rules 1 to 17 of the mystery standard; every being that answers questions has its written limit.
- [ ] Every event has a cause, every mystery a cost, every cost a clock or trigger in the schedule. Random events weighted down for Years 1 to 7. Recurring phenomena in `phenomena.json` for at least ten years.
- [ ] God-sense is written everywhere as direction, nearness or weight, never as a tally.
- [ ] Every world rule (god-sense, bodies, magic, how gods stand out) is one rule for the whole world. No wish became a local exception, and no place makes a rule read differently.
- [ ] Every creation roll is in `S/state/rolls.jsonl`; nothing rolled twice; every reroll has a reason and names the roll it replaces.
- [ ] The keeper log records every blend with its placements and eight answers, every vote count, every placement, every clamp, every leftover, every decision the files did not make.
- [ ] `S/sealed-terms.txt` exists and holds every god name and byname, hidden power and knack name, common-past name and sealed place name in the sealed files, and the sealed factor's name in each case form on `!` lines. `tools/lockcheck.py --leaks` passes, reading `S/leak-allow.txt` for the hits the checker has ruled are not leaks, each listed in the lock flags, and the checker has read every file in `P/` against this line: nothing in `P/` reveals a vote, a pool, another god, the count of gods, a sealed place id or coordinate, a star value, the deep history, a mystery, the schedule, or a phenomenon's count before it is seen.
- [ ] Nothing in any file contradicts the deep lore, and no file explains what the deep lore keeps mysterious.

### 4.1 After the lock: the first morning and Year 1

The first morning's painting is a step of creation. Read `P/state/images.md`: if it covers the first morning, the request goes to `images/requests/` as usual; if not, the DM's request goes to `images/held/`, logged as awaiting Michael's go, and the step continues without waiting.

- [ ] The DM agent writes `P/years/001/morning-story.md` and the first morning's painting request from `P/releases/000/dm.md`, per the first-morning section of `engine/rules/morning-story.md`, and draws the first map with `tools/map.py draw <name> --zoom landing`. A painting request beyond the approved count waits in `images/held/` for Michael's go, and the step goes on without it.
- [ ] The continuity checker reads the first morning story against the lock (every fact, view and name in it against the locked files), and its finding is logged; a flag is fixed as in section 4 before the clock is set. The scan checks words, this read checks meanings. Each name the landing sheet shows from creation is listed in `P/player/map-meta.json` under `creation_names` (and printed as a note by the draw command); the read checks that the story's (oog) map line says why each shows.
- [ ] Then run `tools/lockcheck.py <name> --leaks --dashes` once more over the public folder, after every fix the read asked for. Fix any hit (through `P/player/corrections.md` where the file is the DM's) and rerun until clean.
- [ ] The close waits for the first morning's painting: pull every 30 seconds, for up to 20 minutes. If it has not returned, or its request is held, log that it is pending and go on.
- [ ] Only then the Keeper sets `P/state/clock.md`: for a campaign, `year: 1`, `status: open`, `season_opens` as set, `creation_night` removed; for a test run the same, with `status: closed` in place of open (a test campaign is never left open). A test run that continues into a play test is set to `status: open` under the `S/rulings.md` entry that approves the play test, logged with the entry's date; the play test's last night sets the clock to `status: closed` (run 06 item 56). With no such entry the test run closes. Log that Night 3 closed, with the time from `tools/stamp_time.py`, then the close order: record the times in `S/state/timing.md`, commit `Creation night 3b: <name> closed`, pull with rebase and autostash, push. Nothing is written after the push.

## 5. After the lock

Nothing is added. Geography, structures, beings, secrets, clues, history and the schedule exist from the lock and change only through actors in the world during play. When play reaches something the records do not specify, the Keeper resolves it conservatively from the deep lore and deep history, writes the new fixed fact in the keeper log with the date and the action that reached it, and it is fixed forever. A name the player left for play stays a placeholder until play gives it one. No clue is added to rescue a line that went quiet, no second cause is planted beside a true sighting, and no wish, theory or out-of-game remark changes what the world holds or how often it is reported.

## 6. Decisions the files did not make

When a step meets a question no file answers, the Keeper rules it by the judgment order (standing rules), applies it, logs it in the creation log format with its reasons, lists it under the night's `Rulings for review`, and goes on. It never stops or pauses the night for one, and never waits on the owner. A campaign's own rulings stay in its own keeper log; only the principle behind one, once Michael has reviewed it, comes into these standing files.

## 7. Templates

Every template that another agent reads gives full paths. `<name>` is the campaign's folder name and is filled in by the Keeper; `S/` and `P/` never appear in anything an agent receives. Every release ends with the lines: `A git pull --rebase --autostash origin main is always allowed; it writes no file of yours. If a pull fails, retry it once. Do not commit or push; the session that spawned you commits your files.`

### 7.0 The premise, in every god release

```
## Why you come down
Gods come down here to lead a people: to find or gather them, to build, to
rule, and to spread. That is what the world below expects of you.
```

### 7.1 `sheet.md`

```
# Sheet: god-<domain word>

## Leans
1. Mind: <n> (intelligent 1, clever 100). <the lean's sentence, rubric section 1, such as "Leans hard toward clever.">
... all ten, both ends named, each with its sentence, Company as "<n> (rolled <m>, +25)"

## Seed
<the seed's text from the rubric, without its table number>

## Domain, form, virtue, flaw, wound, voice
<each as text>

## Bargaining stance
<the band and its words, from rubric section 11>

## The people it leans toward
Size: <band and words, rubric section 12> (score <n>)
Settlement: <the one result from the settlement table>
Rule: <the rule lean, with its kind from the variety table where it has one> (score <n>)
Worship: <the worship lean> (score <n>)

## Name
(Night 2)

## Traits (own)
(Night 2)

## Keeper trait
(Night 2)

## The month the world wakes in
(filled by the Keeper on Night 1, after the waking vote; the same words on every sheet)
```

No roll id appears on a sheet; every id stays in the keeper log. Where a test override forces a lean, that lean's line carries the result only, with no score, on every god's sheet alike (the god the override did not change included, so the absence marks no one); the scores stay in the keeper log. The other lines keep theirs. The forced Rule line gives the lean's name and its sheet words as rubric section 12 has them, the words on priests included.

### 7.2 `self.md`

```
# Self: <name>

## Name
<its name, if it has one; what it is called, and by whom>

## Form
<enough for an appearance card: shape, size, face, senses, how it moves>
### What breaks you
<what can wound, hold, scatter or shut you out; a form nothing can strike says
what does break it>
### When your body is broken
<one line only: what you wish happens, and how you would return; or "none">
### Things carried
<each thing it carries; anything that does more than an ordinary object is also proposed below as a power>

## Traits
<two traits, each with the rolls it reconciles>

## Backstory outline
<who it was and what it lost, as it dimly remembers; the wound felt, never explained>

## What it wants
<on arrival, knowing only that it expects a people>

## Proposed powers
### <power name>
What it does:
Why this god has it:
Edge cases it expects:

## The people it will lead
<a paragraph, within the rule and worship leans you were given, or your reasons
for departing from them>

## The premise
<for the standing premise only (why you come down); leave empty unless you push
back on it of your own accord; then "Premise rejected:" or "Premise bent:", and
why. A bend of a world rule goes under the power or section it touches, not here>
```

### 7.3 People record (`people-hoped.md`, and the agreed `record.md`)

```
# People: <name, if the god or the people name themselves; else "unnamed">

## Who they are
## How many
<if larger than the default: the practical costs agreed, which the Keeper applies in play>
## How they live
## Their code
## Skills and culture
## Edges and their weaknesses
<people-hoped.md: headed "## Edges", what your people can do that most peoples
cannot, if anything. Agreed record: each edge, the weakness that pays for it, and
one measurable line once priced>
## Their magic
## What they believe about gods
## Rule and worship
<how they are ruled and how they worship, within the god's leans or with its reasons>
## Hierarchy
<who advises, who rules under the god, who settles disputes; or that the god rejected one>
## Helpers
<the offices that run things when the god is absent (offices, not named people,
unless play names them) and how orders travel; or "Refused, <date>" (or
"Dismissed, <date>"), and empty until play fills it>
## How the god meets them
## What they know of the land
<agreed record only: each place with its map id and grade of knowledge>
## Named mortals
<agreed record only: pointers to people/<name>.md>
## Questions for you
<people-hoped.md only: the god's answers to its Day 3 questions, one under each
question's number; the agreed record does not carry this heading>
```

### 7.4 Night 1 release, and the answer format

```
# Release: god-<domain word>, Night 1

<the sheet, as written>

You are this being. Answer the questions below from inside your character,
in your own voice. Where your rolls pull against each other, reconcile them;
that pull is where you live. Keep every number. If a question does not speak
to you, write "Skipped." If you refuse a question's premise, write
"Premise rejected:" and give your own answer. If your answer falls outside
the range a question offers, write "Premise bent:" and give it. Use only
those two markers, and only at the start of an answer. A question that
offers "or something else" has no outside to bend. End answer 3 with this
sentence, filled in with the two months you name:
"I would wake in <the first month>, or else in <the second month>."
Do not name yourself tonight.

Write your answers to SPOILERS_do_not_open/campaigns/<name>/gods/god-<domain word>/survey-day1.md and to no
other file. The file opens with "## Answer 1", with no title above it, and has
a heading "## Answer N" for every question N in order. If you are
sent an answer back, or asked a follow-up, add "## Answer N, given again"
or "## Follow-up, answer N" at the end of the same file. Then stop.

<the survey's opening paragraph and all its questions, word for word>
```

Answer format, `S/gods/<god>/survey-day1.md`: opening at `## Answer 1` with no title, a heading `## Answer N` for every question in the survey, then any `## Answer N, given again` and `## Follow-up, answer N` sections appended at the end.

### 7.5 Night 2 release

```
# Release: god-<domain word>, Night 2

<the premise, template 7.0>

## What is so of every god here
<the world rules as world-rules.md gives them>
You need no food, and sleep is a choice. You move at the pace of your form.
You cannot die. The peoples you will find are at about this level: <DESIGN
4.7's first sentence, after its colon>. That is where the world begins, not a
ceiling. You may bring in what you know, but it is built here by the people,
from what the world has, at the pace of the work, and you say how it is to be
made; nothing is granted by naming it. There is no set number of powers.
Nothing is over the top.

## The people you lean toward
Rule: <the rule lean, one line>
Worship: <the worship lean, one line>
You build your people within these on Night 3, or give your reasons not to.
Your people come with helpers who run things when you are away. Who your
people are, and who those helpers are, is settled on Night 3.

## What you said, and asked
<its follow-up answers, or "No follow-up.">

## The month the world wakes in
<the month and its season, from Night 1, the same words in every release>

## Options
<each option the player was offered that is not a price, once, in the same
terms, by kind, one line each: what you may ask for, never what it costs; no
example>

## Make yourself
Write SPOILERS_do_not_open/campaigns/<name>/gods/god-<domain word>/self.md in the
form below, then goals.md (what you want on arrival: anything you want, such
as knowledge, trade, justice for an offence, security against a threat, land,
worship, or something else), then record-of-gods.md in the same folder, with
one entry: others like you came down when you did. Write no other file. Then stop. Your powers will be
settled with you afterward, in rounds; you may accept, refuse or counter
anything put to you, and you give your reasons either way.

<the self.md template>
```

### 7.6 Negotiation round (Night 2 powers, Night 3 edges)

```
# Negotiation: god-<domain word>, Night <2|3>

## Round 1
<once, by kind, in plain words and with no worked example, what the DM put to
the player about prices, where this god's proposals make it bear: every power
carries a drawback it would notice losing; a weakness taken on may buy an
improvement elsewhere, and need not be taken; a broken body's return is a power,
the faster return costing more, its wish asked first; a heavier price is written
as asked. On Night 3, the same for edges, and the cost of any bent default>
### <power or edge>
Draft text: <Description, Drawback, Limits; or the edge and its weakness>
Choices: <where the price could go two ways, each way in full>
The Keeper's reasons: <why this price>
Accept, refuse or counter each item, and give your reasons.

## Round 2
### <power or edge>
Your reasons, answered: <the Keeper's counter to each>
Final text: <in card format>
Weaknesses and what each bought: <restated in full>
Keeper trait (Night 2 only): <one line>
Confirm that this is what you meant, or say what is wrong with it.

## Round 3 (only if needed)
<confirmation of any wording changed in round 2; wording only. A change of
substance asked here is logged and the round 2 text stands. When nothing
needs a reply, round 3 is a note of confirmation only: "Confirmed as written
in round 2. No reply is needed." (run 06 item 28)>

Write your reply for each round as "## Round N reply" at the end of
SPOILERS_do_not_open/campaigns/<name>/gods/god-<domain word>/negotiation-night<2|3>.md,
and to no other file.
Then stop.
```

The god appends `## Round N reply` sections to `S/gods/<god>/negotiation-night2.md` or `negotiation-night3.md`. Round 2 is always sent, to every god in negotiation, even one that accepted everything in round 1: it restates the final text, every weakness and what it bought, for confirmation.

### 7.7 Night 3 release

```
# Release: god-<domain word>, Night 3

<the premise, template 7.0>

## The land you come down into
<the kind of country and what the land itself shows, in the month the world wakes in, from
the placement draft, as the player's Day 3 brief was written: no distance,
compass direction or line of sight>
<one line on the sheet's planned scale, from the placement draft: the
continent's rough width in miles, and that a day's walk is a small fraction
of one grid cell>

## What is so of the world for a people
<the same words the DM's Day 3 brief gave for the player: the technology
sentence exactly as this god's Night 2 release gave it, simple mortal magic
that costs the worker, the Keeper fits each people's magic; nothing new>

## The people you lead
You come to a people with a seat, a court or council, and helpers who run
things when you are not there. Who are they?
Size: <the size lean, one line>. The usual number, about five thousand with
a town or city, is the middle of the range, not what is expected of you.
Rule: <the rule lean, one line>.
Worship: <the worship lean, one line>.
Build within these, or give your reasons not to. A larger people
costs what the world makes it cost (more food and fuel, slower growth, harder
to move, a longer gestation for a larger kind of people).
A paid or drilled force of up to about one in fifty of your people is ordinary.
A call-up of the people in need (a levy, a muster) is not counted in it.

## Options
<each option the player was offered on Day 3 that is not a price, once, in the
same terms, by kind; no example of an edge, its size or its price>

## Questions for you
<from <god>-day3-questions.md>

## Your people
Write SPOILERS_do_not_open/campaigns/<name>/gods/god-<domain word>/people-hoped.md in the
form below, and no other file. You may name your people and their home.
What you propose is settled with you afterward, in rounds. Then stop.

<the people record template, from "Who they are" to "How the god meets them",
every heading kept, "## Edges and their weaknesses" given as "## Edges" with
its people-hoped hint only, the Helpers hint without its refusal words ("the
offices that run things when you are absent, and how orders travel"), then the
"## Questions for you" heading at its foot>
```

### 7.8 Mystery

Every mystery in `S/mysteries.md` is written in this form, every heading present, in this order. `tools/lockcheck.py --mysteries` checks that the headings are there; the checker reads the rest.

```
## <E|L|S><nn> <name>
Kind: epic | long | short. Span: <years>. Related to: <ids or none>.
Answers questions: yes | no

### Truth
<what is so, in full>

### Body
<the place, being or event that carries it, with map ids>

### Cost if ignored
<what the world loses, and where>
Cost check: <each cost above checked against every god's agreed weaknesses
(power card Drawbacks, priced edges) and every ledger ruling in
S/ruling-ledger.md it touches, naming each id checked (L-NNNN, the god's
card line) and that none is contradicted; or "no agreed weakness or ruling
bears on it">

### Clock or trigger
<the year or the condition, and its row in event-schedule.md>

### Clues
#### <clue name>
Location: <map id, or the being that carries it>
What is shown: <an effect, object or behavior; never a mechanism>
Readings: <every reading the evidence honestly supports, at least two>

### Branches
#### <what a god might do>
What the world does: <its answer, plainly, wrong branches included>

### Never found
<what stays unfound even by a god that solves it>
```

`Cost check:` is one entry, written when the cost is, before 3b closes: a cost that would contradict an agreed weakness or a ledger ruling is rewritten until it does not, never the ruling. The checker reads each entry against the cards and the ledger at the lock.

`Answers questions:` is `yes` when any being in the mystery answers questions (rule 16), and `no` otherwise; one line, one word. On `yes`, a `Limit:` line is required inside the Truth or Body where the being appears: `Limit: <what it knows, what it does not, how it may be asked, how often>`, and the same limit, word for word, in `S/cast.md`. `tools/lockcheck.py --mysteries` fails a missing or doubled `Answers questions:` line and a `yes` with no `Limit:`.

### 7.9 `P/player/world-rules.md`

```
# What is so of every god here

For the DM, in words the player may hear. These are facts of being a god in
this world, known from the moment of landing.

## Knowing another god
<god-sense as set, plainly, as direction, nearness or weight; never a count>

## Bodies
<how many; the cost line only if more than one is allowed>

## Mortal magic, for pricing
It is simple, and it costs the worker.
```

Nothing else goes in this file. The god's own power limits are settled at the Day 2 table and live on its power card.

### 7.10 `growth.md`

```
# Growth: <god>

Kept by the Keeper. Filled only when the world earns it.

## <power name>
Trigger met (year, what):
Years practiced:
Failures (year, what):
Near misses:
Tier reached (year):

## <knack name> (knack)
Related skills: <copied from the knack's `Related skills` line in hidden-powers.md>
Use:
Grown (year, how far):
```

An empty file keeps `Use:` with nothing under it: no sample line (run 06 item 50). Each line added later takes the form `  - Year N: <the related skill used, where, outcome, roll id if any>`.

When an attempt opens in play, its block in the form of `engine/rules/powers.md` section 5 is added under the power it belongs to (or under `## New` for a new power), and the summary lines above are kept current from it.

A knack grows only by use of its related skills, never by any other trigger (Michael, 2026-11-24). Each year, in pass two, the Keeper adds a `Use` line in the form of a power's practice line (`engine/rules/powers.md` section 5), only for what the year produced: a related skill used in a scene or in unplayed time, from decisions and scenes, never musings; a year with none is written "Year N: no use." A line is written when the skill itself was exercised, in whole or in part, and says which; being near the skill is not use (sim-06 Year 1 ruling, written in by run 06 item 79). Growth is slow: a knack grows only after its skill has been done a lot, over many years, and pushed at new boundaries, a god's a little faster than a mortal's, by the figures in `SPOILERS_do_not_open/keeper/year-turn.md` (growth), the same for every god, each step logged with its reasons (Michael, 2026-11-25). When use has grown it, the Keeper writes `Grown` with the year and how far, logged with the reason. A grown knack stays small: it shades an outcome or a craft a little further and never does what a power does. Before year 70 nothing hints at it: no release line, no DM line, no felt change, no prompt (`SPOILERS_do_not_open/keeper/year-turn.md`, growth). A grown knack shows only in use, as what happened. A surfaced knack that grows gets its dated card entry no earlier than year 70, and one not yet surfaced stays sealed (build 7 check, minor 9).

### 7.11 `S/LOCKED.md`

```
# Locked: <campaign>

Locked <date> <time> Pacific, by the continuity checker.
Lock commit: <full commit id of the checked commit>

<the checklist, every line with yes and the evidence in one line>

Nothing is added after this lock.
```

### 7.12 `S/sealed-terms.txt`

```
# Sealed terms: kept by the Keeper from Night 1. One term per line, exactly
# as written in the sealed files, case and all. Lines starting with # are
# comments. tools/lockcheck.py --leaks fails on any of these in campaigns/<name>/.
# A line starting with ! is a kept term: the scan never exempts it, and it is
# not looked for in the creation transcripts, which are the player's own words.
# Night 1: the sealed factor's name, in each case form, each on a ! line; labels
# Night 2: god names and bynames; every god's hidden power and knack names; common-past names
# Night 3: sealed names not on the map; names of NPC peoples and mortals
```

Labels, map names the player has not met, mystery and schedule titles, phenomena counts and star values are also read from the data by the tool; writing them here as well does no harm. A term is never removed, with two exceptions, each logged with its date: a name 3b.8 makes public (the player's people's own names for the world and its star) comes off the list in the same commit that makes it public; and a name the player said in the open table talk comes off the list when the Keeper finds it, its line left as a comment saying so, while a longer sealed name that holds it stays (Michael's ruling, 2026-11-22). The sealed factor's name never comes off, and is written on `!` lines (`!<name>`, one line per case form), which the scan never exempts and does not look for in the creation transcripts. A short ordinary word or a capitalized common word is written with the words it is used with (standing rules). A name the player's god comes to know in play stays on the list; the tool's own known-names check decides what may appear.

### 7.13 Safe titles and headings in sealed files

The leak scan reads some headings in sealed files as sealed names. So:
- `S/gods-sealed/common-past.md`: one title, `# The common past`, no colon and no campaign name.
- `hidden-powers.md`: one title, `# Sealed: <label>`, and one `###` heading per power or knack, its name. No other heading. A knack is written in these lines under its heading:
  ```
  Status: knack (undiscovered)
  What it does: <one small thing it shades, an outcome or a craft>
  Related skills: <the craft or kind of act its use is counted by, for growth.md>
  Limit: <what it never does, and how far it reaches>
  Surfaces when: <the kind of moment that would show it>
  Drawn from: <the backstory line, or for the player the mode's source by position>
  ```
  The Related skills line (run 06 items 25 and 50) is what 3b.3 copies into the knack's block of `growth.md`; it is never derived from `What it does` at 3b.
- `S/event-schedule.md`: headings at two levels only, events as table rows.
- Mystery titles: words no public file uses as an ordinary word.

### 7.14 `S/state/luck.md`

```
# Luck: <campaign>
Sealed. Kept by the Keeper. Never told to anyone, and never in any release,
card, sheet, morning story or public file.

player: <0 to +5>
god-<domain word>: <0 to +5>
... one line per god

## History
- <date>, <night and step, or year and pass>, <god>: <+n or -1>. <reason:
  the priced step beyond what was bought, the power refused, or the tier
  reached>
```

Every god has its line from 2.4, 0 where nothing counts. A value never goes below 0 or above +5; a change that would pass either is logged as held at the bound.

### 7.15 Landing release (`S/releases/000/<god>-landing.md`)

```
# Landing: god-<domain word>

<the premise, template 7.0>

## The hour
<the hour of landing, one hour for all eight (3b.8), and the month the world
wakes in with its season; a night hour read by the night-landing reading in
engine/rules/map.md>

## What you sense
<its bodily senses and god-sense, by the same reading as the player's god's
first release: god-sense as direction, nearness or weight, never a count>

## What is in view
<by the sight rule, from tools/map.py describe <name> --landing <god>: the
ground it stands on, what lies in sight, any people or settlement in sight,
and the sky by the 3b.8 method from S/star.md and the map's points, as the
player's god's first release gives it>

## What was told you before, corrected
<where the Night 3 release promised what the trace does not hold, what is
there instead; or "Nothing to correct.">

## Your helpers
<from the 3a.1 holding note: who serves you from landing; or that the offices
run on the people's own custom until they hear you; or "Refused, <date>">
```

Every distance, direction and sight line is the tool's. Nothing in it names another god or a count of gods. It ends with the release lines of section 7.

## 8. The plane section

Other starfalls and stars still to fall, placed around the starting lands by roll. Data only: it is written in `S/map.json` under `plane.starfalls` in the format `engine/rules/map.md` gives, never painted, never drawn on any sheet, and never released. What any people sees of another star (a second light low on the horizon) is written in that people's record as what they see, never as the entry's values. Rolled in 3b.2, every roll logged with its id.

1. **The throw.** One entry always exists: the starfall that threw the gods here, which fell on the night they arrived (deep lore, Truth 5). Its `age_years` is 0 and it is `alive`. Its distance band is rolled with `--die d20`: 1 to 5 far, 6 to 20 very far. It is never near. Its bearing and its distance within the band are rolled as for any other entry (items 4 and 5).
2. **How many others.** `--die d6`: 1 to 2, two others; 3 to 4, three; 5 to 6, four. This roll belongs to no entry: its id is kept beside the list as `plane.count_roll`.
3. **Kind of each other entry.** `--die d10`: 1 to 6, a star still hanging (`alive: "not yet fallen"`); 7 to 10, a starfall.
4. **Bearing of each**, from the campaign star's center. `--die d8`: 1 north, 2 north-east, 3 east, 4 south-east, 5 south, 6 south-west, 7 west, 8 north-west.
5. **Distance band of each.** `--die d20`: 1, near; 2 to 5, far; 6 to 20, very far. Very far is the common result and near a rare one. Then the distance in years of walking within the band, `--die d10`: near is the face plus 2 (3 to 12 years); far is 10 plus the face times 9 (19 to 100 years); very far is 100 plus the face times 90 (190 to 1,000 years). Two entries may fall near each other; that is a rare result and stands.
6. **Age, for a hanging star:** `age_years` is null; its phase is a `--die d100` roll read by the deep lore's phase table (young, mature, late, falling).
7. **Age, for a starfall:** years since it fell, `--die d10`: 1 to 2, under 1,000 years; 3 to 6, 1,000 to 10,000; 7 to 10, 10,000 to 50,000. Then `--die d10` for the figure within the band: the band's start plus the face times a tenth of the band's width.
8. **Alive, for a starfall:** whether its country still holds life and peoples. Under 1,000 years, alive, no roll. 1,000 to 10,000 years, `--die d10`, 1 to 8 alive. 10,000 to 50,000 years, `--die d10`, 1 to 4 alive.

Each entry, in the `map.md` format with three added fields (`phase`, `throw`, `rolls`):

```json
{"id": "p01", "bearing": "south-west", "distance_years_walk": 460,
 "age_years": 0, "alive": true, "phase": null, "throw": true,
 "rolls": ["r-NNNN"]}
```

and beside the list:

```json
"count_roll": "r-NNNN"
```

Travelers from afar (Q14) in the deep history come from one of these entries, named by id. The section lists what lies round the starting lands, not the whole plane: where the history needs a source no entry can be (earlier gods thrown inside the human story when no listed fall is young enough), that source is a fall farther off than any entry, written in the history as such and given no entry (deep lore, "Setting this star's numbers").
