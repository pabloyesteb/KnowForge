---
id: tum-fda-bernstein-weighted-sums
source: tum-foundations-data-analysis
parent: fda-probability
title: Bernstein concentration from a local quadratic MGF bound
type: theorem
caption: "Derives the quadratic and linear tail regimes for independent centered subexponential weighted sums."
---

# Bernstein concentration from a local quadratic MGF bound

Let independent centered variables \(X_i\) obey the common local MGF bound \(\mathbb E e^{\theta X_i}\le e^{c_2\theta^2}\) for \(|\theta|\le c_1\), with positive constants. For nonzero \(a\), independence and exponential Markov yield
\[
\mathbb P(S>t)\le\exp(-\theta t+c_2\theta^2\|a\|_2^2),\qquad S=\sum_i a_iX_i,
\quad0<\theta\le c_1/\|a\|_\infty.
\]
Choose \(\widetilde\theta=\min\{t/(2c_2\|a\|_2^2),c_1/\|a\|_\infty\}\). Then \(c_2\widetilde\theta^2\|a\|_2^2\le\widetilde\theta t/2\). Applying the same calculation to \(-S\) gives
\[
\mathbb P(|S|>t)\le2\exp(-\widetilde\theta t/2)
=2\exp\left[-\min\left\{\frac{t^2}{4c_2\|a\|_2^2},\frac{c_1t}{2\|a\|_\infty}\right\}\right].
\]
The coefficient Euclidean norm controls the small-deviation quadratic regime, and the largest coefficient controls the large-deviation linear regime and the admissible exponential tilt. If \(a=0\), the tail probability is zero and the quotients are unnecessary. The sample exam assumes identically distributed subexponential variables and supplies the local MGF statement without proof; the calculation needs only independence and common MGF constants.

The printed target and final handwritten conclusion omit the factor one half in the exponent for the stated \(\widetilde\theta\). The handwritten blue annotation correctly asks for exponent at most \(-\theta t/2\); the bound above is what the displayed MGF derivation establishes. Constants must be adjusted before writing a stronger-looking exponent.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 2 introductory MGF assumption, p. 4; Problem 2(b), p. 5, complete handwritten derivation including blue exponent annotation.
