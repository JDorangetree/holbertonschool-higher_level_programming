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
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
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
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        else:
            self.__height = value
