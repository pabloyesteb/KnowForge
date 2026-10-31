---
id: tum-co-prim
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Prim growth across a cheapest boundary edge
type: algorithm
caption: "Grows one connected tree and maintains cheapest connecting edges to obtain a quadratic-time MST algorithm."
---

# Prim growth across a cheapest boundary edge

Start with an arbitrary vertex \(v_0\) of a connected undirected weighted graph. While the selected vertex set \(S\) is not all of \(V\), add a cheapest edge of \(\delta(S)\), together with its exterior endpoint. Exactly one vertex joins at each step, so the partial graph stays connected and cycle-free and finishes as a spanning tree after \(n-1\) additions.

Each selected edge is minimum on a cut crossed by none of the earlier selected edges. The ordered-cut optimality certificate therefore proves minimum total weight. Ties can be resolved arbitrarily, but can lead to different optimum trees; the initial vertex can also change the selection order. The worked eight-vertex lecture example has optimum weight 14. Sheet 2's separate execution graph has stated MST cost 23; neither figure asserts a unique edge order without a starting point and tie rule.

For an \(O(n^2)\) implementation, store for each exterior vertex the cheapest edge connecting it to the current tree, or infinity if none exists. Scan these keys to choose the next vertex and update keys using edges incident to the newly added vertex. Each iteration uses \(O(n)\) work with suitable adjacency access, over \(n-1\) iterations. The notes also state \(O(m+n\log n)\) using a Fibonacci heap, without developing that data structure. Connectedness ensures a crossing edge exists until completion; a disconnected input requires separate component forests rather than one spanning tree.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §2.2, pp. 12–14, Algorithm 1, Figure 8, Theorem 2.5 and Remark 2.6.
- `Lecture Notes/class notes for 26 April.pdf`, physical pp. 6–14, recurrence of cheapest cuts, annotated weight-14 example and correctness/runtime proof.
- `Problem Sheets/Exercise Sheet 2/exercise_sheet_2.pdf`, Exercise 1, p. 1; `Problem Sheets/Exercise Sheet 2 - solutions/exercise_sheet_2 - sol.pdf`, Exercise 1(c), p. 1, stated weight 23.
