---
id: tum-fa-lp-compactness
source: tum-functional-analysis
parent: fa-weak-compactness
title: Fréchet–Riesz–Kolmogorov compactness in finite-exponent spaces
type: theorem
---

# Fréchet–Riesz–Kolmogorov compactness in finite-exponent spaces

## Family-level translation criterion

Let \(\Omega\subset\mathbb R^n\) be open and bounded and \(1\le p<\infty\). A family \(F\subset L^p(\Omega)\) is relatively compact iff it is bounded and, after zero extension,
\[
\lim_{h\to0}\sup_{f\in F}\int_\Omega|f(x+h)-f(x)|^p\,dx=0.
\]
The theorem controls small translations **uniformly over the family**. For each fixed \(f\), translation continuity is automatic, but that pointwise fact alone is insufficient for compactness of \(F\). The bounded-domain and finite-\(p\) hypotheses delimit the source's statement; no criterion for unbounded domains without additional tail control is asserted.

This is an \(L^p\) analogue of equicontinuity-based compactness, replacing pointwise function oscillations by translation differences in norm. Relative compactness means compact closure; closedness must be added to conclude that \(F\) itself is compact.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Proposition 5.10 and preceding translation result, p. 50. The compactness criterion is stated without proof.
