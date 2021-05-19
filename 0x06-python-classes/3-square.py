#!/usr/bin/python3
""" Class Square that defines a square by size """


class Square:
    """ Create class square """
    def __init__(self, size=0):
        """ Initializing size attribute """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method to calculate area """
        area = self.__size ** 2

        return area
