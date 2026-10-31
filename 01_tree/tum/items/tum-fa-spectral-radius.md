---
id: tum-fa-spectral-radius
source: tum-functional-analysis
parent: fa-spectral-theory
title: Spectral radius and asymptotic operator-power growth
type: theorem
caption: "Identifies spectral radius with asymptotic operator-power growth using spectral mapping and scalar resolvent expansions."
---

# Spectral radius and asymptotic operator-power growth

For bounded \(T\) on a nonzero complex Banach space,
\[
r(T)=\max_{\lambda\in\sigma(T)}|\lambda|
=\lim_{n\to\infty}\|T^n\|^{1/n}
=\inf_{n\ge1}\|T^n\|^{1/n}.
\]
Polynomial spectral mapping gives \(\lambda^n\in\sigma(T^n)\), hence \(|\lambda|^n\le\|T^n\|\). Taking a maximum and then an infimum proves the lower bound for the power-growth expression.

For the reverse bound, apply \(\ell\in\mathcal L(X)^*\) to the resolvent. Its Laurent series for \(|\lambda|>\|T\|\) is
\[
\ell(R_\lambda)=\sum_{k=0}^\infty\lambda^{-k-1}\ell(T^k).
\]
Holomorphy and uniqueness of the Laurent expansion continue this scalar series to \(|\lambda|>r(T)\). Its terms tend to zero, so \(\lambda^{-k}T^k\) is weakly null in \(\mathcal L(X)\). Weak convergence implies norm-boundedness, yielding \(\|T^k\|^{1/k}\le |\lambda|M^{1/k}\). Thus \(\limsup_k\|T^k\|^{1/k}\le|\lambda|\), and letting \(|\lambda|\downarrow r(T)\) proves equality.

The radius measures asymptotic growth, while \(\|T\|\) controls one application. They need not be equal for an arbitrary bounded operator. For a normal Hilbert-space operator, the separate identity \(\|T^n\|=\|T\|^n\) makes them equal.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Lecture notes.pdf` (WS 2017/18), Definition 12.8, Proposition 12.9 and Eqs. (12.19)–(12.24), pp. 84–85; Proposition 13.4, p. 89.
