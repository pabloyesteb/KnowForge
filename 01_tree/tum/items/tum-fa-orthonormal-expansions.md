---
id: tum-fa-orthonormal-expansions
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Orthonormal bases, Fourier expansions and Hilbert coordinates
type: theorem
---

# Orthonormal bases, Fourier expansions and Hilbert coordinates

## Systems, bases and finite projection

An orthonormal system \(S\) consists of unit vectors orthogonal in pairs. An orthonormal basis is a maximal such system, not an algebraic basis of finite expansions. Every orthonormal system in a Hilbert space extends to a basis: partially order its orthonormal extensions by inclusion; unions of chains are upper bounds, so Zorn's lemma gives a maximal extension.

In a separable infinite-dimensional Hilbert space, every orthonormal basis is countably infinite. Distinct orthonormal vectors are at distance \(\sqrt2\), excluding an uncountable system in a separable space; a finite system can be extended using the orthogonal component of a vector outside its span.

For \(U=\operatorname{span}\{e_1,\ldots,e_n\}\),
\[
P_Ux=\sum_{k=1}^n\langle x,e_k\rangle e_k,\qquad
\sum_{k=1}^n|\langle x,e_k\rangle|^2\le\|x\|^2.
\]
Orthogonality characterizes the projection; Pythagoras gives Bessel's inequality. Even for an uncountable system, each vector has at most countably many nonzero coefficients: for each positive threshold only finitely many can exceed it, by Bessel.

## Completeness and coordinates

For a countable orthonormal system in a separable infinite-dimensional Hilbert space, the following are equivalent:
- maximal orthonormality;
- \(S^\perp=\{0\}\);
- \(\overline{\operatorname{span}S}=H\);
- \(x=\sum_{k=1}^\infty\langle x,e_k\rangle e_k\) in norm for every \(x\);
- Parseval: \(\|x\|^2=\sum_{k=1}^\infty|\langle x,e_k\rangle|^2\).

Double orthogonal complements connect totality and density. Projections onto the growing finite spans approximate any vector in the dense span's closure; Pythagoras then yields Parseval. If maximality fails, a unit vector orthogonal to all of \(S\) contradicts Parseval.

The coefficient map \(x\mapsto(\langle x,e_k\rangle)_k\) is a linear isometric isomorphism \(H\cong\ell^2\). Surjectivity follows by extending the isometric finite-series synthesis map from \(c_e\) to \(\ell^2\). Such series are order-independent but need not converge absolutely: \(x_k=1/k\) in \(\ell^2\) gives summable squared coefficients but divergent \(\sum_k\|x_ke_k\|_2\).

## Fourier application and non-complete systems

In \(L^2((-\pi,\pi);\mathbb C)\), the established orthonormal basis
\(e_k(t)=(2\pi)^{-1/2}e^{ikt}\), \(k\in\mathbb Z\), gives
\[
f=\sum_{k\in\mathbb Z}c_ke_k,\qquad
c_k=(2\pi)^{-1/2}\int_{-\pi}^{\pi}f(t)e^{-ikt}\,dt.
\]
Convergence here is in \(L^2\), not a claim of pointwise or uniform convergence. Bessel for the normalized sine and cosine systems also proves the \(L^2\) Riemann–Lebesgue conclusion: both integrals against \(\sin(nt)\) and \(\cos(nt)\) tend to zero.

On the unit disk with area measure,
\(P_n(z)=\sqrt{(n+1)/\pi}\,z^n\) is an orthonormal system by polar-coordinate integration, but not a basis of all \(L^2(D)\): the nonzero function \(\overline z\) is orthogonal to every \(P_n\). Orthonormality alone does not establish completeness.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Definition 2.15, Propositions 2.16–2.17, Lemma 2.18, Corollary 2.19 and Propositions 2.20–2.21, pp. 27–31.
- `Problem sheets/Problem Sheet 5.pdf` and `Solutions to problem sheets/Solutions Sheet 5.pdf`, A5.1–A5.2.
