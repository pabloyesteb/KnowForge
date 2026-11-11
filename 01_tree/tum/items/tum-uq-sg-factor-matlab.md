---
id: tum-uq-sg-factor-matlab
source: tum-numuq
parent: uq-stochastic-galerkin
title: Supplied spatial and stochastic Galerkin factor constructors
type: implementation
caption: Builds sparse finite-element factors and total-degree Legendre couplings while exposing a model-index mismatch.
---

# Supplied spatial and stochastic Galerkin factor constructors

`A_mats(ne,sigma,mu,P)` creates the constant diffusion stiffness matrix and unit load with \(ne\) uniform elements, midpoint coefficient values and boundary nodes removed. It then constructs \(P\) fluctuation factors. The local FE helper assembles \((a_e/h)\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\) and \(f_eh(1,1)^T/2\) into sparse arrays.

A concrete source-code discrepancy matters: the loop is `for k=2:P+1` and uses \(\sigma/(k\pi)^2\cos(k\pi x)\) in cell `A{k}`. Consequently factors coupled to inputs 1 through \(P\) correspond to frequencies **2 through \(P+1\)**. The exercise and Monte Carlo sampler instead specify frequencies 1 through \(P\). Both standalone and nested copies have this same offset; the resulting SG code does not solve exactly the stated MC comparison model. Its nominal amplitude bound remains valid, but the first and strongest random mode is omitted.

`G_mats(M,k)` generates all multi-indices of total degree at most \(k\), recursively enumerating each exact-degree set and concatenating them. It stores indices as `uint8`, sets \(G_0=I\), finds the neighbor \(\alpha+e_m\), and inserts the normalized Legendre recurrence value \(n/\sqrt{4n^2-1}\) symmetrically. This implements uniform inputs on \([-1,1]\), rather than the standardized \([-\sqrt3,\sqrt3]\) interval used in part of the notes. Degrees must fit the integer storage type; this is not a general arbitrary-degree representation. The code attributes the index/matrix routines to IFISS/SIFISS contributors and a recursive indexing routine originating in SPQUAD.

The package also contains a separate `oned_linear_FEM_mat.m` with signature `(ne,a,f)` but references undefined `p,q` internally. It is a defective standalone helper; `A_mats.m` includes its own correctly parameterized local helper, so that separate file is not the helper used by its assembly. These limitations describe the supplied files and do not imply they were repaired or executed.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/A_mats.m` and `Problem Sheets/G_mats.m`, complete files including all local helpers.
- `Problem Sheets/SG_matlab.zip`, byte-identical `A_mats.m` and `G_mats.m`; complete separate `oned_linear_FEM_mat.m`.
- `Problem Sheets/Sheet 05 (02.07.2023)`, Problem 19, intended coefficient frequencies; `Problem Sheets/oned_MC_FEM.m`, loop over frequencies 1 through P.
