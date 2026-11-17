# Rules: powers

How a god's powers are written down, ruled on, grown and trimmed. Binding on the DM, the Keeper and every NPC god agent. Sources: DESIGN.md 3.7, 3.9, 3.10, 3.14, 3.15, 4.8, 6.1 to 6.7, 12.7, 13.1, 13.6.

## 1. The power card

Every god has one power card. The player's is `player/power-card.md`. Each NPC god's is `SPOILERS_do_not_open/campaigns/<name>/gods/<god>/power-card.md`, in the same format (6.6). The card is canon: it never condenses and nothing on it is ever deleted (12.4). A change is a new dated entry, never an edit of an old one.

### Format

```
# Power card: <god's name>

## Form
<the body or bodies the god wears; how many bodies this campaign allows (3.13);
what the form can and cannot do by itself; senses; pace relative to the pace
table (10.1); god-sense as set for this campaign (7.2)>

## Powers

### <Power name>
Status: main | hidden (undiscovered) | hidden (discovered Year N) | grown (Year N)
Description: <what it does, as first written on Day 2 or on Night 2, in one
paragraph. This text is never rewritten. It is "the power as first written" that
rulings are judged against (6.3).>
Drawback: <the cost that always comes with it (6.2). Also never rewritten.>
Limits settled at creation: <the main edge cases agreed on Day 2 (6.1), one line each>
Rulings:
  - Year N, <date>. <Case in one sentence.> Ruled: <the ruling in one sentence>.
    Binds: <what it now covers>. Ledger: <ledger entry id>.
Trades: <what was given up to buy this, or what this bought (3.7), one line each>
Growth: <open attempts, see section 5 of this file; completed growth with year>

### <next power> ...

## Hidden powers
<For the player's card this section says only "Two hidden powers exist (3.9).
Discovered powers are added above as they surface." For an NPC card the two
hidden powers are written in full, marked hidden (undiscovered).>

## Weaknesses bought against powers
<any weakness taken to buy an improvement (3.7), with what it bought>

## Ceiling
<For the player's card: "Set by the world. Not shown." For an NPC card the
Keeper writes the rolled ceiling for this world (6.7) here. The player never sees
this number.>
```

### Rules for the card

- Description and Drawback are written once and frozen. Everything learned later goes under Rulings as precedent (6.1).
- Every power has a drawback. A power with no drawback is not finished and cannot be used until it has one (6.2).
- A ruling is dated twice: the campaign year it arose in and the real date it was made. Both are kept because the player may later argue from either.
- Each ruling points to its entry in the sealed ruling ledger (12.7). The card shows the ruling; the ledger holds the arguments.
- Hidden powers are discovered through play (3.9). When one surfaces, the Keeper releases it to the DM, who adds it to the card the same day with the scene it surfaced in. Until then the player's card does not name it.
- Loopholes belong to whoever finds them (3.10). A loophole found is recorded as a ruling in the finder's favor, never closed retroactively. Countermeasures come only through the world (6.4).

## 2. How a ruling is requested

A ruling is needed when a power is used in a way the Description, Drawback, Limits and existing Rulings do not plainly cover. Rulings are argued as cases arise, not in advance (6.3).

1. The player attempts the use in play, or asks in (oog) whether it would work. The DM does not resolve anything yet (10.5, 13.1).
2. The DM checks the card. If an existing ruling covers it, the DM applies it and cites it. Done.
3. If not, the DM says in (oog) that this needs a ruling, states what question it is putting to the Keeper, and asks the player for their argument if they have one.
4. The DM writes the case to the Keeper (`player/rulings-pending.md`): the power, the attempted use, the player's stated original intent for the power on Day 2, the player's argument, and the DM's own argument on the player's behalf. The DM argues the player's case genuinely (6.3). It does not argue against the player; the Keeper supplies the other side itself.
5. The Keeper first checks the sealed ledger for a prior ruling on the same matter and follows it if one exists (12.7). Otherwise it rules in real time when the scene is waiting (6.3), or in the night turn when the matter can wait until the year resolves.
6. The Keeper records the ruling in the ledger: date, year, god, power, matter, both arguments, the ruling, what it binds. It releases the ruling to the DM.
7. The DM adds the ruling to the power card and tells the player in (oog) in one or two sentences: what was ruled and what it now covers. The scene resumes from where it stopped.

Nothing resolves while the ruling is pending. If the Keeper cannot be reached during the day, the DM says so and the attempt is held to the night turn as a major encounter would be (10.6).

### Appeal

The player may appeal once per ruling, in (oog), with a better argument than the one already made (2.9). The DM carries the appeal the same way. If the Keeper changes the ruling, the old ruling stays on the card struck through with the new one dated beneath it, and the Change List gets a line. A ruling that has been appealed once is settled until the player brings an argument the Keeper has not heard.

## 3. The judgment order

The Keeper decides every ruling in this order (6.3). A later test is reached only when the earlier one does not settle the matter.

1. **Fairness, above all to the player's original intent.** What did the player mean this power to be when they described it on Day 2? If the use is what they plainly meant and the card simply failed to say so, it works.
2. **Fit with the power as first written.** Does the use follow from the Description and Drawback text as written? A use that is a natural reading of the words stands. A use that needs the words stretched does not.
3. **Balance.** Does allowing it push this god clearly above the others (3.10, 3.15)? Balance is a reason to narrow a ruling, never to deny a use the first two tests allowed; the narrowing is written into the ruling.

Two further checks on any ruling:

- The ruling must come from the world. It may not depend on anything the god could not know (12.2) and it may not invent terrain, history or routes to make the power work or fail (13.1).
- Gods are kept roughly equal, not exactly equal (3.15). The Keeper does not rule against a god merely because its power is the strongest in the campaign.

## 4. Tiers of growth

Three things grow in different ways (6.5). The Keeper rules on which tier an attempt belongs to before it is tracked.

### Craft

Craft is how time is spent. Its reward is what that time produces: a wall built, a language learned, a people taught to smelt, a route mapped. Craft has no ceiling and needs no ruling. It is tracked by the civ agent and the DM as ordinary work and resolves over scene time or unplayed time at the pace table (10.1, 10.4). A god that spends a year forging is a better smith; it has not gained a power.

### God powers

Powers are innate, separate from craft and from mortal magic, like eyes or legs (4.8, 6.5). Practice at craft never produces a power. Powers grow only by the two tiers below.

### Small refinements

A small refinement makes an existing power more precise, slightly longer in reach, slightly faster, or usable in one new narrow way that the Description already implies. It never adds a new effect and never removes a drawback.

Needed: time, practice and risk (6.5).

- Time: at least one full year in which the god gives real part of its time to the practice. The DM confirms this from decisions and scenes, not musings.
- Practice: at least one logged attempt in a scene or in unplayed time where the refinement was tried and the result recorded.
- Risk: the practice must have been able to cost something real (the drawback paid at full, a body hurt, a person harmed, a plan failed). A refinement practiced where nothing could go wrong does not count.

A refinement does not need a trigger, a new drawback or a ceiling check. It is recorded as a ruling on the card ("Refined, Year N: ...").

### New powers and big upgrades

A new power is any effect not on the card and not a hidden power surfacing. A big upgrade is an existing power doing something its Description does not imply, or doing its thing at a different order of scale.

Needed, all five (6.5):

1. **A trigger in the world.** Something the god met in play: a mentor who showed it, a realization in a scene the DM can point to, an example witnessed in another god or being. The trigger must be in the record before the attempt starts. A player saying "I want to be able to do X" is a goal, not a trigger.
2. **Years of practice with failures.** At least two years of attempts after the trigger, and at least one logged failure that cost the god something. The Keeper may require more years for a larger power. No growth completes in the year its trigger appeared.
3. **Real risk.** Each attempt is rolled (`encounters.md`) with the drawback and the stakes stated first. A failed attempt may wound, exile or cut off the god (7.8), may harm its people, or may show the god to its enemies.
4. **A new drawback.** The grown power gets its own drawback, negotiated between the DM and the Keeper with the player's input in (oog), before the final attempt. No new drawback, no new power (6.2).
5. **Within the ceiling.** The Keeper checks the world's secret ceiling (6.7). If the growth would pass it, the Keeper says so to the DM in one line ("the ceiling holds") without giving the number, and the DM tells the player the attempt is beyond what this world allows. The practice is not wasted; it counts toward a smaller growth if one is argued.

Growth is rare and modest; the status quo holds (6.7). A god that grows one power in five years has grown fast.

## 5. Tracking an attempt across years

An attempt to grow a power is a thread that may run for years. It is tracked on the power card under Growth, one block per attempt:

```
Growth attempt: <what the god is trying to gain>
Tier: refinement | new power | big upgrade
Trigger: Year N, <the event in the record, one line, with a pointer to the scene or year file>
Practice:
  - Year N+1: <what was tried, where, outcome, roll id, what it cost>
  - Year N+2: <same>
Failures counted: <n>
Drawback proposed: <text once negotiated, else "not yet">
Ceiling check: not yet | passed Year N | held Year N
Status: open | completed Year N | abandoned Year N | beyond ceiling Year N
```

Rules:

- The DM opens the block the day the player states the attempt and the trigger is confirmed in the record. The Keeper confirms the tier.
- Each year the god practices, the DM or the civ agent (for practice in unplayed time, per standing conduct) adds one line. A year with no practice is written as "Year N: no practice." Gaps do not reset the count, but the Keeper may rule that a long gap costs a year of practice.
- The player may abandon an attempt at any time. The block stays, marked abandoned. If the player returns to it later, the old practice counts.
- When all five needs are met, the player plays the final attempt as a scene. It is rolled. Success adds the power or upgrade to the card with its drawback and the date. Failure costs what was staked and adds one more failure line; the player may try again the next year.
- An NPC god's attempts are tracked in exactly the same block on its own card. Its civ agent and the Keeper fill the practice lines from its decisions and the year's resolution.

## 6. NPC gods

NPC gods negotiate their powers with the Keeper on Night 2 (3.3, 6.6) and keep cards in the format above in the spoiler folder. They are bound by the same rules:

- Their Descriptions and Drawbacks are frozen on Night 2. Their main edge cases are settled then, as the player's are on Day 2.
- When an NPC god uses a power in an unruled way during the night turn, its agent asks the Keeper to rule, stating its own case. The Keeper rules by the same judgment order, with the NPC god's original intent in place of the player's. The ruling goes into the same ledger. The NPC's card gets the ruling.
- NPC gods grow under section 4 and section 5 with no shortcut. The Keeper does not hand an NPC a power to make a story.
- NPC gods can find loopholes (6.6). A loophole found by an NPC stands for that NPC as a player's would.
- The Keeper keeps all gods at roughly equal total power as far as it can foresee (3.10, 3.14). It does this at creation through the budget and later only through rulings that pass the judgment order, never by quietly altering a card.
- The player learns an NPC god's powers only by seeing, being told or working them out (7.9). Nothing from an NPC card is ever released to the DM except what the player's god witnessed.

## 7. What the DM may trim

The DM may trim a power slightly to keep the game fun (6.4). Trimming is the only change to a power's use that does not go through the Keeper first, and it is narrow.

What a trim may be:

- Declining to resolve a use at a scale that would end a scene, a thread or a people in one stroke without play, and instead resolving it at a scale that leaves the outcome to be played.
- Requiring a roll (with factors stated) for a use the card would otherwise make automatic, when the automatic version would settle something the whole year turns on.
- Holding a use to the night turn so the Keeper can rule, when the DM judges it touches other gods or the event schedule.

What a trim may never be:

- Changing the Description, Drawback or any ruling.
- Denying a use the card plainly allows.
- Trimming the same use twice. The second time, it goes to the Keeper as a ruling.
- Silent. Every trim is announced.

How the DM says it, in (oog), in this shape: "(oog) I am trimming this one: <the use> would <what it would settle>. I am resolving it as <the trimmed version> so the rest can be played. If you want it ruled on, I will put it to the Keeper." The trim is logged in `player/rulings-pending.md` with the tag `trim` and reported to the Keeper at 1:30. If the player asks for a ruling, the trim is set aside and section 2 runs. If the Keeper later rules the full use allowed, the trim does not bind the future, and the DM says so.

Countermeasures against a power are never a trim. They must be genuine and earned inside the world by someone in it (6.4): a people that learned, a god that watched, a thing found. The DM never invents one.
