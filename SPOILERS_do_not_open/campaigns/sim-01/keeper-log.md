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

### Night 1 resumed

Resumed 2026-11-18 at 23:07 Pacific. The seven agents were spawned by the coordinator and each wrote `S/gods/<label>/survey-day1.md`.

### 1.3 Reading the seven

All seven files hold 19 numbered answers. Skips, all allowed: g2 Q14; g5 Q19; g7 Q5 and Q12. Premises rejected, each with the god's own answer in its place: g2 Q10 (that fear of each other and fear of the world are separate), g4 Q8 (that standing out is a choice between the two ends), g5 Q16 (that a word could be worth only its giver). No file names or quotes its seed. No dashes.

Character check against each sheet:
- g1-stone: holds. Wary to the limit and still wants neighbors; says so. Few words throughout.
- g2-law: holds. A god of law that leans hard to freedom and breaking; the answers reconcile it (walls are what it is for; it wants oaths to stand even against itself).
- g3-song: holds. Proverbs, patience, wariness, seen only when needed.
- g4-harvest: holds. Open trust and fear both show (gives its word easily, nervous of being located).
- g5-fate: one break. Presence 90 (works unseen) against answer 8 (a god unmistakable, the gap visible from a long way off), with no reconciliation. This is the runbook's own example. Sent back once, the contradiction named, in `S/releases/creation/g5-fate-night1.md`. The new answer goes at the end of its survey file; the first answer is kept. Not rewritten by the Keeper.
- g6-dreams: holds. Leans hidden and wishes to be remembered; the wound carries it, and the lean is mild.
- g7-beasts: holds. Bargain voice throughout; the wish to be served sits against the wound and is owned.

One gap that is a god's own (1.6): g1-stone answer 6 names two places on the range that sit far apart. Follow-up written into `S/releases/creation/g1-stone-night1.md`.

Waking seasons recorded on the sheets from answer 3: g1 spring, g2 spring, g3 autumn, g4 autumn, g5 autumn, g6 autumn, g7 autumn. The player: late autumn (for `P/state/clock.md` on Night 3).

### 1.4 The blend

P is the player. Scale placements are the Keeper's reading of each answer on 1 to 10. Rules set tonight where the runbook gave none:
- A median that falls on a half is settled by one roll at even odds before the variation roll: success rounds up, failure rounds down.
- A god who skipped a scale question has no place on it. The median is taken over those who answered.

**Q1 feel. Pool.**
P: quiet, old, a little lonely; the blue hour after sunset, smoke straight up from a few chimneys, dark country that does not care. g1: grey light on high rock, many fires in the valleys, quiet then voices. g2: a great hall with doors open and the table loud, a held breath before a vow and after a broken one. g3: a long table in a low house, door open, something old humming under the floor; warm on top, dark underneath. g4: a long field at day's end, gold gone brown, low heavy light, a weight carried honestly. g5: a hearth in a long house with weather turning outside, kind and orderly. g6: a house at night with every lamp lit and the door unlocked, the dark outside deep and not hostile, a held breath. g7: a long table after a hunt, firelight, cold at the door, a deal at every elbow.
Blend: eight of eight give a small lit inside set against a large outside. Seven give the inside as shared and warm (fire, table, hall, lamps); the player gives it from outside, as a few chimneys in dark country. Low light in all eight (dusk, firelight, autumn, grey). Something old underneath in four (P, g3, g4, g6). A held breath in two (g2, g6).
Built: the world's tone is small warm lights in a large, old, indifferent country. Light is low and from one source: dusk, the blue hour, fire, lamp, overcast. Weather tends to turning: mist in low ground, cold at the door, clear cold dusks on high ground. Palette within the house style: umber, ochre, gold going to brown, near-black, with the blue hour as the cool accent. Peoples gather close indoors, talk, swear and bargain; the country outside is not hostile and not kind. The loud hall is a people's temper, not the world's; the loneliness belongs to the high and empty places.

**Q2 land. Placement wishes.**
P: high country, uplands, moors and broken hills with long valleys, thin soil and stone; coast within a few weeks' walk, not at the start. g1: mountains, with valleys that hold people. g2: river country and the broken ground where rivers change course; flood plains, fords, cliffs cut by water; cracked mountains, marsh. g3: river country going down to marsh and a fogbound coast; low wet ground, slow water. g4: river country, flat flood land on both banks, deep soil, one low hill in sight. g5: river country with low hills folded round it; a fog coast second; not the high bare places. g6: river country with hills at its edges, a long coast in reach, marsh at the river mouths. g7: forest edge and high steppe, game country, deep cover behind and open grass in front.
Built: terrain the world must contain: mountains with peopled valleys; upland moor and broken hills with long valleys and thin stony soil; at least four separate river systems (five gods ask for river country and must be spaced), among them one of gorges, fords and shifting channels, one of broad flood plain with deep soil, one with low folding hills, one running to marsh and delta; marsh and river-mouth marsh; a fogbound low coast; a long coast; deep forest; forest edge; high steppe and grassland. Placement is Night 3; the wishes are listed in the draft.

**Q3 seasons. Scale, 1 harshest to 10 mildest.**
P 3 (hard winters, short bright summers). g1 3. g2 4 (sharp turns, long gold summer). g3 4 (long honest seasons, hard winter, generous harvest). g4 4 (winter feared but short enough to survive). g5 5 (hard enough to teach thrift, generous summer, reliable). g6 3 (long winter, short bright summer). g7 3 (hard winter that thins the weak).
Sorted 3,3,3,3,4,4,4,5. Median 3.5. Half settled by r-0122 (roll 51, failure): 3. Variation r-0123 (roll 25): lower by one. Result 2.
Built: a harsh climate. Four real seasons everywhere, eight of eight. Long hard winters, short bright summers, sharp turns between, an autumn with an edge. Varies by latitude, altitude and distance from the sea as real climate does; the low river country and the coast are less hard than the high ground, and nowhere is mild.

**Q4 past the borders. Scale, 1 wild and unwalked to 10 old kingdoms everywhere.**
P 3 (weighted to wild, old kingdoms as rumor). g1 5 (some of each, neighbors and room). g2 7. g3 8 (a little unwalked country at the edge). g4 7 (two thirds rooted). g5 7. g6 7. g7 8 (a few unwalked valleys).
Sorted 3,5,7,7,7,7,8,8. Median 7. Variation r-0124 (roll 18): lower by one. Result 6.
Built: somewhat more land held than open. Godless peoples are rooted, old and several: toward the upper part of the three-to-five range, with long-claimed land, borders and customs. Real wild country remains, in large pieces, between and beyond them. Number and claims are set on Night 3 from this 6.

**Q5 age of the human story. Scale, 1 living memory to 10 ruins under ruins over thousands of years.**
P 10. g1 10. g2 8 (five or six thousand years, stacked, still traceable). g3 10. g4 7 (thousands of years, but not buried under itself). g5 9. g6 10 (many thousands). g7 skipped.
Seven answers, sorted 7,8,9,10,10,10,10. Median 10. Variation r-0125 (roll 93): raise by one, clamped to 10. Clamp logged. Result 10.
Built: the deepest history the scale allows. Several risen and fallen peoples, layer under layer, the oldest older than any tongue now spoken. Night 3 writes it to that depth.

**Q6 mortal magic. Scale, 1 a rumor most doubt to 10 a wise-woman in every valley. Provisional until the star.**
P 2. g1 unclear (two places named; follow-up sent). g2 6 (one valley in three). g3 7. g4 3. g5 6. g6 3. g7 7 (one in every few valleys).
Not blended yet. Waits on g1's follow-up answer.

**Q7 magic's feel and cost. Pool.**
Feel. P: listening, or being listened to; small, specific, tied to place. g1: cold water on a hot day. g2: a promise kept in the body, a pull in the chest, iron on the tongue. g3: singing, a held breath, the world leaning toward the note. g4: effort, lifting something heavy and slow. g5: a debt entered, a ledger opening. g6: listening, sideways, nearer remembering than casting. g7: a bargain struck, the price named first.
Cost. P: personal and slow, something ordinary: sleep, the taste of food, a name once answered to; no clean meter. g1: rest, or years. g2: a sworn word given up, a name, a vow. g3: memory: a face, a name, a morning; the worker cannot read the ledger afterward. g4: the body, then time: years, a season of sleep, a field's yield. g5: years, memory or small comforts, on the spender and never a stranger. g6: sleep. g7: years, a memory, a season of luck, a thing loved.
Blend: the cost is the most shared thing. Seven of eight put it on the worker's own person, slow and ordinary. Sleep or rest: P, g1, g4, g6. Memory or name: P, g2, g3, g5, g7. Years: g1, g4, g5, g7. For feel, a reaching that is answered (listening, singing, asking, a pull) is in P, g2, g3, g6, g7.
Built, one system, inside the deep lore's Truth 4: a working feels like listening hard and being answered. A held breath, a reach, the place leaning in. It is small, specific and tied to where the worker stands. It makes nothing. It costs the worker something particular of her own, slowly and never in a countable way: the rest in her sleep, the taste of food, a face, a morning, a name she answered to. She often cannot say afterward what went. The land near a working pays too; that part is the deep lore's and is not common knowledge.
Minority answers kept as local understandings, each wrong about something that matters: that the price is named before the work and is fair (g7); that it falls only on the one who spends and never on a stranger (g5); that it costs years of life (g1, g4, g5, g7; workers do seem old early); that it is paid in a sworn word (g2); that it is a debt someone keeps a ledger of (g5). None is a second system.
Left out as rule: any price agreed in advance, and any guarantee that only the worker pays. The deep lore does not allow either.

**Q8 how much a god stands out. Scale, 1 barely more than a great sorcerer to 10 the one-eyed man among the blind.**
P 7 (closer to the one-eyed man, but nearsighted and able to be wrong). g1 2. g2 8 (a great deal, with mortal powers worth being wary of). g3 3. g4 6 (well above a sorcerer; mortals can hurt a god's work). g5 first answer 9; sent back, new answer awaited. g6 3. g7 6 (a mountain among hills; a crowd can make a god's life hard).
Not blended yet. Waits on g5's answer given again.
Shared whatever the number: gods can be wrong (P, g6), and mortals can oppose a god or its work (g2, g4, g7). Both go in the draft.

**Q9 strangeness of the wild. Scale, 1 familiar animals and a few legends to 10 creatures no one has a name for.**
P 3 (mostly ordinary, familiar animals a bit off, one nameless thing somewhere high). g1 3. g2 6 (a good third unnamed). g3 7 (well toward strange; a creature or two older than the people). g4 3 (the nameless at the edges). g5 2. g6 3. g7 4 (seven in ten known, two in ten legend, one in ten nameless).
Sorted 2,3,3,3,3,4,6,7. Median 3. Variation r-0126 (roll 58): leave. Result 3.
Built: a mostly ordinary wild. Familiar beasts, a handful of true legends in the deep places, and a very few things with no name, kept to the edges, the heights and old ground. Strangeness gathers where the deep lore puts it, for the lore's reasons; the rule for creatures is one rule.

**Q10 fears. Pool.**
P: slow things: famine, a bad winter, a pass that closes, sickness moving along a trade road, a rumor that turns a village on itself; not knowing what is coming. g1: the mountain itself, falling, hunger in winter, walls that give way. g2: the broken oath (premise rejected, own answer given). g3: forgetting, the slow kind, a village losing its songs a winter at a time; patient hunger. g4: hunger, bad year on bad year; the neighbor who stops being one when the bins are empty. g5: slow hunger; a bargain gone wrong, a debt that outlives its maker. g6: being forgotten, the name gone before the grave; what walks when the lamps run out. g7: the refused stranger and the debt that comes due; a beast that hunts the hunters; a hard winter.
Blend: slow hunger, 5 (P, g1, g3, g4, g5). Hard winter, 3 (P, g1, g7). Broken faith, 4 (g2, g5, g7, and g4's neighbor). Forgetting, 2 (g3, g6), and it is the deep lore's own Truth 3.
Built, widespread standing threats for the schedule: runs of bad harvests and hard winters; broken faith between peoples and its debts; the slow loss of what a place knows of itself. Rare candidates, unplaced: a pass that closes; a sickness that travels a trade road; a village turned on itself by rumor; ground or walls that give way in the mountains; a beast that hunts hunters; something abroad in the lampless hours. Each needs a body, a cause and a cost on Night 3.

**Q11 scarcity. Pool.**
P: salt; iron second. g1: safe passage, salt, shelter in the cold, trust most. g2: trust that holds; salt and iron also hard to find. g3: those who remember, the old singers. g4: seed grain. g5: surety, a promise that holds; grain, salt and iron for trade. g6: sleep that restores. g7: salt, and honest weights.
Blend: salt, 5 (P, g1, g2, g5, g7). A word that can be relied on (trust, surety, honest weights), 4 (g1, g2, g5, g7). Iron, 3 (P, g2, g5), always second.
Built: two world scarcities. Salt, the material one, shaping roads, marriages and wars everywhere. Reliable faith, the social one: in this world a promise that will still be good in ten years is rare and dear, so witnesses, sureties, hostages and true scales are things peoples pay for and fight over. This is a temper of the world's peoples and their history, not a rule. Iron is short in many places, as a local matter of geography. Local candidates, unplaced: kept seed grain; living rememberers; safe passage and winter shelter; restful sleep.

**Q12 buried things. Pool.**
P: old roads that go where they should not, built by people with another idea of distance; a sealed door or two; bones of something enormous as a detail only. g1: old roads, sealed doors, bones left unopened. g2: sealed doors with the oath written on the frame; old roads straight to places no longer there. g3: roads that go under water; sealed doors with a song for a lock; enormous bones farmers plow around and call hills; something buried that is waiting. g4: old roads, a few sealed doors, great stone granaries no one remembers building, empty. g5: old roads and sealed doors. g6: old roads first, a few sealed doors, one or two buried halls with carved walls; no enormous bones. g7: skipped.
Blend: old roads, 7 of 7 who answered. Sealed doors, 7 of 7, always few. Enormous bones, 3 for (P as a detail, g1, g3), 2 against (g4, g6).
Built: old roads are a widespread feature of the deep history, more than one people's, some running to places that are gone or under water. Sealed doors exist, few, each a single site. Rare candidates, unplaced: one set of enormous bones, taken for hills; empty great granaries; buried halls with carved walls; a door with an oath on its frame; a door with a song for a lock; tablets no one can read (from g2 Q5). The deep lore's own buried body, the glass under the deepest ruins, is there regardless.

**Q13 non-human peoples. Pool and scale, 1 none to 10 many kinds and many of them.**
P 3: few and strange, not elves or dwarves, barely able to talk with us, living in the old ruins with their own reasons; asks not to be told. g1 3: few, old, slow of speech, keep to the stone and watch. g2 4: two or three peoples, each with its own idea of a promise: one that cannot lie, one that lies as courtesy, one old, small and watchful that keeps records. g3 3: few, slow, far longer-lived, grudges kept; milk at the door. g4 3: one or two, keeping their own seasons, slow, grim, bad at lying. g5 3: few, keep to their own places, long memories, hard to bargain with, honest once bargained with. g6 3: a few, awake when humans sleep, quiet, courteous, hard to read, with laws and grudges. g7 4: forest path-keepers who guide for a fee, grass breeders of fine animals, one hard to like.
All eight say yes, and all say few. Sorted 3,3,3,3,3,3,4,4. Median 3. Variation r-0127 (roll 8): lower by one. Result 2.
Built: non-human peoples exist and are very few. At 2 the world holds one kind for certain and at most a second, rare. The shared shape, in six or more answers: old, slow, long in memory, keeping to old places, poor at lying or unwilling to, with their own law. That is the widespread candidate. Rare candidates, unplaced, for the possible second kind or for single bands: a people who keep the night hours; keepers of forest paths; breeders on the high grass; record-keepers; a people who lie as courtesy. What they are is decided on Night 3 with the deep history and is never told to the player, by the player's own request.

**Q14 travelers from afar. Scale, 1 none to 10 many, and a pool.**
P 2 (one or two, very rare). g1 3 (a few). g2 skipped. g3 2 (one or two, no more). g4 3 (a handful at most, late). g5 3 (one or two a generation). g6 3 (a handful). g7 3 (one or two a generation).
Seven answers, sorted 2,2,3,3,3,3,3. Median 3. Variation r-0128 (roll 2): lower by one. Result 2.
Built: travelers from afar are very rare: a single one, or two, within the reach of the campaign's history. Pool of what they brought, unplaced: a tool no one understands and a language only half of which works (P); a song no one has heard and a trade no one can place (g3); plain knowledge, how to store grain or read weather (g4); tools no one can explain and no way home (g6); a seed, a map no one can read, a trick of smithing (g7). They arrive hungry and tired (g1) and are weighed before they are welcomed (g5). Consistent with the deep lore: they come from under another star.

**Q15 god-sense. Rule by vote.**
P: face to face only, and not instant; perhaps a faint unease at close range, nothing at a distance. g1: a faint pull at distance, certain face to face. g2: face to face, known all at once. g3: face to face; a pull at distance is a leash. g4: face to face, needing to stand in the same place. g5: a faint knowing at distance with a direction, clearer face to face. g6: a pull, faint at distance and sharp up close, and able to be wrong. g7: face to face, by manner more than sense, the first meeting a test.
Vote: face to face only, 5 (P, g2, g3, g4, g7). Some sense at a distance, 3 (g1, g5, g6). No tie. Face to face carries.
Second count, on how the knowing comes in presence: a plain sense, quick or at once, 5 (g1, g2, g3, g4, g5). Slow, by working it out, or fallible, 3 (P, g6, g7). The plain sense carries.
Where the vote meets the deep lore. Truth 5 lists a pull between gods among its bodies and, under what investigation reveals, says gods feel each other at a distance. The deep lore wins over everything built here. Ruling for this campaign, logged as a Keeper decision and marked for Michael: the pull exists, as the lore says, and it is not a sense a god has unasked. Nothing reaches a god at a distance by default. The pull is among the things investigation can reveal: a god that goes looking, in the right way or the right place, may come to feel it. How is set on Night 2 and Night 3 with the powers and the star, and is never stated. This keeps the vote as each god's ordinary experience and keeps the lore's body in the world.
Built, the rule: every god knows from the fall that others like it came down when it did, and nothing more. On the ground a god senses another only in its presence, about as near as speech carries. There it feels plainly that this is one like itself. The sense says that, and not what: nothing of nature, power, name or intent. A god may try to hold its presence in; whether it can is a matter for its own card. The player's wish is kept in part: face to face only, and the working out of what a stranger is stays slow. The instant of knowing that it is a god is not slow.

**Q16 oaths. Rule by vote.**
P: binds, but as a debt binds, not as an enforced rule; consequences later and sideways; the world a little less willing to listen to a breaker. g1: worth only the god who gave it; force would only make liars quiet. g2: binds with real force; freely taken on; costs to swear and more to break. g3: real force. g4: real force. g5: real force; worth more than its giver; leaves a mark (premise rejected, own answer given). g6: real force, not total. g7: real force, as a debt; the world keeps the account and collects with interest.
Vote: binds with real force, 7 (P counted here, since the player asks for a real consequence). Worth only its giver, 1 (g1). No tie.
Form, from the pool of those seven: a debt the world collects later (P, g7); not instant or total (P, g6); costly to swear and never compelled (g2, g7); a mark on the swearer (g5).
Built, the rule: an oath sworn between gods binds with real force. It must be sworn freely and on purpose, with something of the god's own named behind it; a promise in passing is only a promise. Nothing stops a god from breaking one. A broken oath is collected on, later and sideways, at the breaker's cost, and the cost is real. The form of the cost is fixed on Night 3 inside the deep lore, which already says the plane keeps accounts; it is never stated to any god, and no god is told a rule exists beyond this: a sworn word is a real thing here. Reputation applies besides.

**Bodies. Rule.**
No survey of the eight speaks to how many bodies a god may have, and no rejected premise does. No question asks it. Default applied and logged as a default, not a vote: one body.

**Q17 mortals worth following. Pool.**
P: a mapmaker, surveyor, trader or wandering healer; curious, goes places, writes things down; ends with more knowledge than power; not a king, not chosen. g1: one who shelters others, stays, breaks a bad law and keeps a good one. g2: one who changes their mind in public and means it; a judge, a witness, a liar made better. g3: one who tells the truth when it costs; a midwife who washes the dead; a singer who will not flatter. g4: a steady one who lays up stores, tells bad news, stays on the land, can say no to a god. g5: one who keeps faith when betrayal is easy and unrewarded. g6: a keeper of a house, a ledger and a promise who does one impossible thing late in an ordinary life; mender, midwife, gatekeeper, teacher. g7: generous at the table, ruthless about fairness; hunter, headwoman or trader with a full hall.
Blend: ordinary, stubborn, honest people; no conquerors and no chosen ones, eight of eight. Truth told at a cost (g2, g3, g4). Faith kept (g1, g5, g6, g7). Able to refuse a god (g4).
Built: the kinds of mortal this world's peoples tend to raise, and candidates for the small cast, unplaced: the wandering recorder; the midwife who also lays out the dead; the public witness or judge; the storekeeper who tells bad news; the keeper of faith; the host with true scales; the late-blooming keeper. No one is scripted.

**Q18 discoveries. Pool.**
P: a companion, or a place that turns out to be listening back; something with its own mind. g1: a people who need it; a door in the rock; a truth about the one before. g2: a companion who can say no and have it matter; a truth about itself; a place it cannot enter without paying. g3: a companion who can bear a long silence; a truth it did not carry down. g4: a companion who stays; a truth it has been circling. g5: a companion who stays. g6: a companion long here, neither god nor mortal, who tells the truth when asked. g7: a companion out of the wild that chooses to stay; a power that comes only from being many.
Blend: a companion, 7 of 8, each not a servant and not a worshipper. A truth about oneself, 4 (g1, g2, g3, g4).
Built: beings able to become a companion to a god are a widespread candidate: several in the world, each its own thing with its own mind, none assigned to any god. Truths about a god's own past are already the deep lore's Truth 5 and are served by the secret backstories on Night 2. Rare candidates, unplaced: a place that listens back; a door in the rock; a place that takes a price to enter; a being long here that is neither god nor mortal and does not lie; a thing from the wild that follows; a strength that comes of being many (close to the deep lore's Truth 8, a candidate discoverable power).

**Q19 undared wishes. Pool, handled with care.**
P: that the world stay indifferent and keep secrets never solved; and that someone remember what the god did, long after. g1: that this time they live. g2: that the first oath ever sworn in this land be kept, and that no one ever learn what it was. g3: that nothing truly broken is ever finished being sung, and that someone is still listening at the last verse. g4: that it not have to take anything back; that it keep what it grows and wake to glad people. g5: skipped. g6: to be remembered, its name known in a thousand years. g7: to be known by name in every hall, the stranger's place set for it; to be served.
Each wish the world can hold, as a candidate, unplaced, never a rule, and none to be set on its own god's certain path:
- P: kept as the world's standing temper (indifference, secrets left unfound, mystery standard rule 11). The remembering is a candidate thread: something in the world that keeps what was done.
- g1: no promise that a people lives can be a rule. Candidate: a people that did come through, somewhere.
- g2: a first oath still being kept, under everything, its terms known to no one. A hidden thing that may never be found.
- g3: a song still being sung of something long broken, and a listener for it. Sits close to the deep lore's carriers.
- g4: a thing grown and kept through a long sleep. A place or a breed that came through.
- g6, g7: fame is earned in play and cannot be placed. The custom of a place set for the stranger is a candidate custom for some people, not theirs.
What each would mean is fixed on Night 3.

**Left out, and why.**
- Any distance sense as a default (g1, g5, g6): lost the vote. The lore's pull is kept as above.
- An oath worth only its giver (g1): lost the vote.
- A magic price agreed beforehand, and a cost that never touches a stranger (g7, g5): the deep lore does not allow them. Kept only as local beliefs.
- A promise that a god's people lives, or that a god keeps what it grows (g1, g4): the world listens and does not obey. Kept as candidate places only.
- Uneven magic (P, a few valleys where everyone knows one): not left out. It is one rule spread unevenly, which the deep lore already gives.

### 1.5 World draft

Wrote `S/world-draft.md`: tone, climate and seasons, magic (level pending; feel and cost set), the three rules, how much gods stand out (pending), the wild, past the borders, the age of the human story, non-human peoples, travelers, the terrain list, each god's placement wish, and every pool with widespread features set apart from rare candidates. Every rare candidate is marked unplaced.

### 1.6 Follow-ups

Wrote `P/player/followups-day2.md`: three questions, each with a form for the fiction and an (oog) fallback. Sources: the player's question 2 (high ground or valley, needed for placement); the bent premise on question 15 (whether the god would hide what it is); the bent premise on question 16 (what the god sets behind its word). No follow-up on question 13, by the player's request. Nothing in the file shows a vote, a pool, another god or anything sealed.

The same file carries a short section for the DM with the three rules a god's build must fit (bodies, knowing another god, a word given), in words the player may read. The runbook names no file for this, and the Day 2 guide needs the bodies rule and the power card needs god-sense. The NPC gods receive the same rules in their Night 2 releases, so the player learns no more than they do. The player will see from it that the wish for a slow recognition was kept only in part; no count or reason is given.

NPC gods with a gap of their own: g1-stone (answer 6). With g5-fate's send-back from 1.3, two gods have something to answer.

### Night 1 paused a second time

Paused 2026-11-18 at about 23:14 Pacific, waiting on two answers: g5-fate (`## Answer 8, given again`) and g1-stone (`## Follow-up, answer 6`), each to be added at the end of the god's own `survey-day1.md`. Still to do when they return: place both answers, blend Q6 and Q8 with their rolls, fill the two PENDING lines in `S/world-draft.md`, run the neutrality self-check, and log that Night 1 closed. Night 1 is not closed.

### Night 1 resumed a second time

Resumed 2026-11-18 at 23:13 Pacific. Both gods answered, each adding one section to the end of its own survey file and changing nothing else.

- g1-stone, follow-up on answer 6: three valleys in ten, a rumor in the rest. Its first answer 6 stays in the file and now reads against the follow-up; the follow-up is the answer, as the god chose the nearer of its two points. Placed at 3.
- g5-fate, answer 8 given again: reconciled. Hidden is how it works and unmistakable is what it is; a gap of kind, not of display; no mortal able to point at it, none able to doubt it is there. It stands four parts in five toward the one-eyed man. The character check now holds. Placed at 8 (the first answer had been read as 9). One send-back used; none remains for this god.

### 1.4 The blend, completed

**Q6 mortal magic. Scale, 1 a rumor most doubt to 10 a wise-woman in every valley. Provisional until the star.**
P 2 (rare but real, a rumor most doubt, a few valleys where everyone knows one). g1 3 (three valleys in ten). g2 6 (one valley in three, the other two unsure). g3 7 (nearer a wise woman in many valleys). g4 3 (low, a few valleys). g5 6 (past the rumor, toward the wise woman, rationed). g6 3 (nearer the rumor end, not at it). g7 7 (one in every few valleys, known by name).
Sorted 2,3,3,3,6,6,7,7. Median 4.5. Half settled by r-0129 (roll 53, failure): 4. Variation r-0130 (roll 81): raise by one. Result 5.
Built: a middle level, provisional. Across the whole world a mortal with the gift is found in something under half the valleys, known by name where she is, sought out and feared a little, doubted a few valleys off. Still an event, not a trade. Spread is uneven under one rule. On Night 3 the star's range is rolled (step 3.4); if 5 lies outside it, it clamps to the nearest end and the clamp is logged.

**Q8 how much a god stands out. Scale, 1 barely more than a great sorcerer to 10 the one-eyed man among the blind.**
P 7. g1 2. g2 8. g3 3. g4 6. g5 8 (answer given again). g6 3. g7 6.
Sorted 2,3,3,6,6,7,8,8. Median 6. Variation r-0131 (roll 42): leave. Result 6.
Built: a god is plainly more than any mortal and not beyond all answer. Mortals meeting one feel awe and wariness, not helplessness. A god can be wrong, and mortals can oppose a god and damage its work. The 6 shades the ceiling roll on Night 3 as the Keeper notes direct.

Both PENDING lines in `S/world-draft.md` are filled. No line in the draft is open.

Roll count for Night 1: r-0001 to r-0131. 121 for the seven gods (two of them rerolls with reasons), 10 for the blend (three half-median rolls, seven variation rolls; Q8 needed no half roll). Nothing rolled twice.

### Neutrality self-check, Night 1

Each place where the Keeper could have leaned, and what was done.
- The player's voice. Counted once in every scale, pool and vote. The player lost on Q4 (asked for wild, the world came out more held than open), was softened on Q6 (asked for 2, the world is at 5 for now) and was kept only in part on Q15. None was adjusted.
- Scale placements are the Keeper's reading of free prose, and several medians sat one step from changing. Each was placed before its roll and none was moved after a roll was seen.
- g5-fate's first answer 8 was read as 9 and its second as 8. The median was 6 either way, so the send-back did not move the result.
- g1-stone's follow-up moved the Q6 median from 5.5 (had the unclear answer been read as the midpoint of its two places) to 4.5. The follow-up was asked before any Q6 roll was made, and the god's own number was used.
- The Q15 ruling is the one decision tonight that the files did not make for the Keeper. It keeps the vote as each god's ordinary experience and keeps the deep lore's pull as something to be found. It favors no god: the three who asked for a distance sense and the five who did not all land under the same rule. Marked for Michael.
- The rules section added to the player's follow-up file tells the player only what the seven other gods will be told on Night 2, in the same substance.
- No answer of any agent was rewritten. No candidate was placed. No wish was granted whole.

### Night 1 closed

Night 1 closed 2026-11-18 at about 23:16 Pacific (2026-11-19 07:16 UTC). All checkboxes of runbook sections 1.1 to 1.6 are done. Open for Night 2: the player's answers to the three follow-ups; the Q15 ruling awaiting Michael's eye; the magic level provisional until Night 3.

## Night 2

Night 2 began 2026-11-18 at 23:24 Pacific (2026-11-19 07:24 UTC). A fresh Keeper session, working from the repository alone. Read: `CLAUDE.md`, DESIGN.md, the keeper and npc-god role files, every file in `engine/rules/`, every file in `SPOILERS_do_not_open/keeper/`, everything in `S/`, and the player's Day 2 outputs in `P/player/`.

Found on reading, before any work:
- The player's three follow-ups are answered in `P/player/followups-day2.md`. The player took the campaign's three rules as given and asked for no means of hiding from other gods.
- The player's card says two hidden powers exist and no more, and its Ceiling line reads `Set by the world. Not shown.` No correction is needed under 2.5.
- The Q15 ruling from Night 1 still awaits Michael's eye. Night 2 builds on it as logged.

### 2.1 Releases written

Wrote `S/releases/creation/<label>-night2.md` for all seven. Each holds: the rules that bear on a god's build (one body; god-sense as set; a sworn word; how far a god stands above mortals, at the blended 6, in words and without the number; mortal magic at its provisional level and its feel and cost, in words, the common understanding only), the god's own follow-up answers (g1-stone answer 6, g5-fate answer 8 given again; the other five were asked nothing), its waking season, and the Day 2 checklist turned toward an NPC as eight fixed sections of `self.md` (name, form, traits, backstory outline, what it wants, proposed powers with drawback and edge cases, trades, the people it hopes to lead), plus `goals.md` and `record-of-gods.md`. Nothing of other gods beyond the rule that they exist, no vote, no pool, no number from the blend, nothing of the player, nothing of the deep lore.

Choices made in writing the releases, because the files did not give them:
- Bodies, as an item of the checklist, is folded into the rules block and the Form section. The rule is one body; there is nothing for the god to choose.
- Added to the rules block, from DESIGN.md and the role file and not from the blend, so that proposals come in at a scale that can be priced: gods need no food and sleep is a choice; a god moves at the pace of its form; a god cannot die; gods speak mortal tongues; the peoples work bronze and no steel; every power carries a drawback; there is no set number of powers; nothing over the top. A god would know all of these of itself.
- Holding its presence in from another god is offered as something to ask for and pay for, the same offer the player received in follow-up 2. A god that does not ask cannot.
- The mortal magic paragraph gives only the common understanding. The part of the cost that is the deep lore's is left out.
- Each agent is told to stop after its three files. Pricing follows in a negotiation file, at most three rounds.

Night 2 paused here for the seven agents (step 2.2). This Keeper session has no tool for spawning agents; the coordinator runs them.
