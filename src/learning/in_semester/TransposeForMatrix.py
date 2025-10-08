"""
File: TransposeForMatrix.py
Author: Shiqi Su
Date: 2025-09-03 17:25
Description:
"""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Return the transpose of the given matrix.

    The transpose is obtained by swapping the rows and columns of the input
    matrix. For a matrix of size m x n, the resulting matrix will be of size
    n x m.
    Args:
        matrix (list[list[int]): A 2D list representing the input matrix.
            - Assumes len(matrix) > 0.
            - Assumes all inner lists are of equal length.
    Returns:
        list[list[int]: A new 2D list representing the transpose.

    """
    row = len(matrix)

    swap_list = [[]]
    # Check if it has an empty list
    if row == 0:
        return swap_list

    col = len(matrix[0])
    for c in range(col):
        new_row = [[]]
        for r in range(row):
            new_row = matrix[r][c]
        swap_list.append(new_row)
    return swap_list

