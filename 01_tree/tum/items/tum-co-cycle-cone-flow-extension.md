---
id: tum-co-cycle-cone-flow-extension
source: tum-combinatorial-optimization
parent: co-general-matching
title: Flow extension of cycle-cone cut constraints
type: method
caption: "Uses a separate capacitated endpoint flow for every edge to replace exponentially many cut inequalities."
---

# Flow extension of cycle-cone cut constraints

For each undirected edge \(e=\{s,t\}\), replace graph edges by both directed orientations with capacities \(x_{\{u,v\}}\), and introduce a separate flow commodity \(y^e\). The cycle-cone inequalities require every cut separating \(s,t\) to have capacity at least \(2x_e\). By max-flow/min-cut this is equivalent to an endpoint flow of value at least \(2x_e\), with conservation at every other vertex and individual bounds \(0\le y^e_{uv}\le x_{\{u,v\}}\). Capacities are imposed independently per commodity; these are witnesses for separate max-flow problems, not simultaneously shared traffic. There are \(O(m^2)\) flow variables and \(O(m^2+mn)\) constraints, giving a polynomial-size projection formulation. Add normalization and the cycle-cost objective to formulate minimum mean cycle.

The displayed source system bounds only gross flow leaving \(s\), rather than net flow value. Unless incoming flow at \(s\) is forbidden, that admits circulation that does not reach \(t\) and invalidates the claimed equivalence. The corrected requirement is
\[
\sum_v y^e_{sv}-\sum_u y^e_{us}\ge2x_e,
\]
with conservation at other vertices (or an equivalent source/sink restriction). For example, on the two-edge path with the center chosen as source for each commodity, unit flows in both directions on both edges have gross source outflow two despite the graph containing no cycle. The literal printed constraints accept this vector; the net-value constraint rejects it. The cut/max-flow argument justifies the corrected formulation, not the gross-outflow display.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.5.2, Lemma 4.27 and complete cut/max-flow proof sketch, pp. 92–93; extended LP, p. 94.
- `Lecture Notes/class notes for 19 July.pdf`, physical pp. 22–23, extension statement and gross-outflow display.
