---
id: tum-uq-saob-allocation
source: tum-numuq
parent: uq-multilevel
title: Sample-allocation optimal BLUE and complexity transfer
type: method
caption: Optimizes group counts under a work constraint and compares its cost with any feasible unbiased linear competitor.
---

# Sample-allocation optimal BLUE and complexity transfer

For group cost \(W^k=\sum_{\ell\in S^k}w_\ell\), the sample-allocation problem minimizes \(e_L^T\Psi(m)^{-1}e_L\) subject to \(\sum_km_kW^k\le p\) and nonnegative integer counts supporting an identifiable design. Applying BLUE at an optimal allocation gives the sample-allocation optimal BLUE (SAOB). Covariance-estimation work is excluded from this production budget. The slides also state a sparse-support property (at most \(L\) active groups); no proof or integer-design qualifications are supplied, so this is not a general recipe for dropping arbitrary groups in the discrete problem.

For a prescribed vector \(\alpha\), replace \(e_L\) by \(\alpha\) to estimate \(\alpha^T\mu\). Unbiasedness becomes \(\sum_kP^k\beta^k=\alpha\). Its bias relative to the continuum target is \(\alpha^T\mu-EZ\), which SAOB's variance optimization does not remove.

If a linear estimator of the same \(\alpha^T\mu\), using the admitted model groups, achieves MSE \(\varepsilon^2\) at work \(\varphi(\varepsilon^2)\), SAOB can achieve no larger MSE at no greater work: it has the same bias and minimal variance at that work. This is the supplement's complexity-transfer argument. “Smallest cost” therefore means cost for a specified accuracy, not unconditionally cheapest regardless of variance.

Alternatively, a sequence of bias vectors and correction groups with bias rate \(2^{-\ell b}\), group variance rate \(2^{-kv}\) and cost rate \(2^{kc}\) permits the same geometric allocation argument as MLMC. Work is bounded by \(O(\varepsilon^{-c/b})\) plus the three terms \(O(\varepsilon^{-2})\), \(O(\varepsilon^{-2}|\log\varepsilon|^2)\), or \(O(\varepsilon^{-2-(c-v)/b})\), for \(v>c\), \(v=c\), or \(v<c\). The supplement emphasizes that verifying those rates can be difficult; comparison with an already analyzed MLMC or Richardson estimator avoids directly analyzing optimal weights.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Slides on Multilevel BLUE (27.06.24)`, physical pp. 18–24 (printed 17–23), allocation, generalized bias constraint, Theorems 2–3 and transfer proof; summaries physical pp. 34–35.
- `Lecture Topics and Slides/Lecture 15 (27.06.24)`, corresponding pages, budget and group-count annotations.
