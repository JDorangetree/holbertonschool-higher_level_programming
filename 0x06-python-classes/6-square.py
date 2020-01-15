class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method of the square class
        Args:
            size: Is the type int private attribute
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Private instance attribute getter method."""
        return self.__position

    @size.setter
    def position(self, value):
        """Private instance attribute property setter."""
        x = isinstance(value, tuple)
        if x and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2\
positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """method to calculate the area of ​​a square"""
        a_square = self.__size**2
        return a_square

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            x = self.__position
            for i in range(0, x[1]):
                print("")
            for i in range(0, self.__size):
                y = "_"
                z = x[0] * y
                print("{}".format(z), end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
