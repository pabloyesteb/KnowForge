---
id: tum-fda-l1-ball-projection
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Euclidean projection onto an l1 ball by threshold selection
type: algorithm
caption: "Finds a shared nonnegative threshold for exterior points and preserves points already in the ball."
---

# Euclidean projection onto an l1 ball by threshold selection

For the unit \(\ell_1\) ball \(B_1=\{x:\|x\|_1\le1\}\), Euclidean projection minimizes \(\frac12\|y-x\|_2^2\) under the constraint. Its Lagrangian is
\[
L(x,\lambda)=\tfrac12\|y-x\|_2^2+\lambda(\|x\|_1-1),\qquad\lambda\ge0.
\]
For a fixed multiplier, minimization in \(x\) separates coordinatewise into \(x_i=S_\lambda(y_i)\).

If \(\|y\|_1\le1\), take \(\lambda=0\) and return \(y\), already at zero distance. If \(\|y\|_1>1\), choose the unique positive threshold satisfying
\[
\sum_i\max(|y_i|-\lambda,0)=1.
\]
The left side is continuous and strictly decreasing while positive, so the root lies between zero and \(\max_i|y_i|\). Its piecewise-linear structure supports scalar root selection. Return the coordinatewise thresholded vector. It is feasible, minimizes its Lagrangian, and satisfies complementary slackness; comparing the Lagrangian values of feasible points proves projection optimality. Strict convexity of the squared-distance objective gives a unique projected point.

The booklet's unconditional boundary-equality prescription omits the feasible-input case. An interior input must remain itself, rather than being forced to norm one. The multiplier must also be nonnegative for the constraint \(\|x\|_1-1\le0\); an arbitrary negative threshold is not the stated projection procedure.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.5(1,3), pp. 63–64; Lagrangian and coordinate-separation solutions, pp. 72–73; threshold function, Exercise 5.1.6 and solution pp. 64, 74.
- `1. Juli - 7. Juli/Exercise Sheet 11.pdf`, Exercise 11.2(a,c), pp. 1–2.
- `8. Juli - 14. Juli/Solution Sheet 11.pdf`, single physical page, Exercise 11.2(a,c), nonnegative Lagrange multiplier and coordinate-separation argument.
