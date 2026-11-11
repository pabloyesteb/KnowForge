---
id: tum-uq-hilbert-gaussian-fields
source: tum-numuq
parent: uq-random-fields
title: Viewing a measurable Gaussian process as an L2-valued Gaussian
type: theorem
caption: Uses mean-square continuity and Gaussian quadrature limits to obtain a function-valued Gaussian variable.
---

# Viewing a measurable Gaussian process as an L2-valued Gaussian

A strongly measurable variable in a separable Banach space is Gaussian when every bounded linear functional of it is a scalar Gaussian (allowing zero variance). Let \(Z:[0,1]\times\Omega\to\mathbb R\) be a jointly measurable centered Gaussian process with continuous covariance \(C\).

The mapping \(t\mapsto Z(t)\) is continuous in \(L^2(\Omega)\) exactly when \(C\) is continuous: use \(E|Z(t)-Z(s)|^2=C(t,t)+C(s,s)-2C(t,s)\) in one direction, and Cauchy–Schwarz on covariance differences in the other. Compactness gives bounded diagonal variance and uniform mean-square continuity.

For \(h\in L^2(0,1)\), Tonelli and Cauchy–Schwarz give
\[
E\int_0^1|h(t)Z(t)|\,dt\le\sup_t C(t,t)^{1/2}\|h\|_{L^1}<\infty.
\]
Thus the integral is defined almost surely. Approximate it by
\[
Y_n=\sum_{i=0}^{n-1}Z(i/n)\int_{i/n}^{(i+1)/n}h(t)\,dt.
\]
Each sum is Gaussian. The integral triangle inequality bounds its \(L^2(\Omega)\) error by \(\int |h(t)|\|Z(t)-Z(\lfloor nt\rfloor/n)\|_{L^2(\Omega)}dt\to0\). Scalar Gaussian laws are closed under \(L^2\) convergence, so the limit is Gaussian.

Also \(E\|Z\|_{L^2(0,1)}^2=\int C(t,t)dt<\infty\). Joint measurability and separability supply the function-valued measurable representative. Riesz representation identifies every bounded linear functional on spatial \(L^2\) with pairing against such an \(h\); hence \(Z\) is an \(L^2(0,1)\)-valued Gaussian. This conclusion gives square-integrable spatial realizations, not continuous sample paths merely from covariance continuity.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 01 (25.04.2024)`, Problem 4 and its Banach-valued Gaussian definition; `Problem Sheets/Solution Sheet 01 (update  complete).pdf`, pp. 3–5, parts (a)–(d).
