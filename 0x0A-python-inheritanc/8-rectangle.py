#!/usr/bin/python3
"""Write an empty class BaseGeometry."""

BaseGeometry =  __import__('7-base_geometry').BaseGeometry

"""class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name, "must be an integer")
        if value <= 0:
            raise ValueError(name, "must be greater than 0")
"""

class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """ def __init__(self, width, height):"""
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
