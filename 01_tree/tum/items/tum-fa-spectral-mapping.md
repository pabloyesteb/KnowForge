---
id: tum-fa-spectral-mapping
source: tum-functional-analysis
parent: fa-spectral-theory
title: Polynomial spectral mapping and commuting factorizations
type: theorem
---

# Polynomial spectral mapping and commuting factorizations

For bounded \(T\) on a nonzero **complex** Banach space and polynomial \(p(z)=\sum_{j=0}^nc_jz^j\), define \(p(T)=\sum_{j=0}^nc_jT^j\). Then
\[
\sigma(p(T))=p(\sigma(T)).
\]
The proof transfers scalar polynomial factorization to commuting operator factors. If \(AB=BA\) and \(AB\) is boundedly invertible, both \(A,B\) are boundedly invertible. The product inverse gives a right and a left inverse for each factor; a left inverse and a right inverse must coincide. Commutation is necessary to that argument.

For \(\lambda\in\sigma(T)\), factor \(p(z)-p(\lambda)=(z-\lambda)q(z)\). If \(p(T)-p(\lambda)I\) were invertible, the commuting-factor result would make \(T-\lambda I\) invertible, a contradiction. This gives one inclusion.

Conversely, for \(\mu\in\sigma(p(T))\), the fundamental theorem of algebra gives
\[
p(z)-\mu=c\prod_{j=1}^n(z-\lambda_j),\qquad
p(T)-\mu I=c\prod_{j=1}^n(T-\lambda_jI).
\]
Some factor must fail to be invertible, so \(\lambda_j\in\sigma(T)\) and \(\mu=p(\lambda_j)\). Constant polynomials are handled separately: \(p(T)=cI\) has spectrum \(\{c\}\).

In particular \(\sigma(T^n)=\{\lambda^n:\lambda\in\sigma(T)\}\). The source proves polynomial mapping, not a general holomorphic functional calculus.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Lecture notes.pdf` (WS 2017/18), Lemma 12.6 and Proposition 12.7, pp. 83–84, Eqs. (12.16)–(12.18). The factorization is a product; the printed sum signs in Eq. (12.18) are typographical errors.
