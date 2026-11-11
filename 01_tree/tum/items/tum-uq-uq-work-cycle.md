---
id: tum-uq-uq-work-cycle
source: tum-numuq
parent: uq-probability
title: Uncertainty models and the forward–inverse UQ cycle
type: concept
caption: "Separates intrinsic variability and incomplete information while linking data, uncertain parameters and model outputs."
---

# Uncertainty models and the forward–inverse UQ cycle

Uncertainty can arise from intrinsic variability (aleatoric) or incomplete knowledge (epistemic). Additional measurements can reduce the latter in principle, while repeated experiments still exhibit the former. The distinction depends on the model and available information and need not be uniquely meaningful. Examples include manufacturing variability, uncertain material parameters and competing biological models. Probability supplies the course's common representation; merely naming fuzzy sets or interval arithmetic does not develop those alternatives.

The UQ cycle starts with a probability law for unknown parameters, updates it using observations in an inverse problem, propagates that law through a forward model, and evaluates output statistics. Experimental design can then select informative measurements. Forward propagation asks what uncertain inputs imply for outputs; sensitivity analysis ranks input influence, dimension reduction retains influential combinations, and inverse UQ uses observed outputs to improve input characterization. These are distinct tasks within the cycle, not interchangeable names for Monte Carlo.

For expensive PDE models, repeated solves, high- or infinite-dimensional probability measures, complex sampling and nonsmooth random functions are central obstacles. Nonintrusive sample-based methods reuse a deterministic solver as a black box; surrogate approaches approximate its parameter-to-observation map and often exploit smoothness or alter the solver. The introductory examples illustrate these roles rather than establishing personal experiments or quantitative prediction accuracy.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Topics and Slides/Lecture 01 (16.04.24)`, all 38 physical pages (printed slides 1–48 with gaps), especially physical pp. 18–25 and 33–37, uncertainty types, work-cycle diagram, computational challenges and method distinctions.
- `Oral exam/Topics and sample questions (08.07.24)`, §1, p. 1, uncertainty models and PDE challenges.
