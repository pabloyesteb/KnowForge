---
id: tum-uq-gaussian-sampling-matlab
source: tum-numuq
parent: uq-discretization
title: MATLAB spectral sampling of Gaussian-covariance processes
type: implementation
caption: Builds grid covariance square roots and compares supplied process realizations across three correlation lengths.
---

# MATLAB spectral sampling of Gaussian-covariance processes

The supplied `sample1D.m` constructs the 129 points \(x_j=j/128\), their pairwise distance matrix, and Gaussian covariance matrices \(\exp[-(R/\ell)^2]\) for \(\ell=0.01,0.1,1\). It uses `eig`, forms \(V=U\sqrt D\), multiplies by a standard normal vector, and repeats with a second vector. Within each repetition, the same normal vector drives all three correlation lengths, coupling the comparisons. Each covariance still has its intended marginal sampling construction.

The script plots the real parts of two realizations per correlation length. The supplied solution figure illustrates the increasing spatial scale of variation as \(\ell\) increases. The solution recommends spectral factorization because Cholesky can fail numerically for the finely sampled smooth Gaussian covariance at large correlation length. Positive definiteness in exact arithmetic is distinct from severe numerical ill-conditioning: tiny negative computed eigenvalues may also make the script's square root complex. Taking `real` for plotting is the script's behavior, not a general validated repair for an indefinite covariance. The supplied file contains no explicit eigenvalue tolerance or covariance-error check.

This is course-provided MATLAB material; the evidence establishes its implementation and supplied plots, not a personally performed experiment.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 02 (09.05.2024)`, Problem 1(a)–(b); `Problem Sheets/Solution Sheet 02.pdf`, pp. 1–2, solution and Figure 1.
- `Problem Sheets/sample1D.m`, complete script, covariance assembly, eigendecomposition, shared draws and plotting.
