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

- ~~A heavier price that buys nothing is not taken.~~ A heavier price a god asks for is written as asked. (Section 12.6; the Keeper's sealed files)
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

## Build 6, after creation simulation run 05 (November 2026)

The findings are `tests/creation-sim/run-05/changes.md`; Michael's decisions are in `run-05/build-plan.md`. Reversed decisions:

- ~~A variety-table tie in the rubric is broken by an even-odds roll.~~ It is the Keeper's call, by what makes the more interesting game, reason logged, no die. (Michael, 2026-11-23, item 7; section 3.8)
- ~~A return is taken only on the standing rungs.~~ A god, player or NPC, may take a slower, costlier return than the rungs, priced by the DM or the Keeper; a return never takes a possession. (Michael, 2026-11-23, item 20; section 6.11, `engine/rules/powers.md`, the Keeper's sealed files)
- ~~A sealed request gets no answer the DM can see.~~ The Keeper writes one line per request in the sealed `S/player/requests-answered.md`, which the DM may read: "received and ruled", not how, unless the Keeper gives an explicit reason to tell more and the DM agrees: the reason as an indented line under the request's entry there, the DM's dated agreement beneath the request in `S/player/unsaid.md`, and only then the further line. (Michael, 2026-11-23, item 32; section 10.7)
- ~~A god that bends a default but proposes no edge gets no negotiation round.~~ It gets a round on the bent default alone, with the cost stated, and the change itself may be the price. (Michael, 2026-11-23, item 51; section 3.8a)
- ~~How far travelers arrive, and which season a cross-country event takes, are unsaid.~~ How each far traveler arrived is the Keeper's to decide, logged sealed; an event takes the season it was designed for at creation, or the one the world's actions determine. (Michael, 2026-11-23, item 67; sections 4.10, 8.1)
- ~~The campaign's timing file is public.~~ It is sealed, `S/state/timing.md`; nothing public carries night or stage times; the player sees in-game data such as the years passed. (Michael, 2026-11-23, item 74; section 12.2a)
- ~~A test run's first morning ends without the 1:30 line.~~ Every first morning closes with it, a test run's too. (Michael, 2026-11-23, item 78; section 3.3)
- ~~One sealed answer, the unsaid want, asked last.~~ Any reply on any creation day may carry a `SEALED:` part on any subject, written as it arrives under a heading for its kind. (Items 14, 43, 64; section 10.7)
- ~~A name the player gave at creation shows on the map from the first morning.~~ It shows only once heard in play, or the (oog) map line says why it shows; the landing sheet draws a seen line only as far as it was seen. (Item 76; `engine/rules/map.md` 2.1, 4.2)
- ~~Whether the player learns what a return took is unsettled.~~ The player is told in (oog) after a return; the god in the fiction does not know. (Item 22; `engine/rules/powers.md`)
- ~~Knacks never grow.~~ A knack grows only by use of the skills related to it, never by any other trigger, and never into a power; its use is tracked in the sealed growth file. (Michael, 2026-11-24, item 68; section 6.5, `engine/rules/powers.md` section 4)

## Build 7, after creation simulation and play test run 06 (November 2026)

The findings are `tests/creation-sim/run-06/changes.md`; Michael's decisions are in its closing section and in `run-06/build-plan.md` (approved 2026-11-25, 21:16 Pacific). Reversed decisions:

- ~~A scene the player prepares for, and a held moment with a world figure whose words are the Keeper's, are resolved in the night and told in the morning (ledger L-0038).~~ Every held moment, prepared or not, is held at its opening moment and played live on the next play day. The Keeper writes the scene's facts, its parameters (what each figure wants, what it will and will not do or accept, its stance and opening words, the ranges outcomes fall in) and the reasons for them, the reasons for the DM only, who may share them, lie about them in a figure's voice, or not mention them. The DM plays the scene; a played scene holds, and the Keeper accepts the result and never unmakes it. (Michael, 2026-11-25, decision 1, items 81, 94; DESIGN 10.5a)
- ~~The morning stops at the first held moment, tells the rest of the year as it stood, and an event added to a told stretch comes out unless play gives it a cause (ledger L-0046, item 101).~~ The morning tells the year only up to the first held moment. The night after it is played works the played answer in, and the next morning tells the rest. A held moment keeps its own date, and the decisions file carries what was played under the year it was played in. Item 82 is resolved by this, and item 101 falls away. (Michael, 2026-11-25, decision 1, items 82, 90, 101; DESIGN 10.5a, `engine/night/night-turn.md`, `engine/rules/morning-story.md`, `engine/rules/encounters.md`)
- ~~Growth is felt in play, and the release tells the god what it feels of an attempt each year.~~ Powers feel limited to their given capabilities; a skill or power progresses slowly, by being done a lot and by pushing at new boundaries, gods a bit faster than mortals; nothing prevents an attempt. No hint of any kind about a change in powers reaches any god, player or NPC, until at least year 70, and NPC gods are not prompted to grow. A hidden power surfaces when its condition is met, and the Keeper sets the conditions so they are rarely met in the early years. (Michael, 2026-11-25, decision 2, item 99; DESIGN 3.9, 6.5, 6.8, `engine/rules/powers.md`)
- ~~Whether a clue is found is left to the search roll alone.~~ A thing that came about in the game is found by a roll with modifiers, weighed by the evidence, Bayesian fashion; a thing the Keeper placed is there. (Michael, 2026-11-25, decision 3; DESIGN 8.7, `engine/rules/encounters.md`, `engine/roles/keeper.md`)
- ~~An absent god's people may make its call for it.~~ A town acts on the god's behalf only where the god expressed that intention or obviously assumed it; with no way to reach the god, the town has no answer from it, the price of not giving explicit permission; the civ agent may decide that someone in the town took it upon themselves to make the call. (Michael, 2026-11-25, decision 4; DESIGN 10.6, `engine/roles/civ.md`, `engine/rules/encounters.md`)
- ~~Silence from an absent god may be read as an answer.~~ A question put to an absent god meets silence and stays pending unless the god noted otherwise (conduct profile, standing words). People know only what happened. (Michael, 2026-11-25, decision 5; DESIGN 10.6, 12.9)
- ~~Each country opens its year in its own season, and a cross-country event takes the season it was designed for (DESIGN 8.1; ledger L-0043).~~ All the world goes through the seasons at the same time. Every god, player and NPC, votes its top two months to wake in the Day 1 survey (question 3); the Keeper decides the waking month on Night 1 and logs why. (Michael, 2026-11-25, decision 6; DESIGN 8.1, `engine/creation/day1-world-survey.md`, `engine/night/creation-nights.md`)
- ~~The player's people's public files carry what their mortals did out of the god's sight.~~ Sealed: the public files hold only what the god could witness or be told; the rest goes in the people's sealed files, and the asking and telling of sealed things are themselves sealed. (Michael, 2026-11-25, decision 7, items 76, 100; DESIGN 12.2, `engine/roles/civ.md`)
- ~~A sealed part is never acted on.~~ An act the god says it does is done, wherever it is said, a sealed note included. An ordinary habit (checking a pocket) is conduct, carried out and never priced. Wants and fears stay feelings. (Michael, 2026-11-25, decision 8; DESIGN 10.7, `engine/creation/day2-the-god.md`, `engine/roles/dm.md`)
- ~~A mortal knack is priced by the DM at the table, at the worker's own cost alone when it is one worker (item 33 as proposed).~~ Giving a power to a mortal costs the god something. The Keeper prices it; one that dies with the person is less powerful and costs less. The DM records the player's wish and the Keeper prices it at night, put back to the player as a cost. (Michael, 2026-11-25, decision 9, item 33; DESIGN 3.16a, `engine/rules/powers.md`, `engine/creation/day3-the-people.md`)
- ~~An NPC god's release offers the DM's options as worked examples with their price.~~ An NPC god's release says nothing about prices, trades or weaknesses and gives no example; the god proposes its powers, and every price is found in the negotiation with that god, as with the player. (Michael, 2026-11-24, item 24; DESIGN 3.8a)
- ~~The DM rolls small world facts in a scene itself, with odds stated after.~~ World facts come from the Keeper's day sheet in the DM release; a fact not on it is rolled with odds stated before, logged for the Keeper. (Michael, 2026-11-24, item 60; DESIGN 10.5)
- ~~Unplayed time answers every ask by silence.~~ A simple ask is answered by the conduct profile's stated temper where it speaks, logged as conduct, not as a decision. (Michael, 2026-11-24, item 69; DESIGN 10.6)
- ~~The DM's open rolls and the Keeper's share one log and one id series.~~ The DM's open rolls stay in the public `state/rolls.jsonl`, with their own id prefix, and the checks are fixed to allow them; the Keeper's rolls are sealed. (Michael, 2026-11-24, item 70; DESIGN 12.6)
- ~~The checker runs after pass two, before the releases and the morning story.~~ It runs once over everything the night wrote, after the morning story, with a quick script check after pass two. (Item 73; DESIGN 5.8, `engine/night/night-turn.md`)
- ~~The DM writes the closing sequence at 1:30.~~ The night turn writes it from the resolved year. (Item 63; `engine/rules/morning-story.md`)
- ~~The Keeper, resolving the year, may overrule a DM roll's outcome by the sealed factors (build 5), and in build 7 not in a played held scene.~~ The Keeper never changes the result of a roll the DM made in play. Luck stays and works only through the odds the Keeper sets: its own rolls, and the odds and ranges it writes in advance for the DM. (Michael, 2026-11-25, 22:03; DESIGN 12.6, `engine/roles/dm.md`, `keeper.md`, `checker.md`, `engine/night/night-turn.md`)
- ~~A search for a thing the Keeper placed is always rolled, or always found.~~ With no pressure or race it works out, with no roll; under pressure or in a race it is rolled. (Michael, 2026-11-25, 21:57; DESIGN 8.7, `engine/rules/encounters.md`)
- ~~An ask the god promised to answer later is always held (a Year 2 Keeper ruling).~~ It is pending by default, and held only when it is a crucial live scene. (Michael, 2026-11-25, 22:00; DESIGN 12.9, `engine/rules/encounters.md`)
- ~~Knack growth by fixed figures of years and uses.~~ No fixed figures: the Keeper judges by how much and how often the skill is used and how intently the god pushes it, and errs slow. (Michael, 2026-11-25, 22:03; DESIGN 6.5, `engine/rules/powers.md`)
