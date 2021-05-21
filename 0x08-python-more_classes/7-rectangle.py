#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:

    """Rectangle"""

    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    """point3"""
    def __str__(self):

        j = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    j += str(self.print_symbol)
                if h != self.__height - 1:
                    j += "\n"
        return j
    """end point3"""

    """point4"""

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)

        test = "Rectangle({}, {})".format(self.__width, self.__height)
        return eval(repr("{}".format(test)))

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
        if self.height == 0 or self.width == 0:
            return 0
        else:
            _perimeter = (self.__width * 2) + (self.__height * 2)
        return _perimeter

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
