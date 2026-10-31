---
id: tum-fda-probability-events-laws
source: tum-foundations-data-analysis
parent: fda-probability
title: Events, random variables and probability laws
type: concept
caption: "Distinguishes events in the sample space from sets of variable values and computes probabilities through densities or discrete masses."
---

# Events, random variables and probability laws

A probability space is \((\Omega,\mathcal F,\mathbb P)\): elementary outcomes lie in \(\Omega\), measurable events belong to \(\mathcal F\), and \(\mathbb P\) assigns their probabilities. A real random variable is a measurable map \(X:\Omega\to\mathbb R\). For a measurable value set \(C\), notation \(\mathbb P(X\in C)\) means the probability of its inverse-image event \(\{\omega:X(\omega)\in C\}\); \(C\) itself need not be an event in the original sample space.

For an absolutely continuous law, \(\mathbb P(X\in C)=\int_C\varphi_X(x)\,dx\). For a finite discrete law with values \(x_i\) and masses \(p_i\), it is \(\sum_i p_i\mathbf1_C(x_i)\). For a fair die and \(C=[-3,3.2]\), this sums the masses of 1, 2 and 3, giving \(1/2\). Continuous and discrete probabilities require their respective representations; a finite discrete variable does not possess an ordinary Lebesgue density.

Monotonicity gives \(\mathbb P(A\cap B)\le\min(\mathbb P(A),\mathbb P(B))\). Inclusion–exclusion gives \(\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)\), with simple additivity only for disjoint events. Likewise, when computing the probability of a union of value intervals, merge or disjointify overlapping intervals before summing their integrals.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `10. Juni - 16. Juni/All you... math 8`, single physical page, opening probability-space discussion, random-variable inverse images, continuous/discrete laws, overlapping intervals and fair-die example.
