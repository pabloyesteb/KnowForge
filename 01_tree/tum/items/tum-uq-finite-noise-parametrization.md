---
id: tum-uq-finite-noise-parametrization
source: tum-numuq
parent: uq-stochastic-galerkin
title: Conditional expectation and finite-dimensional PDE parametrization
type: theorem
caption: Shows that the solution depends only on the coefficient inputs and transfers the problem to a weighted parameter
  domain.
---

# Conditional expectation and finite-dimensional PDE parametrization

For a separable Hilbert space \(H\), conditional expectation \(E[X\mid\mathcal G]\) is the orthogonal projection of \(L^2(\Omega,\mathcal A;H)\) onto its closed \(\mathcal G\)-measurable subspace. Under the uniform ellipticity assumptions, if the diffusion coefficient is \(\mathcal G\)-measurable and the forcing deterministic, the stochastic weak solution is \(\mathcal G\)-measurable as well.

To prove this, solve first in the smaller subspace, obtaining \(u_*\). For any full-space test \(v\), the projected test \(E[v\mid\mathcal G]\) lies in that subspace. The measurable coefficient and \(u_*\), the tower property, and commutation with the bounded spatial differential/pairing operations give \(\mathcal A(u_*,E[v\mid\mathcal G])=\mathcal A(u_*,v)\) and \(\ell(E[v\mid\mathcal G])=\ell(v)\). Thus \(u_*\) solves the full problem, and uniqueness identifies it with \(u\).

If \(\widetilde a\) depends on a finite vector \(\xi=(\xi_1,\ldots,\xi_M)\), choose \(\mathcal G=\sigma(\xi)\). Doob–Dynkin gives \(\widetilde u=\widetilde u(\xi)\). With joint density \(p\) on \(\Gamma\subset\mathbb R^M\), expectation becomes integration in \(y=\xi(\omega)\):
\[
E\|v(\xi)\|_{H_0^1}^2=\int_\Gamma p(y)|v(y)|_{H^1}^2dy.
\]
The equivalent weak problem is in \(L_p^2(\Gamma;H_0^1(D))\), with bilinear form \(\int_\Gamma p(y)\int_D\widetilde a(x,y)\nabla u\cdot\nabla v\). Uniform positive coefficient bounds yield well-posedness as before. It is an \((M+d)\)-dimensional deterministic parametric problem, with spatial Dirichlet conditions and no derivatives in \(y\). A density is needed for this Lebesgue-weighted representation; independence is only needed later to factor the density.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Definition 10.3, Corollary 10.4 with proof, §10.3, Definitions 10.10 and 10.12, Lemma 10.11, Assumption 10.13 and Theorem 10.14, pp. 73 and 75–76.
- `Lecture Topics and Slides/Lecture 16 (02.07.24)`, physical pp. 6–7, projection and handwritten diagram; `Lecture Topics and Slides/Lecture 17 (08.07.24)`, physical pp. 7–11, finite-dimensional noise and parameter forms.
- `Oral exam/Topics and sample questions (08.07.24)`, §10, p. 4, finite-dimensional noise.
