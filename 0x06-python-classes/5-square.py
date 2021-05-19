#!/usr/bin/python3
""" Class Square that defines a square """
class Square:
    """ Define class Square """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """ Method to calculate area """
        area = self.__size ** 2
        return area

    def my_print(self):
        """ Method to print square """
        if self.__size is 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()

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
