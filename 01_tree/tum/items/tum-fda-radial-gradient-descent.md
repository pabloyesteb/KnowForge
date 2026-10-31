---
id: tum-fda-radial-gradient-descent
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Gradient descent for a quadratic objective with a linear radial tail
type: algorithm
caption: "Proves finite entry into a quadratic region followed by geometric convergence for a fixed gradient step."
---

# Gradient descent for a quadratic objective with a linear radial tail

Fix \(a\in\mathbb R^2\), \(\|a\|<1\), and let
\[
f(x)=\begin{cases}\|x\|^2-\langle a,x\rangle&\|x\|\le1,\\2\|x\|-\langle a,x\rangle-1&\|x\|>1.\end{cases}
\]
Its gradient is \(2x-a\) inside the unit ball and \(2x/\|x\|-a\) outside; the formulas agree on the boundary. Consequently \(\|\nabla f\|\le2+\|a\|<3\), and integration along segments proves that \(f\) is 3-Lipschitz. A Lipschitz upper bound need not be the smallest possible constant. The unique minimizer is \(a/2\): inside, complete the square; outside, the radial derivative along any ray is \(2-\langle a,u\rangle>0\), so moving toward the unit ball decreases the value.

Apply \(x_{k+1}=x_k-\eta\nabla f(x_k)\) with \(\eta=1/4\). Inside the ball,
\[
x_{k+1}=\tfrac12x_k+\tfrac14a,\qquad
x_k-\tfrac12a=2^{-(k-k_0)}(x_{k_0}-\tfrac12a).
\]
The ball is invariant because \(\|x_{k+1}\|\le\frac12+\frac14\|a\|<1\). Outside it,
\[
x_{k+1}=(\|x_k\|-2\eta)\frac{x_k}{\|x_k\|}+\eta a,
\quad\|x_{k+1}\|\le\|x_k\|-2\eta+\eta\|a\|<\|x_k\|-\eta.
\]
The positive radial coefficient permits this estimate. The iterates therefore enter the ball after finitely many steps from every initial point and then converge geometrically to \(a/2\).

More generally, the same invariant-ball and finite-entry proof works for \(0<\eta\le1/2\). The interior error recurrence is \(e_{k+1}=(1-2\eta)e_k\); its formal stability condition \(0<\eta<1\) alone does not establish invariance or the outside-region argument. The booklet's specialized recurrence prints a minus sign before \(a/4\); its general update, the weekly solution and the minimizer require the plus sign above.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 6.1.1, p. 77 and solution p. 78.
- `8. Juli - 14. Juli/Exercise Sheet 12.pdf`, Exercise 12.2, p. 1.
- `15. Juli - 21. Juli/Solution Sheet 12.pdf`, single physical page, Exercise 12.2, bounded gradient, interior recurrence, invariant ball and exterior finite-entry argument.
