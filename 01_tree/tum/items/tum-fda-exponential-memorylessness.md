---
id: tum-fda-exponential-memorylessness
source: tum-foundations-data-analysis
parent: fda-probability
title: Conditional probabilities and exponential waiting-time memorylessness
type: theorem
caption: "Normalizes event probabilities after conditioning and derives an unchanged exponential residual lifetime."
---

# Conditional probabilities and exponential waiting-time memorylessness

For events \(A,B\) with \(\mathbb P(B)>0\),
\[
\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)}.
\]
Conditioning restricts attention to \(B\) and rescales it to probability one. If the two events are independent, \(\mathbb P(A\mid B)=\mathbb P(A)\); the observed event then leaves that probability unchanged.

An exponential variable of rate \(\alpha>0\) has density \(\alpha e^{-\alpha x}\mathbf1_{x>0}\), normalized by integrating the exponential tail. Integration by parts gives \(\mathbb EX=1/\alpha\). Its survival function is \(\mathbb P(X>t)=e^{-\alpha t}\) for \(t\ge0\).

If a waiting time has already exceeded \(a\ge0\), then for \(b\ge0\),
\[
\mathbb P(X>a+b\mid X>a)
=\frac{\mathbb P(X>a+b)}{\mathbb P(X>a)}
=e^{-\alpha b}=\mathbb P(X>b).
\]
The intersection reduces to the smaller event because \(\{X>a+b\}\subset\{X>a\}\). Thus the residual waiting time has the same exponential survival law; with mean waiting time \(T\), the rate is \(1/T\). This memoryless property belongs to the assumed exponential model, not to arbitrary physical lifetimes.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `17. Juni - 23. Juni/All you... math 9`, single physical page, “Conditional Probability”, independence remark, “Example (Exponential Distribution)”, normalization, expectation, and residual waiting-time derivation.
