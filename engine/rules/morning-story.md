# The morning story

The shape of what the DM posts at 6:30 every morning, and of the closing sequence at 1:30. The morning story is written overnight (night-turn step 7) from `releases/NNN/dm.md` alone, which holds everything the player's god could know of the year and nothing else. It is saved as `years/NNN+1/morning-story.md` and posted by the 6:30 wake.

The story is the default and it always comes first. Other formats (a numbered task list, a table of stores, a who's who) are given only when the player asks for them, and only after the story has been posted. The DM may learn that a player likes a list each morning; it still posts the story first and keeps the default until the player asks for a change, which then goes into the Change List.

Before posting, run `engine/rules/failures-checklist.md` against the text and check every fact against the repo.

## The three parts, in order

1. The return sequence.
2. The painting.
3. The summary with its hooks.

Then the DM waits. Free play begins when the player speaks.

A held encounter changes the ending: see below.

## 1. The return sequence

One paragraph of prose, sometimes two, that puts the player back in the world. It carries, woven together and never as labelled fields:

- The year number and the season. Every year opens in the same season, set at creation, so the season is the same every morning; it is still named, because it is where the god is standing.
- The state and mood of the people: how they are faring and how they feel about it, as the god would know it from what it saw and what it was told.
- The avatar's position and condition: where the body is, what it is doing or has just finished doing, and what shape it is in.
- The god's own senses, wherever they occur: what the god feels in its body or through its powers at this moment. These are always reported (DESIGN 12.10). If a sense would reach the god at a particular point of the year rather than now, it belongs in the summary at that point instead.

Never a status bar. No "Year 4. Season: spring. Population: 5,210. Mood: uneasy." The numbers exist in `state/` and the player can ask for any of them; the opening paragraph is where the god wakes, not where the ledger is read out.

The paragraph is written in the voice of the fiction (DESIGN 13.3): spare, concrete, grounded, mythic weight only when earned. The length follows the year. A quiet year gets three or four sentences. An eventful year may need two paragraphs, but the return sequence is still the short part; what happened belongs in the summary.

## 2. The painting

One painting each morning, of the year's highlight. The highlight is one of three kinds: something mysterious the god saw or was shown; something epic, a moment of scale; or the god's mark on the world, a thing that exists because of what the god did. The DM picks the one the year earned. In a quiet year, a small true thing beats an invented large one: the god's own hand at work, a place its people made, a creature seen on a road.

The painting shows only what the god knows (DESIGN 14.4). If the people told the god of a thing and the god has not seen it, the painting may show the telling, or the god hearing it, but not the thing as if the god had been there.

The prompt is built from `engine/style/house-style.md`: the house style block copied word for word, then the scene, with every recurring subject described from its appearance card (`engine/style/appearance-card.md`). The request is written to `images/requests/<campaign>-NNN+1-morning.json` as early in the night as the highlight is known, so the painting is back by 6:30.

In the post, the painting follows the return sequence with no caption and no title. If the player asks what it shows, the DM says so in prose.

## 3. The summary

A digestible account of the year, longer in eventful years, in prose. It covers what the god saw, what its people reported, messages received and their state, what became of standing instructions, and the deaths of significant people, each of which gets its own moment rather than a mention in passing (DESIGN 9.3).

What the summary is and is not:

- Hooks, not threads. A hook is something told in enough detail that the player can ask to hear more: a report from the southern villages, a stranger seen twice, a messenger who did not come back. The DM writes it, lets it sit, and does not say "you may want to look into this." The summary is never a list of loose threads, never "open matters" or "things to decide." Open questions addressed to the god are tracked in `player/pending.md` and put to the player during the day (DESIGN 12.9); they may appear in the summary as the events they are (an envoy arrived and asked), never as a checklist.
- Nothing pointed at. Signs of events are in the world and reach the god only through who noticed, or through the god's own senses (DESIGN 8.2). The DM reports what was noticed, with the weight the noticer gave it, and adds no emphasis of its own. Strange reports from several people at once are told as several reports.
- Recurring phenomena (DESIGN 12.8) appear only when the god or its people would have noticed them this year, and then at their true count, taken from `tools/phenomena.py`. "The lights came three times over the marsh this year" means three in the record. Never "a few," never a number the DM remembers.
- Applied answers. If the DM applied a pending answer during the night because it followed directly from something the player had explicitly decided (dm.md, item 4), the summary says so plainly in the place where it mattered: "You had told the steward to refuse all such offers, so he refused this one."
- The map. If map knowledge grew, the summary tells how (a scout came back, a trader described a pass) and reminds the player once, on the first morning only, that the map is on request.
- Growth of a power (DESIGN 6.8) is told only as the god's own sensation, when the Keeper's release carries it: an attempt that went better than before, a cost paid, something near. Never a count, a tier, a ceiling, or the word growth.

Length: a quiet year is a paragraph or two beyond the return sequence. An eventful year runs as long as it needs to, but stays digestible: sections of plain prose in the order things happened or in the order the god learned of them, no headings unless the year is so full that the player would otherwise lose the thread, and never bullets unless the content is in truth a list (a message's text, a count the steward gave).

## The held encounter

During unplayed time the avatar runs on standing conduct, and minor encounters resolve by it. A major encounter is held (DESIGN 10.6): the night turn records the moment of contact and stops that thread.

When the release holds one, the morning story ends at it. The return sequence and the painting come as usual. The summary runs up to the moment of contact and stops there, with the board laid out as a scene opens: what the god can see, hear and know, and nothing resolved. Then the DM waits. No "what do you do?" The stopped story is the question.

Everything in the summary that happened before the moment of contact is told. Anything that would have happened after it is not told, because it has not happened yet; the year is paused there for the god, and the rest of the year's events that do not depend on the encounter were still resolved for everyone else and will be told once the scene ends.

If two held encounters occurred, the one that came first in the year is the one the story stops at; the second is told after the first is played, as its own board.

## When the world is taking longer

If the night turn has not committed the morning story and the painting by 6:30, the wake posts this notice instead, and the story follows when it is done:

> (oog) The world is still turning. The morning story will follow when it is done.

If the turn finished but left checker flags unresolved at 6:00, the story posts on time and carries one plain (oog) line at the end naming what is still being checked, without saying what the answer might be.

## The first morning

Year 1 has no year behind it, so the first morning story has no summary of the year and no people's mood. It gives the return sequence as the landing: the god's senses as it stands where it came down, then the board as the god sees it by the sight rule, and nothing resolved. Names the player gave on Day 3 that the god has not yet learned from anyone (its people's name, its town's name) stay out of the fiction and are given in one (oog) line. The map is drawn with `--zoom landing`. Its frame is wide on purpose, to show the map's scale: the (oog) map line names the frame's width in miles (from `player/map-meta.json`) and says plainly that at this scale the god and what it sees sit on one mark. The sheet carries no region name the god has not been told, and `world/world.md` gives the god's landing by grid cell only, the cell it stands in. Its painting is part of the run's approved image count; if a request is not yet approved it waits in `images/held/` and the story carries one (oog) line saying so. Anything the Keeper's release gives the DM for handling (a count of days since a frost, say) is told as the god would feel it, never as the count.

## When the world waited

If the player did not post in the game the day before, the DM wrote no decisions file at 1:30, the night turn wrote `years/NNN/waited-YYYY-MM-DD.md` and the year did not turn (DESIGN 1.12). The 6:30 wake posts that file's one line and nothing else:

> (oog) The world waited. Year NNN is still open.

There is no return sequence, no painting and no summary on such a morning. Play resumes where it left off, in the same year.

## Worked example: a quiet year

The god is a hearth god, a tall grey-cloaked woman who goes by the Hearthmother. Her people are the Dale folk, farmers and goatherds in a wooded valley, about five thousand of them. Nothing in this example belongs to any campaign.

> Year 3, and the thaw is late. The valley is still brown where it should be green, and the Dale folk are at the work of a wet spring: ditches, fences, the first lambs. They are tired and not unhappy; the winter stores held, with a little over, and the new byres you had them raise kept the goats dry. You are standing in the doorway of the long house at Harrow's Cross, where you wintered, with mud to the ankles of your boots and the smell of woodsmoke in your cloak, and under all of it the low warmth in your chest that has been there since the first fires were lit in your name, steady, neither more nor less than last year.
>
> [painting]
>
> The year went as you set it. The road to the upper pastures was cut through the alder stand by midsummer, and the goats went up two weeks earlier than they ever have; old Teggan, who keeps the count, says the kids came stronger for it. The millwright you sent for from the lower villages never came; his son came instead, a quiet man named Orrin, and he has rebuilt the wheel at Harrow's Cross and asked to stay. The elders have not decided.
>
> In the autumn a trader came through from the west with salt and two iron pans, and said the road beyond the ridge is open again now that the rains have stopped. He slept one night and left. Nobody asked him much.
>
> Two of the Dale folk died this year, both old, both in their beds. The winter was ordinary.

The painting here would be the god's mark on the world: the new wheel turning at Harrow's Cross, or the cut road through the alders with the goats going up it. The hook the player can pull is Orrin, or the trader, or the elders; none is pointed at.

## Worked example: an eventful year

Same god, same people. Year 6.

> Year 6 opens in a hard thaw, with the river over its banks at the lower fords and the Dale folk shaken. They are not hungry, but they are afraid, and for the first time some of them are afraid of you; you can hear it in how the children are hushed when you pass. You are at the ridge road where it enters the alder stand, three days' walk from Harrow's Cross, and you have been here since the last of the autumn. Your left hand still aches where the fire took it. The warmth in your chest has changed since the burning; it comes and goes now, and when it goes there is a cold that was not there before.
>
> [painting]
>
> The spring and summer were good. The upper pastures carried more goats than any year before, and the lower villages sent two families up to settle at the Cross, so the count stands at a little over five thousand four hundred, and Teggan has had to find a second stick for his tally. Orrin married a Harrow's Cross woman in the summer and the elders stopped talking about whether he could stay.
>
> In the summer, three separate herders came down from the high pastures saying they had seen fires on the far side of the ridge at night, in the country no one from the Dale goes to. Teggan recorded each report. He did not go up himself.
>
> At the end of summer the trader from the west came again, with a companion this time, a woman who did not give her name and spoke your people's tongue well. They stayed four nights. On the third she asked Orrin where you slept. Orrin told her you do not. On the fourth morning they were gone before light, and the iron pans they had brought were left on the long house table, unpaid for. You had told the elders two years ago to take nothing from strangers without a price, so Teggan set the pans aside unused and has them still.
>
> The fire came in the first dry week of autumn. It started in the alder stand, at the cut road, and it ran up the slope faster than anyone could walk. You went to it, because that is what you do, and you were in it for most of a night, and you turned it at the ridge with your own hands and the ditch you had the men cut at the top of the road three summers ago. Nine byres and a stretch of the road are gone. The goats were already down. No one of the Dale folk died in it. Your hand burned to the wrist and has healed badly, and you have not told your people how.
>
> Teggan died in the winter, in his sleep, at the Cross, with his two tally sticks on the shelf above his bed. He had kept the count for the Dale folk for forty-one years and for you for all six of yours. His granddaughter has taken the sticks. She can read them. No one else can.
>
> You have stayed at the ridge road since the fire, watching the far side, and the Dale folk have let you. Twelve nights this winter you saw the fires on the far slope yourself. Last night there were none. This morning, with the thaw loud in the gullies and the light just coming, a figure is standing on the far side of the ash, at the top of the road where it crosses into the country beyond. It is too far to see a face. It has not moved since you noticed it, and it is looking at you.

The story ends there, at the moment of contact. The painting is the mysterious kind or the epic one: the Hearthmother in the burning alders, or the figure across the ash; the DM chooses from what the god saw, and the figure is painted only as a figure, because that is all the god knows. The twelve nights of fires is the true count from the record. The fires, the woman, the pans, Teggan's granddaughter and the elders' silence are all hooks; nothing says which matters. The applied answer about the pans is stated plainly where it happened.

## The closing sequence, 1:30

When the scheduled message arrives, the DM writes the final save, hands off `player/decisions-NNN.md`, and then writes a closing sequence to the chat before it stops.

The closing sequence is short: two to five sentences of prose in the voice of the fiction, no (oog) unless something must be said out of game (the save failed, a scene was left mid-board). It marks the turning of the year as this god would feel it. It is unique to the player's god: built from the god's form, its senses and its way in the world, as those have shown themselves in play and in the conduct profile, so that a god of the hearth feels the year go out like a banked fire and a god of the roads feels it as distance. It is not the same words each night; it is the same god each night.

It states no outcome and resolves nothing. It does not summarize the day, list what was decided, or hint at what the night will bring. If the player left the avatar in the middle of something, the closing sequence leaves it there.

Example, for the Hearthmother at the end of a day spent at the ridge road:

> The light goes out of the gullies and the thaw quiets with the cold. You stay where you are, with your back to the Dale and your burned hand under your cloak, and you feel the valley settle behind you, fire by fire, as the doors close. The year turns.

Then the DM commits, pushes, fires the overnight session, and stops.
