---
id: tum-fda-convex-conjugate
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Convex conjugates and a separable quartic example
type: method
caption: "Maximizes affine-minus-function expressions and solves the quartic conjugate by coordinate stationarity."
---

# Convex conjugates and a separable quartic example

The Legendre–Fenchel conjugate is
\[
f^*(y)=\sup_x\{\langle y,x\rangle-f(x)\},
\]
allowing value \(+\infty\). Each fixed \(x\) gives an affine function of \(y\), which motivates the convex character of the construction; finiteness is a separate issue.

The review introduces power objectives \(f(x)=\frac1p\sum_i|x_i|^p\), \(p>1\), whose gradient has entries \(|x_i|^{p-1}\operatorname{sign}(x_i)\), and works out \(p=4\). For
\[
f(x)=\tfrac14\sum_i x_i^4,
\]
maximizing the conjugate expression is separable. Its stationarity equations are \(y_i-x_i^3=0\), hence \(x_i=\sqrt[3]{y_i}\), using real cube roots. The negative quartic makes the expression tend to \(-\infty\) as \(\|x\|\to\infty\), and each coordinate maximum is unique. Substitution gives
\[
f^*(y)=\tfrac34\sum_i|y_i|^{4/3}.
\]
For negative coordinates, the absolute-value expression makes the real interpretation of the handwritten \(y_i^{4/3}\) explicit. Stationarity is sufficient in this example because of the concave maximization structure and attainment, not for arbitrary functions merely appearing inside a supremum.

For a differentiable strictly convex scalar function with injective derivative, and \(y\in\operatorname{range}f'\), the equation \(f'(x)=y\) identifies the maximizer of \(yx-f(x)\). Thus
\[
f^*(y)=y(f')^{-1}(y)-f((f')^{-1}(y)).
\]
The booklet assumes strong convexity for this step, but inverse-derivative evaluation on its range also applies to its strictly convex example \(f(x)=e^x\), which has no positive uniform strong-convexity constant on all of \(\mathbb R\). The inverse here is a function inverse, not the reciprocal of \(f'\).

For that exponential, \(\operatorname{range}f'=(0,\infty)\) and \((f')^{-1}(y)=\log y\), so
\[
f^*(y)=\begin{cases}y\log y-y&y>0,\\0&y=0,\\+\infty&y<0.\end{cases}
\]
At zero the supremum is approached as \(x\to-\infty\) without a finite maximizer; for negative \(y\) the same limit makes \(yx-e^x\) unbounded above. One cannot apply the inverse-derivative formula outside its derivative range without checking the supremum separately.

The later review states the general conjugate pair \(\frac1p\|x\|_p^p\leftrightarrow\frac1q\|y\|_q^q\), for \(p>1\), \(1/p+1/q=1\). Coordinate stationarity gives \(x_i=\operatorname{sign}(y_i)|y_i|^{1/(p-1)}\); substituting yields \(|y_i|^q/q\) per coordinate. This includes the worked quartic case with \(q=4/3\).

For the linear function \(f(x)=c^Tx\), its conjugate is \(f^*(y)=\delta_{\{c\}}(y)\): the supremum of \((y-c)^Tx\) is zero when \(y=c\), and is unbounded above otherwise by taking \(x=t(y-c)\), \(t\to\infty\). This turns an unconstrained linear supremum into an exact equality constraint in dual calculations.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, final “Convex Conjugate”, power objectives, gradient and quartic maximization through end of page.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.2(c1–c2), p. 62; inverse derivative and exponential boundary cases, p. 68.
- `24. Juni - 30. Juni/Exercise sheet 10.pdf`, Exercise 10.2(c1–c2), p. 1.
- `1. Juli - 7. Juli/Solution sheet 10.pdf`, single physical page, Exercise 10.2(c1–c2), full argument and illustrations.
- `8. Juli - 14. Juli/All you ... math 12`, single physical page, opening “Convex Conjugate”, quartic Hessian and maximization, and conjugate-exponent general rule.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 3(a), p. 7, singleton-indicator conjugate.
