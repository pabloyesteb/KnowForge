---
id: tum-uq-control-variates
source: tum-numuq
parent: uq-monte-carlo
title: Optimal single and multiple control variates
type: method
caption: Preserves the target mean while minimizing variance through known-mean correlated quantities.
---

# Optimal single and multiple control variates

For a cheap control \(Z\) with known mean, define \(X^c=X+c(Z-EZ)\). For a fixed coefficient the expectation remains \(EX\), while
\[
\operatorname{Var}X^c=\operatorname{Var}X+2c\operatorname{Cov}(X,Z)+c^2\operatorname{Var}Z.
\]
When \(\operatorname{Var}Z>0\), minimization gives \(c_*=-\operatorname{Cov}(X,Z)/\operatorname{Var}Z\) and variance \(\operatorname{Var}X-\operatorname{Cov}(X,Z)^2/\operatorname{Var}Z\). Nonzero correlation gives a strict reduction; a constant control contributes nothing. For \(Ee^{U^2}\), \(U\sim U[0,1]\), the course uses \(Z=U^2\) with known mean \(1/3\).

With two controls, write \(b_i=\operatorname{Cov}(X,Z_i)\) and \(\Sigma_{ij}=\operatorname{Cov}(Z_i,Z_j)\). The variance is \(\operatorname{Var}X+2c^Tb+c^T\Sigma c\), and the stationary equations are \(\Sigma c=-b\). If \(\Delta=\operatorname{Var}Z_1\operatorname{Var}Z_2-\operatorname{Cov}(Z_1,Z_2)^2>0\),
\[
c_1=\frac{-\operatorname{Var}Z_2\,b_1+\Sigma_{12}b_2}{\Delta},\qquad
c_2=\frac{-\operatorname{Var}Z_1\,b_2+\Sigma_{12}b_1}{\Delta}.
\]
Uncorrelated controls decouple into the two scalar formulas. A singular covariance requires handling redundant/constant controls, rather than dividing by \(\Delta\). The supplied solution prints the square outside the denominator parentheses; the correct determinant squares only the cross-covariance, as shown here.

Unknown covariances and variances are estimated in pilot simulations. The unbiasedness derivation assumes fixed coefficients (or coefficients estimated independently of the final draws); reusing the same sample to fit coefficients requires separate bias analysis. Evaluation overhead must be included when comparing work savings.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §7.3.4 and Example 7.9, pp. 58–59 before ch. 8.
- `Lecture Topics and Slides/Lecture 12 (13.06.24)`, physical pp. 6–8 (printed 18–20).
- `Problem Sheets/Sheet 04 (19.06.2024)`, Problem 12; `Problem Sheets/Solution Sheet 04.pdf`, p. 1, two-control variance and stationary equations.
