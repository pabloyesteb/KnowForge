---
id: tum-nloa-logarithmic-barrier
source: tum-nonlinear-optimization
parent: nloa-sqp-barrier
title: Logarithmic barrier continuation and convergence of global subproblem solutions
type: algorithm
caption: "Proves monotonic comparisons and optimal accumulation points for globally solved barrier subproblems when the strict interior is dense in the feasible set."
---

# Logarithmic barrier continuation and convergence of global subproblem solutions

Let \(f,g_i\) be continuous, \(X=\{x:g(x)\le0\}\), and let the strict interior \(X_\circ=\{x:g(x)<0\}\) be nonempty. Define
\[
\beta(x)=-\sum_i\log(-g_i(x)),\qquad
B_\tau(x)=f(x)+\tau\beta(x)\quad(x\in X_\circ).
\]
Choose \(\tau_1>0\); at each iteration compute a **global minimizer** \(x_k\) of \(B_{\tau_k}\) on its domain, then decrease \(\tau_{k+1}\in(0,\tau_k)\). Assume the subproblem minimizers exist and \(\tau_k\downarrow0\). This is an idealized continuation algorithm, not a supplied numerical interior-point implementation.

## Monotonic comparisons

Optimality at the two consecutive parameters gives
\[
f(x_k)+\tau_k\beta(x_k)\le f(x_{k+1})+\tau_k\beta(x_{k+1}),
\]
\[
f(x_{k+1})+\tau_{k+1}\beta(x_{k+1})
\le f(x_k)+\tau_{k+1}\beta(x_k).
\]
Adding proves \(\beta(x_k)\le\beta(x_{k+1})\). Inserting this into the second inequality proves \(f(x_{k+1})\le f(x_k)\). No assumption \(\beta\ge0\) is needed; the logarithmic sum may be negative.

## Accumulation points and the closure hypothesis

Assume **\(\overline{X_\circ}=X\)**. Every accumulation point \(\bar x\) is feasible by continuity and is a global solution of the original problem; moreover
\[
f(x_k)\to f(\bar x),\qquad B_{\tau_k}(x_k)\to f(\bar x).
\]
For any fixed interior \(y\), monotonicity of \(\beta\) and global subproblem optimality bound
\[
f(x_k)+\tau_k\beta(x_1)\le B_{\tau_k}(x_k)
\le f(y)+\tau_k\beta(y).
\]
Monotone objective values converge to their accumulation-point value. The displayed comparison excludes any interior point with smaller objective; density of the strict interior extends that exclusion to every feasible point. Taking interior points arbitrarily close in objective to the optimum and using the same bounds gives convergence of barrier values.

The closure condition allows feasible boundary minimizers; it does not require \(X_\circ=X\). Existence of an accumulation point is not proved, nor are rates or guarantees for approximate/local subproblem solutions.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 7.pdf`, T.7.4 and Algorithm 1, p. 2; `Exercise materials/Solution Exercise Sheet 7.pdf`, Solution 7.4, pp. 5–6. The original hypothesis has an overbar on \(X_\circ\), which is essential to the theorem.
