#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            conv = ord(c)
            c = chr(conv - 32)
        print("{}".format(c), end="")
    print()
