#!/usr/bin/python3
"""function that prints a square with the character #."""


def print_square(size):
    """function that prints a square with the character #."""
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print("")
    else:
        raise TypeError("size must be an integer")
