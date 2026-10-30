---
id: tum-fa-banach-spaces
source: tum-functional-analysis
parent: fa-normed-spaces
title: Normed spaces, completeness and function-space examples
type: concept
---

# Normed spaces, completeness and function-space examples

## Framework

Over \(\mathbb K=\mathbb R\) or \(\mathbb C\), a norm is positive definite, absolutely homogeneous and subadditive. It defines \(d(x,y)=\|x-y\|\), open/closed balls and sequential convergence. A Banach space is a normed space in which every Cauchy sequence converges in the space. The closure, interior and boundary are taken in this norm topology.

A complete linear subspace is closed in its ambient normed space; a closed subspace of a Banach space is complete. For the latter, take the ambient limit of a Cauchy sequence and use closedness. Finite-dimensional subspaces are closed: equivalence of finite-dimensional norms makes them complete. Every proper linear subspace has empty interior, since scaling a vector outside it gives arbitrarily small perturbations outside it.

## Principal examples and proof mechanisms

- \(\mathbb K^n\) with any norm is complete. On a finite product \(X_1\times\cdots\times X_m\), the component \(p\)-norms and maximum norm are equivalent; convergence is componentwise and completeness holds exactly when every factor is complete. Addition and scalar multiplication are continuous.
- Bounded functions \(B(D;\mathbb K)\) are complete in the supremum norm. For compact metric \(D\), continuous functions \(C(D;\mathbb K)\) form a closed subspace: a uniform limit of continuous functions is continuous.
- \(L^p(D;\mathbb K)\), \(1\le p<\infty\), uses \((\int_D|f|^p)^{1/p}\) and identifies functions equal almost everywhere. Without that identification the expression is not positive definite on individual functions.
- \(\ell^\infty\) consists of bounded sequences; \(c\) and \(c_0\) are its closed subspaces of convergent and null sequences. A uniform approximation argument transfers the scalar Cauchy or null property to the limit.
- \(\ell^p\), \(1\le p<\infty\), uses \((\sum_k|x_k|^p)^{1/p}\). Minkowski on finite sums proves the triangle inequality. For completeness, a norm-Cauchy sequence has coordinatewise limits; bounds on every finite partial sum pass to these limits, then to the infinite sum, establishing membership and norm convergence.

## What completeness does not imply

In \(C([0,1])\) with the sup norm, \(V=\{f:f(0)=f(1)=0\}\) is closed with empty interior. It need not give convergent subsequences: triangular functions of height \(n\) in \(V\) are unbounded.

The same vector space \(C([0,1])\), equipped instead with \(\|\cdot\|_2\), is an **incomplete pre-Hilbert space**. Let \(f_n\) be zero up to \(1/2\), increase linearly to one on \([1/2,1/2+1/n]\), then remain one. For \(m\ge n\),
\[
\|f_n-f_m\|_2^2\le 1/n.
\]
An \(L^2\) limit would equal the step function almost everywhere; no continuous function can be zero on the left half and one on the right half. Completeness therefore depends on both the space and its norm; taking an inner product alone does not make a Hilbert space.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, pp. 2–6, Proposition 1.3; pp. 7–8, Proposition 1.7/Corollary 1.8.
- `Problem sheets/Problem Sheet 1.pdf` and corresponding `Solutions to problem sheets/Solutions Sheet 1.pdf`, T1.1, T1.3.
- `Problem sheets/Problem Sheet 2.pdf` and `Solutions to problem sheets/Solutions Sheet 2.pdf`, A2.1.
- `Problem sheets/Problem Sheet 3.pdf` and `Solutions to problem sheets/Solutions Sheet 3.pdf`, T3.4.
