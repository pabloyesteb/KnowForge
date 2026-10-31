---
id: tum-co-dijkstra-maze
source: tum-combinatorial-optimization
parent: co-foundations
title: Dijkstra labels and unit-edge maze path reconstruction
type: algorithm
caption: "Relates minimum-distance vertex selection to a supplied Python grid-maze implementation and its unit-weight assumptions."
---

# Dijkstra labels and unit-edge maze path reconstruction

Dijkstra initializes \(d(s)=0\) and all other labels to infinity, repeatedly selects an unvisited vertex with the smallest finite label, settles it, and relaxes its outgoing edges by \(d(v)\leftarrow\min\{d(v),d(u)+c(u,v)\}\). Nonnegative costs justify finality of settled labels. In a general weighted graph, stop when the target is settled, or when no finite unvisited label remains; first discovery alone does not establish a weighted shortest path.

The supplied Python exercise implements the special case of undirected unit-weight grid edges. Vertices are consecutive integer indices; a dictionary maps endpoint tuples to weight 1, and adjacency is tested at either endpoint. `random_graph.py` samples each horizontal/vertical edge with parameter `p`, seeding from the current timestamp. Despite “weighted” names, this generator does not sample varying edge costs.

The missing `minDistance` routine is a linear scan of all vertices for the smallest finite unvisited distance, returning −1 if none exists. Both provided solution files implement that scan. The surrounding algorithm initially marks the source visited, initializes its neighbors to distance 1, and repeatedly relaxes edges by adding 1. It stops as soon as `dist[t]` becomes finite. That early-discovery rule is supported here by equal edge lengths and increasing distance layers; extending it to arbitrary nonnegative weights would be incorrect. Isolated or disconnected targets terminate with infinite distance.

The returned pair contains discovery/relaxation edges and a distance array, rather than the dictionary of shortest-path edges claimed in a comment. `maze.py` traces backward from the target along recorded edges whose opposite endpoint has distance one less, then draws the route separately from explored edges. Grid coordinates map vertices to every other square and edges to their midpoint squares; the displayed square count is \(2(d(t)+1)\), which differs from graph edge distance. The driver exposes grid dimensions, block size and sampling probability; it prints timings but supplies no fixed measured benchmark.

The renderer explicitly imports `processing_py`, a visualization dependency named by the sheet as `processing-py`. The starter and completed routines are supplied instructional code, not evidence of personal authorship. Their list scans and repeated full edge filtering do not implement the lecture's Fibonacci-heap complexity.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §1.3, p. 9, nonnegative-cost Dijkstra theorem.
- `Problem Sheets/Exercise Sheet 1/exercise_sheet_1.pdf`, Exercise 4, pp. 2–3; `Problem Sheets/Exercise Sheet 1 - solutions/exercise_sheet_1 - sol.pdf`, Exercise 4, pp. 2–4, maze screenshots and task.
- `Problem Sheets/Exercise Sheet 1/dijkstra.py`, `minDistance` scaffold and `dijkstra_algorithm`; `Problem Sheets/Exercise Sheet 1 - solutions/code - sol.py` and `Problem Sheets/Exercise Sheet 1 - solutions/dijkstra_complete.py`, completed selection routine and unit-edge algorithm.
- `Problem Sheets/Exercise Sheet 1/main.py`, full driver; `Problem Sheets/Exercise Sheet 1/random_graph.py`, `Graph.build_weighted_grid`; `Problem Sheets/Exercise Sheet 1/maze.py`, full grid geometry, drawing and `draw_solution` path reconstruction.
