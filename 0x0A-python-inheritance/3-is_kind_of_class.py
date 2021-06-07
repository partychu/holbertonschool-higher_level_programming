#!/usr/bin/python3
"""
is_kind_of_class
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True is obj is an instance or an instance
    of an inherited class, of specificed class.
    Otherwise False.
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
