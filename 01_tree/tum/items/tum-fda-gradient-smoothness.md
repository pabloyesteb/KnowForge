---
id: tum-fda-gradient-smoothness
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Bounding gradient Lipschitz constants by Hessians
type: theorem
caption: "Distinguishes function Lipschitz continuity from gradient smoothness and bounds the latter by Hessian operator norms."
---

# Bounding gradient Lipschitz constants by Hessians

For a twice continuously differentiable scalar function on a convex domain, a uniform Hessian bound \(\|\nabla^2 f(x)\|_2\le L\) implies
\[
\|\nabla f(x)-\nabla f(y)\|_2\le L\|x-y\|_2.
\]
Apply the Jacobian criterion to the vector map \(\nabla f\). For a symmetric Hessian the operator norm is the largest absolute eigenvalue, so negative eigenvalues also contribute; the largest signed eigenvalue alone is insufficient outside the positive-semidefinite case. The Frobenius norm is an accessible upper bound but can be less sharp.

This is a bound on the variation of the gradient. In contrast, a uniform bound on \(\|\nabla f\|\) controls the Lipschitz constant of \(f\) itself. These constants have different roles. The weekly gradient-descent review's rule \(\eta\le1/L\) uses a Lipschitz constant of the gradient; the bounded-gradient estimate for a function cannot be substituted for it. Convergence claims additionally require the relevant optimization assumptions; a Hessian norm bound by itself does not imply convexity or convergence to a global minimum.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `15. Juli - 21. Juli/All you... math 13`, single physical page, distinction between Lipschitz continuity of a function and of its gradient; Hessian spectral/Frobenius estimates.
- `15. Juli - 21. Juli/Solution Sheet 12.pdf`, single physical page, final gradient-step reminder following Exercise 12.2.
