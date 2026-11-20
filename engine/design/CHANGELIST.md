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
