---
id: tum-uq-brownian-bridge-kl
source: tum-numuq
parent: uq-discretization
title: Brownian bridge KL modes and explicit truncation bound
type: method
caption: Derives sine eigenfunctions, positive covariance and an explicit inverse-mode-count squared-error bound.
---

# Brownian bridge KL modes and explicit truncation bound

On \([0,1]\), \(c(x,y)=\min(x,y)-xy\) is the Brownian bridge covariance. Splitting its integral eigen-equation gives
\[
(1-x)\int_0^x y\phi(y)dy+x\int_x^1(1-y)\phi(y)dy=\nu\phi(x).
\]
Two differentiations imply \(\nu\phi''=-\phi\), and the endpoints give Dirichlet conditions. Nonzero eigenfunctions have \(\nu_j=(\pi j)^{-2}\) and \(\phi_j=\sqrt2\sin(j\pi x)\). Nonzero eigenvalues permit bootstrapping from the integral equation to justify the derivatives; the zero-eigenvalue case yields the zero function by almost-everywhere differentiation.

The centered Gaussian bridge has
\[
Z(x)=\sum_{j\ge1}\frac{\sqrt2}{\pi j}\sin(j\pi x)\xi_j,\qquad \xi_j\stackrel{\rm iid}{\sim}N(0,1).
\]
Its truncation satisfies
\[
E\|Z-Z_J\|_{L^2}^2=\int_0^1[\operatorname{Var}Z(x)-\operatorname{Var}Z_J(x)]dx
=\sum_{j>J}\frac1{\pi^2j^2}\le\frac1{\pi^2J},
\]
by comparison with \(\int_J^\infty t^{-2}dt\).

Positive semidefiniteness follows either from the process \(W_x-xW_1\), or analytically: write \(\min(x,y)=\int_0^1\mathbf1_{[0,x]}(t)\mathbf1_{[0,y]}(t)dt\). For \(f(t)=\sum_i a_i\mathbf1_{[0,x_i]}(t)\), the quadratic kernel form is \(\int f^2-(\int f)^2\ge0\) by Cauchy–Schwarz.

The same covariance operator is the inverse of the positive Dirichlet Laplacian \(L_D=-d^2/dx^2\) on \((0,1)\). Its weak inverse maps \(f\in L^2\) to \(u\in H_0^1\); the distributional identity \(u''=-f\) upgrades \(u\) to \(H^2\). Energy testing bounds the inverse into \(H_0^1\), and Rellich compactness makes it compact as an operator on \(L^2\). Testing two weak equations against one another proves self-adjointness; energy testing proves positive eigenvalues. Solving \(-\lambda\phi''=\phi\) gives exactly the bridge eigenpairs, so its Green kernel is \(\min(x,y)-xy\). The exercise's displayed operator map and one solution ODE omit the minus sign; the positive-Laplacian convention is required for the stated positive spectrum. The forward Laplacian is not compact: for \(u_n=\sqrt2\sin(n\pi x)/(n\pi)^2\), the sequence is bounded in its \(H^2\) domain but its images are orthonormal in \(L^2\).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 02 (09.05.2024)`, Problem 2(a)–(c) and bonus; `Problem Sheets/Solution Sheet 02.pdf`, pp. 3–6, complete ODE, tail bound and both covariance-positivity arguments.
- `Problem Sheets/Problem Sheet 03 (21.05.2024)`, Problem 1(a)–(e) and bonus; `Problem Sheets/Solution Sheet 03.pdf`, pp. 1–3, inverse-Laplacian covariance construction.
