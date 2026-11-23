# Rulings from Michael during the run (sim-04)

Written only by the orchestrator, from Michael's words in chat, quoted, with the Pacific time and the question he answered. Each entry carries Michael's go for exactly what it says.

## 2026-11-22, about 12:05 Pacific

Question: the lock is stuck on a leak flag only Michael can rule on. The player gave a mortal a name openly at the Day 3 table; the same name sits in the sealed record and on the sealed-terms list, and the scan fails 19 times. The checker ruled none of the hits reveals anything, but its rules forbid allow-listing a sealed term or removing one from the list. What rule should cover a sealed term the player has said openly?

Michael chose: "Open name leaves the list (Recommended)": a name the player says in the open table talk is never a sealed term; it comes off the list, the scan passes, and this becomes a standing rule.

Applied as a standing rule by the orchestrator on Michael's go: `tools/lockcheck.py --leaks` lets through any sealed term found in a "## Player:" section of a creation transcript; `engine/roles/checker.md` and runbook section on sealed terms say so.
