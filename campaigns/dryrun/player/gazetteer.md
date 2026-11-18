# Gazetteer: dryrun

Everything the god knows of the ground, exact where the map is pictorial. Regenerated from `player/map-knowledge.json` by `tools/map.py gazetteer`; never edited by hand. Places are given by map grid cell, with the painting pixel in brackets; distances are in miles (0.06 miles to the pixel). Grades: seen (found so), reported (as told, may be wrong), rumored (a name and a rough place).

## Regions

- **The Ald Valley** (D5), valley, water meadow and scattered oak, about 43 miles across, seen, source: walked, the first year, year 1.
- **The Sea Marsh** (C7), marsh, tidal flats and reed, about 39 miles across, seen, source: the landing on the shingle bar, year 1.
- **The Drover's Hills** (G6), hill country, sheep and heather, reported, source: the boatmen Hask and Brin, who walked it; the hill people there call it theirs, year 1; history: year 1: reported -> reported (the boatmen Hask and Brin, who walked it; the hill people there call it theirs).
- **the wood above the falls** (C2), forest, old oak and pine, reported, source: walked for ten days by the boatmen Hask and Brin; seen from the falls, year 1; history: year 1: rumored -> reported (walked for ten days by the boatmen Hask and Brin; seen from the falls).

## Places

- **Aldford** (town), at D5 (px 400,520), in The Ald Valley, seen, source: walked, year 1.
- **Fallstead** (village), at C3 (px 335,365), in The Ald Valley, seen, source: walked to the falls, year 1.
- **Oxmouth** (town), at D8 (px 385,905), in The Sea Marsh, seen, source: the landing, year 1.
- **Wellbrook** (village), at D6 (px 505,690), in The Ald Valley, seen, source: walked, year 1.
- **an old king's fort** (ruin), at G4 (px 770,410), reported, source: the boatmen Hask and Brin, who passed below it, year 1; history: year 1: rumored -> reported (the boatmen Hask and Brin, who passed below it).

## Waters, woods and ranges

- **River Ald** (river), 58 miles long, from C3 (px 300,330) to C8 (px 335,1000), in the wood above the falls, The Ald Valley, The Sea Marsh, seen, source: walked its bank, year 1.
- **the Reed Flats** (marsh), about 19 by 24 miles, centered C7 (px 260,769), in The Sea Marsh, seen, source: the landing, year 1.
- **Black Mere** (lake), about 8 by 4 miles, centered H4 (px 909,480), reported, source: the boatmen Hask and Brin, who stood on its shore, year 1; history: year 1: reported -> reported (the boatmen Hask and Brin, who stood on its shore).

## Rivers as routes

- **River Ald**, 58 miles, seen: Fallstead, Aldford, Wellbrook.

## Distances

As the crow flies, in miles, from the positions the god believes; a reported endpoint makes the distance reported. The pace table (`engine/rules/time-and-pace.md`) turns miles into days.

- **Aldford**: Fallstead 10 (seen); Wellbrook 12 (seen); Oxmouth 23 (seen); an old king's fort 23 (reported).
- **Fallstead**: Aldford 10 (seen); Wellbrook 22 (seen); an old king's fort 26 (reported); Oxmouth 33 (seen).
- **Oxmouth**: Wellbrook 15 (seen); Aldford 23 (seen); Fallstead 33 (seen); an old king's fort 38 (reported).
- **Wellbrook**: Aldford 12 (seen); Oxmouth 15 (seen); Fallstead 22 (seen); an old king's fort 23 (reported).
- **an old king's fort**: Wellbrook 23 (reported); Aldford 23 (reported); Fallstead 26 (reported); Oxmouth 38 (reported).

## Rumors

None.
