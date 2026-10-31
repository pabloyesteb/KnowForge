---
id: tum-fda-svd-image-compression
source: tum-foundations-data-analysis
parent: fda-svd
title: Grayscale image approximation with truncated singular factors
type: method
caption: "Documents the supplied MATLAB image demonstration and its rank-dependent visual and matrix-norm errors."
---

# Grayscale image approximation with truncated singular factors

Treat a grayscale image as a real matrix and retain the leading singular factors. The course solution shows MATLAB code that loads `peppers.png` with `imread`, converts with `rgb2gray`, casts to `double`, computes `[U,S,V]=svd(image)`, and forms
\[
I_k=U(:,1:k)S(1:k,1:k)V(:,1:k)^T
\]
for \(k=10,25,100\). Display code converts the floored reconstructions to `uint8`; the matrix norms are computed on the floating-point residual before this display conversion.

The original RGB image is supplied as an asset. The solution's figure compares the original grayscale image with three reconstructions: rank 10 loses fine detail, rank 25 improves the shapes and shading, and rank 100 visually approaches the original. The screenshot reports:

| Rank | Frobenius residual norm | Spectral residual norm |
|---|---:|---:|
| 10 | \(6.0144\times10^3\) | \(1.8500\times10^3\) |
| 25 | \(3.2952\times10^3\) | \(779.4500\) |
| 100 | \(938.1950\) | \(150.5925\) |

These are absolute errors in the demonstration's grayscale intensity scale, not relative percentages. Their decrease agrees with retaining more singular terms. The evidence consists of course-solution code/output screenshots, not a standalone executable solution file or a personally attributable implementation; the figures and values are source-reported rather than newly reproduced here.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `6. Mai - 12. Mai/Problem Set 3.pdf`, Exercise 3.2, p. 1.
- `13. Mai - 19. Mai/Solution Sheet 3.pdf`, single physical page, Exercise 3.2, MATLAB loading/SVD/display screenshots, four-panel reconstruction figure and matrix-norm outputs.
- `6. Mai - 12. Mai/peppers.png`, supplied 512 × 384 RGB image.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 2.1.6, p. 18; solution pointer, p. 30.
