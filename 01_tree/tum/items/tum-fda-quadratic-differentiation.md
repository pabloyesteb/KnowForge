---
id: tum-fda-quadratic-differentiation
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Differentiating general quadratic forms and squared matrix norms
type: method
caption: "Tracks matrix symmetry and dimensions when deriving gradients and constant Hessians of quadratic objectives."
---

# Differentiating general quadratic forms and squared matrix norms

For \(A\in\mathbb R^{n\times n}\), \(b\in\mathbb R^n\),
\[
f(x)=x^TAx+b^Tx+c,\quad
\nabla f(x)=(A+A^T)x+b,\quad\nabla^2 f=A+A^T.
\]
Differentiate \(\sum_{i,j}x_iA_{ij}x_j\): the terms in which the variable occurs as the first factor give \(Ax\), and those in the second give \(A^Tx\). Only for symmetric \(A\) does this simplify to \(2Ax+b\). With the conventional factor \(1/2\), a symmetric quadratic has gradient \(Ax+b\) and Hessian \(A\). The antisymmetric part contributes zero to the scalar quadratic.

A rectangular matrix cannot be inserted into \(x^TAx\) without matching dimensions. For \(A\in\mathbb R^{m\times n}\), however,
\[
\|Ax\|_2^2=x^TA^TAx,\qquad
\nabla\|Ax\|_2^2=2A^TAx,\quad\nabla^2\|Ax\|_2^2=2A^TA.
\]
The symmetric positive-semidefinite matrix \(A^TA\) makes these formulas applicable to least-squares objectives and supplies their curvature and gradient Lipschitz bounds.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `15. Juli - 21. Juli/All you... math 13`, single physical page, quadratic-form warning, componentwise derivation, symmetric half-quadratic convention, and rectangular squared-norm example through end.
