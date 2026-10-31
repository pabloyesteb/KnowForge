---
id: tum-fda-svd-ellipsoid-geometry
source: tum-foundations-data-analysis
parent: fda-svd
title: Singular axes versus eigenvector directions
type: concept
caption: "Interprets singular values as ellipsoid semiaxes and explains why nonorthogonal eigenvectors do not determine Euclidean amplification."
---

# Singular axes versus eigenvector directions

For \(A=U\Sigma V^T\), a unit input is first expressed in right singular coordinates, stretched by the singular values, and mapped into the left singular directions. The image of a Euclidean unit ball is an ellipsoid in the range of \(A\); its positive semiaxes have lengths \(\sigma_i\) along \(u_i\), with input directions \(v_i\) satisfying \(Av_i=\sigma_i u_i\). In the invertible square case, the unit sphere maps to its boundary. The longest semiaxis is the spectral norm, while the Frobenius norm combines all squared semiaxis lengths.

Eigenvectors of a square diagonalizable matrix instead identify invariant lines: \(Av=\lambda v\). These lines need not be orthogonal, eigenvalues may be negative, and their magnitudes need not equal singular values. A symmetric positive semidefinite matrix is a special case where orthonormal eigenvectors also provide matching singular directions.

The review constructs
\[
A=Q\operatorname{diag}(2,-4)Q^{-1}
=\begin{pmatrix}-1&-12\\-3/4&-1\end{pmatrix},\qquad
Q=\begin{pmatrix}1&1\\-1/4&1/4\end{pmatrix}.
\]
Its eigenvectors are nearly aligned rather than orthogonal. The review gives approximate singular values \(12.09\) and \(0.66\), markedly different from the eigenvalue magnitudes 2 and 4. Plotting \(A(\cos t,\sin t)^T\) reveals the ellipse axes directly. The example shows why a general eigenvalue decomposition cannot substitute for Euclidean singular geometry.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `13. Mai - 19. Mai/All you... math 4`, single physical page, “Intuition for Eigenvectors/values vs Singular Vectors/values”, nonorthogonal diagonalization example, circle-to-ellipse plot and matrix norms.
