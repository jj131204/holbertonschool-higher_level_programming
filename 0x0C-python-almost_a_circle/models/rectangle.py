#!/usr/bin/python3
"""  Write the class Rectangle that inherits from Base: """

from models.base import Base


class Rectangle(Base):
    """class Rectangle (Base)"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ def __init__(self, width, height, x=0, y=0, id=None) """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width attribute."""

        return self.__width

    @property
    def height(self):
        """height attribute."""

        return self.__height

    @property
    def x(self):
        """x attribute."""

        return self.__x

    @property
    def y(self):
        """y attribute."""

        return self.__y

    @width.setter
    def width(self, value):
        """ def width(self, value): """
        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ def height(self, value):"""
        if type(value) != int:
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must be > 0")

        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """ def x(self, value):"""
        if type(value) != int:
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """ def y(self, value): """
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    def area(self):
        """calculates the area"""
        area_ = self.__height * self.__width
        return area_

    def display(self):
        """ display"""

        for a in range(self.__y):
            print()

        for i in range(self.__height):

            for b in range(self.__x):
                print(" ", end="")

            for j in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        """method so that it returns [Rectangle] (<id>) <x>/<y>
         - <width>/<height>"""
        str_ = "[Rectangle] ({}) {}/{} - {}/{}" .format(
            self.id, self.__x, self.__y, self.__width, self.__height)

        return str_
