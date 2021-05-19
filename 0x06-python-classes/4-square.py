#!/usr/bin/python3
""" Class Square that defines a square by size """


class Square:
    """ Create class square """
    def __init__(self, size=0):
        """ Initializing size attribute """
        self.__size = size

    def area(self):
        """ Method to calculate area """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
