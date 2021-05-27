#!/usr/bin/python3
""" Define class rectangle by width and height """


class Rectangle:
    """ Class rectangle """

    """Class variable"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Destructor method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
                    rec_str += str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns biggest rectangle based on area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle instance"""
        return cls(size, size)
