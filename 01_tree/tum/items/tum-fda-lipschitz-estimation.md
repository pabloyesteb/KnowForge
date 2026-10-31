---
id: tum-fda-lipschitz-estimation
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Estimating Lipschitz constants by derivatives and algebra
type: method
caption: "Combines Jacobian bounds, scalar sum and product rules, and conservative domain bounds to establish Lipschitz continuity."
---

# Estimating Lipschitz constants by derivatives and algebra

A map \(F:D\subset\mathbb R^n\to\mathbb R^m\) is \(L\)-Lipschitz when \(\|F(x)-F(y)\|\le L\|x-y\|\) for every pair in \(D\). On a convex domain, a differentiable map with \(\|DF(z)\|_2\le L\) along every joining segment satisfies this inequality by integrating its derivative. Appropriate differentiability on a neighborhood handles boundary points. Conversely, on an open domain an \(L\)-Lipschitz differentiable map has derivative operator norm at most \(L\), by taking directional difference quotients. The segment/domain condition matters; a bound on disconnected pieces alone does not control pairs in different pieces.

For scalar functions the derivative norm is \(\|\nabla f\|_2\). For vector maps, \(\|DF\|_2\le\|DF\|_F\) gives a convenient sufficient bound by summing squared Jacobian entries, although it may overestimate the needed constant. Any larger constant remains valid; to prove a specified bound, the established upper bound must be no larger than that target.

Sums of functions with constants \(L_1,L_2\) have constant \(L_1+L_2\). If scalar \(g_i\) are also bounded by \(|g_i|\le B_i\), then adding and subtracting a mixed product gives
\[
|g_1(x)g_2(x)-g_1(y)g_2(y)|
\le(B_1L_2+B_2L_1)\|x-y\|.
\]
For \(e^{x_1+x_2}x_2^2\) on the unit disk, bounding on the containing square yields \(B_1=e^2,L_1=\sqrt2e^2,B_2=1,L_2=2\); hence \((2+\sqrt2)e^2\) is a valid product bound. Direct component bounds on the gradient also give \(e^2\sqrt{10}\). The review's displayed squared-gradient simplification is not used: the correct expression is \(e^{2(x_1+x_2)}[x_2^4+(x_2^2+2x_2)^2]\).

A bound on separate coefficients does not justify factoring the same coefficient out of a difference: \(c_1,c_2\le b\) does not imply \(\|c_1v-c_2w\|\le b\|v-w\|\). The review's counterexample takes \(v=(1,0),w=(1,1),c_1=1/2,c_2=1,b=1.05\), giving \(\sqrt{1.25}>1.05\). Use an actual difference decomposition or derivative bound instead.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `15. Juli - 21. Juli/All you... math 13`, single physical page, Lipschitz-continuity definition, coefficient counterexample, derivative/Jacobian criteria, scalar example, sum and product estimates, and spectral/Frobenius bounds.
