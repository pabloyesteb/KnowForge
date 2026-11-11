---
id: tum-uq-moment-pathwise-rates
source: tum-numuq
parent: uq-probability
title: From moment error rates to tail and almost-sure rates
type: theorem
caption: "Combines the norm-moment tail bound with Borel–Cantelli to recover nearly matching pathwise rates."
---

# From moment error rates to tail and almost-sure rates

For \(X\in L^p(\Omega;H)\) and \(R>0\), the source's Chebyshev bound is \(P(\|X\|\ge R)\le R^{-p}E\|X\|^p\). Integrate \(\|X\|^p\) only over \(\{\|X\|\ge R\}\), where it is at least \(R^p\), to prove the inequality. Borel–Cantelli says that \(\sum_nP(A_n)<\infty\) makes the events occur only finitely often almost surely; this direction requires no independence.

Suppose \(\|X_n-X\|_{L^p(\Omega;H)}\le K_p n^{-r}\). For any \(\varepsilon>0\), apply the bound with \(R=n^{-r+\varepsilon}\):
\[
P(\|X_n-X\|\ge n^{-r+\varepsilon})\le K_p^p n^{-p\varepsilon}.
\]
Choose \(p\) such that \(p\varepsilon>1\). Summability gives an almost-sure random index after which the error is at most \(n^{-r+\varepsilon}\). Absorb the finitely many earlier errors into
\(K(\omega)=\max\{1,n^{r-\varepsilon}\|X_n(\omega)-X(\omega)\|:n\le n_*(\omega)\}\), yielding \(\|X_n-X\|\le K(\omega)n^{-r+\varepsilon}\) for all \(n\) almost surely.

The theorem assumes the same rate exponent \(r>0\) for every sufficiently large moment order, with constants allowed to depend on that order. Then any prescribed small rate loss \(0<\varepsilon<r\) is available, and the bound tends to zero. A single fixed \(p\) only gives summability for losses satisfying \(p\varepsilon>1\); a tail bound with nondecaying threshold does not alone imply convergence. The random constant need not have any moment bound supplied by this argument.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.4, Lemmas 2.53–2.54 and Theorem 2.55, pp. 12–13, full tail and random-index proof.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical pp. 19–21 (printed 33–35), inequalities and rate theorem.
