#!/usr/bin/python3
"""

write_file

"""


def write_file(filename="", text=""):
    """
    writes a string to a text file, returns number of characters written
    """
    with open(filename, 'w') as f:
            return f.write(text)
