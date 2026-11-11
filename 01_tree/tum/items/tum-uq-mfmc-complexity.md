---
id: tum-uq-mfmc-complexity
source: tum-numuq
parent: uq-multilevel
title: Multifidelity complexity from adjacent-model variance decay
type: theorem
caption: Bounds correlation increments through coupled differences and recovers three multilevel work regimes.
---

# Multifidelity complexity from adjacent-model variance decay

In addition to the model-selection conditions, assume \(|EQ-EQ_\ell|\lesssim s^{-\alpha\ell}\), \(C_\ell\lesssim s^{\gamma\ell}\), \(0<\sigma_{\rm low}\le\sigma_\ell\le\sigma_{\rm up}<\infty\), and \(\operatorname{Var}(Q_\ell-Q_{\ell-1})\lesssim s^{-\beta\ell}\), with \(s>1\).

Minkowski applied to the centered telescoping sum bounds \(\operatorname{Var}(Q_L-Q_{\ell-1})\lesssim s^{-\beta\ell}\), uniformly in the final level. After choosing model signs so correlations with \(Q_L\) are nonnegative, the identity relating difference variance to covariance gives
\[
0\le\rho_{L,\ell}-\rho_{L,\ell-1}\le\frac{\operatorname{Var}(Q_L-Q_{\ell-1})}{2\sigma_L\sigma_{\ell-1}}.
\]
Multiplying by a sum of correlations bounded by two gives \(\Delta_\ell\lesssim\sigma_{\rm low}^{-2}s^{-\beta\ell}\). The coarse endpoint is absorbed in the uniform constant; the finest residual \(1-\rho_{L,L-1}^2\) is bounded similarly.

Choose \(L=O(|\log\varepsilon|)\) to bound squared bias by \(\varepsilon^2/2\), then substitute this correlation bound into the optimal MFMC variance. The resulting squared sum \((\sum_{\ell\le L}s^{(\gamma-\beta)\ell/2})^2\) yields production-work rates \(O(\varepsilon^{-2})\), \(O(\varepsilon^{-2}|\log\varepsilon|^2)\), or \(O(\varepsilon^{-2-(\gamma-\beta)/\alpha})\), according as \(\beta>\gamma\), \(\beta=\gamma\), or \(\beta<\gamma\). The notes sketch the first case explicitly. Feasible integer sampling additionally incurs finest-level work \(O(\varepsilon^{-\gamma/\alpha})\) unless dominated; the handwritten lecture annotation adds that term. Pilot work is excluded, and the source mentions splitting work between correlation exploration and final estimation without developing a bandit algorithm.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Assumption 9.9, Lemmas 9.10–9.11 and proof, Theorem 9.12 and its proof sketch, Remark 9.13, pp. 68–71 before ch. 10.
- `Lecture Topics and Slides/Lecture 14 (25.06.24)`, physical pp. 10–12 (printed 9–11), including added finest-resolution cost term.
