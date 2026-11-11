---
id: tum-uq-sg-pcg-comparison
source: tum-numuq
parent: uq-stochastic-galerkin
title: Supplied stochastic Galerkin PCG driver and reported convergence study
type: implementation
caption: Solves a tensor system without assembly, extracts moments, and compares polynomial accuracy and preconditioning.
---

# Supplied stochastic Galerkin PCG driver and reported convergence study

`oned_SG_FEM.m` obtains spatial and total-degree Legendre factors, forms a load with only the constant stochastic block populated, and calls matrix-free PCG with \(I\otimes A_0\) preconditioning, tolerance \(10^{-6}\) and 1000-iteration maximum. It records MATLAB's `flag`, relative residual and history internally, but prints only the iteration count and does not stop moment extraction on a failure flag. Reshaping the returned coefficients and restoring zero boundary rows gives mean from the first column and pointwise variance from squared nonconstant columns.

`oned_SG_FEM_noprec.m` uses the same operator with no preconditioner. `oned_SG_FEM_plots.m` plots moments. `oned_SG_FEM_error.m` computes a same-mesh reference with degree `kmax+4`, solves degrees 1 through `kmax`, and plots the Euclidean norm of the mean-vector differences. Its comment says degree six, but with the supplied `kmax=4` call the actual reference is degree eight. This is a discrete nodal norm and polynomial reference, not a spatial continuum error norm.

The supplied Sheet 5 solution calls \((ne,\sigma,\mu,P,k)=(512,4,1,10,3)\) for mean/variance plots, and uses \(ne=32,P=6,k=1,\ldots,4\) against degree eight for mean error. Its plotted errors drop from about \(4\times10^{-6}\) to \(10^{-9}\), with a symmetric mean and two interior variance lobes. At \(ne=32,P=6,k=4\), it reports six PCG iterations versus 86 unpreconditioned iterations, increasing to 170 and 340 at 64 and 128 elements without preconditioning. The text labels the latter counts as “h=64” and “h=128”; they are element counts, not mesh widths.

These are source-reported figures and iteration counts, not a new execution. The supplied `A_mats` frequency offset means their SG/MC comparison cannot be assumed to use identical coefficients. The package includes reused MC and linear-FE files; its `oned_MC_FEM.m` drops `hold on` and adds a closing `end`, while its `oned_linear_FEM.m` disables plotting. Those changes leave the sampled numerical model and FE algebra otherwise unchanged; the MC plot wrapper is identical to the standalone file.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/SG_matlab.zip`, complete `oned_SG_FEM.m`, `oned_SG_FEM_noprec.m`, `oned_SG_FEM_plots.m`, `oned_SG_FEM_error.m`; reused `oned_MC_FEM.m`, `oned_MC_FEM_plots.m` and `oned_linear_FEM.m`.
- `Problem Sheets/Sheet 05 (02.07.2023)`, Problem 19(a)–(d); `Problem Sheets/Solution Sheet 05.pdf`, pp. 5–7, full study specification, Figures 1–2 and iteration counts.
