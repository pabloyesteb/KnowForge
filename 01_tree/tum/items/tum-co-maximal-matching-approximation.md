---
id: tum-co-maximal-matching-approximation
source: tum-combinatorial-optimization
parent: co-bipartite
title: Half-optimal cardinality of any maximal matching
type: theorem
caption: "Charges optimum edges to endpoints of a maximal matching to obtain a factor-two bound."
---

# Half-optimal cardinality of any maximal matching

An inclusion-maximal matching admits no additional edge; a maximum matching has largest possible cardinality. Let \(M\) be maximal and \(M^*\) any other matching. Every edge of \(M^*\) must touch an endpoint of \(M\), or it could be added. Each edge of \(M\) has two endpoints, and each endpoint can meet at most one edge of \(M^*\). Therefore \(|M^*|\le2|M|\). Selecting arbitrary available edges until none remain gives a one-half approximation for maximum cardinality. This endpoint argument applies to general graphs as well as the bipartite setting of one submission. It supplies no analogous guarantee for arbitrary edge weights. The four-vertex path with only its middle edge selected attains the bound against the two outer edges.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Ketelhut Vanessa.pdf`, pp. 1–2, handwritten maximal/maximum definitions, incidence bound and example diagram.
- `Student Submitted Exercises/Zehong Ruan.pdf`, p. 1, general-graph counting proof; the final set-difference notation must choose an addable edge from the comparison matching, as the preceding proof explains.
