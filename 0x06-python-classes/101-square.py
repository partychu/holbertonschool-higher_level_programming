#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Define class Square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """ Method to calculate area """
        area = self.size ** 2
        return area

    def my_print(self):
        """ Method to print square """
        if self.size is 0:
            print()
        else:
            for i in range(0, self.position[1]):
                print()
            for x in range(self.size):
                for y in range(self.size):
                    if y == 0:
                        for i in range(self.position[0]):
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
        flag = False
        if type(value) is tuple and len(value) is 2:
            if type(value[0]) is int and value[0] >= 0:
                if type(value[1]) is int and value[1] >= 0:
                    flag = True
                    self.__position = value
        if flag is False:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """ String module for print function """
        square_str = ""
        if self.size is 0:
            square_str += "\n"
        else:
            for i in range(0, self.position[1]):
                square_str += '\n'
            for x in range(self.size):
                for y in range(self.size):
                    if y == 0:
                        for i in range(self.position[0]):
                            square_str += " "
                    square_str += "#"
                square_str += '\n'
            square_str = square_str[:-1]
        return square_str
