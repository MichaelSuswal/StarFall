# Time and pace

The public pace table for StarFall. Every number here is a real-world rate from pre-medieval history, rounded for play. The DM and the Keeper use these numbers for every journey and every long task, and the player may read them, quote them and argue them. `tools/pace.py` holds the same numbers and does the arithmetic; the table here and the dictionary in the tool must always match.

Everything in this file is a baseline for a fair day in good season. The adjustments in section 6 bend the baseline; the DM applies them openly and says which ones it applied. Any rate can be argued in (oog). A ruling that changes a number goes to the Change List and into the tool on the same day.

Travel is priced by route and means (`engine/rules/map.md` section 5.1): the trip is cut into segments along the route the traveler chooses, and each segment takes the rate for its means on its ground. On foot uses section 1, on horse section 2, by wagon the ox-cart table in section 3, by boat or barge section 4. A road segment takes the good road row; a path takes the rough ground row; a river segment by boat takes downstream or upstream; a sea segment takes coastal sailing; open ground takes the row for the terrain of each region crossed. Different routes to one place give different times; `tools/map.py travel` does the segment arithmetic from the map data.

Distances are in miles, time in days. A travel day is about ten hours of movement for a mortal, with the rest for camp, food and sleep. A work day is about ten hours of labor in summer, less in winter when the light is short.

---

## 1. On foot

Miles per day for one healthy adult, carrying only a day's food and a weapon or tool.

| Ground | Miles per day | Notes |
|---|---|---|
| Good road | 20 | Built or beaten road, firm and dry. Armies on good roads managed this for weeks. |
| Rough ground | 14 | Open country with tracks, hills, fords, fences of brush. |
| Forest | 10 | Old forest with no track. Half that in dense undergrowth. |
| Mountain | 8 | Passes and ridge paths. A known pass counts as rough ground. |
| Marsh | 6 | Only with a guide or a known causeway. Without one, the DM may halve it or refuse the crossing. |
| Snow | 6 | Deep snow without snowshoes or skis. With them, treat as rough ground. |

Adjustments to the foot rate:

| Condition | Multiply by | Notes |
|---|---|---|
| Laden | 0.75 | Carrying a real load: a pack of 40 pounds or more, armor, trade goods, a child. |
| Group | 0.8 | Twenty or more people moving together with baggage. A warband or a caravan. A whole people on the move, with old and young and herds, is 0.5, by DM ruling. |
| Forced march | 1.5 | One day at a time, at a cost: the marchers arrive tired, and a second forced day in a row is a roll against exhaustion. |

Both laden and group may apply together.

## 2. Riding

Horses of this age are small, there are no stirrups, and a rider who does not spare the horse loses it. Miles per day for a rider with one horse.

| Ground | Miles per day | Notes |
|---|---|---|
| Good road | 30 | A rider who rests the horse every few days. |
| Rough ground | 20 | |
| Forest | 10 | The rider leads the horse much of the way. |
| Mountain | 10 | Ponies and mules do better than horses here. |
| Marsh | 4 | A horse in a marsh is a liability. The DM may refuse. |
| Snow | 8 | |

Laden riders and pack animals multiply by 0.8. A mounted group of twenty or more multiplies by 0.8. A courier with fresh horses waiting at stations covers 50 to 80 miles a day on a good road; that is a system someone must build, not a rate anyone can claim.

## 3. Ox-cart

Carts need a road or firm open ground. Miles per day with a laden cart.

| Ground | Miles per day | Notes |
|---|---|---|
| Good road | 10 | Oxen walk at two miles an hour and work five or six hours. |
| Rough ground | 6 | Breakdowns are common. |
| Snow | 3 | Only on a known road under light snow. |
| Forest, mountain, marsh | no passage | Unless a road has been cut through, in which case use the road rate. |

A cart group multiplies by 0.8. Carts are already laden; no laden adjustment.

## 4. On water

| Mode | Miles per day | Notes |
|---|---|---|
| River boat, downstream | 30 | Drifting and rowing in daylight on a navigable river. Fast rivers in spring give more, with more risk. |
| River boat, upstream | 12 | Rowing, poling or towing from the bank. On a strong current the DM may halve it. |
| Coastal sailing | 50 | Daylight sailing with a fair wind, beaching or anchoring at night. Headwinds cut this to 15 or stop the boat. Expect one day in three lost waiting for weather. |
| Swimming | 2 | The longest open-water crossing an ordinary strong swimmer makes in a day, then rests. Cold water cuts this hard and kills the unlucky. |

Open sea, out of sight of land, is not on this table. Nobody in this age does it on purpose unless their people brought the craft from another star; if they did, the DM prices it with the Keeper.

Boats carry what people cannot. A river boat carries ten people or two tons of goods; the god who moves grain by water instead of by cart moves it ten times cheaper.

## 5. Work rates

Rates are given in worker-days: the number of days one worker needs for one unit of work. Days for the whole job are worker-days times units, divided by the number of workers. Workers here are ordinary adults with the tools of the age: bronze or stone axes, antler picks, wooden shovels, baskets.

More hands help only up to a point. The DM may argue crowding when the crew outgrows the job: forty people cannot all dig one well.

### Building

| Task | Worker-days | Per | Notes |
|---|---|---|---|
| Palisade | 2 | yard of wall | Felling, hauling, trenching and raising a wall of timbers eight to ten feet high. Fifty workers put 400 yards around a village in sixteen days. |
| Wooden hall | 300 | one hall | A great hall or longhouse of about 60 feet with posts, plank walls and a thatched roof. Timber should be felled a season ahead or the hall warps. |
| Stone wall | 6 | yard of wall | Rubble and mortar or fitted stone, ten feet high and four thick, with a footing. Dry stone to head height is 2. |
| Weir | 6 | yard of river width | A timber and stone weir across a river, for fish or to raise water for a mill or channel. A small fish weir in a stream is 20 worker-days flat. |
| Well, soil | 1.5 | foot of depth | Hand-dug and lined with stone or wicker. Thirty feet in a month for one digger and one hauler. |
| Well, rock | 5 | foot of depth | Fire-setting and antler picks. Slow, and sometimes dry at the bottom. |

### Earth and land

| Task | Worker-days | Per | Notes |
|---|---|---|---|
| Digging | 0.7 | cubic yard | Ditch, rampart or canal in ordinary soil with antler picks and baskets. Roughly a cubic yard and a half per worker per day. Clay or stony ground doubles it. |
| Clearing forest | 20 | acre | Felling and burning, stumps left to rot. Full stump removal for a plowed field is 60. |
| Planting | 1 | acre | With an ard plow and a team of oxen, then broadcast sowing. Five worker-days per acre with hoes and no oxen. |
| Harvest | 3 | acre | Reaping with sickles, binding and carrying in. Threshing happens later in the barn, over the winter. |

Planting and harvest happen in their seasons or not at all. In a temperate land the spring sowing window is about five weeks, with an autumn sowing of hardy grain where the people know the trick, and the grain harvest is a frantic three to four weeks in late summer. A people of 5,000 needs roughly 5,000 acres of grain under cultivation to eat, with fallow land besides; the math of hands and acres is what shapes a people's year.

### Crafting

| Task | Worker-days | Per | Notes |
|---|---|---|---|
| Boat, dugout | 30 | one boat | A single log hollowed by fire and adze, for four to six people on a river. |
| Boat, planked | 120 | one boat | Twenty feet, sewn or pegged planks, for ten people or two tons on a river or coast. Add a season for the timber to dry. |
| Bow | 3 | one bow | Shaping and tillering a seasoned stave, plus a string and a dozen arrows. The stave itself must season for one to two years; a bowyer keeps staves ahead. |
| Charcoal, batch | 30 | one clamp | Stacking, sealing, burning and cooling a clamp of about ten tons of wood, yielding two to three tons of charcoal. Three workers watch it for ten days. |
| Copper, smelt | 20 | ten pounds of metal | Ore crushing, a furnace of clay, charcoal and bellows for a day and a night, then breaking out the metal. Needs a charcoal batch for every few smelts. |
| Bronze, cast | 5 | one tool or weapon | Alloying copper with tin, a clay or stone mold, casting, grinding and hafting. Tin is the problem, not the labor; most lands have none. |

### Healing

Mortal bodies heal at mortal speed. The DM reports the course of a wound as the person who has it would know it.

| Wound | Time to heal | Notes |
|---|---|---|
| Bruises, scrapes, a shallow cut | 1 week | Fit for work within days. |
| Deep cut or stab, clean | 3 to 4 weeks | Fit for light work in two. Infection is the real danger; a fouled wound is a roll against death in the first ten days. |
| Broken arm or collarbone | 6 weeks | Set and splinted. A badly set bone heals crooked. |
| Broken leg | 10 to 12 weeks | No marching for three months. |
| Grave wound, survived | 3 months | A spear through the body, a crushed hand, a head blow. Half of such wounds kill. Some never fully heal. |
| Fever or camp sickness | 2 weeks | Longer in winter and in crowded quarters. |
| Exhaustion | 1 to 2 days | Rest and food. |

Gods can be wounded and cannot die. A god's wound heals on its power card's terms, or at mortal speed if the card is silent.

## 6. Season and weather

The baseline is a fair day in summer. The DM multiplies by these and says so.

| Condition | Travel | Work (outdoors) | Notes |
|---|---|---|---|
| Spring | 0.9 | 0.9 | Mud, swollen fords, rivers high. Downstream boats go faster. |
| Summer | 1.0 | 1.0 | Long days. Heat in dry lands cuts travel to 0.9 and the DM may move marching to night. |
| Autumn | 0.95 | 0.9 | Rains begin. Harvest takes every hand. |
| Winter | 0.7 | 0.6 | Short days, frozen ground, snow in the hills. Mountain passes and coastal sailing may close. Stone work stops in frost because mortar will not set. |
| Rain, steady | 0.8 | 0.7 | |
| Storm | 0.5 | 0 | Boats stay ashore. Nobody builds. |

Weather lands on top of season. A winter storm in the mountains stops everything, and the DM may simply say so.

## 7. How a god moves

A god moves at mortal pace unless its power card says otherwise. Its form has legs or wings or fins, and those move at the speed such things move. What a god does not have is a need for food or sleep. Sleep is a choice. So a god gains ground through endurance, not speed.

On foot, a god that never stops walks about sixteen hours where a mortal walks ten, and covers up to 1.6 times a mortal's daily distance. The remaining hours go to darkness, weather and ground that cannot be crossed blind. The DM may argue the number per terrain: a god in a marsh at night is no better off than anyone else, and a god in deep forest without moonlight may be held to the mortal rate.

Swimming is the mode where a god gains the most, because a mortal swimmer is limited by exhaustion, not speed. A god swims at about one mile an hour for as long as it likes and covers up to 20 miles in a day, though cold water still bites a mortal form and the DM may rule on it.

Riding, carts and boats with a crew move at the pace of the horse, the oxen or the rowers, and a god aboard changes nothing. A god rowing alone gains the same 1.6 as on foot. A god sailing alone may sail through the night along a coast it knows, for about 1.5 times the daylight rate, and wrecks like anyone else on a coast it does not.

Working, a god labors sixteen hours to a mortal's ten, so a god working alone counts as 1.6 workers. A god's strength beyond that is on its power card. All gods share occasional incredible feats; how often and how large is set in world-building, and the DM will say when one is in reach.

## 8. How much of the year is yours

A year holds about 365 days and four seasons, and every year opens in the same season. The DM will tell you the season when you ask. No calendar is shown; you decide how much time passes in a scene or a journey, and the DM holds you to what has already been decided.

That is a long time. Here is what fits in a year:

- Walking across a campaign region the size of a large country takes a season, not a year. A hundred miles of good road is five days; a hundred miles of mountain is two weeks.
- A village palisade is a month's work for fifty people. A hall is a season for twenty. A stone wall around a town is years, and the town's whole labor besides the harvest.
- A field is cleared in a season and planted the next spring. The first harvest from new land is about a year away from the first axe stroke.
- A charcoal clamp is a month from stacking to cold charcoal. A copper smelt is a week's work for a few people once the ore and the charcoal are at hand. A bronze blade is a week after that.
- A broken leg is a season. A grave wound is a season and a scar.

One to three scenes are played live each year, and god-scale decisions besides. The rest of the year is not lost. Time you do not spend in scenes still passes in the world, and your god is still in it: your standing orders run, your advisors and kings do what you told them, your tasks get done and your journeys arrive. Say "I will do this then" and it is scheduled; say "see to it" and it is delegated. Long tasks resolve overnight and the morning story tells you what came of them.

Where time is spent in the world and not in a scene, your god follows the conduct you set, or by default its own character, cautious and never reckless. Minor encounters resolve by that conduct. A major one is held for you: the morning story stops at the moment of contact and you play it live.

If you want to spend the whole year in the world, working with your hands and walking your land, you may. It counts.

---

## Quick reference

The same numbers as `tools/pace.py`. Travel in miles per day, work in worker-days per unit, adjustments as multipliers.

```
Route:  road = road row; path = rough row; river = boat up or down; sea = coastal sail; open ground = each region's terrain
Walk:   road 20, rough 14, forest 10, mountain 8, marsh 6, snow 6
Ride:   road 30, rough 20, forest 10, mountain 10, marsh 4, snow 8
Oxcart: road 10, rough 6, snow 3; no passage elsewhere
Boat:   downstream 30, upstream 12, coastal sail 50, swim 2
Laden x0.75 (ride x0.8); group x0.8
Season: spring 0.9, summer 1.0, autumn 0.95, winter 0.7 (work: 0.9, 1.0, 0.9, 0.6)
God: walk x1.6, swim 20 miles a day, row alone x1.6, sail alone x1.5, work x1.6

Palisade 2 per yard; hall 300; stone wall 6 per yard; weir 6 per yard of river
Well 1.5 per foot in soil, 5 in rock; digging 0.7 per cubic yard
Clear forest 20 per acre; plant 1 per acre; harvest 3 per acre
Dugout 30; planked boat 120; bow 3; charcoal clamp 30; copper smelt 20; bronze cast 5
```
