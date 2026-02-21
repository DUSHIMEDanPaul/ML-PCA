"""
Matrix Operations Module
"""

from typing import List, Union


class Matrix:
    """Represents a 2D numeric matrix with basic validation."""

    def __init__(self, data: List[List[Union[int, float]]]):
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty.")

        row_length = len(data[0])
        for idx, row in enumerate(data):
            if len(row) != row_length:
                raise ValueError(
                    f"Inconsistent row length at row {idx}: "
                    f"expected {row_length}, got {len(row)}."
                )

        self.data = data
        self.rows = len(data)
        self.cols = row_length

    def __str__(self) -> str:
        return "\n".join(
            "[" + " ".join(f"{value:8.2f}" for value in row) + "]"
            for row in self.data
        )

    def __repr__(self) -> str:
        return f"Matrix(rows={self.rows}, cols={self.cols})"

    def get_dimensions(self) -> tuple:
        return self.rows, self.cols


class MatrixMultiplicationError(Exception):
    """Raised when matrix multiplication constraints are violated."""

    def __init__(self, message: str, error_type: str = "general"):
        self.error_type = error_type
        super().__init__(message)


class MatrixMultiplier:

    @staticmethod
    def _build_dimension_error(matrix1_dims: tuple, matrix2_dims: tuple) -> str:
        return (
            "Matrix multiplication failed due to dimension mismatch.\n"
            f"Matrix A: {matrix1_dims[0]}x{matrix1_dims[1]}\n"
            f"Matrix B: {matrix2_dims[0]}x{matrix2_dims[1]}\n"
            "Requirement: number of columns in Matrix A must equal "
            "number of rows in Matrix B."
        )

    @staticmethod
    def multiply(
        matrix1: Union[Matrix, List[List]],
        matrix2: Union[Matrix, List[List]]
    ) -> Matrix:

        if not isinstance(matrix1, Matrix):
            matrix1 = Matrix(matrix1)

        if not isinstance(matrix2, Matrix):
            matrix2 = Matrix(matrix2)

        if matrix1.cols != matrix2.rows:
            error_message = MatrixMultiplier._build_dimension_error(
                matrix1.get_dimensions(),
                matrix2.get_dimensions(),
            )
            raise MatrixMultiplicationError(
                error_message,
                "dimension_mismatch"
            )

        result = [
            [
                sum(matrix1.data[i][k] * matrix2.data[k][j]
                    for k in range(matrix1.cols))
                for j in range(matrix2.cols)
            ]
            for i in range(matrix1.rows)
        ]

        return Matrix(result)

    @staticmethod
    def can_multiply(
        matrix1: Union[Matrix, List[List]],
        matrix2: Union[Matrix, List[List]]
    ) -> bool:

        if not isinstance(matrix1, Matrix):
            matrix1 = Matrix(matrix1)

        if not isinstance(matrix2, Matrix):
            matrix2 = Matrix(matrix2)

        return matrix1.cols == matrix2.rows

    @staticmethod
    def get_result_dimensions(
        matrix1: Union[Matrix, List[List]],
        matrix2: Union[Matrix, List[List]]
    ) -> tuple:

        if not isinstance(matrix1, Matrix):
            matrix1 = Matrix(matrix1)

        if not isinstance(matrix2, Matrix):
            matrix2 = Matrix(matrix2)

        if not MatrixMultiplier.can_multiply(matrix1, matrix2):
            error_message = MatrixMultiplier._build_dimension_error(
                matrix1.get_dimensions(),
                matrix2.get_dimensions(),
            )
            raise MatrixMultiplicationError(
                error_message,
                "dimension_mismatch"
            )

        return matrix1.rows, matrix2.cols


def multiply_matrices(matrix1, matrix2):
    """Convenience wrapper for matrix multiplication."""
    return MatrixMultiplier.multiply(matrix1, matrix2)


def create_matrix(data):
    """Convenience wrapper for Matrix creation."""
    return Matrix(data)
