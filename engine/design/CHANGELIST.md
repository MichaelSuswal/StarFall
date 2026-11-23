# StarFall Change List

Permanent record of design decisions that were reversed or revised. Resolved items are struck through and kept.

## Design conversation, November 2026

- ~~NPC gods: 6 to 12, rolled at random.~~ Now 7, each with a civilization. (Section 5)
- ~~Morning status bar showing year, season, avatar location and condition.~~ Replaced by the return sequence, an opening paragraph carrying year, season, the people's state and mood, and the avatar's position and condition. (Section 5)
- ~~Godless civilizations each get their own civ agent.~~ The Keeper runs all godless peoples. (Section 5)
- ~~The player's god also gets a hidden Keeper trait.~~ Only NPC gods get a Keeper trait. (Section 3)
- ~~NPC gods learn their Keeper trait on Day 1 of play.~~ They know it from arrival. (Section 3)
- ~~Hidden powers known on arrival.~~ The two hidden powers are discovered through play. (Section 3)
- ~~Company lean +35 toward gathering.~~ +25, capped at 100. (Section 3)
- ~~The world turn runs inside the play chat.~~ It runs in a separate overnight session that reads only the repo. (Section 2)
- ~~Save after each scene.~~ Rolling saves during play; everything saved at 1:30am. (Section 2)
- ~~Telegram as the platform.~~ Claude plus the StarFall repository. (Section 2)
- ~~290 years after the original game.~~ Each campaign starts clean; nothing carries over. (Sections 1, 9)
- ~~Lore fixes: add a second wrong explanation beside a true sighting; add a late surfacing to rescue a quiet mystery line.~~ Rejected as guiding. Clues are never held back and the world never guides toward or away from a conclusion. (Mystery standard rules 8 to 10)
- ~~Survey questions 3, 11, 13 as first drafted.~~ Reworded; question 13 split into 13 and 14; the survey assumes the god will rule a land and a people. (Section 3)
- ~~Image generator undecided; Gemini considered.~~ OpenAI `chatgpt-image-latest` via a GitHub job. (Section 14)
- ~~Deep lore draft v1.~~ Archived as too obvious; v2 written from scratch under the revised mystery standard. (Spoiler folder)

## Build 2, after creation simulation run 01 (November 2026)

The full list of 100 findings and proposals is `tests/creation-sim/run-01/changes.md`. Reversed decisions:

- ~~Oaths between gods bind or not per campaign, by survey vote (question 16).~~ Oaths are not a world rule; a promise is worth what the god is worth. Question 16 now asks about bodies. (Sections 3, 7)
- ~~God-sense fixed: every god senses that others exist and all recognize each other's presence.~~ God-sense is set per campaign by the survey vote alone, and given to the player before Day 2. (Sections 1, 7)
- ~~The star is rolled on Night 3 and the magic level stays provisional until then.~~ The star is rolled on Night 1, before the blend. (Section 3)
- ~~The Keeper runs the lock checklist and writes LOCKED.md; the version is a git tag.~~ The continuity checker runs the lock and writes LOCKED.md with the commit id. No tag. (Section 15)
- ~~Night 3 is one sitting.~~ Two sittings back to back, 3a peoples and map, 3b history, mysteries and schedule. (Sections 3, 15)
- ~~The world turns every night; a missing save still turns the year on the god's last course.~~ The world turns only on a day the player posted; otherwise it waits. (Sections 1, 2, 5)
- ~~Underground layers each painted at creation.~~ One underground sheet only if the world has one; otherwise none. (Section 11)
- ~~Map rules assumed a sheet of about 256 miles with regions 20 to 60 miles wide.~~ One continent per sheet at the scale of a map of Middle-earth. (Section 11)
- ~~Hidden powers written on the NPC god's own card and the secret backstory in its own folder.~~ Both live in a sealed sibling folder the god's agent never receives. (Section 3)
- ~~NPC god folders labeled g1 to g7.~~ Labeled by domain, with no number. (Section 3)
- ~~Map painting requests public.~~ Sealed. (Sections 11, 14)
- ~~The permission exception covers only the two scheduled turns.~~ It also covers a campaign or test run once Michael has started it, for the files each release names. (CLAUDE.md)

## Build 3, after creation simulation run 02 (November 2026)

The findings are `tests/creation-sim/run-02/changes.md`. Reversed decisions:

- ~~A people with a town, hierarchy and advisors is assumed, not forced, and refusing any part is one option among several.~~ Leading a people is the stated premise, from the descent on; the DM opens Day 3 from a seat and helpers, and refusing is a choice the player argues for and pays for. (Sections 3.0, 3.11)
- ~~How an NPC god rules and is worshipped is left to the agent.~~ Set by rule and worship leans from its rolls; every NPC god starts with helpers. (Section 3.8)
- ~~A people larger than the default is a priced edge.~~ Its costs are practical and come from the world, argued case by case. (Section 3.11)
- ~~The Keeper may name places the player left unnamed.~~ It uses placeholders until play names them. (Section 3.11a)
- ~~An NPC may share the player's theme.~~ A matching NPC domain is rerolled on Night 1. (Section 3.8)
- ~~The leak scan guesses sealed names from prose.~~ The Keeper keeps a sealed-terms list; the scan reads it. (Section 12.2)

## Build 4, after creation simulation run 03 (November 2026)

The findings are `tests/creation-sim/run-03/changes.md`; Michael's decisions are in `run-03/build-plan.md`. Reversed decisions:

- ~~A heavier price that buys nothing is not taken.~~ A heavier price taken willingly is written as asked and buys nothing on the card. (Section 12.6; the Keeper's sealed files)
- ~~The technology line gives the world's starting level only.~~ The starting level is not a ceiling; a god may introduce what it knows, built in play from what the player knows or looks up. (Section 4.7)
- ~~A name a god gives as a wish counts as given.~~ A place keeps its name; other names are aliases, and a name changes only when the place's people come to use it. (Section 3.11a)
- ~~Travel over mixed ground priced by the ground the straight line crosses, or by a road's length.~~ Priced by route and means, segment by segment. (Section 10.1)
- ~~The continent at 2 to 4 miles per pixel (2,000 to 4,000 miles across the sheet).~~ At least 600 miles across at its narrowest and about 1,000 on average; the lock checks it. (Section 11.1a)
- ~~The player's map redrawn on every request.~~ Redrawn only when the map knowledge changed. (Section 11.6)
- ~~The god's unsaid wants kept in the open conduct profile.~~ Sealed in `S/player/unsaid.md`, the DM's one sealed file, and confirmed with the player before acted on. (Section 10.7)
- ~~Refusing a default counts toward an edge by judgment.~~ One step in the god's favor per default refused, in the one price it bears on. (Section 3.11)
- ~~Michael's in-run rulings relayed by the orchestrator in any file.~~ Recorded only in the sealed `S/rulings.md`, quoted with the time. (Section 2.7a, CLAUDE.md)
- ~~Only the files a release names may be touched inside a run.~~ A pull is always allowed. (CLAUDE.md)

## Build 5, after creation simulation run 04 (November 2026)

The findings are `tests/creation-sim/run-04/changes.md`, with run 03 item 94 (mirror mode); Michael's decisions are in `run-04/build-plan.md`. Reversed decisions:

- ~~The game never mines the player's chat history.~~ Mirror mode, opt-in at the start of Day 1, draws the god's hidden powers and two or three small knacks from the player as a person (chat history and memory, or a short survey), never anything sensitive; standard mode draws nothing. (Sections 1.1, 3.4c, 3.9)
- ~~A creation run starts on Michael's go, and the lock pauses on a flag only Michael can clear.~~ The player starts a campaign; no step waits on Michael; rulings the files do not settle are made by the Keeper or the checker by the judgment order and logged for review; the lock never pauses. Engine and design changes and spending beyond `images.md` still need the owner. (Sections 2.7a, 15.2, 15.5, CLAUDE.md)
- ~~The sealed factors apply only to rolls the Keeper makes.~~ The DM rolls in the open with stated odds; the Keeper, resolving the year, may overrule a DM roll's outcome by the sealed factors, logged sealed. (Section 12.6)
- ~~The unsaid want is asked and answered at the open table and moved to the sealed file after.~~ It is asked last and answered in a separate `SEALED:` reply written straight to the sealed file. (Section 10.7)
- ~~The people's knowledge of the land is kept in their record and reaches the DM with the first release.~~ A public, DM-readable `civs/<people>/knowledge.md`, separate from the god's map knowledge. (Section 11.4)
- ~~An underground the world has may be traced as data only, after the paint, and the data follows the paint.~~ Night 1 decides whether there is an underground; if there is, it is written into `map.json` before any painting and the data rules below ground. (Section 11.2)
- ~~One step in the god's favor per default refused, with what a step is worth left unsaid.~~ The DM names the edge each refusal bears on; one step drops one weakness. (Section 3.11)
- ~~Only the player's god gets small innate knacks.~~ Every god gets two or three: an NPC god's drawn from its own sealed backstory and written on Night 2 in its sealed folder, the player's as before; all sealed, found only in play, counted toward balance, named in no public file, and checked at the lock. (Michael, 2026-11-22, decision 7; section 3.9)
- ~~A sealed term the player says in the open table talk comes off the list, whatever it is.~~ The sealed factors' names never come off the sealed list and are never exempted by the scan; the creation transcripts, the player's own words kept verbatim, are not scanned for them, and every other public file is. (Michael, 2026-11-22, decision 8)
- ~~A tie in the survey blend is settled by an even-odds roll, and a quarter step is rounded.~~ Every tie in the survey blend (an even vote, a half or quarter median, any even-odds tie) is decided by the Keeper by what makes the more interesting game, with its reason logged; no die. (Michael, 2026-11-22, decision 9; section 3.19)
