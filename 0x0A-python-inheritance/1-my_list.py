#!/usr/bin/python3
"""
Class MyList
public method: print_sorted
prints list in ascending sort
"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
