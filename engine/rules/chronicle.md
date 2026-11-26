# Rules: the chronicle

The player's chronicle: what it holds, who writes each part, what may and may not appear in it, and how it condenses with age. Binding on the DM and the player's civ agent, and on the Keeper for what it releases. Sources: DESIGN.md 2.6, 5.4, 7.1, 7.9, 9.2, 9.3, 12.1 to 12.4, 12.9.

## 1. What the chronicle is

The chronicle is the player's own record of the campaign: everything their god knows, readable at any time (12.3). It is the first thing the DM reads at the start of a session and the first thing an agent opens before any full log (12.4). The player may ask for any part of it in play, and the DM gives it as the record stands, in the chronicle's own form.

It lives in `player/chronicle/`:

```
player/chronicle/
  README.md           how to read this folder, three lines
  years.md            year by year (section 3)
  canon.md            power card pointer, rulings, the people's code, settled facts
  people.md           who's who, with status
  threads.md          open and closed
  messages.md         sent and received, with fate as known
  chronicle-god.md    the DM's working draft of the god's side (not read by the player)
  chronicle-people.md the civ agent's working draft of the people's side
```

The player reads `years.md`, `canon.md`, `people.md`, `threads.md`, `messages.md`. The two working drafts are the raw material the DM assembles from.

## 2. Who writes what

- **The civ agent** writes the people's side (12.3): what the people did, produced, lost, built, feared, and what they say about their god and their kings. It writes `chronicle-people.md` each night (civ.md 6) from its own year file and `lore.md`. It writes about the people, never about the god's inner life, and it writes only what the people would tell their god or what the god could see of them.
- **The DM** writes the god's side (12.3): where the god went, what it did, saw, sensed, decided, who it met, what it was told, what it learned of other gods. It writes `chronicle-god.md` from the day's scenes, the rolling save, the decisions handed off, and the Keeper's release.
- **The DM assembles** both into the five player-facing files after each night turn (night-turn.md 6), before the morning story is finished. Assembly is the DM's job alone; the civ agent does not touch the player-facing files.
- **The Keeper** writes none of it. It releases to the DM what the god could know (12.2) and the DM writes from that. If the DM finds in assembly that the release and the chronicle disagree, the DM does not reconcile them silently: it logs the disagreement in `player/corrections.md` and tells the player in (oog), citing both (13.6).

Nothing enters the chronicle that the player did not experience in the chat or that the Keeper did not release. The chat is the first authority (2.6, 12.1): if the player points to something in the chat the chronicle lacks or contradicts, the chronicle is corrected and the correction logged with its proof.

## 3. The year-by-year record

`years.md`, newest year at the top. Each year has one block:

```
## Year NNN

Season opened: <the waking month, the same each year for the whole world, 8.1>
The god: <where it was, its condition, what it decided and did; scenes played,
one line each with a pointer to the scene in the save; what it saw and sensed;
whom it met; what it was told>
The people: <state and mood at year's end; the numbers the god would know
(population, stores, strength as reported to it); what they did; what they say>
Encounters: <minor ones in a line; major ones as scenes above>
Messages: <sent this year, received this year, each with its id>
Rulings this year: <one line each, pointer to canon.md>
Deaths of note: <with their moment, 9.3>
Map: <regions entered, charts gained, grade of knowledge>
Open at year's end: <pointer to threads.md items touched this year>
Full record: <paths to the year's save, decisions, release and morning story>
```

A year block is written the night the year closes and is the detailed form (section 6). Everything in it is in the god's own knowledge. Numbers are the numbers the god was given by its people, not the civ agent's true state; if the people misreported, the chronicle holds the misreport until the god learns better, and then both.

## 4. Canon

`canon.md` is the part of the chronicle that never condenses and is never deleted (12.4). It holds:

- **Power card.** A pointer to `player/power-card.md`, which is itself canon under `powers.md`. The chronicle does not copy it; it points.
- **Rulings.** Every ruling that touched the player, in date order: year, real date, matter, ruling, what it binds. Rulings the player has seen in play only (12.7); nothing from the sealed ledger beyond what was released.
- **The people's code.** The laws, customs and oaths the people live by as the god has set them or found them, each with the year it was set and the year it was changed if it was. Changes are added beneath, never written over.
- **Settled facts.** Things about the world the god has seen with its own senses or had confirmed beyond doubt, in the god's knowledge: the name of the river, that the salt coast god is a woman in a grey cloak, that the pass is shut in winter. A settled fact carries its source (seen, told by whom, worked out from what) and the year. A settled fact that later proves wrong is not deleted; it is marked "contradicted Year N by <what>" and the new fact added. The god's beliefs may be wrong (7.9) and the DM never corrects them (13.1, 13.6); the chronicle records what the god holds true and lets the world correct it.

Canon is the DM's to write and the player's to challenge. A challenge is an appeal under `powers.md` section 2 or a correction under 2.6.

## 5. Who's who, threads, messages

### `people.md`

Every mortal, god or being the god has met or heard named, with status: alive, dead (year and moment), missing, unknown. One block per person: name as the god knows it, who they are to the god, where last seen, what the god believes of them, and the year each belief was formed. Once a person becomes significant their nature and history are fixed (9.2); the chronicle holds the god's view of that history, which may differ from the record. Deaths the god would know reach the chronicle the year it learns them, not the year they happened, with both years noted.

Other gods have blocks here too, built only from what the god saw, was told or worked out (7.9). The block says how the god knows each thing.

### `threads.md`

Two lists, open and closed. A thread is anything begun that has not ended: a building under way, an alliance proposed, a search, a growth attempt, an enemy unanswered, a question the god asked the world. Each thread: name, year opened, what began it, its current state as the god knows it, what the god is waiting on. When a thread closes it moves to the closed list with the year and how it closed. Closed threads are never deleted.

Pending questions (12.9) are not kept here. They are the DM's `player/pending.md` and are put to the player before 1:30. A pending question that the player has answered and that leads somewhere becomes a thread.

### `messages.md`

Every message the god sent or received, by id, from `state/messages.jsonl` as the god knows it, never from the log directly (`messages.md` rules, section 6). For each: year sent or received, to or from whom, carrier, one line of content, and fate as the god knows it: "rider returned Year 5, delivered," "no word," "reply received Year 6, m-0031," "carrier found dead on the hill road Year 7." A fate the god does not know is "unknown." The DM never fills in a fate from the log.

## 6. What the chronicle may contain

Only what the god knows (12.3). This is the one hard limit, and it binds every line:

- Nothing from the sealed folder, the keeper log, the event schedule, another god's files or another civ's files.
- Nothing from the true `state/` numbers unless the god was given them by its people or saw them.
- No roll numbers. Outcomes only (12.6).
- No cause the god did not learn. If a storm sank the grain barge, the chronicle says the barge sank in a storm if the god heard that, and only that the barge did not arrive if that is all it knows.
- No sign pointed at (8.2). A strange report goes in as the report, in the words it came in, with no weight added.
- No correction of the god's beliefs by the DM (13.1). Wrong beliefs stand until the world corrects them.
- No musings as decisions (5.9). A musing may appear as "the god considered ..." only if the player asks for musings to be recorded; by default they are the DM's material for the conduct profile and not chronicle.

The checker reads the chronicle against the DM's release each night (checker.md 4). Anything in the chronicle that is not in a release or the chat is a flag.

## 7. Condensation with age

Nothing is ever deleted (12.4). The chronicle condenses so that agents and the player can read it quickly; the full logs stay where they are and every condensed line points to them.

### Tiers

- **Recent years, detailed.** The current year and the five before it keep the full block of section 3.
- **Middle years, reduced.** Years six to twenty back are reduced to a short block: season opened, three to eight key lines (what changed for the god, the people, the threads), deaths of note, messages by id, and the `Full record` pointers. The reduction is written by the DM in the night turn when a year ages out of the recent tier, and is appended beneath a line `Condensed Year NNN+6` so the reader knows when and why.
- **Old years, key lines.** Years more than twenty back are reduced to one to three lines each, plus pointers. Several uneventful old years may be grouped under one heading ("Years 12 to 15: the quiet years; the wall finished Year 13; see full records") when nothing in them is still open.

### Rules of condensation

- The detailed block is not overwritten. It is moved, whole, to `player/chronicle/full/years-NNN.md` and the reduced block in `years.md` points to it. The full file is never touched again.
- A line is kept in the reduced block if it bears on anything still open in `threads.md`, any person still alive in `people.md`, any settled fact in `canon.md`, or any message not yet `delivered` or otherwise closed in the god's knowledge. A thread reopening pulls its years back into fuller detail in a note under the thread, not by rewriting `years.md`.
- Canon never condenses (12.4): `canon.md` is the same length it was the night before plus whatever was added. `people.md` never condenses; dead people stay, with status. `threads.md` moves closed threads to the closed list and keeps them.
- `messages.md` never condenses; it is already one line per message.
- The DM announces a condensation in the morning story's (oog) notes only when the player has asked to be told; otherwise it is silent and the `Condensed` line in the file is the record.
- Agents read the condensed version first and open full logs only when needed (12.4). "Needed" means a question in play turns on a detail the condensed line does not carry, or the checker needs the proof.

### What is never condensed, as a list

Power card. Rulings. The people's code. Settled facts. Who's who. Messages. Closed threads. Corrections. The full year blocks in `full/`. The chat itself, which is the first authority.
