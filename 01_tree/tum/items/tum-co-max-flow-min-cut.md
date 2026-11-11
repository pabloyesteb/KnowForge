---
id: tum-co-max-flow-min-cut
source: tum-combinatorial-optimization
parent: co-max-flow
title: Residual reachability and the max-flow/min-cut certificate
type: theorem
caption: "Proves that absence of an augmenting path yields a saturated outgoing cut with zero incoming flow."
---

# Residual reachability and the max-flow/min-cut certificate

A feasible flow is maximum exactly when its residual network has no source-sink path. If such a path exists, augmentation by its positive bottleneck increases the value, contradicting optimality.

Conversely, suppose no path exists and let \(S\) be all vertices reachable from \(s\) by positive-capacity residual arcs. Then \(s\in S\) and \(t\notin S\). Every original arc leaving \(S\) is saturated, otherwise its forward residual arc would reach another vertex. Every original arc entering \(S\) carries zero flow, otherwise its reverse residual arc would leave \(S\). Therefore
\[
\operatorname{val}(f)=f(\delta^{\rm out}(S))-f(\delta^{\rm in}(S))
=u(\delta^{\rm out}(S)).
\]
The cut upper bound proves both maximum flow and minimum cut optimality. This also gives the max-flow/min-cut equality: the maximum feasible flow value equals minimum source-sink cut capacity. For rational capacities, terminating Ford-Fulkerson constructs both witnesses; the reachability argument certifies any feasible flow without requiring knowledge of how it was obtained.

The proof must distinguish outgoing saturation from incoming zero flow. The printed proof changes set letters and loses complement marks in some expressions; using the explicit incoming/outgoing boundaries above retains the cancellation and reachability argument unambiguously.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Theorem 3.8 and proof, pp. 26–27; Theorem 3.9, p. 27; residual reachable set in Figure 18, p. 30.
- `Lecture Notes/class notes for 17 May.pdf`, physical pp. 15–21, residual reachability proof and capacity-six certificate.
