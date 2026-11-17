# Rules: messages

How a message from one god to another, or from any party to any distant party, is written, carried, delayed, stopped and delivered. Binding on the DM, the Keeper, every NPC god agent and every civ agent. Sources: DESIGN.md 7.1, 7.3, 7.9, 10.1, 10.2, 12.2, 12.6, 12.9.

## 1. What counts as a message

A message is anything one party sends to another who is not present: a letter, a spoken word carried by a messenger, a gift with meaning, a token, a treaty for signature, an envoy's errand. It applies between gods, between a god and a distant mortal ruler, between peoples, and from a god to its own people when the god is far from them. Speech between two parties in the same place is not a message; it is a scene.

Only the world can carry a message (7.1). There is no god-to-god channel unless a power card says so for a specific god, and that power's drawback and rulings apply. God-sense (7.2) tells a god that others exist and roughly where; it carries no words.

The engine never loses a message (7.1). Every message has a log entry from the moment it is sent until its fate is known, and the fate is always one of the states in section 4. A message with no entry did not happen.

## 2. Writing a message

The sender's agent writes the message in full: the words as the sender gave them, in the sender's voice, in the language chosen (7.3). For the player's god the DM takes the words from the player and does not improve them. The player may write the message in character in quotes or describe it in (oog); either way the DM records the text as given and reads it back once before sending.

Each message is stored as its own file: `campaigns/<name>/messages/<id>.md`.

```
# Message <id>

Year sent: NNN
Sender: <god or person, and their people>
Recipient: <god, person or people, as the sender named them>
Language: <mortal tongue | god-tongue | both | token with no words>
Carrier: <see section 3>
Route: <from, to, by way of, as the sender or carrier chose it>
Form: <letter | spoken | token | envoy | gift>

## Text
<the words, exactly as given>

## Carried with it
<anything sent alongside: gifts, hostages, a chart, a sample>

## Sender's instructions to the carrier
<what to do if the recipient cannot be found, is hostile, or asks questions>
```

The recipient's agent sees this file, and only the parts a recipient would see, once the message is delivered (section 5). Until then only the sender's agent and the Keeper can read it.

## 3. The log

`campaigns/<name>/state/messages.jsonl`, one line per message, appended by the Keeper. The line is never rewritten; a change of status is a new line with the same `id` and a later `year`. The current state of a message is its last line.

```
{"id": "m-0017", "year": 4, "sender": "the fox god", "recipient": "the god of the salt coast",
 "carrier": "rider, Oren of the ford", "route": "ford, hill road, salt marsh causeway",
 "sent": 4, "expected": 5, "status": "sent", "file": "messages/m-0017.md", "note": ""}
```

Fields:

- `id`: `m-` plus a running number, never reused.
- `year`: the year this line was written.
- `sender`, `recipient`: as named by the sender. The Keeper does not correct a wrong name; a message to a god the sender has misidentified goes where the carrier takes it.
- `carrier`: `in person` or the kind of messenger and, if a notable person, their name.
- `route`: the way the carrier is taking, in the sender's or carrier's words.
- `sent`: the year the carrier set out.
- `expected`: the year the Keeper expects arrival from the pace table (section 4). Not shown to the player unless the player's god would know it (a god who has sent riders along that road before knows roughly how long it takes).
- `status`: one of `sent`, `in transit`, `delayed`, `delivered`, `intercepted`, `lost with carrier`, `returned`, `refused`, `undeliverable`. Each is defined in section 4.
- `file`: path to the message file.
- `note`: what happened this year, one line, with the roll id if a roll decided it.
- `reply_to`: optional, the id of the message this answers.

## 4. Carriage

### Speed

A message moves at the carrier's pace from the pace table (`tools/pace.py`, 10.1): real-world rates for a walker, rider, cart, boat or ship, adjusted for terrain, weather and season. A god carrying its own message moves at mortal pace unless its power card says otherwise (10.1). Gods need no sleep or food (10.2), so a god carrying a message in person covers more ground per day than a mortal, but not faster ground.

The Keeper computes the expected arrival year from route length and pace and writes it to `expected`. Within one year, the Keeper also notes the season of arrival in the keeper log, so a message sent in spring to a neighbor three weeks away arrives the same year and the recipient's agent can act on it in that same night turn.

If the route is unknown to the carrier (no one from the sender's people has traveled it), the Keeper adds time for finding the way, as a factor on the year's carriage roll, and the carrier may arrive somewhere other than intended.

### What can stop a message

Only the world (7.1). The Keeper does not stop a message for story reasons, and no agent may decide a message simply fails. Each hazard is a contest resolved by factors and a logged roll through `tools/roll.py` (12.6), factors recorded before the roll, who=`keeper`, what=`carriage of <id>, <hazard>`.

| Hazard | When it is rolled | Typical factors |
|---|---|---|
| Bad road, hard country | Any year the route crosses terrain the pace table marks as hard, or unknown ground | known route +10, guide +5, mountains or marsh -10, unknown ground -10 |
| Storm, flood, winter | When the Keeper's pass one puts weather or season on the route in the carriage window | sea crossing in storm season -20, river in flood -10, waited for season +10 |
| Interception | When the route crosses a people or god hostile or curious enough to stop travelers, as the record shows, or when a god has set watchers | sealed and plain-looking +5, escorted +10, known hostile border -20, god watching the road -10 |
| Death or loss of the carrier | When any of the above fails badly, or when the route crosses plague, war or wild country | notable and skilled carrier +10, alone -5, war on the route -20 |
| Refusal | When the recipient will not receive it, decided by the recipient's agent in character | not rolled; the recipient's choice |

A message that passes a hazard continues. A message that fails one gets a new status line:

- `delayed`: the carrier waits out the season, takes a longer way or recovers. `expected` moves out. The message continues next year.
- `intercepted`: someone in the world has the message. The interceptor's agent receives the text as a release and decides what to do with it: read, destroy, forward, forge a reply. The original recipient may or may not ever learn. The carrier's fate is rolled separately.
- `lost with carrier`: the carrier is dead or cannot continue, and the message lies where they fell. It is not gone from the world; it is a fixed fact at that place in the keeper log and may be found.
- `returned`: the carrier came back, with the message or with news, per the sender's instructions.
- `undeliverable`: the recipient could not be found where the carrier looked. The carrier acts on the sender's instructions: wait, search, return.
- `refused`: the recipient would not take it. The carrier learns this and returns or waits.

A message that reaches its recipient is `delivered` in the year it arrives, and that is the end of its line except for a later `reply_to`.

A message carried in person by a god is subject to the same hazards. A god cannot die (7.8), so "lost with carrier" for a god means the god is detained, turned back, wounded or cut off, and the message's fate follows the god's. Where a god's carrying becomes a major encounter for the player's god, section 6 of `encounters.md` applies: the story stops at the moment of contact and the player plays it.

### Routing through other gods' lands

When a route crosses another god's country, the Keeper writes the carrier's passing into that god's civ release for the year if its people would have noticed. A god whose land is crossed may act on that in the next turn. Nothing is hidden from the world merely because a message is private.

## 5. Delivery in the night turn

Delivery happens in Keeper pass two (night-turn.md 4) and is released in stage 6.

1. In pass two the Keeper takes every message whose `expected` is this year or earlier and whose last status is `sent`, `in transit` or `delayed`, and rolls its hazards for the year's leg of the route, factors first.
2. For each message that arrives, the Keeper writes a `delivered` line to the log and copies the message file's Text, Carried with it, and the carrier's name and condition into the recipient agent's release (`releases/NNN/<agent>.md`), under a heading `Messages received`. For the player's god, that is the DM's release. The recipient's agent sees the sender's instructions to the carrier only if the carrier would reveal them.
3. For a message delivered to an NPC god, that god's agent reads it at the start of its next decisions step (night-turn.md 1) and may answer. An answer is a new message under section 2, with `reply_to`. For a message delivered to the player's god, the DM puts it in the morning story as the moment the carrier arrived, and the question it carries, if any, becomes a pending item (12.9).
4. If the message arrives within the year while the recipient's civ agent is still acting (a short route), the Keeper may release it in pass one instead so the recipient's year can respond to it. The Keeper notes this in the keeper log.
5. A message to a people or a mortal ruler goes to that people's civ agent (or the Keeper for a godless people), who decides in character how it is received and reported to its god.

The recipient's agent is given only what a recipient would have: the words, the carrier and what the carrier says, the gifts. It is not given the sender's log line, the route rolls, or the sender's instructions.

## 6. How the sender learns the fate

The sender learns nothing from the engine. It learns only through the world (7.9, 12.2):

- A carrier who returns brings word: delivered, refused, could not find them, turned back. The return trip takes its own time at the pace table and is its own log line (`returned`) on the same message.
- A reply arriving tells the sender the message was delivered, and when, if the reply says so.
- A carrier who does not return in the expected time tells the sender nothing certain. The DM may report, if the god would think it, that the rider is late. It never says why.
- Interception may never be learned, or learned years later by its consequences.
- A god's own senses, if its card gives it any that bear on this, apply as the card says.

The DM does not tell the player the `expected` year unless the god has grounds to know it, and never tells the player a message's status from the log. The chronicle (`chronicle.md`) lists each sent message with its fate as the god knows it, and the god's knowledge may be wrong (7.9).

NPC gods are under the same rule. An NPC god's agent is never shown the log; it knows what its carriers tell it.

## 7. Checks

The continuity checker flags: any message in a release without a `delivered` line; any `delivered` line with no release; any status change without a roll id where a hazard was in play; any message older than its `expected` year with no new line that year; any agent acting on a message it was not released; and any message mentioned in play that has no file or log line. The Keeper reworks each flag before the morning story.
