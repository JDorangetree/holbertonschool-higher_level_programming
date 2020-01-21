#!/usr/bin/python3
class BaseGeometry():
    """geometry class"""
    def area(self):
        """ no yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validated value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be a greater than 0".format(name))
