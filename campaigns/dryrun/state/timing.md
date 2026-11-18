# Night turn timing (dry run)

## Year 1, run 2026-11-18 (Pacific)
- Turn started: 01:46 PST (session woke 01:46; repository pulled, all rules read by 02:05).
- Models: keeper fable (this session), npc-god sonnet, civ sonnet, checker opus, dm fable, per state/models.md.
- Notes at start: no night turn ran on 2026-11-17 (the 1:30 save ran both nights; this is the first turn). The dry run has two NPC gods and one civ record, not seven and eight; the turn runs with what exists.
- Stage 1, decisions in (2 NPC god agents, sonnet, run one after the other): done 01:58.
- Stage 2, Keeper pass one: done 02:00.
- Stage 3, civ agents (3, sonnet): done 02:06.
- Stage 4, Keeper pass two, releases, sealed year record: done 02:13.
- Stage 5, check (opus): first run 02:14 to 02:22, 19 flags; Keeper rework with the Thornmere and Riverfolk agents 02:22 to 02:33; second run 02:44 to 02:49, 10 flags, all worked by 02:51; a third run followed the close.
- Stage 6, releases: with stage 4, rewritten 02:33.
- Stage 7, morning story and painting request (DM, fable): 02:34 to 02:44; painting request pushed 02:44; painting back in images/out at 02:51 (the GitHub job took about seven minutes).
- Stage 8, close: clock set to Year 2 open at 02:52. Turn total about 1 hour 10 minutes from wake to close, most of it the check loop.
- Tokens: subagents about 65k + 66k (gods), 86k + 58k + 51k (civs), 184k + a second run (checker), 134k + a second pass (DM); the Keeper session's own usage not visible to it.
- Lessons for Stage B: the NPC god and civ agents could have run in parallel (the Keeper ran them one at a time); the checker is the costly stage and the first run found real rule conflicts (r-001, god-sense bearing only, the hold's timing belonging to the NPC agent) worth keeping in the rules rather than re-finding each night.
- Third check 02:52 to 02:53: one flag (the DM release's wording), fixed 02:53. Clean at close. (Times in this file are from the session clock; two lines first written with estimated times were corrected.)
