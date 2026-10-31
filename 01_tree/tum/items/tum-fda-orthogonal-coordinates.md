---
id: tum-fda-orthogonal-coordinates
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Finite orthogonal coordinates and Pythagoras–Fourier projection identities
type: theorem
caption: "Minimizes finite-basis approximation error by Fourier coefficients and derives projection-energy and residual identities."
---

# Finite orthogonal coordinates and Pythagoras–Fourier projection identities

Let \(W\) be a finite-dimensional subspace of a real or complex Hilbert space, with orthonormal basis \(w_1,\ldots,w_n\). With inner product linear in its first argument,
\[
P_Wv=\sum_{i=1}^n\langle v,w_i\rangle w_i.
\]
To derive it, expand an arbitrary candidate \(w=\sum_i\alpha_iw_i\):
\[
\|v-w\|^2=\|v\|^2-\sum_i|\langle v,w_i\rangle|^2
+\sum_i|\alpha_i-\langle v,w_i\rangle|^2.
\]
The last sum is minimized uniquely by the Fourier coefficients. Orthogonality gives
\[
\|P_Wv\|^2=\sum_i|\langle v,w_i\rangle|^2,\qquad
\|v-P_Wv\|^2=\|v\|^2-\sum_i|\langle v,w_i\rangle|^2.
\]
These identities describe exact finite-subspace approximation, not merely a coordinate convention. Finite-dimensional subspaces are closed, so the projection theorem applies; no completeness of an arbitrary infinite orthonormal system is asserted here.

The underlying inner-product norm also supplies Cauchy–Schwarz and the triangle inequality. The booklet's further exercises ask for their equivalence in a real pre-Hilbert space; these inequalities concern inner-product geometry and do not require completion. Completion is needed in the separate existence proof for projections onto arbitrary closed convex sets.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 1.1.5, p. 5; further Pythagoras–Fourier/pre-Hilbert exercises, p. 6; solution, p. 13.
- `22. April - 28. April/Problem Set 1.pdf`, Exercise 1.2, p. 1.
