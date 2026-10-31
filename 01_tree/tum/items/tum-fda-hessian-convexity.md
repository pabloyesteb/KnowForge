---
id: tum-fda-hessian-convexity
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Hessian characterization of twice differentiable convex functions
type: theorem
caption: "Equates convexity with positive semidefinite Hessians on open convex domains using supporting planes and Taylor formulas."
---

# Hessian characterization of twice differentiable convex functions

Let \(C\subset\mathbb R^n\) be open and convex and \(f\in C^2(C)\). Then
\[
f\text{ is convex}\quad\Longleftrightarrow\quad\nabla^2f(x)\succeq0\quad\text{for every }x\in C.
\]
For necessity, fix \(x\) and a direction \(z\). Openness permits sufficiently small displacements \(x+tz\) in both signs. Convexity's differentiable supporting inequality and the second-order expansion give
\[
0\le f(x+tz)-f(x)-t\nabla f(x)^Tz
=\tfrac12t^2z^T\nabla^2f(x)z+o(t^2).
\]
Divide by \(t^2\) and let \(t\to0\), obtaining a nonnegative quadratic form in every direction.

Conversely, along the segment from \(y\) to \(x\), Taylor with an intermediate Hessian gives
\[
f(x)=f(y)+\nabla f(y)^T(x-y)
+\tfrac12(x-y)^T\nabla^2f(\zeta)(x-y)
\ge f(y)+\nabla f(y)^T(x-y).
\]
This supporting-plane inequality characterizes differentiable convexity. To see it implies the chord inequality, apply it at \(z=\lambda x+(1-\lambda)y\) to each endpoint, multiply by the corresponding weight, and add; the gradient terms cancel. Domain convexity keeps the segment feasible. The factor \(1/2\), absent in one printed solution display, is part of Taylor's formula and does not change the nonnegativity argument.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.1(1), p. 62; solution using supporting inequality and Taylor, p. 66.
- `24. Juni - 30. Juni/Exercise sheet 10.pdf`, Exercise 10.1(a), p. 1.
- `1. Juli - 7. Juli/Solution sheet 10.pdf`, single physical page, Exercise 10.1(a), full argument and illustrations.
