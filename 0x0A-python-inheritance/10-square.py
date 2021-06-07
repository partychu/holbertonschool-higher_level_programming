#!/usr/bin/python3
"""
Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Class Rectangle"""

    def __init__(self, size):
        """Class constructor"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
