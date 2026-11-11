---
id: tum-uq-blue-pde-comparison
source: tum-numuq
parent: uq-multilevel
title: Supplied MLBLUE and Richardson comparison for a lognormal elliptic model
type: experiment
caption: Compares estimator work for a local-average PDE output under physical and artificial model cost rates.
---

# Supplied MLBLUE and Richardson comparison for a lognormal elliptic model

The supplement's experiment solves \(-\operatorname{div}(a\nabla y)=1\) on \(D=(0,1)^2\) with zero boundary data and \(a=e^\kappa\). The centered Gaussian field \(\kappa\) has Whittle–Matérn smoothness \(3/2\), variance one and correlation length 0.5. Its output is the average of \(y\) over \(D_{\rm obs}=(3/4,7/8)\times(7/8,1)\).

Six linear-FE models use uniform mesh refinement; the supplied comparison assigns cost exponent two and estimates their covariance with \(10^5\) pilot samples. Work-versus-RMSE plots compare Monte Carlo, MLMC, MFMC, restricted/full SAOB and Richardson variants for the ordinary finest-level bias vector and a higher-order Richardson vector. A second comparison artificially changes the cost exponent to six. The plots distinguish fractional-sample SAOB(*) from feasible sample allocations, showing why continuous relaxations and integer counts can differ at small tolerances.

The supplement identifies SAOB and third-order Richardson variants as attaining the favorable complexity for the higher-order target in its artificial-cost example. Its summary reports about 50% computational-cost reduction versus standard MLMC for this scalar PDE output. This is a source-reported example claim, not a universal speedup; pilot covariance cost is excluded from the allocation budget. No experiment code or raw numerical measurements accompany these slides, so the figures and stated setup are the available evidence. The supplement attributes this work to Daniel Schaden's TUM PhD work (2017–2021).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Slides on Multilevel BLUE (27.06.24)`, physical p. 2 (acknowledgment), physical pp. 30–32 (printed 29–31), PDE definition and all four work plots; physical pp. 34–37, conclusions and references.
- `Lecture Topics and Slides/Lecture 15 (27.06.24)`, corresponding physical pages with annotations, including cost and covariance-pilot parameters.
