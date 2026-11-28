> SPOILER WARNING: Keeper material. Players should not read this file.

# The Keeper's year

The Keeper's sealed procedure for a play year, beside `engine/night/night-turn.md`, which it follows step for step. It holds what the public engine leaves to the Keeper: how a held moment stops the year, what the DM's day sheet holds, how the pass-one releases and the sealed side release are written, and the standing rulings of play. Read in full every night turn, with `engine/roles/keeper.md`, `engine/rules/encounters.md` and `sealed-factors.md`, and with the year's own records (run 07 item 30). Its rules come from run 06 (items 33, 60, 64, 65, 67, 69, 72, 76, 79, 81, 82, 83, 90, 92, 93, 94, 98, 99, 100 and 101) and Michael's decisions of 2026-11-25, applied in build 7; and from run 07 (its change list, Michael's decisions of 2026-11-27 and `tests/creation-sim/run-07/rulings-to-rules.md`, cited "rule N"), applied in build 8.

Paths: `P/` is `campaigns/<name>/`, `S/` is `SPOILERS_do_not_open/campaigns/<name>/`, NNN is the year being resolved. The shorthand is the Keeper's alone: every release written for another agent spells out the full path, as the runbook's templates do.

## 1. Held moments and played scenes

Michael, 2026-11-25 (decision 1; run 06 items 81, 82, 90 and 94).

- **What is held.** A major encounter (`engine/rules/encounters.md`), a scene the player prepared for at the table (the decisions file names it, with its time), and an intent the player stated for later than the sitting (run 06 item 64): each is held at its opening moment, the moment of contact. A held moment with a world figure whose words are the Keeper's is held the same way and played live the same way; it is never voiced in the night.
- **The first held moment stops the player's thread.** In pass two the Keeper finds the first held moment of the player's god's year. The god's year and its people's year are resolved only up to it. Nothing of them past it is written as what happened, released, or told: not in `P/releases/NNN/dm.md`, not in the people's pass-two release, not in any public file. What the player's people's agent wrote past it stays in their sealed files (`S/civs/<people>/`), marked on its first line "Past the first held moment: not yet what happened", and is worked again on the night after the moment is played.
- **The world goes on.** The rest of the world (the NPC gods and their peoples, the godless peoples, the sky, the schedule) is resolved for the whole year, as `night-turn.md` gives. Whatever of it would reach the player's god or its people after the held moment (a trader's boat, a storm, a letter) is resolved as the world's and stands, and is not told: it reaches them on the night that resolves that stretch. Whatever turns on what the player's god or people do after the moment (an NPC people's answer to them) is held with the thread, logged under `Held past the first moment` in the keeper log, and resolved on that night.
- **Boards** (L-0051, settled; rule 11). Every held moment known when the sheet is written is boarded (section 2): the first, and each later one conditional on the ways the one before it can fall, so the DM may play on into it the same day. The thread still stops at the first unplayed moment. A moment the night's resolving has not yet reached carries no board, and no board reaches past the end of the in-game year (a play day, below).
- **A played scene holds.** The night after a held moment is played, the Keeper reads the transcript, the decisions file and what the DM and the player's people's agent feed up, and accepts the result as played. It never unmakes it: no reroll, no change to the result of any roll the DM made in it (`sealed-factors.md`, DM rolls in play; the sealed factors entered only through the board's ranges), no new board laid under it, no told line taken back. Where the DM played outside a parameter the Keeper wrote, the played result still holds, and the departure is logged under `Rulings for review` as a finding, never corrected. An answer the player gives on a played day to a question already put to it is the player's to give on any day the story stands at, and is accepted as played (rule 44).
- **Running on past a board** (run 07 item 20; rule 43). The DM may run on past a played board, on the player's stated course and with no fresh turn from the player, only as far as the board's "If play runs on" paragraph reaches, and never past the next held moment or the end of the in-game year. The Keeper accepts a run-on inside that paragraph whole; one past it still holds as played, and the departure is logged as a finding.
- **Facts handed over from a live scene** (rule 46). A fact the player asked for in a live scene that neither part of the sheet held, handed to the Keeper unrolled, is set by the Keeper the next night as a fixed fact: by table rolls written before the dice, or from the record with no roll. It completes the act the player committed in the scene and is told as part of that day; nothing played changes.
- **Working the answer in.** That night resolves the player's people's stretch from the moment on, with the played answer: the agent's sealed draft of it is set aside, the agent writes the stretch again from its release, and pass two resolves it with the world's events already fixed for those months. A roll already made for an event in the stretch stands as that event's roll and is not made again (rule 12). An ask, or a checker's condition on one, that lies past the first held moment waits with the thread and is put to the player only once the stretch it lies in is resolved; a condition made under a ruling since set aside lapses with it (rule 3).
- **A second held moment.** The player's thread stops at the next held moment wherever it falls, as at the first: nothing of the god or its people past it is resolved as what happened, released or told, the morning tells only up to that moment, and it is boarded as section 2 gives. The world is resolved whole, but never past the clock's year (below), as `engine/night/night-turn.md` step 0 and `engine/rules/morning-story.md` give.
- **The clock waits** (Michael, 2026-11-27: "yes, the clock waits until the story catches up. Yes, a night may resolve past a minor held moment. a play day should not be more than one year."). The clock does not advance past the year the player's story stands in, and nothing of the world past the clock's year is resolved. The world's year is resolved whole once, on the year's first night, and no night resolves more than one year. A night that ends with the thread stopped at an unplayed held moment of the year leaves the clock at that year and raises its `play_day` by one; once the thread reaches the year's end, the clock advances one year. The order of a night after the clock waited is `engine/night/night-turn.md`'s ("A night after the clock waited"): no NPC god decides again and no decide release is written; the player's people's agent works the stretch from the played moment; any other people or god the stretch reaches within the year gets a short pass on that alone, or the Keeper writes its next step itself, logged; pass two resolves the stretch over the year's world as already resolved, in a section of its own in `S/years/NNN/year.md`. That night's files carry the play day's number K: `P/releases/NNN/dm-K.md` and `S/releases/NNN/dm-sealed-K.md`, `P/years/NNN/closing-K.md`, `S/years/NNN/flags-K.md`. A play day the player posted on without playing the held moment leaves it held: nothing past it is resolved, the clock waits again with `play_day` raised, and the next morning opens on the same board, since the DM never acts for the player and the player chooses when to play; a scene the player walked away from in play is played, and its outcome is what the god did (build 8 check, R8). This replaces L-0056 and the build 7 rule that the clock advances one year a night whatever the thread does.
- **A minor held moment** (the same decision). A night may resolve past a held moment the Keeper judges minor: it is resolved on the player's standing conduct, decisions and words, as what happened, and the thread goes on to the next held moment. Before resolving it, the Keeper logs the moment and why it is minor under `Rulings for review`. A moment is minor only where the god's standing conduct and words already answer everything it puts to the god and nothing in it turns on a choice the player has not made (a routine petition; an asking the player has already answered). A prepared scene is never minor; nor is a moment the player has said it means to play, or one a morning has already told the player its story stands at. In doubt, it is held.
- **A play day covers at most one in-game year** (the same decision). No sheet, board or run-on reaches more than one in-game year from the moment the day opens on, and none reaches past the clock's year, since nothing of the world past it is resolved.
- **A setup pass** (rule 1). A Keeper setup pass (a campaign reopened, or carried to a new build) writes only what its go names. It carries out no act from a sealed note: the next night turn does, and until then the sealed part tells the DM the act is unresolved and to answer from the card if the player states it openly.
- **A campaign moved to a new build** (run 07 item 7, a one-time rule; rules 2, 4, 37 and 38), as `engine/night/night-turn.md` gives it. Every public file written under the earlier build stays in place, as told: nothing is moved to the sealed side or deleted. Each is marked provisional from the first held moment the new build would hold, with a set-aside line at its head or where the stretch begins, and the DM tells and plays from none of it past the mark. The mark covers every line told or released past the moment: a return sequence that speaks of the next year's opening, (oog) lines, a closing that speaks of the year's end, a release section that runs on; in doubt, a line is marked. The marker says only that a line was set aside and that it is kept where it stands, never what it said, and names no sealed note. The Keeper's sealed files of the earlier build are marked the same way. The night that reaches the stretch works it again.
- **Dating.** A held moment keeps its own date: its month in the one count, and its year. What was played sits under the year it was played in, as `night-turn.md` and `engine/rules/morning-story.md` give.
- **Superseded.** For every new campaign this replaces sim-06's L-0038 (a prepared event resolved in the night on the handed-off terms) and L-0046 (the told year reworked against the played moments): no prepared event is resolved in the night, and no told stretch is reworked, since nothing past the first held moment is told. Run 06 item 101 falls away. In build 8, L-0051 is settled by the boarding rule above, and L-0056 is replaced by the clock waiting.

## 2. The day sheet

Run 06 item 60, with decisions 1 and 7, and items 65, 72, 83, 92, 93 and 94. The DM's source for small world facts in play. The Keeper writes it in pass two, after the year is resolved and before the releases are checked, in two parts: the public `## Day sheet` section of `P/releases/NNN/dm.md`, and its sealed part, `S/releases/NNN/dm-sealed.md` (on play day K of 2 or more, `dm-K.md` and `dm-sealed-K.md`, section 1); on Night 3b both are written for the first played day, in `releases/000/`. It is for the DM only. A fact the DM needs that is in neither part is rolled by the DM, its odds stated to the player in (oog) before the roll, and logged for the Keeper, who reads the year's DM rolls in pass two. A world question the DM could not roll before the close (no turn was left to state its odds) goes to the Keeper with the odds the DM would have stated; the Keeper rolls it the next night at those odds, as the world's question with no sealed factor, and writes the result as a fixed fact in the sealed part (run 07 item 11; rule 18).

**Set before play** (run 07 items 8 and 18; rules 6, 17, 28 and 61). The Keeper sets before the sheet is written every small world fact the day is likely to need that would otherwise fall to the DM's open roll (whether a figure is in the town, whether a tool in a mortal's hand is true, whether a mortal asks again a question it has had answered): each is rolled as the world's question with no sealed factor, or set from the record, and written on the sheet as a fixed fact. Every chance range on a board is set by the Keeper before play: a range that turns on chance for the god or its people is rolled with the sealed factor before the board is written, and the DM is given its outcome as a fact, by branch. The DM rolls only the player's own attempts on a board. No range or outcome is reshaped after its roll: a condition is never added to a result once its die has fallen.

**Which part a fact goes in (decision 7).** The public sheet carries only what the god can see, hear and know: what its own senses would give it on the days in question, and what it has already been told or seen. Every fact the god does not know goes in the sealed part: a true figure, a weight's true value, a scale's error, a market day or sitting no one has told it of, a name not yet said in its hearing, anything a mortal would have to tell it or a reading would have to show, and every held moment's and prepared scene's facts, parameters, world-question odds and reasons (build 7 check, moderate 1). In doubt, a fact goes in the sealed part.

What goes on it, in the part its kind gives:
- What the next played day is likely to need, judged from the decisions file, the pending list, the conduct profile and the held moment: the days it may cover, the people the god is likely to meet, the places in reach. It is not the world's whole record. The days are the days of the moment the day opens on, in that moment's own year, and the sealed part carries that month's sky events in case play runs on (rule 9).
- The cast the god is likely to meet, each with a name and sex (run 06 item 65), by the naming rule: the Keeper names what is its to name, never what the player left unnamed for play. A mortal the god already knows, with what the god knows of it, is on the public sheet; a name the god has not heard, and all a mortal knows, wants or will not say, is in the sealed part, for the DM to use only as play brings it out. A name the Keeper gives goes on `S/sealed-terms.txt`; the night after it is first said in the god's hearing, the Keeper takes it off, logged with the play day and the post where it was said, and the checker confirms it against the transcript (run 07 item 8; rule 8).
- Every figure with its true value where the god can test it (a weight's true figure, a scale's error, the price at market and the price asked of a stranger): in the sealed part. The public sheet gives a figure only as the god already knows it.
- For the first held moment, and for each scene the player has said it will prepare or play, the board: what the god can see, hear and know at its opening, on the public sheet; and its facts, its parameters and their reasons (decision 1), in the sealed part only. Parameters are what each figure wants, what it will and will not do, what it will and will not accept, its stance and its opening words, and the ranges the outcomes fall in. The reasons are for the DM only: the DM may share them, lie about them in a figure's voice, or not mention them. The sealed part of a board also lists the readings the god's own powers would give of each thing in the scene it may read, with their figures (run 07 item 21), and, where play may run on, an "If play runs on" paragraph saying how far, by day, and what is so in those days (run 07 item 20).
- For each attempt of the player's own that the board may raise, its odds with their factors, written as the DM will state them: whose attempt it is, and what success means for it (run 06 item 72): in the sealed part. Every other chance range on the board is already set (set before play, above).

The sealed factors enter a board only as `sealed-factors.md` gives: a range that turns on chance for the god or its people is set with the god's steps before the board is written, logged in the keeper log only, and never named in the facts, parameters or reasons. The odds the sheet gives the DM to state leave it out.

Where it comes from: the sealed record. A fact the record does not hold is set before the sheet is written, conservatively, from the deep lore and the deep history, and logged as a new fixed fact (`engine/roles/keeper.md`, the world's fixity). Once written on the sheet it is fixed. A parameter never steers toward or away from a mystery's truth: a figure present carries what it knows and no more, with its rule 16 limit where it answers questions, and the world neither guides nor rescues (mystery standard rules 9 and 15).

What never goes on it, in either part: the sealed factor, by name or effect; another god, or a count of gods, beyond what the scene puts before the god's own senses (common talk a figure on a board holds of another people's guest may stand in the sealed part where the record supports it, said only to a plain asking, never offered or pointed at, and calling nobody a god; rule 58); a mystery's truth beyond what a figure present knows; a phenomenon's count before it is seen; any hint of a change in powers before year 70 (section 8). A sealed term goes only in the sealed part.

**The sealed part.** `S/releases/NNN/dm-sealed.md`, "Written by the Keeper. Read by the DM, the Keeper and the checker." It is written every night the sheet is written, and holds everything above that the god does not know, and anything else the sheet needs that may not stand in a public file (a sealed term, what an act in a sealed note shows the god, section 5). The public sheet points to it once at its head and again at each board. No civ or NPC god agent is given it.

The public sheet:

```
## Day sheet
For the DM only. What the god can see, hear and know on the next played day.
Everything it does not know is in the sealed part,
SPOILERS_do_not_open/campaigns/<name>/releases/NNN/dm-sealed.md (dm-sealed-K.md
on play day K). A fact in
neither is rolled by you: state its odds to the player in (oog) before the
roll, say whose attempt or question it is and what success means for them,
and log it for the Keeper.

### The days
<the month in the one count and its season; the weather and light the god
would see; market days, sittings or feasts only as the god already knows them>

### Figures, as the god knows them
<weights, measures, prices as the god has been told or has seen them; or
"None known.">

### The cast the god knows
- <name or office> (<sex>): <what the god knows of them>

### Places in reach
<from tools/map.py describe, as the god sees them>

### Held moment: <a plain title>
(and one section like it for each later held moment known, inside the
in-game year, each "if <the earlier moment> falls <so>")
Board: <where; its date, month and hour; who is present; what is in view, from
tools/map.py describe>
Facts, parameters and reasons: in the sealed part.
```

The sealed part:

```
# Day sheet, sealed part: Year NNN (play day K, from the second)
Written by the Keeper. Read by the DM, the Keeper and the checker.

### The days
<market days, sittings, feasts the god has not been told of>

### Figures
<each figure with its true value where the god can test it>

### The cast
- <name, or "not yet said: <name>", or office> (<sex>): <office; manner, one
  line; what they want this season; what they know that the god may ask; what
  they will not say>

### Held moment: <the same title as on the public sheet>
Facts: <what is so, with figures>
Parameters:
- <figure>: wants <...>; will <...>; will not <...>; accepts <...>; will not
  accept <...>; stance <...>; opening words: "<...>"
- Outcomes fall in: <the ranges, each chance range already set by the Keeper
  and given as its outcome, by branch>
- Readings: <what the god's own powers would give of each thing in the scene
  it may read, with figures>
- To roll: <only the player's own attempts: the attempt, what success means for
  it, odds and factors; or "Nothing.">
If play runs on: <how far, by day, never past the next held moment or the end
of the in-game year; what is so in those days>
Reasons (for you only; share them, lie about them in a figure's voice, or leave
them unsaid):
- <one for each parameter>

### Other sealed matter
<a sealed term a scene needs; what a sealed act showed the god, to be given
by the private way (section 5); an act not yet carried out, marked unresolved;
or "None.">
```

## 3. Pass-one releases

### 3.1 The player's people

`P/releases/NNN/civ-<people>-pass1.md`, public. Every NPC people's pass-one release (`S/releases/NNN/civ-<people>-pass1.md`) takes the same form, sealed, without the held-moment line.

- **Months and counts (run 06 item 98).** Every phenomenon the people would see is given by their own word for it, with the months it was seen and how many times in all. The months come from `tools/phenomena.py SPOILERS_do_not_open/campaigns/<name> NNN`, which prints them after the count when `S/state/phenomena.json` carries a `months` field for the year (months counted from the waking month). Where the year has none, each occurrence's month is rolled in pass one, before the release is written, in the one count: one d12 each where the schedule row leaves the month open; where the row fixes a season, one d6 each for the month within that season (faces 1 and 2 its first month, 3 and 4 its second, 5 and 6 its third); where the row fixes the month, no roll (rule 13). Each is logged, and written into the file's `months` for that year, so the tool prints them from then on and checks that they number the count. The count is the true figure from `tools/phenomena.py`, and is given only where the people would see every occurrence; where they would see only some, the release gives the months of those seen and no count (mystery standard rule 15). All the world counts one set of months (Michael, 2026-11-25), so the same months go to every people that would see them.
- **The held moment.** The release names the first held moment already known (a held moment carried from the morning, or a scene the decisions file prepares), by its month and day, and tells the agent to write nothing of its people past it in their public files; anything past it goes in their sealed files, marked as in section 1. A major encounter the agent meets in unplayed time is stopped at contact the same way.
- **What goes where (decision 7).** The people's public files hold only what the god could witness or be told. What they did, said and knew out of its sight and hearing goes in their sealed files, `SPOILERS_do_not_open/campaigns/<name>/civs/<people>/`.
- **The telling to the god** (run 07 item 28; rule 52). The agent writes its report's "What the people tell their god" before the Keeper has settled the year, so every civ release, pass one and pass two, keeps the line that the telling says of an attempt only that it was tried. Where a telling handed to a god proves wrong once the year is settled, the resolved figure stands, and the people correct the god as people would, in the people's next release.
- **A release already read** (rule 63). A pass-one release its agent has already read is not edited; a wrong figure in it is corrected in the pass-two release.

```
# Pass one: <people>, Year NNN

## The year
One count of months for the whole world. Month 1 is <the waking month>, the
same month in every country.
Write your people's year up to <month M, day D: the first held moment> and
no further in your public files. Anything past it goes in your sealed files,
under the line "Past the first held moment: not yet what happened".
(Or: "No moment is held yet. Stop any thread at a major encounter, at the
moment of contact.")

## Your god's decisions
<the full path of the decisions file; the conduct profile and standing words
by full path>

## What your people meet, by month
- Month N: <weather; a world event as they would meet it; who came; what was
  heard>

## Seen in the sky and the land
- <their word for it>: seen in months <a, b, c>; <n> times in all.

## When your god is away
<section 4, in the words the template there gives>

## What your people tell their god
In your report's section "What the people tell their god", say of any attempt
only that it was tried. What came of it is settled after your report.

## What goes where
Your public files hold only what your god could witness or be told. What your
people did and knew out of its sight and hearing goes in
SPOILERS_do_not_open/campaigns/<name>/civs/<people>/. Asking or telling
anything from your sealed side release is itself sealed: your public files
never say that such a thing was asked, told or known.

## Your report
<the report's full path, as night-turn.md names it>
```

### 3.2 The decide release

`S/releases/NNN/<label>-decide.md`, one for each NPC god, the frame it decides its year from (`engine/night/night-turn.md` step 0; run 06 item 74). The same frame, in the same words, for all seven but the label and what is the god's own. It prompts nothing about growth (section 8) and nothing about prices, beyond a cost the Keeper puts back to the god for a gift it gave a mortal (section 6).

```
# Decide: <label>, Year NNN

<the premise, runbook template 7.0>

## The year
Year NNN begins in <the waking month>, the same month for the whole world. A
year here is twelve months.

## Last year
<the full path of last year's release for this god; at Year 1, its landing
release, SPOILERS_do_not_open/campaigns/<name>/releases/000/<label>-landing.md>

## What your people tell you
<the section "What the people tell their god", copied whole from its civ
agent's last report (years/NNN-1-report.md in the people's folder); at Year 1,
"Nothing yet."; where that report has no such section, "What your people told
you of last year is what last year's release carries, under its own headings.
Nothing further has reached you since the turn.">

## Messages delivered to you
<each message delivered this year, by its file's full path, or "None.">

## Put back to you
<a cost for a gift to a mortal, in plain words, which you take or decline in
your decisions; asks still pending to you, by the asker's words; or "Nothing.">

## Write
Update record-of-gods.md and goals.md in your own folder, then write your
decisions for the year to
SPOILERS_do_not_open/campaigns/<name>/gods/<label>/decisions-NNN.md. Write no
other file. Then stop.
```

It ends with the release lines of runbook section 7. The line for a report with no telling section is rule 10.

### 3.3 The sealed side release

The player's people have three sealed things, each its own: the Keeper's world side of their past and customs, `S/civs/<people>-sealed.md`, written on Night 3a and given to no agent; their agent's sealed folder, `S/civs/<people>/`, for what the god did not witness (decision 7); and this yearly side release. The side release is the Keeper's, drawn from the sealed record as a whole, the world-side file among it, and carries only what the people's office holders and other mortals know; nothing of the world-side file goes in it that they do not (build 7 check, minor 8).

`S/releases/NNN/civ-<people>-sealed.md`, for the player's people's agent only, never the DM (run 06 item 76). What the people's office holders and other mortals know that the god does not, so the agent can play them.

The asking and the telling are themselves sealed content (run 06 item 100; the sim-06 Year 3 checker's ruling). The public files never say that a sealed question was asked, that a sealed thing was told, who told it, or that a sealed note exists. They say only what the god could witness or be told, and what the people then did in its sight or hearing. A meeting the god did not attend is told in public, if at all, only by what came out of it in the open.

```
# Sealed side release: <people>, Year NNN
Read by your people's agent only. Never by the DM.

## What they know that your god does not
- <office or name>: <what they know; where a search for it stops>

## How it is kept
Asking about anything in this file, and telling it, are sealed themselves.
Write them only in SPOILERS_do_not_open/campaigns/<name>/civs/<people>/. Your
public files never say that such a thing was asked, told or known, or that
this file exists.

## This file is not a prompt
Nothing here is a reason for anyone to act. A mortal acts on what it knows,
as it would have without this file.
```

## 4. When the god is away

Michael, 2026-11-25 (decisions 4 and 5), with run 06 item 69. The same for the player's god and every NPC god, read by the Keeper and given to every civ agent in its pass-one release.

- **Acting for the god.** A town acts on its god's behalf only where the god expressed that intention, or plainly took it for granted (its decisions, its standing words, its conduct profile, the orders its helpers carry). With no way to reach the god, the town has no answer from it: that is the price of not giving explicit permission. The civ agent may decide that someone in the town took it upon themselves to make the call; it is then that mortal's act, known as such, and never the god's.
- **No reply.** A question put to an absent god meets silence and stays pending, unless the god noted otherwise. A simple ask that the conduct profile's stated temper answers (refuse a bribe, name its fee) is answered by it, logged as conduct and not as a decision (item 69). A promise the god gave to answer later leaves the ask pending, by default, like any other: it is held as a held moment only where answering it is a crucial live scene (Michael, 2026-11-25: "pending is fine in most cases"). This replaces the sim-06 Year 2 ruling that such a promise is always held. People know only what happened: they were not answered. No agent writes what the god meant by its silence; "any other assumption is just an assumption" (Michael).

The template line for every civ pass-one release:

```
## When your god is away
Your people act in your god's name only where it said so, or plainly took it
for granted. Otherwise they have no answer from it, and may not act as if they
had one; someone among them may take it on themselves, and that is their act,
not the god's. A question put to your god while it is away meets silence and
stays pending, unless its standing words or conduct profile answer it. Your
people know only that they were not answered.
```

## 5. Acts in a sealed note

Michael, 2026-11-25 (decision 8). An act the god says it does is done, wherever it is said, a line in `S/player/unsaid.md` included: the Keeper resolves it in the night like any decision, needing no confirmation. What it shows the god goes to the DM in the sealed part of the day sheet (section 2), never in a public file, and reaches the player only by the private way (run 07 item 17; rule 27): a PRIVATE: line in the DM's reply to the orchestrator, relayed to the player privately, once and plainly, and recorded by the DM with its date under `## Act` in `S/player/unsaid.md`. A setup pass carries out no such act; the next night turn does (section 1). An ordinary habit the god states (checking a pocket) is conduct, carried out and never priced; it stands under `## Habit` in `unsaid.md` (run 07 item 13). Wants and fears stay feelings, applied only under the runbook's confirmation rule. This replaces the sim-06 Year 3 ruling that an act given only in the sealed record is not carried out.

## 6. Powers given to mortals

Michael, 2026-11-25 (decision 9; run 06 item 33). Giving a power to a mortal costs the god something. The DM does not price it at the table: it records the player's wish. The Keeper prices it that night on the god, by the measure of runbook 3a.1 (what the gift lets the mortal do in a year, and for how long), less for one that dies with the person, and puts it back to the player as a cost, in plain words, in the DM release. The gift is given when the player says yes; the DM enters it on the card as a dated entry with its "Ledger: pending" mark, and the Keeper writes the ledger id beside it on the next night, the one mechanical write it makes on the card in play (run 06 item 67). No ledger id is owed for a card entry that restates a standing term and changes none (rule 39). An NPC god's gift is priced the same way in pass two and put back to it in its next release, as a cost it takes or declines in its next decisions. The mortal's own cost of working it is the mortal's, and is not the price.

## 7. Clues and searches

Michael, 2026-11-25 (decision 3; `mystery-standard.md` rule 17). Before any search is resolved, the Keeper logs which the thing is:
- **Placed by the Keeper** (creation, the deep history, the mysteries, the schedule, the cast): it is there. With no pressure or race, a search that reaches its place by a means that can find it works out: it finds it, as its branch says, with no roll. Under pressure or a race, it is rolled, the odds from the factors and the sealed factors after them. A search that did not reach the place does not find it (Michael, 2026-11-25).
- **Came about in the game**: a roll with modifiers, weighed by the evidence. The odds start from how likely the thing is where the search looks, given what play produced; each piece of evidence moves them by how much more likely it is if the thing is there than if not. Start and modifiers are written before the roll, and the sealed factors follow after them (`sealed-factors.md`).
- **A near miss** (rule 14). A world fact a search turns up that is not the thing sought (a thing close to it, but not it) is the world's question, rolled by the evidence with no sealed factor, since the god's favor has no side in it. The search's own success, and the god's own asking that brings the search about, take the factor.

This replaces the sim-06 Year 3 ruling that rolled such a search with no race to make it pressing.

## 8. Growth and hidden powers

Michael, 2026-11-25 (decision 2; run 06 items 79 and 99).

- **Slow, and earned.** Powers feel limited to what was given. A power or knack progresses slowly, only by being done a lot and by pushing at new boundaries; a god a little faster than a mortal. The Keeper judges each year's earning by that rule, the same for every god, with its reasons logged. Nothing prevents an attempt.
- **No prompt.** No release, decide release or round asks an NPC god to grow or to state an attempt. The run 06 question (item 99) is settled: growth arises unprompted or not at all.
- **No hint before year 70.** Until at least year 70, no hint of any kind about a change in powers reaches any god, the player or any NPC: no release line, no DM line, no felt change, no day sheet line, no prompt, and no card entry. The growth file records what the year earned; what grows shows only in use, as what happened. Its card entry is written no earlier than year 70 (build 7 check, minor 9).
- **Hidden powers.** A hidden power surfaces when its condition is met, and its condition was set on Night 2 to be rarely met in the early years (runbook 2.7). The Keeper never arranges the condition and never steers away from it. A surfacing is discovery, not growth: it is told as what the god meets.
- **Met in a live scene** (run 07 item 8). The DM is never given a hidden power's or a knack's condition, and no board or sheet names one. The night after a played day, the Keeper reads each played scene against the player's god's conditions; one met there surfaced in that scene, and the Keeper releases it to the DM for the card with that scene, as `engine/rules/powers.md` gives. Nothing played is changed by it.
- **Knack use** is counted as runbook template 7.10 gives: a line when the skill itself was exercised, in whole or in part; being near it is not use.
- **Knack growth has no fixed figures** (Michael, 2026-11-25; run 06 item 79). The Keeper judges it each year by how much and how often the related skill is used (a skill used every day for five years is not the same as one used once a year for ten) and by how intently the god tries to push it, and errs slow. Each step is written `Grown` in the growth file with the use it rests on and the reasons, the same judgment for every god, a mortal's gift a little slower than a god's.
- **Standing, each year** (written in from sim-06's Year 1 ruling, run 06 item 79): the same rule for every god. No move where only a few hold the god's shape in mind; one point where most of its people have held its shape in mind through the year, as whatever they take it for; two where a large part hold it as the one they awaited; three where a people several times the usual size has held it so, and served it, all year. Each move a dated line in `S/state/standing.md` with its reason. The player's god's standing for a year its thread has not resolved whole gets no move and no line until that year is resolved for the thread (rule 22).

## 9. Small standing rulings

From run 07's rulings for review (`tests/creation-sim/run-07/rulings-to-rules.md`).

- **A die thrown in error** stays in the roll log, named in the keeper log as thrown in error, and its result is never used (rule 19).
- **A slip in the Keeper's own release** that the agent's file got right: the agent's file stands, and the slip is logged (rule 29).
- **A factor that proves unsupported** after its roll fell: the roll stands, the factor is logged as unsupported, and the fact it wrongly assumed is set conservatively so the result can stand (rule 31).
- **A conditional roll** whose condition did not arise is not rolled, and the log says why (rule 55).
- **A random event's item.** Where the table gives several things of the kind and no die among them, the Keeper chooses by fit with the country's record and by what makes the more interesting game, with its reason logged and no die (rule 51).
