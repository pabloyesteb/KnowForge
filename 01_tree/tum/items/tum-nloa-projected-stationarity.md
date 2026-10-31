---
id: tum-nloa-projected-stationarity
source: tum-nonlinear-optimization
parent: nloa-existence-geometry
title: Euclidean projection and projected-gradient stationarity
type: method
caption: "Characterizes constrained stationarity as a projected-gradient fixed point and identifies the convexity needed for global optimality."
---

# Euclidean projection and projected-gradient stationarity

For nonempty closed convex \(X\subset\mathbb R^n\), define
\[
P_X(y)=\operatorname*{argmin}_{x\in X}\frac12\|x-y\|_2^2.
\]
The objective is continuous and coercive, giving existence on closed \(X\); its strong convexity and convexity of \(X\) give uniqueness. Thus projection is a well-defined map on all of \(\mathbb R^n\).

For \(f\) continuously differentiable on a neighborhood of \(X\) and \(\tau>0\), let
\[
d_\tau(x)=x-P_X(x-\tau\nabla f(x)).
\]
Applying the variational inequality to the strongly convex projection objective gives
\[
d_\tau(\bar x)=0
\iff\bar x\in X,\quad
\tau\nabla f(\bar x)^T(w-\bar x)\ge0\quad\forall w\in X.
\]
For convex \(f\), this is equivalent to global constrained optimality. Every constrained global minimizer satisfies the fixed-point condition even without convexity of \(f\); convexity is what makes the condition sufficient. The positive step size cancels from the inequality, so the characterization holds for any \(\tau>0\), not a selected algorithmic step-size range.

The equation identifies a projected-gradient stationary point. By itself it proves neither convergence of repeated projected steps nor a convergence rate; no such iteration analysis is supplied by this exercise.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 1.pdf`, T.1.3(c–d), p. 2.
- `Exercise materials/Solution Exercise Sheet 1.pdf`, Solution 1.3(c–d), p. 4.
