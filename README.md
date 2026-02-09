# Machine Learning Project: Matrix Operations and PCA on African Dataset

## Overview

This project is structured into **three phases** and demonstrates key linear algebra and machine learning techniques in Python. It includes:

1. A custom Python library for matrix multiplication (`group15multiplyingmatrices`)
2. Implementation of **Principal Component Analysis (PCA)** on an African dataset
3. Manual computation of **eigenvalues** and **eigenvectors**

The goal of this project is to build core ML capabilities from scratch, enhance mathematical intuition, and apply PCA for dimensionality reduction and data interpretation.

---

## Project Structure

```
project-root/
│
├── matrices/
│   └── matrix.py         # Custom matrix multiplication logic
│
├── pca/
│   ├── Africa_1997-2020_Jan08.csv  # African dataset used in PCA
│   └── Template_PCA_Formative_1[15].ipynb      # PCA implementation and visualization
│     
│
└── README.md             # Project documentation
```

---

## Phase 1: Matrix Multiplication Library

This custom library implements basic matrix multiplication without using external libraries like NumPy.

**Features:**

* Input validation
* Multiplication of 2D matrices
* Clean API for reuse

**Usage Example:**

```python
from group15multiplyingmatrices.matrix import multiply_matrices

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = multiply_matrices(A, B)
print(result)
```

---

##  Phase 2: Principal Component Analysis (PCA)

PCA is implemented to analyze and reduce dimensionality of a real-world African dataset.

**Key Steps:**

* Data normalization
* Covariance matrix calculation
* Eigen decomposition
* Projection to lower dimensions
* Data visualization (2D plot)

**Libraries Used:**

* `pandas`, `numpy`, `matplotlib`, `seaborn`

> 📌 Dataset: A CSV file containing Africanized data.

---

## Phase 3: Eigenvalue and Eigenvector Work

Handwritten eigenvalues and eigenvectors calculation.

## Contributors
* DUSHIME Dan Paul

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

