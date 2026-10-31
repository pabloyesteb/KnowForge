---
id: tum-nloa-minimizer-existence
source: tum-nonlinear-optimization
parent: nloa-existence-geometry
title: Existence of constrained minimizers and the distinct roles of convexity
type: theorem
caption: "Uses compact sublevel sets to prove attainment and distinguishes strict-convexity uniqueness from strong-convexity coercivity."
---

# Existence of constrained minimizers and the distinct roles of convexity

## Compactness from coercivity

Let nonempty \(X\subset\mathbb R^n\) be closed and \(f:X\to\mathbb R\) continuous. If \(f(x)\to+\infty\) as \(x\in X\), \(\|x\|\to\infty\), then \(f\) attains a global minimum. Fix \(y\in X\); its sublevel set \(N_y=\{x\in X:f(x)\le f(y)\}\) is closed by continuity and bounded by coercivity. It is nonempty and compact. Minimizing over \(N_y\) suffices, since points outside it cannot improve on \(y\).

For compact nonempty \(X\), continuity alone suffices by Weierstrass. A condition concerning divergent sequences inside a bounded \(X\) is vacuous and adds no existence guarantee beyond compactness.

## What convexity does and does not supply

- Coercivity without closedness is insufficient: \(X=(0,\infty)\), \(f(x)=x\), has unattained infimum zero.
- Convex feasible set and convex objective alone are insufficient: \(e^x\) on \(\mathbb R\) has unattained infimum zero.
- The same example is strictly convex on a closed convex set. Strict convexity supplies uniqueness **if a minimizer exists**, not existence on an unbounded domain.

For nonempty closed convex \(X\), a continuous strongly convex objective does attain a unique minimizer. The sheet's convention is: for some \(\mu>0\),
\[
f(\lambda x+(1-\lambda)y)+\mu\lambda(1-\lambda)\|x-y\|^2
\le\lambda f(x)+(1-\lambda)f(y).
\]
To see coercivity without differentiability, fix \(y\in X\) and let \(r=\|x-y\|>1\). Convexity puts \(z=y+(x-y)/r\) in \(X\). The continuous function has a finite lower bound \(m\) on the compact unit-sphere intersection with \(X\) whenever such \(x\) exists. Applying strong convexity with \(\lambda=1/r\) and rearranging yields
\[
f(x)\ge f(y)+r[m-f(y)]+\mu(r^2-r).
\]
The quadratic term dominates the linear terms, proving coercivity along unbounded feasible sequences. The preceding existence argument applies, and strict convexity excludes two distinct minimizers by their midpoint.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`, Winter Term 2024/25.
- `Exercise materials/Exercise Sheet 1.pdf`, T.1.1(a–f), p. 1.
- `Exercise materials/Solution Exercise Sheet 1.pdf`, Solution 1.1, pp. 1–2.
