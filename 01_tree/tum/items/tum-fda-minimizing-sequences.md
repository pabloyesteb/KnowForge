---
id: tum-fda-minimizing-sequences
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Infima, minimizers and minimizing sequences
type: concept
caption: "Separates convergence of objective values from attainment and convergence of the underlying feasible points."
---

# Infima, minimizers and minimizing sequences

For an extended-real objective \(F\) on a nonempty set \(X\), the infimum is the greatest lower bound of its values. A minimum requires a feasible point attaining that value; \(\operatorname{argmin}_X F\) denotes all such points and may be empty or contain several points. A finite infimum need not be attained, while an objective unbounded below has infimum \(-\infty\), as for \(\log x\) on \(x>0\).

If \(c=\inf_XF\) is finite, for each \(\varepsilon_n\downarrow0\) choose a feasible \(x_n\) with
\[
c\le F(x_n)\le c+\varepsilon_n.
\]
Then \(F(x_n)\to c\). This defines a minimizing sequence; constructing its terms can still be difficult computationally.

Convergence of these scalar values does not ensure convergence of the points or attainment of a minimum. For \(F(x)=1/x\) on \((0,\infty)\), \(x_n=n\) is minimizing, with values tending to zero, but the points diverge and zero is never attained. Existence arguments therefore need additional structure. In the Hilbert projection proof, the parallelogram identity makes the minimizing sequence Cauchy, completeness supplies its limit, and closedness keeps that limit feasible.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `29. April - 5. Mai/Notes All you... math week 2`, single physical page, “Infima, Minima, Minimizing Sequences” through the \(1/x\) example and projection-proof connection.
