---
id: tum-fda-chernoff-exponential-tilting
source: tum-foundations-data-analysis
parent: fda-probability
title: Exponential-moment tail bounds and tilt selection
type: method
caption: "Applies Markov to an exponential transform and optimizes the positive tilt within the MGF domain."
---

# Exponential-moment tail bounds and tilt selection

For \(\theta>0\) with finite \(M_X(\theta)\),
\[
\mathbb P(X>t)=\mathbb P(e^{\theta X}>e^{\theta t})
\le e^{-\theta t}M_X(\theta).
\]
Minimize this expression over allowed positive \(\theta\), or equivalently minimize \(\log M_X(\theta)-\theta t\). The choice of tilt uses more distributional information than a first-moment bound; finiteness of the exponential moment matters.

For \(X\sim U[0,4]\),
\[
M_X(\theta)=\frac{e^{4\theta}-1}{4\theta},\qquad
\mathbb P(X>3)\le\frac{e^{4\theta}-1}{4\theta e^{3\theta}}.
\]
The booklet reports a numerical tilt near 0.89839, giving a bound around 66.5%, compared to the exact 25%. This example does not outperform its optimized power-moment estimate: exponential tilting is a family of bounds, not a universal claim of greater sharpness for every finite distribution.

For independent copies \(R_i\), let \(C_R(\theta)=\log\mathbb E e^{\theta R}\) on its finite domain. Factoring exponential moments gives, for any allowed \(\theta>0\),
\[
\mathbb P\left(\frac1N\sum_iR_i>\mu+\varepsilon\right)
\le\exp\{-N[\theta(\mu+\varepsilon)-C_R(\theta)]\}.
\]
Optimize by taking the supremum of the bracket over positive tilts. Lower tails use \(-R\) and \(C_{-R}(\theta)=C_R(-\theta)\). This derivation explains the review's Cramér-type exponential estimates; it supplies an upper bound rather than asserting an exact asymptotic equivalence without further hypotheses.

For the review's return law at price 10,
\[
C_R(\theta)=\log[0.05e^{-90\theta}+0.01e^{-290\theta}+0.94e^{10\theta}],\quad \mu=2.
\]
This finite-support model has finite exponential moments for every real tilt. By contrast a density proportional to \(1/(1+x^4)\) has finite variance but lacks finite nonzero exponential moments on the full real line. One cannot infer exponential concentration merely from finite variance.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.2(4), p. 42; solution, p. 49, equations (46)–(47).
- `3. Juni - 9. Juni/Problem Set 7.pdf`, Exercise 7.1(d), p. 1.
- `10. Juni - 16. Juni/Solution Sheet 7.pdf`, single physical page, Exercise 7.1(d), full derivations and comparisons.
- `17. Juni - 23. Juni/All you... math 9`, single physical page, cumulant-generating function, “Cramér Theorem” upper/lower-tail computation, and polynomial-tail contrast.
