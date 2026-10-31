---
id: tum-nloa-augmented-lagrangian
source: tum-nonlinear-optimization
parent: nloa-second-order-penalty
title: Augmented-Lagrangian local exactness through Debreu's lemma
type: method
---

# Augmented-Lagrangian local exactness through Debreu's lemma

For \(\min f(x)\) with \(h(x)=0\), adding any fixed multiplier term \(\mu^Th(x)\) leaves all constrained objective comparisons unchanged. Applying a quadratic penalty to this equivalent constrained Lagrangian problem gives
\[
P_\alpha^\mu(x)=f(x)+\mu^Th(x)+\frac\alpha2\|h(x)\|^2.
\]
This is not simply a nonnegative penalty added to \(f\); the multiplier term can change sign off the constraint set.

## Local exactness at the correct multiplier

Let \(f,h\in C^2\), \((\bar x,\bar\mu)\) be KKT, and assume Lagrangian Hessian positivity on nonzero equality-tangent directions:
\[
d^T H d>0\quad\text{if }d\ne0,\quad Ad=0,
\qquad H=\nabla_{xx}^2L(\bar x,\bar\mu),\quad A=\nabla h(\bar x)^T.
\]
Feasibility and stationarity give
\[
\nabla P_\alpha^{\bar\mu}(\bar x)=0,\qquad
\nabla^2P_\alpha^{\bar\mu}(\bar x)=H+\alpha A^TA.
\]
Debreu's lemma makes this Hessian positive definite for all sufficiently large \(\alpha\). Hence \(\bar x\) is a strict unconstrained local minimizer of \(P_\alpha^{\bar\mu}\): local exactness holds with a finite penalty once the correct multiplier is fixed. The result is local and conditional on that multiplier and curvature; it does not assert global exactness or supply a multiplier-update algorithm.

## Debreu's lemma

If symmetric \(H\) is positive on \(\ker A\setminus\{0\}\), then \(H+\rho A^TA\) is positive definite for all sufficiently large \(\rho\). Otherwise select unit \(d_k\) with
\[
0\ge d_k^T(H+kA^TA)d_k=d_k^THd_k+k\|Ad_k\|^2.
\]
A subsequence converges to unit \(d\), with \(d^THd\le0\). Boundedness of \(d_k^THd_k\) gives \(\|Ad_k\|^2\le-d_k^THd_k/k\to0\), so \(Ad=0\), a contradiction. Monotonicity of the added positive-semidefinite term then extends positivity to every larger parameter.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 5.pdf`, T.5.4(a–c), p. 2; `Exercise materials/Solution Exercise Sheet 5.pdf`, Solution 5.4, pp. 4–5, including the proof of Debreu's lemma.
