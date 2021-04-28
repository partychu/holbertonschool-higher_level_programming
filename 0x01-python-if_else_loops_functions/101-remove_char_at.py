#!/usr/bin/python3
def remove_char_at(str, n):
    mod = ""
    for i in range(len(str)):
        if i != n:
            mod += str[i]
    return mod
