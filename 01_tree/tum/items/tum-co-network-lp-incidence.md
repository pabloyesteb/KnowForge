---
id: tum-co-network-lp-incidence
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Network-matrix linear programs as minimum-cost flows
type: method
caption: "Interprets sparse signed columns as arcs while preserving inequality slacks, variable signs and balances."
---

# Network-matrix linear programs as minimum-cost flows

For \(\max\{c^Tx:Ax\le b\}\) where each column of \(A\) contains at most one +1 and one −1, rows can represent vertices and columns arcs. With +1 as incoming and −1 as outgoing incidence, a two-entry column is an arc from its −1 row to its +1 row. A missing endpoint can be supplied by one auxiliary vertex. Negating the objective gives arc costs \(-c_j\). These are balance coefficients, not vertex throughput capacities.

To make the reduction exact, first specify variable signs. For free \(x_j\), write \(x_j=x_j^+-x_j^-\) with nonnegative variables; the two arc orientations have opposite costs. For nonnegative original variables only the original orientation is needed. Add nonnegative slacks \(s\) so \(Ax+s=b\). Each slack column has one +1 and zero objective cost and is completed with its missing −1 at the auxiliary vertex. Complete all other single-entry columns there too. Then original rows have incoming-minus-outgoing balance \(b_i\), hence course-convention supply \(-b_i\); the auxiliary supply is \(\sum_i b_i\). Use unbounded upper capacities unless original variable bounds are supplied. Feasible flows and feasible LP points correspond by restriction, slack recovery and the variable split. Parallel arc variables can be retained separately, or subdivided with private zero-balance vertices when a simple-digraph representation is required.

An all-zero column is an unconstrained variable, not automatically infeasibility as the submission claims: its objective and sign determine whether it causes unboundedness or can be ignored, subject to feasibility of the other constraints. It can also be modeled separately as a circulation variable. The submitted diagrams motivate the incidence mapping and cost sign, but their vertex-capacity interpretation, omitted slack/conservation equations and unspecified signs do not by themselves prove the claimed reduction. The balance completion above states the necessary conditions explicitly.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Yichen Gao.pdf`, pp. 1–5, complete sparse-column LP task, three column cases, diagrams and objective transformation.
