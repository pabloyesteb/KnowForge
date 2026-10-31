---
id: tum-fa-compact-spectral-decomposition
source: tum-functional-analysis
parent: fa-spectral-theory
title: Spectral decomposition and finite-rank approximation of compact normal maps
type: theorem
---

# Spectral decomposition and finite-rank approximation of compact normal maps

Let \(T\) be compact and normal on a complex separable Hilbert space \(H\). For \(U_\lambda=\ker(\lambda I-T)\), choose an orthonormal basis \(E_\lambda\); for nonzero eigenvalues each \(U_\lambda\) is finite-dimensional, and their union is at most countable. Let \(\{e_j\}\) enumerate those nonzero-eigenvalue basis vectors, with repeated \(\lambda_j\) according to multiplicity, and let \(E_0\) be a basis of \(\ker T\).

## Orthogonal representation

Then \(E_0\cup\{e_j\}\) is an orthonormal basis, and
\[
H=\ker T\oplus\overline{\operatorname{span}}\{e_j\},\qquad
\overline{\operatorname{ran}T}=\overline{\operatorname{span}}\{e_j\},
\]
\[
Tx=\sum_{\lambda\ne0}\lambda P_\lambda x
=\sum_j\lambda_j\langle x,e_j\rangle e_j,
\]
where \(P_\lambda\) is orthogonal projection onto the eigenspace and the sums converge in norm. The **range closure** is necessary; compact infinite-rank maps need not have closed range.

For completeness, the orthogonal complement \(V\) of all the eigenvectors is invariant under \(T\) and \(T^*\). If the compact normal restriction \(T|_V\) were nonzero, its spectral radius equals its positive norm, giving a nonzero eigenvector in \(V\), a contradiction. Thus \(T|_V=0\); then \(V\subset\ker T\) and orthogonality forces \(V=0\).

For nonzero \(T\), \(\|T\|=\max_j|\lambda_j|\); the zero operator has norm zero without requiring a nonzero-eigenvalue maximum. Separability can be removed: the nonzero-eigenvalue part remains at most countable, while the kernel may have an uncountable orthonormal basis.

## Operator-norm approximation

Define \(T_nx=\sum_{j=1}^n\lambda_j\langle x,e_j\rangle e_j\). Then
\[
\|T-T_n\|=\sup_{j>n}|\lambda_j|\longrightarrow0,
\]
with error zero after the last term for finite rank. The upper bound uses orthogonality; testing omitted unit eigenvectors gives the lower bound. Compactness leaves only finitely many eigenvalues above any fixed magnitude, including their finite multiplicities, so the tail tends to zero. The enumeration is a mathematical representation, not the chronology of source material.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Lecture notes.pdf` (WS 2017/18), Eqs. (13.11)–(13.20), Propositions 13.7–13.8 and proofs, pp. 90–92.
