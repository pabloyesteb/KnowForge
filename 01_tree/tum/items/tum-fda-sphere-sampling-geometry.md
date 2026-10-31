---
id: tum-fda-sphere-sampling-geometry
source: tum-foundations-data-analysis
parent: fda-probability
title: Gaussian normalization and high-dimensional sphere experiments
type: method
caption: "Samples uniform sphere directions by Gaussian normalization and describes the source tasks on projected coordinates and pairwise distances."
---

# Gaussian normalization and high-dimensional sphere experiments

If \(G=(G_1,\ldots,G_d)\) has independent standard Gaussian components, then \(G/\|G\|_2\) is uniform on \(S^{d-1}\). The zero vector has probability zero. Rotational invariance of the Gaussian law and normalization make the direction rotationally invariant; this is surface sampling, distinct from sampling uniformly throughout the ball.

The booklet's numerical tasks explore several consequences and comparisons:

- Generate 200 points on the unit sphere in 50-dimensional space, project them onto several uniform random lines, and plot the one-dimensional distributions to examine concentration near equators.
- Compare histograms of all pairwise distances among 100 uniform points on \(S^3\) and \(S^{100}\).
- Generate 20 points on a sphere of radius 30 in 900-dimensional space; project onto subspaces of dimensions 100, 50, 10, 5, 4, 3, 2 and 1. Compare projected distances with \(\sqrt{k/d}\) times the originals and report the maximal difference as a percentage of \(\sqrt k\).
- Compare two ways to obtain 1000 nearly orthogonal vectors in \(\mathbb R^{100}\): project 1000 orthonormal vectors from dimension 1000 into a random 100-dimensional subspace, or generate random Gaussian vectors. Orthogonality comparisons concern normalized directions rather than unnormalized magnitudes.

The final task's introductory statement about exactly \(d\) orthogonal unit vectors is an upper bound on the cardinality of a mutually orthogonal nonzero set, not a count of all unit vectors. These are proposed MATLAB experiments with no supplied programs or measurements; the tasks alone do not establish observed histograms or distortion results.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, final further “Random Variables” task, p. 44; all four “Numerical Experiment” tasks, p. 45.
