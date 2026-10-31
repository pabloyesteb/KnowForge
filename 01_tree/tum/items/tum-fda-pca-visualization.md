---
id: tum-fda-pca-visualization
source: tum-foundations-data-analysis
parent: fda-svd
title: Principal-component coordinates for data visualization
type: method
caption: "Projects observation rows onto leading right singular vectors for labeled two- and three-dimensional displays."
---

# Principal-component coordinates for data visualization

The booklet's PCA exercise takes a high-dimensional data matrix and asks for its SVD and a plot in the first three principal components. Singular directions provide orthogonal coordinates; retaining the leading coordinates produces a low-dimensional representation associated with the leading rank approximation.

The prescribed example loads MATLAB's `ovariancancer` data, inspects the sample count and dimension, and plots diagnosed samples as red crosses and controls as blue circles. The supplied `Code for Exercise 6.2` is MATLAB text: it calls `load ovariancancer`, `whos`, and `[U,S,V]=svd(obs,'econ')`, then plots `diag(S)` on a logarithmic scale. Each row `obs(i,:)` is an observation. Its first three coordinates are computed as \(V(:,j)^T\operatorname{obs}(i,:)^T\), for \(j=1,2,3\), and displayed in both 3D and the first two dimensions with class-dependent markers. Equivalently the scores are the first columns of \(\operatorname{obs}V=U\Sigma\).

The code applies SVD directly to `obs`: it contains no explicit mean subtraction or feature scaling. It therefore documents uncentered singular coordinates as supplied, rather than establishing an ordinary centered covariance-PCA pipeline. The group labels determine plot colors/markers; they are not used to train a classifier.

This is a concrete course-provided plotting script and a requested data-analysis exercise. The dataset is loaded from MATLAB rather than packaged in the archive, and no predictive metrics, medical findings or personally attributable implementation are established. The booklet's solution contains only a MATLAB-code pointer; the separate weekly asset supplies the script text.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 2.1.12, p. 21; solution, p. 38.
- `27. Mai - 2. Juni/Problem Set 6.pdf`, Exercise 6.2, p. 1.
- `3. Juni - 9. Juni/Code for Exercise 6.2`, entire extensionless MATLAB text, economy SVD, singular-value plot, per-row coordinate products and labeled 2D/3D plots.
