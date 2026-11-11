---
id: tum-uq-doob-dynkin
source: tum-numuq
parent: uq-probability
title: Doob–Dynkin measurable dependence on random inputs
type: theorem
caption: "Characterizes when an observable can be represented as a measurable function of a specified random input."
---

# Doob–Dynkin measurable dependence on random inputs

In the course's Hilbert-valued setting, an observable \(X\) is measurable with respect to \(\sigma(Y)\) precisely when it can be written \(X=h\circ Y\) for a measurable mapping \(h\) on the input space. The statement is used with the usual separable Hilbert/Borel targets of the PDE setting; general measurable target spaces require care with factorization hypotheses. For completed sigma-algebras, one normally interprets a corresponding representation up to almost-sure equality.

This converts a measurability claim into explicit dependence on the chosen random inputs. Classical applications include representing conditional expectations as functions of observed variables. For a PDE whose coefficient is specified by \((X_1,\ldots,X_n)\), proving that its solution is measurable with respect to those inputs justifies a parameter-to-solution representation \(u=u(X_1,\ldots,X_n)\). It does not itself prove PDE well-posedness or that measurability; those are prerequisites. The notes state the lemma and refer its proof externally.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.2, Lemma 2.39 and both applications, p. 9.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical p. 8 (printed 22), corresponding definitions and statements.
