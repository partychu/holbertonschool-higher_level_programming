#!/usr/bin/python3
"""
inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited directly or indirectly from specified class
    """
    return issubclass(type(obj), a_class)
