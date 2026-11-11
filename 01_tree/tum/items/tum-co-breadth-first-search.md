---
id: tum-co-breadth-first-search
source: tum-combinatorial-optimization
parent: co-max-flow
title: FIFO breadth-first search, shortest paths and cycle detection
type: method
caption: "Uses discovery labels and parent forests to obtain unweighted shortest paths and detect undirected cycles."
---

# FIFO breadth-first search, shortest paths and cycle detection

Maintain a FIFO queue, mark the source discovered before enqueueing it, and repeatedly remove the oldest vertex and discover each unmarked neighbor. Mark on insertion so each vertex enters the queue at most once. With adjacency lists and constant-time queue operations, scanning all vertices and incidences costs \(O(n+m)\). In a digraph, neighbors must follow outgoing arcs; the relevant question is directed reachability, not just connected-component membership.

Set \(d(s)=0\), and on discovering \(v\) from \(u\), record \(d(v)=d(u)+1\) and parent \(u\). FIFO order processes all distance-\(k\) vertices before distance-\(k+1\), proving the labels are shortest edge counts. Following parents reconstructs a shortest path. Handle \(s=t\) immediately; an exhausted queue without discovering the target proves unreachability.

For a simple undirected graph, explore a parent forest and stop at the first edge joining already discovered vertices that is not the parent edge. The two tree paths, after removing their shared prefix, and this extra edge form a cycle. Search all components to certify acyclicity. With adjacency lists, stop-at-first-cycle exploration examines only forest edges and the first extra edge, giving \(O(n)\) work including reconstruction; an acyclic graph itself has at most \(n-1\) edges. This specialized bound does not include reading an arbitrary dense input matrix or apply unchanged to directed cycle detection. The sheet's instruction to include an edge in the auxiliary tree before testing it is understood as retaining a forest and treating the first nontree edge separately.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 4/exercise_sheet_4.pdf` and `Problem Sheets/Exercise Sheet 4 - solutions/exercise_sheet_4 - sol.pdf`, Exercise 1(a–c), task p. 1 and solutions pp. 1–2.
