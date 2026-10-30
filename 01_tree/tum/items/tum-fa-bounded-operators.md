---
id: tum-fa-bounded-operators
source: tum-functional-analysis
parent: fa-normed-spaces
title: Bounded linear operators and operator norms
type: concept
---

# Bounded linear operators and operator norms

## Continuity and the operator space

For linear \(T:X\to Y\) between normed spaces, continuity everywhere, continuity at zero, a bound \(\|Tx\|\le C\|x\|\), and Lipschitz continuity are equivalent. To prove the nontrivial implication, failure of a bound yields \(x_n\) with \(\|Tx_n\|>n\|x_n\|\); normalization produces \(z_n\to0\) but \(\|Tz_n\|>1\).

On \(\mathcal L(X;Y)\),
\[
\|T\|=\sup_{x\ne0}\frac{\|Tx\|}{\|x\|}
=\sup_{\|x\|\le1}\|Tx\|,\qquad
\|ST\|\le\|S\|\|T\|.
\]
For nonzero \(X\) one may also take the supremum over the unit sphere. If \(Y\) is Banach, \(\mathcal L(X;Y)\) is Banach even when \(X\) is not: an operator-norm Cauchy sequence defines \(Tx=\lim T_nx\); its uniform Cauchy bound proves boundedness and norm convergence. In particular, \(X^*=\mathcal L(X;\mathbb K)\) is complete.

The initial ODE example becomes an operator equation:
\[
y'=f(t,y),\quad y(t_0)=y_0
\quad\Longleftrightarrow\quad
y(t)=y_0+\int_{t_0}^t f(s,y(s))\,ds.
\]
This motivates a map on continuous functions; the opening example alone supplies no contraction or existence theorem.

## Norm-sensitive examples

- \(Mf(t)=tf(t)\) is bounded on \(C([0,1])\) with the sup norm.
- \(Tf(t)=tf(1)\) is bounded in the sup norm, but not when both spaces use the \(L^1\) norm: \(f_n(t)=t^n\) has norm \(1/(n+1)\), while \(Tf_n(t)=t\) has fixed norm \(1/2\).
- On finitely supported sequences with the sup norm, \(Te_k=k\) defines an unbounded functional.
- Polynomials with coefficient norm \(\|\sum a_k t^k\|_{\mathrm{coef}}=\sum|a_k|\) are isometric to finite sequences with the \(\ell^1\) norm. Translation \(f(t)\mapsto f(t+1)\) is unbounded: \(t^m\) has norm 1 but its translate has coefficient norm \(2^m\). Integration \(f(t)\mapsto\int_0^t f(s)\,ds\) is bounded by 1. The worksheet's subscript \(p\) here names this coefficient norm, not a variable exponent.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, p. 2, Eqs. (1.1)–(1.4); pp. 6–12, Propositions 1.4, 1.7–1.10, Example 1.11(6)–(7) and Lemma 1.12.
- Sheet/solution pair 1: `Problem sheets/Problem Sheet 1.pdf`, `Solutions to problem sheets/Solutions Sheet 1.pdf`, T1.4.
- Sheet/solution pair 2: `Problem sheets/Problem Sheet 2.pdf`, `Solutions to problem sheets/Solutions Sheet 2.pdf`, T2.1, A2.3.
