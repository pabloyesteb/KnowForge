---
id: tum-co-shortest-path-regimes
source: tum-combinatorial-optimization
parent: co-foundations
title: Choosing shortest-path algorithms by graph and weight assumptions
type: method
caption: "Matches acyclicity and edge-cost restrictions to linear-time DAG, Dijkstra and Bellman–Ford bounds."
---

# Choosing shortest-path algorithms by graph and weight assumptions

The shortest-path problem seeks an \(s\)-to-\(t\) path minimizing the sum of its arc costs; an unreachable target has no such path. The prerequisite results distinguish three regimes, with \(n\) vertices and \(m\) arcs:

- In a directed acyclic graph, use a topological order and relax outgoing arcs after their predecessors have been processed. This takes \(O(n+m)\) operations and permits negative costs because no directed cycle can occur.
- With nonnegative costs in a general digraph, Dijkstra's algorithm applies. A basic implementation takes \(O(n^2)\), while the stated Fibonacci-heap bound is \(O(m+n\log n)\); the prerequisite notes do not develop the advanced data structure.
- With negative costs, Bellman–Ford gives the stated \(O(nm)\) bound when no relevant negative cycle occurs, and its extension detects a negative cycle. The notes impose the stronger global absence of negative cycles for the shortest-path assertion.

A negative cycle that can be reached from \(s\) and can reach \(t\) makes costs of unrestricted \(s\)-to-\(t\) traversals unbounded below; it must not be confused with minimizing over simple paths or with a negative cycle in an irrelevant component. Dijkstra's nonnegativity condition cannot be dropped merely because a particular graph happens to have a finite answer.

Exercise 3 supplies a directed weighted graph including an arc of cost \(-3\); the official answer states minimum path weight 11. In its diagram a route attaining 11 goes from \(s\) to the middle-left vertex (4), the center (3), the top vertex immediately right of \(s\) (−3), the next top vertex (3), the lower vertex beneath it (1), then \(t\) (3). This is a weighted example distinct from the unit-edge maze task.

The continuation states Bellman–Ford's dynamic-programming viewpoint: track minimum costs of source-to-vertex traversals of a prescribed number of edges. Such traversals may repeat vertices and edges, so they use a broader convention than the course's edge-nonrepeating “walk” definition. The notes' Theorem 1.17 states shortest path or negative-cycle output in \(O(nm)\).

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §1.3, p. 9, Theorems 1.15–1.16 and Bellman–Ford statement.
- `Lecture Notes/class notes for 19 April.pdf`, printed slides 29–31 (physical pp. 44–47).
- `Problem Sheets/Exercise Sheet 1/exercise_sheet_1.pdf`, Exercise 3, p. 1; `Problem Sheets/Exercise Sheet 1 - solutions/exercise_sheet_1 - sol.pdf`, Exercise 3 diagram and answer, p. 2.
- `Lecture Notes/lecture notes.pdf`, Theorem 1.17 and fixed-edge-count dynamic-programming paragraph, p. 10, before Chapter 2.
