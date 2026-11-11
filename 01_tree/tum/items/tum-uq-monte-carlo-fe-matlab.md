---
id: tum-uq-monte-carlo-fe-matlab
source: tum-numuq
parent: uq-monte-carlo
title: Supplied Monte Carlo FEM mean and variance estimators
type: implementation
caption: Samples bounded diffusion expansions, solves each realization and accumulates nodal first and second moments.
---

# Supplied Monte Carlo FEM mean and variance estimators

`oned_MC_FEM(ne,sigma,mu,P,Q)` draws independent vectors with components uniform on \([-1,1]\). It evaluates the affine cosine diffusion with weights \(\sigma/(\pi k)^2\) at element midpoints and uses these as piecewise constant diffusion data in the linear FE solver, with unit forcing and zero reaction. Midpoint coefficient approximation is part of the implemented model discretization.

For \(Q\) solution vectors it accumulates \(S=\sum_j u_j\) and \(T=\sum_j u_j^2\), componentwise, then returns
\[
\bar u=S/Q,\qquad s_u^2=\frac{T-S^2/Q}{Q-1}.
\]
The sample variance requires \(Q>1\). This subtraction-based expression can lose precision when fluctuations are tiny relative to the mean; the files use direct sums rather than a stable online recurrence. `oned_MC_FEM` plots individual realizations; `oned_MC_FEM_plots` uses its local no-plot solver and plots the final mean and variance.

The supplied exercise uses \(ne=512,\mu=1,\sigma=4,P=10\), for which the uniform lower bound is \(1-4/6>0\). Its solution shows five realizations and mean/variance estimates with \(Q=10\) and \(10^3\). The mean is roughly symmetric and peaked centrally; variance vanishes at the fixed boundaries and has two interior lobes. The small-sample variance plot is visibly asymmetric, while the larger sample is more balanced. These supplied figures illustrate sampling variability; they do not measure a convergence rate or separate sampling, FE and coefficient-approximation errors.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 03 (21.05.2024)`, Problem 4(a)–(b); `Problem Sheets/Solution Sheet 03.pdf`, printed Problem 11, pp. 7–8, code calls and Figures 1–3.
- `Problem Sheets/oned_MC_FEM.m` and `Problem Sheets/oned_MC_FEM_plots.m`, complete functions and their solver calls.
