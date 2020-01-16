#!/usr/bin/python3
class Rectangle:
    """ Class that creates a Rectangle Object """
    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    def __str__(self):
        print_string = ""
        if self.__width == 0 or self.__height == 0:
            print_string = ""
        else:
            for i in range(0, self.__height):
                print_string = print_string + "{}".format("#" * self.__width)
                if not (self.__height - i) == 1:
                    print_string = print_string + "\n"
        return print_string

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

    def __repr__(self):
        return "Rectangle ({:d}, {:d})".format(self.width, self.height)
