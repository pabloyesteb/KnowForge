---
id: tum-fda-density-convolution
source: tum-foundations-data-analysis
parent: fda-probability
title: Convolution densities for sums of independent variables
type: theorem
caption: "Integrates the independent joint density over a half-plane to recover the sum CDF and convolution density."
---

# Convolution densities for sums of independent variables

For independent real variables \(X,Y\) with densities \(\varphi_X,\varphi_Y\), their joint density factors. Integrating over \(x+y\le t\) gives
\[
F_{X+Y}(t)=\int_{\mathbb R}\varphi_X(x)
\left(\int_{-\infty}^{t-x}\varphi_Y(y)\,dy\right)dx
=\int_{\mathbb R}\varphi_X(x)F_Y(t-x)\,dx.
\]
Differentiation in the density sense yields, almost everywhere,
\[
\varphi_{X+Y}(t)=\int_{\mathbb R}\varphi_X(x)\varphi_Y(t-x)\,dx
=(\varphi_X*\varphi_Y)(t).
\]
The half-plane limit \(t-x\) explains the shifted second factor. Independence and the density assumptions are necessary for this product-density derivation; one cannot obtain the sum density from marginal convolution for an arbitrary dependent pair. The CDF identity also avoids requiring pointwise differentiability of an arbitrary density everywhere.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.7, p. 43; solution, p. 56.
- `10. Juni - 16. Juni/Problem Set 8.pdf`, Exercise 8.3, p. 2.
- `17. Juni - 23. Juni/Solution Sheet 8.pdf`, single physical page, Exercise 8.3, integration-domain diagram, iterated integral and CDF differentiation.
