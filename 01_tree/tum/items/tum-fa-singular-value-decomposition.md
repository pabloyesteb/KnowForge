---
id: tum-fa-singular-value-decomposition
source: tum-functional-analysis
parent: fa-spectral-theory
title: Compact-operator SVD, optimal rank approximation and perturbation bounds
type: theorem
caption: "Constructs compact-operator singular systems and derives optimal low-rank errors and perturbation bounds for singular values."
---

# Compact-operator SVD, optimal rank approximation and perturbation bounds

## Construction without normality

For compact \(T\) on Hilbert space, \(T^*T\) is compact, positive and self-adjoint. Let \(T^*Te_k=\nu_ke_k\), \(\nu_k>0\), on the orthonormal basis of the kernel's orthogonal complement. Define
\[
s_k=\sqrt{\nu_k},\qquad f_k=s_k^{-1}Te_k.
\]
Since \(\ker(T^*T)=\ker T\) by \(\langle T^*Tx,x\rangle=\|Tx\|^2\), expanding \(x\) in the \(e_k\) and kernel basis gives
\[
Tx=\sum_ks_k\langle x,e_k\rangle f_k.
\]
The output vectors are orthonormal:
\(\langle f_k,f_m\rangle=(s_ks_m)^{-1}\langle T^*Te_k,e_m\rangle=\delta_{km}\).
Unlike a normal spectral expansion, the input and output systems need not coincide. The construction extends to compact maps between distinct Hilbert spaces. For a normal compact map, its singular values are the magnitudes of its eigenvalues, with multiplicity.

## Truncation and optimality

Order singular values decreasingly with multiplicity, padding by zeros when appropriate. For nonzero \(T\), \(\|T\|=s_1\). The truncation
\[
T_nx=\sum_{k=1}^ns_k\langle x,e_k\rangle f_k
\]
has rank at most \(n\), exactly \(n\) if \(s_n>0\), and
\[
\|T-T_n\|=s_{n+1}\longrightarrow0.
\]
Thus every compact Hilbert-space operator is an operator-norm limit of finite-rank maps; this does not extend to all Banach spaces.

The stronger best-approximation statement is
\[
s_n(T)=\inf_{\operatorname{rank}Q<n}\|T-Q\|.
\]
The notes state this optimality theorem without proof; it identifies the truncation error with the best achievable operator-norm error at the corresponding rank.

## Stable singular values

For compact \(T,S\), rank subadditivity and best approximation give
\[
s_{n+m-1}(T+S)\le s_n(T)+s_m(S).
\]
Indeed rank-\(<n\) and rank-\(<m\) approximants sum to rank \(<n+m-1\), and their approximation errors add. Taking \(m=1\) for \(S=\widetilde T-T\), then interchanging \(T,\widetilde T\), gives
\[
|s_n(T)-s_n(\widetilde T)|\le\|T-\widetilde T\|.
\]
Singular values therefore provide stable operator-norm-sensitive descriptors and controlled low-rank approximations even without normality. The source contrasts this with the lack of such a general eigenvalue perturbation bound; it does not report a numerical implementation.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Lecture notes.pdf` (WS 2017/18), Eqs. (13.21)–(13.30), Proposition 13.9, Corollary 13.10, Proposition 13.11 and Corollaries 13.12–13.13, pp. 92–94.
