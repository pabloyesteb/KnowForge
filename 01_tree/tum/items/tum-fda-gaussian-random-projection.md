---
id: tum-fda-gaussian-random-projection
source: tum-foundations-data-analysis
parent: fda-random-projections
title: Gaussian random maps and fixed-vector norm concentration
type: theorem
caption: "Computes the projected covariance and rescales the Gaussian annulus bound to obtain a near-isometry for a fixed vector."
---

# Gaussian random maps and fixed-vector norm concentration

Let \(u_1,\ldots,u_k\) be independent standard Gaussian vectors in \(\mathbb R^d\), \(1\le k<d\), and define \(f(v)=(\langle u_i,v\rangle)_{i=1}^k\). For deterministic \(v\), rotational invariance gives each component law \(N(0,\|v\|_2^2)\). Different rows are independent, so
\[
f(v)\sim N(0,\|v\|_2^2I_k).
\]
For nonzero \(v\), divide by \(\|v\|_2\) to obtain a standard \(k\)-dimensional Gaussian. Applying its annulus estimate at width \(\varepsilon\sqrt k\) yields, for \(0<\varepsilon<1\),
\[
\mathbb P\left(\left|\|f(v)\|_2-\sqrt k\|v\|_2\right|\ge\varepsilon\sqrt k\|v\|_2\right)
\le3e^{-ck\varepsilon^2}
\]
for an absolute \(c>0\). The zero vector maps exactly to zero and should be treated separately from division or the degenerate “\(\ge0\)” failure event.

For the normalized map \(A v=f(v)/\sqrt k\), entries are independent \(N(0,1/k)\), and the norm is within factors \(1\pm\varepsilon\) of the input norm outside the failure event. The unnormalized map instead has typical amplification \(\sqrt k\); it is not already a near-isometry or an orthogonal projector.

The exercise asks for a plot of \(\|f(v)\|-\sqrt k\|v\|\) for \(v=(1,\ldots,1)/20\in\mathbb R^{400}\), a unit vector, over \(k=1,\ldots,400\). The weekly solution supplies MATLAB screenshots and one realization of the absolute deviation, computed from successive row prefixes of a Gaussian matrix. Its blue comparison curve is \(0.1\sqrt k\), although the task requests \(\varepsilon=10^{-2}\). The accompanying observation that the plotted threshold is not exceeded for \(k\ge30\) describes that realization at tolerance 0.1, not a uniform guarantee at tolerance 0.01. The theorem concerns a fixed vector independent of the random matrix, not a vector chosen after seeing its rows.

Independence of the tested vector is essential. Let \(G\in\mathbb R^{m\times n}\) have independent standard Gaussian entries and let \(g_1\) be its own first row, viewed as a column input. The self-inner-product contributes \(\mathbb E\langle g_1,g_1\rangle^2=n^2+2n\), using \(\mathbb E g_{1j}^4=3\). Each other independent row contributes \(\mathbb E\langle g_i,g_1\rangle^2=n\). Thus
\[
\mathbb E\|Gg_1/\sqrt m\|_2^2
=\frac{n^2+2n+(m-1)n}{m}
=n+\frac{n^2+n}{m}.
\]
This exceeds \(\mathbb E\|g_1\|^2=n\), potentially by a large factor. It does not contradict fixed-vector or finite-set embedding guarantees: the input was selected from the very matrix used to embed it, violating independence.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 4.1.1, p. 57; Gaussian law and annulus-reduction solution, p. 59.
- `17. Juni - 23. Juni/Exercise sheet 9.pdf`, Exercise 9.2(a–c), p. 1; `24. Juni - 30. Juni/Solution Sheet 9.pdf`, single physical page, Exercise 9.2(a–c), MGF/covariance derivation, annulus scaling and numerical plot.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 2(c–d), p. 6, fourth-moment calculation and dependence caveat.
