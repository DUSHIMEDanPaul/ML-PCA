"""
 Matrix Multiplication Library
A fun and educational matrix multiplication library with personality!

Authors:
- DUSHIME Dan Paul

Version: 1.0.0
"""

from .matrix_ops import MatrixMultiplier, Matrix, multiply_matrices, create_matrix, MatrixMultiplicationError

__version__ = "1.0.0"
__author__ = "DUSHIME Dan Paul"

# Make key classes available at package level
__all__ = ['MatrixMultiplier', 'Matrix', 'multiply_matrices', 'create_matrix', 'MatrixMultiplicationError']
