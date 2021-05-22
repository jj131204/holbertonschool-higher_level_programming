#!/usr/bin/python3
"""advanced point  (N queens)"""

from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit (1)

    if argv[1].isdigit is False:
        print("N must be a number")
        exit (1)
    else:
        if int(argv[1]) < 4:
            print("N must be at least 4")
            exit(1)

    """all cases possibles"""

