#!/usr/bin/python3
"""
Lookup
Returns list of available attributes & methods
of an object
Returns a list obj
"""


def lookup(obj):
    """
    Looks up object
    """
    a = list(dir(obj))
    return a
