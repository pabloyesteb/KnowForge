---
id: tum-uq-fixed-cost-confidence
source: tum-numuq
parent: uq-multilevel
title: Fixed-work Monte Carlo confidence intervals and supplied multilevel comparison
type: method
caption: Separates sampling uncertainty from discretization bias and implements level-wise variance estimates under a fixed
  runtime target.
---

# Fixed-work Monte Carlo confidence intervals and supplied multilevel comparison

For scalar iid draws, the course uses the asymptotic interval \(\bar Q\pm2s_Q/\sqrt M\). It describes sampling uncertainty around \(EQ_h\); it does not cover discretization bias in the continuum target \(EQ\). At fixed computational work, coarse time steps allow more samples and narrower intervals but can leave substantial bias. Fine steps reduce bias while allowing fewer samples and wider intervals. Choosing the finest grid alone therefore need not minimize total error.

For independent MLMC level averages, estimate sampling variance by \(s_0^2/M_0+\sum_{\ell=1}^Ls_\ell^2/M_\ell\) and use the summed estimator plus/minus twice its square root. Do not divide this estimator variance by another total sample count. Bias of the finest resolution still lies outside that sampling interval. Approximate normal coverage requires sufficiently informative samples and is not a deterministic guarantee.

The supplied `mc_confidence.m` times single solves, then uses \(M\approx\operatorname{round}(3/C_h)\) on grids \(h=2^{-5},\ldots,2^{-10}\), forms sample variance, and plots intervals against reference \(1.493005355935809\). Runtime calibration itself costs extra and is outside its three-second production target.

`twolevel_confidence.m` first fits cost, bias and correction-variance slopes; it sets `L=2`, so despite its filename it uses **three** grids: a base and two corrections. It sets successive counts with factor \(2^{-\operatorname{round}(\beta+\gamma)/2}\), normalizes the base count using the measured costs of all coupled solves, samples level groups independently, shares the initial condition within each correction, and sums means and variance/count contributions. Counts use nearest rounding, so the target runtime is approximate, not a hard cap; no guard ensures positive adequate sample counts.

Supplied Figure 2 illustrates bias at coarse grids and broader single-level intervals at fine grids, with more comparable widths in the multilevel example. Its explanation that independent terms “increase variance” does not prove that MLMC is inherently worse at equal work; the allocation and correction variances determine that comparison. No new timing experiment is implied.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Sheet 04 (19.06.2024)`, Problem 15(a)–(c); `Problem Sheets/Solution Sheet 04.pdf`, pp. 5–6, discussion and Figure 2.
- `Problem Sheets/mlmc_matlab.zip`, complete members `mc_confidence.m` and `twolevel_confidence.m`, including calibration, sample allocation and confidence formulas.
