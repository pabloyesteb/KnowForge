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

In real Euclidean space the normalized inner product of nonzero vectors is \(\cos\theta=\langle x,y\rangle/(\|x\|_2\|y\|_2)\). It measures directional alignment: values near zero indicate near-orthogonality, while absolute values near one indicate alignment up to sign. This is geometric information, not by itself statistical independence. If \(Q\) has the orthonormal basis vectors as columns, the projection is \(QQ^Tx\). For example, projecting \((3,2)^T\) onto \(\operatorname{span}(1,1)^T\) gives \((5/2,5/2)^T\).

The finite-subspace projection is linear and admits \(P_W=\sum_i w_iw_i^T\), an SVD whose positive singular values are all one. Changing to another orthonormal basis of the same subspace leaves this operator unchanged. Its residual is perpendicular to every subspace vector: \(\langle x-P_Wx,y\rangle=0\) for all \(y\in W\); for a general closed convex set the corresponding condition is an inequality instead.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 1.1.5, p. 5; further Pythagoras–Fourier/pre-Hilbert exercises, p. 6; solution, p. 13.
- `22. April - 28. April/Problem Set 1.pdf`, Exercise 1.2, p. 1.
- `29. April - 5. Mai/Solution Sheet 1.pdf`, Exercise 1.2, single physical page (handwritten proof and geometric illustrations).
- `29. April - 5. Mai/Notes All you... math week 2`, single physical page, “Scalar Products and Projections #1”, cosine interpretation, subspace projection and Pythagoras–Fourier derivation through the line example.
- `13. Mai - 19. Mai/All you... math 4`, single physical page, final “Projections onto Subspaces” and “Projections on Convex Sets”.
- `20. Mai - 26. Mai/All you... math 5`, single physical page, “Question: Pythagoras–Fourier Formula” and “Projections onto Subspaces”, basis independence and projector representations.
