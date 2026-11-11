---
id: tum-uq-orthogonal-polynomial-recurrence
source: tum-numuq
parent: uq-stochastic-galerkin
title: Orthonormal polynomial recurrence and Jacobi matrix spectra
type: theorem
caption: Relates weight-adapted polynomial bases to symmetric tridiagonal multiplication matrices and their roots.
---

# Orthonormal polynomial recurrence and Jacobi matrix spectra

For a positive weight with the moments/nondegeneracy needed to construct all degrees, orthogonal polynomials satisfy \(P_j=(a_jy+b_j)P_{j-1}-c_jP_{j-2}\), with \(P_{-1}=0\). After orthonormalization, symmetry of multiplication by \(y\) implies \(c_j/a_j=1/a_{j-1}\). Also \(b_j=-a_j(yP_{j-1},P_{j-1})_p\). On a symmetric interval with even weight, parity gives \(b_j=0\), and
\[
yP_{j-1}=a_j^{-1}P_j+a_{j-1}^{-1}P_{j-2}.
\]
The finite multiplication matrix is symmetric tridiagonal, with zero diagonal in this even-weight case and off-diagonals \(1/a_j\). The recurrence vector equation has a last-coordinate remainder proportional to \(P_N(y)\). Hence its eigenvalues are the roots of \(P_N\); these lie inside the weight support under the standard positive-weight hypotheses.

For the normalized uniform law on \([-\sqrt3,\sqrt3]\), define \(\widehat L_j(z)=\sqrt{2j+1}(2^jj!)^{-1}(d/dz)^j(z^2-1)^j\) and \(L_j(y)=\widehat L_j(y/\sqrt3)\). Substitution proves orthonormality with density \(1/(2\sqrt3)\); this interval corresponds to a mean-zero unit-variance uniform input. It differs from Sheet 5's uniform input on \([-1,1]\).

On \([-1,1]\) with density \(1/2\), normalized Legendre recurrence coefficients are \(c_n=n/\sqrt{(2n+1)(2n-1)}\), \(n\ge1\), with the \(c_0L_{-1}\) term defined as zero. The matrix \(T_{ij}=(yL_i,L_j)_p\) has adjacent entries \(c_{i+1}\). Gershgorin and decreasing \(c_n\) bound every eigenvalue by \(c_1+c_2=(1+2/\sqrt5)/\sqrt3<2/\sqrt3\) in absolute value (smaller matrices have no larger row sums). The sharper support bound is \([-1,1]\). “Classical” here includes the orthonormal scaling; the usual unscaled Legendre polynomials have different norms.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.5.3, equations (10.20)–(10.24), Example 10.20 and Remark 10.21, pp. 79–81.
- `Problem Sheets/Sheet 05 (02.07.2023)`, Problem 16; `Problem Sheets/Solution Sheet 05.pdf`, pp. 1–2 before Problem 17, tridiagonal derivation, Gershgorin and sharper-root remark.
- `Lecture Topics and Slides/Lecture 18 (11.07.24)`, physical pp. 1–3, handwritten recurrence derivation and standardized Legendre example.
