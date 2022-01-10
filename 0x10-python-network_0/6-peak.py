#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Searches for peak in list"""
    n = len(list_of_integers)
    li = list_of_integers
    peak = 0
    if n == 0:
        return None
    if n == 1:
        return
    if li[0] >= li[1]:
        return li[0]
    elif li[n - 1] >= li[n - 2]:
        return li[n - 1]
    for i in range(1, n - 1):
        if li[i] >= li[i - 1] and li[i] >= li[i + 1]:
            return li[i]
