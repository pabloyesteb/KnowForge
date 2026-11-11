---
id: tum-uq-richardson-multilevel
source: tum-numuq
parent: uq-multilevel
title: Richardson combinations in multilevel model hierarchies
type: method
caption: Cancels leading parametric discretization terms and combines extrapolated differences with multilevel sampling.
---

# Richardson combinations in multilevel model hierarchies

The supplement assumes a pathwise asymptotic hierarchy \(Z_\ell=Z+\sum_jc_j(\omega)2^{-\ell\gamma^j}+O(2^{-\ell\gamma^q})\), with ordered rates and sufficiently integrable remainder for the stated mean/variance bounds. Richardson combinations of adjacent models cancel leading powers to obtain vectors \(v^{k,q}\) with improved bias. The slides state the asymptotic form but do not supply a construction of all extrapolation weights or a proof of the required remainder integrability.

Telescope extrapolated vectors through group coefficients \(v^{k,q}-v^{k-1,q}\), sampling each group with common inputs. The resulting estimator has target \((v^{L,q})^T\mu\). More general \(\alpha=\sum_kg_kv^{k,q}\) uses the weighted group differences \(g_k(v^{k,q}-v^{k-1,q})\). The supplement identifies its \(q=2\) convention with ordinary MLMC.

Under the asserted asymptotic-expansion conditions, Theorem 4 gives bias \(O(2^{-k\gamma^q})\), correction variance \(O(2^{-2k\gamma^q})\), and the model-group cost rate. This improves the rates used in multilevel allocation when the expansion is available. The stated SAOB comparison can inherit the resulting work bound for the same bias vector; it does not make extrapolation valid for arbitrary nonsmooth quantities merely because BLUE weights can be computed.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Slides on Multilevel BLUE (27.06.24)`, physical pp. 26–28 (printed 25–27), asymptotic hierarchy, Richardson estimators and Theorem 4; `Lecture Topics and Slides/Lecture 15 (27.06.24)`, corresponding pages.
