---
id: tum-uq-mean-based-preconditioner
source: tum-numuq
parent: uq-stochastic-galerkin
title: Mean-based stochastic Galerkin preconditioning
type: theorem
caption: Bounds preconditioned eigenvalues by diffusion variation relative to its positive constant mean.
---

# Mean-based stochastic Galerkin preconditioning

For orthonormal parameter polynomials, the mean-based matrix is \(P=I\otimes A_0\). Assume \(a_0\equiv\mu_a>0\), parameter support \([-1,1]^M\), and positive coefficient bounds \(\widetilde a_{\min},\widetilde a_{\max}\). Comparing the weak forms gives
\[
\frac{\widetilde a_{\min}}{\mu_a}v^TPv\le v^TAv\le\frac{\widetilde a_{\max}}{\mu_a}v^TPv.
\]
Since \(P^{-1}A\) is similar to the symmetric positive definite \(P^{-1/2}AP^{-1/2}\), Rayleigh quotients bound its spectrum in the same interval.

With \(\tau=\sum_{m=1}^M\|a_m\|_\infty\), the affine coefficient lies between \(\mu_a-\tau\) and \(\mu_a+\tau\), giving interval \([1-\tau/\mu_a,1+\tau/\mu_a]\). This yields a positive useful condition-number bound \((\mu_a+\tau)/(\mu_a-\tau)\) only if \(\tau<\mu_a\); positivity of the actual coefficient alone does not make this looser lower bound positive. The bounds are independent of spatial mesh and polynomial degree. Uniformity in input dimension additionally requires a uniformly bounded summable coefficient-amplitude sequence and a positive margin; it does not follow just by taking \(M\to\infty\), as the solution's prose suggests.

For the cosine model, \(\tau\le\sigma/6\), so \(\mu_a>\sigma/6\) supplies such a dimension-uniform margin. Supplied `SG_prec.m` reshapes a vector into \(J\times Q\), solves \(A_0W=V\) for all columns, and vectorizes. This applies \(P^{-1}\) without forming a Kronecker matrix; the file uses a direct backslash solve rather than supplying an explicit reusable factorization.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Sheet 05 (02.07.2023)`, Problem 18(a)–(b); `Problem Sheets/Solution Sheet 05.pdf`, pp. 4–5, form bounds and similarity/Rayleigh-quotient proof.
- `Problem Sheets/SG_matlab.zip`, complete `SG_prec.m` and preconditioner handle in `oned_SG_FEM.m`.
