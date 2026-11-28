# StarFall

Version 1.0 (build 8, 2026-11-27).

A single-player god game played in one long chat, at most one year of the world per real day. You fall into a world that does not know you yet, land in country suited to you, and lead whoever you find there. Other gods have fallen too. You will never be told how many.

## Starting a campaign

Creation takes three days, played like a tabletop. Speak in character in quotes; step out with (oog) when you want to negotiate. Each night the world is built a little further from what you said.

- Day 1 opens with one (oog) question: mirror mode or standard. In mirror mode a few of your god's smaller gifts are drawn from you as a person (never anything sensitive); in standard mode, nothing is. Then the world survey. Nineteen questions about the world you hope to land in. Answer what speaks to you, skip the rest, and reject any premise you like. Your answers are one voice among the gods falling with you; the world listens to all of them and grants none of them whole.
- Day 2, your god. Describe it freely: form, past, what it wants, what it can do. The DM asks, prices and rules. Every power comes with a drawback, and a weakness can buy something elsewhere. You end the day with a power card read back to you in plain words.
- Day 3, your people. Who they are, how many (about 5,000 by default), their customs, their skills. Ordinary culture is free; anything that gives a real edge is priced against a weakness.
- Day 4, 6:30am. The first morning story. Year 1 begins.

## A day of play

At 6:30am the morning story arrives: where you are and how you are, the state and mood of your people, one painting of the day's highlight, and a summary with hooks you can ask about. Then the day is yours. Play scenes, make god-scale decisions, ask about anything, muse aloud. Nothing resolves until you commit, and costs and odds are stated first. Ask for the map any time. You may request up to two more paintings a day.

Unplayed time is delegated to your advisors or scheduled ahead. Your god keeps doing what it last decided.

## The clock

- 1:30am: finish typing before this. The chat saves, the world turns overnight (your decisions, the other gods' decisions, and everything that follows from both), and a closing sequence is written for you.
- 6:30am: the morning story posts. If the world is still turning, a short notice says so and the story follows when done.
- When the morning stops at a moment held for you to play, the clock waits: the year does not turn past where your story stands, and you play the moment the next day. A day of play never covers more than one year.

The overnight scheduled task runs with automatic approval: whoever enables it sets "Automatically approve" in its settings, so no night waits for a go.

## Resuming in a new chat

Run `python3 tools/bundle.py <campaign-name>`. It writes a zip under `bundles/` with the engine, the tools and your campaign. Upload it to a new chat and say you are resuming. The record in the repo is the authority; the narrator's memory never is.

## Where things live

- `campaigns/<name>/player/`: your power card, appearance card, conduct profile, chronicle and saves.
- `campaigns/<name>/world/`: public facts about the world as you know them.
- `campaigns/<name>/years/`: each year's morning story.
- `images/out/`: the paintings.
- `engine/`: the rules and the design record, including the Change List.
- `tools/`: the scripts (dice, map, bundle).

## The one rule

Never open `SPOILERS_do_not_open/`. It holds the other gods, the hidden history and every mystery's answer. The game runs on the honor system, and it is only a game if you do not look.
