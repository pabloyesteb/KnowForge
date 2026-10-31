---
id: tum-fda-taylor-expansions
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Taylor expansions with little-o and intermediate-point remainders
type: theorem
caption: "Distinguishes local error order from exact intermediate-point formulas in scalar and multivariable Taylor expansions."
---

# Taylor expansions with little-o and intermediate-point remainders

The notation \(r(t)=o(t^p)\) as \(t\to0\) means \(r(t)/t^p\to0\). For example \(t^3=o(t^2)\) and \(o(t)\), while \(t^2=o(t)\). A first-order scalar expansion of a differentiable function is \(f(x+t)=f(x)+f'(x)t+o(t)\); for \(C^2\) functions it extends by \(f''(x)t^2/2+o(t^2)\).

For \(f\in C^2\) on an open neighborhood of \(x\in\mathbb R^n\), the vector form is
\[
f(x+h)=f(x)+\nabla f(x)^Th+\tfrac12h^T\nabla^2 f(x)h+o(\|h\|_2^2).
\]
The Hessian collects second partial derivatives and is symmetric under the stated continuous-second-derivative hypothesis. Its contribution is a scalar quadratic form, not a Hessian multiplied by the scalar \(\langle h,h\rangle\).

On a segment in the domain, the first-order mean-value formula instead gives \(f(x+h)=f(x)+\nabla f(x+\tau h)^Th\) for some \(0<\tau<1\). The second-order version gives
\[
f(x+h)=f(x)+\nabla f(x)^Th+\tfrac12h^T\nabla^2f(x+\tau h)h
\]
for some such \(\tau\). These are exact equalities but the intermediate point is unspecified and may change with the displacement. They follow by applying scalar Taylor formulas to the line restriction \(t\mapsto f(x+th)\). The local little-o formula evaluates derivatives at the base point and retains a remainder instead.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, “Taylor Expansions (Ex. 10.1)”, little-o examples, scalar and multidimensional mean-value formulas, Hessian example and second-order quadratic forms.
