---
id: tum-co-mst-certificates
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Tree structure and cut/cycle certificates for minimum spanning trees
type: theorem
caption: "Characterizes minimum spanning trees through local exchanges across fundamental cuts and cycles."
---

# Tree structure and cut/cycle certificates for minimum spanning trees

A forest is cycle-free; a tree is a connected forest. On \(n\) vertices, a tree has \(n-1\) edges and a unique path between every pair. Conversely, connectivity together with \(n-1\) edges, or acyclicity together with \(n-1\) edges, characterizes a tree. Removing any tree edge disconnects it into two components; adding a non-tree edge creates exactly one cycle. A forest with \(p\) components has \(n-p\) edges.

For a connected undirected graph with rational edge costs, a minimum spanning tree minimizes the sum of its \(n-1\) edge costs. Given a spanning tree \(T\), the following are equivalent:

- \(T\) has minimum weight.
- For every non-tree edge \(e=\{u,v\}\), all edges of the unique \(u\)-to-\(v\) path in \(T\) have cost at most \(c(e)\).
- Each tree edge is cheapest across the cut formed by deleting it from \(T\).
- Its edges can be ordered so that each is cheapest across a cut crossed by none of the preceding chosen edges.

The exchange arguments explain necessity: replacing a more expensive tree edge on a fundamental cycle, or reconnecting a fundamental cut with a cheaper edge, improves the tree. For sufficiency of the ordered-cut criterion, choose an optimum agreeing with the proposed tree for the longest initial edge prefix. Add the first missing edge to this optimum. Its cycle must cross the certifying cut again; that other crossing edge is not in the agreed prefix. Exchanging it preserves optimal cost by the cheapest-cut property and increases the agreement, a contradiction. The fundamental-cut condition supplies such a certificate for any ordering of \(T\).

The MST formulation permits negative costs even though the algorithm boxes restrict inputs to nonnegative costs: shifting every cost by the same constant leaves the ordering and every spanning-tree comparison unchanged, since all trees have \(n-1\) edges. Likewise \(c'(e)=M-c(e)\), with \(M>\max_e c(e)\), turns minimization into positive-weight maximization because \(c'(T)=(n-1)M-c(T)\). This fixed-cardinality argument does not apply to arbitrary feasible sets of different sizes.

A maximum-weight edge of any cycle can be deleted while preserving at least one MST. If an optimum uses it, delete it to form a fundamental cut and choose another edge of that cycle crossing this cut. Its weight is no larger, and exchanging restores a spanning tree of optimal cost. An arbitrary other cycle edge need not reconnect the cut; the supplement's replacement step needs that choice. Ties allow the deleted edge to belong to some other optimum.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §§2.1–2.2, pp. 10–14, Definitions 2.1–2.3 and Theorem 2.4 with proof; Remark 2.9, p. 16.
- `Lecture Notes/class notes for 26 April.pdf`, physical pp. 1–17, tree definitions, complete MST characterization/exchange proof and cut/cycle diagrams.
- `Lecture Notes/class notes for 03 May.pdf`, physical p. 3, maximization transformation.
- `Student Submitted Exercises/Saghar Rezaei .pdf`, p. 1(a), cycle-edge deletion statement, exchange proof and diagrams.
