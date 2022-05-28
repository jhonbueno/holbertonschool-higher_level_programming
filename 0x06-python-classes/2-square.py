#!/usr/bin/python3


"""Class square with size"""


class Square:
    """Empty class"""
    __size = None

    def __init__(self, size=0):

        if type(size) is not int:
            raise NameError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
