---
id: tum-fda-linear-program-dual
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Lagrange dual of an inequality-form linear program
type: method
caption: "Resolves the dual function of a linear objective over componentwise inequalities by testing unbounded primal directions."
---

# Lagrange dual of an inequality-form linear program

Consider \(\inf\{c^Tx:Ax\le b,\ x\in\mathbb R^n\}\), where \(A\in\mathbb R^{m\times n}\). For nonnegative multipliers \(\lambda\in\mathbb R^m\), the Lagrangian is
\[
L(x,\lambda)=c^Tx+\lambda^T(Ax-b)
=(c+A^T\lambda)^Tx-\lambda^Tb.
\]
Taking the infimum over unrestricted \(x\) resolves the dual function completely:
\[
g(\lambda)=\begin{cases}-b^T\lambda&A^T\lambda+c=0,\\-\infty&\text{otherwise}.\end{cases}
\]
When the linear coefficient is nonzero, choosing \(x=-t(c+A^T\lambda)\) sends the value to minus infinity. The dual problem is therefore
\[
\sup_{\lambda\ge0,\ A^T\lambda+c=0}(-b^T\lambda).
\]
The sign of the equality and objective follows from using \(Ax-b\le0\) in the primal Lagrangian. On a feasible primal point, \(L(x,\lambda)\le c^Tx\), so each finite dual value is a lower bound on the primal minimum. The assessment derives this dual; it does not establish a numerical solver or a separate strong-duality argument. Its last handwritten rewrite minimizes \(b^T\lambda\), which selects equivalent optimizers when attained, but its optimum is the negative of the displayed dual maximum and must not be equated numerically to it.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 3(b–c), p. 8, Lagrangian, resolved infimum and final dual sign convention.
