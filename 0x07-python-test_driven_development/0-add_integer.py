#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """Given 2 variables, return the addition them"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b
