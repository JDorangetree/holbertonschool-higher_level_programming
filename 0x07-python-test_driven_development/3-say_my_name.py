#!/usr/bin/python3
"""doctest: examples embedded in the documentation
and verifying that they produce the expected results.
in this project we used External Documentation.

"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
