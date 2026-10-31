---
id: tum-fda-covariance-correlation
source: tum-foundations-data-analysis
parent: fda-probability
title: Covariance, Pearson correlation and the limits of uncorrelatedness
type: concept
caption: "Measures linear association and separates zero correlation from independence except for jointly Gaussian variables."
---

# Covariance, Pearson correlation and the limits of uncorrelatedness

For real variables with finite second moments,
\[
\operatorname{Var}(X)=\mathbb E(X-\mathbb EX)^2=\mathbb EX^2-(\mathbb EX)^2,
\]
\[
\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)]
=\mathbb E(XY)-\mathbb EX\mathbb EY.
\]
When both variances are positive, the Pearson coefficient is
\[
\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}.
\]
It measures normalized linear association, not arbitrary dependence. The review's scatter examples contrast positive/negative line patterns with nonlinear shapes having zero correlation. Zero variance makes this normalized coefficient undefined.

Independence implies zero covariance whenever the needed moments exist, by factoring the product expectation. The converse fails in general: nonlinear dependence can survive a zero coefficient. In the special case of a jointly Gaussian pair, zero covariance does imply independence; Gaussian marginal distributions alone are not the same hypothesis as joint Gaussianity.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `10. Juni - 16. Juni/All you... math 8`, single physical page, “Correlation and Uncorrelation”, covariance/variance formulas, Pearson coefficient, scatter diagrams and Gaussian exception.
