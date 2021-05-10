#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)

    if argc is 1:
        print("0 arguments.")
    if argc is 2:
        print("1 argument:")
    if argc > 2:
        print("{:d} arguements:".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
