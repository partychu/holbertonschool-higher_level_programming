#!/usr/bin/python
"""

read_file

"""


def read_file(filename=""):
    """
    appends a string at end of file, returns number of characters written
    """
    with open(filename, encoding='UTF8') as f:
        for line in f:
            print(line, end="")
