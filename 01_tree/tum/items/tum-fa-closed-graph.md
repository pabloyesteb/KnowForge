---
id: tum-fa-closed-graph
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Closed graph theorem and differentiation on an incomplete domain
type: theorem
caption: "Derives boundedness from a closed graph on Banach domains and contrasts it with differentiation on an incomplete domain."
---

# Closed graph theorem and differentiation on an incomplete domain

## Theorem and proof mechanism

Let \(X,Y\) be Banach and \(T:X\to Y\) an everywhere-defined linear map. Then \(T\) is bounded exactly when
\(\operatorname{graph}T=\{(x,Tx):x\in X\}\) is closed in the product norm.

Boundedness implies that \(x_n\to x\), \(Tx_n\to y\) forces \(y=Tx\). Conversely a closed linear graph is a Banach subspace of \(X\times Y\). Its coordinate projection onto \(X\) is a bounded linear bijection; the bounded inverse theorem gives a bounded inverse \(Q:x\mapsto(x,Tx)\). Composition with the \(Y\)-projection proves \(T\) bounded.

This replaces a direct estimate with a uniqueness-of-limit test: it is enough to identify \(y\) whenever both \(x_n\) and \(Tx_n\) already converge. It does not assert boundedness for operators defined only on arbitrary noncomplete domains.

## Why the hypotheses matter

Let \(D:C^1([-1,1])\to C([-1,1])\), \(Df=f'\), with both spaces using the sup norm. Its graph is closed: uniform limits \(f_n\to f\), \(f_n'\to g\) satisfy
\(f(t)-f(0)=\int_0^t g(s)\,ds\), so \(f'=g\). But \(f_n(t)=t^n\) has norm 1 and \(\|Df_n\|_\infty=n\); \(D\) is unbounded.

There is no contradiction: \(C^1([-1,1])\) with only the sup norm is incomplete. The functions \(\sqrt{t^2+1/n}\) converge uniformly to \(|t|\), which is not \(C^1\).

## Everywhere-defined formal adjoints: Hellinger–Toeplitz

If linear maps \(A,B:H\to H\) on an entire Hilbert space satisfy
\(\langle Ax,z\rangle=\langle x,Bz\rangle\) for all \(x,z\), both are bounded. Indeed, \(x_n\to x\), \(Ax_n\to y\) gives
\[
\langle y,z\rangle=\lim_n\langle x_n,Bz\rangle
=\langle x,Bz\rangle=\langle Ax,z\rangle.
\]
Therefore \(y=Ax\), its graph is closed, and the closed graph theorem applies. The argument for \(B\) is symmetric. The full-domain hypothesis is crucial; this is not a boundedness result for arbitrary densely defined operators.

The same graph argument proves that an everywhere-defined linear map \(T:X\to Y\) between Banach spaces is bounded if it preserves weakly null sequences. For \(x_n\to x\) and \(Tx_n\to y\), the hypothesis gives \(T(x_n-x)\rightharpoonup0\), while strong convergence gives \(T(x_n-x)\rightharpoonup y-Tx\). Uniqueness of weak limits implies \(y=Tx\).

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Proposition 3.10, p. 36.
- E7/S7, A7.1.
- `Problem sheets/Problem Sheet 14.pdf` and `Solutions to problem sheets/Solutions Sheet 14.pdf`, T14.3 (repeated differentiation example).
- `Problem sheets/Problem Sheet 11.pdf` and `Solutions to problem sheets/Solutions sheet 11.pdf`, T11.3.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.3.
