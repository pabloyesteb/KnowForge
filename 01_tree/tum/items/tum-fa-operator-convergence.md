---
id: tum-fa-operator-convergence
source: tum-functional-analysis
parent: fa-normed-spaces
title: Pointwise versus operator-norm convergence
type: concept
---

# Pointwise versus operator-norm convergence

## Two different limits

For bounded linear maps \(T_n:X\to Y\), operator-norm convergence to \(T\) implies \(T_nx\to Tx\) for every fixed \(x\), because
\[
\|(T_n-T)x\|\le\|T_n-T\|\|x\|.
\]
The converse fails: pointwise convergence tests each vector separately, whereas the operator norm takes a supremum over the unit ball.

## Diagonal and tail operators on \(\ell^2\)

Using the worksheet's zero-based coordinates, define
\[
(A_nx)_k=\frac{x_k}{n(k+1)},\qquad
(B_nx)_k=\begin{cases}0&k<n,\\x_k&k\ge n.\end{cases}
\]
Then \(\|A_nx\|_2\le\|x\|_2/n\), hence \(\|A_n\|\le1/n\) and convergence is in operator norm. For \(B_n\),
\[
\|B_nx\|_2^2=\sum_{k=n}^{\infty}|x_k|^2\longrightarrow0
\]
for each \(x\in\ell^2\), but a unit coordinate vector in the retained tail gives \(\|B_n\|=1\). For \(n<m\), choosing a coordinate in \(n\le k<m\) gives \(\|B_n-B_m\|=1\): the sequence is not even norm-Cauchy.

These examples separate convergence of outputs on fixed inputs from a uniform error bound on all unit inputs.

## When the pointwise limit is bounded

Let \(X,Y\) be Banach spaces and suppose \(T_nx\) converges in \(Y\) for each \(x\in X\). Its limit \(Tx\) is linear. Convergence gives \(\sup_n\|T_nx\|<\infty\) for each \(x\); the uniform boundedness principle then yields \(C=\sup_n\|T_n\|<\infty\). Passing to the limit gives \(\|Tx\|\le C\|x\|\). This does not give operator-norm convergence, as the tail projections above show.

Completeness of the domain matters: on \(c_e\) with the sup norm, \(F_nx=nx_n\) is continuous with norm \(n\), but for each finite sequence \(x\), \(F_nx=0\) eventually and \(\sup_n|F_nx|<\infty\). Pointwise boundedness on this incomplete domain gives no uniform operator bound.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Problem sheets/Problem Sheet 2.pdf`, T2.2, physical p. 1.
- `Solutions to problem sheets/Solutions Sheet 2.pdf`, T2.2, physical p. 1.
- `Materials/Lecture notes.pdf`, Proposition 1.10, pp. 9–10, for the operator norm and completeness distinction.
- `Problem sheets/Problem Sheet 5.pdf` and `Solutions to problem sheets/Solutions Sheet 5.pdf`, T5.2–T5.3.
