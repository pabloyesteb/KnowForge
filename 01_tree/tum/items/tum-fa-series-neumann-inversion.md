---
id: tum-fa-series-neumann-inversion
source: tum-functional-analysis
parent: fa-normed-spaces
title: Banach-space series and Neumann inversion
type: method
caption: "Uses absolutely convergent Banach-space series to invert small operator perturbations and solve a concrete integral equation."
---

# Banach-space series and Neumann inversion

## Series and the role of completeness

A series \(\sum_{k=1}^\infty x_k\) converges when its partial sums converge in norm. Absolute convergence means \(\sum_k\|x_k\|<\infty\). In a Banach space, absolute convergence implies convergence and
\[
\left\|\sum_kx_k\right\|\le\sum_k\|x_k\|.
\]
Indeed \(\|\sum_{k=m+1}^nx_k\|\le\sum_{k=m+1}^n\|x_k\|\) makes the partial sums Cauchy. Every permutation has the same limit: retain all of a fixed finite initial block, then bound the remaining terms by the arbitrarily small absolute tail. Addition and scalar multiplication of convergent series follow from continuity.

Completeness is essential to this implication; the Cauchy estimate alone need not produce a limit inside an incomplete space.

## Inverting a small bounded perturbation

Let \(X\) be Banach and \(A\in\mathcal L(X;X)\) satisfy \(\|A\|<1\). Then
\[
(I-A)^{-1}=\sum_{k=0}^{\infty}A^k.
\]
Submultiplicativity gives \(\|A^k\|\le\|A\|^k\). Completeness of the operator space and the series result yield a bounded operator \(B\). For partial sums \(B_N=\sum_{k=0}^NA^k\),
\[
(I-A)B_N=B_N(I-A)=I-A^{N+1}.
\]
Pass to the operator-norm limit on both sides; \(\|A^{N+1}\|\to0\) proves both inverse identities. Thus one may solve \((I-A)x=b\) by partial sums of \(\sum A^kb\). The strict norm bound is the stated sufficient condition, not a necessary criterion for invertibility.

## Integral equation with a convergent power series despite norm one

On \(C([0,1])\) with the sup norm, set
\[
(Tx)(t)=2t\lambda(x),\qquad \lambda(x)=\int_0^1s x(s)\,ds.
\]
Here \(\|T\|=1\), so the strict-norm criterion above cannot be applied directly. Nevertheless
\[
T^nx(t)=2(2/3)^{n-1}t\lambda(x),\qquad
\|T^n\|\le(2/3)^{n-1}\quad(n\ge1).
\]
Thus the operator series converges absolutely, and the same telescoping identities prove it is \((I-T)^{-1}\). Since \(\lambda(\sin(\pi t))=1/\pi\), the solution of
\(x(t)-\int_0^1 2stx(s)\,ds=\sin(\pi t)\) is
\[
x(t)=\sin(\pi t)+6t/\pi.
\]
This example illustrates the sufficient nature of \(\|T\|<1\); summability of operator powers also suffices.

## Stability of bounded invertibility

If \(T:X\to Y\) is a bounded isomorphism between Banach spaces and
\(\|\widetilde T-T\|<1/\|T^{-1}\|\), then
\[
\widetilde T=T\bigl(I-T^{-1}(T-\widetilde T)\bigr)
\]
is again a bounded isomorphism. The operator inside the parentheses is invertible by the Neumann criterion. Thus boundedly invertible maps form an operator-norm open set; the admissible perturbation size depends on the inverse norm.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Definition 1.21 and Proposition 1.22, pp. 18–19; Proposition 1.10 and Lemma 1.12 for the operator-space ingredients.
- `Problem sheets/Problem Sheet 3.pdf`, T3.3; `Solutions to problem sheets/Solutions Sheet 3.pdf`, T3.3, physical pp. 1–2.
- `Problem sheets/Problem Sheet 4.pdf` and `Solutions to problem sheets/Solutions Sheet 4.pdf`, T4.1.
- `Materials/Lecture notes.pdf`, Proposition 11.4 and Corollary 11.5, Eqs. (11.6)–(11.8), p. 78.
