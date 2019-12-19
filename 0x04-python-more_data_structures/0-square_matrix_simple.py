#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = [[row[i]**2 for i in range(len(matrix))]for row in matrix]
        return new_matrix
    return matrix
