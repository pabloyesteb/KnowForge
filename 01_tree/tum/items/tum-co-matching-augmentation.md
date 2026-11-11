---
id: tum-co-matching-augmentation
source: tum-combinatorial-optimization
parent: co-bipartite
title: Alternating paths and maximum-cardinality matching
type: algorithm
caption: "Certifies cardinality optimality by absence of augmenting paths and explains symmetric-difference improvements."
---

# Alternating paths and maximum-cardinality matching

An alternating path switches between matching and nonmatching edges. If its two distinct endpoints are uncovered, toggling all its edges preserves the matching at internal vertices, covers both endpoints, and increases cardinality by one. Endpoint degrees change from zero to one; they do not remain unchanged as the surrounding lecture prose suggests.

For matchings \(M_1,M_2\), the graph of \(M_1\triangle M_2\) has maximum degree two. Each component is an alternating path or even alternating cycle. Cycles have equal numbers of edges from each matching, and each path has imbalance at most one. If \(|M_1|-|M_2|=k>0\), at least \(k\) vertex-disjoint components are \(M_2\)-augmenting paths. Hence a matching is maximum cardinality if and only if no augmenting path exists. The argument also applies to general graphs, since alternation itself makes the symmetric-difference cycles even; bipartiteness makes finding the paths simpler.

Start with the empty matching, find an augmenting path, toggle, and repeat. At most \(\lfloor|V|/2\rfloor\) augmentations are possible; a polynomial path finder yields a polynomial algorithm. An inclusion-maximal matching may still have a longer augmenting path: the exercises' phrase “maximal (on the number of edges)” denotes maximum cardinality, not merely the inability to add a single edge. The lecture's six-panel example illustrates revision of earlier pairings rather than permanently committing to greedy edges.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.2, Definitions/Theorems 4.7–4.9, pp. 70–72, full symmetric-difference proof and augmentation diagrams.
- `Problem Sheets/Exercise Sheet 9/exercise_sheet_9.pdf`, Exercise 1(a–b), p. 1; `Problem Sheets/Exercise Sheet 9 - solutiors/exercise_sheet_9 - sol.pdf`, Exercise 1(a–b), p. 1, toggling argument and polynomial iteration bound.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 3–8, alternating paths and complete sequential augmentation diagrams.
