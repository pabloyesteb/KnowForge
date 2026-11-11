---
id: tum-co-mst-connected-restriction
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Connected induced restrictions of a minimum spanning tree
type: theorem
caption: "Shows that replacing a connected subtree by a cheaper local tree would improve the global spanning tree."
---

# Connected induced restrictions of a minimum spanning tree

Let \(T\) be an MST of \(G\), and let \(W\subseteq V\) induce a connected subtree \(T[W]\). Then \(T[W]\) is an MST of the induced graph \(G[W]\). Otherwise replace it by a cheaper spanning tree on \(W\), retaining every other edge of \(T\). Contracting \(W\) in the original tree shows the replacement is connected and has no cycle; equivalently it has \(|V|-1\) edges and remains connected. Its cost is strictly lower, contradicting global optimality. The connectedness hypothesis is essential: an arbitrary vertex restriction of a spanning tree may be a forest and need not span its induced graph. The submission's replacement proof needs this connectivity or contraction argument; separately being acyclic on two regions does not alone exclude a cycle through both.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Saghar Rezaei .pdf`, p. 1(b), full connected-induced-subtree statement, replacement proof and diagrams.
