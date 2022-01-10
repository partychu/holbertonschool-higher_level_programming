#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Searches for peak in list"""
    length = len(list_of_integers)
    li = list_of_integers
    peak = 0
    if length == 0:
        return None
    if length == 1:
        return
    if length == 2:
        if li[0] >= li[1]:
            return li[0]
        else:
            return li[1]
    for i in range(1, length - 1):
        if li[i] >= li[i - 1] and li[i] >= li[i + 1]:
            return li[i]
