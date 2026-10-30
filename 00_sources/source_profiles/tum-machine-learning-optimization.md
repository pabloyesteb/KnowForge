# Machine Learning and Optimization — supplementary academic materials

## Source identity

| Field | Value |
|---|---|
| Source ID | tum-machine-learning-optimization |
| Module code | EI71058 |
| Academic term | Winter Semester 2025/26 |
| Source category | Supplementary academic material |
| Academic credit | Not established |
| Profile status | complete_validated |

The introduction identifies the material as EI71058 — Machine Learning and Optimization, distinct from Fundamentals of Optimization for Machine Learning. It is supplementary material without a transcript match; the learning relationship and personal assignment or implementation outcomes are unspecified.

## Source files

- **Archive:** `00_sources/raw/tum/archives/Machine Learnin 950839125 (W25_26)_20261012_1602.zip`
- **Lectures:** `Introduction Slides.pdf` and weekly lecture-note PDFs [N1–N11]
- **Exercises and solutions:** weekly homework/solution PDFs and tutorial files
- **Notebooks:** `logistic_regression_with_early_stopping.ipynb`, `mnist_homework.ipynb`, `neural_networks_pytorch.ipynb`, `Jupyter Notebook on GPT.json`; other notebook-format JSON files
- **Data and packages:** archived CSV and `.imscc` packages
- **Past exams:** archived examination PDFs

## Content structure

```text
Lecture documents
├── Introduction Slides.pdf
├── Week 1 and 2 — Linear Regression, Ridge Regression [N1]
├── Notes 2 — Model selection [N2]
├── Week 3 — Convex optimization / stochastic gradient [N3]
├── Week 4 — Logistic regression [N4]
├── Week 5 — Statistical learning theory [N5]
├── Week 6 — Algorithmic Regularization [N6]
├── Week 7 — SVM and Kernels [N7]
├── Notes 8 — Neural Network [N8]
├── Week 9 — CNN [N9]
├── Acceleration and adaptive gradient methods [N10]
└── Role of Training Data [N11]

Practice
├── Homework and solutions
├── Tutorials
├── logistic_regression_with_early_stopping.ipynb
├── mnist_homework.ipynb
├── neural_networks_pytorch.ipynb
└── Jupyter Notebook on GPT.json

Other material
├── Historical exams
└── Nested IMSCC packages
```

The introduction plus eleven note references account for twelve documents, not twelve uniformly numbered weeks. Entries abbreviate the established filenames; exact titles, dates and the truncated N3 filename remain in the source index.

## Technical topic map

### Regression, regularization and evaluation

Linear least squares is developed through convex-optimization and linear-algebra arguments, including collinearity, ridge estimates and bias–variance trade-offs. Model selection distinguishes training, validation and test risks. Logistic and multiclass logistic regression connect probabilistic classification to gradient-based fitting. [N1–2, N4.]

Statistical learning theory includes no-free-lunch discussion, generative/discriminative distinctions, empirical versus population risk, uniform convergence, Hoeffding bounds/union bounds and algorithmic stability. The archive therefore links optimization error and generalization rather than only listing supervised predictors. Early stopping for least squares introduces **algorithmic regularization**. [N5–6.]

### Optimization algorithms

Convexity, quadratic gradient-descent convergence and stochastic-gradient analysis accompany incremental gradients, soft-margin classification, population-risk minimization, stochastic approximation and coordinate descent. Epoch/momentum concepts precede acceleration and adaptive updates: **Nesterov acceleration, AdaGrad and Adam**. The adaptive-method note gives an illustrative diagonal least-squares AdaGrad convergence analysis, not an unrestricted rate for every ML objective. Randomized Kaczmarz is explicitly marked additional reading not discussed in class; it belongs to the supplied corpus with that distinction. [N3, N10.]

### Margins, kernels and nonlinear predictors

Perceptron, hard/soft-margin SVM, Lagrangian duality, dual SVM formulation, nonlinear features, the **representer theorem** and Gaussian kernels build a kernel-method block. This supplies both optimization and function-representation viewpoints. [N7, §§11–12.]

### Neural networks and vision

Neural architectures, optimization, automatic differentiation and vanishing gradients lead into convolutional networks. Local connectivity and shift equivariance motivate convolutional inductive bias; channels, learned kernels, stride, padding and pooling control representation size and computation. Examples include LeNet, AlexNet, ResNet and U-net, with image classification, segmentation and reconstruction applications. [N8–9; CNN deck pp. 4–22.]

### Training data and language-model context

The final deck emphasizes leakage from feature selection/evaluation, distribution shift, pretraining versus task-specific fine-tuning, web-data quality and dataset evaluation at controlled model/compute/token scales. A GPT diagram explicitly shows tokenization → transformer → next-token probabilities with cross-entropy loss. The data-curation sequence includes heuristic filtering, deduplication and ML-based quality filtering, illustrated by DCLM/FineWeb/C4 examples; it is source-era context, not a current ranking of models or datasets. [N11, pp. 2–23, especially pp. 12–21.]

## Computational material, tools and applications

Static notebook/JSON cell inspection evidences **Python, NumPy, SciPy, pandas, scikit-learn, PyTorch, torchvision, Matplotlib and tqdm**. Named files include logistic-regression early stopping, MNIST, PyTorch neural-network exercises, a house-price CSV, `PyTorchFromScratch.json` and a GPT notebook JSON. Hitters/nuclear datasets are supplied as nested `.imscc` packages. Notebook presence is evidence of available exercises, not user authorship or successful training. The introduction names fraud detection, recommendations, NLP, self-driving and scientific signal reconstruction as applications, while actual represented examples include regression and image learning.

## Relationships and potential professional relevance

This material overlaps usefully with [Statistical Learning](tum-statistical-learning.md), [Foundations of Data Analysis](tum-foundations-data-analysis.md), [FOML](tum-fundamentals-optimization-ml.md), [NLP](tum-nlp.md) and [Deep Generative Models](tum-advanced-machine-learning.md), but is not a newly credited version of them. Generalization/data reliability connect to the [scientific paper](ngvalidation.md); optimizer/regularization/data workflows connect to [pyLowOrder](pyloworder.md) without changing that project's contribution evidence.

Potential domains: ML/data engineering, robust evaluation, scientific ML and quantitative predictive modeling. Thematic categories: machine learning; optimization; statistics and data science; software/data engineering.

## Source index and deeper-extraction priorities

All references resolve inside the named archive:

- Identity: `14. Oktober - 20. Oktober/Introduction Slides.pdf`, p. 1.
- **N1:** `14. Oktober - 20. Oktober/Lecture Notes Week 1 and 2 (Linear Regression, Ridge Regression).pdf` (10 pp.). **N2:** `21. Oktober - 27. Oktober/Lecture Notes 2 (model selection).pdf` (5 pp.).
- **N3:** `28. Oktober - 3. November/Lecture Notes Week 3(convex opt___nd stochastic gradient method).pdf` (13 pp.). **N4:** `4. November - 10. November/Lecture Notes Week 4(Logistic regression).pdf` (5 pp.).
- **N5:** `11. November - 17. November/Lecture Notes Week 5(Statistical learning theory).pdf` (9 pp.). **N6:** `18. November - 24. November/Lecture Notes Week 6(Algorithmic Regularization).pdf` (4 pp.).
- **N7:** `25. November - 1. Dezember/Lecture Notes Week 7 (SVM and Kernels).pdf` (14 pp.). **N8:** `9. Dezember - 15. Dezember/Lecture Notes 8(Neural Network).pdf` (7 pp.).
- **N9:** `16. Dezember - 22. Dezember/Lecture Notes Week 9 - CNN.pdf` (22 pp.). **N10:** `27. Januar - 2. Februar/Lecture Notes(Acceleration and adaptive gradient methods).pdf` (5 pp.). **N11:** `3. Februar - 9. Februar/Lecture Notes(Role of Training Data).pdf` (23 pp.).
- Computational anchors: `25. November - 1. Dezember/logistic_regression_with_early_stopping.ipynb`; `9. Dezember - 15. Dezember/mnist_homework.ipynb`; `16. Dezember - 22. Dezember/neural_networks_pytorch.ipynb`; `20. Januar - 26. Januar/Jupyter Notebook on GPT.json`.
- Inventory: stable source ID in `00_sources/inventory/sources.yaml`; exact members in `archive_files.csv`.

The 11 numbered N references cover the available subject-note sequence; the introduction is separate, and N1 combines linear and ridge regression. Prioritize stability/generalization assumptions, early-stopping spectral analysis, kernel/representer derivations and optimizer rates; then inspect selected notebook objectives/data splits and dataset packages. Additional visual inspection should precede extracting detailed architecture/layout-dependent claims. This map covers the full available lecture-topic sequence without validating all homework, historical exams or every notebook result.
