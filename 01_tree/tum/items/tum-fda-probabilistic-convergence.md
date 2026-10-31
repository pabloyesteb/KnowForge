---
id: tum-fda-probabilistic-convergence
source: tum-foundations-data-analysis
parent: fda-probability
title: Mean-square convergence versus convergence in probability
type: theorem
caption: "Proves the mean-square implication and uses rare growing values to disprove its converse."
---

# Mean-square convergence versus convergence in probability

Mean-square convergence to \(X\) means \(\mathbb E|X_n-X|^2\to0\). Convergence in probability means \(\mathbb P(|X_n-X|\ge\varepsilon)\to0\) for every fixed \(\varepsilon>0\). Markov applied to the squared difference gives
\[
\mathbb P(|X_n-X|\ge\varepsilon)
\le\frac{\mathbb E|X_n-X|^2}{\varepsilon^2},
\]
so mean-square convergence implies probability convergence.

The converse fails for \(\mathbb P(X_n=n)=1/n\), \(\mathbb P(X_n=0)=1-1/n\). For every fixed positive \(\varepsilon\) and sufficiently large \(n\), the exceptional event has probability \(1/n\to0\), but \(\mathbb EX_n^2=n\to\infty\). Rare events can vanish in probability while their squared magnitude dominates the expectation.

The accompanying diagram also records \(L^2\Rightarrow L^1\Rightarrow\) convergence in probability and almost-sure convergence \(\Rightarrow\) convergence in probability \(\Rightarrow\) convergence in distribution. Here \(L^p\) convergence means \(\mathbb E|X_n-X|^p\to0\); almost-sure convergence means pathwise convergence outside a null event; convergence in distribution uses convergence of distribution functions at continuity points of the limit CDF. The continuity-point qualification is needed beyond the diagram's abbreviated CDF formula.

The same Markov argument works for any finite \(p\ge1\): \(\mathbb P(|X_n-X|>\varepsilon)\le\mathbb E|X_n-X|^p/\varepsilon^p\). On a probability space, \(L^{p_2}\) convergence implies \(L^{p_1}\) convergence for \(1\le p_1<p_2\), as noted in the handwritten solution. The implication does not by itself supply a sharp convergence rate; quantitative tail estimates require quantitative control of its numerator.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.4, p. 42; solution and remarks, p. 51; implication diagram, p. 52.
- `3. Juni - 9. Juni/Problem Set 7.pdf`, Exercise 7.3, pp. 1–2.
- `10. Juni - 16. Juni/Solution Sheet 7.pdf`, single physical page, Exercise 7.3 and final \(L^p\) comparison remarks.
