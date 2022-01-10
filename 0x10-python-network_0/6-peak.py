#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Searches for peak in list"""
    p_list = []
    if list_of_integers is None:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers
    if length == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    for i in range(1, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            p_list.append(list_of_integers[i])
    return p_list
