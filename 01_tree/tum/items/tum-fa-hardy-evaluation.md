---
id: tum-fa-hardy-evaluation
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Hardy-space coefficient geometry and bounded point evaluation
type: concept
caption: "Builds a Hilbert space from square-summable power-series coefficients and represents interior evaluation by an explicit kernel."
---

# Hardy-space coefficient geometry and bounded point evaluation

On the unit disk \(\mathbb D\subset\mathbb C\), form
\[
H=\left\{f_a(z)=\sum_{n=0}^\infty a_nz^n:a\in\ell^2\right\}.
\]
Square-summable coefficients are bounded, so the power series converges absolutely for \(|z|<1\) and defines a holomorphic function. Uniqueness of power-series coefficients makes \(a\mapsto f_a\) bijective. Transporting the \(\ell^2\) inner product gives
\[
\langle f_a,f_b\rangle_H=\sum_{n=0}^\infty a_n\overline{b_n}.
\]
This makes \(H\) a Hilbert space isometrically isomorphic to \(\ell^2\); the construction is by coefficient norm, not a sup norm on the disk.

For \(\lambda\in\mathbb D\), the vector \((\overline\lambda^n)_{n\ge0}\in\ell^2\) corresponds to
\[
g_\lambda(z)=\sum_{n=0}^\infty\overline\lambda^nz^n
=\frac1{1-\overline\lambda z},\qquad
f(\lambda)=\langle f,g_\lambda\rangle_H.
\]
Thus evaluation is a bounded functional represented by an explicit kernel. Cauchy–Schwarz gives
\[
|f(\lambda)|\le\|f\|_H\|g_\lambda\|_H,
\qquad\|g_\lambda\|_H=(1-|\lambda|^2)^{-1/2}.
\]
The displayed norm follows from the geometric coefficient series. Interior evaluation is controlled, but the bound grows near the unit circle; no boundary-evaluation theorem is asserted.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Problem sheets/Problem Sheet 14.pdf` and `Solutions to problem sheets/Solutions Sheet 14.pdf` (WS 2024/25), T14.2(a–d).
