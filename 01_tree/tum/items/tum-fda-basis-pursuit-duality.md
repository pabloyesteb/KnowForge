---
id: tum-fda-basis-pursuit-duality
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Lagrange dual of basis pursuit
type: theorem
caption: "Derives the l-infinity dual feasibility constraint for l1 minimization with equality data constraints."
---

# Lagrange dual of basis pursuit

Basis pursuit solves
\[
\min_x\|x\|_1\quad\text{subject to }Ax=y,
\qquad A\in\mathbb R^{m\times n}.
\]
Using the source's multiplier sign convention,
\[
L(x,\xi)=\|x\|_1+\xi^T(Ax-y),\qquad
H(\xi)=\inf_xL(x,\xi).
\]
Set \(z=A^T\xi\). If \(\|z\|_\infty\le1\), then \(x^Tz\ge-\|x\|_1\|z\|_\infty\), hence \(L(x,\xi)\ge-\xi^Ty\); equality holds at \(x=0\). If some \(|z_i|>1\), take \(x=-t\operatorname{sign}(z_i)e_i\). Its variable-dependent objective is \(t(1-|z_i|)\to-\infty\). Thus
\[
H(\xi)=\begin{cases}-\xi^Ty&\|A^T\xi\|_\infty\le1,\\-\infty&\text{otherwise},\end{cases}
\]
and the dual problem is
\[
\max_{\|A^T\xi\|_\infty\le1}-\xi^Ty.
\]
The \(\ell_\infty\) condition arises from its dual pairing with the \(\ell_1\) norm, not from a componentwise primal constraint. Changing the multiplier sign would change the displayed dual objective consistently. The derivation supplies a dual lower bound on any feasible primal value; it does not by itself prove feasibility, attainment, equality of optimal values, or a sparse-recovery guarantee for an arbitrary \(A,y\).

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.7, p. 65; two-case dual-function proof and dual maximization, p. 75.
- `8. Juli - 14. Juli/Exercise Sheet 12.pdf` and `15. Juli - 21. Juli/Solution Sheet 12.pdf` (single physical solution page), Exercise 12.1, p. 1; corresponding solution, coordinatewise infimum and dual feasibility.
