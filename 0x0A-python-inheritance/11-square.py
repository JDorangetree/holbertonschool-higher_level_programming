#!/usr/bin/python3
""" Class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area method"""
        My_area = self.__size * self.__size
        return My_area

    def __str__(self):
        """ Method for when print is used """
        my_string = "[Square] {}/{}".format(self.__size, self.__size)
        return my_string
