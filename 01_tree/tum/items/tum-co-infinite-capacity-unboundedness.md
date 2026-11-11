---
id: tum-co-infinite-capacity-unboundedness
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Unbounded minimum-cost flows with infinite-capacity cycles
type: theorem
caption: "Characterizes unbounded cost improvement by a negative cycle entirely within infinite-capacity arcs."
---

# Unbounded minimum-cost flows with infinite-capacity cycles

For a feasible finite network allowing infinite capacities, minimum-cost flow is unbounded below exactly when some negative-cost directed cycle has infinite capacity on every arc. Any positive multiple of that cycle can be added to a feasible flow, preserving balances and driving cost to minus infinity.

Conversely, decompose an improving difference from a fixed feasible flow into positive cycle multiples in its residual graph. Reverse residual capacities are finite because the fixed flow is finite. If no negative cycle uses only infinite forward capacities, every negative residual simple cycle includes a finite-capacity arc, bounding its coefficient by that finite bottleneck. There are only finitely many simple cycles, so the sum of their maximum possible negative contributions has a finite lower bound; nonnegative-cost cycles cannot lower it. Hence costs cannot tend to minus infinity.

To decide unboundedness, restrict to original arcs of infinite capacity and detect a negative cycle anywhere in that subgraph with Bellman–Ford, using an auxiliary zero-cost source reaching all vertices. Feasibility is an explicit prerequisite; an infeasible instance is not unbounded in this sense. The source's converse instead modifies finite-edge costs; its stated increment mixes cycle cost with bottleneck units, so the finite-cycle bound above makes the required boundedness argument explicit without using that increment formula.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 6/exercise_sheet_6.pdf`, Exercise 2, p. 1; `Problem Sheets/Exercise Sheet 6 - solutions/exercise_sheet_6 - sol.pdf`, Exercise 2(a–b), pp. 1–2.
