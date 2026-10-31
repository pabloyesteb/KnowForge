---
id: tum-fa-sobolev-holder
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: One-dimensional Sobolev regularity and Hölder representatives
type: theorem
---

# One-dimensional Sobolev regularity and Hölder representatives

For \(1<p<\infty\), every \(u\in W^{1,p}(\mathbb R)\) has a representative \(\tilde u\) satisfying
\[
|\tilde u(x)-\tilde u(y)|
\le\|u\|_{W^{1,p}}|x-y|^{1-1/p}.
\]
The representative agrees with \(u\) almost everywhere; the assertion does not assign pointwise meaning to every arbitrary representative of its equivalence class.

For smooth mollifications \(u_n=u*\omega_n\), the fundamental theorem and Hölder give
\[
|u_n(y)-u_n(x)|
\le\left(\int_x^y|u_n'(t)|^pdt\right)^{1/p}|y-x|^{1-1/p}
\le\|u_n'\|_p|y-x|^{1-1/p}.
\]
Convergence \(u_n\to u\) in \(W^{1,p}\) bounds these Hölder constants. Together with bounded \(L^p\) norms this bounds function values on compact intervals. Arzelà–Ascoli, followed by a diagonal choice over expanding intervals, gives a locally uniformly convergent subsequence. Its continuous limit inherits the estimate; convergence in \(L^p\) identifies that limit with \(u\) almost everywhere.

This connects integral control of one weak derivative to regularity of a representative, with dimension and exponent explicitly fixed. The supplement presents this one-dimensional result as an example, not a general-dimensional Sobolev-embedding classification.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Distributions.pdf` (WS 2024/25), Section 8, Corollary 1, Eq. (16) and proof, p. 10.
