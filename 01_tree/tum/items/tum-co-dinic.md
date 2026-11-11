---
id: tum-co-dinic
source: tum-combinatorial-optimization
parent: co-max-flow
title: Dinic phases with minimum-throughput blocking flows
type: algorithm
caption: "Combines shortest-path layers and push/pull throughput routing to obtain blocking phases and an O(n³) flow algorithm."
---

# Dinic phases with minimum-throughput blocking flows

Starting from zero flow, construct the residual graph and compute edge-count distances from the source. If the sink is unreachable, the flow is maximum. Otherwise let its distance be \(k\), retain the source, sink and intermediate distance layers, and retain only residual arcs from layer \(i\) to layer \(i+1\). Every shortest augmenting path lies in this acyclic layered graph.

A blocking flow saturates at least one arc on each source-sink path in the layered graph: no path of remaining forward capacity survives. It need not be a maximum flow in that graph when reverse rerouting is allowed. This distinction supports completing a phase without solving another full maximum-flow problem.

The course constructs blocking flows by minimum throughput. For an internal vertex set
\[
p(v)=\min\left\{\sum_{e\in\delta^{\rm in}(v)}r(e),\sum_{e\in\delta^{\rm out}(v)}r(e)\right\},
\]
using current layered capacities. At the source use total outgoing capacity and at the sink total incoming capacity. Remove vertices of throughput zero and their incident arcs. Select a remaining vertex of minimum throughput \(\lambda\), push \(\lambda\) units toward the sink and pull the same amount from the source. Combining the two routings is a feasible source-sink augmentation through that vertex.

PushFlow propagates excess through successive layers with a FIFO queue. Send the smaller of the current excess and the remaining capacity on a chosen outgoing arc, updating both quantities, until the excess has moved onward. PullFlow is the reverse-layer analogue. Minimum throughput ensures enough outgoing/incoming capacity to route the selected amount. Residual capacities must reflect amounts already assigned, and terminal excess must be accumulated without processing the terminal as an ordinary internal vertex. The printed pseudocode omits some capacity bookkeeping; repeatedly using an unchanged arc capacity would violate the intended routing. After routing, delete saturated arcs and zero-throughput vertices and repeat until no layered path remains.

After a blocking phase, residual source-sink distance strictly increases. Old residual arcs cannot move forward by more than one old distance layer; newly introduced reverse arcs move backward. A path as short as the old distance would therefore have to use only old forward layer arcs, but all such paths are blocked. There are at most \(n-1\) finite distances, hence \(O(n)\) phases. Termination gives maximum flow, and integer capacities preserve integrality.

Each minimum-throughput routing eliminates at least its selected vertex, giving at most \(n\) such routings per phase. Charge saturated-arc processing to deleted arcs, at most \(m\) per phase; unsaturated capacity updates contribute at most \(O(n)\) per routing with the described layer processing. The resulting phase bound is \(O(m+n^2)\), and for the course's simple-graph setting the total is \(O(n^3)\). This bound concerns the minimum-throughput push/pull construction, rather than every possible implementation of the blocking-flow framework.

The illustrated six-vertex network uses a first phase of three-edge paths, followed by a four-edge residual path. The annotated routing removes vertices 3, 1 and 2 in the first phase and finishes the second phase at flow value 6, matching the cut certificate.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.4, pp. 34–38, Definition 3.12, PushFlow, Algorithm 6, Lemma 3.13 and Theorem 3.14 with proofs, Figure 21.
- `Lecture Notes/class notes for 24 May.pdf`, physical pp. 1–20, complete handwritten definition, algorithm, PushFlow/PullFlow, two-phase annotated example and correctness/runtime proof.
