---
id: tum-fa-distribution-regularization
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Smooth regularization of distributions
type: method
---

# Smooth regularization of distributions

## Convolution through test functions

Choose a nonnegative, even, smooth compactly supported kernel \(\omega\), supported in the closed unit ball, with integral 1, and put \(\omega_n(z)=n^d\omega(nz)\). For \(f\in\mathcal D'\), define
\[
f_n(x)=(f*\omega_n)(x)=f\bigl(\omega_n(\,\cdot-x)\bigr).
\]
The test-function dependence on \(x\) is smooth. Derivatives act on that dependence:
\[
\partial_x^\alpha f_n(x)
=(-1)^{|\alpha|}f\bigl((\partial^\alpha\omega_n)(\,\cdot-x)\bigr).
\]
This sign matches \(\tau_x\varphi(y)=\varphi(y-x)\). For a regular distribution \(T_u\), evenness of the kernel identifies this construction with ordinary \(u*\omega_n\).

## Recovery of the distribution

For every \(\varphi\in\mathcal D\),
\[
T_{f_n}(\varphi)=f(\varphi*\omega_n)\longrightarrow f(\varphi).
\]
Indeed \(\varphi*\omega_n\to\varphi\) in \(\mathcal D\): supports stay in one enlarged compact set and each derivative converges uniformly. The supplement justifies interchanging the functional and integration by finite Riemann sums converging in the test-function space. Hence every distribution is a distributional limit of smooth regular distributions.

For regular \(f=T_u\), convergence strengthens to \(u*\omega_n\to u\) in \(L^1_{\mathrm{loc}}\). Differentiation is continuous in \(\mathcal D'\), so
\[
T_{\partial^\alpha f_n}\longrightarrow\partial^\alpha f.
\]
If \(u\) has weak derivative \(v=\partial^\alpha u\in L^1_{\mathrm{loc}}\), then \(\partial^\alpha(u*\omega_n)=v*\omega_n\to v\) locally in \(L^1\). Singular limits require distributional rather than integrable-density convergence.

## Examples

- \(\delta_0*\omega_n=\omega_n\): concentrating smooth unit-mass bumps converge to a point mass.
- In one dimension, \(\delta'_0*\omega_n=\omega'_n=n^2\omega'(nx)\), with positive derivative sign despite the minus sign in \(\delta'_0(\varphi)=-\varphi'(0)\).
- The average on \([-1,1]\) regularizes to \(\frac12 1_{[-1,1]}*\omega_n\), smoothing the two edges.

These distinguish approximation of an ordinary density, a singular mass and a derivative of a singular mass; a narrow smooth peak need not converge to a finite pointwise density.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Distributions.pdf`, WS 2024/25.
- Section 3, Example 2 and Lemma 3, pp. 3–4; Section 5, Lemma 5, Theorem 1 and Example 6/Figure 1, pp. 5–7; Lemmas 8 and 10, pp. 8–9.
- The derivative formula uses the sign implied by the definition of translation; the printed translation-difference sign is inconsistent.
