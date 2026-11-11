---
id: tum-uq-software-roles
source: tum-numuq
parent: uq-probability
title: Software roles across uncertainty-quantification workflows
type: concept
caption: Maps the course software survey to propagation, inversion, field sampling and model-coupling tasks without implying
  use.
---

# Software roles across uncertainty-quantification workflows

The notes' software appendix distinguishes several roles in a UQ workflow. UQLab and MUQ are listed as broader environments for forward propagation, polynomial chaos and inverse UQ; their listed capabilities also include sensitivity analysis and random fields, with reliability/design functions highlighted for UQLab and MCMC/Gaussian-process regression for MUQ. hIPPyLib is listed for Gaussian-field sampling, Monte Carlo/control-variate propagation and inversion. These are the capabilities reported by this course appendix, rather than a current product comparison.

Other entries have narrower roles: the Sparse Grids MATLAB Kit supplies sparse-grid propagation; S-IFISS targets stochastic Galerkin diffusion models; CUQIpy is listed for inverse UQ in image reconstruction. UMBridge couples statistical/optimization software to numerical models and supplies benchmarks, separating the model interface from the inference or propagation algorithm. The MLMC software entry points to a collection of implementations in multiple languages rather than one monolithic package.

The appendix identifies MATLAB, Python, C++ and R interfaces across this landscape. It lists all eight resources as open software or software collections, but provides no execution evidence for them. In particular, the existence of course-supplied MATLAB scripts does not establish hands-on use of every surveyed package or personal implementation of their algorithms.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, appendix F.1–F.8, pp. 107–109, complete software survey.
