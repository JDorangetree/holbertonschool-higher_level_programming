#!/usr/bin/python3
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        x = isinstance(size, int)
        if x == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
