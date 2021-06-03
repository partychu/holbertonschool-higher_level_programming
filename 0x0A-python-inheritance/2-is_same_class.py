#!/usr/bin/python3
"""
is_same_class
determines if objects is exact instance of specified class

"""


def is_same_class(obj, a_class):
    """
    Returns True if exact instance, otherwise False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
