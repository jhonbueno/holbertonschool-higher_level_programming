#!/usr/bin/python3


"""Class square with size"""


class Square:
    """Empty class"""
    __size = None

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if ((isinstance(value, tuple)) and len(value) == 2 and
                (value[0] >= 0 and value[1] >= 0)
                and (isinstance(value[0], int)) and
                (isinstance(value[1], int))):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(0, self.__size):
            if (self.__position[1] == 0):
                print(" " * self.__position[0], end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")
