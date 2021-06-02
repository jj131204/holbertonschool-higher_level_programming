#!/usr/bin/python3
"""Write an empty class BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """ def __init__(self, width, height):"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
