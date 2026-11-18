> SPOILER WARNING. Keeper log (dry run).

## Year 1, night turn of 2026-11-18

### Dry-run deviations, for Michael to see
- The dry run has two NPC gods and three peoples, not seven and eight. The turn ran with what exists.
- No night turn ran on 2026-11-17 though the 1:30 save did; this was the first turn. The DM's closing for Year 1 (years/001/closing.md) anticipated the year (it says the two boats went past the falls and had not come back, and puts the god on the shingle bar at year's end). The Keeper did not treat the closing as authority; the year was resolved from the decisions and the dice. The closing disagrees with the resolved year in two places (the boatmen returned in week 17; the god's thread is held at the falls in week 23). Logged for the checker and for player/corrections.md.
- The player's map-knowledge.json as committed before the turn already held the boatmen's Year 1 reports (made as a map-tool test). The resolved year happened to confirm them, so nothing was lowered; the Keeper raised north-wood and kings-fort to reported from the boatmen's walk and left the rest. Had the dice gone otherwise the file would have needed lowering with --force.
- NPC releases, NPC civ records and the message log are kept in the sealed folder, not under campaigns/dryrun/, because campaigns/dryrun/ is the player's side and the design says nothing there may reveal another god. The rules name campaigns/<name>/releases/ and state/messages.jsonl for these; the paths need a decision. years/001/year.md is likewise sealed here, since night-turn.md calls it sealed but names a path on the player's side.
- Pass one gave the Kiln civ agent the fate of its two parties and told the Gatefolk agent the Keeper had resolved that the walkers were let through on payment, so the two agents could write one consistent year. Noted per messages.md 5.4.
- The civ agent's chronicle-people.md used the word "Keeper" twice in player-facing text; the Keeper struck those two phrases and left the rest for the DM's assembly.
- tools/roll.py writes state/rolls.jsonl relative to the working directory; the Keeper ran it from campaigns/dryrun so the log landed in campaigns/dryrun/state/rolls.jsonl. roll.py also prints a DeprecationWarning (datetime.utcnow) on every call; harmless, worth a one-line fix when Michael approves.
- The Riverfolk civ agent could not write its report file (the subagent harness refused the write); the Keeper saved its text verbatim as civs/riverfolk/report-001.md.

### Resolutions (one line each: action, branch, truth, what was shown)
- Random event Year 1: rolled none. Nothing shown.
- Thornmere west through the Carn hills, hidden: Carn saw her (roll failed). Truth: Carn know a lone night-walker went west in week 4. Shown: nothing to her; nothing to the Riverfolk.
- Thornmere crosses the Wellbrook brook, week 6: river-sense fires (certain, not rolled). Shown to the god: a single unknown walker crossed from the hills; the near pull stopped in the hills east of Wellbrook.
- Thornmere shadows the god all summer: herders do not see her (roll failed); the god sees her once, week 19, at dusk on the crest, a figure only (roll succeeded). Shown: the figure, at the distance seen.
- Wellbrook petition, week 5: pending question, silence met (r-001). Shown: the ask, as asked.
- Aldford plea, week 9: god stands at the door, no power applies; Ede dies, the daughter lives (two rolls). Shown: the night, the death, the child. New fixed facts: Tam, net-maker of Aldford, about 30; Ede, dead week 9 Year 1; daughter unnamed.
- Boats pass the falls, week 14: trigger fired. Carn stop the boatmen (roll succeeded), keep them two nights, send them back with a warning and the word that the Carn will come down to see the river. Truth: the Carn's poles count the sky-lights (Long 1); the boatmen saw notched poles and were told nothing. Shown: poles notched top to bottom by the houses, at the weight of the rest of the telling. New fixed facts: Grandmother Ceth, Carn elder, about 70, one eye clouded, at the high steading above Black Mere; the Carn have dogs and herds and stone-and-turf steadings; the Carn's warning words. Boatmen home unhurt week 17 (roll succeeded).
- Carn watcher: chosen at their autumn gathering, sets out in the last weeks of winter with a notched staff, reaches Fallstead early Year 2. Fixed.
- Weir at Oxmouth: built weeks 16 to 19 as the civ designed; holds through the run and gales (roll succeeded); about four tons of fish taken, a tenth returned. River-sense: the god feels the flow change at the mouth. Shown: his sense, the people's report.
- Old posts at Oxmouth, week 17: struck by the weir mauls (clue Short 1, "posts at low water"). Truth: the drowned salt-road village. Shown: two rows of black square-cut posts; Maren's and Hobb's wrong explanations.
- Ashwake's parties: m-0001 returned undelivered (watched, not stopped); m-0002 returned undelivered (stopped by the Carn, two pots given, notched poles seen). Both home early summer.
- Gatefolk: let the Kiln walkers through on toll both ways, told no one. Fixed as the civ agent wrote it.
- Timber people north of the burning hills: new fixed fact from Ashwake's landing release; trade with the Kiln, dislike them, no blows this year.
- Sky-lights: four, at the moments fixed in years/001/world-events.md. Shown to the Riverfolk as four; two villages' elders missed one under cloud (their counts, not the record's). From the burning hills and the passes only the midsummer and midwinter lights are above the horizon (fixed).

### One line per NPC god
- Ashwake: built his great kiln, bought hall timber, kept a watch and a coal custom, sent two parties west that found no god; the nearer pull drifted west; he knows of toll-takers in the passes and hill people with notched poles who turn strangers back.
- Thornmere: walked west through the Carn hills unseen as far as she knows, watched the Riverfolk and their god a whole summer from the hills, learned his people's name for him, and came down to speak to him at the falls in week 23; held at contact.

### Neutrality self-check
- Temptation: to let the Carn deliver the boatmen a hint about the poles. Did instead: the boatmen saw the poles and were told nothing, at the same weight as the dogs and the food.
- Temptation: to let Ede live because the god stood at the door. Did instead: rolled it with the factors in the record; she died.
- Temptation: to make the weir fail for drama in the gale. Did instead: rolled it; it held.
- Temptation: to hold the Wellbrook petition and stop the year at week 5, or to resolve it with an answer the player had not given. Did instead: ruled r-001 after the arguments, met it with the god's standing silence, and sent it to pending.
- Temptation: to tie the midsummer light to the posts' discovery for effect. The civ agent put them on the same night; the light's moment was fixed in pass one before the civ wrote, and the posts' week came from the civ's labor plan. Left as it fell; Oxmouth's belief that the posts called it up is a mortal error.
- Temptation: to give Thornmere's contact earlier or later to suit the morning story. Did instead: timed it from her decisions (watch first, patient temper) and the god's walking pace.
- New fixed facts in Thornmere's release: eleven notches and nine fords between the Gatefolk passes and the Ald valley along the line she walked; Carn steadings of stone and turf with more dogs than people; the Carn questioner of Kiln party two was an old man who smiled (from the Kiln walker's words).
- Stage timing: decisions in 01:58; pass one 02:00; civ agents done 02:06; pass two and releases 02:13.
