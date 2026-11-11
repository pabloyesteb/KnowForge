---
id: tum-co-chinese-postman
source: tum-combinatorial-optimization
parent: co-general-matching
title: Minimum street-covering tours through parity correction
type: method
caption: "Adds a minimum-cost odd-vertex join to make a connected network Eulerian."
---

# Minimum street-covering tours through parity correction

In a connected undirected graph with nonnegative street costs, find a minimum-cost closed walk visiting every edge and returning to the disposal facility. Every feasible walk pays \(\sum_{e\in E}w(e)\) once, so optimization concerns only additional traversals \(\sum_e w(e)(r_W(e)-1)\). Let \(T\) be the odd-degree vertices of the original graph. Duplicate one copy of each edge in a minimum-cost \(T\)-join. The resulting connected multigraph has even degrees everywhere, so an Euler tour yields a feasible street-covering walk with added cost equal to the join cost.

Conversely, additional traversals in any feasible tour have odd-degree set \(T\). Keeping only edges with odd extra multiplicity gives a \(T\)-join whose cost is no greater than the total extra traversal cost, by nonnegativity. Hence minimum duplication cost equals minimum join cost. A feasible join always exists here: the original full edge set has odd-degree set \(T\), equivalently doubling every street makes all degrees even. If the graph is already Eulerian, no extra cost is needed. Any cycle contained in an optimal nonnegative-cost join must consist entirely of zero-cost edges, because deleting it preserves parity; removing such cycles gives the forest/path form used in shortest-path matching.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 11/exercise_sheet_11.pdf`, Exercise 2(a–e), pp. 1–2, garbage-collection model and supplied solution.
- `Problem Sheets/Exercise Sheet 11 - solutions/exercise_sheet_11 - sol.pdf`, Exercise 2(a–e), pp. 1–2, Eulerization and optimal-cycle/shortest-path arguments.
