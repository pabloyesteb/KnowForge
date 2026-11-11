---
id: tum-co-flow-cut-bounds
source: tum-combinatorial-optimization
parent: co-max-flow
title: Feasible network flows and cut-capacity bounds
type: theorem
caption: "Derives net flow identities by cancellation and bounds throughput by every source-sink cut."
---

# Feasible network flows and cut-capacity bounds

A network consists of a digraph, distinct source \(s\) and sink \(t\), and nonnegative rational arc capacities \(u\). A feasible flow satisfies \(0\le f(e)\le u(e)\) and equal incoming/outgoing totals at every other vertex. Its value is net source outflow, not gross outgoing flow. Summing vertex balances cancels internal arcs and proves equality with net sink inflow.

For any \(S\) containing \(s\) but excluding \(t\), write \(\bar S=V\setminus S\). The directed cut contains only arcs from \(S\) to \(\bar S\). The same cancellation gives
\[
\operatorname{val}(f)=f(\delta^{\rm out}(S))-f(\delta^{\rm in}(S))
\le u(\delta^{\rm out}(S)).
\]
The reverse crossing flow is subtracted; it is not part of cut capacity. Equality holds exactly when every outgoing cut arc is saturated and all incoming cut arcs carry zero flow. Such a matching feasible flow and cut certify maximum throughput and minimum cut capacity.

The notes eliminate antiparallel original arcs by subdividing them through auxiliary vertices, assigning the original capacity to each segment. Conservation at the new vertices forces equal segment flows and preserves the original feasible transfers and objective. This is a representational convenience for distinguishing original arcs from later reverse residual arcs. Zero flow is always feasible in this model; lower bounds or prescribed supplies would change that claim. The lecture's final example has source-side set \(\{s,1,2\}\), cut capacity \(1+2+3=6\), and a flow of value 6. The 10 May annotation instead shows an earlier, weaker cut of capacity 7; a valid upper bound need not be tight.

Integral capacities guarantee an integral maximum flow, not prescribed parity on each arc. A supplement gives two unit-capacity source branches that merge before a capacity-three final arc. Every capacity is odd, but the maximum value is two and the final arc necessarily carries two. Thus there need not be a maximum flow odd on every arc.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Chapter 3 and §3.1, pp. 22–24, Definition 3.1, Lemma 3.2, antiparallel transformation, Definition 3.4 and Theorem 3.5; final flow/cut Figure 18, p. 30.
- `Lecture Notes/class notes for 10 May.pdf`, physical pp. 9–12, network model, balances, matching diagram and annotated capacity-seven cut.
- `Lecture Notes/class notes for 17 May.pdf`, physical pp. 2–9, network and cut definitions, matching model and complete cancellation proof.
- `Student Submitted Exercises/Moritz Kund.pdf`, p. 1, handwritten odd-capacity question and merging-branch counterexample.
