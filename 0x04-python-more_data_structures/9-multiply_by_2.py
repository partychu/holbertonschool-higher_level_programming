#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    aux = {}
    for v in a_dictionary:
        aux[v] = a_dictionary[v] * 2
    return aux
