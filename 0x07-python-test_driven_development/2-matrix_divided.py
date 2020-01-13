#!/usr/bin/python3
"""doctest: examples embedded in the documentation
and verifying that they produce the expected results.
in this project we used External Documentation.

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Arguments:
    matrix: must be a list of lists ints or floats
    with rows of the same size
    div: must be a number int or float and not 0
    Result is rounded to 2 decimal places
    and a new matrix is generated
    Raise TypeError or ZeroDivisionError if conditions not
    met"""

    new_matrix = [x[:] for x in matrix]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not isinstance(matrix[i][j], (int, float)):
                    raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
                num = matrix[i][j] / div
                num_round = round(num, 2)
                new_matrix[i][j] = num_round
            if len(matrix[0]) != (j + 1):
                raise TypeError("Each row of the matrix must have\
 the same size")
        return new_matrix
