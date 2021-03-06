#!/usr/bin/python3
class Rectangle:
    """ Class that creates a Rectangle Object """
    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area_rectangle = (self.__height) * (self.__width)
        return area_rectangle

    def perimeter(self):
        if self.__height > 0 and self.__width > 0:
            perimeter_rectangle = (self.__height * 2) + (self.__width * 2)
        else:
            perimeter_rectangle = 0
        return perimeter_rectangle
