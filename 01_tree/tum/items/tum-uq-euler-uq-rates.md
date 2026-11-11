---
id: tum-uq-euler-uq-rates
source: tum-numuq
parent: uq-multilevel
title: Random-initial-value Euler model and supplied MLMC rate study
type: implementation
caption: Couples Euler trajectories by initial condition and compares bias, correction variance and sample cost rates.
---

# Random-initial-value Euler model and supplied MLMC rate study

The model is \(u_1'=u_1(1-u_2)\), \(u_2'=u_2(u_1-1)\), with \(u(0)=(0.5,2)^T+0.2\xi\), independent uniform coordinates \(\xi_i\in[-1,1]\), final time \(T=6\), and quantity \(Q=u_1(T)\). Supplied `DynSys.m` stores the initial vector and forward-Euler iterates \(u_{n+1}=u_n+hf(u_n)\); its allocation assumes \(T/h\) is an integer.

The exercise's deterministic bound is \(\|u(nh)-u_n\|\le h\,M_2(\omega)(e^{LT}-1)/(2L)\), for a Lipschitz constant valid over the relevant trajectories. Finite \(EM_2\) gives weak bias \(O(h)\). Using the same random initial condition for both resolutions and \(EM_2^2<\infty\) gives \(\operatorname{Var}(Q_h-Q_{2h})\lesssim h^2\). With \(T/h\) constant-cost Euler steps, cost is \(O(h^{-1})\), so the expected rates are \(\alpha=1,\beta=2,\gamma=1\). The solution's phrase “linearly in the time step size” means linearly in the number of time steps, hence inversely in \(h\).

`mlmc_complexity.m` checks deterministic error against an \(h=2^{-12}\) trajectory, times 1000 draws on geometric grids from \(h_0=2^{-3}\), estimates weak bias using 10,000 draws and supplied reference \(1.493005355935809\), then estimates coupled correction and full-solution variances using 1000 draws. Log–log `polyfit` estimates slopes; some loops use `parfor`. Its correction loop explicitly reuses each initial vector for coarse and fine evaluations. The supplied Figure 1 reports approximate slopes 1.45, 2.16 and 0.96 for weak bias, correction variance and cost; full-solution variance approaches a nonzero plateau on fine levels. Monte Carlo noise and finite-resolution effects limit interpretation of fitted slopes as exact asymptotic rates.

These are supplied scripts and a supplied example output, with acknowledgment to Bjoern Sprungk (2016), rather than personally run experiments.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Sheet 04 (19.06.2024)`, Problems 13–14; `Problem Sheets/Solution Sheet 04.pdf`, pp. 2–4, deterministic rate argument and Figure 1.
- `Problem Sheets/mlmc_matlab.zip`, complete members `DynSys.m` and `mlmc_complexity.m`.
