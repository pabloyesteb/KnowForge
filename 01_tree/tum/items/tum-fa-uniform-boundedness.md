---
id: tum-fa-uniform-boundedness
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Uniform boundedness of operator families
type: theorem
caption: "Uses Baire category to turn pointwise bounds on bounded-operator families over a Banach domain into a common operator-norm bound."
---

# Uniform boundedness of operator families

## Statement and proof

Let \(X\) be Banach, \(Y\) normed, and \(\mathcal T\subset\mathcal L(X;Y)\). If \(\sup_{T\in\mathcal T}\|Tx\|<\infty\) for each \(x\in X\), then \(\sup_{T\in\mathcal T}\|T\|<\infty\). Completeness of \(Y\) is not required.

The sets \(A_n=\{x:\sup_T\|Tx\|\le n\}\) are closed and cover \(X\). Baire gives one \(A_k\) containing a ball \(K(x_0,\varepsilon)\). For \(x\ne0\), put \(z=x_0+\varepsilon x/\|x\|\). Since both \(z,x_0\in A_k\),
\[
\|Tx\|=\frac{\|x\|}{\varepsilon}\|Tz-Tx_0\|
\le\frac{2k}{\varepsilon}\|x\|.
\]
This single bound applies to the whole family. Pointwise boundedness does not mean that the bound initially given for each vector is already uniform on the unit ball.

## Dual boundedness criterion

A subset \(M\) of any normed space \(X\) is norm-bounded exactly when \(f(M)\) is bounded for every \(f\in X^*\). Apply uniform boundedness on the Banach space \(X^*\) to the evaluation operators \(J_Xx:f\mapsto f(x)\), \(x\in M\). Hahn–Banach gives \(\|J_Xx\|=\|x\|\). Thus completeness of \(X\) itself is not required for this criterion.

The consequences and incomplete-domain counterexample for pointwise operator limits are in [operator convergence](tum-fa-operator-convergence.md).

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Proposition 3.5, pp. 33–34; Proposition 4.15, p. 43.
- E5/S5, T5.2–T5.3.
