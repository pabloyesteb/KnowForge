---
id: tum-fda-orthogonal-dyad-svd
source: tum-foundations-data-analysis
parent: fda-svd
title: Recovering an SVD from orthogonal rank-one expansions
type: method
caption: "Normalizes signed orthogonal dyads, handles common-direction differences and detects rank collapse from a repeated factor."
---

# Recovering an SVD from orthogonal rank-one expansions

Suppose
\[
A=\sum_i c_i a_i b_i^T,
\]
where the nonzero \(a_i\) are mutually orthogonal and the nonzero \(b_i\) are mutually orthogonal. The coefficients need not be positive and the vectors need not be normalized. For each nonzero term, set
\[
u_i=\operatorname{sign}(c_i)a_i/\|a_i\|_2,\quad
v_i=b_i/\|b_i\|_2,\quad
\sigma_i=|c_i|\|a_i\|_2\|b_i\|_2.
\]
Discard zero terms and sort the positive \(\sigma_i\) in decreasing order. The resulting expansion is an SVD. Sign changes preserve orthogonality; normalization transfers the missing lengths into the singular coefficients. A negative coefficient is not a negative singular value.

For two matrices sharing the same orthonormal left/right directions, subtract their coefficients first. Their difference has singular values equal to the absolute coefficient differences, after removing zeros and reordering. This shortcut requires shared directions: unrelated SVDs cannot generally be subtracted term by term. The review's common-direction example yields singular values 1 and \(1/2\), hence nuclear norm \(3/2\) and Frobenius norm \(\sqrt{1+1/4}\) for either sign of the difference.

A repeated factor changes the situation. If
\[
A=c_1u_1v^T+c_2u_2v^T=(c_1u_1+c_2u_2)v^T,
\]
with orthonormal \(u_1,u_2\), unit \(v\), and coefficients not both zero, then \(A\) has rank one, not two. Normalize the combined left vector to get its only positive singular value \(\sqrt{c_1^2+c_2^2}\). If both coefficients vanish the rank is zero. Counting dyads only determines rank when the required independence/orthogonality is present on both sides.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `27. Mai - 2. Juni/All you... math 6`, single physical page, “SVD of Differences of Matrices”, “Tricks for Decomposed Matrices”, signed/common-direction examples, normalization and repeated-factor examples.
