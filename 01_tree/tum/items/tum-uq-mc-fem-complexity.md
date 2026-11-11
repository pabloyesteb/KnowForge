---
id: tum-uq-mc-fem-complexity
source: tum-numuq
parent: uq-monte-carlo
title: Monte Carlo FEM bias–variance split and balanced work
type: theorem
caption: Balances finite-element approximation bias against sampling variance to obtain tolerance-dependent cost.
---

# Monte Carlo FEM bias–variance split and balanced work

For iid \(H_0^1(D)\)-valued approximations \(u_h^{(j)}\in L^2\), estimate \(Eu\) by \(\widehat u_{h,M}=M^{-1}\sum_ju_h^{(j)}\). It is unbiased for \(Eu_h\), but generally biased for \(Eu\). Expanding around \(Eu_h\) eliminates the cross term because the sampling fluctuation is centered, giving
\[
E\|\widehat u_{h,M}-Eu\|_{H_0^1}^2
=\frac1M E\|u_h-Eu_h\|_{H_0^1}^2+\|E(u_h-u)\|_{H_0^1}^2.
\]
Independence makes off-diagonal sample inner products vanish. Jensen and centering bound this by \(M^{-1}\|u_h\|_{L^2(\Omega;H_0^1)}^2+\|u_h-u\|_{L^2(\Omega;H_0^1)}^2\).

Assume uniform-in-mesh second moments, strong error \(\|u-u_h\|_{L^2(\Omega;H_0^1)}\lesssim h^\alpha\), and per-realization cost \(C_h\lesssim h^{-\gamma}\), with \(\alpha,\gamma>0\). Taking \(M\asymp h^{-2\alpha}\) balances the two squared errors, yielding RMSE \(O(h^\alpha)\) and work \(O(h^{-2\alpha-\gamma})\). Equivalently tolerance \(\varepsilon\) costs \(O(\varepsilon^{-2-\gamma/\alpha})\). A mere upper bound \(M=O(h^{-2\alpha})\), as printed, does not ensure enough samples; a corresponding lower bound is required for the asserted error.

Per-sample work includes both coefficient generation and the FE solve. With \(N\asymp h^{-d}\), an ideal linear solver costs \(O(N)\), while dense covariance sampling can cost \(O(N^2)\) online plus \(O(N^3)\) one-off factorization. The assumed cost exponent must cover the actual online components; reusable setup is accounted separately. For \(\alpha=1,\gamma=d\), halving tolerance multiplies online work by \(2^{2+d}\). Refining the mesh alone leaves sampling error, and increasing samples alone leaves discretization bias.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §7.2, Lemma 7.2, equations (7.1)–(7.7), Assumptions 7.3–7.4 and Theorem 7.5 with proof, pp. 52–55.
- `Lecture Topics and Slides/Lecture 11 (11.06.24)`, physical pp. 7–14, Hilbert-space error split, full cost assumptions and handwritten proof.
- `Oral exam/Topics and sample questions (08.07.24)`, §7, p. 3, MC convergence and cost/error proof.
