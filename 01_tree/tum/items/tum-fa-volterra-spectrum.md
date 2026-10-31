---
id: tum-fa-volterra-spectrum
source: tum-functional-analysis
parent: fa-spectral-theory
title: Volterra integration and a spectral point without eigenvectors
type: method
---

# Volterra integration and a spectral point without eigenvectors

On \(L^2(0,1)\), define
\[
(Vf)(x)=\int_0^xf(t)\,dt.
\]
Since \(\|f\|_1\le\|f\|_2\), \(\|Vf\|_2\le\|f\|_2\); this defines a bounded linear map on a.e. equivalence classes with a specific continuous representative for each output. Moreover
\[
|Vf(y)-Vf(x)|\le|y-x|^{1/2}\|f\|_2.
\]

If \(Vf=\lambda f\), \(\lambda\ne0\), that representative makes \(f\) continuous, then differentiable, with \(\lambda f'=f\). Thus \(f(x)=c e^{x/\lambda}\), but \(Vf(0)=0\) forces \(f(0)=0\) and hence \(c=0\). For \(\lambda=0\), vanishing indefinite integral also forces \(f=0\) a.e. There are therefore **no eigenvalues**.

Nevertheless \(0\in\sigma(V)\): a nonzero constant a.e. class cannot be an output, since the continuous representative of every \(Vf\) vanishes at zero. The full spectrum and the point spectrum are different objects; lack of eigenvectors does not imply invertibility.

## Continuous-function domain

On \(C([0,1])\) with sup norm, the same integration formula is compact. The image unit ball is bounded by 1 and satisfies \(|Vf(y)-Vf(x)|\le|y-x|\), so its closure is compact by Arzelà–Ascoli. This proof uses a uniformly Lipschitz family, distinct from the \(L^2\) half-Hölder estimate above.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Problem sheets/Problem Sheet 12.pdf` and `Solutions to problem sheets/Solutions Sheet 12.pdf` (WS 2024/25), T12.3(a–d), including the final remark about representatives.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.6, for the continuous-function compactness argument (compact closure of the image is the required conclusion).
