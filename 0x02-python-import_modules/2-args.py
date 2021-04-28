#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    j = len(argv)

    if j is 1:
        print("0 arguments.".format(j))

    else:
        print("{} arguments.".format(j))
    for i in range(1, j):

        if j > 1:
            print("{} :{} ".format(i, argv[i]))
