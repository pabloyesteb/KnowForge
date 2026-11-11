---
id: tum-uq-parameter-spectral-error
source: tum-numuq
parent: uq-stochastic-galerkin
title: Tensor polynomial projection error and directional exponential rates
type: theorem
caption: Reduces parameter approximation to univariate projections and links rapid convergence to derivative or analyticity
  control.
---

# Tensor polynomial projection error and directional exponential rates

For product parameter density and tensor polynomial degrees \(k_1,\ldots,k_M\), the coordinate projections commute and \(P_k=\prod_mP_{k_m}\). The identity
\[
I-\prod_mP_{k_m}=\sum_m\left(\prod_{i<m}P_{k_i}\right)(I-P_{k_m})
\]
and orthogonal-projection contractions give \(\|\widetilde u-P_k\widetilde u\|_V\le\sum_m\|(I-P_{k_m})\widetilde u\|_V\).

For the normalized uniform law on \([-\sqrt3,\sqrt3]\), the course's Legendre approximation estimate is
\[
\|(I-P_{k_m})v\|_{L_p^2}\le\frac{(\sqrt3)^{k_m+1}}{(k_m+1)!}\|\partial_{y_m}^{k_m+1}v\|_{L_p^2}.
\]
For sufficiently differentiable Hilbert-valued solutions, apply it to spatial gradient components, integrate, and sum coordinates:
\[
\|\widetilde u-P_k\widetilde u\|_V\le\sum_{m=1}^M\frac{(\sqrt3)^{k_m+1}}{(k_m+1)!}\|\partial_{y_m}^{k_m+1}\widetilde u\|_V.
\]
The derivative is of order \(k_m+1\), not a power of a first derivative; the lecture annotations clarify this notation. The estimate assumes the differentiability and integrability needed for the projection bound; factorial denominators alone do not ensure exponential convergence for an arbitrary smooth function with uncontrolled derivative growth.

For the uniformly elliptic affine model with the strong-solution and approximation hypotheses stated by the course, Theorem 10.38 supplies
\[
\|\widetilde u-P_k\widetilde u\|_V\le\frac{\sqrt3K_P}{\widetilde a_{\min}}\sum_m\alpha_m e^{-r_mk_m}\|f\|_{L^2},
\]
with directional constants depending on the coefficient functions. The detailed PDE derivative bounds are referred to the cited approximation-theory work, not derived in the notes. Direction-dependent rates motivate anisotropic degrees and the lecture's brief suggestion to adapt both input dimension and degrees; no adaptive algorithm is supplied.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.7.3, Definition 10.34, Corollary 10.35 with proof, Proposition 10.36, Lemma 10.37 with proof and Theorem 10.38, pp. 90–92.
- `Lecture Topics and Slides/Lecture 19 (16.07.24)`, physical pp. 7–11, directional projection estimates and corrected derivative notation.
