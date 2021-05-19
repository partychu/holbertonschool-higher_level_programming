#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Define class Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """ Method to calculate area """
        area = self.__size ** 2
        return area

    def my_print(self):
        """ Method to print square """
        if self.__size is 0:
            print()
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                if y == 0:
                    for i in range(self.__position[0]):
                        print(" ", end="")
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

    @property
    def position(self):
        """ Getter for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for position """
        if type(value) is tuple and len(value) is 2:
            for i in value:
                if type(value[i]) is int and value[i] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
