#!/usr/bin/python3
"""

append_write

"""


def append_write(filename="", text=""):
    """
    reads a text file and prints to stdout
    """
    with open(filename, 'a') as f:
        return f.write(text)
