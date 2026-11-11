---
id: tum-uq-mlmc-allocation
source: tum-numuq
parent: uq-multilevel
title: Cost-optimal allocation of multilevel samples
type: method
caption: Allocates samples according to correction variance divided by cost and normalizes them to a variance target.
---

# Cost-optimal allocation of multilevel samples

For level variances \(V_\ell\ge0\) and positive per-correction costs \(C_\ell\), minimize \(\sum_\ell V_\ell/M_\ell\) subject to \(\sum_\ell C_\ell M_\ell=C\), initially treating sample counts as positive real numbers. Lagrange stationarity yields \(-V_\ell/M_\ell^2+\lambda C_\ell=0\), so
\[
M_\ell\propto\sqrt{V_\ell/C_\ell}.
\]
Let \(S=\sum_\ell\sqrt{V_\ell C_\ell}\). At fixed cost, \(M_\ell=(C/S)\sqrt{V_\ell/C_\ell}\) gives variance \(S^2/C\). Equivalently a sampling-variance target \(v\) is attained with \(M_\ell=(S/v)\sqrt{V_\ell/C_\ell}\), costing \(S^2/v\). The theorem uses \(v=\varepsilon^2/2\). Actual counts are rounded upward; nonzero active levels require at least one sample, which adds a finest-resolution work term.

If variance falls faster than cost grows, coarse levels dominate the allocation's work and many cheap samples replace expensive full-resolution samples. When cost grows faster, fine-level work dominates but the small correction variance can still reduce the required fine sample count. These are rate-based comparisons, not a guarantee from sample allocation alone: coupling quality, bias and costs determine the actual gain.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §8.2, pp. 61–62, complete Lagrange functional, stationarity and limiting cost comparisons; appendix E, pp. 105–106, integer rounding.
- `Lecture Topics and Slides/Lecture 13 (18.06.24)`, physical p. 9 (printed 7), variance/cost allocation and handwritten rate substitution.
