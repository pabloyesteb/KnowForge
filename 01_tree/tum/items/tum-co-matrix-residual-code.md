---
id: tum-co-matrix-residual-code
source: tum-combinatorial-optimization
parent: co-max-flow
title: Mutable residual matrices for augmenting-path flow algorithms
type: method
caption: "Tracks parent chains, bottlenecks and paired residual updates in the supplied Python flow routines."
---

# Mutable residual matrices for augmenting-path flow algorithms

The supplied `Graph` stores an adjacency matrix as its mutable residual capacity matrix. Stack and FIFO searches traverse entries with positive capacity and record a parent on first discovery. Each successful search supplies a source-sink parent chain; walk backward to find its minimum residual capacity, then walk backward again to subtract that bottleneck from each forward matrix entry and add it to the transposed entry. Increment the accumulated flow value by the same amount. The completed Ford-Fulkerson routine uses the stack search, and the completed Edmonds-Karp routine uses FIFO search.

The residual invariant is \(r(u,v)=c(u,v)-F(u,v)\), where \(F\) is antisymmetric net flow. Paired updates therefore also accommodate antiparallel capacities by combining cancellation with opposite-direction spare capacity in one entry. This representation returns the maximum value, not a separate nonnegative flow for every original directed arc. It differs from the lecture's arc-by-arc representation that first removes antiparallel arcs.

The starter leaves the residual update empty and Edmonds-Karp returning zero. With a reachable sink, unchanged residual capacities cause the Ford-Fulkerson loop to rediscover paths without progress. The official completion supplies the paired update and duplicates the augmentation loop with FIFO search. The driver copies every matrix row before each algorithm, preventing one mutated residual state from becoming the other's input.

Each search scans a full row per processed vertex, taking \(O(n^2)\) work; its Python queue uses `pop(0)`, which is not the abstract constant-time dequeue. Thus the adjacency-list BFS \(O(n+m)\) bound cannot be assigned to this code unchanged. The random generator samples integer entries, clamps negative samples to zero, suppresses diagonal entries, and permits antiparallel arcs. The driver prints elapsed times for a manual matrix or optional random instance; no fixed performance measurements are supplied. These are instructional reference implementations, not personally attributable software.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 4/exercise_sheet_4.pdf` and `Problem Sheets/Exercise Sheet 4 - solutions/exercise_sheet_4 - sol.pdf`, Exercise 4, task pp. 2–3 and solution pp. 3–4.
- `Problem Sheets/Exercise Sheet 4/graph_module.py`, full scaffold and search routines; `Problem Sheets/Exercise Sheet 4/main.py`, full driver and row copying.
- `Problem Sheets/Exercise Sheet 4 - solutions/graph_module - complete.py`, full generator, searches, both flow loops and `update_residual`.
