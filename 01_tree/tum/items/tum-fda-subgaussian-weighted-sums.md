---
id: tum-fda-subgaussian-weighted-sums
source: tum-foundations-data-analysis
parent: fda-probability
title: Subgaussian tails and independent weighted sums
type: theorem
caption: "Optimizes an exponential quadratic MGF bound and tracks the coefficient norm in independent sums."
---

# Subgaussian tails and independent weighted sums

A mean-zero variable is subgaussian in the booklet's convention if some \(K>0\) satisfies
\[
\mathbb E e^{\theta X}\le e^{K^2\theta^2}\quad\text{for all real }\theta.
\]
For \(t>0\), positive exponential tilting bounds each one-sided tail by \(e^{K^2\theta^2-\theta t}\). Choosing \(\theta=t/(2K^2)\), and applying the same argument to \(-X\), gives
\[
\mathbb P(|X|>t)\le2e^{-t^2/(4K^2)}.
\]
The square on \(t\) and the event direction follow from this minimization; several displayed formulas in the booklet's solution omit or reverse them.

For independent mean-zero variables with the same bound and real coefficients \(a_i\), factor their MGFs:
\[
\mathbb E\exp\!\left(\theta\sum_i a_iX_i\right)
\le\prod_i e^{K^2a_i^2\theta^2}
=e^{K^2\|a\|_2^2\theta^2}.
\]
Thus the sum is subgaussian with parameter \(K\|a\|_2\), and for \(a\ne0\),
\[
\mathbb P\left(\left|\sum_i a_iX_i\right|>t\right)
\le2\exp\left(-\frac{t^2}{4K^2\|a\|_2^2}\right).
\]
For zero coefficients the sum is identically zero. Independence enables the MGF product; identical distribution is sufficient but the uniform bound is the property actually used. For a standard Gaussian one may take \(K^2=1/2\).

The weekly solution allows distinct subgaussian parameters \(K_i\): independence gives \(\mathbb E\exp(\theta\sum_i a_iX_i)\le\exp(\theta^2\sum_iK_i^2a_i^2)\). Thus the tail denominator can be \(4\sum_iK_i^2a_i^2\); replacing every \(K_i\) by their maximum is a simpler, possibly looser bound. Neither symmetry of each variable's law nor identical distributions are needed when both signs of the MGF parameter are controlled.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.5, pp. 42–43; solution, p. 53, interpreted through its exponential-moment derivation.
- `10. Juni - 16. Juni/Problem Set 8.pdf`, Exercise 8.1(a–b), p. 1.
- `17. Juni - 23. Juni/Solution Sheet 8.pdf`, single physical page, Exercise 8.1(a–b) and distinct-parameter remark.
