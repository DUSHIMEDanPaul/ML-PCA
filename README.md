# Machine Learning Project: Matrix Operations and PCA on African Dataset

## Overview

This project is structured into **three phases** and demonstrates key linear algebra and machine learning techniques in Python. It includes:

1. A custom Python library for matrix multiplication (`alumath`)
2. Implementation of **Principal Component Analysis (PCA)** on an African dataset
3. Manual computation of **eigenvalues** and **eigenvectors**

The goal of this project is to build core ML capabilities from scratch, enhance mathematical intuition, and apply PCA for dimensionality reduction and data interpretation.

---

## Project Structure

```
ML-PCA/
│
├── work/                          # Matrix multiplication library
│   ├── setup.py                   # Package installation configuration
│   ├── alumath/                   # Main library package
│   │   ├── __init__.py            # Package exports
│   │   └── matrix_ops.py          # Matrix operations implementation
│   └── tests/                     # Unit tests
│       ├── __init__.py
│       └── test_matrix_ops.py     # Tests for matrix operations
│
├── PCA/                           # Principal Component Analysis
│   ├── Africa_1997-2020_Jan08.csv # African dataset used in PCA
│   ├── README.md                  # PCA-specific documentation
│   └── Template_PCA_Formative_2.ipynb  # PCA implementation notebook
│
├── Eigen/                         # Eigenvalue/Eigenvector calculations
│
└── README.md                      # Project documentation
```

---

## Phase 1: Matrix Multiplication Library (`alumath`)

A custom matrix multiplication library with input validation and descriptive error messages, implemented without external dependencies like NumPy.

### Installation

```bash
cd work
pip install -e .
```

### Features

- **Matrix class**: Create and manipulate 2D matrices with dimension validation
- **MatrixMultiplier class**: Perform matrix multiplication with detailed error messages
- **Input validation**: Ensures matrices have valid dimensions before operations
- **Descriptive errors**: Clear, informative error messages when multiplication fails
- **Convenience functions**: Simple API with `multiply_matrices()` and `create_matrix()`

### API Reference

| Function/Class | Description |
|----------------|-------------|
| `Matrix(data)` | Create a matrix from a 2D list |
| `MatrixMultiplier.multiply(A, B)` | Multiply two matrices |
| `MatrixMultiplier.can_multiply(A, B)` | Check if multiplication is valid |
| `MatrixMultiplier.get_result_dimensions(A, B)` | Get result matrix dimensions |
| `multiply_matrices(A, B)` | Convenience function for multiplication |
| `create_matrix(data)` | Convenience function to create a Matrix |

### Usage Example

```python
from alumath import multiply_matrices, create_matrix, Matrix

# Using convenience function with 2D lists
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = multiply_matrices(A, B)
print(result)

# Using Matrix class
matrix_a = create_matrix([[1, 2, 3], [4, 5, 6]])
matrix_b = Matrix([[7, 8], [9, 10], [11, 12]])
result = multiply_matrices(matrix_a, matrix_b)
print(result)
```

---

## Phase 2: Principal Component Analysis (PCA)

PCA is implemented to analyze and reduce dimensionality of a real-world African dataset (1997-2020).

**Key Steps:**

* Data normalization
* Covariance matrix calculation
* Eigen decomposition
* Projection to lower dimensions
* Data visualization (2D plot)

**Libraries Used:**

* `pandas`, `numpy`, `matplotlib`, `seaborn`

**Dataset:** `PCA/Africa_1997-2020_Jan08.csv` - Contains African socio-economic data for analysis.

**Notebook:** `PCA/Template_PCA_Formative_1[15].ipynb` - Full PCA implementation with visualizations.

---

## Phase 3: Eigenvalue and Eigenvector Computation

Manual computation of eigenvalues and eigenvectors to understand the mathematical foundations of PCA.

**Location:** `Eigen/` directory

---

## Requirements

- Python >= 3.7
- For PCA: `pandas`, `numpy`, `matplotlib`, `seaborn`
- For matrix library: No external dependencies

## Contributors

* DUSHIME Dan Paul

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
