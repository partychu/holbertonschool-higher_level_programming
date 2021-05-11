#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    holder = 0
    for i in range(len(my_list)):
        if holder < my_list[i]:
            holder = my_list[i]
    return holder
