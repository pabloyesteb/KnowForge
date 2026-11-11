---
id: tum-co-t-join-cycle-optimality
source: tum-combinatorial-optimization
parent: co-general-matching
title: Cycle toggling and T-join optimality
type: theorem
caption: "Characterizes all parity-preserving differences and cost improvements by edge-disjoint cycles."
---

# Cycle toggling and T-join optimality

If \(F\) is a \(T\)-join, then \(F'\) is another \(T\)-join exactly when \(F\triangle F'\) is a union of edge-disjoint cycles. Indeed,
\[
\deg_{F\triangle F'}(v)=\deg_F(v)+\deg_{F'}(v)-2\deg_{F\cap F'}(v)
\]
is even when both edge sets have the same odd-degree vertices. Each nonempty connected component of this even-degree subgraph decomposes into cycles. The difference need not be connected even if the original graph is connected. Conversely toggling a cycle changes incident degrees by an even number and preserves parity; iterate over the disjoint cycles.

Define signed change costs \(\tilde c(e)=-c(e)\) for \(e\in F\), otherwise \(\tilde c(e)=c(e)\). For any cycle \(C\), toggling gives \(c(F\triangle C)=c(F)+\tilde c(C)\). Thus \(F\) is minimum cost exactly when no undirected cycle has negative change cost. If a better \(F'\) exists, decompose the difference and sum its change costs; at least one cycle is negative. Unlike directed residual flow, membership is toggled rather than capacity-adjusted, and cycles may share vertices but not edges in the decomposition.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.5.1, pp. 85–86, Lemmas 4.22–4.23 with full proofs; Figure 38, p. 90.
- `Lecture Notes/class notes for 19 July.pdf`, physical pp. 7–15, full diagram sequence, parity proof and negative-cycle criterion (the nonmember case in its cost display means e outside F).
