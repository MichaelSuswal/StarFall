# Build 3 plan: applying the run 02 change list

Michael approved this build on 2026-11-20 (21:06 Pacific): apply the run 02 change list (`changes.md`, 51 items; item 39 is already applied, item 18 is skipped) with the decisions below. No image requests. No scheduled task is created, changed or enabled. Run 03 is not approved yet; Michael will be asked again before it runs. The image budget he set for run 03 is three: surface, clouds, first morning.

## Michael's decisions

1. **The premise.** The game is about leading and building a people. The descent in The Between says, as the original did, that gods come down to lead a people, to build, rule and spread. That is the expected course of every god. A player may push back; pushback is recorded in `rejected-premises.md` and honored, and the game then remembers out loud that this god does not play the usual way.
2. **Day 3 assumes a seat and a hierarchy.** The DM opens as though the god leads a people with a seat, advisors and a hierarchy, and asks who they are. Refusing any of it is allowed, but it is a choice the player argues for, not an item on a menu. The default people is about 5,000 with a town or city.
3. **NPC gods lead.** Every NPC god starts with a people and with helpers who run things in its absence. The rule lean (below) decides the form, never whether. A god, the player's included, may deny those helpers, dismiss them, never meet them, or never employ them; once dismissed they are not forced back; new loyal helpers may come later through play. The release spells out what it costs to have no one: unplayed time runs on the god's own conduct alone, no one acts for it while it is away, and its people drift.
4. **Rule lean and worship lean** in the rubric, set from each god's rolls: rule runs from god-king with a court and priesthood, through priest-king, warlord, merchant-prince, sacred monarch behind a court, council of elders or chieftains, to a lone god with no one (rare, and only on an extreme roll); worship runs from state cult with temples and tithes, through a priesthood, local shrines, to none. Each god builds within its result and gives reasons to depart from it.
5. **Run 03 override.** For run 03 only, every NPC god's rule lean is forced to a god-king variety, varied by its rolls (tyrant, priest-king, warlord, merchant-prince, sacred monarch), so the engine gets the hang of ruling gods. The stand-in keeps playing in Michael's style, so the run also shows whether the player's god stays distinct among seven kings. Wars are allowed. The override lives in the campaign's `state/models.md` (or a `state/test-overrides.md`), never in the rubric itself.
6. **Naming (43).** The Keeper never names what the player left for play. For its own records it uses a placeholder like "unnamed house 1" or "unnamed location" until play names it.
7. **Size (37).** A people larger than the default is not a priced edge. Its costs are practical and come from the world (more food and fuel, slower growth, harder to move, longer gestation for a larger kind of people), argued case by case and open to argument, and the Keeper applies them in play. More than a few large peoples is possible.
8. **The player's theme (7).** On Night 1, an NPC domain that matches what the player has said their god is about (from the survey and any remark) is rerolled, logged. Michael wants his god to be somewhat unique.
9. **Options record (18).** Skipped.
10. **Sealed terms (30).** The leak scan reads sealed names from `S/sealed-terms.txt`, which the Keeper writes and maintains (god names and bynames, hidden power names, common secrets names, place names), instead of guessing from prose. The old prose guesses stay as warnings only.
11. **No codex.** The player's files and the morning stories carry the history. Nothing is built.
12. **Items 1 to 6 of Michael's list** (change list 36, 44, 45, 43, 49, 42) and 7 (47) are all in.

## Shared specifications

- **Advisors by default.** The people record for every god, player and NPC, carries a `## Helpers` section: who runs things when the god is absent (named offices, not named people, unless play names them), and how orders travel. For a god that refused them it records the refusal and the date, and stays empty until play fills it.
- **Rule lean and worship lean** are rolled on Night 1 with the other leans and written on the sheet; the Night 2 and Night 3 releases carry the result in one line each and ask the god to build within it.
- **Sight at landing (45).** `map.md` defines it: from the landing point the god sees what a tall mortal would see from that ground, out to the skyline the map's elevation gives (a worked example in the rule); anything released as seen at landing must be within it, and the checker tests every god's starting view against it.
- **`tools/map.py stamp <campaign>`** appends the bracketed id after every map name in the sealed files (idempotent). **`tools/map.py describe <campaign> <region-or-landing>`** writes a land description from the data (distances, directions, travel days, sight lines). **`--zoom landing`** crops to the seen region plus a margin at its own scale, with label collision avoidance on every zoom.
- **Leak scan (44).** `--leaks` also matches number words (one to twelve, "a dozen") within a few words of "god", "gods", "like me", "like us", "of us", "pulls", "came down"; and the mystery template carries `Answers questions: yes|no`, which `--mysteries` uses instead of guessing; a yes requires a `Limit:` line.
- **Image count (47).** When Michael starts a run, the orchestrator asks once for the full count (maps, first morning, and any underground). The runbook names the first-morning painting as part of creation.
- **Held requests** live in `images/held/`, outside the paint trigger.
- **Clock to Year 1** is set by the Keeper after the DM's first morning story and the final leak check; `creation-nights.md` says so. Test runs end `status: closed`.
- **First morning** gets its own section in `morning-story.md` (no year to summarize; the board as seen; names the player knows but the god does not are given in (oog)); the appearance card marks its copy paragraph.
- **`lockcheck.py`** skips `lock-flags.md`. A Keeper fix to a DM-owned public file goes through `corrections.md`.

## Assignment

- **Orchestrator (engine side):** DESIGN.md and CHANGELIST.md; `engine/creation/*` (premise, Day 3 assumptions, naming rule, size rule, helpers); `engine/roles/*` (helpers, naming, sight rule references); `engine/night/creation-nights.md` (clock, image count, held folder); `engine/rules/map.md` (sight at landing, stamp and describe, landing zoom), `morning-story.md` (first morning), `powers.md` (Day 3 power block, ledger placeholder, size rule), `appearance-card.md`; the test README.
- **Agent T (tools):** `tools/map.py` (stamp, describe, landing zoom, label collisions, gazetteer told data for reported regions, sub-pixel coordinates), `tools/lockcheck.py` (sealed-terms file, number words, Answers questions field, skip flags file, case-sensitive titles), `tools/paint.py` (held folder), tests.
- **Agent K (sealed):** the runbook (every runbook item from the list: 5, 6, 10, 11, 13, 14, 16, 17, 21, 22, 25, 26, 29, 31, 34, 35, 37, 43, 45, 50; the helpers default; the theme reroll; the sealed-terms file; the first-morning painting; the Keeper sets the clock), the rubric (rule and worship leans, exclusive shape results, .5 rounding, Keeper trait wording), the Keeper notes (star conflicts), the mystery template (`Answers questions`), and the test override mechanism for run 03.

Each side logs what it changed in `applied.md` under its own heading, by item number.
