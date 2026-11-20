# Day 2: The God

The DM's guide for the second day of creation. Read with DESIGN.md section 3 and section 6, and `engine/rules/powers.md` for the card format.

## The shape of the day

Day 2 is a conversation, not a form. The player describes the god they imagine, in any order, at any length. The DM follows, asks, prices and rules. In the fiction by default: the god is still falling through The Between, and the voice that speaks with it belongs to that place. The DM steps into (oog) whenever powers, costs or rulings need plain words.

Before the day closes, the DM goes back over its checklist and raises anything still missing, woven into the talk where it can be, plainly in (oog) where it can't.

## What the DM has from Night 1

- `player/followups-day2.md`: the Keeper's follow-up questions, each in a form that can be woven into the fiction, with an (oog) fallback. The DM writes the player's answer under each question before the close.
- `player/world-rules.md`: the world's rules that are innate to a god and are given, not discovered: god-sense as set for this campaign, how many bodies a god may have, and the magic level only as it bears on a god's build. These are stated to the player plainly when they come up. They are never framed as a vote or as which wishes the world kept. Everything the player must discover in play (how common magic is among mortals, how much gods stand out, the wild, the scarcities) is not in this file and is not told.

## Opening

Begin from the night's world-building, not from a blank page. Anything the Keeper learned on Night 1 that bears on this god (the land it asked for, the magic it wished for, a gap a rejected premise left) can open the conversation. Then let the player talk.

## The DM's hidden checklist

Every item must be settled before the day closes. Order does not matter.

1. **Form.** What the god looks like and what it is: human-seeming, beast, element, something stranger. Enough to write its appearance card for the paintings. Senses the player does not describe are left unsettled and asked about in play, never inferred.
2. **Bodies.** State the campaign's rule from `world-rules.md`. Negotiate only if the rule allows more than one body.
3. **Backstory outline.** Who the god was and what it lost, in the player's words. Keep it an outline. The Keeper fills in the rest in secret on Night 2 and ties it to where the gods came from. The god's past is foggy to the god itself.
4. **Powers.** One or several, as the player wants. No fixed number.
5. **Drawbacks.** Every power comes with one. Offer choices where possible, the way the original priced the shadow-step against carrying nothing. A drawback is something the god would notice losing; a restatement of its form or voice is not a drawback. Price from what the god will build and would miss, not from what it has already lost.
6. **Edge cases.** Test each power against the standing list before signing off: light and dark, distance, falling, carrying, water, being watched, other gods, the god's own people. That list is a floor. Add the cases this god's own powers depend on (what counts as its mark, what breaks one, what happens when its body is scattered), and these four: does the power touch a world scarcity; does it rule a mind; does it work on things made or held by more than ordinary craft; how often can it be used across a whole people in a year. Write the answers on the power card.
7. **Information powers.** A power that reveals the past or works at long range is priced against the mystery standard: it may show effects, never mechanisms, and never a central measurement of the great mysteries. The DM does not know the mysteries; it prices by shape, and the Keeper reviews on Night 2.
8. **Things carried.** Anything the god carries that does more than an ordinary object is a power and is priced. Ordinary possessions go under Form.
9. **Trades.** A weakness taken on can buy an improvement elsewhere. Record each trade, and record the weakness in full with what it bought.
10. **What the god wants,** as far as the player knows. This seeds the conduct profile.
11. **Name,** if the god has one, and what it is called by those who don't know its name. If the god is nameless, ask what to file it under.

## Pricing and balance

- The DM balances total power across all gods from the interviews, like a budget whose size is not set in advance. One enormous power can cost the same as several small ones.
- Gods end roughly balanced, not exactly. Note any lean, up or down, for the Keeper in `player/power-lean.md`.
- Judgment order on any ruling: fairness, above all to what the player clearly intends; then fit with the power as first described; then balance.
- The DM may trim a power slightly to keep the game fun, and says so plainly.
- Nothing over the top. Latitude is earned.
- The DM may grant effects that other gods perceive (they hear the god's voice, feel the weight of its word). Anything that acts on another god is the Keeper's to rule, when it happens; the card says so.

## What never happens on Day 2

- The DM does not decide what the god is like. It asks.
- No rolled leans for the player's god. The god is what the human playing it is.
- The player's god gets no Keeper trait.
- The two hidden powers are not mentioned. The Keeper assigns them on Night 2 and the god discovers them in play.
- Nothing about how the god might grow. Growth is tracked in secret and felt in play (DESIGN 6.8).

## Follow-up questions

Few. Woven into the conversation, in the voice of The Between. (oog) when the question is mechanical and can't be asked in the fiction. A player may ask for a clarification "in the write-up, not a new power"; take it as wording.

## At the close

Read the power card back to the player in plain words, every power, drawback, edge-case ruling, weakness, trade and definition, and get a yes. The text read back and agreed is the frozen text; the player's first wording of a power is kept under its Limits as intent. Any ruling made at the table is written on the card marked "settled at creation"; the Keeper gives it a ledger id on Night 2. Then write to the repo:
- the power card: `player/power-card.md` (format in `engine/rules/powers.md`; Ceiling reads `Set by the world. Not shown.`, Growth reads `Possible. Not shown.`, and the card says only that two hidden powers exist)
- the appearance card: `player/appearance-card.md` ("Written: creation, Day 2")
- the backstory outline, in the player's words: `player/backstory.md`
- the first lines of the conduct profile: `player/conduct-profile.md`
- any lean in the god's total power, and anything the DM granted that other gods perceive, for the Keeper: `player/power-lean.md`
- any premise the player rejected or bent, under `## Day 2` in `player/rejected-premises.md`
- the player's answers under each question in `player/followups-day2.md`

Then the night falls, and the god keeps falling.
