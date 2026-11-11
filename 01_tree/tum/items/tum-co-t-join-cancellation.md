---
id: tum-co-t-join-cancellation
source: tum-combinatorial-optimization
parent: co-general-matching
title: Dummy-edge initialization and T-join cycle cancellation
type: algorithm
caption: "Initializes arbitrary parity demands in a complete extension and uses negative cycles to improve cost."
---

# Dummy-edge initialization and T-join cycle cancellation

For integer-cost minimum \(T\)-join with even \(|T|\), put \(S_c=\sum_{e\in E}|c(e)|\) and \(M=S_c+1\). Add every missing edge at cost \(2M\), pair the vertices of \(T\) arbitrarily, and take those pair edges as the initial join. The empty set initializes \(T=\varnothing\). Repeatedly negate costs of selected edges, find a negative undirected cycle under those change costs, and toggle its edges. Parity remains feasible and cost strictly improves. Stop when no negative cycle exists; the cycle criterion proves optimality in the completed graph.

If the result uses a dummy edge, its cost is at least \(2M-S_c>M\), whereas every original-only join costs at most \(S_c<M\). Hence no original feasible join exists. Otherwise the result is an original optimum. The original costs cannot equal \(2M\), so the source's cost-based dummy test is unambiguous.

The initial cost is at most \(|T|M\le nM\), the final cost is at least \(-S_c\), and every integral update improves by at least one. This gives \(O(n(1+S_c))\) updates, with polynomial cycle-search work per update if such a subroutine is supplied. The additive one also covers all-zero original costs. The text's intermediate arithmetic for its initial bound is inconsistent; the direct pairing bound yields the stated pseudopolynomial behavior. It does not establish polynomial time in the binary input length.

Replacing each undirected edge with two opposite directed arcs is invalid for this cycle search: a negative edge would create a negative directed two-arc cycle that traverses the same undirected edge twice. An undirected simple cycle cannot use that edge twice. Bellman–Ford on that replacement therefore supplies false witnesses; the later cycle-cone construction addresses a different oracle.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.5.1, pp. 86–88, Algorithm 13, dummy-edge proof and numerical iteration bound; Figure 39, p. 90; Theorem 4.32, p. 95.
- `Lecture Notes/class notes for 19 July.pdf`, physical pp. 15–18, full algorithm and false directed-cycle example.
