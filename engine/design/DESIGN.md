# StarFall: Design Record (pre-build)

The final design decisions for StarFall, gathered from the design conversation (November 2026). This is the source the engine is built from. Where this file and the conversation disagree, this file wins unless Michael says otherwise. Reversed decisions are kept in CHANGELIST.md.

Hidden material (deep lore, the mystery standard, the NPC god rubric, Keeper notes) lives in `SPOILERS_do_not_open/` and is referenced here, not repeated.

---

## 1. Vision and scope

1. A single-player god game built for many kinds of god. The game bends toward whoever is created, using the intake conversation only. It does not mine the player's chat history.
2. Goals are a mix. The world has unifying events, and any god may ignore them.
3. Open chronicle. The world is planned around several possible big events, and play shows which happen. A god stops when its purpose is reached, becomes impossible, or the world ends. A player who sees no way out may end the campaign; if a way out exists, the DM offers a clue first.
4. Seven NPC gods, each run by its own agent so they are independent and not designed to complement each other. Players never learn how many gods arrived.
5. All gods arrive at the same moment, most from another plane. None has walls or an abode yet. Each lands in country suited to it. Every god knows that others like it came down when it did, and nothing more; what else a god can sense of another is god-sense, set per campaign (7.2).
6. Scenes are the heart of the game: one to three played live each year, plus god-scale decisions. Seedings and similar acts are usually played as scenes. The original's wolf siege (several nights played in detail inside one year) is the model for scene time.
7. The player may stay in the world all year and keep working.
8. Latitude is earned. A god can do things that would be hard for its form, but nothing over the top, and rewards come from work in the world.
9. The world turns each night: the player's actions, the NPC gods' actions, and the knock-on effects in both directions.
10. The world changes only through events inside it. Nothing may turn out to have "always" been there.
11. Freedom. Every god and kingdom acts as it wishes. Consequences reach whoever notices; credit and blame depend on who noticed. Characters change because of what happens to them.
12. One year per real day, on the days the player plays. The world turns at a time each player chooses (Michael: 1:30am Pacific), and the morning story arrives at 6:30am. The world turns only on a day the player posted in the game; reading does not count. On a day with no post the world holds, nothing happens, and the morning carries one (oog) line saying the world waited.
13. Version 0.1 is character creation plus the first five years. Later versions iterate, as with Ashmoor and The Quiet List.

## 2. Engine conventions

1. The engine is a small set of markdown files read by the agents, plus small scripts wherever something must be exact: dice and contested rolls, the map, the pace table, consistency checks, the painting job. All files can be bundled and downloaded to carry into a new chat.
2. Home: the private GitHub repository MichaelSuswal/StarFall.
3. Secrets: honor system. Hidden material lives in `SPOILERS_do_not_open/`, with a warning at the top of every file.
4. Carried over from the other games: the (oog) prefix for out-of-game talk; the Change List as a permanent record, resolved items struck through; version bumps with migration files.
5. Play happens in one long chat. It can be retired at any time by loading the bundle into a new chat.
6. Authority, in order: what the player points to in the chat; then the repo; then the narrator's memory, which is never an authority on its own. Every fix goes into a corrections log with date, what changed and the proof. Anything built on a bad fact is reworked; the repo's history shows what it touched.
7. Saving: the narrator writes rolling saves to the repo during play. The player must finish typing by 1:30am. At 1:30 a scheduled message wakes the play chat, which saves everything and, if the player posted that day, writes the decisions file. A separate overnight session, on its own schedule at 1:45, reads only the repo: if the decisions file is there it turns the year; if not, it writes the waited note and stops. Each night's year is committed as its own version. The three creation nights run in the same overnight session, chosen by the campaign clock (`engine/night/creation-nights.md`).
7a. Permission inside a run: once the player has started a campaign, its days and nights run under this design, and every agent in the run takes its release as the go for the files the release names (CLAUDE.md).
8. Morning: at 6:30 the morning story posts. If the world is still turning, a short notice says so and the story follows when done.
9. Rules: rulings are negotiated, then binding, and change only when the player brings a better argument. The DM proposes rule changes in (oog), explaining what changes and what it affects; nothing changes without the player's yes, and every change goes into the Change List. The world's geography, structures and event schedule are set before play and change only through actors in the world.

## 3. The Between: creation

0. The premise. A god comes down to lead a people: to find or gather them, to build, to rule, and to spread. The descent in The Between says so, every god release says so, and Day 3 opens from it. It is the expected course of every god, player and NPC. A player may push back, and the pushback is recorded in `player/rejected-premises.md` and honored; the game then remembers out loud that this god does not play the usual way. The DM does not offer alternatives to the premise unasked.

1. Creation runs like a tabletop. In-fiction by default, the player's in-character speech in quotes. The player may step out with (oog) to negotiate. The DM decides; the player may appeal.
2. The opening is a descent: the god is falling from wherever it was into a world that does not know it yet. This is The Between.
3. Three days, one part per day:
   - Day 1, the world survey. Night 1: the Keeper rolls the NPC gods and creates their agents; each answers the same survey.
   - Day 2, the player's god. Night 2: each NPC god creates itself and negotiates its powers with the Keeper. The Keeper assigns each NPC its Keeper trait, gives every god its two hidden powers, and writes the secret rest of every backstory.
   - Day 3, the player's people. Night 3, in two sittings back to back: 3a, the NPC peoples, the placement plan, the paintings, the tracing and the starting map knowledge; 3b, the deep history, the mysteries, the event schedule, the cast and the first morning's inputs. Then the continuity checker runs the lock checklist and locks the world.
   - Day 4, 6:30am: the first morning story. Year 1 begins.
   - Each night is a scheduled overnight session, picked by the campaign clock (`status: creation`, `creation_night`). Guide: `engine/night/creation-nights.md`.
4. The world survey is in `engine/creation/day1-world-survey.md` (19 questions). The questions assume the god will rule a land and a people. A player may reject a premise (refuse its assumption) or bend it (answer outside the range offered) and answer their own way; the game never punishes it, and the DM records both kinds in `player/rejected-premises.md`, one section per day. An answer that asks not to be told something is honored and never turned into a follow-up. When a rejection leaves a gap, the Keeper writes follow-ups for the DM to put to the player the next day; the DM may ask a clarifying question in the moment. Days 2 and 3 add follow-up questions generated from what the previous night built.
4a. Given and discovered. The player is never told which wishes the world kept, and nothing is reported as a vote. What is innate to a god is given before Day 2, in `player/world-rules.md`: god-sense as set, how many bodies a god may have, and the pricing terms for mortal magic (it is simple and it costs the worker), never how common it is. The god's own power limits are settled at the Day 2 table. What is learned from the world is discovered in play: the prevalence and feel of magic, how much gods stand out, the strangeness of the wild, the scarcities.
4b. Day 1 closes like Days 2 and 3: the answers are written verbatim to `player/survey-day1.md`, premises to `player/rejected-premises.md`, and one line closes the day in the voice of The Between.
5. The world's name is set by the Keeper. Different peoples call it different things, even within one language, and new names can arise.
6. Backstory: the player sketches the outline (who the god was, what it lost). The DM secretly fills in the rest and ties it to where the gods came from. The avatar arrives with its past foggy.
7. The player's god is negotiated freely, as in the original. It has no rolled leans; it is what the human playing it is. A weakness can buy an improvement elsewhere.
8. NPC gods are built by the rubric in `SPOILERS_do_not_open/keeper/npc-god-rubric.md`: ten leans rolled 1 to 100 (Company +25 toward gathering, capped at 100), a mythic archetype seed from world mythologies, a domain, a form, a virtue and a flaw, a wound, a voice, two traits chosen by the god after its rolls, and one Keeper trait it knows from arrival. No two gods in a campaign share a seed or a domain. The leans also set how hard a god bargains for its powers, the size and shape of the people it hopes for, how it rules (the rule lean: from god-king with a court and priesthood, through priest-king, warlord, merchant-prince, sacred monarch behind a court, council of elders or chieftains, to a lone god with no one, which only an extreme roll gives), and how it is worshipped (the worship lean: from a state cult with temples and tithes, through a priesthood, to local shrines, to none), so seven gods do not come out alike. Each god builds within its results and gives reasons to depart from them. A god's folder is labeled by its domain, never by a number, so no god can count the others. An NPC domain that matches what the player has said their god is about is rerolled on Night 1, so the player's god stays its own. A test campaign may force lean results through the sealed `S/state/test-overrides.md`, logged; the rubric itself never changes for a test.
8a. NPC gods negotiate for real. The Keeper's releases offer every option once and neutrally, with no steer toward any choice, and offer the NPC gods every option the player was offered. A god gives reasons for what it asks; the Keeper counter-argues; at most three rounds: draft text with choices, counter and final text, confirmation. Accepting everything is a choice the god is told it has, not the default.
9. Every god, player and NPC, gets two hidden powers fitted to its backstory: one cool, one minor, both weaker than its main power, discovered through play. The player's god has no Keeper trait. Hidden powers, secret backstories, the ceiling and the growth file live in a sealed folder the god's own agent never receives (`SPOILERS_do_not_open/campaigns/<name>/gods-sealed/<god>/`, and `S/player/` for the player).
10. The DM keeps the gods at roughly equal power, as far as it can foresee, on a rough 1 to 10 weight per god. Loopholes belong to whoever finds them.
11. The people: a civilization with a town or city, about 5,000 strong, with a seat and helpers who run things in the god's absence, is the default and the DM opens from it. The god talks about the people it will lead; the actual people is negotiated. A smaller people, no town, or no helpers are allowed, and are choices the player argues for; refusing a default counts toward pricing the people's edges. A larger people is not a priced edge; its costs are practical and come from the world, argued case by case. With no helpers, unplayed time runs on standing conduct alone, no one acts for the god while it is away, and its people drift.
11b. Helpers. Every people's record carries a Helpers section: the offices that run things when the god is absent and how orders travel. A god may refuse its helpers, dismiss any of them, or never meet or employ them; the refusal or dismissal is recorded with its date, and dismissed helpers are never forced back on the god. New loyal helpers may come later through play. This holds for the player's god and for every NPC god alike.
11a. The player sets who a mortal is, never what that mortal will do. A player's description of the land or its past is a wish or the people's belief, never a fact, until the Keeper places it. Naming a home does not place it. The player names its own people and their home; the Keeper names everything else, and never names what the player left for play: for its own records it uses a placeholder ("unnamed house 1", "unnamed location") until play names the thing.
12. Day 2 is mainly a discussion. The player describes the god freely; the DM follows, asks, prices and rules, then fills any gaps from its hidden checklist before the day closes. Guide: `engine/creation/day2-the-god.md`.
13. How many bodies a god may have is set per campaign through the surveys (Day 1 question 16), and given to the player before Day 2.
14. There is no fixed number of powers. A god may have one enormous power or several smaller ones; the DM balances total power across gods from the interviews, like a budget whose size is not set in advance.
15. Gods are roughly balanced but not exactly. Some campaigns have a noticeably stronger god, and the world's politics deal with it.
16. Day 3, the people: ordinary culture, customs and skills are described. Anything giving a real edge over other peoples (a rare skill, unusual longevity) is priced against a weakness. Guide: `engine/creation/day3-the-people.md`.
17. How a god meets its people (already there, waiting for it, or arrived with it) comes from the world's history and the player together, worked out in the Day 3 negotiation and reconciled with the deep history.
18. Follow-up questions on Days 2 and 3 are woven into the conversation and kept few. The DM may switch to (oog) when needed.
19. Survey answers carry equal weight: the player is one voice in eight. Every answer is blended into one world with one set of rules; special places may exist, and one rule may be unevenly spread (magic rare overall, common in a few valleys), but no wish makes a different rule hold in one place. Keeper notes: `SPOILERS_do_not_open/keeper/survey-keeper-notes.md`.
20. The star is rolled on Night 1, before the blend, so the magic level and everything else the star fixes are final before Day 2.
21. Creation records what the player agrees. A power's frozen text is the agreed text read back at the close, with the player's first wording kept under Limits as intent. Rulings made at the Day 2 or Day 3 table are marked "settled at creation" on the card; the Keeper copies each into the sealed ledger that night and writes the id back. A people's edge that changes the god's powers goes on the power card as a dated Day 3 entry.

## 4. The world

1. A new world every campaign, built in stages over the three creation nights from every god's input. It is fairly set from Day 4; after that every change comes from play.
2. The world must have driving forces: things to discover, alliances to make, and looming events whose course shifts with the gods' behavior. A paperwork war can be a thread, never a main theme.
3. The reasons behind every mystery are set at creation and never change.
4. The setting is an infinite plane, endless in space and time, under glowing blue "stars." What they are is sealed deep lore, constant across campaigns. The lore is its own; it is neither the original Telegram game's story nor Michael's 2012 StarFall story.
5. Each campaign is a different star with its own properties. Nearby stars are similar and distant ones differ more. Other starfalls, and stars still to fall, are placed around the starting lands by roll in the sealed map's plane section: usually very far apart, with a near pair a rare roll. They are data only and are never painted. Nothing beyond the edge of the sheet is drawn; the edges stay in fog.
6. A campaign region is a continent, painted on one sheet in the manner of a map of Middle-earth: less detail at larger scale, topography and the names of areas, towns as points.
7. Technology starts at about the original's level: before the medieval era, no steel forges. Peoples who walked from a dying star may bring more.
8. Magic: its level is set by the star through the surveys, with the DM deciding. There is always some and it is never everywhere; under high-magic stars mortal magic stays simple. A god shares its people's magic in its own way. God powers are innate and separate from magic, like eyes or legs.
9. Peoples without a god: claimed and unclaimed land are balanced, varying by star. Every people has a real backstory and may or may not tie into the great events.
10. Humans are the default. A god may lead another kind of people, and non-human peoples can come from other stars.
11. God-kings are the default civilization, with courts, advisors and cities fully supported. Odd builds (a fox god of loners, a clan of 100 warriors) are equally possible.

## 5. The player's people and the agents

1. Most gods lead through advisors, instructions and counts. The fox's seeing, seeding and wordless dream were the fox's own way, not a system.
2. A god can turn its 5,000 away to keep a small clan, or grow through births and immigration, and finds followers in its own way.
3. Hierarchy is assumed: advisors who carry out the god's wishes come built in. A player may reject them, and the game remembers out loud that this god plays differently.
4. Everything is tracked underneath: population, stores, treasure, trade, mood. The player decides what gets highlighted by what they ask about.
5. The morning, for every player:
   - A return sequence: an opening paragraph carrying the year, the season (each year opens in the same season), the people's state and mood, and the avatar's position and condition.
   - The day's painting, of a highlight: mysterious, epic, or showing the god's mark on the world.
   - A digestible summary, longer in eventful years, with hooks the player can ask to hear more about.
   - Then free play.
   - At 1:30am, a closing sequence as the world turns, unique to each player.
6. A god's style shapes its people. A harsh god may drive people away but gain production for a while; a god who draws talent and art may be poorly defended. Each people forms its own feelings, stories, lore and warnings about its god and its chosen kings.
7. Agents:
   - The DM: runs the player's day.
   - One agent per NPC god (seven).
   - One civ agent per god-led people, the player's included, all with the same will.
   - The Keeper: runs the world and all godless peoples (three to five godless civilizations per campaign), and rules on powers.
   - The continuity checker: its own agent, reads everything including spoilers, writes only flags and the lock (sealed flags, a one-line public note, `LOCKED.md`), and flags problems back to the Keeper.
8. The night, from 1:30:
   1. The play chat saves. If the player posted that day, the DM writes the decisions file; if not, the overnight session finds no decisions file, writes the waited note, and the year does not turn.
   2. The player's decisions go to the player's civ agent; each NPC god decides its year and hands its decisions to its own civ agent.
   3. Keeper pass one sets the year's world events and gives each civ what it would experience.
   4. Every civ agent works out how its people act and react.
   5. Keeper pass two resolves everything together. Contests are settled by stated odds and logged rolls.
   6. The continuity checker runs, including the failures checklist.
   7. Each agent receives only what it could know.
   8. The DM writes the morning story from what the player's god could know.
9. Musings go to the DM as sentiment. They shape how the DM talks with the player and can lead to real decisions; only decisions are handed off. The avatar keeps doing what it last decided for the rest of the year.
10. During the day, NPC gods speak through their own agents when the player meets them.

## 6. Powers

1. The main edge cases of each power are settled on Day 2. Every later ruling is added to the power card as permanent precedent.
2. Every power comes with a drawback. Turning drawbacks into advantages and finding unexpected uses are encouraged.
3. Rulings are argued as cases arise. The DM argues the player's case to the Keeper genuinely; the Keeper rules, in real time when it matters to the story. Judgment order: fairness, above all to the player's original intent; then fit with the power as first written; then balance.
4. The DM may trim a power slightly to keep the game fun. Countermeasures must be genuine and earned inside the world.
5. Tiers of growth:
   - Craft is how time is spent; its reward is what that time produces.
   - God powers are innate, separate from craft and magic.
   - New powers and big upgrades need a trigger in the world (a mentor, a realization, an example witnessed), years of practice with failures, real risk, a new drawback, and a ceiling.
   - Small refinements need time, practice and risk.
6. NPC gods negotiate their powers with the Keeper on Night 2, keep power cards in the same format in the spoiler folder, grow under the same rules, and can find loopholes.
7. The ceiling on growth is secret deep lore, rolled within a small range per world. Power growth stays rare and modest; the status quo holds.
8. Growth is tracked in secret. The Keeper keeps a sealed growth file per god (`S/player/growth.md` for the player, `S/gods-sealed/<god>/growth.md` for each NPC): for each power, the triggers met, the years practiced, the failures, the near misses, and the tier reached. The night turn logs progress only when something in the world earns it, never on a schedule. The player learns of growth only through what the god feels, woven into the morning story, and the public card changes only when a tier actually lands, as a dated entry. The card's Growth line says only that growth is possible.
9. The power card has room for what Day 2 produces: a Definitions block under Form for terms several powers rely on, a Things carried subsection for anything a god carries that does more than an ordinary object (which is a power and is priced), and a Weaknesses taken block recording each weakness in full with what it bought. An ability bought by a trade is a power with status `main`, with the trade recorded both ways.
10. Powers that reveal information, about the past or at long range, are priced against the mystery standard: they may show effects, never mechanisms, and never a central measurement of the epic. A drawback must be something the god would notice losing. A memory-loss drawback on an NPC god is enacted by the Keeper removing an item from the god's record.

## 7. NPC gods

1. Messages travel by messenger or in person, take real time, and mostly arrive. Only the world can stop one (interception, storm, bad roads). The engine never loses a message, and every message is logged with what happened to it.
2. God-sense is decided per campaign by the Day 1 survey vote (question 15) and nothing else; the sealed lore does not fix it. It is given to the player before Day 2. Whatever the vote sets, god-sense is never a tally: a god feels direction, nearness or weight, never a count, so the number of gods (1.4) stays unknown however the sense is set. Michael's preference, as one voice in eight: gods sense the presence of other gods, and perhaps other immortals.
3. Gods can speak any mortal language unless the Keeper keeps some a mystery. The god-tongue is understood only by immortals, perhaps only those from the same plane. Whether gods recognize each other's presence is god-sense, as set for the campaign; they recognize the god-tongue when they hear it.
4. No shared meeting place.
5. Placement: gods are spaced evenly. The Keeper lays out the land after creation. Each god's country suits it, with real topography that shifts over distance; there is a lot of space between civilizations, and borders emerge where the land changes.
6. Every god arrives expecting to find a people to lead, without knowing why. NPC gods form goals once they see their land, pursue them, change them as their peoples grow, and can be swayed by argument or sway others.
7. Oaths are not a rule of the world. A promise between gods is worth what the god who gave it is worth; nothing in the world enforces it or punishes breaking it. Consequences come from those who remember. A god may still bind itself by its own nature, as a weakness bought on Day 2.
8. Gods cannot die. They can be wounded, imprisoned, exiled, cut off from their people, or forgotten.
9. Each NPC god keeps its own record of every other god, built only from what it saw, was told or worked out. Beliefs can be wrong. Deception is allowed for everyone; consequences come from whoever was deceived, once they find out.

## 8. Story architecture

1. Natural events run on a fixed clock no one controls. Other events are triggered by what gods and peoples do, and triggered events can speed up, delay or redirect clocked ones.
2. Signs of every event are in the world, and the DM never points at them. They reach a god through who noticed, or through the god's own senses. Strange reports from several people at once are a typical tell.
3. Lead time fits the event: days for a storm, little for a comet. An event can itself be the sign of a bigger one.
4. Fully free. An NPC god can complete what the player is pursuing. Gods chasing the same goal usually learn of each other along the way.
5. No forced convergence. Gods are never herded to one place for a finale. No paths or secret ways are invented for the plot.
6. The distance between gods makes the opening quiet. The clock and the triggers decide everything, and random events are weighted down in the first seven years.
7. All mysteries follow the mystery standard in `SPOILERS_do_not_open/keeper/mystery-standard.md` (16 rules), including: layered mysteries by time scale and power (about one epic, several long, many short); clues never held back; no guiding toward or away from any conclusion; some things never found; a fully specific deep history written on Night 3b; every mystery written to one template with every required field, checked by script; every being that answers questions has a written limit on what it knows and how it may be asked.
8. Every place named in any sealed file carries a bracketed map id, and a script fails the lock on any id the map does not hold. Nothing anywhere points at ground the map does not have.

## 9. Important characters

1. Both sources: the Keeper places a small cast of world-level figures at creation, which can include whole peoples; everyone else rises from play. The best characters come from play and may grow far more important than anyone intended.
2. Once a character becomes significant, their nature and history are fixed in the record.
3. Mortals age realistically on the yearly clock. A significant character's death reaches the god if it would know, and gets its own moment in the morning story.
4. Legacy carries on only if someone set it up: the character, the government or the god, through students, books, teachers, libraries, universities. Otherwise it is lost.
5. Extending a mortal's life must be earned.
6. Every campaign starts clean. Nothing from the original Telegram world carries over.

## 10. Time and turns

1. The pace table uses real-world rates, adjusted for terrain, weather and season, and is public. Gods move at mortal pace unless their powers say otherwise.
2. Gods need no food or sleep (sleep is optional), so they achieve more through endurance, not speed. All gods share occasional incredible feats; how often and how large is set in world-building. The game makes clear to players how much of the year is theirs to use.
3. No calendar is displayed. The player decides how much time passes, negotiating against what has already been decided. The timeline stays consistent. Earlier years are locked unless the DM, the civ agent and the Keeper all accept an argument.
4. Unplayed time is delegated to advisors and kings, or scheduled ("I'll do this then"). Long tasks resolve at night.
5. Scenes: each starts with the board (what the god can see, hear and know), then the DM waits. The DM never acts for the player. Nothing resolves until the player commits; costs, risks and odds are stated first. The player ends the scene. The DM may discuss things in (oog).
6. During unplayed time, the god follows standing conduct: what the player sets, or by default the god's conduct profile, cautious and in character, never reckless. Minor encounters resolve by that conduct. Major ones are held, the morning story stops at the moment of contact, and the player plays it live.
7. The DM asks about the player's intentions and leans into musings, asking for more, to understand the god. It keeps a conduct profile of the god in the repo, built from choices, musings and answers.

## 11. The map

1. Two views: a painted map and a gazetteer of exact facts. The world is painted once, by the image model, on Night 3a (the surface, an underground sheet only if the world has one, and a cloud layer for fog), from the Keeper's placement plan, after the gods and peoples exist and their land preferences are known. The Keeper then traces the map data onto the paintings in painting coordinates and checks every feature lands where the painting shows it. Where the paint departs from the plan, the data follows the paint; if it departs so far that a god's asked-for country is gone, one repaint is allowed, as an image request that needs Michael's go. Every description of land released to a god, a people or the DM is written after the tracing, from the map data, never from the plan. The paintings never change; the map is composed from them and the record every time, so ground cannot be lost.
1a. The map shows topography and the names of areas, with towns marked as points. No armies, characters, routes or other markers. One sheet holds the continent, at the scale of a map of Middle-earth; regions are large and detail is coarse, and that is the intended look.
1b. Every map segment is labeled for out-of-game reference: a letter-number grid of about 16 to 20 cells (5 by 4) on all four edges, and each region's name with its grid cell, so "the hills in D3" and "the Drover's Hills" both work.
1c. Map painting requests are sealed (`SPOILERS_do_not_open/images/requests/`), since a prompt describes the whole world. Scene requests stay public.
1d. The map data carries, per region, its elevation, water, climate band and neighbors with travel days at the pace table; and, for the sheet, roads, the gods' landing points, and the plane section (4.5).
2. The whole world exists from Day 1, underground layers included, and changes only through the world.
3. Terrain is revealed a region at a time. Regions are smaller than in the original; entering one reveals its general topography with some uncertainty.
4. Three grades of knowledge: seen (drawn exactly), reported (drawn as told, possibly wrong, with its source), rumored (a faint note, given generously). Ground corrects to the truth once seen. What a god sees at landing is set by the sight rule in `engine/rules/map.md`, settled before any description is written, and the checker tests every god's starting view against it. The player's knowledge file holds opaque ids; a rumor is a name and a grid cell, never a coordinate; a report may carry the shape the god was told, in painting pixels, because that is the god's belief and may be wrong. The truth's coordinates reach the file only when the god has seen the ground. At landing a god knows only what it can see; its people's knowledge reaches it as they tell it.
5. A god's senses add hints, not sight. How a god gathers information is what grows its map.
6. The map is on request and always ready. On the first morning it arrives zoomed in on the god's known regions, with a note that it can be requested any time.
7. Traded charts enter at the reported grade with their source, and may be lies.

## 12. State and memory

1. The repo is the authority after anything the player points to in the chat (section 2.6).
2. Each agent sees only its own files plus what the Keeper releases to it. Nothing in the player's campaign folder reveals a vote, a pool, another god, the count of gods (as a numeral or a number word), the deep history, the star, a mystery, the schedule, a hidden power, or a recurring phenomenon's true count before it has been seen. The Keeper keeps a sealed list of sealed terms (`S/sealed-terms.txt`) from Night 1 on, and a script searches the public folder for them before every lock and every morning. The checker reads every public file as well, since a script catches words and not meanings.
2a. A real clock, not an estimate. Every real time an agent logs is Pacific, taken from the time tool or the commit record. The keeper log is the index of a campaign; an agent reads a file in full only where its step needs it, and says in the log what it read in summary.
3. A chronicle for each player, holding only what their god knows and readable any time: year by year, canon, who's who, threads, messages. The civ agent keeps the people's side; the DM keeps the god's side and assembles both after each night.
4. Nothing is ever deleted. The chronicle condenses with age; canon (power cards, rulings, the people's code, who's who) never condenses. Agents read the condensed version first and open full logs only when needed.
5. A failures checklist, built from the 703 DM mistakes logged in the original game, ships with the engine. The continuity checker runs it every night and the DM runs it before any report. When a kind of mistake recurs, a new check is proposed in (oog), approved by the player, and added to the Change List.
6. Rolls: dice are hidden from the player, who sees only outcomes. Odds are worked out from factors and can be argued with the DM in (oog). Odds start at even (50), move by fixed steps for each factor (numbers, ground, preparation, surprise, skill and craft, powers, condition, and any other circumstance, which may be added or negated as it arises), and are clamped between 5 and 95; certain or impossible things are not rolled. Factors and odds are logged before the roll. A successful appeal recalculates the odds; a roll is never redone after its result is known. Only `tools/roll.py` rolls, and it logs every call to `state/rolls.jsonl`. The continuity checker flags any contested outcome without a logged roll and anything rolled twice.
7. The ruling ledger is sealed, in the spoiler folder. Every ruling the Keeper or DM makes is recorded there, and every agent checks it before ruling on anything already ruled on. The ledger takes any request settled against a god in whole or in part, any ruling that binds more than one card, and every ruling made at the creation table. When nothing was disputed it opens with a line saying so. The player sees rulings only as they come up in play and on their power card.
8. Recurring phenomena (a yearly event, a seasonal migration, a repeating sign) appear in the story only when the god or its people would notice them. Whenever they appear, the count is the true one, taken from the record by script, never estimated or varied by an agent.
9. Open questions addressed to the god (an envoy's question, a letter, an offer) are tracked as pending items. The DM makes sure each is put to the player before 1:30, woven into play or plainly in (oog); this is never a list of loose threads, only things someone has asked the god. If the answer follows directly from something the player has explicitly decided, the DM may apply it and says so in the morning story. Otherwise the thread is held unresolved if the world can wait; if it cannot, the other side meets the god's silence and reacts as it would.
10. The god's own bodily senses are always reported when they occur, woven into the story wherever they appear, in scenes and in the morning story alike.

## 13. Narrator boundaries

1. The DM never: acts for the player; resolves anything before the player commits; treats musings as orders; changes an established rule without approval; invents terrain, history or routes; voices an NPC god itself; points at signs; corrects a god's beliefs about the world.
2. The morning story is the default. Other formats, such as a numbered task list, only when the player asks. The DM may learn a player's habits but keeps the default unless asked, and the story always comes first.
3. Voice: in the fiction, spare, concrete and grounded, with mythic weight when earned; no purple prose, no flattery. In (oog), plain and direct. Prose by default; lists only when asked for or when the content is a list.
4. Mood, not invented drama. There is no drama agent. Tension comes from the world's events and from choices. Drama inside scenes is welcome when it grows out of what is actually there.
5. The voice follows the player's heart, shaped by musings as well as actions. A gentle god forced into war is still told as a gentle god.
6. Mistakes about the rules or the record are corrected at once in (oog), citing the record. Beliefs about the world are never corrected; the DM may challenge the player's musings with questions in (oog), without supplying the answer.

## 14. The daily painting

1. One house style for every campaign: a 19th-century academic oil painting with a smooth, finely blended surface (soft glazed transitions, fine detail, minimal visible brushstrokes, no heavy impasto or rough texture); strong light and shadow from a single warm source (lamp, torch, fire, low sun) or heavy overcast; umber, ochre, gold, olive and near-black with occasional cool accents. Romantic landscapes, grand historical scenes, and natural-history studies of creatures painted as if real. Low, close views; wet reflective stone; ancient architecture; a saturated subject against darkness; scale shown by something small beside something vast. Quiet, watchful, ominous. Never text, borders, grid texture or a photographic look.
2. References: Michael's first five fox paintings are primary; the later batch is secondary. The photographic beast image is excluded.
3. Appearance cards in the repo keep the avatar, significant characters, creatures and places looking the same every time.
4. Paintings show only what the god knows.
5. Generator: OpenAI's `chatgpt-image-latest`, run by the GitHub job `.github/workflows/paint.yml` with the key stored as the `OPENAI_API_KEY` secret. Scene requests go in `images/requests/`, paintings land in `images/out/`. Map requests are sealed (11.1c) and land in `SPOILERS_do_not_open/images/out/`. The house style has a map block of its own for the map paintings.
6. Shape is chosen per scene: wide for vistas and crowds, square for close studies.
7. One painting each morning, plus up to two on request during the day; after that, the player is asked to wait until the next day.

---

## 15. Creation nights and the lock

1. Nights 1 to 3 are overnight sessions like the world turn, chosen by the campaign clock. Night 1 rolls the gods and the star and blends the surveys. Night 2 has the gods make themselves and negotiate. Night 3a builds the peoples and the map; 3b the history, mysteries, schedule and cast. Guide: `engine/night/creation-nights.md`; the Keeper's procedure is the sealed runbook.
2. The lock is run by the continuity checker, not the Keeper. The checker runs the lock checklist line by line, by script where a script exists (place ids, leaks, mystery template, rolls, dashes), and writes `LOCKED.md` naming the commit it checked, committed alone after it. The Keeper fixes what fails and the checker reruns. If the lock has not passed by 6:00, the clock stays in creation at 3b, the 6:30 wake posts a notice that the world is still being built, and the next overnight session resumes 3b from the flags. Nothing is added after the lock.
3. Each night ends with a close check: every file in the night's writes list exists, and the Keeper writes a neutrality self-check for the night.
4. Creation took about 1 hour 20 minutes of agent time in run 01 (Day 1 to the lock, in one sitting), with Night 2 about 23 minutes and Night 3 about 29 minutes. Run 02 took about 1 hour 50 minutes of agent time, with Night 2 at 36 minutes and the lock passing on its third round.
5. The first morning's painting is part of creation. When Michael starts a run or a campaign, the image count is settled once at the start: the surface, the clouds, the first morning, and an underground sheet only if the world has one. A held request waits in `images/held/` (scenes) or `SPOILERS_do_not_open/images/held/` (maps), outside the paint job's trigger.
6. There is no codex. The player's own files and the morning stories carry the history.

---

## Open before and during the build

- One real painting through the API (proves billing and verification; compare against the ChatGPT app tests).
- Dry runs: the 1:30 wake-and-save, the handoff to the overnight session, the 6:30 morning story, overnight access to the repo.
- Night-turn model: time a turn on Fable against Opus.
- Update the repo address to the capitalized StarFall.
- Creation simulation run 03 on build 3, with every NPC god forced to a god-king variety by test override, to see the engine handle ruling gods and the player's god stay distinct.
- The scheduled night task's prompt needs updating to `engine/night/scheduled-prompt.md`, with Michael's go.
