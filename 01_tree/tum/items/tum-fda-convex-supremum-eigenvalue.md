---
id: tum-fda-convex-supremum-eigenvalue
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Pointwise suprema and convexity of the largest eigenvalue
type: theorem
caption: "Preserves convexity under arbitrary pointwise suprema and applies the Rayleigh representation to symmetric matrices."
---

# Pointwise suprema and convexity of the largest eigenvalue

If every \(f_y\) is convex on the same convex domain, then \(g(x)=\sup_y f_y(x)\) is convex, allowing extended-real values. For interior weights,
\[
g(\lambda x+(1-\lambda)z)
\le\sup_y[\lambda f_y(x)+(1-\lambda)f_y(z)]
\le\lambda g(x)+(1-\lambda)g(z).
\]
Endpoint weights are immediate. No attainment of the supremum or convexity of its index set is needed for this pointwise argument; the booklet gives convex sets as sufficient setting, but does not use that additional index-set assumption in its proof.

For real symmetric matrices,
\[
\lambda_{\max}(A)=\sup_{\|u\|_2=1}u^TAu.
\]
Each fixed-unit-vector quadratic form is linear in the matrix entries. Thus the largest eigenvalue is a convex function on the vector space of symmetric matrices:
\[
\lambda_{\max}(\lambda A+(1-\lambda)B)
\le\lambda\lambda_{\max}(A)+(1-\lambda)\lambda_{\max}(B).
\]
This concerns eigenvalues of symmetric matrices, where the real variational characterization applies; it does not define a comparable ordered-real maximum eigenvalue for arbitrary nonsymmetric matrices.

An alternative proof uses \(\operatorname{epi}g=\bigcap_y\operatorname{epi}f_y\). Each epigraph is convex and intersections preserve convexity. This also works for the unit-sphere index set in the Rayleigh representation, even though that sphere itself is not convex.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.2(a–b), p. 62; supremum and Rayleigh-quotient solution, p. 68.
- `24. Juni - 30. Juni/Exercise sheet 10.pdf`, Exercise 10.2(a–b), p. 1.
- `1. Juli - 7. Juli/Solution sheet 10.pdf`, single physical page, Exercise 10.2(a–b), full argument and illustrations.
