---
id: tum-uq-event-probability-mc
source: tum-numuq
parent: uq-monte-carlo
title: Monte Carlo event probabilities, relative error and Hoeffding control
type: method
caption: Quantifies why rare-event relative accuracy is expensive and bounds a false-majority event.
---

# Monte Carlo event probabilities, relative error and Hoeffding control

For \(p=P(X\le c)\), draw independent \(X_j\) with the law of \(X\) and average the Bernoulli indicators: \(\widehat p=M^{-1}\sum_j\mathbf1_{X_j\le c}\). It is unbiased and has mean-square error \(p(1-p)/M\). Strict absolute RMSE tolerance \(\varepsilon\) requires \(M>\varepsilon^{-2}p(1-p)\); \(p(1-p)\le1/4\) supplies a bound when \(p\) is unknown.

For \(p>0\), strict relative RMSE tolerance \(\varepsilon p\) instead requires \(M>\varepsilon^{-2}(1-p)/p\). Thus fixed relative accuracy for rare events scales inversely with the event probability, even though fixed absolute accuracy does not.

Hoeffding's inequality for independent \([0,1]\)-valued draws states \(P(\bar Z-EZ\ge\delta)\le e^{-2M\delta^2}\). If \(p=1/2-\beta\), then the event that at least half the draws satisfy \(X_j\le c\) implies \(\widehat p-p\ge\beta\), and hence has probability at most \(e^{-2M\beta^2}\). The strict-majority event is a subset and obeys the same bound. This is a finite-sample tail guarantee, distinct from an RMSE statement.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 03 (21.05.2024)`, Problem 3(a)–(d) and supplied Hoeffding theorem; `Problem Sheets/Solution Sheet 03.pdf`, printed Problem 10, pp. 6–7.
