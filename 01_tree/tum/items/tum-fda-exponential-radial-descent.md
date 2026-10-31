---
id: tum-fda-exponential-radial-descent
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Invariant-ball gradient descent for an exponential quadratic
type: algorithm
caption: "Bounds gradient smoothness and proves convergence from every point of the open unit ball by a radial contraction."
---

# Invariant-ball gradient descent for an exponential quadratic

For \(f(x)=e^{\|x\|_2^2}\) on the open unit ball \(B_1\subset\mathbb R^n\),
\[
\nabla f(x)=2e^{\|x\|^2}x,\qquad
\nabla^2f(x)=2e^{\|x\|^2}I+4e^{\|x\|^2}xx^T.
\]
Its Hessian operator norm is at most \(6e\) on this convex domain, so the gradient is \(6e\)-Lipschitz. The supplied solution obtains the same constant by adding and subtracting a mixed term, bounding the exponential derivative on \([0,1]\), and using \(|\|x\|^2-\|y\|^2|\le2\|x-y\|\).

Gradient descent with \(\alpha=1/20\) reads
\[
x_{k+1}=\left(1-\tfrac1{10}e^{\|x_k\|^2}\right)x_k.
\]
For \(\|x_k\|<1\), the multiplier lies between \(1-e/10>0\) and \(9/10\). Hence \(\|x_{k+1}\|\le(9/10)\|x_k\|<1\). Induction proves that every initial point in \(B_1\) stays there and satisfies \(\|x_k\|\le(9/10)^k\|x_0\|\to0\). The whole open ball is therefore a convergence set, and the limit is its unique minimizer because \(e^{\|x\|^2}\ge1\), with equality only at zero. Invariance is proved for the actual iterates; a local smoothness bound alone would not ensure they remain in its domain.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 4(a–d), pp. 9–10, smoothness estimate, explicit recurrence, ball invariance and whole-ball convergence conclusion.
