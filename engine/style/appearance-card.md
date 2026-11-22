# Appearance cards

An appearance card is a fixed visual description of a recurring subject, written once and copied word for word into every painting prompt that shows it (DESIGN 14.3, house-style.md, the appearance-card rule). The card is what keeps the avatar, a significant character, a creature or a place looking the same across years of paintings. It is never paraphrased, never trimmed, never rewritten from memory.

## Who gets a card

- The avatar: always, written on Day 2 from the negotiated god and kept at `player/appearance-card.md`.
- Significant characters: once a character becomes significant (DESIGN 9.2), their nature and history are fixed in the record, and their card is written the same day.
- Creatures: any creature the god has seen that may be seen again, written from the first sighting and only from it.
- Places: any place the god has been that may be painted again.

Cards for everything but the avatar live in `player/appearance-cards/<slug>.md`, one per subject, because they belong to the god's side of the record: they describe only what the god has seen. NPC gods keep cards for their own avatars in their sealed folders; the player's card for an NPC god, if there is one, holds only what the player's god has seen of it, and the two may disagree.

## The card

```
# <Name>
Kind: god | mortal | creature | place
Written: Year NNN (or "creation, Day 2" for the avatar), from <what the god saw or who told it>

<The card text: 40 to 80 words, one paragraph.>

## Changes
Year NNN: <one line, the change and its cause>
```

### The card text

One paragraph, 40 to 80 words, in plain descriptive prose that a painter could work from: build, size, color, clothing or hide or stone, the two or three details that make this subject this one and no other. It describes what is seen, not what is known or felt: no "kindly," no "a feared man," no "the heart of the valley." Scale is given against something concrete (the height of a tall man, a horse's shoulder, the span of a doorway). For a place, the card fixes the parts that do not move (the shape of the ground, the building, the stone) and not the weather or the hour.

It is written from what the god saw at the time it was written, and no more. If the god saw a creature at thirty paces at dusk, the card says what thirty paces at dusk showed; it does not fill in the teeth. A card for a place the god has stood outside describes the outside.

Once written, the paragraph is not edited. Its words are the fixed point.

The copy text is the only paintable part. Anything else the card needs to say (a line that cannot be painted, such as a sound or a smell, or a line that holds only in some situations) goes below it, each such line marked `Not painted:` or `When <situation>:`, and is never copied into a prompt except a `When` line whose situation is the scene's. A card that gives no face says so in a `Not painted:` line, and every painting of that subject uses the house style's back-view line.

### Changes

Subjects change through events in the world: a wound, a greying, a rebuilt roof, a burned wing. A change is never written into the card text. It is appended under Changes as one dated line, with its cause, and from then on the DM copies the card text and every applicable change line into the prompt together. A change line is visual and brief: "Year 6: left hand burned to the wrist in the alder fire; the scar runs across the back of the hand." If the god learns that its first sight was wrong (the creature is smaller than it seemed), that is also a change line, with the year the god learned it, and the card text still stands above it.

A character's death closes the card with a final change line. The card is kept; nothing is deleted.

## Examples

Invented for this file. No campaign uses them.

### A god

```
# The Hearthmother (the avatar)
Kind: god
Written: creation, Day 2, from the god's own form as negotiated
Copy text: the first paragraph below is what the painting prompt copies word for word; nothing after it is copied

A tall woman of about forty with a long, plain face, grey eyes, and dark hair bound back in a single braid, wearing a hooded cloak of undyed grey wool over a brown dress, with bare feet. She stands a head above the tallest of her people. Her hands are large, red-knuckled, and always uncovered. She carries nothing. Where she stands for long, the ground beneath her feet dries.

## Changes
Year 6: left hand burned to the wrist in the alder fire; the scar runs across the back of the hand, shiny and pale.
```

### A mortal

```
# Teggan, keeper of the count at Harrow's Cross
Kind: mortal
Written: Year 1, from the god's first meeting with him at the long house

A short, thick old man of about seventy with a bald, freckled scalp, a white beard cut close, and a bent back that puts his eyes at the height of a child's. He wears a sleeveless sheepskin over a long wool shirt, belted with rope, and wooden-soled shoes. He carries a notched tally stick of dark hazel as long as his forearm, held in his left hand, and squints with his right eye.

## Changes
Year 4: a second tally stick, pale new hazel, carried with the first.
Year 6: died in his sleep at the Cross in the winter. Card closed.
```

### A creature

```
# The grey wader of the lower river
Kind: creature
Written: Year 5, from the god's own sighting at dusk, thirty paces, on the shingle below the lower ford

A heron-like wading bird the height of a tall man, with a body of pale ash-grey feathers that darken to near-black at the wingtips and tail, long black legs with backward-bending knees, and a narrow head carried low on a long neck. Its bill is the dull bronze of an old blade, as long as a forearm, and its eyes are small, round, and the yellow of tallow. It stood side-on and did not move while watched.

## Changes
```

### A place

```
# The long house at Harrow's Cross
Kind: place
Written: Year 1, from the god's first winter in it

A single-storey timber hall, five bays long, with walls of upright split oak gone silver and a roof of thick thatch that reaches nearly to the ground on the north side. A wide door at the west gable, with a stone step worn hollow in the middle and a sill of flat river stone. Inside, one open hearth in the middle of an earth floor, a smoke hole above it, and sleeping benches along both walls. It stands at the meeting of two tracks on flat ground above the river.

## Changes
Year 3: the mill wheel beside the house rebuilt in new oak by Orrin; the race cleared and running.
```
