from codewars_kata_diary import testing

import numpy as np
from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]


def build_minor(
    matrix: Matrix, crossout_row: int, crossout_col: int
) -> Matrix:
    size = len(matrix)
    assert size >= 2

    res = []
    for idx_row in range(size):
        if idx_row == crossout_row:
            continue

        row = []
        for idx_col in range(size):
            if idx_col == crossout_col:
                continue

            row.append(matrix[idx_row][idx_col])
        res.append(row)

    return res


def build_minor2(
    matrix: Matrix, crossout_row: int, crossout_col: int
) -> Matrix:
    size = len(matrix)
    assert size >= 2

    return [
        row[:crossout_col] + row[crossout_col + 1 :]
        for row in (matrix[:crossout_row] + matrix[crossout_row + 1 :])
    ]


def determinant(matrix: Matrix) -> int:
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        sum = 0
        idx_row = 0
        signs = [1, -1]
        for idx_col in range(size):
            sign = signs[idx_col % 2]
            multiplier = matrix[idx_row][idx_col]
            minor_matrix = build_minor(matrix, idx_row, idx_col)
            sum += sign * multiplier * determinant(minor_matrix)

        return sum


def determinant2(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        sum = 0
        idx_row = 0
        for idx_col in range(size):
            sign = (-1) ** idx_col
            multiplier = matrix[idx_row][idx_col]
            minor_matrix = build_minor2(matrix, idx_row, idx_col)
            sum += sign * multiplier * determinant(minor_matrix)

        return sum


if __name__ == "__main__":
    inputs = [
        [[1, 3], [2, 5]],
        [[2, 5, 3], [1, -2, -1], [1, 3, 4]],
        [[2, 5, 3, 1], [1, -2, -1, 0], [1, 3, 4, 2], [1, 3, 4, 2]],
    ]
    expected = [round(np.linalg.det(inp)) for inp in inputs]

    testing.test_func(inputs, expected, determinant2)
