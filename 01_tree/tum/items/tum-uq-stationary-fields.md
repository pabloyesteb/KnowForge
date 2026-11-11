---
id: tum-uq-stationary-fields
source: tum-numuq
parent: uq-random-fields
title: Strict and weak stationarity of random fields
type: concept
caption: Distinguishes translation invariance of full field laws from translation invariance of second moments.
---

# Strict and weak stationarity of random fields

Strict stationarity means that every finite-dimensional law is unchanged when all its spatial arguments are shifted by the same vector, whenever both the original and translated points lie in the domain. Weak stationarity requires second-order integrability, a constant mean and a covariance of lag form \(c(x,y)=\widetilde c(x-y)\).

Strict stationarity implies weak stationarity for second-order fields, by taking expectations and pairwise covariances of the invariant laws. Weak stationarity need not imply strict stationarity for general fields: equal means and covariances do not specify their higher-dimensional laws. For a Gaussian field the implication reverses, because every finite Gaussian law is completely determined by those means and covariances. A radial covariance \(\widetilde c(\|x-y\|)\) is a particular lag-dependent model.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §3.4, Definitions 3.20–3.21 and Remark 3.22, p. 23.
- `Lecture Topics and Slides/Lecture 05 (30.04.24)`, stationary-field definitions and Gaussian equivalence.
