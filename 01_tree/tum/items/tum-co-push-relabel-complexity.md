---
id: tum-co-push-relabel-complexity
source: tum-combinatorial-optimization
parent: co-max-flow
title: Height bounds and amortized push-relabel operation counts
type: theorem
caption: "Bounds relabels and saturating pushes and explains the highest-label phase/potential analysis with its implementation limits."
---

# Height bounds and amortized push-relabel operation counts

Labels never decrease, and every vertex that is relabeled is active both before and after the change. Its residual path back to the source implies \(h(v)\le h(s)+n-1=2n-1\). Hence there are at most \(2n-1\) relabels per vertex and \(O(n^2)\) in total.

A saturating push exhausts a residual arc. Before the same orientation can saturate again, some reverse push must restore capacity. Admissibility and monotone heights require the relevant endpoint heights to rise by at least two between opposite pushes and their next reversal. With heights bounded by \(2n-1\), each residual orientation saturates \(O(n)\) times, giving \(O(mn)\) saturating pushes.

For highest-label selection, let \(h^*\) be the greatest active height and call a period between its changes a phase. Its total upward movement is bounded by total label increases, \(O(n^2)\), and its total downward movement is no greater up to endpoints. Thus there are \(O(n^2)\) phases. Cheap phases with at most \(\sqrt m\) nonsaturating pushes contribute \(O(n^2\sqrt m)\).

The source analyzes expensive phases using
\[
\Phi=\sum_{v\text{ active}}|\{w:h(w)\le h(v)\}|.
\]
A nonsaturating push deactivates its sender and can activate only a lower-height receiver. More than \(\sqrt m\) such pushes at an unchanged highest level require more than \(\sqrt m\) vertices at that level; each such transfer decreases the potential by at least that level's cardinality, even when a receiver becomes active. Relabels and saturating pushes supply the increases charged against this decrease. The notes state a bound of \(8n^2\sqrt m\) nonsaturating pushes from this argument. This sharper count depends on highest-label selection, not arbitrary choices of active vertices.

Operation counts and implementation costs must be distinguished. Height buckets can track active vertices, and adjacency scans find a new minimum neighbor height on relabel. Up to \(O(n)\) scans per vertex give \(O(nm)\) aggregate neighbor examination; maintaining admissible-arc data also requires specified updates. The final source proof is internally inconsistent: it calls \(O(n)\) relabels a total bound even though that bound is per vertex, states \(O(n^2\sqrt m)\) in the theorem, and ends with \(O(n^2m)\). Its instruction to increment the highest bucket by one also omits relabel jumps. Retain the proved height/saturation bounds and the stated sharper highest-label analysis separately; the printed implementation paragraph alone does not establish the advertised sharper runtime. It asserts faster variants without supplying their implementations.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.5, pp. 43–45, Lemmas 3.20–3.22, complete phase/potential argument and Theorem 3.23 with implementation discussion.
- `Lecture Notes/class notes for 31 May.pdf`, physical pp. 39–45, total relabel bound, saturation proof, stated nonsaturation lemma and runtime sketch; nonsaturation proof deferred to typed notes.
