---
id: tum-uq-linear-fe-matlab
source: tum-numuq
parent: uq-pde
title: Supplied one-dimensional linear finite-element assembly
type: implementation
caption: Assembles diffusion, reaction and load contributions and solves interior degrees of freedom with homogeneous boundary
  data.
---

# Supplied one-dimensional linear finite-element assembly

The supplied `oned_linear_FEM(ne,p,q,f)` solves \(-(pu')'+qu=f\) on \((0,1)\) with zero endpoint values, uniform mesh \(h=1/ne\), and piecewise constant element data. For each element, its helper constructs
\[
K_e=\frac{p_e}{h}\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\quad
M_e=\frac{q_eh}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad
b_e=\frac{f_eh}{2}\binom11.
\]
Connectivity scatters these arrays into sparse global matrices and a global load vector. Deleting endpoint rows and columns imposes homogeneous Dirichlet data; the code solves \((K+M)u_{\rm int}=b\), restores zero boundary entries, and plots the result. It returns the solution, system, load, diffusion and weighted mass matrices.

The plotting Monte Carlo wrapper includes a local `oned_linear_FEM_noplot` with the same assembly and boundary treatment. This is supplied course code with an attribution comment to Shardlow's introductory computational-SPDE materials; it does not establish a personal implementation. Positivity/coercivity depends on input coefficients rather than an explicit guard in the file.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/oned_linear_FEM.m`, complete function and `get_elt_arrays` helper.
- `Problem Sheets/oned_MC_FEM_plots.m`, local `oned_linear_FEM_noplot` and element-array helper.
- `Problem Sheets/Problem Sheet 03 (21.05.2024)`, Problem 4(a), deterministic FE component description.
