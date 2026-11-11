---
id: tum-co-order-preserving-matching
source: tum-combinatorial-optimization
parent: co-bipartite
title: Dynamic programming for order-preserving weighted matching
type: algorithm
caption: "Optimizes noncrossing assignments through prefix subproblems and traceback."
---

# Dynamic programming for order-preserving weighted matching

Let ordered bipartition classes be \(A=(a_1,\ldots,a_p)\), \(B=(b_1,\ldots,b_q)\). A matching is order-preserving when \(i<i'\) implies \(j<j'\) for every two selected pairs \((a_i,b_j),(a_{i'},b_{j'})\). Let \(D(i,j)\) be the best weight using the two prefixes. Set \(D(i,0)=D(0,j)=0\) and compute
\[
D(i,j)=\max\{D(i-1,j),D(i,j-1),D(i-1,j-1)+w(a_i,b_j)\},
\]
including the third candidate only when that edge exists. The source omits this necessary admissibility guard for a noncomplete input graph.

If either last vertex is unused, the solution lies in the corresponding smaller prefix. If both are used, order preservation forces them to be paired together; two distinct partners would reverse the required order. Removing that pair leaves the smaller diagonal prefix. Induction proves the recurrence, including signed weights because skipping vertices and the empty matching remain available. The table takes \(O(pq)\) arithmetic operations and storage; retain predecessor choices or trace maximizing candidates backward to recover a matching, rather than just its value.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 9/exercise_sheet_9.pdf`, optional Exercise 3, p. 1; `Problem Sheets/Exercise Sheet 9 - solutiors/exercise_sheet_9 - sol.pdf`, Exercise 3, pp. 2–3, full prefix recurrence, induction and reconstruction.
