---
id: tum-fa-weak-semicontinuity
source: tum-functional-analysis
parent: fa-weak-compactness
title: Weak lower semicontinuity and convex closedness
type: theorem
---

# Weak lower semicontinuity and convex closedness

## Norms and support functionals

If \(x_n\rightharpoonup x\) in a normed space, then
\[
\|x\|\le\liminf_n\|x_n\|.
\]
Choose a norming functional for \(x\); its values converge and are bounded by \(\|x_n\|\). Similarly weak-star convergence \(f_n\to f\) gives
\(\|f\|\le\liminf_n\|f_n\|\) by testing each unit vector and taking the supremum. Equality need not hold: orthonormal vectors converge weakly to zero with norm 1.

For a nonempty family \(\mathcal F\subset X^*\) on a real normed space with \(\|f\|\le1\), the support functional
\(\phi(x)=\sup_{f\in\mathcal F}f(x)\) is finite, convex and 1-Lipschitz:
\[
|\phi(x)-\phi(y)|\le\|x-y\|.
\]
It is weakly sequentially lower semicontinuous. Indeed a subsequence with \(\phi(x_{n_k})\le\alpha<\phi(x)\) is contradicted by one \(f\in\mathcal F\) with \(f(x)>\alpha\). Taking the dual unit ball gives \(\phi(x)=\|x\|\).

## Closed convex feasible sets

A norm-closed convex \(K\subset X\) is weakly sequentially closed. If \(x_n\in K\) and \(x_n\rightharpoonup x\notin K\), strict point–set separation gives a functional with
\(f(x)>\sup_Kf\ge f(x_n)\), contradicting convergence. Over \(\mathbb C\), use real parts. Convexity is material; arbitrary norm-closed sets need not contain weak limits.

These two properties keep feasibility and prevent an objective jump upward when taking weak limits of minimizing sequences.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Lemma 6.3, p. 52, and Proposition 6.6, p. 53.
- E9/S9, A9.2.
