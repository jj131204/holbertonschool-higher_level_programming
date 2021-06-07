#!/usr/bin/python3
"""

"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle(Base)"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ def __init__(self, width, height, x=0, y=0, id=None): """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

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
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")

        elif value < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    """ point 4 """
    def area(self):
        """area"""
        area_ = self.__height * self.__width
        return area_

    def display(self):
        """ display"""

        for i in range(self.__height):

            for j in range(self.__width):
                print("#", end="")

            print()
