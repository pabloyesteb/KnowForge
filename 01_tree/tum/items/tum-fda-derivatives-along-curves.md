---
id: tum-fda-derivatives-along-curves
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: First and second objective derivatives along curves
type: method
caption: "Applies the chain rule to separate directional curvature from curve acceleration and derives objective decay along gradient flow."
---

# First and second objective derivatives along curves

Let \(f:\mathbb R^n\to\mathbb R\) and \(\gamma:\mathbb R\to\mathbb R^n\) be twice continuously differentiable, and set \(g(t)=f(\gamma(t))\). Then
\[
g'(t)=\nabla f(\gamma(t))^T\gamma'(t),
\]
\[
g''(t)=\gamma'(t)^T\nabla^2f(\gamma(t))\gamma'(t)
+\nabla f(\gamma(t))^T\gamma''(t).
\]
The second derivative includes both the Hessian along the velocity and the effect of curve acceleration. For a line \(\gamma(t)=x+th\), the acceleration vanishes, leaving \(g''(t)=h^T\nabla^2f(x+th)h\), which connects line convexity to Hessian tests.

Along a differentiable gradient-flow trajectory \(\gamma'(t)=-\nabla f(\gamma(t))\),
\[
\frac d{dt}f(\gamma(t))=-\|\nabla f(\gamma(t))\|_2^2\le0.
\]
This is continuous-time objective decay; it does not by itself establish global existence of the flow or convergence of a discrete gradient algorithm for arbitrary steps.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, “Derivations Along Curves”, first/second chain rules, gradient-flow remark and final segment example.
