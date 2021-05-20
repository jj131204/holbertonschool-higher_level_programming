#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__height = value
    """point2"""

    def area(self):
        _area = self.__width * self.__height
        return _area

    def perimeter(self):
        _perimeter = (self.__width * 2) + (self.__height * 2)
        return _perimeter
