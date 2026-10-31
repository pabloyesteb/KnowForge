---
id: tum-fda-trace-spectral-invariants
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Cyclic trace and eigenvalue sums with multiplicity
type: theorem
caption: "Derives cyclic trace identities and explains why eigenvalue sums require algebraic multiplicities and remain invariant under basis changes."
---

# Cyclic trace and eigenvalue sums with multiplicity

For compatible rectangular matrices, \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\). Indeed both traces sum the same products \(a_{ij}b_{ji}\) over all indices. This implies cyclic invariance for compatible triple products,
\[
\operatorname{tr}(ABC)=\operatorname{tr}(BCA),
\]
and invariance under similarity, in particular unitary change of basis. Cyclic permutation does not assert arbitrary permutation of matrix factors.

If a square matrix is diagonalizable, \(A=PDP^{-1}\), then cyclicity gives
\[
\operatorname{tr}(A)=\operatorname{tr}(D)=\sum_j\lambda_j.
\]
Distinct eigenvalues are sufficient for the diagonalization argument, but the trace formula also holds with repeated eigenvalues counted by **algebraic multiplicity**. The booklet identifies Jordan decomposition as the extension beyond the distinct-eigenvalue case without developing that theory. Summing only distinct numerical eigenvalues would generally lose the trace.

Thus trace gives a basis-independent aggregate spectral quantity, while not determining individual eigenvalues or eigenvectors.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 1.1.6(a), p. 5; further exercise “Trace”, p. 6; solution, p. 14.
- `22. April - 28. April/Problem Set 1.pdf`, Exercise 1.3(a), p. 2.
