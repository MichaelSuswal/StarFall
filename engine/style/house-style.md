# House style for paintings

One style for every painting in every campaign (DESIGN 14). The DM builds each prompt in two parts: the house style block below, copied word for word, then the scene. Nothing in the block is changed, shortened or paraphrased per painting; it is the constant, and the scene is the only variable.

The reference paintings are `images/out/test-fox-doorway-2.png` (approved: smooth, finely blended surface) and `images/out/test-fox-doorway.png` (rejected: rough, visible brushwork). The difference between them came entirely from the first sentence of the prompt. The approved opening is the one in the block. Never ask for visible brushwork, impasto, texture, canvas weave or painterly strokes in the scene text, because any of those words undoes the block.

## The house style block

Copy this exactly, as the first paragraph of every prompt:

> A 19th-century academic oil painting with a smooth, finely blended surface: soft glazed transitions, delicate fine detail, minimal visible brushstrokes, no heavy impasto, no rough texture. Strong light and shadow from a single warm source (a lamp, a torch, a fire, a low sun) or from heavy overcast, with deep chiaroscuro. Palette of umber, ochre, gold, olive and near-black, with occasional cool accents. The manner of a romantic landscape, a grand historical scene, or a natural-history study of a creature painted as if real. A low, close viewpoint. Wet, reflective stone where there is stone; ancient architecture where there is architecture; one saturated subject held against darkness; scale shown by something small beside something vast. Quiet, watchful, ominous mood. No text, no lettering, no border, no frame, no grid texture, not photographic.

Then a blank line, then the scene.

## The map block

The map paintings (Night 3a: the surface, the cloud layer, and an underground sheet only if the world has one) are not scenes. They use this block instead, as the first paragraph, and then the Keeper's placement plan written as a painter's brief: the coasts, ranges, rivers, woods, marshes, deserts and plains in their places, by compass direction and rough proportion of the sheet, with no names.

> A hand-painted map of a whole continent seen from directly above, in the manner of a painted fantasy map such as a map of Middle-earth: coastlines, mountain ranges drawn as shaded ridges, rivers as fine dark lines running downhill to the sea, forests as textured masses, marsh, desert and open plain each in its own tone. Oil on parchment in a 19th-century academic manner with a smooth, finely blended surface, soft glazed transitions, fine detail, no heavy impasto. Palette of umber, ochre, gold, olive and sea-green with near-black shading. Less detail at larger scale; nothing drawn smaller than a hill or a wood; no settlements, no roads, no figures, no borders between countries. No text, no lettering, no compass rose, no scale bar, no frame, no grid, not photographic. The whole sheet is land and sea; nothing is cut off at the edges.

For the cloud layer:

> A continuous sheet of pale cloud seen from directly above, painted in oil in a 19th-century academic manner with a smooth, finely blended surface: soft, dense, overcast cloud with slow variations of grey, cream and faint ochre where light comes through, no gaps, no ground visible, no horizon, no text, no border, no frame, not photographic.

For an underground sheet, the surface block with "a whole continent" replaced by "a vast cavern country: galleries, sunken rivers, salt flats and lightless lakes, lit faintly from within". The brief after it is the layer as it is in `map.json`, which is written before the painting. A layer that is mostly solid is asked as solid rock, with the hollows described as its only features: for such a layer the replacement is "a continent's depth of unbroken solid rock seen from directly above, dark and close-grained" and the brief names each hollow, where it lies and how large, and nothing else. The painter does not keep to "nothing else is hollow" for a mostly empty layer, so the Keeper checks the painting against the data: where they differ, the data rules and the player's sheet is shown only fogged to the known hollows (`engine/rules/map.md` 1.1).

Map requests are sealed: `SPOILERS_do_not_open/images/requests/<campaign>-map-surface.json`, `-map-clouds.json`, `-map-under-1.json`, with outputs in `SPOILERS_do_not_open/images/out/`. A map prompt describes the whole world, so it is a spoiler.

## The scene

The scene is one paragraph of plain description, in the order the eye should take it: the subject, where it is, what the light is and where it comes from, what is near, what is far, and what the small thing beside the vast thing is. It names the time of day and the weather. It does not repeat the style block, name a painter, or add mood words the block already carries; it gives the block something to paint.

Keep the scene concrete. "A river in flood under a low sun" paints; "a sense of foreboding over the valley" does not.

### The three kinds of picture

Every painting is one of three, and the DM knows which before writing the scene:

- Mysterious: something the god saw and does not understand. Painted plainly, at the distance the god saw it from, with nothing added to explain it.
- Epic: a moment of scale. A crowd, a march, a storm, a burning, a city seen whole. Wide shape.
- The god's mark on the world: a thing that exists because of what the god did. A road, a wheel, a wall, a healed field, a people at a work the god set them. Often the quietest of the three and often the best.

### The appearance-card rule

Every recurring subject (the avatar, a significant character, a creature the god has seen before, a place the god has been) has an appearance card (`engine/style/appearance-card.md`). When such a subject is in the scene, its card text is copied into the scene word for word, in full, every time. The DM never paraphrases a card, never shortens it to the parts that seem to matter today, and never describes a carded subject from memory. If a dated change on the card applies (a scar, a rebuilt roof), that line is copied too. The same words every time are what keep the subject the same every time.

A god whose card gives no face is never painted with one, since any painted face invents it. Its scene adds this line, word for word, after the card text: "Seen from behind or in deep shadow, the head turned away or lost in darkness, no face visible." A god whose body is not a figure (a swarm, a mist, a flock, a stone) has no head to turn, so its scene adds this line instead, word for word: "Seen at a distance or in deep shadow, with no face anywhere in it."

A subject seen for the first time has no card yet. The DM describes it from the release, and if it will recur, writes its card that day so the next painting copies the card.

### The knowledge rule

A painting shows only what the god knows (DESIGN 14.4). It may show what the god saw, from where the god saw it; what the god sensed, as the god sensed it; or a telling (people reporting to the god), but never the reported thing as if the god had stood before it. A figure seen at a distance is painted as a figure at a distance. A creature known only from a herder's description is painted as the herder's description, with the herder in the frame, or not painted at all. A place the god has not entered is painted from its threshold.

The painting never shows terrain the god has not seen, a face the god has not seen, a hidden cause, or anything from `SPOILERS_do_not_open/`. The DM cannot read that folder and should not need to; if a scene would require it, the scene is wrong.

### Shape

Chosen per scene (DESIGN 14.6): wide for vistas and crowds, square for close studies. In the request file this is `"shape": "wide"` or `"shape": "square"` (`tools/paint.py` also accepts `"tall"`, which the house style does not use). A creature study, a single figure, a doorway, a hand at work: square. A valley, a march, a city, a storm front, a crowd at a gate: wide.

### The daily limit

One painting each morning, made overnight. During the day the player may ask for up to two more. After the second, the DM asks the player to wait until the next day (DESIGN 14.7). Each request costs money on Michael's account; the DM never makes a painting the player did not ask for, beyond the morning one.

## The request file

`images/requests/<campaign>-NNN-morning.json` for the morning painting; `images/requests/<campaign>-NNN-request-1.json` and `-request-2.json` for the two on request. The file is one JSON object:

```
{"id": "<campaign>-NNN-morning", "shape": "wide", "prompt": "<house style block>\n\n<scene>"}
```

The `id` is the output filename without `.png`. The GitHub job paints anything in `images/requests/` that has no output yet and puts the painting in `images/out/<id>.png`.

## Three complete example prompts

Each is the block followed by a scene. The subjects are invented for this file and belong to no campaign. Where a card would be copied in a real prompt, the example shows card text in place.

### A landscape, wide

Kind: the god's mark on the world.

> A 19th-century academic oil painting with a smooth, finely blended surface: soft glazed transitions, delicate fine detail, minimal visible brushstrokes, no heavy impasto, no rough texture. Strong light and shadow from a single warm source (a lamp, a torch, a fire, a low sun) or from heavy overcast, with deep chiaroscuro. Palette of umber, ochre, gold, olive and near-black, with occasional cool accents. The manner of a romantic landscape, a grand historical scene, or a natural-history study of a creature painted as if real. A low, close viewpoint. Wet, reflective stone where there is stone; ancient architecture where there is architecture; one saturated subject held against darkness; scale shown by something small beside something vast. Quiet, watchful, ominous mood. No text, no lettering, no border, no frame, no grid texture, not photographic.
>
> A new road cut through a stand of alder trees, climbing a wooded valley side toward high pasture, seen from low on the road itself just after dawn in a wet spring. The low sun comes from the right, behind the ridge, and lights the wet ruts of the road gold while the alders on either side stay dark. Far up the road, small, a herder and a line of goats are going up into the light. Near the viewer, a single cut alder stump, fresh and pale, with rainwater standing in the rings. Mist in the valley bottom behind. No figures near the viewer.

### A creature study, square

Kind: mysterious. The creature was seen once by the god, at dusk, at thirty paces, and has a card from that sighting. The card text is the second and third sentences of the scene.

> A 19th-century academic oil painting with a smooth, finely blended surface: soft glazed transitions, delicate fine detail, minimal visible brushstrokes, no heavy impasto, no rough texture. Strong light and shadow from a single warm source (a lamp, a torch, a fire, a low sun) or from heavy overcast, with deep chiaroscuro. Palette of umber, ochre, gold, olive and near-black, with occasional cool accents. The manner of a romantic landscape, a grand historical scene, or a natural-history study of a creature painted as if real. A low, close viewpoint. Wet, reflective stone where there is stone; ancient architecture where there is architecture; one saturated subject held against darkness; scale shown by something small beside something vast. Quiet, watchful, ominous mood. No text, no lettering, no border, no frame, no grid texture, not photographic.
>
> A natural-history study of a single animal standing on wet shingle at the edge of a dark river at dusk. A heron-like wading bird the height of a tall man, with a body of pale ash-grey feathers that darken to near-black at the wingtips and tail, long black legs with backward-bending knees, and a narrow head carried low on a long neck. Its bill is the dull bronze of an old blade, as long as a forearm, and its eyes are small, round, and the yellow of tallow. It stands side-on with its head turned to look at the viewer. The last light is low from the left, warm on the near side of the bird and the wet stones; the far bank is black. A single small river snail on the shingle in the foreground gives the scale. The bird is painted as if real, with every feather described.

### A crowd scene, wide

Kind: epic. The avatar has a card; the card text is the sentence beginning "A tall woman."

> A 19th-century academic oil painting with a smooth, finely blended surface: soft glazed transitions, delicate fine detail, minimal visible brushstrokes, no heavy impasto, no rough texture. Strong light and shadow from a single warm source (a lamp, a torch, a fire, a low sun) or from heavy overcast, with deep chiaroscuro. Palette of umber, ochre, gold, olive and near-black, with occasional cool accents. The manner of a romantic landscape, a grand historical scene, or a natural-history study of a creature painted as if real. A low, close viewpoint. Wet, reflective stone where there is stone; ancient architecture where there is architecture; one saturated subject held against darkness; scale shown by something small beside something vast. Quiet, watchful, ominous mood. No text, no lettering, no border, no frame, no grid texture, not photographic.
>
> A grand historical scene: several hundred farming people gathered at night in the mud of a village square before a long timber hall, holding torches, seen from low among them near the back of the crowd. The only light is the torches, which catch on wet thatch, wet faces and the puddles in the mud. At the far end, on the hall's step, stands a tall woman of about forty with a long, plain face, grey eyes, and dark hair bound back in a single braid, wearing a hooded cloak of undyed grey wool over a brown dress, with bare feet and a burn scar across the back of her left hand. She is the one figure the torchlight reaches fully; she stands still with both hands at her sides. Between her and the crowd, a small child has stepped out alone into the open mud and is looking up at her. Rain is beginning. Beyond the hall, the valley side is black.
