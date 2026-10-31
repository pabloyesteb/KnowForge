---
id: tum-fda-gaussian-norm-concentration
source: tum-foundations-data-analysis
parent: fda-probability
title: Subexponential Gaussian squares and concentration of Gaussian norms
type: theorem
caption: "Uses centered Gaussian squares and Bernstein concentration to place isotropic Gaussian vectors in a thin radial shell."
---

# Subexponential Gaussian squares and concentration of Gaussian norms

The booklet calls \(Z\) subexponential when \(\mathbb P(|Z|>t)\le c e^{-Ct}\) for positive absolute constants and all \(t>0\). If \(G\sim N(0,1)\), translating its tail integral shows \(\mathbb P(G>s)\le\frac12 e^{-s^2/2}\). Reflection gives
\[
\mathbb P(G^2>t)=\mathbb P(|G|>\sqrt t)\le e^{-t/2},
\]
so a Gaussian square is subexponential, although its mean is one rather than zero. Centering it preserves the exponential tail class with suitable constants; equality of the original constants is not required.

For independent \(G_i\sim N(0,1)\), set \(Y_i=G_i^2-1\). Then \(\mathbb EY_i=0\), and a Bernstein inequality for independent centered subexponential variables gives the source's consequence
\[
\mathbb P\!\left(\left|\sum_iY_i\right|>n\varepsilon\right)
\le2e^{-c\varepsilon^2n},\qquad 0<\varepsilon<1,
\]
for an absolute \(c>0\). The squared-norm deviation is exactly this sum. Therefore, with probability at least \(1-2e^{-c\varepsilon^2n}\),
\[
\sqrt{n}\sqrt{1-\varepsilon}\le\|G\|_2\le\sqrt{n}\sqrt{1+\varepsilon}.
\]
The booklet invokes a lecture Bernstein result rather than supplying its general proof.

Its additional Gaussian Annulus Theorem states that for \(0<\beta\le\sqrt n\),
\[
\mathbb P\big(\sqrt n-\beta\le\|G\|_2\le\sqrt n+\beta\big)
\ge1-3e^{-c\beta^2}.
\]
This is radial concentration about \(\sqrt n\) for mean zero and identity covariance, not concentration around the origin in a fixed-radius ball. The two shell formulations use different relative/absolute deviation parameters.

A further proof in the weekly solution uses \(\mathbb E e^{\theta G^2}=(1-2\theta)^{-1/2}\), valid for \(\theta<1/2\). For \(0<\theta<1/2\), Markov gives \(\mathbb P(G^2>t)\le e^{-\theta t}/\sqrt{1-2\theta}\); even the fixed choice \(\theta=1/4\) already proves an exponential tail. The square-MGF domain differs from the all-real domain of a Gaussian variable's own MGF.

The later annulus proof uses the event implication
\[
|\|G\|-\sqrt n|>t\ \Longrightarrow\
|\|G\|^2-n|>t\sqrt n,
\]
because \(\|G\|+\sqrt n\ge\sqrt n\). The right-hand quantity is a sum of independent centered Gaussian squares, so Bernstein yields a bound \(Ce^{-ct^2}\) for \(0<t\le\sqrt n\). This proves an absolute-width shell estimate, rather than only asserting it as in the earlier booklet remark.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.6 and Gaussian-annulus remark, p. 43; solution invoking Bernstein, pp. 54–55.
- `10. Juni - 16. Juni/Problem Set 8.pdf`, Exercise 8.2 and annulus remark, p. 2.
- `17. Juni - 23. Juni/Solution Sheet 8.pdf`, single physical page, Exercise 8.2(a), three proofs including square MGF; 8.2(b), centered-square Bernstein argument.
- `17. Juni - 23. Juni/Exercise sheet 9.pdf`, Exercise 9.1, p. 1; `24. Juni - 30. Juni/Solution Sheet 9.pdf`, single physical page, Exercise 9.1, factorization and Bernstein proof.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 2(a), p. 4, translated Gaussian tail integral and explicit subexponential parameters alpha = 1/2, beta = 1.
