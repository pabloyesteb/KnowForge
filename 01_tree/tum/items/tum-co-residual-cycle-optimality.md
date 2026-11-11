---
id: tum-co-residual-cycle-optimality
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Residual circulations and negative-cycle optimality for cost flows
type: theorem
caption: "Represents feasible-flow differences by residual circulations and decomposes them to certify minimum cost."
---

# Residual circulations and negative-cycle optimality for cost flows

In a cost-flow residual graph, a forward arc has capacity \(u(e)-f(e)\) and cost \(c(e)\); a reverse arc has capacity \(f(e)\) and cost \(-c(e)\). Cancelling one unit refunds its original cost. Keep residual arcs associated with their original edges when parallel/antiparallel edges are present; opposite original costs cannot generally be merged into one residual-cost entry.

For feasible \(f,f'\) with the same balances, assign \(\max(f'(e)-f(e),0)\) to the forward residual arc and \(\max(f(e)-f'(e),0)\) to its reverse. The result \(g\) respects residual capacities, has zero balance everywhere, and has cost \(c_f(g)=c(f')-c(f)\). The capacity inequalities follow directly from \(f'\le u\) and \(f'\ge0\); subtracting the two balance equations proves conservation. This circulation belongs to the residual graph of \(f\), not necessarily that of \(f'\).

Every nonnegative circulation decomposes into at most \(m\) positive multiples of directed simple cycles. Find a cycle in its positive support, subtract its minimum flow, and repeat. Conservation persists and at least one positive-support edge disappears each time. Consequently a negative-cost circulation contains a negative-cost cycle.

Augmenting around a residual cycle by its bottleneck preserves all balances and changes cost by bottleneck times cycle cost. Thus a feasible \(b\)-flow is minimum-cost exactly when no negative-cost residual cycle exists. Necessity is an improving augmentation; sufficiency follows because any cheaper feasible \(f'\) would produce a negative residual circulation and hence an improving cycle. A residual cycle of zero or positive cost does not disprove optimality.

Sheet 6 illustrates two feasible flows with costs 42 and 34. Their residual difference is one unit around the four-arc cancellation cycle, costing −8: reverse the return arc, the forced cost-two arc and two other used arcs. This realizes the identity \(34=42-8\). The 7 June smaller diagram gives another improving residual cycle of cost −2; both preserve the original supplies.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.7, pp. 51–55 through the end of Theorem 3.33's proof, Definitions 3.28–3.29, Lemmas 3.30–3.31 and cycle augmentation.
- `Lecture Notes/class notes for 07 June.pdf`, physical pp. 11–19, full residual definition/example and difference-circulation capacity/conservation proof.
- `Problem Sheets/Exercise Sheet 6/exercise_sheet_6.pdf`, Exercise 1, p. 1; `Problem Sheets/Exercise Sheet 6 - solutions/exercise_sheet_6 - sol.pdf`, Exercise 1 and all three flow diagrams, p. 1.
- `Lecture Notes/class notes for 14 June.pdf`, physical pp. 1–5, circulation decomposition, cycle augmentation and full optimality proof.
