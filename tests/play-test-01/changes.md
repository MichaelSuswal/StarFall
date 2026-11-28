# Play test 01 change list

Michael's play test of StarFall 1.0 from the drop-in file (`starfall_v1_0.md`) and the template `MichaelSuswal/StarFall-Game`, begun 2026-11-27. Each item is Michael's observation, in his words where quoted, with the proposed change. Nothing is applied without his go.

| # | Where | Observation | Proposed change | Status |
|---|---|---|---|---|
| 1 | Setup, S6 | Setup asks the player to name the campaign before anything else about the game. Michael, 21:23: "it is asking me to name the campaign as the first thing. That is stupid. It should be the last thing... I have no sense of what the game is yet. In fact... maybe the game should always be called starfall... I'm not sure. but naming it as the first thing is dumb". | Setup never asks for a name. The campaign folder is always `starfall` (`tools/new_campaign.py` defaults to it), so each player's copy holds one campaign called `starfall`. If the player wants a name for their world or their story, it is asked at the close of Day 3, once the world exists, and recorded as a display name only; no path changes. The GitHub copy's name (S3) stays, since GitHub needs it, with `StarFall-<their name>` suggested. | proposed |
