#!/usr/bin/python3
""" Model Square that inherits from Base """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that defines a Square Object """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ Print Method """
        msg = "[Square] ({:d}) {:d}/{:d} - {:d}"
        msg = msg.format(self.id, self.x, self.y, self.size)
        return msg

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Function to update arguments of each attr """
        args_list = ["id", "size", "x", "y"]
        i = 0
        if args and len(args) != 0:
            for item in args:
                if i == 0:
                    Rectangle.update(self, item)
                elif i < len(args_list):
                    setattr(self, args_list[i], item)
                i += 1
        else:
            for key, values in kwargs.items():
                if key == "id":
                    Rectangle.update(self, values)
                else:
                    setattr(self, key, values)

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        my_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return my_dict
