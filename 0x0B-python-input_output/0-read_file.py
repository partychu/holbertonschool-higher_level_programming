#!/usr/bin/python3
"""
read_file - reads a text file
filename: file to read

"""


def read_file(filename=""):
    """
    reads txt in UTF8 and prints to stdout
    """
    with open(filename, encoding='UTF8') as f:
        for line in f:
            print(line, end="")
