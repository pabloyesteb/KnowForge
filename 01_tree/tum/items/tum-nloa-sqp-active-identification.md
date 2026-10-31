---
id: tum-nloa-sqp-active-identification
source: tum-nonlinear-optimization
parent: nloa-sqp-barrier
title: Finite identification of the limiting active set in SQP
type: theorem
caption: "Proves eventual identification of the limiting QP active set under convergent SQP triples, positive step-size bounds and strict complementarity."
---

# Finite identification of the limiting active set in SQP

Assume a globalized SQP sequence \((x_k,\lambda_k,\mu_k)\) converges to KKT triple \((\bar x,\bar\lambda,\bar\mu)\), with \(C^2\) data, QP KKT multipliers chosen as \((\lambda_{k+1},\mu_{k+1})\), and
\[
x_{k+1}=x_k+\sigma_ks_k,\qquad0<\bar\sigma\le\sigma_k\le1.
\]
Then \(s_k=(x_{k+1}-x_k)/\sigma_k\to0\). A vanishing step-size sequence would not justify this inference from convergence of \(x_k\) alone.

Define
\[
A_{QP}(s_k)=\{i:g_i(x_k)+\nabla g_i(x_k)^Ts_k=0\}.
\]
For any inactive limiting inequality, \(g_i(\bar x)<0\), its model value tends to that same negative number. Hence eventually \(A_{QP}(s_k)\subset A(\bar x)\). QP complementarity also gives
\[
\lambda_{k+1}^T[g(x_k)+\nabla g(x_k)^Ts_k]=0.
\]
If strict complementarity holds at the limiting triple, each \(i\in A(\bar x)\) has \(\bar\lambda_i>0\), and thus \(\lambda_{k+1,i}>0\) for all large \(k\). With nonpositive model constraint values, complementarity forces each such value to be zero. Therefore eventually
\[
A_{QP}(s_k)=A(\bar x).
\]
This is conditional finite identification of the QP active set. It does not prove that the nonlinear iterates lie exactly on the limiting active surfaces, or establish global convergence of an arbitrary SQP implementation.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 6.pdf`, T.6.3(a–d), p. 2; `Exercise materials/Solution Exercise Sheet 6.pdf`, Solution 6.3, pp. 2–3.
