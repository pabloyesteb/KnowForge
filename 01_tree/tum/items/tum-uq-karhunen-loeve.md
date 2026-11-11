---
id: tum-uq-karhunen-loeve
source: tum-numuq
parent: uq-discretization
title: Karhunen–Loève representation and its convergence modes
type: theorem
caption: Diagonalizes random-field covariance to obtain uncorrelated coordinates and mean-square convergent spatial expansions.
---

# Karhunen–Loève representation and its convergence modes

For \(Z\in L^2(\Omega;L^2(D))\), Jensen gives \(\mu=EZ\in L^2(D)\), realizations belong to spatial \(L^2\) almost surely, and Cauchy–Schwarz gives \(\|c\|_{L^2(D\times D)}^2\le[\int_D\operatorname{Var}Z(x)dx]^2<\infty\). Thus its covariance integral operator is compact, self-adjoint and positive.

For its positive eigenpairs \((\nu_j,\phi_j)\), define
\[
\gamma_j=(Z-\mu,\phi_j)_{L^2(D)},\qquad \xi_j=\gamma_j/\sqrt{\nu_j}.
\]
Fubini and the eigen-equation imply \(E\gamma_j=0\) and \(E[\gamma_j\gamma_k]=\nu_k\delta_{jk}\). Hence the normalized coordinates have mean zero, variance one and are pairwise uncorrelated. The KL expansion is
\[
Z=\mu+\sum_j\sqrt{\nu_j}\phi_j\xi_j.
\]
It converges almost surely in spatial \(L^2\), and in \(L^2(\Omega;L^2(D))\). To see the latter, expand in a full orthonormal basis, use Parseval and bound partial-sum energies by \(\|Z-\mu\|_{L^2(D)}^2\); dominated convergence applies. Nullspace coefficients have zero second moment and vanish almost surely, so zero eigenvalues are omitted rather than divided by.

Under the compact continuous-covariance assumptions of Mercer, the spatial covariance expansion converges uniformly and
\[
\sup_x E|Z(x)-Z_J(x)|^2=\sup_x\sum_{j>J}\nu_j\phi_j(x)^2\to0.
\]
This is uniform **pointwise mean-square** convergence, not convergence of the expected spatial supremum or pathwise uniform convergence. For a jointly measurable Gaussian field in the course's bounded continuous-covariance setting, every finite set of integral coordinates is jointly Gaussian; diagonal covariance makes them independent standard normals after normalization. For non-Gaussian fields, uncorrelated KL coordinates need not be independent. Replacing them by independent Gaussians would generally change the field law, and Gaussian truncated KL sampling itself reproduces only the truncated covariance.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §4.3.1 and §4.3.3, Lemma 4.26, Theorems 4.27–4.28 with proofs and Remark 4.30, pp. 31 and 36–40.
- `Lecture Topics and Slides/Lecture 08 (16.05.24)`, physical pp. 4–16, including handwritten Jensen, covariance and convergence proofs; Gaussian integral-coordinate justification in `Problem Sheets/Solution Sheet 01 (update  complete).pdf`, Problems 2 and 4.
