---
id: tum-co-matching-t-join
source: tum-combinatorial-optimization
parent: co-general-matching
title: Perfect matching through minimum-cost T-joins
type: method
caption: "Uses odd-degree parity and a dominant cardinality penalty to encode perfect weighted pairing."
---

# Perfect matching through minimum-cost T-joins

For an undirected graph, a \(T\)-join is an edge subset whose odd-degree vertices are exactly \(T\). The handshake identity requires even \(|T|\), and disconnected components impose parity separately. A perfect matching is precisely a \(V\)-join with \(|V|/2\) edges: every vertex has positive odd degree, and equality in the degree-sum lower bound forces all degrees to be one. Merely being a \(V\)-join does not force a matching.

Set all costs to one and solve minimum \(V\)-join. Infeasibility or an optimum with more than \(|V|/2\) edges rules out a perfect matching; equality produces one. Having established existence, encode maximum perfect-matching weight by \(K=1+2\sum_e|w(e)|\) and positive costs \(c(e)=K-w(e)\). Any nonperfect \(V\)-join has at least one extra edge and pays a penalty exceeding any possible original-weight benefit. An optimum must therefore be perfect, and its cost is \(K|V|/2-w(M)\), so cost minimization maximizes weight.

Rational weights can be multiplied by a common denominator to obtain integers without changing optima; arithmetic complexity must still distinguish numerical magnitude from binary encoding size. These are reductions conditional on a T-join solver, not by themselves a polynomial implementation of general matching.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.5, pp. 82–84, Definition 4.19, Problem 4.20 and full Lemma 4.21 proof; Figure 37, p. 89.
- `Lecture Notes/class notes for 12 July.pdf`, physical pp. 20–26, T-join examples and unit-cost reduction.
- `Lecture Notes/class notes for 19 July.pdf`, physical pp. 1–6, full dominant-penalty reduction and weight identity.
