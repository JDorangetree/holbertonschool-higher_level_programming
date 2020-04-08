#!/usr/bin/python3
""" Function to find a peak in list """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""

    if len(list_of_integers) > 0:
        pick = list_of_integers[0]
        for item in list_of_integers:
            if item > pick:
                pick = item
        return(pick)
    else:
        return(None)
