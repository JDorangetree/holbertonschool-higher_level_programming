#!/usr/bin/python3
"""class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define object Rectangle from BaseGeometry inheritance """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Method for when print is used """
        my_string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return my_string

    def area(self):
        """Method for area calculation """
        My_area = self.__width * self.__height
        return My_area
