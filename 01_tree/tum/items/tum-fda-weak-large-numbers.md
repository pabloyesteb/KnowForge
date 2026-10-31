---
id: tum-fda-weak-large-numbers
source: tum-foundations-data-analysis
parent: fda-probability
title: Chebyshev control and the weak law of large numbers
type: theorem
caption: "Uses variance additivity to bound sample-average deviations and interprets aggregation in a stipulated insurance example."
---

# Chebyshev control and the weak law of large numbers

Let \(X_i\) be i.i.d. with finite mean \(\mu\) and variance \(v\). Centering gives \(Y_i=X_i-\mu\), and independence cancels cross terms in the squared sum. Therefore
\[
\mathbb E\left|\frac1N\sum_iX_i-\mu\right|^2=\frac{v}{N}.
\]
Markov on this square yields the Chebyshev estimate
\[
\mathbb P\!\left(\left|\frac1N\sum_iX_i-\mu\right|>\varepsilon\right)
\le\frac{v}{N\varepsilon^2}\to0.
\]
This proves the finite-variance weak law, with an explicit \(1/N\) bound at fixed deviation. It controls probability, not a deterministic outcome for a particular finite sample. Linearity of expectation alone would not cancel variance cross terms; the independence assumption is material.

The review stipulates independent identically distributed device repair costs: 100 with probability 0.05, 300 with probability 0.01 and zero with probability 0.94, hence mean cost 8. A price 6 gives mean return minus 2; a price 10 gives mean return 2. At price 10, returns are \(-90,-290,10\), with second moment 1340 and variance \(1340-2^2=1336\). The average return therefore has a deviation bound \(1336/(N\varepsilon^2)\). A single contract can still lose money despite positive expected return.

The example illustrates aggregation under explicit i.i.d. assumptions. It is not an empirical failure model or a guarantee against common failures across devices. Finite variance gives this bound without an exponential moment, whereas sharper exponential estimates need additional tail information.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `17. Juni - 23. Juni/All you... math 9`, single physical page, “Limiting Laws in Probability”, device-insurance setup, centered-variance proof and numerical return moments, before the cumulant-generating function.
