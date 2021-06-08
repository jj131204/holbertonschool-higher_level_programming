#!/usr/bin/python3
"""class square """

from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size
        super().__init__(size, size,  x,  y,  id)

    def __str__(self):
        """str_ = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

        return str_"""

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return s
