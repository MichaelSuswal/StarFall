# Gazetteer: map-painted

Everything the god knows of the ground, exact where the map is pictorial. Regenerated from `player/map-knowledge.json` by `tools/map.py gazetteer`; never edited by hand. Places are given by map grid cell, with the painting pixel in brackets; distances are in miles (0.25 miles to the pixel). Grades: seen (found so), reported (as told, may be wrong), rumored (a name and a rough place).

## Regions

- **The Ald Valley** (D5), valley, water meadow, about 211 miles across, seen, source: walked, the first year, year 1.
- **The Sea Marsh** (C7), marsh, reed and tidal creek, about 151 miles across, seen, source: walked from the landing, year 1.
- **The Drover's Hills** (G6), hill, sheep country, reported, source: Orrin the drover, year 1.
- **The Grey Sea** (B6), sea, reported, source: boatmen at Oxmouth, year 1.
- **the dark wood north**, rumored, somewhere near D2 (px 480,150) by the telling of boatmen at Oxmouth, year 1.

## Places

- **Aldford** (town), at D5 (px 505,575), in The Ald Valley, seen, source: walked, year 1.
- **Oxmouth** (town), at C7 (px 262,884), in The Sea Marsh, seen, source: the landing, year 1.
- **Salt Cave** (cave), at C7 (px 300,860), in The Sea Marsh, seen, source: found by the Oxmouth salters, year 1.
- **Wellbrook** (village), at D6 (px 430,760), reported, source: a drover's telling, year 1.

## Waters, woods and ranges

- **River Ald** (river), 200 miles long, from F3 (px 760,300) to B8 (px 240,900), in a region not yet known, The Ald Valley, The Sea Marsh, seen, source: walked its bank, year 1.
- **Black Mere** (lake), about 20 by 15 miles, centered E3 (px 600,330), reported, source: Orrin the drover, year 2.
- **The Grey Sea** (sea), about 40 by 151 miles, centered B6 (px 161,716), reported, source: boatmen at Oxmouth, year 1.

## Rivers as routes

- **River Ald**, 200 miles, seen: Aldford, Salt Cave, Oxmouth.

## Distances

As the crow flies, in miles, from the positions the god believes; a reported endpoint makes the distance reported. The pace table (`engine/rules/time-and-pace.md`) turns miles into days.

- **Aldford**: Wellbrook 50 (reported); Salt Cave 88 (seen); Oxmouth 98 (seen).
- **Oxmouth**: Salt Cave 11 (seen); Wellbrook 52 (reported); Aldford 98 (seen).
- **Salt Cave**: Oxmouth 11 (seen); Wellbrook 41 (reported); Aldford 88 (seen).
- **Wellbrook**: Salt Cave 41 (reported); Aldford 50 (reported); Oxmouth 52 (reported).

## Rumors

- **a stead below the falls** (village), somewhere near F3 (px 690,360), by the telling of boatmen past the falls, year 1.
- **a king's fort in the hills** (ruin), somewhere near G6 (px 860,720), by the telling of Orrin the drover, year 1.

## Below, layer 1: The Salt Roads

- **The Salt Gallery** (cave), 80 miles, from under C7 (px 300,860) to under E6 (px 540,650), reported, source: the Oxmouth salters, year 2.
