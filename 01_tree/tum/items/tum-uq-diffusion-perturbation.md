---
id: tum-uq-diffusion-perturbation
source: tum-numuq
parent: uq-stochastic-galerkin
title: Solution sensitivity to diffusion approximation
type: theorem
caption: Controls coefficient truncation error in a uniform norm and explains why KL mean-square convergence alone is insufficient.
---

# Solution sensitivity to diffusion approximation

Let \(a\) and \(\widetilde a\) both satisfy the deterministic uniform ellipticity/boundedness conditions, and let \(u,\widetilde u\in V=L^2(\Omega;H_0^1(D))\) solve their stochastic weak problems with the same forcing. Subtracting their equations and testing with \(e=\widetilde u-u\) gives
\[
\widetilde a_{\min}\|e\|_V^2\le E\int_D(a-\widetilde a)\nabla u\cdot\nabla e
\le\|a-\widetilde a\|_{L^\infty(\Omega;C(\overline D))}\|u\|_V\|e\|_V.
\]
The intermediate bound requires absolute values of gradients/products before Cauchy–Schwarz; the notes suppress them. Thus
\[
\|\widetilde u-u\|_V\le\widetilde a_{\min}^{-1}\|a-\widetilde a\|_{L^\infty(\Omega;C(\overline D))}\|u\|_V.
\]
For convergence over truncations, the approximate lower bound must remain uniformly positive.

A general KL expansion converges in \(L^2(\Omega;L^2(D))\), which does not provide this stronger coefficient norm or preserve positivity automatically. For the bounded uniform-input cosine model with coefficients \(\sigma/(\pi k)^2\), however, its infinite tail is bounded uniformly by \(\sigma/(\pi^2M)\) after \(M\) terms, using \(\sum_{k>M}k^{-2}\le1/M\). If \(\mu>\sigma/6\), both full and truncated coefficients have the same positive lower bound, and the theorem gives a controlled solution error.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.2, Assumption 10.5, Theorems 10.6–10.7 with proof, Remark 10.8 and Example 10.9, pp. 73–75.
- `Lecture Topics and Slides/Lecture 17 (08.07.24)`, physical pp. 2–5 (printed 7–10).
