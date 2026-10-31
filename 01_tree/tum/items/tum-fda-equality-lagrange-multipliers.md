---
id: tum-fda-equality-lagrange-multipliers
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Lagrange multipliers for a smooth equality constraint
type: method
caption: "Uses tangent and normal directions to derive constrained stationarity and compare extrema on an ellipse."
---

# Lagrange multipliers for a smooth equality constraint

Consider a differentiable objective \(F:\mathbb R^m\to\mathbb R\) constrained by \(g(x)=0\), with \(g\) continuously differentiable. At a regular feasible point \(y\), \(\nabla g(y)\ne0\), the tangent space is orthogonal to \(\nabla g(y)\). A constrained local extremum must have zero objective derivative in every tangent direction. Consequently,
\[
\nabla F(y)=\lambda\nabla g(y),\qquad g(y)=0.
\]
With \(\mathcal L(x,\lambda)=F(x)-\lambda g(x)\), these are the stationarity equations in \(x\) and \(\lambda\). They identify candidates, not a sufficiency test; the nonzero constraint gradient is needed for the normal-space argument. Unconstrained differentiable local extrema instead satisfy \(\nabla F(y)=0\). For a nonzero gradient the unit direction of maximal first-order increase is its normalization, and its negative gives maximal decrease.

The review optimizes \(F(x_1,x_2)=3x_1+x_2\) on \(2x_1^2+x_2^2=1\). The equations are
\[
3=4\lambda x_1,\quad 1=2\lambda x_2,\quad 2x_1^2+x_2^2=1.
\]
Thus \(x_1=3x_2/2\), \(x_2=\pm\sqrt{2/11}\). Comparing values gives the maximum at \((\frac32\sqrt{2/11},\sqrt{2/11})\), and the minimum at its negative. The ellipse is compact and the gradient of its defining constraint is nonzero there, so the candidates exhaust the extrema. Coordinates here follow the equations in \((x_1,x_2)\) order; the final handwritten ordered pairs swap their order.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `29. April - 5. Mai/Notes All you... math week 2`, single physical page, “Lagrange Multipliers (Constrained Optimization)”, tangent/normal diagrams, Lagrangian and ellipse example.
