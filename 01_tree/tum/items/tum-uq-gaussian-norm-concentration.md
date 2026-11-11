---
id: tum-uq-gaussian-norm-concentration
source: tum-numuq
parent: uq-probability
title: Gaussian quadratic exponential moments and norm concentration
type: theorem
caption: Derives finite polynomial moments and dimension-dependent Gaussian shell bounds from an explicit generating integral.
---

# Gaussian quadratic exponential moments and norm concentration

For \(X\sim N(0,I_n)\), completing the density exponent gives
\[
E e^{t\|X\|_2^2}=(1-2t)^{-n/2},\qquad 0<t<1/2.
\]
Independence factors polynomial moments into scalar Gaussian integrals. Odd powers integrate to zero; even powers are bounded by a multiple of an integrable exponential series, proving finiteness of all mixed absolute moments as well.

For \(0<\varepsilon<1\), exponential Markov with \(t=\varepsilon/2\) gives
\[
P\left(\|X\|_2^2\ge\frac n{1-\varepsilon}\right)
\le\exp\left[-\frac n2\left(\frac\varepsilon{1-\varepsilon}+\log(1-\varepsilon)\right)\right]
\le e^{-n\varepsilon^2/4}.
\]
The last inequality follows by expanding both functions: the linear terms cancel and the remaining sum is at least \(\varepsilon^2/2\). The solution also states the analogous lower bound \(P(\|X\|_2^2\le n(1-\varepsilon))\le e^{-n\varepsilon^2/4}\). Together these express concentration near radius \(\sqrt n\), with exponentially small probabilities outside a fixed relative shell as dimension increases.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 03 (21.05.2024)`, Problem 2(a)–(c); `Problem Sheets/Solution Sheet 03.pdf`, printed Problem 9, pp. 4–5, explicit Gaussian integral, polynomial-moment proof and concentration derivation.
