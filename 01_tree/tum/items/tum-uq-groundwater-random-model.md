---
id: tum-uq-groundwater-random-model
source: tum-numuq
parent: uq-probability
title: Random conductivity and quantities of interest in groundwater flow
type: method
caption: "Propagates a spatial coefficient model through an elliptic PDE to pressure and transport observables."
---

# Random conductivity and quantities of interest in groundwater flow

A steady porous-medium model solves \(-\nabla\cdot(a\nabla u)=f\) in a spatial domain, with suitable boundary conditions; the standard course example uses \(u=0\) on the boundary. Here \(u\) is pressure, \(a\) conductivity and \(f\) sources or sinks. Treating conductivity as a random field makes the solution a random function \(u(x,\omega)\). Uncertainty propagates from conductivity through pressure to derived transport quantities, such as particle travel time or boundary flux.

The introductory lognormal model is \(a(x,\omega)=\exp Z(x,\omega)\), with Gaussian expansion
\[
Z(x,\omega)=z_0(x)+\sigma\sum_{m\ge1}\sqrt{\lambda_m}\,z_m(x)y_m(\omega),\qquad y_m\sim N(0,1)\text{ independently}.
\]
This incorporates spatial dependence beyond a single uncertain scalar and ensures pointwise positivity. Convergence and coefficient regularity require hypotheses developed in the random-field and PDE analysis; positivity alone does not give a deterministic uniform ellipticity constant.

Often the goal is a scalar quantity of interest \(Q(u)\), rather than every solution value. Examples are an average \(|D_0|^{-1}\int_{D_0}u(x)\,dx\), a point observation \(u(x_0)\), effective conductivity, or travel time. Point observation requires sufficient solution regularity to make it well-defined. The diagrams compare rough and smooth log-conductivity realizations and their differing flow trajectories, motivating spatial random-field models without reporting new numerical measurements.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Topics and Slides/Lecture 01 (16.04.24)`, physical pp. 26–32 (printed slides 31–37), complete groundwater diagrams, coefficient expansion, elliptic model and QoI examples.
