---
id: tum-uq-mercer-kernels
source: tum-numuq
parent: uq-discretization
title: Mercer kernel expansion, diagonal tails and trace
type: theorem
caption: Relates uniform covariance expansions to positive eigenvalues and integrated pointwise variance.
---

# Mercer kernel expansion, diagonal tails and trace

For a continuous symmetric positive semidefinite kernel on a compact spatial closure, with Lebesgue integration on its bounded domain, the covariance integral operator has continuous positive-eigenvalue eigenfunctions and the Mercer expansion
\[
G(x,y)=\sum_j\lambda_j\phi_j(x)\phi_j(y),\qquad\lambda_j>0,
\]
converges uniformly. Finite-rank kernels have the corresponding finite expansion. The continuous representative follows from \(\phi_j(x)=\lambda_j^{-1}\int_DG(x,y)\phi_j(y)dy\).

Residual positivity and Cauchy–Schwarz give the useful diagonal-tail bound
\[
\sup_{x,y}|G(x,y)-G_J(x,y)|\le\sup_x\sum_{j>J}\lambda_j|\phi_j(x)|^2\longrightarrow0.
\]
The trace of a positive operator is \(\sum_k(L e_k,e_k)\) in an orthonormal basis. Mercer yields
\[
\operatorname{tr}L=\sum_j\lambda_j=\int_DG(x,x)dx<\infty,
\]
so the operator is trace class.

The proof strategy is spectral expansion of the kernel in product eigenfunctions, positivity of the residual kernel, uniform decay of its diagonal, and the displayed Cauchy–Schwarz bound. Dini's lemma upgrades monotone continuous functions converging to a continuous limit on a **compact** set to uniform convergence. Mere boundedness of an open domain does not suffice for Dini, boundedness of a continuous kernel, or the course's uniform Mercer conclusion. The compact continuous-kernel hypotheses must be retained; the notes' proof sketch also invokes Dini before explicitly establishing continuity of its diagonal limit, so that step alone is not a complete proof of Mercer.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Lemma 4.23, Definition 4.24 and Theorem 4.25 with its proof, pp. 34–36.
- `Lecture Topics and Slides/Lecture 08 (16.05.24)`, physical pp. 1–3 (printed 24–26), including added absolute value in the remainder bound.
