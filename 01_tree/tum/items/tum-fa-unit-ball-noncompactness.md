---
id: tum-fa-unit-ball-noncompactness
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Distance from subspaces and noncompact unit balls
type: theorem
caption: "Constructs unit vectors separated from proper closed subspaces and proves that compact unit balls characterize finite dimension."
---

# Distance from subspaces and noncompact unit balls

## Approximate separation without Hilbert geometry

Let \(X\) be normed and \(U\subsetneq X\) a closed linear subspace. There are unit vectors \(x_n\) with \(\operatorname{dist}(x_n,U)\to1\).

Choose \(a\notin U\), set \(d=\operatorname{dist}(a,U)>0\), and choose \(u_n\in U\) with \(\|a-u_n\|\to d\). For \(x_n=(a-u_n)/\|a-u_n\|\),
\[
1\ge\operatorname{dist}(x_n,U)\ge d/\|a-u_n\|\to1.
\]
The lower bound follows by scaling a competitor in \(U\). In a Hilbert space an exactly orthogonal unit vector attains distance 1, but that exact conclusion need not hold in a general normed space.

## Compactness characterizes finite dimension

In infinite dimension, construct unit vectors recursively, choosing \(x_{n+1}\) at distance at least \(1/2\) from
\(U_n=\operatorname{span}\{x_1,\ldots,x_n\}\).
These finite-dimensional subspaces are closed and proper, so the preceding result applies. The resulting sequence has pairwise distances at least \(1/2\), hence no convergent subsequence. The closed unit ball is therefore not compact, even if \(X\) is Banach.

Conversely finite-dimensional norm equivalence and finite-dimensional compactness make the closed unit ball compact. Thus a normed space has compact closed unit ball exactly when it is finite-dimensional.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Lemma 2.13 and Corollary 2.14, pp. 26–27.
