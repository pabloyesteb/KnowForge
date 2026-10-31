---
id: tum-fda-metric-completeness
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Cauchy sequences, metric completeness and an integral-distance counterexample
type: concept
caption: "Contrasts convergence of a diagonal iteration with continuous functions whose integral-distance Cauchy limit lies outside the space."
---

# Cauchy sequences, metric completeness and an integral-distance counterexample

A Cauchy sequence becomes arbitrarily close to itself in the chosen metric; completeness additionally requires its limit to belong to the space. Both the metric and the underlying set matter.

For \(\rho(x,y)=\sum_i|x_i-y_i|\) on \(\mathbb R^2\) and \(A=\operatorname{diag}(1/3,1/4)\),
\[
x_m=A^mx_0,\qquad
\rho(x_m,0)=3^{-m}|(x_0)_1|+4^{-m}|(x_0)_2|\to0.
\]
This explicitly verifies convergence of a contracting diagonal iteration in the specified metric.

In contrast \(C([0,1])\) is not complete under
\(\rho(f,g)=\int_0^1|f(t)-g(t)|dt\). For \(m\ge2\), let \(f_m\) be zero on \([0,1/2]\), rise linearly with slope \(m\) on \((1/2,1/2+1/m)\), then equal one. If \(n\ge m\), the area between the ramps is
\[
\rho(f_m,f_n)=\frac1{2m}-\frac1{2n}\le\frac1{2m},
\]
so the sequence is Cauchy. A continuous limit \(f\) in this metric would have to be zero on \([0,1/2)\) and one on \((1/2,1]\): the nonnegative integrals of the respective differences tend to zero, and continuity upgrades a.e. equality on each open interval to equality everywhere there. Such an \(f\) cannot be continuous at \(1/2\).

The obstruction is not failure of the Cauchy property but exclusion of the discontinuous limit from the given space. Convergence in integral distance is weaker than uniform convergence; no claim of a complete function space follows merely from finite-dimensional intuition.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 1.1.2, p. 3; solution and ramp illustration, pp. 8–9.
- `15. April - 21. April/Exercise sheet 0.pdf`, Exercise 0.2, pp. 1–2.
