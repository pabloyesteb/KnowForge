---
id: tum-nloa-second-order-qualification
source: tum-nonlinear-optimization
parent: nloa-second-order-penalty
title: Why second-order necessity requires an appropriate curve qualification
type: method
---

# Why second-order necessity requires an appropriate curve qualification

Consider
\[
\min\tfrac12(x_1^2+x_2^2),\qquad g(x)=x_1^4-x_2^2\le0.
\]
The origin is the unique global minimizer, even without constraints. At zero, both objective and constraint gradients vanish, so every \(\lambda\ge0\) gives a KKT tuple. The sheet's cones \(T_a,T_+,T_l\) all equal \(\mathbb R^2\) there, because the active gradient vanishes. Equality of these first-order cones does not supply the required second-order curve condition.

For \(d=(0,1)^T\), the stated CQ2 would require a \(C^2\) arc \(\gamma\) with \(\gamma(0)=0\), \(\gamma'(0)=d\), and \(g(\gamma(t))=0\) for nonnegative small \(t\). But boundary equality implies \(|\gamma_2(t)|=\gamma_1(t)^2\). Differentiability and \(\gamma_1(0)=0\) give \(\gamma_1(t)=O(t)\), hence \(\gamma_2(t)/t\to0\), contradicting \(\gamma'_2(0)=1\). Thus the required arc cannot exist. This argument avoids assuming that the sign of the boundary branch stays fixed.

At multiplier \(\lambda=1\),
\[
\nabla_{xx}^2L(0,1)=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
which is not positive semidefinite on \(T_+=\mathbb R^2\). This does not contradict constrained minimality: the qualification needed for that multiplier-dependent second-order necessary condition fails. In particular first-order qualification information cannot be substituted for the specified CQ2 arc hypothesis. The example establishes this obstruction without requiring the unavailable lecture's complete CQ2 formulation.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 5.pdf`, H.5.2(a–e), p. 1; `Exercise materials/Solution Exercise Sheet 5.pdf`, Solution 5.2, pp. 1–2.
