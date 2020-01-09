#!/usr/bin/python3
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        x = isinstance(size, int)
        if not x:
            print("size must be an integer", end=" ")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end=" ")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        a_square = self.__size**2
        return a_square
