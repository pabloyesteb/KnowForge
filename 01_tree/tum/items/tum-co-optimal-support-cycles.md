---
id: tum-co-optimal-support-cycles
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Zero-cost cycles in the union of optimal flow supports
type: theorem
caption: "Uses convex averaging and cycle subtraction to characterize cycles supported by optimal flows with nonnegative costs."
---

# Zero-cost cycles in the union of optimal flow supports

Assume all arc costs are nonnegative and let \(F\) contain every arc used positively by at least one minimum-cost feasible flow. If a directed cycle \(C\) lies in \(F\), then one optimal flow is positive on all its arcs simultaneously. For each cycle arc choose an optimum positive on that arc and average these finitely many flows. Capacity bounds and balance equations are preserved by averaging, the objective remains the common optimum, and each cycle arc receives a positive contribution.

Let \(\gamma>0\) be the smallest flow on this cycle in the averaged solution. Subtract \(\gamma\) from every cycle arc. Conservation and nonnegative flow are preserved, and upper capacities remain satisfied. If any cycle arc had strictly positive cost, this would strictly lower the objective because all other cycle costs are nonnegative. Therefore every arc of \(C\) has cost zero.

The union of individually optimal supports is not itself a feasible flow; averaging is what justifies simultaneous positivity. The conclusion concerns directed cycles and nonnegative costs, not arbitrary cycles in an underlying undirected graph or signed-cost instances.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 7/exercise_sheet_7.pdf`, Exercise 2, p. 1; `Problem Sheets/Exercise Sheet 7 - solutions/exercise_sheet_7 - sol.pdf`, Exercise 2(a–b), p. 2, full averaging and cycle-subtraction proof.
