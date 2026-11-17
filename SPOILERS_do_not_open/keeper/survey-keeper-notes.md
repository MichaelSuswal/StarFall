> SPOILER WARNING: Keeper material. Players should not read this file.

# Keeper Notes: Turning the World Survey into a World

How the Keeper uses the Day 1 survey answers (and the Day 2 and 3 follow-ups) to build the world on the three creation nights. Read with DESIGN.md sections 3, 4 and 7, the mystery standard, and the deep lore. The deep lore always wins: no survey answer can change what the stars are, where the gods came from, or anything else sealed there.

## Governing rules

1. **Equal weight.** The player and each of the seven NPC gods are one voice in eight. The player's answers carry no extra pull.
2. **One world, one set of rules.** Every answer is blended into a single world. Special places may exist, and may be strange, but the rules of the world are the same everywhere. A wish can become a place; it can never become a local exception to the rules.
3. **The world listens; it does not obey.** No single wish is granted whole. Gods discover in play which wishes the world kept. The Keeper never tells any god which of its answers were used.
4. **Three kinds of answer, three ways of blending:**
   - **Scales** (how much, how old, how strange): place each god's answer on a 1 to 10 scale, take the median of the eight, then roll a small variation (plus or minus 1) with `tools/roll.py`. The median keeps one extreme god from dragging the world.
   - **Pools** (what is scarce, what is feared, what is buried, what peoples exist): gather every god's answers into one pool. The most common themes become widespread features of the world. Rarer answers may become special places, single beings, or local histories, never rules.
   - **Rules** (god-sense, oaths, bodies): one rule for the whole world, chosen by majority. Ties go to `tools/roll.py` with even odds. Record the vote counts in the Keeper log; never reveal them.
5. **The deep lore and the star come first.** Survey answers shape the world within what this star and the deep lore allow. Where an answer cannot fit, it is quietly left out.
6. **Rejected premises.** When a god rejects a question's premise, record its own answer as given, count it in the blend if it maps to the scale or pool, and if it leaves a gap, ask a follow-up the next day, few and woven in.
7. **Everything is fixed by the end of Night 3.** Nothing derived from the survey may be added after the world locks.
8. **Log every choice.** For each question, the Keeper log records the eight answers in summary, the blend, any rolls, and what was built. This log is how the continuity checker verifies the world later.

## Question by question

**1. The world's feel (mood or image).** Pool. Distill the eight moods into the world's tone: weather tendencies, light, the color of the land, the temper of its peoples. Widely shared moods set the world; a lone mood may color one region or one place. Feeds the paintings' palette within the house style.

**2. The land that calls.** Placement, not a rule. Each god lands in country that suits its own answer (DESIGN.md section 7.5). The answers also tell the Keeper what terrain the world must contain. Lay the land so each god's country shifts realistically into its neighbors' over distance.

**3. Seasons, and the season each year opens on.** The world's climate is a scale blend (harsh to mild, long or short seasons), applied consistently, varying by geography as real climate does: latitude, altitude, distance from sea. The season each god wakes into is personal and kept per god; it sets that god's return sequence.

**4. What lies past the borders.** Scale: from wild and unwalked (1) to old kingdoms rooted everywhere (10). Sets how much land is claimed by godless peoples and how much is open. Balance per DESIGN.md section 4.9.

**5. How old the human story is.** Scale: arrived within living memory (1) to ruins under ruins over thousands of years (10). Sets the depth of the deep history the Keeper must write: how many risen-and-fallen cities, how many layers of ruin, how far back the oldest stories go.

**6. How much magic mortals have.** Scale: a rumor most doubt (1) to a wise-woman in every valley (10). Never 0, never everywhere. Bound by the star's own magic level from the deep lore's per-star variation; the blend chooses a point within the star's allowed range. Mortal magic stays simple even at the top.

**7. What magic feels like and costs.** Pool. The most shared feel and cost become how magic works for mortals everywhere, consistent with what magic is in the deep lore. A god's people share this magic, and the god shares it in its own way. Minority answers may survive as a local tradition's understanding of magic (often wrong, per the mystery standard) but never as a second magic system.

**8. How much a god stands out.** Scale: barely more than a great sorcerer (1) to the one-eyed man in the kingdom of the blind (10). Feeds the secret power ceiling's roll within its small range, and how mortals react to gods at first sight.

**9. How strange the wild is.** Scale: familiar animals and a few legends (1) to creatures no one has a name for (10). Sets the bestiary's strangeness across the whole world. Strangeness may be concentrated in particular places (high country, deep water, old ground) for realistic reasons, but the rules governing creatures are the same everywhere.

**10. What mortals fear.** Pool. The most shared dangers become the world's standing threats and feed the event schedule's clocks and triggers. A lone answer may become one being, one place or one local threat. Every danger obeys the mystery standard: a body, a cause, a cost if ignored.

**11. What is scarce.** Pool. The most common answer, or two, becomes the world's real scarcity, which drives trade, war and migration everywhere. Other answers may be local shortages from geography. Scarcity is a pressure, not a punishment; every god's people must face it somewhere.

**12. What lies buried.** Pool. Every answer is a candidate. The most shared become widespread features of the deep history (common ruins, old roads). Rarer ones become single sites, placed at creation, findable from the moment they exist, and possibly never found. Use these heavily: they are the raw material of the deep history and the short mysteries.

**13. Non-human peoples.** Pool and scale. If most gods want none, the world is human with at most one rare exception. If several want them, include as many kinds as the answers support, each with a real backstory. A god may still lead a non-human people of its own regardless of the blend (Day 3).

**14. Travelers from afar.** Scale: none (1) to many (10), plus a pool of what they brought. Travelers come from other stars, consistent with the deep lore. What they brought becomes the edge they hold over local peoples, and their history in the land.

**15. How gods recognize each other.** Rule, by majority. Becomes the campaign's god-sense (DESIGN.md section 7.2). Michael's own preference when he plays (gods sense other gods, perhaps other immortals) counts as one vote, like any other.

**16. Whether oaths bind.** Rule, by majority. Becomes whether sworn oaths between gods carry real force in this campaign (DESIGN.md section 7.7). Reputation applies either way.

**17. The mortals worth following.** Pool. Feeds the kinds of mortals the world's peoples tend to produce and the Keeper's small cast of world-level figures. Does not script anyone. The best characters still come from play.

**18. What a god could discover.** Pool. Feeds the layered mysteries (one epic, several long, many short) and the discoverable powers. Every answer that fits the deep lore becomes a candidate truth, placed at creation, findable, never held back.

**19. The undared wish.** Pool, handled with care. Each wish the world can hold becomes a special place, a being, a hidden thing, or a thread in the deep history, never a change to the rules. Many will be kept and never found. A god's own undared wish is never placed where it is certain to stumble on it.

## Follow-ups (Days 2 and 3)

Follow-ups come from gaps the night's build exposed or from rejected premises. Few, woven into the day's conversation, (oog) when needed. NPC gods receive theirs from their agents the same night. Blend follow-up answers by the same rules above.

## Day 2 and Day 3 inputs

Day 2 (the gods) and Day 3 (the peoples) are not blended. Each god's own powers, backstory, people and land are its own. The Keeper fits them into the one world, reconciles them with the deep history, and keeps total god power roughly but not exactly balanced.
