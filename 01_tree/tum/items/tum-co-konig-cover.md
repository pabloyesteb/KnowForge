---
id: tum-co-konig-cover
source: tum-combinatorial-optimization
parent: co-bipartite
title: Equality of maximum matching and minimum vertex cover
type: theorem
caption: "Uses Hall’s theorem to attain the universal vertex-cover bound in bipartite graphs."
---

# Equality of maximum matching and minimum vertex cover

A vertex cover meets every edge. Every cover has at least as many vertices as any matching has edges, because matching edges have disjoint endpoints. In bipartite graphs the minimum cover size equals the maximum matching size.

For the reverse inequality take a minimum-cardinality cover \(C\), writing \(C_A=C\cap A\) and \(C_B=C\cap B\). The induced graph between \(C_A\) and \(B\setminus C_B\) satisfies Hall: if \(S\subseteq C_A\) had fewer external neighbors than vertices, replacing \(S\) in \(C\) by those neighbors would produce a smaller cover. Thus a matching covers \(C_A\). Symmetrically a matching between \(C_B\) and \(A\setminus C_A\) covers \(C_B\). Their vertex sets are disjoint, so their union is a matching of size \(|C|\), attaining the lower bound. Edge-disjointness alone would not suffice for that union; disjointness of the four vertex classes justifies it. The theorem is specific to bipartite graphs.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.1, Definition 4.4 and Theorem 4.6 with full Hall-based proof, pp. 69–70.
- `Lecture Notes/class notes for 28 June.pdf`, physical pp. 22–23, vertex-cover definition and König statement.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 1–2, repeated statements.
