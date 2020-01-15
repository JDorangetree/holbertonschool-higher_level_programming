#!/usr/bin/python3
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @__size.setter
    def __size(self, value):
        x = isinstance(value, int)
        if not x:
            print("size must be an integer", end=" ")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end=" ")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """method to calculate the area of ​​a square"""
        a_square = self.__size**2
        return a_square
