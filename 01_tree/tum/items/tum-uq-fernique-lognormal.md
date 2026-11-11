---
id: tum-uq-fernique-lognormal
source: tum-numuq
parent: uq-pde
title: Fernique tails and all-order lognormal ellipticity moments
type: theorem
caption: Controls positive and negative powers of coefficient extrema through Gaussian function-space tails.
---

# Fernique tails and all-order lognormal ellipticity moments

A centered Gaussian measure on a separable Banach space \(E\) is one for which each bounded linear functional has a centered scalar Gaussian law. Fernique's theorem gives constants \(s,K>0\) with
\[
P(\|Z\|_E\ge r)\le Ke^{-sr^2}.
\]
For \(0<t<s\), the layer-cake identity \(EX=\int_0^\infty P(X\ge z)dz\), applied to \(X=e^{t\|Z\|_E^2}\), bounds the tail integral by \(K\int_1^\infty z^{-s/t}dz\); hence \(Ee^{t\|Z\|_E^2}<\infty\). The appendix derives the scalar Gaussian tail directly by shifting the density integral; the Banach-space theorem itself is cited.

For a centered Gaussian variable in \(C(\overline D)\), let \(a=e^Z\). Then \(e^{-\|Z\|_C}\le a_{\min}\le a_{\max}\le e^{\|Z\|_C}\). For any real \(b\), Young's inequality gives
\[
p|b|\|Z\|_C\le t\|Z\|_C^2+\frac{p^2b^2}{4t}.
\]
Therefore every real power of either extremum belongs to every finite \(L^p\), including inverse powers of the minimum. Products \(a_{\min}^{b_1}a_{\max}^{b_2}\) have finite moments as well, by Cauchy–Schwarz with doubled powers. This supplies moment control for pathwise PDE stability and coefficient-ratio error estimates even though deterministic uniform ellipticity is unavailable. Applying Fernique here requires the Gaussian measurable \(C(\overline D)\)-valued version, not just pointwise Gaussian marginals.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, appendix D, Definition D.1, Theorem D.3, Remark D.4, Corollary D.5 and Lemmas D.6–D.7 with proofs, pp. 102–104 before appendix E.
- `Lecture Topics and Slides/Lecture 10 (04.06.24)`, physical pp. 18–24 (title and printed 34–39).
- `Oral exam/Topics and sample questions (08.07.24)`, §6, p. 3, Fernique statement and its PDE application.
