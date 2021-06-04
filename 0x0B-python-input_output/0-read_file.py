#!/usr/bin/python
def read_file(filename=""):
    with open(filename, encoding='UTF8') as f:
        for line in f:
            print(line, end="")
