---
id: tum-fa-convex-projection
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Projection onto closed convex sets in Hilbert spaces
type: theorem
---

# Projection onto closed convex sets in Hilbert spaces

## Existence and uniqueness

Let \(H\) be Hilbert and \(K\subset H\) nonempty, closed and convex. For every \(x\in H\) there is a unique \(P_Kx\in K\) satisfying
\[
\|x-P_Kx\|=\inf_{z\in K}\|x-z\|=:d.
\]
For a minimizing sequence \(y_n\in K\), the parallelogram identity and convexity give
\[
\|y_n-y_m\|^2
\le2\|x-y_n\|^2+2\|x-y_m\|^2-4d^2\to0.
\]
Completeness supplies a limit, closedness keeps it in \(K\), and continuity of the norm proves attainment. Applying the same estimate to two minimizers proves uniqueness.

## Variational characterization and stability

For \(y\in K\),
\[
y=P_Kx
\quad\Longleftrightarrow\quad
\operatorname{Re}\langle x-y,z-y\rangle\le0
\quad\text{for every }z\in K.
\]
The forward implication follows by testing the segment \(y+t(z-y)\) and letting \(t\downarrow0\); the reverse follows by expanding \(\|x-z\|^2\). Applying this inequality to \(P_Kx\) and \(P_K\tilde x\), then adding and using Cauchy–Schwarz, yields
\[
\|P_Kx-P_K\tilde x\|\le\|x-\tilde x\|.
\]
Thus the best approximation is nonexpansive. It is not generally a linear map; linearity holds for closed subspaces.

## Closedness is substantive

The finite sequences \(c_e\) are dense but not closed in \(\ell^2\). For \(x\in\ell^2\setminus c_e\), the distance to \(c_e\) is zero but no finite sequence attains it. Completeness of the ambient space does not compensate for a nonclosed feasible set.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Propositions 2.4–2.5 and Corollary 2.6, pp. 22–23.
- `Problem sheets/Problem Sheet 4.pdf` and `Solutions to problem sheets/Solutions Sheet 4.pdf`, T4.3 and A4.2.
