---
id: tum-nloa-exact-penalties
source: tum-nonlinear-optimization
parent: nloa-second-order-penalty
title: Local exact penalties and their differentiability obstruction
type: theorem
caption: "Shows that local exactness persists above a penalty threshold and explains why smooth nonnegative penalties cannot handle nonstationary constrained optima exactly."
---

# Local exact penalties and their differentiability obstruction

Let \(\pi\ge0\) be a penalty for feasible \(X\), with \(\pi=0\) on \(X\), and \(P_\alpha=f+\alpha\pi\). At a constrained local solution \(\bar x\), local exactness means \(\bar x\) also locally minimizes the unconstrained penalized objective for a finite penalty parameter.

If exactness holds at \(\widehat\alpha>0\), it holds for every \(\alpha\ge\widehat\alpha\): on the same neighborhood,
\[
P_\alpha(\bar x)=f(\bar x)=P_{\widehat\alpha}(\bar x)
\le P_{\widehat\alpha}(x)\le P_\alpha(x).
\]
Nonnegativity of \(\pi\) is needed for monotonicity with the penalty parameter.

If both \(f,\pi\) are differentiable at \(\bar x\), then \(\nabla\pi(\bar x)=0\), since \(\pi\) attains its global minimum zero there. Unconstrained stationarity of the exact penalty therefore gives
\[
0=\nabla P_{\widehat\alpha}(\bar x)=\nabla f(\bar x)+\widehat\alpha\nabla\pi(\bar x)
\quad\Longrightarrow\quad\nabla f(\bar x)=0.
\]
Thus a differentiable nonnegative penalty cannot be locally exact at a constrained solution with nonzero objective gradient. This explains a substantive role for nonsmooth exact penalties; it is not a claim that every nonsmooth penalty is exact or that smooth penalties never converge as their parameter increases.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 5.pdf`, H.5.3(a–b), p. 1; `Exercise materials/Solution Exercise Sheet 5.pdf`, Solution 5.3, p. 3.
