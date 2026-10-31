---
id: tum-fa-complemented-subspaces
source: tum-functional-analysis
parent: fa-compact-fredholm
title: Complemented Banach subspaces and bounded projections
type: theorem
---

# Complemented Banach subspaces and bounded projections

## Algebraic versus topological decomposition

An algebraic complement \(V\) of \(U\subset X\) satisfies \(U\cap V=0\) and \(U+V=X\). Such complements exist by extending a vector-space basis. In a Banach space a complemented decomposition \(X=U\oplus V\) additionally requires both subspaces closed. Algebraic complement existence alone does not provide continuous coordinate projections.

For closed \(U\), a closed complement exists iff a bounded projection \(P:X\to X\) satisfies \(P^2=P\), \(P(X)=U\). Given such \(P\), \(V=\ker P\) is closed and \(x=Px+(I-P)x\). Conversely, for closed \(U,V\), the addition map from Banach \(U\times V\) to \(X\) is a bounded bijection; bounded inverse makes the coordinate projection continuous.

## Finite dimension and codimension

For finite-dimensional \(U=\operatorname{span}\{u_i\}_{i=1}^n\), extend its coordinate functionals to \(f_i\in X^*\) by Hahn–Banach. Then
\[
Px=\sum_{i=1}^nf_i(x)u_i
\]
is a bounded projection onto \(U\). If \(U\) is closed and \(\dim(X/U)<\infty\), any algebraic complement is finite-dimensional, hence closed. Codimension equals the dimension of any complement.

Every closed Hilbert subspace has its orthogonal complement. General Banach spaces need not: the notes state that \(C([0,1])\) is not complemented in \(L^\infty(0,1)\). They also state, without proofs, the Lindenstrauss–Tzafriri characterization of spaces whose every closed subspace is complemented as spaces isomorphic to Hilbert space, and the contrasting Gowers–Maurey example.

## Explicit decompositions

- In \(C([0,1])\), functions vanishing at 0 have complement the constants and codimension 1.
- Functions vanishing at both endpoints have complement \(\operatorname{span}\{1,x\}\) and codimension 2.
- In \(C([-1,1])\), even and odd continuous functions are complementary via \(f(x)=[f(x)+f(-x)]/2+[f(x)-f(-x)]/2\). Both dimensions are infinite.
- In convergent sequences \(c\), the null sequences \(c_0\) have complement the constant sequences; \(x=(x-\lim x)+(\lim x)\mathbf1\), so the codimension is 1.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Definition 10.5, Propositions 10.6/10.8, Definition 10.7 and concluding remarks, pp. 74–76.
- `Problem sheets/Problem Sheet 11.pdf` and `Solutions to problem sheets/Solutions sheet 11.pdf` (WS 2024/25), T11.2, T11.4.
