# Continuity flags, campaign dryrun, Year 1 (checker, stage 5, run 2026-11-18). Ranked by severity, most severe first.

## 1. Ruling r-001 changes an engine rule for all campaigns without Michael's yes
- Check: 3, Rules (no ruling contradicting the rules; DESIGN 2.9 and 12.7). Also 6, The player (held encounters).
- Where: ruling-ledger.md r-001; applied in year.md weeks 5, 9 and 22; releases/001/dm.md weeks 5, 9 and 22.
- Record says instead: encounters.md 6 makes an encounter major when it "would require a decision the player has not made (an offer, a demand, a question...)" and when "the agent is unsure. Unsure means major." The Riverfolk civ agent held all three petitions (report-001.md, "Encounters held"). r-001 overrules that and "binds all campaigns". DESIGN 2.9 says nothing in the rules changes without the player's yes and every change goes into the Change List. There is no Change List entry. The conflict between encounters.md 6 and DESIGN 12.9 is real, but settling it for every campaign is Michael's call, not the Keeper's.
- Fix: correct the record by marking r-001 as a proposal to Michael, scoped to this year only, and say so in the morning notice. If Michael declines it, rework the year: Wellbrook week 5 becomes the first held encounter and the god's thread stops there. Everything in his thread after week 5 (Aldford, the watcher sighting, the boatmen's telling to him, Hask's mother, Thornmere's contact) is then unresolved for him.

## 2. Aldford, week 9: the god acts where the player never typed it
- Check: failures checklist 6, Acting for the player (checker 6).
- Where: year.md week 9 ("He comes to the door of the house and stands there through the night"); releases/001/dm.md week 9; releases/001/civ-riverfolk.md ("with the god standing at the door").
- Record says instead: standing conduct is "observe only, avoid contact with strangers, retreat if seen, defend but do not kill" (conduct-profile.md). The default in encounters.md 5 is to hold, not act. r-001 only covers a petition that standing conduct answers "by silence and inaction". Walking to the house and keeping a night's vigil is an action, and it sets up "Tam has not spoken to him since" as a consequence. So this fails even under r-001.
- Fix: rework the year from week 9. Either hold the plea at contact, as the civ agent did, or have the god stay at the water in silence. The two rolls (Ede, roll 88; the child, roll 19) had no factor for the god's presence, so their outcomes stand and must not be rerolled. Tam's reaction should be rewritten by the civ agent from what the god actually did. The player has not seen this yet, so no corrections entry is needed unless it is posted.

## 3. God-sense reported with distance and strength the card does not give
- Check: 3, Rules (no power beyond its card); failures 8, Re-litigating settled powers; 4, Knowledge.
- Where: releases/001/dm.md ("one east and a little north, the stronger; one due east and fainter, far"; weeks 4 and 5 "comes toward him"; "a day's walk off"; week 22 "closer than it has been, a few hours' walk"). releases/001/thornmere.md ("the near pull", "the far pull", "moved upriver, slowly, a few miles every several days"). releases/001/ashwake.md ("the nearer pull ... the farther pull").
- Record says instead: power-card.md lists god-sense as "a pull at any distance, direction only." No ruling adds strength or range. The player's morning story would hand him the watcher's range and approach, which is information he did not have.
- Fix: correct the record. Every release should give bearing only, and bearing changes over time. Movement may only be told as a change of bearing. If the Keeper thinks NPC gods sense distance, that needs a ruling in the ledger and a card entry, offered to the player's god as well.

## 4. The midsummer sky-light was placed on week 17 by the civ agent, not by the Keeper, and week 17 is not midsummer
- Check: 1, Cause; 2, Fixity; 5, Neutrality (recurring phenomena at their true moments); failures 13, Invented drama.
- Where: civs/riverfolk/years/001.md ("That night the third light rose over the eastern hills"); year.md frame ("midsummer ... the night of week 17"); releases/001/dm.md week 17 ("the night the posts were struck"); keeper-log.md neutrality self-check ("the light's moment was fixed in pass one before the civ wrote").
- Record says instead: world-events.md (pass one) fixes the third light only as "midsummer", with no week. The Keeper's own calendar makes week 14 "the first days of summer" (dm.md), so midsummer falls about week 20. The keeper log's statement is not supported by the pass-one file. The coincidence was chosen by an agent, and it links the drowned-village clue to the lights in the Oxmouth belief "called up by the posts". That belief now sits in the DM's release as a hook.
- Fix: rework the year. The Keeper fixes the midsummer night from the season reckoning and logs it. If it is not the night the posts were struck, the civ agent rewrites the Oxmouth reaction, and dm.md and the chronicle are corrected. Also correct the keeper-log line.

## 5. chronicle-people.md tells post-contact events, drops the boatmen's return and says the headmen asked the god
- Check: 6, The player (held encounters stop at contact); failures 3, Forgetting; 2, Contradiction.
- Where: campaigns/dryrun/player/chronicle/chronicle-people.md.
- Record says instead: dm.md says Part C (after week 23) is "not to be told" until the scene is played. The chronicle, which the player can read at any time (DESIGN 12.3), gives "four sky-lights ... midwinter", a reaped harvest and year-end numbers. It leaves the boatmen "gone upriver", although they came home in week 17, before contact. It says "Both headmen ask what you want done with them", but dm.md says the post questions "were spoken among the headmen" and were never put to the god.
- Fix: correct the record before the player sees it. Cut the chronicle to week 23, add the boatmen's return, and tell the post questions as the headmen's talk. The keeper log covered only the two "Keeper" words, not this.

## 6. Map, gazetteer and world.md show names and facts no one told the god
- Check: 4, Knowledge; failures 11, Map ground lost (nothing added that no one saw); failures 1, Invention.
- Where: player/gazetteer.md and map.png ("The Drover's Hills", "Black Mere", "an old king's fort"); player/map-knowledge.json (drover-hills and black-mere have no told name; kings-fort told name "an old king's fort"); world/world.md Year 1 ("old earthworks on a crest above it", "walked ten days").
- Record says instead: the boatmen reported "a dark mere in a fold of the hills" and "old banks and ditches ... like a fort" (dm.md). They never said "king", "Drover's" or "Black Mere". Those are the sealed names in map.json, and with no told name the tool draws the truth. "Above the mere" is the sealed note's wording, but the boatmen passed the crest a day before the mere, which is about eight miles off. They were turned back on day seven, not after ten days. The boatmen also reported a grey snow range to the north, and it is not in the knowledge file at any grade. The keeper log covers only the pre-turn test entries, not these leaks.
- Fix: correct the record. Use told names "the hill country past the wood", "a dark mere" and "old banks and ditches like a fort", and add greywall as reported from the boatmen. Fix the world.md lines. Redraw with map.py. If the map has been shown to the player, log in corrections.

## 7. Ashwake's release corrects his people's belief and misstates it
- Check: 5, Neutrality (no correction of beliefs); 4, Knowledge (a release holding more than its agent could know); failures 18 and 2.
- Where: SPOILERS_do_not_open/campaigns/dryrun/releases/001/ashwake.md ("The Kiln say they are gods going up ... your people are wrong about what the lights are").
- Record says instead: civs/kiln/lore.md has the Kiln believing the lights are "sparks thrown up when the gods strike each other far off". "Gods going up" is the event schedule's sealed note about mortal belief in general. Nothing in Ashwake's senses tells him his people are wrong.
- Fix: correct the record. Give the Kiln's belief from lore.md and strike the verdict. Ashwake's agent has not yet decided Year 2, so no rework is needed if this is fixed before it does.

## 8. No cause in the record for Thornmere waiting seventeen weeks before contact
- Check: 1, Cause.
- Where: year.md Thornmere section; keeper-log.md ("timed it from her decisions (watch first, patient temper)").
- Record says instead: her decision 4 ("watch first") covers the god's people. Decision 5 says "If I find the god itself, I speak plainly." Decision 1 says she stops "when I reach the river". By the record she was a mile from the god in week 6 and kept level with him all summer. The week 23 contact was timed by the Keeper, and it decides how much of the god's year resolves before the hold.
- Fix: rework the year. Ask Thornmere's agent when, under decisions 4 and 5, she comes down, and record its answer as the cause. If it is earlier than week 23, the hold moves earlier.

## 9. River-sense used on water the god had not touched, with no ruling
- Check: 3, Rules; failures 8.
- Where: year.md week 6; dm.md week 6 (a walker sensed crossing the Wellbrook brook, "certain, not rolled" in keeper-log.md). Also dm.md week 9 ("he has none that bears on it"), a power judgment not in the ledger.
- Record says instead: power-card.md says river-sense covers "any running water it has touched", with "Rulings: none yet". The record shows him touching the Ald at the staithe, not the brook. Whether touching a river covers the streams that feed it is a new case.
- Fix: the Keeper rules on the tributary case, logs it in the ruling ledger and adds it to the card as precedent. If the ruling is no, rework the week 6 sense, which is the only clue the god had about the walker.

## 10. The player's decision 4 was changed without saying so
- Check: 6, The player (nothing done beyond explicitly decided matters; ask rather than infer, mystery standard 15).
- Where: player/decisions-001.md 4 ("Watch the sky-lights each night from the shingle bar"); releases/001/civ-riverfolk-pass1.md 4 (rewritten as "The god watches the sky-lights each night"); year.md and dm.md say nothing about it.
- Record says instead: decision 1 (walk to the falls) and decision 4 (watch from the bar each night) cannot both be carried out. The Keeper quietly kept 1 and dropped "from the shingle bar". The closing put the god on the bar, so the player may believe he is there.
- Fix: correct the record. dm.md should say plainly that the two decisions conflicted and which was followed, and the DM should raise it with the player in (oog). Log in corrections if the player has been told otherwise.

## 11. Hask's mother's question was rewritten by the Keeper
- Check: 1, Cause; failures 14, Characters acting out of character; 2, Fixity.
- Where: year.md weeks 22 to 25 ("the Keeper fixes it: she asked him ... to swear that if her son is sent again he will come back"); dm.md week 22, PENDING QUESTION 2.
- Record says instead: the civ agent wrote her ask as "Will he swear the boatmen back?", made in late summer. By week 22 the boatmen had been home for five weeks. The Keeper replaced a Riverfolk character's words with new ones. The civ agent decides how its people act.
- Fix: rework the year. Send the timing conflict back to the Riverfolk civ agent and have it say what she asks, or whether she asks at all, given her son is home. Update the pending item to match.

## 12. Sky-light counts varied by cloud that is not in the weather, and Thornmere's count hedged
- Check: 5, Neutrality (recurring phenomena at true rate, never varied by an agent; DESIGN 12.8); 2, Contradiction.
- Where: civs/riverfolk/years/001.md ("At Wellbrook and one hill-edge village cloud hid the second"); civ-riverfolk.md and dm.md part C ("two villages three under cloud"); releases/001/thornmere.md ("you may have seen ... the Keeper counts it as seen").
- Record says instead: world-events.md sets late spring as "fair" and says each light is "seen by anyone awake and looking across the whole region". The cloud is the civ agent's invention, with no weather fact or roll behind it. For Thornmere, the early-spring light rose on about the first night of the year, when she was still in or near the passes, where the Gatefolk release says it was "below the hills". The Keeper also says the midwinter light over the far western sea is visible from the passes and the burning hills while the early-spring light over the same sea is not, with no cause given.
- Fix: correct the record. Either the Keeper fixes a cloudy night as a weather fact with its cause, or the two villages count four. Decide Thornmere's count from where she stood and state it without a hedge. Record the visibility cause for each light.

## 13. Contested outcomes settled without a logged roll
- Check: 3, Rules (no contested outcome without a logged roll); messages.md 4 and 7.
- Where: (a) year.md and world-events.md: the Carn saw Thornmere in week 4 and "did not stop her", while the same Carn were rolled at 70 to stop each other party. (b) messages.jsonl m-0001 and m-0002: the routes crossed unknown hill ground, and messages.md 4 requires a "bad road, hard country" roll for unknown ground. Only interception was rolled. (c) civ-gatefolk.md: the three questions the Gatefolk report asked the Keeper to roll (Carn hearing through traders, word of Thornmere's leaving reaching the Carn, word carried east) were decided without a roll and without being stated as certain or impossible. (d) civ-kiln.md: "the timber people did not answer the shoving", decided without a roll.
- Record says instead: rolls.jsonl has eleven rolls. None covers these.
- Fix: rework the year. Roll (a) and (b) with factors from the record. For (c) and (d), either roll them or record in the keeper log, one line each, why the outcome was certain. Every contested outcome in year.md does have a matching roll, and nothing was rolled twice.

## 14. pending.md is empty, and dm.md labels questions never asked as pending
- Check: 6, The player (pending questions handled per the rules; DESIGN 12.9); failures 15, Lists of loose threads.
- Where: player/pending.md ("(none)"); dm.md part A last item ("Other pending questions carried by the people and not yet put to him in person ... The DM decides how they reach the player").
- Record says instead: two questions were put to the god in person (Wellbrook week 5, Fallstead week 22). DESIGN 12.9 limits pending items to "things someone has asked the god". The four headmen's questions were never asked of him.
- Fix: correct the record. Add the two real questions to pending.md, and in dm.md tell the other four as the people's talk (hooks), not as pending items.

## 15. The god's pace upriver stretches without a cause
- Check: failures 12, Time shrunk or stretched; 1, Cause.
- Where: year.md and world-events.md ("several days at each village"); dm.md (Wellbrook week 5, Aldford week 9, still at Aldford in weeks 18 and 19, Fallstead week 22); thornmere.md ("a few miles every several days").
- Record says instead: by the gazetteer, Oxmouth to Wellbrook (15 miles) took 4 weeks and Wellbrook to Aldford (12 miles) took 4 weeks. Aldford to Fallstead (10 miles) took 13 weeks, about 10 of them at Aldford. Nothing in the decisions or the Keeper's pace setting explains the long stay, and the Aldford timing is what puts Brin's telling and the watcher sighting in front of him.
- Fix: rework the year with the pace script and one stated rate. Move or keep the week 18 and week 19 events only as that rate allows.

## 16. Riverfolk pass-one release hints at more under the mud
- Check: 4, Knowledge (no release contains more than its agent could know); 5, Neutrality (no guiding); failures 19, Tone that marks a clue.
- Where: releases/001/civ-riverfolk-pass1.md, the posts item ("Nothing else comes up with them unless someone digs"; "mortals who explain a cause are wrong about something that matters").
- Record says instead: the civ agent cannot know there is anything to dig for. The posts get a guidance note that no other item in the release gets, which marks them as a mystery to the agent. No one dug, so the year was not changed.
- Fix: correct the record by striking both phrases from the release. Keep mystery-standard reminders out of civ releases.

## 17. The Carn ask about "the new god who woke on the bar" with no source for knowing it
- Check: 4, Knowledge.
- Where: year.md weeks 15 to 17; civ-riverfolk.md; dm.md week 18.
- Record says instead: nothing in the record has news of the god's waking reaching the Carn before the boatmen arrived. Their only sighting was a lone night-walker going west (Thornmere).
- Fix: correct the record so the boatmen say it first and the Carn ask after, or give the Carn a source with its cause.

## 18. The closing's contradiction has no corrections entry, and the closing misdescribes the lights
- Check: failures 2, Contradiction (fix: log in corrections); morning-story.md, closing sequence ("It states no outcome").
- Where: years/001/closing.md ("the two boats that went past the falls and have not come back"; "the sky-lights hang where they always hang"). There is no player/corrections.md.
- Record says instead: the keeper log says this was "Logged for the checker and for player/corrections.md", but the file does not exist. The boatmen came home in week 17. The lights rise, climb and vanish (world-events.md); they do not hang.
- Fix: log in corrections, creating player/corrections.md with the date, what changed and the proof.

## 19. Small contradictions in timing
- Check: failures 2, Contradiction.
- Where: (a) world-events.md has Thornmere above Wellbrook "about the sixth week"; year.md and dm.md have week 5. (b) civ-gatefolk-pass1.md and gatefolk years/001.md have the Kiln pairs coming back "about forty days later", but world-events.md puts party one back at the pass about day 40 and party two about day 34, which is 14 to 20 days after day 20.
- Fix: correct the record to one figure from the pace table.

## Morning story
Not checked: campaigns/dryrun/years/002/morning-story.md did not exist when this check finished.

## Noted, already logged
- Two NPC gods and three peoples instead of seven and eight.
- Creation nights skipped: no power cards beyond the sheets, no releases/000/dm.md, no avatar appearance card.
- No turn ran on 2026-11-17; the closing anticipated the year (flagged above only because corrections.md was never written).
- map-knowledge.json held the boatmen's reports before the turn as a tool test (the name leaks in flag 6 are separate).
- NPC releases, NPC civ records, the message log and year.md kept in the sealed folder; the paths need Michael's decision.
- Pass one gave the Kiln and Gatefolk agents resolved outcomes so their years would match (messages.md 5.4).
- The word "Keeper" was struck twice from chronicle-people.md.
- roll.py writes relative to the working directory and prints a DeprecationWarning.
- The Riverfolk report was saved verbatim by the Keeper after the civ agent's write was refused.

19 flags.
