---
id: tum-uq-basic-monte-carlo
source: tum-numuq
parent: uq-monte-carlo
title: Monte Carlo sample means, consistency and root-sample error
type: theorem
caption: Separates almost-sure consistency, central-limit behavior and exact mean-square sampling error.
---

# Monte Carlo sample means, consistency and root-sample error

For iid copies \(X_j\) of an integrable scalar variable, \(\bar X_M=M^{-1}\sum_jX_j\) is unbiased and converges almost surely to \(EX\) by the strong law. A finite second moment additionally gives
\[
E|\bar X_M-EX|^2=\operatorname{Var}(X)/M,\qquad
\sqrt M(\bar X_M-EX)\Rightarrow N(0,\operatorname{Var}X).
\]
Independent centered cross terms vanish in the variance calculation. Thus RMSE is \(\sqrt{\operatorname{Var}X}\,M^{-1/2}\); the CLT describes an asymptotic law rather than a finite-sample deterministic error bound.

Chebyshev also gives \(P(|\bar X_M-EX|\ge M^{-1/2+\delta})\le\operatorname{Var}(X)M^{-2\delta}\) for \(\delta>0\). This alone is not an arbitrary near-\(M^{-1/2}\) almost-sure rate, since summability needs \(2\delta>1\) unless higher-moment information is added. The notes' variance-reduction paragraph writes \(M\to0\); consistency is for \(M\to\infty\).

The exponent does not require integrand smoothness and does not explicitly depend on input dimension. Variance and sample-generation cost can still depend on dimension, so dimension-independent rate is not dimension-independent total work. Reducing variance or using a better integration rule can improve accuracy at fixed work.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §7.1, Definition 7.1 and listed laws, p. 51; §§7.3.1–7.3.2, pp. 56–57.
- `Lecture Topics and Slides/Lecture 11 (11.06.24)`, physical pp. 3–5; `Lecture Topics and Slides/Lecture 12 (13.06.24)`, physical p. 5.
