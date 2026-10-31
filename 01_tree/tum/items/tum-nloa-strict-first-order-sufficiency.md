---
id: tum-nloa-strict-first-order-sufficiency
source: tum-nonlinear-optimization
parent: nloa-existence-geometry
title: Strict tangent-direction positivity as a local sufficiency condition
type: theorem
---

# Strict tangent-direction positivity as a local sufficiency condition

Let \(X\subset\mathbb R^n\) be nonempty, \(f:\mathbb R^n\to\mathbb R\) differentiable and \(\bar x\in X\). If
\[
\nabla f(\bar x)^Td>0\quad\forall d\in T(X,\bar x)\setminus\{0\},
\]
then \(\bar x\) is a strict local minimizer. Neither feasible-set convexity nor objective convexity is required.

If this failed, there would be distinct feasible \(x_k\to\bar x\) with \(f(x_k)\le f(\bar x)\). Put \(t_k=\|x_k-\bar x\|>0\), \(d_k=(x_k-\bar x)/t_k\). Compactness of the unit sphere supplies a subsequence \(d_k\to d\), where \(d\in T(X,\bar x)\) and \(\|d\|=1\). Differentiability gives
\[
0\ge f(x_k)-f(\bar x)=t_k\nabla f(\bar x)^Td_k+o(t_k).
\]
Division by \(t_k\) and passage to the limit contradict strict positivity. The finite-dimensional unit-sphere subsequence is central to this proof.

This is stronger than the nonnegative first-order necessary condition. It is a sufficient test, not a characterization of all strict local minimizers, and it does not imply global optimality in a nonconvex problem.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 2.pdf`, H.2.1, p. 1, and `Exercise materials/Solution Exercise Sheet 2.pdf`, Solution 2.1, p. 1.
