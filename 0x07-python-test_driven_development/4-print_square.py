#!/usr/bin/python3
"""
print_square - prints a square with the # character
Parameters: size
"""
def print_square(size):
    """
    Prints a square
    Size is the length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, size):
        for y in range(0, size):
            print('#', end="")
        print()
