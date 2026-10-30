---
id: tum-fa-density-separability
source: tum-functional-analysis
parent: fa-normed-spaces
title: Density, separability and coordinate expansions
type: concept
---

# Density, separability and coordinate expansions

## Density and countable approximation

A subset \(A\) is dense in \(X\) when \(\overline A=X\), equivalently every nonempty open set meets \(A\). A metric space is separable when it has a finite or countably infinite dense subset. Density is transitive through a dense intermediate subspace.

If \(\overline{\operatorname{span}\{x_n:n\in\mathbb N\}}=X\), rational finite linear combinations of \(x_n\) form a countable dense set (use \(\mathbb Q+i\mathbb Q\) over \(\mathbb C\)). Approximate a vector by a finite linear combination, then approximate its finitely many coefficients; the triangle inequality bounds the error. The worksheet supplies this proof of Proposition 1.17.

By Weierstrass approximation and coefficient approximation, polynomials with rational real/imaginary coefficients are dense in \(C([a,b];\mathbb K)\) with the sup norm.

## Finite sequences and the norm-dependent closure

Write \(c_e\) for finitely supported sequences and \(e_k\) for coordinate vectors. For \(x\in\ell^p\), \(1\le p<\infty\), truncations \(P_Nx=\sum_{k=1}^Nx_ke_k\) satisfy
\[
\|x-P_Nx\|_p^p=\sum_{k>N}|x_k|^p\to0.
\]
Thus \(\overline{c_e}^{\,\ell^p}=\ell^p\) and these spaces are separable. In the sup norm,
\[
\overline{c_e}^{\,\ell^\infty}=c_0,\qquad
\|x-P_Nx\|_\infty=\sup_{k>N}|x_k|.
\]
Since \(c_0\) is closed, both inclusions follow. Consequently \(\sum_kx_ke_k\) converges in \(\ell^\infty\) **exactly for \(x\in c_0\)**, not for every bounded sequence. Outside \(c_0\), arbitrarily distant partial sums differ by at least a fixed positive amount.

The characteristic sequences of all subsets of \(\mathbb N\) form an uncountable family at pairwise distance 1. Their disjoint open balls of radius \(1/2\) exclude any countable dense set in \(\ell^\infty\). This is stronger than failure of density of \(c_e\).

The notes also state separability of \(L^p(D)\), \(1\le p<\infty\), for open \(D\subset\mathbb R^n\), and nonseparability of \(L^\infty(D)\) for nonempty such \(D\). For bounded domains they invoke density of continuous functions and polynomial approximation. For unbounded domains they use the **closure** of the union of bounded-domain spaces, interpreted by zero extension to \(D\): bounded-support approximations, not a claim that every function has bounded support. The unbounded-domain density argument is sketched rather than proved in detail.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, pp. 4–5 (finite sequences), pp. 14–15, Definition 1.15 and Propositions 1.16–1.18.
- `Problem sheets/Problem Sheet 1.pdf` and `Solutions to problem sheets/Solutions Sheet 1.pdf`, T1.2.
- `Problem sheets/Problem Sheet 3.pdf` and `Solutions to problem sheets/Solutions Sheet 3.pdf`, T3.1–T3.2 and A3.1(a).
