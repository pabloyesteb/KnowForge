---
id: tum-nloa-elastic-sqp
source: tum-nonlinear-optimization
parent: nloa-sqp-barrier
title: Elastic SQP feasibility restoration and equivalent l1 model penalties
type: method
---

# Elastic SQP feasibility restoration and equivalent l1 model penalties

Let \(q_k(s)=\nabla f(x_k)^Ts+\tfrac12s^TH_ks\), \(r_g(s)=g(x_k)+\nabla g(x_k)^Ts\), and \(r_h(s)=h(x_k)+\nabla h(x_k)^Ts\). The elastic model with \(\rho>0\) is
\[
\min_{s,v,w_+,w_-}q_k(s)+\rho\mathbf1^Tv+\rho\mathbf1^T(w_++w_-),
\]
\[
r_g(s)-v\le0,\qquad r_h(s)-w_++w_-=0,\qquad v,w_+,w_-\ge0.
\]
It is always feasible: set \(s=0\), \(v=(g(x_k))_+\), \(w_+=(h(x_k))_+\), \(w_-=(-h(x_k))_+\). This relaxes incompatible linearized constraints; it does not itself guarantee a bounded objective or a global minimizer for arbitrary \(H_k\).

## Eliminating violation variables

For fixed \(s\), the least-cost choices are
\[
v=(r_g(s))_+,\quad w_+=(r_h(s))_+,\quad w_-=(-r_h(s))_+.
\]
Feasibility alone does **not** enforce these minima: the two equality slacks can both contain a common positive excess. At an optimum, \(\rho>0\) removes all such excess, and \((a)_++(-a)_+=|a|\). Consequently the reduced problem is
\[
\min_s q_k(s)+\rho\sum_i(r_{g,i}(s))_+
+\rho\sum_j|r_{h,j}(s)|.
\]
A global solution of either formulation gives one of the other by these formulas. For any feasible elastic tuple, its slack cost is at least this reduced violation cost; that inequality proves the reverse comparison without presuming minimal slacks for arbitrary feasible points.

For \(f=-x_1-x_2\), \(g=-x\), \(h=x_1^2+x_2^2-1\), \(H_k=I\), \(x_k=(-1/2,-1/2)\), the explicit model is
\[
\min -s_1-s_2+\tfrac12(s_1^2+s_2^2)+\rho(v_1+v_2+w_++w_-),
\]
subject to \(1/2-s_i-v_i\le0\), \(-1/2-s_1-s_2-w_++w_-=0\), and nonnegative violation variables. The ordinary linearized problem was infeasible; the elastic model has the constructive feasible choice above. The penalty is on model violations, not a claim of exact feasibility for every returned nonlinear iterate.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 7.pdf`, H.7.1, p. 1, T.7.3, p. 2; `Exercise materials/Solution Exercise Sheet 7.pdf`, Solutions 7.1 and 7.3, pp. 1–2, 4. The full elastic formulation is restated in the supplied solutions despite the missing lecture Eq. (18).
