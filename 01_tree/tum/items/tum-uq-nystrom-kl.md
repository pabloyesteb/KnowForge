---
id: tum-uq-nystrom-kl
source: tum-numuq
parent: uq-discretization
title: Nyström covariance eigenpairs and supplied MATLAB parameter studies
type: algorithm
caption: Approximates integral eigenpairs with quadrature-weighted symmetric matrices and compares covariance parameters.
---

# Nyström covariance eigenpairs and supplied MATLAB parameter studies

For quadrature nodes \(x_i\) and positive weights \(q_i\), collocating the covariance eigen-equation gives \(CQv=\nu v\), where \(C_{ik}=c(x_i,x_k)\), \(Q=\operatorname{diag}q_i\), and \(v_i\) approximates \(\phi(x_i)\). Although \(CQ\) is generally nonsymmetric, setting \(D=Q^{1/2}\) gives the equivalent symmetric problem \(DCD\,u=\nu u\), \(v=D^{-1}u\). Normalize in the quadrature norm \(\sum_iq_iv_i^2=1\), and retain leading eigenpairs. This approximates both integration and eigenfunctions; it is distinct from truncating an exact KL expansion.

The supplied `kle_bbridge.m` and `kle_gauss.m` implement this transformation on \([0,1]\) using a uniform mesh, trapezoidal endpoint weights \(h/2\), interior weights \(h\), dense `eig`, descending real eigenvalue sorting, inverse weight transformation and weighted normalization. The bridge script compares eigenvalues to \((\pi j)^{-2}\) by relative error and plots its first three modes against \(\sqrt2\sin(j\pi x)\); eigenvector sign is arbitrary. The source task mixes \(P\) nodes with indices \(0,\ldots,P\); the scripts consistently use \(1/h+1\) nodes.

`kle_gauss_plots.m` sets \(h=1/128\), retains 50 modes, varies \(\sigma=0.1,1,2\) at \(\ell=1\), then varies \(\ell=0.01,0.1,1\) at \(\sigma=1\). Its Gaussian kernel is \(\sigma^2e^{-(x-y)^2/\ell^2}\). Supplied solution plots show variance scaling and much later spectral decay for small correlation lengths, motivating more KL terms. Eigenvalues near machine precision in these plots do not establish a resolved analytic tail. These are supplied implementations and figures; no personal execution or measured solver accuracy is implied.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 02 (09.05.2024)`, printed Problem 7(a)–(c); `Problem Sheets/Solution Sheet 02.pdf`, pp. 6–8, discrete eigenproblem and Gaussian parameter-study Figure 2.
- `Problem Sheets/kle_bbridge.m`, complete function including analytic comparisons; `Problem Sheets/kle_gauss.m`, complete function; `Problem Sheets/kle_gauss_plots.m`, complete script.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Remark 4.29, p. 39.
