#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Searches for peak in list"""
    length = len(list_of_integers)
    peak = 0
    if length == 0:
        return None
    if length == 1:
        return
    if length == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    for i in range(1, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            peak = list_of_integers[i]
            return peak
