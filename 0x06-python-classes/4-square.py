#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Square"""

    def __init__(self, size=0):

        """if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:"""
        self.__size = size

    def area(self):
        _area = self.__size ** 2
        return _area

    @property
    def size(self):

        """ Retrieve the property value """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
