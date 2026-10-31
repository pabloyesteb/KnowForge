---
id: tum-fda-symmetric-positive-matrices
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Orthogonal diagonalization and positive semidefinite Gram matrices
type: theorem
caption: "Characterizes symmetric positivity through eigenvalues and derives nonnegativity of Gram-matrix quadratic forms."
---

# Orthogonal diagonalization and positive semidefinite Gram matrices

An eigenvector \(v\ne0\) satisfies \(Av=\lambda v\). If a square matrix has an eigenvector basis, collecting those vectors in \(Q\) gives \(Q^{-1}AQ=\operatorname{diag}(\lambda_i)\); such a basis need not exist for a general matrix.

A real symmetric matrix does admit an orthonormal eigenvector basis and real eigenvalues. Thus \(Q^{-1}=Q^T\) and
\[
A=Q\operatorname{diag}(\lambda_i)Q^T.
\]
For symmetric \(A\), positive semidefiniteness means \(x^TAx\ge0\) for all \(x\); positive definiteness requires strict positivity for every nonzero \(x\). In orthogonal coordinates the quadratic form is \(\sum_i\lambda_i (Q^Tx)_i^2\), so these properties correspond respectively to all eigenvalues being nonnegative or positive.

For a rectangular real matrix \(B\), \(BB^T\) is symmetric and positive semidefinite because
\[
(BB^T)^T=BB^T,\qquad x^TBB^Tx=\|B^Tx\|_2^2\ge0.
\]
Positive semidefiniteness alone does not imply invertibility: a nonzero vector killed by \(B^T\) gives zero quadratic form. This construction connects a general linear map with the symmetric spectral structure needed for singular values.

In particular, \(A^TA\) is positive definite exactly when \(A\) has independent columns, because \(x^TA^TAx=\|Ax\|^2\) vanishes precisely on its kernel. A wide full-row-rank matrix still gives a singular \(A^TA\): full rank means \(\operatorname{rank}A=\min(m,n)\), not automatically \(n\). Positive definiteness implies invertibility, but invertibility and symmetry alone do not imply positivity, as \(\operatorname{diag}(1,-1)\) shows. For symmetric positive semidefinite \(A\), its own singular values equal its nonnegative eigenvalues; the eigenvalues of \(A^TA\) are their squares.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `22. April - 28. April/All you ... math 1`, single physical page, “Eigenvectors and Eigenvalues”, “Particular Case (Symmetric Matrices)” and “Symmetric and Positive (Semi-)Definite”.
- `6. Mai - 12. Mai/All you ... math 3`, single physical page, “Diagonalization of Symmetric Matrices”, full-rank and positivity discussion and SVD motivation.
