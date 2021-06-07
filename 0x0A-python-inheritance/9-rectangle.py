#!/usr/bin/python3
"""
Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Class constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def __str__(self):
        """Str repr"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
