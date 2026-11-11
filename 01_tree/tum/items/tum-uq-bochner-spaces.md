---
id: tum-uq-bochner-spaces
source: tum-numuq
parent: uq-probability
title: Bochner norms and Hilbert-valued mean-square geometry
type: concept
caption: "Measures random function magnitudes by expected Banach norms and equips square-integrable Hilbert-valued variables with an inner product."
---

# Bochner norms and Hilbert-valued mean-square geometry

For a Banach space \(W\), \(L^p(\Omega;W)\), \(1\le p<\infty\), consists of strongly measurable variables with finite \(E\|X\|_W^p\), identified up to almost-sure equality. Its norm is \((E\|X\|_W^p)^{1/p}\), and the space is complete. The \(L^\infty\) norm is the essential supremum of \(\|X(\omega)\|_W\), so null-set values do not affect it. These are Bochner spaces; integrating a norm over probability is distinct from taking a spatial norm of the mean.

If \(W=H\) is Hilbert, then \(L^2(\Omega;H)\) is Hilbert with inner product \(E[(X,Y)_H]\). Its Cauchy–Schwarz inequality is
\[
|E[(X,Y)_H]|\le(E\|X\|_H^2)^{1/2}(E\|Y\|_H^2)^{1/2}.
\]
A variable in this space is mean-square integrable, and the same geometry measures approximation errors \(X_n-X\). The equivalence-class convention is needed for these expressions to define a norm, rather than merely a seminorm on pointwise representatives.

For independent \(u,v\in L^2(\Omega;H)\) in a separable real Hilbert space, \(E(u,v)_H=(Eu,Ev)_H\). Expand in a countable orthonormal basis: each paired coordinate is independent, and \(E\sum_k|u_kv_k|\le(E\|u\|^2)^{1/2}(E\|v\|^2)^{1/2}\) permits exchange of expectation and sum. Bounded linear functionals commute with Bochner expectation, identifying coordinate expectations with those of the mean.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Definition 2.50 and Remark 2.51, p. 11.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical pp. 15–16 (printed 29–30), complete norm, Hilbert inner-product and Cauchy–Schwarz displays.
- `Problem Sheets/Problem Sheet 01 (25.04.2024)`, Problem 3; `Problem Sheets/Solution Sheet 01 (update  complete).pdf`, pp. 2–3, independent Hilbert-valued variables.
