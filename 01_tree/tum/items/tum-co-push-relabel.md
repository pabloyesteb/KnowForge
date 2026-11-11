---
id: tum-co-push-relabel
source: tum-combinatorial-optimization
parent: co-max-flow
title: Highest-label push-relabel with preflows and admissible arcs
type: algorithm
caption: "Maintains capacity feasibility and valid height labels while eliminating excess to obtain a maximum flow."
---

# Highest-label push-relabel with preflows and admissible arcs

A preflow satisfies arc capacities and nonnegative excess \(\operatorname{ex}(v)=f(\delta^{\rm in}(v))-f(\delta^{\rm out}(v))\) at every vertex other than the source. An internal vertex with positive excess is active. Unlike augmenting-path methods, push-relabel temporarily permits accumulated surplus instead of enforcing conservation at every internal vertex.

Initialize by saturating source-outgoing arcs and setting other flows to zero. Set heights \(h(s)=n\) and \(h(v)=0\) elsewhere. A valid distance labeling satisfies \(h(t)=0\) and \(h(v)\le h(w)+1\) for every residual arc \((v,w)\). An arc is admissible when equality holds. Repeatedly select an active vertex of greatest height. If it has an admissible outgoing residual arc, push \(\gamma=\min\{\operatorname{ex}(v),r(v,w)\}\) along it, updating original flow or cancelling it according to orientation. Otherwise relabel it to \(1+\min_{(v,w)\text{ residual}}h(w)\).

A push preserves capacities and nonnegative excess: it removes at most the sender's surplus. Any new reverse residual arc respects the labeling because a push descends exactly one height unit. A relabel strictly increases its vertex height and retains all residual inequalities; incoming inequalities only become weaker. The source and sink are never selected as active vertices.

An active vertex always has a residual path back to the source. Otherwise its residual reachable set would exclude the source, have no positive original inflow across its boundary, and hence nonpositive total excess, contradicting its positive member and nonnegative excess everywhere in that set. Thus relabel has an outgoing candidate. Along any simple residual path, height drops by at most one per arc. Since \(h(s)=n\), \(h(t)=0\), and a simple path has at most \(n-1\) arcs, no residual source-sink path exists throughout the algorithm. Once no active vertex remains, conservation is restored, and the residual optimality certificate proves maximum flow. Integral capacities preserve integral pushes and the final integral flow.

Surplus that cannot reach the sink can return to the source after heights rise above \(n\). The worked example explicitly raises vertex 1 to height 7 while the source has height 6, returns one surplus unit, and then sends the remaining unit through vertex 3 to finish at value 6. The diagrams illustrate valid local operations; they do not consistently select the greatest-height active vertex at every intermediate step, so their entire order should not be used as a trace of the highest-label selection rule.

The Sheet 5 Python completion implements paired residual updates and excess transfers in `push`, and a full residual-row minimum-height scan in `relabel`. Its main loop linearly searches active vertices for the highest label and scans a matrix row for an admissible arc. These choices do not implement the theoretical bucket/admissible-list runtime. The driver gives each flow algorithm a separate row-wise matrix copy; random networks and timing comparisons are proposed without fixed measured results.

The source excess array is bookkeeping rather than the mathematical source imbalance: it initially assigns the source its total outgoing capacity before subtracting the saturations, so it is offset from the usual negative source excess. Internal and sink excess are updated by the ordinary conservation transfers. More seriously, initialization appends every recipient of a positive source saturation to the active list without excluding the sink. A direct positive source-to-sink arc can therefore make the algorithm process the sink as active, contrary to the definition; the later activation checks do exclude both terminals. The manual driver matrix has no such direct arc, but the optional random generator can produce one. No universal correctness claim for all generated inputs follows from the supplied implementation.

Sheet 5's hand-execution answer gives value 4, with approximately ten pushes and eight relabels depending on choices. These counts describe its example and are not an invariant operation count.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.5, pp. 39–42, Definitions 3.15–3.16, Push/Relabel, Algorithm 7 and Lemmas 3.17–3.19; complete worked Figures 22–23, pp. 46–47.
- `Lecture Notes/class notes for 31 May.pdf`, all 45 physical pages, preflow/height definitions, full annotated execution, invariants and optimality proofs.
- `Problem Sheets/Exercise Sheet 5/exercise_sheet_5.pdf`, Exercises 2–3, pp. 1–2; `Problem Sheets/Exercise Sheet 5 - solutions/exercise_sheet_5 - sol.pdf`, corresponding answers, pp. 1–2.
- `Problem Sheets/Exercise Sheet 5/graph_module.py`, full scaffold, initialization and activation rules; `Problem Sheets/Exercise Sheet 5/main.py`, full comparison driver.
- `Problem Sheets/Exercise Sheet 5 - solutions/code - sol.py` and `Problem Sheets/Exercise Sheet 5 - solutions/graph_module - complete.py`, completed push/relabel routines and full implementation.
