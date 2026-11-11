---
id: tum-uq-mlmc-complexity
source: tum-numuq
parent: uq-multilevel
title: MLMC complexity in three variance–cost regimes
type: theorem
caption: Combines geometric bias control, optimal sample allocation and integer counts to prove tolerance-dependent work bounds.
---

# MLMC complexity in three variance–cost regimes

Assume geometric levels and positive rates satisfying
\[
\|Eu-Eu_{h_\ell}\|\le c_1h_\ell^\alpha,\quad
V_\ell\le c_2h_\ell^\beta,\quad C_\ell\lesssim h_\ell^{-\gamma}.
\]
There are a finest level and independent correction sample counts with RMSE at most \(\varepsilon\) and cost
\[
O(\varepsilon^{-\gamma/\alpha})+
\begin{cases}
O(\varepsilon^{-2}),&\beta>\gamma,\\
O(\varepsilon^{-2}|\log\varepsilon|^2),&\beta=\gamma,\\
O(\varepsilon^{-2-(\gamma-\beta)/\alpha}),&\beta<\gamma.
\end{cases}
\]
The first term pays for at least one sample at the finest resolution; it must be retained unless a relation between rates makes it subordinate. Cost for a coupled difference includes both adjacent solves and is comparable to the fine solve on a geometric hierarchy.

For the proof, rescale \(h_0=1\) and choose \(L=\lceil\alpha^{-1}\log_s(\sqrt2c_1/\varepsilon)\rceil\), adjusted to be nonnegative. Bias is then at most \(\varepsilon/\sqrt2\), with \(L+1=O(|\log\varepsilon|)\). The variance-target allocation is proportional to \(\varepsilon^{-2}S\sqrt{V_\ell/C_\ell}\), rounded upward. The sum \(S\lesssim\sum_{\ell=0}^Ls^{(\gamma-\beta)\ell/2}\) is bounded, grows linearly in \(L+1\), or is dominated by its final term, respectively. Squaring it gives the three regimes. The rounding surplus costs \(\sum C_\ell=O(h_L^{-\gamma})=O(\varepsilon^{-\gamma/\alpha})\). The appendix constructs the corresponding counts explicitly and bounds sampling variance by \(\varepsilon^2/2\).

A strong approximation rate \(\|u-u_h\|_{L^2}\lesssim h^t\) implies admissible \(\alpha=t\) by Jensen and \(\beta=2t\) by the coupled triangle bound. These are sufficient bounds, not necessarily sharp weak or variance rates. For the lecture example \(\alpha=1,\beta=\gamma=2\), work improves from single-level \(O(\varepsilon^{-4})\) to \(O(\varepsilon^{-2}|\log\varepsilon|^2)\).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Theorem 8.3 and verification of (M1)–(M3), pp. 62–63; appendix E, complete proof pp. 104–106.
- `Lecture Topics and Slides/Lecture 13 (18.06.24)`, physical pp. 11–13 (printed 10, handwritten example, 11).
