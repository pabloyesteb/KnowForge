---
id: tum-uq-expectation-quadrature
source: tum-numuq
parent: uq-monte-carlo
title: Expectation as weighted integration and alternatives to random quadrature
type: concept
caption: Relates Monte Carlo to deterministic quadrature choices and their smoothness and dimension dependence.
---

# Expectation as weighted integration and alternatives to random quadrature

For a variable with density \(p\), expectation is integration against its law: \(EX=\int x\,p(x)dx\), and \(Ef(X)=\int f(x)p(x)dx\). Monte Carlo is a quadrature rule with iid random nodes distributed according to that law and equal weights \(1/M\). For example, \(\int_0^1e^{x^2}dx=Ee^{X^2}\) for \(X\sim U[0,1]\).

The course contrasts it with Gaussian quadrature, nested Clenshaw–Curtis nodes, tensor products of univariate rules, sparse grids reducing tensor-product node counts, and quasi-Monte Carlo equal-weight deterministic nodes on \([0,1]^s\). These are presented as alternatives, without deriving individual convergence theorems. Their efficiency depends on integrand regularity, the relevant function space and dimension; tensor products exhibit rapidly growing node counts. The reference weight one on \([-1,1]\) is an unnormalized integration weight, not a probability density unless divided by two. Monte Carlo's \(M^{-1/2}\) RMSE requires only finite variance rather than smoothness, though its constants and evaluation cost still matter.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §7.3.1, Example 7.6 and alternative quadrature list, pp. 55–56.
- `Lecture Topics and Slides/Lecture 12 (13.06.24)`, physical pp. 2–4 (printed 14–16).
