#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = ""
        for val in row:
            print("{:s}{:d}".format(space, val), end="")
            space = " "
        print()
