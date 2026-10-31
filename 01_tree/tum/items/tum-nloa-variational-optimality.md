---
id: tum-nloa-variational-optimality
source: tum-nonlinear-optimization
parent: nloa-existence-geometry
title: Variational inequalities for constrained first-order optimality
type: theorem
caption: "Derives nonnegative gradient pairings along feasible segments and shows their global sufficiency when the objective is convex."
---

# Variational inequalities for constrained first-order optimality

Let \(X\subset\mathbb R^n\) be nonempty and convex, and \(f\) continuously differentiable on a neighborhood of \(X\). If \(\bar x\) globally minimizes \(f\) on \(X\), then
\[
\bar x\in X,\qquad
\nabla f(\bar x)^T(w-\bar x)\ge0\quad\forall w\in X.
\]
For fixed \(w\), the feasible segment \(v(t)=\bar x+t(w-\bar x)\), \(0\le t\le1\), gives \(f(v(t))-f(\bar x)\ge0\). Divide by \(t>0\) and let \(t\downarrow0\). No convexity of the objective is needed for this necessity argument.

If \(f\) is convex on \(X\), the inequality is also sufficient for global optimality: its supporting-plane inequality yields
\[
f(w)\ge f(\bar x)+\nabla f(\bar x)^T(w-\bar x)\ge f(\bar x)
\quad\forall w\in X.
\]
Thus the gradient need not vanish at a constrained minimizer; it must pair nonnegatively with all feasible displacement directions. Closedness is unnecessary for this characterization at an existing feasible point; it becomes relevant when constructing projections or proving existence.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 1.pdf`, T.1.3(a–b), pp. 1–2.
- `Exercise materials/Solution Exercise Sheet 1.pdf`, Solution 1.3(a–b), p. 4.
