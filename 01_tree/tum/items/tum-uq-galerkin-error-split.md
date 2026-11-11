---
id: tum-uq-galerkin-error-split
source: tum-numuq
parent: uq-stochastic-galerkin
title: Separating coefficient, spatial and parameter approximation errors
type: theorem
caption: Bounds mean error through a Bochner norm and separates finite-element and polynomial contributions with explicit
  regularity requirements.
---

# Separating coefficient, spatial and parameter approximation errors

Jensen bounds the mean error by \(\|Eu-E\widetilde u^{hk}\|_{H_0^1}\le\|u-\widetilde u^{hk}\|_V\). Split this into coefficient perturbation \(\|u-\widetilde u\|_V\), controlled in a uniform coefficient norm, and the discretization of the perturbed parametric solution.

The semidiscrete spatial solution \(\widetilde u^h\in L_p^2(\Gamma;W^h)\) leaves parameter dependence unrestricted and is the energy projection of \(\widetilde u\). For piecewise linear conforming elements on a shape-regular mesh, assume \(\widetilde u\in L_p^2(\Gamma;H^2(D))\) and \(\|\widetilde u\|_{L_p^2(H^2)}\le K_2\|f\|_{L^2}\). Interpolation and energy quasi-optimality give
\[
\|\widetilde u-\widetilde u^h\|_V\lesssim h\sqrt{\widetilde a_{\max}/\widetilde a_{\min}}\|f\|_{L^2}.
\]
Uniform ellipticity alone does not establish this \(H^2\) regularity assumption.

Let \(P_k\) be the orthogonal parameter projection onto \(S^k\), with Hilbert-valued coefficients. A separated approximation bound is
\[
\|\widetilde u-\widetilde u^{hk}\|_V\le\sqrt{\widetilde a_{\max}/\widetilde a_{\min}}
\big(\|\widetilde u-\widetilde u^h\|_V+\|\widetilde u-P_k\widetilde u\|_V\big).
\]
The source's proof uses an energy spatial projection \(P_hP_k\widetilde u\) as a tensor-space competitor. Because the diffusion depends on \(y\), that energy projection can itself depend on \(y\) and need not preserve polynomial degree. A valid justification uses instead the fixed spatial \(H_0^1\)-orthogonal projection \(R_h\): it commutes with parameter projection, is a contraction in \(V\), and \(R_hP_k\widetilde u\in W^h\otimes S^k\). Its spatial best error is no larger than \(\|\widetilde u-\widetilde u^h\|_V\). Energy best approximation and norm equivalence then give the displayed bound. Thus spatial interpolation and parameter approximation can be analyzed independently without assuming the coefficient-dependent energy projector preserves polynomials.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.7 through §10.7.2, Definition 10.27, Remark 10.28, Assumption 10.29, Lemma 10.30, Theorem 10.31, Definition 10.32 and Lemma 10.33 with proof, pp. 87–90.
- `Lecture Topics and Slides/Lecture 19 (16.07.24)`, physical pp. 1–7, error split, spatial regularity and handwritten adaptive-choice remark.
