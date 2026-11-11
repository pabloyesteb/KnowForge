---
id: tum-co-expensive-flow-arc
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Exclusion of a prohibitively expensive flow arc
type: theorem
caption: "Combines residual circulation decomposition with a simple-cycle cost bound to exclude an avoidable arc from every optimum."
---

# Exclusion of a prohibitively expensive flow arc

Let \(d\) be an arc with \(c(d)>(n-1)\max_{e\ne d}|c(e)|\), and suppose some feasible \(b\)-flow avoids \(d\). Then every minimum-cost feasible flow avoids it. If an optimum \(f'\) used \(d\) positively, the residual difference toward an avoiding feasible flow would be a nonnegative circulation carrying positive flow on the reverse of \(d\). Decompose it into simple residual cycles and choose one containing that reverse arc. Such a cycle has at most \(n\) arcs, with at most \(n-1\) others, each of cost magnitude at most the displayed bound. Its cost is strictly negative, contradicting residual optimality. The strict inequality matters: equality can leave zero-cost cycles and multiple optima. The existence of an avoiding feasible flow also matters; a large price cannot override required balances. The source's final cost line contains stray symbols, but the reverse-arc and cycle-length argument provides the stated bound.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Lucas Harder.pdf`, p. 1, complete expensive-arc statement and residual-cycle proof.
