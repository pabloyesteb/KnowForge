---
id: tum-uq-pathwise-pde-moments
source: tum-numuq
parent: uq-pde
title: Pathwise random PDE solutions and inverse-ellipticity moments
type: theorem
caption: Turns realization-wise energy estimates into Bochner integrability and clarifies the required measurability.
---

# Pathwise random PDE solutions and inverse-ellipticity moments

For deterministic \(f\in L^2(D)\) and a measurable random diffusion field whose realizations satisfy \(0<a_{\min}(\omega)\le a(x,\omega)\le a_{\max}(\omega)<\infty\), solve
\[
\int_Da(x,\omega)\nabla u(x,\omega)\cdot\nabla v(x)dx=\int_Dfv\quad\forall v\in H_0^1(D)
\]
for almost every outcome. Deterministic Lax–Milgram gives a unique solution for each such realization and
\[
|u(\omega)|_{H^1}\le K_Pa_{\min}(\omega)^{-1}\|f\|_{L^2}.
\]
Measurability of the coefficient as a function-valued variable, together with continuity of the solution map on the positive-coefficient set, is needed to conclude that \(u\) is an \(H_0^1\)-valued random variable; continuity by itself is not a substitute for measurable input data.

If \(a_{\min}^{-1}\in L^p(\Omega)\), then
\[
\|u\|_{L^p(\Omega;H_0^1)}\le K_P\|a_{\min}^{-1}\|_{L^p}\|f\|_{L^2},\qquad
\|u\|_{L^p(\Omega;L^2)}\le K_P^2\|a_{\min}^{-1}\|_{L^p}\|f\|_{L^2}.
\]
All finite inverse-ellipticity moments give all finite solution moments; pathwise solvability alone does not. Uniform ellipticity makes the inverse bound deterministic, while lognormal models use Fernique's theorem. A Bochner \(L^2(\Omega;L^2(D))\) variable supplies pointwise second moments for almost every spatial point in a measurable representative; the notes' Remark 6.11 should not be read as pointwise evaluation at every \(x\) without additional regularity.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §6.2, Theorems 6.9–6.10, inequalities (6.7)–(6.8) and Remark 6.11, pp. 48–49.
- `Lecture Topics and Slides/Lecture 10 (04.06.24)`, physical pp. 11–13, solution map, pathwise bound and Bochner estimates.
- `Oral exam/Topics and sample questions (08.07.24)`, §6, p. 3, pathwise weak problems and lognormal challenges.
