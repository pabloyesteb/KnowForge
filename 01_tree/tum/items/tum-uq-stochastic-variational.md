---
id: tum-uq-stochastic-variational
source: tum-numuq
parent: uq-stochastic-galerkin
title: Stochastic variational formulation on space and probability
type: theorem
caption: Establishes a coupled Bochner-space weak problem under deterministic uniform ellipticity bounds.
---

# Stochastic variational formulation on space and probability

For deterministic \(f\in L^2(D)\), seek \(u\in V=L^2(\Omega;H_0^1(D))\) satisfying
\[
\mathcal A(u,v)=\ell(v)\quad\forall v\in V,\qquad
\mathcal A(u,v)=E\int_Da\nabla u\cdot\nabla v,\quad\ell(v)=E\int_Dfv.
\]
Unlike individual sample solves, test and trial functions depend jointly on space and the random outcome. The \(V\) norm is \((E|v|_{H^1}^2)^{1/2}\).

Under deterministic bounds \(0<a_{\min}\le a(x,\omega)\le a_{\max}<\infty\), Cauchy–Schwarz gives boundedness with constant \(a_{\max}\), and \(\mathcal A(v,v)\ge a_{\min}\|v\|_V^2\). Poincaré gives \(|\ell(v)|\le K_P\|f\|_{L^2}\|v\|_V\). Lax–Milgram therefore yields existence and uniqueness in \(V\). These are uniform bounds over space and probability, stronger than the realization-dependent bounds used for pathwise lognormal solvability; that earlier pathwise theorem does not automatically prove coercivity of this unweighted Bochner-space form.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.1, Definition 10.1 and Theorem 10.2 with proof, pp. 71–72.
- `Lecture Topics and Slides/Lecture 16 (02.07.24)`, physical pp. 1–5, model, forms and well-posedness.
- `Oral exam/Topics and sample questions (08.07.24)`, §10, p. 4, stochastic weak solution and well-posedness.
