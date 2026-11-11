---
id: tum-co-regular-bipartite-decomposition
source: tum-combinatorial-optimization
parent: co-bipartite
title: Perfect-matching decomposition of regular bipartite graphs
type: theorem
caption: "Applies Hall’s condition repeatedly to partition every edge of a regular bipartite graph."
---

# Perfect-matching decomposition of regular bipartite graphs

For a finite \(k\)-regular bipartite graph with \(k>0\), count edges from \(S\subseteq A\): \(k|S|\le k|\Gamma(S)|\). Hall's condition gives a matching covering \(A\). Counting all edges as \(k|A|=k|B|\) shows the two parts have equal size, so this matching is perfect. Remove it; every degree decreases by one and the residual graph remains bipartite. Repeat to partition the edges into \(k\) edge-disjoint perfect matchings. These matchings share vertices, necessarily, but no edges. For \(k=0\) the empty collection partitions the empty edge set; the division and equal-part-size argument is used only when \(k>0\).

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Julian Streit.pdf`, p. 1, full Hall/counting/recursive deletion proof.
