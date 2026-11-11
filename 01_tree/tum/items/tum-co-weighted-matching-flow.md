---
id: tum-co-weighted-matching-flow
source: tum-combinatorial-optimization
parent: co-bipartite
title: Weighted bipartite matching as minimum-cost flow
type: method
caption: "Encodes optional pairings through unit-capacity arcs and a zero-cost bypass."
---

# Weighted bipartite matching as minimum-cost flow

A matching is an edge set with no shared endpoint; a perfect matching covers every vertex. Pairing professors with courses gives a bipartite model, while pairing people with each other may give a general graph. Maximum weight and maximum cardinality are different objectives. For a bipartition \(A\cup B\), orient admissible pairings from \(A\) to \(B\), put unit capacities on these arcs and on auxiliary \(s\to A\) and \(B\to t\) arcs. Integral maximum flow gives maximum cardinality. Multiple places can be represented by identical vertex copies, each with the original neighbors.

For maximum weight, assign pairing cost \(-w(a,b)\), zero cost on auxiliary arcs, and balances \(b(s)=K,b(t)=-K\) for \(K\) at least any matching cardinality. A direct \(s\to t\) bypass of capacity \(K\) and cost zero carries unused pairing slots. Integral feasible flows correspond to matchings plus bypass flow, with objective exactly \(-w(M)\). Integrality is essential when reading unit-flow pairing arcs as selected edges. A zero-cost bypass also handles negative weights correctly by permitting vertices to remain unmatched; the source's proposed high-cost bypass for signed weights instead biases cardinality and does not preserve arbitrary maximum-weight matching.

With all weights one, a negative residual cycle contains the backward bypass \(t\to s\) and an alternating path through the bipartite graph. Forward pairing arcs cost −1, backward ones +1; toggling the path adds one matching edge and reduces cost by one. Minimum-mean cycle cancellation therefore becomes an augmenting-path variant. Its mean criterion favors shorter such cycles among equal cost improvements.

The maximal-matrix-sum supplement is the fixed-cardinality assignment version: one node per row and column, unit source/row and column/sink arcs, pairing cost \(-M_{ij}\), and exactly \(n\) units of flow with no bypass. There are \(2n+2\) vertices and \(n^2+2n\) arcs. Every row and column is used exactly once in an integral solution. Its three-by-three example selects entries 4, 6 and 8 for total 18, corresponding to minimum flow cost −18.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Chapter 4 introduction and §4.1, pp. 66–69, Problems 4.2–4.3 and both flow reductions.
- `Lecture Notes/class notes for 28 June.pdf`, physical pp. 12–22, models, coverage and full flow transformations.
- `Problem Sheets/Exercise Sheet 9/exercise_sheet_9.pdf`, Exercise 1(c), p. 1; `Problem Sheets/Exercise Sheet 9 - solutiors/exercise_sheet_9 - sol.pdf`, Exercise 1(c), p. 1 (corrects task wording from perfect to optional matching).
- `Student Submitted Exercises/Jasmin El-Wafi.pdf`, pp. 1–4, full matrix task, reduction, numerical example and network diagram.
