#!/usr/bin/python3
""" Model Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Class that defines a Rectangle model """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ Print Method """
        msg = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        msg = msg.format(self.id, self.x, self.y, self.width, self.height)
        return msg

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area value of Rectangle instance """
        Area = self.width * self.height
        return Area

    def display(self):
        """ Function to print Rectangle """
        if self.width == 0 or self.width == 0:
            return
        for i in range(self.y):
            print("")
        space = " "
        for i in range(self.height):
            print("{}".format(self.x * space), end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ Function to update arguments of each attr """
        args_list = ["id", "width", "height", "x", "y"]
        i = 0
        if args and len(args) != 0:
            for item in args:
                if i == 0:
                    Base.__init__(self, item)
                elif i < len(args_list):
                    setattr(self, args_list[i], item)
                i += 1
        else:
            for key, values in kwargs.items():
                if key == "id":
                    Base.__init__(self, values)
                else:
                    setattr(self, key, values)

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        my_dict = {"id": self.id, "width": self.width, "height": self.height,
                   "x": self.x, "y": self.y}
        return my_dict
