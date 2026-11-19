> SPOILER WARNING. Keeper log. Players must never read this file.

# Keeper log: campaign sim-01

Campaign: sim-01 (creation simulation, run 01).
Real date: 2026-11-18 Pacific (2026-11-19 UTC).

## Night 1

Night 1 began 2026-11-18 at 23:04 Pacific (2026-11-19 07:04 UTC).

### 1.1 Sealed folder

Made `S/`, `S/state/`, `S/gods/`, `S/releases/creation/`. This log opened.

Conventions set tonight, because the files did not give them:
- Roll ids. `tools/roll.py` writes no id. A roll's id is its line number in `S/state/rolls.jsonl`, written `r-NNNN` (r-0001 is line 1). The file is append-only, so the ids are stable.
- Rolls are made with `--campaign sim-01`, which logs to `S/state/rolls.jsonl` from any working directory. For table rolls only the `roll` field is used; `odds` and `success` mean nothing there.
- Folder labels. `g<N>-<domain>` uses the first word of the domain, lower case (for example a domain of two joined words keeps only the first).

### 1.2 Seven gods rolled

All rolls by `tools/roll.py --who keeper --campaign sim-01`, in god order, r-0001 to r-0121 (121 rolls: 17 per god, plus two rerolls). Mapping per the runbook's standing rules. Each line gives the value used and its roll id.

- `g1-stone`. Leans: Mind 20 [r-0001], Body 41 [r-0002], Presence 50 [r-0003], Temper 21 [r-0004], Regard for mortals 25 [r-0005], Order 89 [r-0006], Making 32 [r-0007], Company 89 (rolled 64, +25) [r-0008], Appetite 40 [r-0009], Trust 100 [r-0010]. Seed: The god who dies each year and returns (Osiris, Dumuzi, Baldr, Persephone) [r-0011, roll 39 maps to 9]. Domain: stone and mountains [r-0012, roll 49 maps to 9]. Form: a shape of weather or element [r-0013, roll 77 maps to 5]. Virtue: mercy [r-0014, roll 91 maps to 1]. Flaw: pride [r-0015, roll 81 maps to 1]. Wound: it failed to save a people once before [r-0016, roll 38 maps to 2]. Voice: speaks in very few words [r-0017, roll 62 maps to 2].
- `g2-law`. Leans: Mind 28 [r-0018], Body 13 [r-0019], Presence 12 [r-0020], Temper 100 [r-0021], Regard for mortals 52 [r-0022], Order 83 [r-0023], Making 95 [r-0024], Company 59 (rolled 34, +25) [r-0025], Appetite 49 [r-0026], Trust 29 [r-0027]. Seed: The child-god, ancient but small, cruel without malice (Krishna as infant, Eros, Horus the child) [r-0028, roll 25 maps to 25]. Domain: law and oaths [r-0029, roll 73 maps to 13]. Form: human-seeming, uncannily perfect [r-0030, roll 85 maps to 1]. Virtue: patience [r-0031, roll 92 maps to 2]. Flaw: cowardice dressed as caution [r-0032, roll 30 maps to 10]. Wound: it killed a sibling [r-0033, roll 16 maps to 4]. Voice: speaks in proverbs and old sayings [r-0034, roll 3 maps to 3].
- `g3-song`. Leans: Mind 9 [r-0035], Body 83 [r-0036], Presence 64 [r-0037], Temper 2 [r-0038], Regard for mortals 49 [r-0039], Order 60 [r-0040], Making 89 [r-0041], Company 100 (rolled 78, +25) [r-0042], Appetite 56 [r-0043], Trust 79 [r-0044]. Seed: The devouring mother who is also the cradle (Tiamat, Kali) [r-0045, roll 61 maps to 1]. Domain: song and memory [r-0046, roll 95 maps to 15]. Form: an old one [r-0047, roll 45 maps to 9]. Virtue: honesty [r-0048, roll 35 maps to 5]. Flaw: cruelty from indifference [r-0049, roll 28 maps to 8]. Wound: it broke an oath and the world broke with it [r-0050, roll 70 maps to 10]. Voice: speaks in proverbs and old sayings [r-0051, roll 93 maps to 3].
- `g4-harvest`. Leans: Mind 32 [r-0052], Body 79 [r-0053], Presence 56 [r-0054], Temper 2 [r-0055], Regard for mortals 48 [r-0056], Order 39 [r-0057], Making 64 [r-0058], Company 78 (rolled 53, +25) [r-0059], Appetite 63 [r-0060], Trust 2 [r-0061]. Seed: The sleeping king under the hill who will wake (Arthur, Barbarossa, Kronos in Elysium) [r-0062, roll 5 maps to 5]. Domain: harvest [r-0063, roll 62 maps to 2]. Form: something with no fixed face that others see differently [r-0064, roll 48 maps to 12]. Virtue: restraint [r-0065, roll 18 maps to 8]. Flaw: fear [r-0066, roll 5 maps to 5]. Wound: it killed a sibling [r-0067, roll 88 maps to 4]. Voice: blunt as a hammer [r-0068, roll 35 maps to 5].
- `g5-fate`. Leans: Mind 6 [r-0069], Body 91 [r-0070], Presence 90 [r-0071], Temper 38 [r-0072], Regard for mortals 95 [r-0073], Order 16 [r-0074], Making 7 [r-0075], Company 70 (rolled 45, +25) [r-0076], Appetite 47 [r-0077], Trust 76 [r-0078]. Seed: The jealous sibling who kills and is cursed (Set, Cain, Romulus) [r-0079, roll 42 maps to 12]. Domain: fate and chance [r-0081, roll 40 maps to 20]. Form: a shape of weather or element [r-0082, roll 77 maps to 5]. Virtue: mercy [r-0083, roll 81 maps to 1]. Flaw: greed [r-0084, roll 4 maps to 4]. Wound: it loved a mortal who died [r-0085, roll 69 maps to 9]. Voice: warm and mothering with iron under it [r-0086, roll 16 maps to 6].
- `g6-dreams`. Leans: Mind 82 [r-0087], Body 16 [r-0088], Presence 65 [r-0089], Temper 53 [r-0090], Regard for mortals 29 [r-0091], Order 29 [r-0092], Making 10 [r-0093], Company 68 (rolled 43, +25) [r-0094], Appetite 38 [r-0095], Trust 26 [r-0096]. Seed: The bound god whose venom drips and shakes the earth (Loki bound, Prometheus bound, Fenrir) [r-0097, roll 86 maps to 26]. Domain: dreams and night [r-0098, roll 36 maps to 16]. Form: human-seeming, uncannily perfect [r-0099, roll 61 maps to 1]. Virtue: curiosity [r-0100, roll 67 maps to 7]. Flaw: cowardice dressed as caution [r-0101, roll 30 maps to 10]. Wound: it was once worshipped and then forgotten [r-0102, roll 87 maps to 3]. Voice: blunt as a hammer [r-0103, roll 75 maps to 5].
- `g7-beasts`. Leans: Mind 19 [r-0104], Body 4 [r-0105], Presence 46 [r-0106], Temper 40 [r-0107], Regard for mortals 51 [r-0108], Order 81 [r-0109], Making 59 [r-0110], Company 96 (rolled 71, +25) [r-0111], Appetite 38 [r-0112], Trust 29 [r-0113]. Seed: The wandering stranger who tests hospitality and punishes its absence (Zeus Xenios, Odin Grimnir, the Elohim at Mamre) [r-0115, roll 30 maps to 30]. Domain: beasts and the hunt [r-0116, roll 91 maps to 11]. Form: an old one [r-0117, roll 45 maps to 9]. Virtue: justice [r-0118, roll 79 maps to 9]. Flaw: lust for being worshipped [r-0119, roll 67 maps to 7]. Wound: it was the servant of a greater thing and fled [r-0120, roll 44 maps to 8]. Voice: speaks like a merchant with everything a bargain [r-0121, roll 70 maps to 10].

Rerolls (two, each logged in the rolls file with its reason in `--what`):
- r-0080, `g5-fate`, Domain: roll 9 maps to 9, stone and mountains, already held by `g1-stone`. Rerolled as r-0081: roll 40 maps to 20, fate and chance.
- r-0114, `g7-beasts`, Archetype seed: roll 72 maps to 12, the seed already held by `g5-fate`. Rerolled as r-0115: roll 30 maps to 30.
- No d12 roll came above 96 and no d30 roll above 90, so there were no range rerolls.

Cross-check of the seven:
- Seeds (table numbers, kept to this log): 9, 25, 1, 5, 12, 26, 30. Seven distinct. No shared seed.
- Domains: stone and mountains, law and oaths, song and memory, harvest, fate and chance, dreams and night, beasts and the hunt. Seven distinct. No shared domain.
- Shared results on tables that allow repeats, noted and left as rolled: form "a shape of weather or element" (g1, g5); form "human-seeming, uncannily perfect" (g2, g6); form "an old one" (g3, g7); virtue mercy (g1, g5); flaw cowardice dressed as caution (g2, g6); wound "it killed a sibling" (g2, g4); voice proverbs (g2, g3); voice blunt (g4, g6). The rubric forbids only shared seeds and domains.

Sheets written: `S/gods/<label>/sheet.md` for g1-stone, g2-law, g3-song, g4-harvest, g5-fate, g6-dreams, g7-beasts. Each holds the ten leans with both ends named, the seed's text without its table number, domain, form, virtue, flaw, wound, voice, the roll ids, and empty headings for Traits (own), Keeper trait, Name, Season it wakes into.

### 1.3 Releases written (first box only)

Wrote `S/releases/creation/<label>-night1.md` for all seven: the god's sheet content, the survey's opening and its 19 questions word for word from `engine/creation/day1-world-survey.md`, and the instruction to answer from inside the character, reconcile contradictions, skip what does not speak to it (keeping the number), and reject any premise it would reject. Nothing about other gods beyond what the survey's own text says, nothing of the deep lore, nothing of the player.

Choices made in writing the releases:
- The survey file's "Survey rules" block was left out of the release, because it speaks of "the player" and of the Keeper's sealed notes. Its usable content (skip, reject a premise) is in the instruction.
- Each agent is told to put the waking season in a plain last sentence of answer 3, so it can be recorded on the sheet.
- Each agent is told not to name itself tonight (naming is Night 2).
- No question about bodies was added. The survey is fixed and asks nothing about bodies; see the note for step 1.4.

### Night 1 paused here

This Keeper session has no tool for spawning agents. Per the instruction for this run, the night stops after the sheets and the releases. Steps 1.1 and 1.2 are complete. Step 1.3 is complete for its first box only. Still to do, in order: spawn the seven agents and collect `S/gods/<label>/survey-day1.md` (1.3), read all seven and send back once where an answer breaks character (1.3), the blend (1.4), the world draft (1.5), the follow-ups (1.6), and the closing line. Night 1 is not closed.

Paused 2026-11-18 at about 23:06 Pacific (2026-11-19 07:06 UTC).

Notes carried forward for the blend, so they are not lost:
- Q15 god-sense. The deep lore states as a truth that the gods feel each other at a distance, as a pull, and its clue tables use that pull. The runbook makes god-sense a vote. If the vote goes against a pull at distance, the deep lore wins by the runbook's own rule, and the vote can only set how the pull is felt and how sure a god is of what it means. To be decided and logged at 1.4.
- Bodies. No survey question asks about bodies, so the runbook's default (one body, logged as a default) is the likely result unless a god volunteers something.
- Q6 magic. The player's "rare overall, a few valleys where everyone knows one" is one rule with uneven spread, which the deep lore already supports (magic follows where the rain is thick and who can find the grip). Not a local exception.
