---
id: tum-co-hall-marriage
source: tum-combinatorial-optimization
parent: co-bipartite
title: Hall condition for covering one side of a bipartite graph
type: theorem
caption: "Characterizes complete assignment through neighborhood sizes and an inductive splitting proof."
---

# Hall condition for covering one side of a bipartite graph

A bipartite graph \(G=(A\cup B,E)\) has a matching covering every vertex of \(A\) exactly when \(|\Gamma(S)|\ge|S|\) for every \(S\subseteq A\). Necessity follows from the distinct partners of the matched vertices in \(S\). This covers one designated side; perfection additionally requires coverage of the other side, for example when both sides have equal size.

For sufficiency induct on \(|A|\). If every nonempty proper subset has strict slack, remove any edge and both endpoints. Every remaining neighborhood loses at most one vertex, so Hall's condition survives; extend the inductive matching with that edge. Otherwise take a nonempty proper tight set \(S\) with \(|\Gamma(S)|=|S|\). Match the induced graph on \(S\cup\Gamma(S)\) by induction. In the complementary graph, for \(T\subseteq A\setminus S\),
\[
|\Gamma(T)\setminus\Gamma(S)|=|\Gamma(S\cup T)|-|\Gamma(S)|\ge|T|.
\]
Match the complement by induction and unite the two vertex-disjoint matchings. A violating subset is a concrete obstruction to complete assignment.

Sheet 10 gives a constructive obstruction from a maximum matching that leaves \(v\in A\) uncovered. Let \(A_v,B_v\) be vertices reachable from \(v\) by alternating paths in their respective parts, including the length-zero root. Every neighbor of \(A_v\) lies in \(B_v\), and every reached right vertex is such a neighbor. No reached right vertex is uncovered, or it would end an augmenting path. Its matched partner is reached on the left, giving a bijection between \(B_v\) and \(A_v\setminus\{v\}\). Consequently \(|A_v|=|B_v|+1>|N(A_v)|\), explicitly violating Hall. The solution calls one path extension “augmenting” where only “alternating” is justified; uncovered endpoints are needed for augmentation.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.1, Theorem 4.5 and full proof, pp. 69–70.
- `Lecture Notes/class notes for 28 June.pdf`, physical pp. 23–24, Hall statement and neighborhood definition.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 1–2, repeated statements.
- `Problem Sheets/Exercise Sheet 10/exercise_sheet_10.pdf`, Exercise 1, p. 1; `Problem Sheets/Exercise Sheet 10 - solutions/exercise_sheet_10 - sol.pdf`, Exercise 1(a–c), p. 1, alternating-reachability proof of Hall.
