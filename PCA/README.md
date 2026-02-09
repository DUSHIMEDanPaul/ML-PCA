# PCA on Africa 1997-2020 Dataset

This project demonstrates how to perform **Principal Component Analysis (PCA)** using **NumPy only** on a dataset of African countries from 1997 to 2020.

PCA is a powerful dimensionality reduction technique that helps us better understand large datasets by identifying the most important patterns (called *principal components*).

We implemented PCA manually — step by step — to better understand the process, without using external machine learning libraries.

---

## Dataset

- CSV file: `Africa_1997-2020_Jan08.csv`
- Source: [Formative2Group15 GitHub Repository](https://github.com/izabayo7/Formative2Group15)
- Size: ~30MB
- Contains data on various indicators for African countries across multiple years.

---

## Project Steps

### 1️ Load and Standardize the Data

First, we loaded the dataset using `pandas`.  
We selected **numerical columns only**, since PCA works on numbers.

Then we **standardized the data**:

- Subtracted the mean of each column
- Divided by the standard deviation of each column

This ensures that features with different scales (for example, population vs. GDP) contribute equally to the analysis.

---

### 2️ Compute the Covariance Matrix

We calculated the covariance matrix, which tells us how different features vary together.  

This step helps PCA find the *directions of maximum variance* in the data.

---

### 3️ Perform Eigendecomposition

We computed the **eigenvalues** and **eigenvectors** of the covariance matrix:

- **Eigenvalues** show how much variance is captured by each principal component.
- **Eigenvectors** define the directions (new axes) in which the data is transformed.

We sorted these components by their importance (largest eigenvalues first).

---

### 4️ Project Data onto Principal Components

We projected the standardized data onto the **top principal components**.

This produces a new dataset where:

- The first component captures the most variance in the data.
- The second component captures the second-most variance, and so on.

We reduced the dimensionality of the data to just the **top 2 principal components** for visualization.

---

### 5️ Visualize Before and After PCA

We created two scatter plots:

1. **Original Data** → Plot of the first two features of the standardized data.
2. **Reduced Data** → Plot of the first two principal components after PCA.

This helps visually compare the structure of the data before and after applying PCA.

---

## Why We Performed PCA

- To **reduce the dimensionality** of the dataset while preserving as much information as possible.
- To **visualize patterns** and relationships that may not be obvious in the original feature space.
- To practice implementing PCA manually using **only NumPy**, deepening our understanding of how it works internally.

---

## Tools Used

- **Python 3**
- **Pandas** → for reading CSV and basic data handling
- **NumPy** → for matrix calculations, standardization, eigendecomposition
- **Matplotlib** → for data visualization (scatter plots)

---

## Summary

Loaded and standardized the dataset  
Calculated covariance matrix  
Performed eigendecomposition  
Projected data onto principal components  
Visualized results  

This project reinforced our understanding of how PCA works step by step.  
We can now apply these techniques to other datasets for dimensionality reduction and data visualization.

---

## Authors

Formative2Group15
Samuel Wanjohi
Cedric Izabayo
Eliel Ntwali
Edith Githinji

---



