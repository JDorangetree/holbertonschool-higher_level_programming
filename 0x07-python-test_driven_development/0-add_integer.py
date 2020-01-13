#!/usr/bin/python3
"""doctest: examples embedded in the documentation
and verifying that they produce the expected results.
in this project we used External Documentation.

"""


def add_integer(a, b=98):
    """function that adds 2 integers,
    arguments are a and b, and they can be float or
    int if arguments are invalid type, a TypeError is raised"""

    x = isinstance(a, (int, float))
    y = isinstance(b, (int, float))
    if not x or not y:
        if not x:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
    else:
        c = int(a) + int(b)
        return c
