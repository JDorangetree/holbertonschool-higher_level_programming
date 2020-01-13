#!/usr/bin/python3
"""doctest: examples embedded in the documentation
and verifying that they produce the expected results.
in this project we used External Documentation.

"""


def print_square(size):
    """Prints a Name
    Args:
        first_name: must be a string
        last_name: must be a string, if no argument given,
        then empty by default
    Otherwise a TypeError is raised"""

    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        if size == 0:
            pass
        else:
            matrix = [[]]
            for i in range(0, size):
                for j in range(0, size):
                    print("#", end="")
                print("")
    else:
        if isinstance(size, (int, float)):
            if size < 0:
                if isinstance(size, float):
                    raise TypeError("size must be an integer")
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
