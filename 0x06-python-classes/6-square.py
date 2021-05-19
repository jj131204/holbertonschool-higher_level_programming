#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Square"""

    def __init__(self, size=0, position=(0, 0)):

        """if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:"""
        self.__size = size
        self.__position = position

    def area(self):
        _area = self.__size ** 2
        return _area

    @property
    def size(self):

        """ Retrieve the property value """
        return self.__size
    """point6"""

    @property
    def position(self):
        """ Retrieve the property value """
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """point6"""
    @position.setter
    def position(self, value):

        """Setting a new value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):

        """ Prints in stdout the square with the character '#' """

        if self.size != 0:
            for first in range(self.size):
                for second in range(self.size):
                    print("#", end="")
                print()

        else:
            print()
