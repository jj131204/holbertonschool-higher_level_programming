#!/usr/bin/python3
import sys

if __name__ == "__main__":

    j = len(sys.argv)

    if j is 1:
        print("0 arguments.".format(j))

    else:
        print("{} arguments.".format(j))
    for i in range(2, j):

        if j > 1:
            print("{} :{} ".format(i, sys.argv[i]))
