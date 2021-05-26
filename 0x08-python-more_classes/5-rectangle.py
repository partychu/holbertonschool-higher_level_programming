#!/usr/bin/python3
""" Define class rectangle by width and height """


class Rectangle:
    """ Class rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        """Method to calculate area"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """ Method to calculate perimeter """
        if self.width == 0 or self.height == 0:
            perimeter = 0
            return perimeter
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation"""
        rec_str = ""
        if self.width == 0 or self.height == 0:
            rec_str += "\n"
            rec_str = rec_str[:-1]
        else:
            for y in range(self.height):
                for x in range(self.width):
                    rec_str += "#"
                rec_str += "\n"
            rec_str = rec_str[:-1]
        return rec_str

    def __repr__(self):
        """Official string representation of object"""
        rep = "Rectangle({}, {})".format(self.width, self.height)
        return rep

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
