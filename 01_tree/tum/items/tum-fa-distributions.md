---
id: tum-fa-distributions
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Test functions and distributions as generalized functions
type: concept
caption: "Defines test-function convergence and continuous linear distributions, distinguishing integrable densities from singular point evaluations."
---

# Test functions and distributions as generalized functions

## Test-function convergence

For real-valued functions on \(\mathbb R^d\), let \(\mathcal D=C_c^\infty(\mathbb R^d)\). Convergence \(\varphi_n\to\varphi\) in \(\mathcal D\) means all derivatives converge uniformly and all supports lie in one compact set. In \(C^\infty\), only locally uniform convergence of each derivative is required. For nonzero \(\varphi\in\mathcal D\), \(n^{-1}\varphi(x/n)\to0\) in \(C^\infty\), but its expanding supports prevent convergence in \(\mathcal D\).

Differentiation is sequentially continuous on \(\mathcal D\): derivatives keep the common compact support and convergence of each further derivative is already required. Translations \(\tau_\xi\varphi(x)=\varphi(x-\xi)\) are continuous, including dependence on \(\xi\). With this sign convention,
\[
\frac{\tau_{he_j}\varphi-\varphi}{h}\longrightarrow-\partial_j\varphi
\quad\text{in }\mathcal D.
\]
The minus sign follows from the translated argument; the supplement's Example 3 prints the opposite sign.

## Generalized functions

A distribution \(f\in\mathcal D'\) is a linear, sequentially continuous functional on \(\mathcal D\). Distributional convergence is convergence of \(f_n(\varphi)\) for every test function, rather than pointwise convergence of ordinary functions. On each fixed compact support \(K\), continuity is characterized by a finite-order bound
\[
|f(\varphi)|\le M_K\sum_{|\alpha|\le m_K}\|\partial^\alpha\varphi\|_\infty,
\qquad \operatorname{supp}\varphi\subset K.
\]
The restriction to tests supported in \(K\) is essential. The supplement uses sequential convergence and does not develop the full test-function topology.

A locally integrable \(u\) gives the regular distribution
\[
T_u(\varphi)=\int_{\mathbb R^d}u\varphi.
\]
Its density is unique almost everywhere: zero pairings with every smooth compactly supported test imply \(u=0\) a.e. Thus equivalence classes, rather than pointwise values, embed injectively in \(\mathcal D'\).

The average over a measurable finite-positive-volume set \(A\) has density \(1_A/|A|\). By contrast, \(\delta_\xi(\varphi)=\varphi(\xi)\) is singular: no locally integrable density represents point evaluation. Further examples integrate directional derivatives of tests along compact smooth submanifolds against finite measures. This viewpoint models spatially weighted measurements and admits objects more singular than integrable densities.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Distributions.pdf`, Daniel Matthes, WS 2024/25.
- Sections 1–4, pp. 1–5; Lemmas 1–4, Definitions 1–3, Remarks 1–2 and Examples 1–5.
