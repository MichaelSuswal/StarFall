# Build 3 check: continuity checker

Checked against `build-plan.md`, `changes.md` and `applied.md` on 2026-11-20, after `git pull origin main` (already up to date). Findings give file and line and describe procedure only. Sealed content is not quoted.

## Check 1. Coverage

In scope: 34 items (51, less 18 skipped, 39 already applied, and the 15 marked no change). Item 38 is met by item 39's change. Applied as the plan says: 29. Applied in part: 5. Applied against the plan: 0 outright, 1 in tension (decision 3 against decision 4).

Items applied in part:

1. Item 20 (weakness pricing rule). Written in `engine/rules/powers.md:76` (section 1, not section 6 as the item says) and in `engine/creation/day2-the-god.md:32`, but not in the runbook. Section 2.3 of `SPOILERS_do_not_open/keeper/creation-runbook.md` (lines 191 to 206) prices weaknesses with no statement of the rule.
2. Item 22 (reconcile the Night 2 limit). The runbook routes it through corrections (`creation-runbook.md:196`), but `engine/rules/powers.md:81` still says the Keeper "may add a Limit, logged" on Night 2, with no mention of `corrections.md`.
3. Item 49 (landing zoom, label collision). Done in the tool, but `engine/rules/map.md` section 4.5 (line 245) describes only `--zoom known` and says nothing of label placement, and `map.md:249` still says the first morning map is "zoomed on the known regions". That contradicts `creation-nights.md:59`, `creation-runbook.md:466` and `morning-story.md:77`, which all say `--zoom landing`. `map.md:204` has a stray comment left from line 203 pasted on the end, and line 203 has lost its comment.
4. Item 47 (image count asked once). The rule is stated (`DESIGN.md:233`, `creation-nights.md:23`, `creation-runbook.md:20`), but no file is named to hold the approved count. Step 1.1 (`creation-runbook.md:69`) tells the Keeper to log "the image count Michael approved", and nothing in the repository gives a fresh session that figure. See check 6.
5. Item 45 (sight rule). `map.md` now has two sections numbered 1.4 (lines 89 and 103). The paragraph at `map.md:101` (the test sheet and scratch file) belongs to 1.3 and sits inside the sight rule. `map.md:96` cites "section 2.2" for the reveal distances, which are in 2.1 (`map.md:147`).

Smaller gaps:

- Plan assignment: the size rule in `powers.md`. `powers.md` has no size line. It is in `day3-the-people.md:25`, `DESIGN.md:60`, the rubric and the runbook, so nothing is missing in practice.
- `landings` format. The runbook (`creation-runbook.md:317`) and the tool (`tools/map.py:522`, keys `at` or `point`) use a region plus a point. `map.md:46` (example) and `map.md:70` (text) still give a region id only.

The twelve decisions, one by one:

1. Premise: in `day1-world-survey.md:3` and `:26`, `DESIGN.md:40`, `npc-god.md:9`, runbook standing rule `:21` and template 7.0 (`:482`), and the rubric (`:117`). Applied. See check 2 for an asymmetry in template 7.0.
2. Day 3 defaults: `day3-the-people.md:9`, `:25`, `:32`, `:43`; runbook 3a.1 (`:277`) and 7.7 (`:723`). Applied. See check 2 for 3a.1's "refusal of any default among them".
3. Helpers and dismissal: `DESIGN.md:61`, `day3-the-people.md:32`, `dm.md:28` and `:32`, `civ.md:7` and `:13`, `keeper.md:18`, `npc-god.md:9`, runbook `:22`, `:281`, `:294`, template 7.3 (`:595`), rubric `:117`, `checker.md:23`. Applied. Tension: decision 3 says every NPC god starts with helpers and "the rule lean decides the form, never whether", while decision 4 keeps "a lone god with no one". The rubric carries both, at `npc-god-rubric.md:117` (every NPC god starts with helpers) and `:146` ("no one helps it"). Run 03 forces every rule lean to god-king, so this does not bear on it. It needs a ruling before a normal campaign.
4. Rule and worship leans: rubric `:141` to `:186`, sheet template `:512`, releases 7.5 (`:649`) and 7.7 (`:725`), `DESIGN.md:56`. Applied as the plan lists them. Note: "sacred monarch" names two different things in the rubric, a band (`:148`, where a mortal line holds the throne) and a god-king variety (`:160`, where the god is the monarch). A sheet line needs the band named beside the kind, or a reader can mistake one for the other.
5. Run 03 override: mechanism in rubric section 13 (`:190` to `:205`), runbook `:25` and 1.3 (`:96`), `keeper.md:41`, `creation-nights.md:23`, `DESIGN.md:56`. Applied, but where the file lives is inconsistent and one allowed location is public. See checks 2 and 4.
6. Naming placeholders: `DESIGN.md:62`, `day3-the-people.md:34`, `keeper.md:15`, runbook `:23`, `:295`, section 5 (`:472`), `checker.md:23`. Applied.
7. Size: `DESIGN.md:60`, `day3-the-people.md:25`, rubric `:130`, runbook `:280`, template 7.3 (`:583`), 7.7 (`:726`). Applied. `DESIGN.md:60` also says "refusing a default counts toward pricing the people's edges", which neither the plan nor `day3-the-people.md` carries. See check 2.
8. Theme reroll: rubric `:54`, runbook 1.3 (`:92`, `:98`), `keeper.md:16`, `creation-nights.md:39`, `DESIGN.md:56`, `survey-keeper-notes.md:19`. Applied, before the sheet is written.
9. Options record (18): skipped, and nothing was built for it. Correct.
10. Sealed terms: `DESIGN.md:195`, `keeper.md:17`, runbook `:24`, 1.1, 1.3, 1.9, 2.4, 2.5, 2.7, 2.10, 3a.1, 3a.8, 3b.8, template 7.12, `tools/lockcheck.py:170` and `:288`. Applied. Minor: `keeper.md:17` lists "place name" without qualification, while the runbook (`:24`, `:322`) lists only place names that are not on the map (map names are read from the map). The tool handles both, so this is wording only.
11. No codex: `DESIGN.md:234`, runbook 3b.7 (`:410`). Applied.
12. Items 36, 44, 45, 43, 49, 42 and 47: all present. 47 and 49 are in part, as above.

## Check 2. Contradictions between files

Findings: 11.

1. **Test overrides path.** `DESIGN.md:56` and `creation-nights.md:23` give `S/state/test-overrides.md` (sealed). `keeper.md:41` says only "`state/test-overrides.md`". `creation-runbook.md:25` says "in `S/state/` or `P/state/`". `npc-god-rubric.md:194` tells the Keeper to also look for `campaigns/<name>/state/test-overrides.md`. Plan decision 5 allows "`state/models.md`", which is public (`P/state/models.md`, runbook 3b.8). There should be one sealed path. Also, `keeper.md:9` says the sealed folder does not exist on Night 1, but the override must be written into it before Night 1 (rubric `:194`).
2. **Refusal as a menu item in the NPC releases.** Standing rule `creation-runbook.md:21` says releases offer no alternative to the premise unasked, and `day3-the-people.md:43` says the DM does not offer refusal unasked. Against that, the runbook offers refusal in three places:
   - Step 3a.1 (`creation-runbook.md:277`) offers "every option the player was offered on Day 3 ... refusal of any default among them", which reads as listing refusal as an option.
   - Template 7.0 (`creation-runbook.md:487` to `:488`), the premise block in every god release, ends "If you do not mean to, say so and why, plainly; it will be honored". The player's descent (`day1-world-survey.md:3`) has no such line, so NPC gods get an explicit invitation the player does not. That breaks the same-terms rule (`creation-runbook.md:33`).
   - Template 7.7 (`creation-runbook.md:728` to `:730`) says "You may refuse your helpers" unprompted. Decision 3 allows the release to spell out what having no one costs, so the cost line is sanctioned. The unprompted offer is the part that reads as a menu item.

   No file still tells a god it may "hope for fewer". Grep found no "hope for", "wants to lead" or "assumed, not forced" outside the struck CHANGELIST line. The rubric's "It may hope for something else, and then it says why" (`npc-god-rubric.md:186`) requires reasons and is in line with the plan.
3. **Refusal and pricing.** `DESIGN.md:60` says "refusing a default counts toward pricing the people's edges", which makes refusal a currency for edges. `day3-the-people.md:9` says only that the DM prices "the cost of it plainly", and the plan says nothing of refusal buying edges. One of the two should change.
4. **The Keeper and DM-owned files.** Standing rule `creation-runbook.md:26` and `keeper.md:20` say the Keeper never edits a DM-owned public file, including `P/civs/<people>/` for the player's people. But runbook 2.3 (`:195`) and 3a.2 (`:291`) have the Keeper write ledger ids into `P/player/power-card.md`, and 3a.2 (`:290`) with the 3a Writes list (`:273`) has it write `P/civs/<people>/state.md`. `day3-the-people.md:53` and `civ.md:9` agree that the Keeper sets those numbers. The standing rule needs these named exceptions, or the steps need to go through corrections.
5. **Clock at the end of 3b.** `creation-nights.md:21` says "Night 3b ends by setting `year: 1`, `status: open`", with no word of the DM's story first and no test-run closed state. `creation-nights.md:59`, `keeper.md:21` and runbook 4.1 (`:468`) say the Keeper sets the clock after the first morning story and the final leak check, and sets a test run to closed. Line 21 is stale.
6. **Two homes for the helpers and the hierarchy.** `day3-the-people.md:52` puts the Helpers section in `civs/<people>/record.md`, and `:55` writes `player/hierarchy.md` as well. Template 7.3 carries both `## Hierarchy` (`creation-runbook.md:593`) and `## Helpers` (`:595`). The overlap invites the two to disagree. The plan's specification names only the Helpers section.
7. **The lock's script scope is stale.** `creation-runbook.md:432` says `--mysteries` checks only headings, readings and branches, and that the checker counts kinds and reads every `Limit:` line by hand. The tool now fails kinds out of count, a missing or doubled `Answers questions:` line, a yes with no `Limit:`, and clues missing `Location:` or `Readings:` (`tools/lockcheck.py:567` to `:627`). Line 453 of the runbook is current. Also, `:430` runs only `--places`, `--mysteries` and `--leaks`, where `checker.md:9` runs `--all`.
8. **The sealed gazetteer has no names.** Runbook 3a.5 (`:325`) builds `S/world/gazetteer.md` from `tools/map.py describe <name> --region <id>`. Without `--names` or `--god`, the tool gives every place a generic name, by design (`tools/map.py:1750`). The Keeper's sealed gazetteer needs `--names`, and the runbook does not say so.
9. **Release text for the size rule.** Template 7.7 (`creation-runbook.md:726` to `:728`) lists the size costs without "a longer gestation for a larger kind of people", which `day3-the-people.md:25` and runbook 3a.1 (`:280`) include. Wording only.
10. **`map.md` against itself** (also in check 1). There are two sections 1.4 (`:89`, `:103`). Line 249 says "known" where creation uses `landing`. Line 129 says a god at landing knows "usually its landing region as seen and nothing else", while runbook 3a.7 (`:344`) and section 1.4 (`:94`) give what is in view at `reported`.
11. **Step order.** Every requested order holds where the steps are written:
   - Night 1: the theme reroll comes before the sheet (runbook 1.3, `:92` before `:97`).
   - The sight rule is read before tracing (3a.5 `:316`) and before describe (`map.md:86` to `:87`).
   - Stamp comes before describe (3a.5 `:322` before `:325`), with stamp run again after (3a.6 `:339`, 3b.8 `:420`).
   - The Keeper sets the clock after the DM's story (4.1).

   The one exception is `creation-nights.md:21`, item 5 above.

Formats checked and consistent:

- `sealed-terms.txt`: path and format, `DESIGN.md:195`, runbook 7.12, `lockcheck.py:170`.
- The mystery template's `Answers questions: yes|no` with a `Limit:` line on yes: runbook 7.8 (`:754`, `:782`), `mystery-standard.md:28`, `lockcheck.py:557` and `:612` to `:622`.
- The Helpers section: template 7.3, `day3-the-people.md:52`, `civ.md:7`, `dm.md:32`.
- The card's Day 3 block: "added Day 3" and "Ledger: pending, Night 3" in `powers.md:73` and `:75`, `day3-the-people.md:58`, runbook 3a.2 `:291`.

## Check 3. Tools against rules

`python3 tests/tools/run.py`: 24 passed, 0 failed. The run wrote nothing to the repository (`git status` shows only this file).

Findings: 8.

1. **`map.py stamp` against `map.md` 1.2 and 1.3.** It matches the runbook's use. It is idempotent, skips `LOCKED.md` and `lock-flags*.md`, never touches the public folder, and has `--dry-run` (`tools/map.py:1610`). It stamps only capitalized names of four or more letters (`:1569`), which is the rule `--places` warns by. A shorter map name is never stamped, but `map.md:73` says "every place named in any sealed file carries its bracketed id". The rule or the tool should state the four-letter floor.
2. **`map.py describe` against `map.md` 1.4: woods.** The rule says nothing past "a ridge, a wood or a wall" is seen (`map.md:91`), and from a floor the view ends at "the first ridge or the first wood" (`:93`). The tool's `blocker` (`tools/map.py:1984`) tests only region elevations, so a forest feature never closes a view.
3. **`map.py describe`: mountains.** The rule gives "line of sight in mountains" for point features (`map.md:96`). The tool reads mountains as open ground at two miles (`tools/map.py:1802`, `:1644`). This departure is stated only in the docstring.
4. **`map.py describe`: weather.** "Less in rain or mist" (`map.md:94`) is not modeled. The tool reads clear air every time. This is fine if the rule says clear air is the landing reading, and it does not say so.
5. **The rule itself: floor against height.** From a valley floor, higher ground shows on the skyline with no cap (the tool's worked example gives peaks at about 136 miles, `tools/map.py:1796`). From a hilltop, everything is capped at forty miles "whatever their size" (`map.md:94`). So a god on a hill sees less far than a god in the valley below it. The tool follows the rule. The rule needs a decision.
6. **`describe --landing` output against the sight rule.** Its `Neighbors:` block (`tools/map.py:1830` to `:1846`) lists every neighboring region with true travel days, its bearing and its nearest edge, whether or not it is in view. Runbook 3a.6 (`creation-runbook.md:335`) says every distance and direction "stays the tool's", and 3b.8 (`:418`) builds `P/releases/000/dm.md` from what the god knows at landing. Nothing tells the Keeper to drop the Neighbors block from a landing description. Copied as the runbook says, it would put unseen ground and sealed travel days in a public file and fail the checker's sight test (`checker.md:21`). See check 4.
7. **`--zoom landing` and the gazetteer against `map.md` 4 and 5.** The landing frame is the seen regions plus a quarter margin, clamped, at its own scale bar, with the full grid's letters (`tools/map.py:1131`). This matches the plan. `map.md` 4.5 does not describe it, and 4.6 contradicts it (check 1). Label collision avoidance is in the tool (`:620` onward) and not in `map.md` 4. Gazetteer: a reported region's distance comes from told data only, with no days (`tools/map.py:1302`, `:1365`), which matches `map.md:263`.
8. **`lockcheck.py --leaks` against DESIGN 12.2 and runbook 7.12.**
   - Number words: two to twelve, "twice", "a dozen", "half a dozen", within six words of the god terms in one sentence (`tools/lockcheck.py:61` to `:64`, `:447`). The plan says "one to twelve". The tool never counts "one", which is logged in `applied.md:45` and in the test README. Defensible, but it departs from the plan.
   - Numerals: DESIGN 12.2 (`DESIGN.md:195`) bars the count "as a numeral or a number word". Numerals are caught only directly before "gods" or "deities" and only for the true count and one more (`lockcheck.py:317`). A digit near "of us", "like me", "came down" or "pulls" passes.
   - Sealed terms: read case and all, with the article rule, and a missing file fails (`:288` to `:291`, `:478`). Map names the god has seen or been told are passed over, as 7.12 (`creation-runbook.md:845`) says. Prose guesses only warn. This matches.
   - Scope: `public_files` (`:416`) scans `campaigns/<name>/` and `images/requests/<name>-*.json`. It does not scan `images/held/`, where a first-morning scene request may wait (`creation-nights.md:59`, `morning-story.md:77`, runbook `:466`).

Also checked:

- **`lockcheck.py --mysteries` against runbook 7.8.** It matches: one `Answers questions:` line, the word yes or no, and `Limit:` in Truth or Body on yes (`:612` to `:622`). The "same limit word for word in `S/cast.md`" (`creation-runbook.md:782`) is not checked by script and is left to the checker's reading.
- **Held folders.** `tools/paint.py:28` skips any path with a `held` folder. `paint.yml:84` triggers only on `images/requests/**` and `SPOILERS_do_not_open/images/requests/**`. So `images/held/` and `SPOILERS_do_not_open/images/held/` are outside the trigger, as `creation-nights.md:59`, `DESIGN.md:233` and runbook 3a.5 (`:324`) require. Consistent.
- **Every lockcheck mode skips `lock-flags*.md`** (`tools/lockcheck.py:89`), matching runbook `:436` and `checker.md:9`.

## Check 4. Leaks by design

Findings: 5. Each is a place where following the engine exactly would put a sealed thing in a player-facing file.

1. **The test override in a public file.** `creation-runbook.md:25` allows `P/state/test-overrides.md`, `npc-god-rubric.md:194` tells the Keeper to look there, and plan decision 5's `state/models.md` is public. The file names NPC rule results and, by its lines, how many NPC gods are forced. A run that put it on either public path would leak the override, the NPC rule leans, and a count of gods by inference. The leak scan would not catch it unless the wording hit a sealed term.
2. **Unseen neighbors in the DM's Day 4 release.** Covered in check 3, item 6. `tools/map.py describe --landing` prints every neighbor with true travel days and bearing. The runbook keeps the tool's figures and gives no instruction to drop that block, so `P/releases/000/dm.md` (runbook 3b.8) or `P/world/world.md` could carry ground and travel days the god has not seen.
3. **`P/state/models.md` (runbook 3b.8, `:417`)**, "the model for each role for the night turn". This is public. Written one line per NPC god agent, it would show the count of gods by its line count, which no script catches, and the labels, which the scan catches. The template should say one line for all NPC gods together.
4. **`P/state/timing.md`**, the Keeper's timing file (`creation-nights.md:31`, runbook `:37`). It is public and its contents are not specified. A timing line like "spawned 7 god agents" would pass the numeral gap in check 3, item 8. The rule should say timing lines carry stage names and times only, never agent counts.
5. **`images/held/`.** A held first-morning scene request is public and is not scanned by `--leaks` (check 3, item 8).

Checked and clean by design:

- `P/player/world-rules.md`: template 7.9, god-sense never a count.
- `P/player/day3-brief.md` (2.8).
- `P/years/000/lock.md`: one line.
- Public `flags.md`: counts only.
- `P/years/000/night-blocked.md`: one line of procedure.
- NPC rule and worship leans: they appear only in `S/gods/<god>/sheet.md` and the sealed releases. No player-facing template carries them.
- The forced result is written on the sheet with no mark (rubric `:196`), so the NPC agent is not told it was forced.

## Check 5. Dashes

Every text file read for this check was scanned for U+2014 and U+2013. That covered 67 files: `CLAUDE.md`, `engine/**`, `tools/*.py`, `tests/tools/**` with the fixture, `tests/creation-sim/run-02/*.md`, `.github/workflows/*.yml`, and the five keeper files named. Found: 0. The only matches were compiled `.pyc` files under `tools/__pycache__/`, which hold the dash characters `check_dashes` searches for. They are not text, and git does not track them. This file was scanned the same way before the verdict was written (0).

## Check 6. Unattended runs

Steps that would stall or end the night with no human present: 4 by design, 3 not by design.

By design. Each stops cleanly, writes a notice and resumes next night:

- Night start with the day's outputs missing: `night-blocked.md` (`creation-nights.md:28`).
- 3a.4: the paintings fail to return within 20 minutes (`creation-runbook.md:312`). Creation then loses a full day.
- The lock not passed by 6:00 (runbook section 4, `:434`).
- A repaint is held for Michael's go (3a.5, `:324`). The night goes on with the sheet in hand, so this is not a stall.

Not by design:

1. **Where the image count lives.** Plan item 47 and decision 12 settle the count once at the start. No file holds it, though: not `state/clock.md` (template `creation-nights.md:11`), the override file, or any template. Step 1.1 (`:69`) asks the Keeper to log "the image count Michael approved", and 3a.4 (`:310`), the underground clause, and 4.1 (`:466`) test requests against it. A fresh overnight session has no source for the figure. It would either invent one (spending without a recorded go, against `CLAUDE.md`) or hold the map requests, which ends in the 3a.4 block. A named file is needed, for example a line in the starting clock or a sealed `S/state/run-approvals.md` written when Michael starts the run.
2. **An underground the count did not cover.** 3a.4 (`:310`) makes the underground sheet "only if ... the run's image count covers it". No step says what happens when the world has an underground and the count does not cover it: whether the request goes to `SPOILERS_do_not_open/images/held/`, or how 3a.5 traces a layer with no painting. Run 03's budget is three (surface, clouds, first morning), so this case can arise in run 03. Under runbook section 6 the Keeper would decide and log it, so it would not stop, but the decision touches spending.
3. **The stale clock line** (`creation-nights.md:21`, check 2, item 5). A session that follows it sets `status: open` at the end of 3b, before the story, and never sets closed for a test. If the scheduled task were enabled, it would then turn a test campaign (`scheduled-prompt.md:13` to `:14`). The scheduled task is paused, so this does not stall run 03, but a test could end open.

The image-count rule, step by step:

- 3a.4 (map sheets): honored, against the count, with the underground only if covered.
- 3a.5 (repaint): outside the count, held in the sealed held folder for Michael's go. Honored.
- 4.1 (first-morning painting): within the count, else `images/held/`. Honored, also in `creation-nights.md:59` and `morning-story.md:77`.
- Every step depends on finding the count, and item 1 above leaves it with no source. As written, the rule is honored in every step's wording and cannot be honored in fact.

Also noted, outside the engine: the run 02 stand-in brief (`tests/creation-sim/run-02/stand-in.md`) tells the stand-in to reject a premise that does not fit. Run 03 needs its own brief if it is to test the premise as now stated.

## Verdict

Not ready for run 03 yet. Five fixes come first, all small text edits:

1. One sealed path for the test override. Drop `P/state/` from `creation-runbook.md:25` and `npc-god-rubric.md:194`, give `keeper.md:41` the full sealed path, and note that the sealed folder exists before Night 1 in a test run (`keeper.md:9`).
2. A named home for the approved image count, which step 1.1, 3a.4 and 4.1 read. Also a line for an underground the count does not cover.
3. The refusal asymmetry in the NPC releases: template 7.0's closing sentence, 3a.1's "refusal of any default among them", and 7.7's unprompted "You may refuse your helpers". Run 03 tests whether ruling gods stay distinct from the player's, so the NPC releases must put the premise on the same terms as the player's descent and Day 3.
4. `creation-nights.md:21`: the clock is set by the Keeper after the first morning, and a test ends closed.
5. The Keeper's writes to DM-owned files (ledger ids on the card, `P/civs/<people>/state.md`): either name them as exceptions in standing rule `creation-runbook.md:26` and `keeper.md:20`, or route them through corrections.

Should fix before run 03, because the checker will flag them at the lock or a public file could carry them:

- Drop the `Neighbors:` block from landing descriptions, or tell the Keeper to (check 3, item 6).
- Add `--names` for the sealed gazetteer (check 2, item 8).
- Give `P/state/models.md` and `P/state/timing.md` one line each saying they carry no per-god lines or agent counts (check 4).
- Bring `powers.md:81` into line with item 22.

May wait until after run 03:

- `map.md` tidy-up: two sections 1.4, the stray comment at `:204`, the 4.5 and 4.6 zoom text, the landings format, the 2.2 cross-reference.
- The pricing rule in the runbook (item 20).
- Numerals near god terms in `--leaks`, and scanning `images/held/`.
- Woods and mountains in `describe`, and the floor-against-height reach in the rule.
- `DESIGN.md:60` on refusal and pricing.
- Hierarchy and helpers living in two places.
- The stale script scope at `creation-runbook.md:432`.
- The lone-god lean against decision 3 (not reached in run 03).
- The two meanings of "sacred monarch".
