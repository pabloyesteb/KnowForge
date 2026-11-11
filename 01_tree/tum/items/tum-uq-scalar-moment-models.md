---
id: tum-uq-scalar-moment-models
source: tum-numuq
parent: uq-probability
title: Scalar moments and Gaussian lognormal parameterization
type: concept
caption: "Relates means, variances and exponential Gaussian transforms used to parameterize uncertain coefficients."
---

# Scalar moments and Gaussian lognormal parameterization

For a scalar integrable variable the first moment is \(E[X]\). Higher moments \(E[X^k]\) require corresponding integrability; central moments use \(X-E[X]\), and variance is \(E[(X-E[X])^2]\) when finite. Standard deviation is its nonnegative square root. For \(X\sim U(a,b)\), \(E[X]=(a+b)/2\) and \(\operatorname{var}X=(b-a)^2/12\). For \(Y\sim N(\mu,\sigma^2)\), the Gaussian density is proportional to \(\exp(-(y-\mu)^2/(2\sigma^2))\), with the indicated mean and variance.

Exponentiating a Gaussian gives a positive lognormal variable \(X=\exp Y\). Its parameters \(\mu,\sigma\) describe the underlying logarithm, and generally are not the mean and standard deviation of \(X\):
\[
E[X]=\exp(\mu+\sigma^2/2),\qquad
\operatorname{var}X=(\exp(\sigma^2)-1)\exp(2\mu+\sigma^2).
\]
This distinction matters when positive uncertain material coefficients are specified through a Gaussian latent model.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.1, Definitions 2.18–2.19 and Examples 2.23–2.25, pp. 6–7.
- `Lecture Topics and Slides/Lecture 02 (18.04.24)`, physical pp. 12–15 (printed 11–14), moments and scalar distributions.
