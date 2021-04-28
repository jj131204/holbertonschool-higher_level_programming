#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    j = len(argv) - 1
    u = len(argv)
    if j == 1:
        print("{} arguments.".format(j))

    else:
        if j == 2:
            print("{} argument:".format(j))
        else:
            print("{} arguments:".format(j))

        for i in range(1, u):
                print("{}: {} ".format(i, argv[i]))
