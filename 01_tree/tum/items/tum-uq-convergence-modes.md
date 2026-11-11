---
id: tum-uq-convergence-modes
source: tum-numuq
parent: uq-probability
title: Modes of convergence for Hilbert-valued random approximations
type: concept
caption: "Separates pathwise, probabilistic, moment and distributional convergence and records their implications."
---

# Modes of convergence for Hilbert-valued random approximations

For Hilbert-valued variables, almost-sure convergence means \(\|X_n(\omega)-X(\omega)\|_H\to0\) outside one null set. Convergence in probability means \(P(\|X_n-X\|_H>\varepsilon)\to0\) for each fixed \(\varepsilon>0\). Convergence in \(p\)-th mean means \(E\|X_n-X\|_H^p\to0\). Distributional convergence tests \(E[\phi(X_n)]\to E[\phi(X)]\) for all bounded continuous scalar \(\phi\).

On a probability space, convergence in \(q\)-th mean for \(q>p\) implies convergence in \(p\)-th mean, which implies convergence in probability and hence in distribution. Almost-sure convergence also implies convergence in probability. The two routes to convergence in probability should not be conflated: almost-sure convergence alone supplies no moment-integrability bound, while convergence in a fixed moment does not by itself give almost-sure convergence of the entire sequence. These qualitative definitions do not specify a rate; moment tail bounds and summability provide that extra information.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.4, Definition 2.52 and implication list, pp. 11–12.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical pp. 17–18 (printed 31–32), convergence definitions.
