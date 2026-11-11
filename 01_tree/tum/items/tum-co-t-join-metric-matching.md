---
id: tum-co-t-join-metric-matching
source: tum-combinatorial-optimization
parent: co-general-matching
title: Nonnegative-cost T-joins through shortest-path matching
type: method
caption: "Pairs odd terminals in the shortest-path metric and restores original edges by parity."
---

# Nonnegative-cost T-joins through shortest-path matching

For nonnegative costs an optimal \(T\)-join can be chosen acyclic: delete any contained cycle without changing parity or increasing cost. With strictly positive costs no optimum contains a cycle. A forest join decomposes into edge-disjoint terminal-to-terminal paths, using every terminal as an endpoint exactly once, although terminals may also occur internally. Repeatedly remove a leaf-to-leaf path in a remaining tree and update the terminal set; parity is unchanged internally and flips at its endpoints.

A path in an optimal forest can be replaced by a cheaper original-graph path between its endpoints: toggling the old and replacement paths preserves parity, and nonnegative costs ensure the change costs no more than the replacement cost minus the removed path cost. Thus the terminal pairing can be represented using shortest paths. Construct the graph on \(T\), weighted by original shortest-path distances, and solve minimum-weight perfect matching there. For disconnected inputs, forbid infinite-distance pairs or work separately in each component; odd terminal count in any component proves infeasibility.

A decomposed original optimum gives a terminal matching with cost no greater than that optimum. Conversely expand a terminal perfect matching into shortest paths and retain edges occurring an odd number of times, taking their symmetric difference. This is a \(T\)-join with cost no greater than the sum of the path costs, proving equality of the optimal values. Ordinary set union is not sufficient when paths overlap; the exercise solution omits this parity cancellation. Nonnegativity is required for the cost comparison, and signed-cost joins require the more general treatment.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 11/exercise_sheet_11.pdf`, Exercise 1, p. 1, and Exercise 2(c–e), pp. 1–2, including supplied solutions within the task PDF.
- `Problem Sheets/Exercise Sheet 11 - solutions/exercise_sheet_11 - sol.pdf`, Exercise 1, p. 1, and Exercise 2(c–e), p. 2, full forest, path replacement and metric-matching arguments.
