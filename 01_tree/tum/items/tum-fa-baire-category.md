---
id: tum-fa-baire-category
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Baire category and the obstruction to countable-dimensional Banach spaces
type: theorem
caption: "Uses dense-open intersections in complete metric spaces to rule out countably infinite algebraic bases for Banach spaces."
---

# Baire category and the obstruction to countable-dimensional Banach spaces

## Dense-open intersection theorem

Let \((X,d)\) be a complete metric space and \(U_n\subset X\) countably many open dense sets. Then \(\bigcap_{n=1}^\infty U_n\) is dense in \(X\). Density means intersection with every nonempty open \(V\), not equality with \(X\).

**Nested-ball proof:** choose a closed ball \(K(x_1,r_1)\subset U_1\cap V\). Inductively choose positive \(r_n<1/n\) with
\[
K(x_n,r_n)\subset U_n\cap B(x_{n-1},r_{n-1}).
\]
Openness and density allow each choice. All later centers lie in an arbitrarily small earlier ball, so they are Cauchy. Completeness gives a limit \(x\); closedness of each nested ball places \(x\) in every \(U_n\) and in \(V\).

## Application to finite sequences and polynomials

A set is nowhere dense when the interior of its closure is empty, and meagre (first category) when it is a countable union of nowhere dense sets. In a nonempty complete metric space, the complement of a countable union of closed nowhere dense sets is dense. Equivalently, any countable closed cover has a member with nonempty interior. The notes mention continuous nowhere-differentiable functions as a dense-set application, without providing that proof.

Suppose an infinite-dimensional normed space is the union of an increasing sequence of finite-dimensional subspaces \(A_n\). Each \(A_n\) is closed and proper, hence has empty interior. Its complement \(U_n\) is open dense, but
\[
\bigcap_nU_n=X\setminus\bigcup_nA_n=\varnothing.
\]
Baire therefore rules out completeness.

In particular, no norm can turn the space \(c_e\) of finitely supported sequences into a Banach space: take \(A_n=\operatorname{span}\{e_1,\ldots,e_n\}\). The same obstruction applies to the algebraic polynomial space \(\mathbb R[t]\). This is stronger than failure of completeness for one particular norm, and does not apply to uncountable-dimensional Banach spaces merely because they are separable.

## Category and measure describe different notions of size

Enumerate \(\mathbb Q=\{a_m:m\ge1\}\). For each \(n\ge1\), surround \(a_m\) by an open interval \(I_{mn}\) of length \(2^{-(m+n)}\). Then \(B_n=\bigcup_m I_{mn}\) is open dense and has Lebesgue measure at most \(2^{-n}\). Therefore
\[
B=\bigcap_n B_n,\qquad A=\mathbb R\setminus B
\]
partition \(\mathbb R\), with \(B\) null and \(A=\bigcup_n(\mathbb R\setminus B_n)\) of first category: each complement is closed with empty interior. A meagre set can thus have full Lebesgue measure, while a dense countable intersection of open sets can be null.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Proposition 3.1, Definition 3.2 and Corollaries 3.3–3.4, pp. 32–33.
- `Problem sheets/Problem Sheet 3.pdf`, A3.1–A3.2, physical p. 2; `Solutions to problem sheets/Solutions Sheet 3.pdf`, A3.1–A3.2, physical pp. 2–3.
- `Problem sheets/Problem Sheet 2.pdf` and `Solutions to problem sheets/Solutions Sheet 2.pdf`, A2.1, for finite-dimensional closedness and empty interior.
- `Problem sheets/Problem Sheet 5.pdf` and `Solutions to problem sheets/Solutions Sheet 5.pdf`, A5.3.
