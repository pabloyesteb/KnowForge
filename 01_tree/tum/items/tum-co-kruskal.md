---
id: tum-co-kruskal
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Kruskal forests and component merging for grid mazes
type: algorithm
caption: "Builds a minimum spanning tree by sorted edge acceptance and relates cycle tests to a supplied Python component-set implementation."
---

# Kruskal forests and component merging for grid mazes

Sort edges in nondecreasing cost order and start with the forest \((V,\varnothing)\). Accept an edge exactly when its endpoints belong to distinct current components; merge those components. This condition is equivalent to not creating a cycle. For a connected graph the result is a spanning tree.

A rejected edge already has a path between its endpoints made from earlier edges of no greater cost. That path remains in the final tree. Hence every rejected edge satisfies the fundamental-cycle MST certificate, proving optimality. Prim keeps one growing connected component; Kruskal can grow several components before joining them. Ties may give different optimal edge sets.

The elementary analysis sorts in \(O(m\log m)\) and tests each prospective edge by a search in the current forest, taking \(O(n)\) per edge and \(O(mn)\) overall for the simple-graph setting. The notes also state the improved \(O(m\log m+m\alpha(m,n))\) bound using an advanced component data structure; the provided Python code is not that implementation.

In Sheet 2, a rectangular grid contains every horizontal/vertical edge with independently sampled integer costs from 0 to 99. The completed code sorts dictionary entries by cost, represents components as a set of immutable `frozenset` vertex sets, finds the two endpoint components by scans, and replaces them with their union when distinct. It returns a dictionary of selected endpoint tuples and original weights. The starter instead returns the entire input edge dictionary, leaving all grid cycles present.

The grid tree defines a maze with exactly one graph path between every pair of cells. `maze.py` maps vertices and edge midpoints to display squares, labels costs and offers incremental or final rendering through `processing_py`. The driver exposes dimensions/block size and prints total selected cost and timings. The supplied screenshots illustrate full-grid and tree mazes; they provide no fixed benchmark or personal implementation result.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §2.3, pp. 15–16, Algorithm 2, Theorem 2.7, Remark 2.8 and Figure 11.
- `Lecture Notes/class notes for 26 April.pdf`, physical pp. 17–19, algorithm and example; `Lecture Notes/class notes for 03 May.pdf`, physical pp. 1–2, runtime and annotated tree.
- `Problem Sheets/Exercise Sheet 2/exercise_sheet_2.pdf`, Exercises 1 and 4, pp. 1–3; `Problem Sheets/Exercise Sheet 2 - solutions/exercise_sheet_2 - sol.pdf`, corresponding material, pp. 1–4.
- `Problem Sheets/Exercise Sheet 2/kruskal.py`, full scaffold; `Problem Sheets/Exercise Sheet 2 - solutions/code - sol.py` and `Problem Sheets/Exercise Sheet 2 - solutions/kruskal_complete.py`, full completed `kruskals_algorithm`.
- `Problem Sheets/Exercise Sheet 2/main.py`, full driver; `Problem Sheets/Exercise Sheet 2/random_graph.py`, full `Graph` and grid generator; `Problem Sheets/Exercise Sheet 2/maze.py`, full coordinate/drawing routines.
