---
id: tum-uq-antithetic-variates
source: tum-numuq
parent: uq-monte-carlo
title: Antithetic coupling and variance reduction at equal work
type: method
caption: Averages identically distributed coupled draws and identifies when negative covariance improves over independent
  sampling.
---

# Antithetic coupling and variance reduction at equal work

Couple \(X\) and \(X^a\) with the same marginal law and finite variance, and average \(Z=(X+X^a)/2\). Independent copies of the pair give an unbiased Monte Carlo estimator for \(EX\). Its per-pair variance is
\[
\operatorname{Var}Z=\tfrac12\operatorname{Var}X+\tfrac12\operatorname{Cov}(X,X^a)\le\operatorname{Var}X,
\]
by Cauchy–Schwarz. This inequality compares \(M\) paired averages with \(M\) individual draws and does not by itself prove an efficiency gain: pairs can cost twice as much.

At the cost of \(2M\) individual evaluations, independent averaging has variance \(\operatorname{Var}X/(2M)\). The antithetic estimator improves on it when \(\operatorname{Cov}(X,X^a)<0\). Perfectly positive coupling can give no variance benefit despite doubled evaluation work.

For \(U\sim U[0,1]\), \(1-U\) has the same law and \(\operatorname{Cov}(U,1-U)=1/6-1/4=-1/12\). In the example integral \(Ee^{U^2}\), pairing \(e^{U^2}\) with \(e^{(1-U)^2}\) exploits oppositely ordered responses. The notes motivate this transformed coupling rather than presenting a measured speedup.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §7.3.3, Lemma 7.7, proof, equal-cost comparison and Example 7.8, pp. 57–58.
