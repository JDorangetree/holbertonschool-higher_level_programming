#!/usr/bin/python3
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """The __init__ method of the square class
        Args:
            size: Is the type int private attribute
        """
        self.__size = size

    @property
    def size(self):
        """Private instance attribute getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """Private instance attribute property setter."""
        x = isinstance(value, int)
        if not x:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method to calculate the area of ​​a square"""
        a_square = self.__size**2
        return a_square
