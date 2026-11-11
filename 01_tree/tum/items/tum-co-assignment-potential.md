---
id: tum-co-assignment-potential
source: tum-combinatorial-optimization
parent: co-bipartite
title: Feasible potentials and tight-edge assignment certificates
type: theorem
caption: "Bounds every perfect assignment by a vertex-potential sum and certifies optimality through equality."
---

# Feasible potentials and tight-edge assignment certificates

For maximum-weight perfect assignment on a complete bipartite graph with equally sized parts, a feasible potential satisfies \(p(a)+p(b)\ge w(a,b)\). Tight edges attain equality and form the equality graph \(G_p\). Every perfect matching \(M'\) obeys
\[
w(M')\le\sum_{\{a,b\}\in M'}(p(a)+p(b))=\sum_{v\in V}p(v).
\]
Every vertex appears exactly once. A perfect matching entirely in \(G_p\) attains this bound and therefore is optimal, with \(p\) providing a directly checkable certificate. This statement concerns perfect assignment; arbitrary signed potentials do not bound optional matchings in the same way.

Initialize \(p(b)=0\) and \(p(a)=\max_b w(a,b)\). Feasibility follows row by row, including negative weights. To change the equality graph, take nonempty \(S\subseteq A\) with \(T=N_p(S)\ne B\), and let
\[
\gamma=\min_{a\in S,b\notin T}\{p(a)+p(b)-w(a,b)\}>0.
\]
Subtract \(\gamma\) on \(S\), add it on \(T\), and leave other potentials unchanged. Edges inside \(S\times T\) and outside both sets retain their slack; slack from \(S\) to \(B\setminus T\) decreases by at most its minimum, and slack from \(A\setminus S\) to \(T\) increases. Thus feasibility survives and at least one new tight edge leaves \(S\). Former tight edges in the latter crossing class can cease to be tight: the equality graph is not globally monotone, contrary to the introductory prose. The preserved search and matching edges, rather than inclusion of the whole previous equality graph, are the useful invariants.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.4, pp. 77–79, Definition 4.13, Theorem 4.14 with full potential-sum proof, Lemmas 4.15–4.16 with four-case update proof.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 19–27, complete certificate proof, initialization and update statement.
- `Lecture Notes/class notes for 12 July.pdf`, physical pp. 1–4, recap and complete update proof.
