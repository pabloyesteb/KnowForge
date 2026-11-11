---
id: tum-co-partition-matching
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Partition quotas and bipartite matching through intersected constraints
type: concept
caption: "Models disjoint-block quotas by a matroid and bipartite matchings by two endpoint-partition matroids."
---

# Partition quotas and bipartite matching through intersected constraints

Partition a finite ground set into disjoint blocks \(E_1,E_2\) and impose nonnegative integer quotas \(d_1,d_2\). The family
\[
\mathcal I=\{F\subseteq E:|F\cap E_1|\le d_1,\ |F\cap E_2|\le d_2\}
\]
is a partition matroid: it contains the empty set and is hereditary; when \(|J|>|I|\), some block contains more elements of \(J\) than \(I\), and an element in that block can augment \(I\) without exceeding its quota.

For a bipartite graph, partition its edge ground set once by left endpoint and once by right endpoint, giving every block quota one. Each constraint family is a partition matroid, but a matching must satisfy both. Thus matchings form their intersection; that intersection need not itself be a matroid, consistent with the four-vertex-path augmentation counterexample.

The lecture also encodes bipartite matching as flow: add a source linked to each left vertex, direct graph edges left-to-right, and link every right vertex to a sink, all with unit capacities. An integral feasible flow selects graph edges carrying one unit, and the source/sink unit capacities enforce at most one selected edge at each endpoint. Conversely, each matching gives such a flow of the same cardinality. Integrality is essential for reading a flow directly as a matching; a fractional flow is not itself an edge subset. The later matching chapter can develop the algorithmic consequences of this encoding.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/class notes for 10 May.pdf`, physical pp. 7–8, partition quotas and intersection/matching discussion; physical p. 11, unit-capacity matching-to-flow diagram.
- `Lecture Notes/class notes for 17 May.pdf`, physical p. 4, repeated matching-to-flow diagram.
