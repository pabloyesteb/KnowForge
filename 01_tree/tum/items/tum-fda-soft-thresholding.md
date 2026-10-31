---
id: tum-fda-soft-thresholding
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Subgradient derivation of soft thresholding
type: algorithm
caption: "Solves quadratic-plus-absolute-value minimization and describes the piecewise-linear thresholded mass."
---

# Subgradient derivation of soft thresholding

For \(\lambda\ge0\), minimize \(f(x)=\frac12(y-x)^2+\lambda|x|\) over real \(x\). The absolute-value subdifferential is \(\{1\}\) at positive \(x\), \(\{-1\}\) at negative \(x\), and \([-1,1]\) at zero. Convex subgradient optimality yields
\[
0\in x-y+\lambda\partial|x|\quad\Longleftrightarrow\quad y\in x+\lambda\partial|x|.
\]
The three sign cases give the unique minimizer
\[
S_\lambda(y)=\operatorname{sign}(y)\max(|y|-\lambda,0)
=\begin{cases}y-\lambda&y>\lambda,\\0&|y|\le\lambda,\\y+\lambda&y<-\lambda.\end{cases}
\]
The quadratic term makes the objective strongly convex, so satisfying the inclusion suffices and the minimizer is unique, including the equality thresholds. The vector problem with squared Euclidean discrepancy and \(\ell_1\) penalty separates into these scalar problems.

For a fixed vector \(y\),
\[
h(\lambda)=\|S_\lambda(y)\|_1=\sum_i\max(|y_i|-\lambda,0).
\]
This is continuous, piecewise linear and nonincreasing, with \(h(0)=\|y\|_1\) and \(h(\lambda)=0\) for \(\lambda\ge\max_i|y_i|\). Away from breakpoints its slope is minus the number of surviving coordinates. Equal-magnitude entries can disappear together, changing the slope by more than one; after all entries vanish it is constant. The booklet asks for a plot for a chosen vector but supplies the analytic shape rather than a measured run.

The weekly solution interprets subgradients as supporting affine functions: \(g\in\partial f(x)\) means \(f(z)\ge f(x)+g^T(z-x)\) for every \(z\). Thus \(0\in\partial f(x)\) is exactly global minimality for a convex function. For the absolute value, all supporting slopes at the kink lie between minus one and one, giving the interval used in the threshold inclusion; a subdifferential is a set, so optimality uses membership rather than equality to one arbitrary slope.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.5(2), pp. 63–64 and solution pp. 72–73; Exercise 5.1.6, p. 64 and solution p. 74.
- `1. Juli - 7. Juli/Exercise Sheet 11.pdf`, Exercise 11.2(b1–b2), pp. 1–2; Exercise 11.3(a–b), p. 2.
- `8. Juli - 14. Juli/Solution Sheet 11.pdf`, single physical page, Exercise 11.2(b1–b2), subgradient geometry and three-case proof; Exercise 11.3, threshold-mass graph and slopes.
